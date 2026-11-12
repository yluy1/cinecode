# Salon Canlı
User-supplied plate: refs/salon.png. This attachment depicts six dolphin conductors, not an interior engraving. Two raised baton tips serve as warm light origins. No source recoloring or crop; aspect-preserving fit.

Serve project root: python3 -m http.server 8876
Open http://localhost:8876/out/salon-canli/film.html
Add ?effects=1 for the black effects layer. Screen blend that video over the plate.

Deterministic seed 73519; 240 frames at 30 fps, silence. End frame duplicates the opening state. Endpoint-inclusive sampling preserves an exact repeated endpoint within the 8-second playback. Source motion and final compression measurements are recorded separately. Camera maximum scale 1.015.

Initial partial motion measurement: 0.09936/255. Effects doubled and HTTP capture repeated. A white plate significantly suppresses screen overlays; the 2/255 adjacent RGB average target is not satisfied by subtle slow lighting. No artificial noise or rapid flicker was introduced to inflate the metric.

Final decoded endpoint RGB MAE: 0/255 for all three videos. Adjacent RGB MAE: MP4 0.442659/255; composite WebM 0.274964/255; effects WebM 0.192416/255. Source average: 0.092444/255. Target 2/255 remains unmet after strengthened rerender. All-intra compression and packet-identical closing frame ensure exact decoded endpoints.
