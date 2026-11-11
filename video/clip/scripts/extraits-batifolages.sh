#!/bin/sh
# Découpe les extraits de sources/batifolages.mp4 utilisés dans le clip.
# Marge de 0,1 s : la durée exacte est fixée par data-duration.
# Recadrage 1170x624 (ratio des emplacements, filigrane effacé), 960x512, sans son.
set -e
cd "$(dirname "$0")/.."
SRC=../../sources/batifolages.mp4
OUT=assets/videos
mkdir -p "$OUT"
cut() { # nom début durée
  ffmpeg -v error -y -ss "$2" -i "$SRC" -t "$(awk "BEGIN{print $3+0.1}")" -an \
    -vf "delogo=x=1128:y=568:w=64:h=64,crop=1170:624:20:0,scale=960:512,fps=30" \
    -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -g 15 -movflags +faststart "$OUT/$1.mp4"
}
cut s1-cuisine-a    101.40 3.55   # le quadra fatigué, plan serré
cut s1-cuisine-b    168.40 3.05   # même homme, tête basse
cut s6-marche       9.40   3.35   # marche tai-chi, plan large
cut s6-pleurs       33.85  0.95   # pleurs sacrés, gros plan
cut s7-pleurs-a     34.80  0.75   # suite du gros plan
cut s7-pleurs-b     123.25 1.67   # pleurs, plan serré
cut s7-muscles      136.95 2.90   # torse sculpté, pratiquantes conquises
cut s7-rires        156.30 0.78   # éclats de rire
