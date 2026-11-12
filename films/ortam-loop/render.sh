#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p renders/frames out
# Start separately: python3 -m http.server 8765 --bind 127.0.0.1
node ../../scripts/capture.mjs --url http://localhost:8765/film.html --out renders/frames --workers 2
ffmpeg -y -v error -framerate 30 -i renders/frames/%06d.png -frames:v 240 -an -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart out/ortam-loop.mp4
ffmpeg -y -v error -framerate 30 -i renders/frames/%06d.png -frames:v 240 -an -c:v libvpx-vp9 -crf 28 -b:v 0 -row-mt 1 -threads 4 -pix_fmt yuv420p out/ortam-loop.webm
ffmpeg -y -v error -framerate 30 -i renders/frames/%06d.png -vf "select='not(mod(n,30))',scale=480:270,tile=4x2" -frames:v 1 out/ortam-loop-kontakt.png
node ../../scripts/capture.mjs --url http://localhost:8765/film.html --params verifyLoop=1 --out renders/seam --frames 0,239,240,241
cmp renders/seam/000000.png renders/seam/000240.png
cmp renders/frames/000001.png renders/seam/000241.png
python3 verify.py
