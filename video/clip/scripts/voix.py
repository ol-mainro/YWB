#!/usr/bin/env python3
"""Voix off en blocs indépendants (un bloc = une scène, ou une partie de scène).

Fichiers :
  assets/voix/blocs.json      texte et réglages de chaque bloc (à éditer)
  assets/voix/<id>.mp3        audio du bloc
  assets/voix/<id>.mots.json  minutage mot par mot, en secondes depuis le début de SA scène
  assets/voix-off-mots.json   minutage global (temps absolus), régénéré à chaque fois

Commandes (depuis video/clip/) :
  python3 scripts/voix.py statut              blocs à jour / modifiés
  python3 scripts/voix.py generer [--essai]   régénère via ElevenLabs les seuls blocs modifiés
  python3 scripts/voix.py generer s4 s5       force la régénération de ces blocs
  python3 scripts/voix.py appliquer           réécrit index.html + minutage global, sans génération
  python3 scripts/voix.py exporter            piste voix complète -> renders/voix-off.wav
  python3 scripts/voix.py importer <mp3> <mots.json>
                                              découpe une prise complète en blocs (une fois)

Quand un bloc régénéré change de durée (écart D), la scène qui le porte s'allonge de D
et toutes les scènes suivantes se décalent de D : leurs animations restent calées.
Seules les animations de la scène régénérée sont à recaler (voir <id>.mots.json).
"""
import base64, hashlib, json, os, re, shutil, subprocess, sys, tempfile, time, urllib.error, urllib.request
from pathlib import Path

CLIP = Path(__file__).resolve().parent.parent
VOIX = CLIP / "assets" / "voix"
BLOCS = VOIX / "blocs.json"
INDEX = CLIP / "index.html"
MOTS_GLOBAL = CLIP / "assets" / "voix-off-mots.json"
DEBUT, FIN = "<!-- voix:debut (généré par scripts/voix.py) -->", "<!-- voix:fin -->"
SILENCE_DB = -45  # seuil de silence pour repérer la parole


# ---------- utilitaires ----------

def run(*cmd):
    return subprocess.run(cmd, check=True, capture_output=True, text=True)

def duree(f):
    return float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(f)).stdout)

def silences(f, d=0.05):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-af",
                          f"silencedetect=n={SILENCE_DB}dB:d={d}", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", err)]
    en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", err)]
    total = duree(f)
    en += [total] * (len(st) - len(en))
    return list(zip(st, en)), total

def bornes_parole(f):
    """(début, fin) de la parole dans le fichier."""
    sil, total = silences(f)
    a, b = 0.0, total
    if sil and sil[0][0] <= 0.01:
        a = sil[0][1]
    if sil and sil[-1][1] >= total - 0.01:
        b = sil[-1][0]
    return a, b

def lufs(f):
    err = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(f), "-af", "ebur128", "-f", "null", "-"],
                         capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", err)[-1])

def r3(x):
    return round(x + 0.0, 3)

def fmt(x):
    """Nombre pour un attribut HTML : 0, 6.6, 47.489."""
    return f"{x:.3f}".rstrip("0").rstrip(".") or "0"

def charger():
    return json.loads(BLOCS.read_text())

def sauver(cfg):
    BLOCS.write_text(json.dumps(cfg, ensure_ascii=False, indent=2) + "\n")

def reglages(cfg, b):
    """Réglages effectifs d'un bloc : valeurs par défaut + surcharges du bloc."""
    r = dict(cfg["defaut"])
    r.update({k: b[k] for k in ("voix", "modele", "vitesse", "voice_settings", "seed", "lufs") if k in b})
    return r

def empreinte(cfg, b):
    r = reglages(cfg, b)
    cle = {"texte": b["texte"], **{k: r.get(k) for k in ("voix", "modele", "vitesse", "voice_settings", "seed")}}
    return hashlib.sha1(json.dumps(cle, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:12]


# ---------- index.html ----------

SCENE_RE = re.compile(r'<div\b[^>]*?\sid="([^"]+)"[^>]*?data-composition-src="[^"]+"[^>]*>', re.S)

def lire_scenes(html):
    scenes = {}
    for m in SCENE_RE.finditer(html):
        tag = m.group(0)
        scenes[m.group(1)] = {
            "start": float(re.search(r'data-start="([\d.]+)"', tag).group(1)),
            "duration": float(re.search(r'data-duration="([\d.]+)"', tag).group(1)),
        }
    return dict(sorted(scenes.items(), key=lambda kv: kv[1]["start"]))

def ecrire_scenes(html, scenes):
    def maj(m):
        sid = m.group(1)
        if sid not in scenes:
            return m.group(0)
        tag = re.sub(r'data-start="[\d.]+"', f'data-start="{fmt(scenes[sid]["start"])}"', m.group(0))
        return re.sub(r'data-duration="[\d.]+"', f'data-duration="{fmt(scenes[sid]["duration"])}"', tag)
    return SCENE_RE.sub(maj, html)

def decaler(scenes, ancre, delta):
    """Allonge la scène `ancre` de delta et décale les scènes suivantes."""
    fin = scenes[ancre]["start"] + scenes[ancre]["duration"]
    for sid, s in scenes.items():
        if sid != ancre and s["start"] >= fin - 1e-3:
            s["start"] += delta
    scenes[ancre]["duration"] += delta

def ecrire_index(cfg, scenes):
    html = INDEX.read_text()
    html = ecrire_scenes(html, scenes)

    # garder les data-hf-id posés par le studio
    hf = {i: h for h, i in re.findall(r'<audio[^>]*?data-hf-id="([^"]+)"[^>]*?\sid="([^"]+)"', html)}
    piste = cfg["defaut"].get("piste", 2)
    lignes = []
    for b in cfg["blocs"]:
        debut = scenes[b["scene"]]["start"] + b["decalage"]
        h = hf.get(f"voix-{b['id']}")
        attr_hf = f' data-hf-id="{h}"' if h else ""
        lignes.append(
            f'      <audio{attr_hf} id="voix-{b["id"]}" class="clip" src="assets/voix/{b["id"]}.mp3"'
            f' data-start="{fmt(debut)}" data-duration="{fmt(b["duree"])}"'
            f' data-track-index="{piste}" data-volume="1"></audio>')
    bloc = "      " + DEBUT + "\n" + "\n".join(lignes) + "\n      " + FIN

    if DEBUT in html:
        html = re.sub(re.escape(DEBUT) + r".*?" + re.escape(FIN), lambda _: bloc.strip(), html, flags=re.S)
    else:  # première fois : remplace l'ancienne piste unique
        html, n = re.subn(r'[ \t]*<audio\b[^>]*\bid="voix-off"[^>]*>\s*</audio>', lambda _: bloc, html, flags=re.S)
        if not n:
            html = html.replace('\n    </div>\n    <script>', "\n" + bloc + '\n    </div>\n    <script>', 1)

    # durée totale = fin de la dernière scène ou du dernier bloc
    fin = max([s["start"] + s["duration"] for s in scenes.values()] +
              [scenes[b["scene"]]["start"] + b["decalage"] + b["duree"] for b in cfg["blocs"]])
    html = re.sub(r'(id="root"[^>]*?data-duration=")[\d.]+"', lambda m: f'{m.group(1)}{fmt(fin)}"', html, count=1, flags=re.S)
    INDEX.write_text(html)
    return fin

def ecrire_mots(cfg, scenes):
    tous = []
    for b in cfg["blocs"]:
        mots = json.loads((VOIX / f"{b['id']}.mots.json").read_text())
        s0 = scenes[b["scene"]]["start"]
        tous += [{"w": m["w"], "start": r3(m["start"] + s0), "end": r3(m["end"] + s0)} for m in mots]
    MOTS_GLOBAL.write_text(json.dumps(tous, ensure_ascii=False, indent=1) + "\n")

def appliquer(cfg, scenes=None):
    scenes = scenes or lire_scenes(INDEX.read_text())
    fin = ecrire_index(cfg, scenes)
    ecrire_mots(cfg, scenes)
    print(f"index.html et voix-off-mots.json à jour — durée totale {fin:.3f} s")


# ---------- ElevenLabs ----------

def cle_api():
    if os.environ.get("ELEVENLABS_API_KEY"):
        return os.environ["ELEVENLABS_API_KEY"]
    env = CLIP / ".env"
    if env.exists():
        for l in env.read_text().splitlines():
            if l.startswith("ELEVENLABS_API_KEY="):
                return l.split("=", 1)[1].strip().strip('"\'')
    sys.exit("ELEVENLABS_API_KEY introuvable (variable d'environnement ou video/clip/.env)")

def tts(cfg, i):
    b, r = cfg["blocs"][i], reglages(cfg, cfg["blocs"][i])
    corps = {"text": b["texte"], "model_id": r["modele"]}
    if i > 0:
        corps["previous_text"] = cfg["blocs"][i - 1]["texte"]
    if i + 1 < len(cfg["blocs"]):
        corps["next_text"] = cfg["blocs"][i + 1]["texte"]
    if r.get("voice_settings"):
        corps["voice_settings"] = r["voice_settings"]
    if r.get("seed") is not None:
        corps["seed"] = r["seed"]
    req = urllib.request.Request(
        f"https://api.elevenlabs.io/v1/text-to-speech/{r['voix']}/with-timestamps?output_format=mp3_44100_192",
        data=json.dumps(corps).encode(), method="POST",
        headers={"xi-api-key": cle_api(), "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as rep:
            d = json.load(rep)
    except urllib.error.HTTPError as e:
        sys.exit(f"ElevenLabs a refusé le bloc {b['id']} ({e.code}) : {e.read().decode()[:400]}")
    a = d["alignment"]
    mots, cur, s = [], "", 0.0
    for c, t0, t1 in zip(a["characters"], a["character_start_times_seconds"], a["character_end_times_seconds"]):
        if c.isspace():
            if cur:
                mots.append({"w": cur, "start": s, "end": e})
                cur = ""
        else:
            if not cur:
                s = t0
            cur, e = cur + c, t1
    if cur:
        mots.append({"w": cur, "start": s, "end": e})
    return base64.b64decode(d["audio_base64"]), mots

def traiter(cfg, b, brut, mots, tmp):
    """Accélère, normalise le volume, cale la parole sur les marges du bloc. Renvoie (durée, mots)."""
    r = reglages(cfg, b)
    v = float(r.get("vitesse", 1.0))
    src = tmp / "brut.mp3"
    src.write_bytes(brut)
    acc = tmp / "acc.wav"
    run("ffmpeg", "-v", "error", "-y", "-i", str(src), "-af", f"atempo={v}", "-ar", "44100", "-ac", "1", str(acc))
    gain = float(r["lufs"]) - lufs(acc)
    a, z = bornes_parole(acc)
    marge_av, marge_ap = b["marges"]
    out = tmp / "final.mp3"
    run("ffmpeg", "-v", "error", "-y", "-i", str(acc), "-af",
        f"atrim={a}:{z},asetpts=N/SR/TB,volume={gain:.2f}dB,afade=t=in:d=0.01,"
        f"afade=t=out:st={max(0, z - a - 0.02):.3f}:d=0.02,"
        f"adelay={int(marge_av * 1000)}:all=1,apad=pad_dur={marge_ap}",
        "-ar", "44100", "-ac", "1", "-b:a", "192k", str(out))
    nouv = duree(out)
    mots = [{"w": m["w"], "start": m["start"] / v - a + marge_av, "end": m["end"] / v - a + marge_av} for m in mots]
    return out, nouv, mots


# ---------- commandes ----------

def cmd_statut(cfg):
    for b in cfg["blocs"]:
        etat = "à jour" if b.get("empreinte") == empreinte(cfg, b) else "MODIFIÉ"
        print(f"{b['id']:>5}  {etat:8}  {b['duree']:6.2f} s  scène {b['scene']:<4} « {b['texte'][:60]}… »")

def cmd_generer(cfg, ids, essai):
    scenes = lire_scenes(INDEX.read_text())
    cibles = [i for i, b in enumerate(cfg["blocs"])
              if (b["id"] in ids if ids else b.get("empreinte") != empreinte(cfg, b))]
    if not cibles:
        print("Rien à régénérer : tous les blocs sont à jour.")
        return
    print("À régénérer : " + ", ".join(cfg["blocs"][i]["id"] for i in cibles))
    if essai:
        return
    archives = VOIX / "archives"
    archives.mkdir(exist_ok=True)
    for i in cibles:
        b = cfg["blocs"][i]
        print(f"→ {b['id']} : génération…", flush=True)
        brut, mots = tts(cfg, i)
        with tempfile.TemporaryDirectory() as t:
            out, nouv, mots = traiter(cfg, b, brut, mots, Path(t))
            stamp = time.strftime("%Y%m%d-%H%M%S")
            for ext in ("mp3", "mots.json"):
                f = VOIX / f"{b['id']}.{ext}"
                if f.exists():
                    shutil.copy(f, archives / f"{b['id']}-{stamp}.{ext}")
            shutil.copy(out, VOIX / f"{b['id']}.mp3")
        delta = nouv - b["duree"]
        # décalage des blocs suivants de la même scène, puis des scènes suivantes
        for b2 in cfg["blocs"][i + 1:]:
            if b2["scene"] == b["scene"]:
                b2["decalage"] = r3(b2["decalage"] + delta)
        decaler(scenes, b["scene"], delta)
        b["duree"], b["empreinte"] = r3(nouv), empreinte(cfg, b)
        rel = [{"w": m["w"], "start": r3(m["start"] + b["decalage"]), "end": r3(m["end"] + b["decalage"])} for m in mots]
        (VOIX / f"{b['id']}.mots.json").write_text(json.dumps(rel, ensure_ascii=False, indent=1) + "\n")
        sauver(cfg)
        print(f"  durée {nouv:.2f} s (écart {delta:+.2f} s) — scène {b['scene']} : "
              f"{scenes[b['scene']]['duration']:.3f} s. Mots (temps dans la scène) :")
        print("  " + " ".join(f"{m['w']}@{m['start']:.2f}" for m in rel))
    appliquer(cfg, scenes)
    print("Ancienne version conservée dans assets/voix/archives/. Recaler les animations des scènes régénérées.")

def cmd_exporter(cfg):
    scenes = lire_scenes(INDEX.read_text())
    out = CLIP / "renders" / "voix-off.wav"
    args, filtres = [], []
    for k, b in enumerate(cfg["blocs"]):
        args += ["-i", str(VOIX / f"{b['id']}.mp3")]
        ms = int(round((scenes[b["scene"]]["start"] + b["decalage"]) * 1000))
        filtres.append(f"[{k}:a]adelay={ms}:all=1[a{k}]")
    mix = "".join(f"[a{k}]" for k in range(len(cfg["blocs"])))
    filtres.append(f"{mix}amix=inputs={len(cfg['blocs'])}:normalize=0[o]")
    run("ffmpeg", "-v", "error", "-y", *args, "-filter_complex", ";".join(filtres), "-map", "[o]",
        "-ar", "48000", "-ac", "1", str(out))
    print(f"{out.relative_to(CLIP)} ({duree(out):.2f} s)")

def cmd_importer(cfg, mp3, mots_json):
    """Découpe une prise complète en un bloc par scène, au milieu du silence le plus proche."""
    html = INDEX.read_text()
    scenes = lire_scenes(html)
    mots = json.loads(Path(mots_json).read_text())
    sil, total = silences(mp3, d=0.25)
    ids = list(scenes)
    coupes = [0.0]
    for sid in ids[1:]:
        t = scenes[sid]["start"]
        a, z = min(sil, key=lambda s: 0 if s[0] <= t <= s[1] else min(abs(s[0] - t), abs(s[1] - t)))
        coupes.append((a + z) / 2)
    coupes.append(total)
    VOIX.mkdir(parents=True, exist_ok=True)
    blocs = []
    for k, sid in enumerate(ids):
        c0, c1 = coupes[k], coupes[k + 1]
        part = VOIX / f"{sid}.mp3"
        run("ffmpeg", "-v", "error", "-y", "-i", str(mp3), "-af",
            f"atrim={c0}:{c1},asetpts=N/SR/TB", "-ar", "44100", "-ac", "1", "-b:a", "192k", str(part))
        a, z = bornes_parole(part)
        d = duree(part)
        dec = c0 - scenes[sid]["start"]
        sel = [m for m in mots if c0 <= m["start"] < c1]
        rel = [{"w": m["w"], "start": r3(m["start"] - scenes[sid]["start"]),
                "end": r3(m["end"] - scenes[sid]["start"])} for m in sel]
        (VOIX / f"{sid}.mots.json").write_text(json.dumps(rel, ensure_ascii=False, indent=1) + "\n")
        blocs.append({"id": sid, "scene": sid, "texte": " ".join(m["w"] for m in sel),
                      "decalage": r3(dec), "duree": r3(d), "marges": [r3(a), r3(d - z)]})
        print(f"{sid:>4}  {c0:6.2f} → {c1:6.2f} s  « {blocs[-1]['texte'][:50]}… »")
    cfg["blocs"] = blocs
    for b in blocs:
        b["empreinte"] = empreinte(cfg, b)
    sauver(cfg)
    appliquer(cfg, scenes)


def main():
    args = sys.argv[1:]
    if not args or args[0] not in ("statut", "generer", "appliquer", "exporter", "importer"):
        sys.exit(__doc__)
    cmd, reste = args[0], args[1:]
    cfg = charger()
    if cmd == "statut":
        cmd_statut(cfg)
    elif cmd == "generer":
        cmd_generer(cfg, [a for a in reste if not a.startswith("--")], "--essai" in reste)
    elif cmd == "appliquer":
        appliquer(cfg)
    elif cmd == "exporter":
        cmd_exporter(cfg)
    elif cmd == "importer":
        cmd_importer(cfg, *reste)

if __name__ == "__main__":
    main()
