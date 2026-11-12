## Result

Adds a silent 8-second, 1920×1080, 30fps orchestra rehearsal room loop for a web dashboard. Two soft overhead cones, periodic dust, gaslight flicker and burgundy curtains surround empty seating. Upper 20% stays dark. All imagery is original Canvas code; no external research or assets.

## Render

From films/ortam-loop:
- `python3 -m http.server 8765 --bind 127.0.0.1`
- `bash render.sh` contains the exact capture, encoding, contact sheet and verification commands.
- Capture: `node ../../scripts/capture.mjs --url http://localhost:8765/film.html --out renders/frames --workers 2`
- MP4: `ffmpeg -y -v error -framerate 30 -i renders/frames/%06d.png -frames:v 240 -an -c:v libx264 -crf 20 -pix_fmt yuv420p -movflags +faststart out/ortam-loop.mp4`
- WebM: `ffmpeg -y -v error -framerate 30 -i renders/frames/%06d.png -frames:v 240 -an -c:v libvpx-vp9 -crf 28 -b:v 0 -row-mt 1 -threads 4 -pix_fmt yuv420p out/ortam-loop.webm`
- Contact: 8 frames at seconds 0–7, scaled to 480×270 and tiled 4×2.

Chromium file:// restriction is handled through capture's supported HTTP --url option. No kit change, policy workaround or --allow-file-access-from-files fallback was needed. The silent custom output uses capture directly rather than make's local-file/audio delivery pipeline.

## Validation

Frames 0/240 and 1/241 are byte-identical PNGs. All animation uses modulo-240 phase and integer harmonics. Frames 0–239 form the delivered cycle; no duplicate endpoint or xfade. `out/verification.txt` records codec, dimensions, duration, absence of audio and the measured adjacent/seam frame differences. Intermediate renders are excluded from Git. Source and final requested deliverables are committed.
