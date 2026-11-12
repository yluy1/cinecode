# Ortam loop

Quick-mode, code-drawn, silent orchestral rehearsal room background. No external assets or dependencies. 8 seconds, 1920×1080, 30 fps. The static audience viewpoint leaves the upper 20% dark for dashboard content. All motion is a deterministic function of frame modulo 240: dust follows closed elliptical paths; velvet, haze and lamp flicker use integer harmonics of the same period.

## Reproduce

From this directory start `python3 -m http.server 8765 --bind 127.0.0.1`, then run `bash render.sh` in another terminal. Chromium commands may require the approved outer executor context. The script invokes the kit's capture tool with `--url http://localhost:8765/film.html`. No file URL, browser policy change or kit patch is necessary. The make pipeline is not used because this delivery is explicitly silent and requires a custom pair of encodings.

Outputs in `out/`: VP9 CRF 28 WebM, H.264 yuv420p faststart MP4 and a 4×2 contact sheet at seconds 0 through 7. There are no audio streams. Frames and other intermediates stay in ignored `renders/`.

## Loop check

The render includes frames 0–239, not a duplicated endpoint. `verifyLoop=1` exposes frames 240 and 241 for checks only. PNG equality at 0/240 and 1/241 establishes exact periodicity. `verify.py` checks video metadata and compares the grayscale RMS change across 239→0 with adjacent steps 238→239 and 0→1. No xfade, duration change or repeated final frame is needed.
