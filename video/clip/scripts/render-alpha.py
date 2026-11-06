#!/usr/bin/env python3
"""Rend la version « titres seuls » sur fond transparent (ProRes 4444, .mov).

Copie le projet dans un dossier temporaire, rend transparents tous les fonds
marqués `/* fond */`, retire la voix off, puis lance le rendu Hyperframes.

Usage (depuis video/clip/) : python3 scripts/render-alpha.py
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "renders" / "ywb-titres-alpha.mov"

with tempfile.TemporaryDirectory() as tmp:
    work = Path(tmp) / "clip"
    shutil.copytree(ROOT, work, ignore=shutil.ignore_patterns("renders", ".hyperframes", "node_modules"))

    for html in [work / "index.html", *(work / "compositions").glob("*.html")]:
        text = html.read_text(encoding="utf-8")
        text = re.sub(r"background:[^;]+;\s*/\* fond \*/", "background: transparent; /* fond */", text)
        text = re.sub(r"\s*<audio[^>]*>\s*</audio>", "", text)
        html.write_text(text, encoding="utf-8")

    OUT.parent.mkdir(exist_ok=True)
    cmd = ["npx", "--yes", "hyperframes@0.9.19", "render", "--format", "mov", "--quality", "high", "--output", str(OUT)]
    sys.exit(subprocess.call(cmd, cwd=work))
