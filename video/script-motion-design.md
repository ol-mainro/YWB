# Yoga With Balls — Script motion design

> Document de travail itératif. Le script est dicté par Romain, puis structuré scène par scène pour une production en motion design avec **Hyperframes** (compositions HTML + animations), générées avec Opus 5.5.

- **Version :** v0.8 — images incrustées dans les scènes 1, 6, 7 et 8
- **Statut :** 8 scènes rendues (MP4 + version titres sur fond transparent), en attente de retours. Durée passée à 66,4 s avec la nouvelle phrase (voir questions ouvertes)

---

## 1. Brief

| Élément | Valeur |
|---|---|
| Objectif | Renverser le dogme du « toujours plus » et faire connaître l'application Yoga With Balls |
| Public cible | Hommes de 40 ans et plus |
| Format | **9:16 vertical** — 1080 × 1920 px (Reels, TikTok, Shorts) |
| Durée | **66,4 s** (cible initiale 60 s) |
| Parti pris visuel | **Clip 100 % typographique** : titres et symboles uniquement, aucune image (incrustations ajoutées ensuite par Romain) |
| Voix off | **Voix de synthèse** — idéalement grave, homme mûr, posée, assurée (voir 5 ter) |
| Musique / ambiance | Pas de piste choisie. Animation calée sur une grille de 120 BPM ; musique ajoutée au montage. Intention : montée rythmique (acte 1), coupure nette (acte 2), nappe ample et triomphante (acte 3) |
| Signature | **En faire moins. En avoir plus.** ✅ |
| Appel à l'action | Mention « Application disponible » — **sans lien ni store** pour l'instant |

## 2. Direction artistique

### Palette (charte du site)

| Rôle | Couleur |
|---|---|
| Vert profond (fond principal) | `#0f3d2e` / `#0a2a20` |
| Or (accents, mots-clés, symboles) | `#d4af37` |
| Crème (texte courant, fonds clairs de l'acte 1) | `#faf6ec` / `#e8e4d5` |
| Rouge (saturation, alerte « toujours plus ») | `#a4321f` |
| Gris olive (texte secondaire) | `#6b6b5a` |

**Logique couleur par acte :**
- **Acte 1 — Le dogme :** fond crème, texte noir/rouge. Ambiance salle de sport, pression, saturation.
- **Acte 2 — La rupture :** bascule sur le vert profond, silence visuel, l'or apparaît.
- **Acte 3 — La méthode :** vert profond + or dominant. Ambiance laboratoire premium.

### Typographie

- Une police **variable** sans-serif (ex. Inter, Archivo ou Barlow, à embarquer en local dans le projet Hyperframes).
- Atout clé : l'**animation de la graisse** (*font-weight*). Les mots « s'épaississent » comme des muscles qui gonflent. C'est le fil rouge visuel du clip.
- Titres en capitales, très gros (120–260 px), une idée par écran.

### Bibliothèque de symboles (SVG simples, dessinés en code)

| Symbole | Usage |
|---|---|
| `+` | le dogme du « toujours plus » |
| `−` | le renversement « en faire moins » |
| `=` `→` | équations et flux |
| Courbes / flèches ↑ ↓ | graphique efforts vs muscle |
| Cadenas | « craquer le code du corps humain » |
| Empreintes de pas | marche tai-chi |
| Goutte | pleurs sacrés |
| Cercle / onde | performance spirituelle |

### Zones de sécurité 9:16

- Garder **tous les textes entre 168 px et 1330 px de haut** (norme Hyperframes pour TikTok/Reels) : au-dessus, la barre d'état ; en dessous, légende, pseudo et boutons. Sous 1330 px : décor uniquement.
- Marges latérales : 80 px minimum.

## 3. Script

### Script dicté (texte brut, référence)

Nous aimerions expliquer que depuis que nous sommes jeunes et dans cette société, on explique que pour être fort et avoir l'air fort, il faut en faire beaucoup. Et il faut en faire toujours plus. Que pour avoir de la masse, pour avoir du muscle, il faut faire beaucoup d'efforts. Toujours plus d'efforts. Toujours plus de performance. Or, l'âge avançant, on nous explique aussi que notre corps a besoin qu'on en fasse toujours plus pour en avoir autant. Et l'âge avance toujours plus et on nous incite à faire toujours plus pour avoir plus ou autant. Nous, chez Yoga with Balls et notre équipe, on a besoin, on a voulu disrupter, on a voulu changer de state of mind et on s'est dit, et si pour en avoir plus, il fallait plutôt en faire moins. On a déplacé le truc, on a craqué le fonctionnement du corps humain et on s'est aperçu que passé 40 ans, on avait plus avantage à en faire moins qu'à en faire plus. Que c'est en accent sur la performance spirituelle qu'on obtenait des performances physiques et des gains musculaires extraordinaires. Alors, on invite tout le monde à essayer sans attendre et à télécharger l'application Yoga with Balls.

### Voix off (v3, ~170 mots ≈ 64 s)

> **[Acte 1 — Le dogme]**
> Depuis l'enfance, on nous répète la même chose.
> Pour être fort, il faut en faire beaucoup.
> Pour prendre de la masse, il faut des efforts. Toujours plus d'efforts. Toujours plus de performance.
>
> Puis les années passent. Et le corps en demande encore plus… juste pour garder ce qu'il a.
> L'âge augmente. On augmente les efforts. Pour toujours moins d'effets.
>
> **[Acte 2 — La rupture]**
> Pourtant, le corps des plus de 40 ans ne fonctionne plus comme à 20. En vrai, c'est exactement l'inverse.
> Chez Yoga With Balls, nous avons changé de *mindset*.
> Et si, pour en avoir plus… il fallait en faire moins ?
>
> Nous avons craqué le code du corps humain.
> Passé 40 ans, en faire moins rapporte plus.
>
> **[Acte 3 — La méthode]**
> Deux piliers. La marche tai-chi. Les pleurs sacrés.
> La performance spirituelle déclenche la performance physique.
> Et des gains musculaires extraordinaires.
>
> Yoga With Balls.
> En faire moins. En avoir plus.
> L'application est disponible.

## 4. Découpage en scènes

8 scènes = 9 compositions Hyperframes (la scène 4 en compte deux : `s4a-inverse` et `s4-et-si`). Structure : le dogme → la rupture → la méthode.

| # | Timecode | Voix off (extrait) | Texte à l'écran | Symboles / animation | Transition |
|---|---|---|---|---|---|
| 1 | 00:00 – 00:06 | « Depuis l'enfance… en faire beaucoup. » | **POUR ÊTRE FORT** | Graisse du texte qui passe de fin à extra-gras | Cut sec |
| 2 | 00:06 – 00:15 | « Toujours plus d'efforts. Toujours plus de performance. » | **PLUS** ×∞ | Les `+` se multiplient jusqu'à saturer l'écran, passage au rouge | Saturation → écran plein rouge |
| 3 | 00:15 – 00:24 | « Puis les années passent… Pour toujours moins d'effets. » | **20 · 30 · 40 · 50** | Graphique en ciseaux : courbe EFFORTS ↑, courbe MUSCLE ↓ | Glitch |
| 4 | 00:24 – 00:39 | « Pourtant, le corps des plus de 40 ans… exactement l'inverse. …mindset. Et si… en faire moins ? » | **40 ≠ 20** · **L'INVERSE.** · **ET SI… ?** → **−** | Tout s'arrête, fond vert, le `+` perd sa barre verticale et devient `−` | Silence, respiration |
| 5 | 00:39 – 00:46 | « Craqué le code… en faire moins rapporte plus. » | **40+** · **MOINS = PLUS** | Cadenas doré qui s'ouvre, les courbes s'inversent | Zoom dans le cadenas |
| 6 | 00:46 – 00:50 | « Deux piliers. La marche tai-chi. Les pleurs sacrés. » | **MARCHE TAI-CHI** / **PLEURS SACRÉS** | Empreintes de pas lentes + goutte dorée qui tombe | Onde partant de la goutte |
| 7 | 00:50 – 00:56 | « La performance spirituelle… gains musculaires extraordinaires. » | **SPIRITUEL → PHYSIQUE** · **MUSCLE** | Le mot MUSCLE gonfle (graisse + échelle) à chaque pulsation | Flash or |
| 8 | 00:56 – 01:06 | « Yoga With Balls. En faire moins. En avoir plus. L'application est disponible. » | **YOGA WITH BALLS** · signature · « Application disponible » | Logo typographique qui se pose, signature mot par mot | Fondu au vert |

### Détail des scènes

#### Scène 1 — Le dogme (00:00 – 00:06)
- **Fond :** crème `#faf6ec`.
- **Texte :** « POUR ÊTRE FORT » au centre, noir.
- **Animation :** apparition mot par mot sur la voix. La graisse passe de 100 à 900 sur « FORT ».
- **Son :** pulsation sourde, comme un battement.

#### Scène 2 — Toujours plus (00:06 – 00:15)
- **Texte :** « TOUJOURS PLUS D'EFFORTS » puis « TOUJOURS PLUS DE PERFORMANCE ».
- **Symboles :** des `+` apparaissent en rythme, de plus en plus vite, jusqu'à couvrir tout l'écran. Leur couleur vire du noir au rouge `#a4321f`.
- **Animation :** léger tremblement de caméra qui s'accentue.
- **Son :** rythme qui accélère, bruit de compteur.

#### Scène 3 — L'âge (00:15 – 00:24)
- **Texte :** compteur d'âge 20 → 30 → 40 → 50 en haut. En bas : « PLUS D'ÂGE. PLUS D'EFFORTS. POUR MOINS D'EFFETS. »
- **Symboles :** graphique minimaliste à deux courbes. EFFORTS (rouge) monte, MUSCLE (gris) stagne puis baisse.
- **Animation :** le tracé des courbes suit le compteur d'âge.
- **Transition :** glitch vers le noir.

#### Scène 4 — L'inverse, et si ? (00:24 – 00:39)
- **Fond :** bascule sur le vert profond `#0f3d2e`.
- **Texte :** « 40 ANS ≠ 20 ANS » (le `≠` en or), puis « EXACTEMENT L'INVERSE. » qui se retourne à 180°. Ensuite « MINDSET. » en or, puis « ET SI… ? » en grand, crème.
- **Symbole :** un grand `+` doré au centre. Sa barre verticale s'efface : il devient `−`.
- **Son :** coupure musicale, une seule note tenue.

#### Scène 5 — Le code craqué (00:39 – 00:46)
- **Symbole :** cadenas doré avec un compteur « 40+ ». Il s'ouvre.
- **Texte :** « MOINS = PLUS », le `=` en or.
- **Animation :** les courbes de la scène 3 reviennent et s'inversent. EFFORTS ↓, MUSCLE ↑.

#### Scène 6 — Les deux piliers (00:46 – 00:50)
- **Écran partagé vertical :**
  - en haut, « MARCHE TAI-CHI » avec des empreintes de pas qui avancent lentement ;
  - en bas, « PLEURS SACRÉS » avec une goutte dorée qui tombe.
- **Animation :** l'impact de la goutte crée une onde concentrique qui sert de transition.

#### Scène 7 — La transformation (00:50 – 00:56)
- **Texte :** « PERFORMANCE SPIRITUELLE → PERFORMANCE PHYSIQUE ». La flèche dorée se trace.
- **Puis :** le mot « MUSCLE » plein écran. Il gonfle à chaque pulsation (graisse + échelle), avec des particules dorées.
- **Texte final :** « GAINS EXTRAORDINAIRES ».
- **Son :** montée triomphale.

#### Scène 8 — Signature (00:56 – 01:06)
- **Texte :** « YOGA WITH BALLS » (logo typographique or), puis « EN FAIRE MOINS. EN AVOIR PLUS. » mot par mot.
- **Mention :** « Application disponible » en petit, crème, sous la signature.
- **Fin :** tenue 2 s, puis fondu au vert.

## 5. Notes de production Hyperframes

- **Résolution :** 1080 × 1920, 30 fps, 66,4 s.
- **Structure :** une composition par scène (9 fichiers pour 8 scènes), assemblées dans une composition maître.
- **Assets :** une police variable embarquée en local, symboles en SVG dessinés en code, 5 images (`assets/images/`, JPEG 1800 px tirés de `images-sources/`).
- **Voix off :** idéalement enregistrée avant l'animation, pour caler les apparitions de texte sur les mots.
- **Incrustations :** images posées directement dans le clip ✅ :
  - scène 1 (« Depuis l'enfance… beaucoup ») → `formule-ancestrale` ; elle s'assombrit quand le `+` rouge s'imprime dessus ;
  - scène 6 → `danse-mystique` sur « Marche tai-chi », puis `homme-qui-pleure` sur « Pleurs sacrés » (la goutte tombe dessus) ;
  - scène 7 → `homme-qui-pleure` continue sur « Performance spirituelle », `testosterone-booster` surgit sur « physique » et gonfle avec « musculaires » ;
  - scène 8 → `logo` à la place du logo typographique, il se pose sur « Yoga » et rebondit sur « With » et « Balls ».
- **Exports :**
  - `final.mp4` — version complète, fond vert, voix off incluse ;
  - `titres-alpha.mov` — titres et symboles seuls sur **fond transparent** (ProRes 4444, `--format mov`), sans voix, pour superposition au montage ✅ ;
  - `voix-off.wav` — piste voix séparée.

### Faut-il prévoir les images dès maintenant ?

Recommandation : **pas les images, mais leur place**.

- Les scènes 1, 6 et 7 sont celles où une image incrustée aurait le plus de sens (silhouette, marche, corps).
- Dans ces scènes, le texte reste dans la **moitié haute** de la zone de sécurité, et on laisse un **calque vide nommé** (ex. `#slot-image`). Tu pourras y poser ton image sans toucher à la mise en page.
- On peut aussi exporter une version avec **fond transparent** (ProRes 4444 ou WebM alpha) pour superposer les titres à tes images au montage.

## 5 bis. Processus de production

Hyperframes est un outil open source de HeyGen qui fabrique une vidéo à partir de pages HTML animées. Chaque scène est une page web, et l'outil la filme image par image (Chrome + FFmpeg) pour sortir un MP4. On ne travaille pas sur une timeline : c'est Claude qui écrit le code, et Romain fait ses retours sur l'aperçu.

1. **Script** : valider ce document (scènes, textes, timing).
2. **Voix off** : enregistrer la voix, ou utiliser une voix de synthèse provisoire. Elle fixe le timing exact de chaque apparition.
3. **Code** : Claude écrit les 8 scènes en HTML/CSS + animations dans `video/clip/`.
4. **Aperçu** : `npx hyperframes preview` ouvre le lecteur dans le navigateur.
5. **Itérations** : retours scène par scène, Claude ajuste le code.
6. **Rendu** : `npx hyperframes render` produit le MP4 1080 × 1920.
7. **Finitions** : incrustation des images et mixage dans le logiciel de montage de Romain.

Prérequis pour travailler en local : Node.js 22 ou plus récent, et une copie à jour du dépôt (`git pull`).

## 5 ter. Voix de synthèse

**Choix : ElevenLabs** (modèle `eleven_multilingual_v2`). La clé d'API est enregistrée de façon sécurisée dans l'environnement cloud « ywb ».

Échantillons dans `video/voix-tests/` (même phrase test) :

| Fichier | Voix | Profil |
|---|---|---|
| `alain2.mp3` | Alain 2 | Français, profond, narration à suspense |
| `adrien.mp3` | Adrien | Français, grave, calme, rassurant |
| `paul-k.mp3` | Paul K | Français, voix de pub et de bande-annonce |
| `david-tyserre.mp3` | David Tyserre | Français, documentaire, posé |

Voix retenue : **Paul K** ✅

- Fichier : `video/clip/assets/voix-off.mp3` (64,6 s, accélérée ×1,12 sans changement de hauteur). La phrase « …changé de mindset » a été régénérée et insérée à la place de « state of mind ». En v0.7, « L'âge augmente… moins d'effets » et « Pourtant… exactement l'inverse » ont été générés d'un seul tenant (même voix, volume ajusté de −1,4 dB) et insérés à 20,55 s, à la place de « Plus d'âge. Plus d'efforts. Pour moins. ». `voix-off-brut.mp3` = première prise (65 s, avec « state of mind »).
- Minutage mot par mot : `video/clip/assets/voix-off-mots.json` (sert à caler chaque apparition de texte).

## 5 quater. Projet Hyperframes

```
video/clip/
  index.html                       # composition maître (scènes + voix off)
  compositions/s1-dogme.html … s8-signature.html   # les 8 scènes (+ s4a-inverse.html)
  scripts/render-alpha.py          # rendu titres seuls, fond transparent
  assets/voix-off.mp3, voix-off-mots.json
  assets/fonts/inter-var-latin.woff2   # Inter variable (graisse animable 100 → 900)
  assets/vendor/gsap.min.js            # bibliothèque d'animation embarquée
  renders/                         # vidéos rendues
```

Commandes (depuis `video/clip/`) : `npm run dev` (aperçu), `npm run check`, `npm run render`, `python3 scripts/render-alpha.py` (version transparente).

Rendus :
- `renders/ywb-clip.mp4` — clip complet avec voix (versionné) ;
- `renders/ywb-titres-alpha.webm` — titres seuls, fond transparent, léger (versionné) ;
- `renders/ywb-titres-alpha.mov` — titres seuls, ProRes 4444 (≈ 400 Mo, non versionné : à régénérer avec le script).

## 6. Questions ouvertes

- **Durée :** la nouvelle phrase porte le clip à 66,4 s. On garde, ou on revient à 60 s (resserrer les pauses de la voix, accélérer légèrement, ou couper une phrase) ?

- **Retours sur le clip complet :** rythme, textes, symboles, scène par scène.
- **Version transparente :** WebM suffisant pour ton logiciel de montage, ou besoin du ProRes .mov ?

## 7. Journal des versions

- **v0.1** — création du squelette.
- **v0.2** — script de base intégré, voix off v1, découpage en 7 scènes.
- **v0.3** — 9:16 / 60 s, clip 100 % typographique, signature validée, ajout de la scène « Les deux piliers » (marche tai-chi, pleurs sacrés), CTA sans lien, détail des 8 scènes, notes Hyperframes.
- **v0.3.1** — ajout du processus de production Hyperframes.
- **v0.4** — emplacements d'incrustation (scènes 1, 6, 7), export fond transparent, voix de synthèse, musique au montage, échantillons de voix.
- **v0.4.1** — passage à ElevenLabs, 4 échantillons de voix masculines françaises.
- **v0.5** — voix Paul K générée et minutée, projet Hyperframes créé, scènes 1 et 2 codées et rendues en test.
- **v0.6** — scènes 3 à 8 codées, « state of mind » remplacé par « mindset » (texte + voix), rendu complet 60 s et version titres sur fond transparent.
- **v0.7** — acte 1 : « L'âge augmente. On augmente les efforts. Pour toujours moins d'effets. » ; ouverture de l'acte 2 : « Pourtant, le corps des plus de 40 ans ne fonctionne plus comme à 20. En vrai, c'est exactement l'inverse. » (voix, scènes 3 et 4, minutage).
- **v0.8** — images de `images-sources/` incrustées : scène 1 (formule ancestrale), scène 6 (danse mystique, homme qui pleure), scène 7 (homme qui pleure, testostérone booster), scène 8 (logo illustré à la place du logo typographique). Rendu complet régénéré.
