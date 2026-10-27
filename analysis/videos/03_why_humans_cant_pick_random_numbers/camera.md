# 03 — Camera language

Measured values come from `tools/motion.py` over `metrics/frame_metrics.csv` (zoom = cumulative scale factor of the content,
dx/dy = content shift in full-res px; "content dx +" = camera pans left; "content dy −" = camera tilts down). Full per-second
output is pasted in `shots.json → camera_motion.measured`.

**Key fact:** the camera never stops. There is not a single locked-off frame range longer than ~1 s; even "holds" carry a
1–4 %/s push-in or a slow drift. Big moves are used as transitions *inside* shots (crane-out from the cheque, dolly into the
car window, crane-out from the elevator to the number city, whip pans between Marge and Rico).

## 1. Shot table

| shot | frames | dur s | size | angle | move | measured (whole shot) | easing |
|---|---|---|---|---|---|---|---|
| S1 | 1–108 | 3.60 | ECU→MCU | high→eye | crane/zoom-out + tilt-up, then push-in | 1–31: **x0.161**, dx +823, dy +1722 · 31–61: x1.171 · 61–105: ≈x1.01 | very hard ease-out on the pull (most of it in 15 f) |
| S2 | 109–300 | 6.40 | WS→MCU→MS | low→eye | push-in w/ roll → dolly into car window → hold → pull-back/pan right | 136–166 x1.358 · 166–196 **x2.446**, dy −1057 · 226–256 x0.705 (pull-back) | ease-in-out dolly, ease-out pull |
| S3 | 301–345 | 1.50 | MS→MCU | eye, slight dutch | truck right + push-in + roll | x1.327, dx −490, roll −6.2° | linear |
| S4 | 346–429 | 2.80 | EWS→WS | worm's-eye | push-in + tilt-down (+orbit) | x2.485, dx −351, dy −1079 (per s: x1.23 → x1.46 → x1.38) | ease-in |
| S5 | 430–739 | 10.33 | MLS→MS | eye | truck right + push-in, near-lock, small pull-back, push | 430–490 x1.24 · 490–670 ≈x1.00 ±0.03/s · 670–700 x0.907 · 700–736 x1.07 | gentle ease-in-out |
| S6 | 740–872 | 4.43 | WS→EWS aerial | eye→high | crane-up + pull-back (+15° roll) | whole x**0.049**; per s x0.474, x0.189, x0.607, x0.907, x0.999 | S-curve, long ease-out tail |
| S7 | 873–954 | 2.73 | MS 3-shot | eye/slightly low | push-in + drift right | x1.206 (≈x1.06/s), dx −90 | linear |
| S8 | 955–1063 | 3.63 | insert top-down | bird's-eye | push-in + pan down, follow pencil | x1.808; per s x1.265, x1.472, x0.956, x1.016 | ease-in-out |
| S9 | 1064–1150 | 2.90 | MLS | eye | slow push → whip-pan start | x1.113, dx +412 (+360 in last 28 f), roll +19° | ease-in into the whip |
| S10 | 1151–1220 | 2.33 | MS | high (≈25°) | whip-pan landing, hold, slight pull-back, whip-out | 1140–1170: x1.082, dx +578, roll +11.8° · 1180–1210 x0.893 | whip ease-out / ease-in |
| S11 | 1221–1290 | 2.33 | MLS | eye | whip landing (pull-back) → static + defocus | 1215–1245 x0.809, dx −394 · then x1.01–1.02/s | ease-out |
| S12 | 1291–1413 | 4.10 | MS→MCU (via lens) | eye | slow push + drift (bars parallax), slight pull while magnifier rises, hold | 1290–1320 x1.035 · 1350–1380 x0.937 · 1380–1410 x1.003 | linear, hard end |

## 2. Recurring moves (this video's vocabulary)

| move | where | typical numbers |
|---|---|---|
| **Slow "breathing" push-in** under narration | S1 tail, S5, S7, S9, S12 | **+3 % to +7 % scale per second** (x1.03–x1.07/s); S7 ≈ x1.06/s, S12 ≈ x1.035/s |
| **Fast reveal pull-out (crane-out)** that starts on an ECU detail | S1 (cheque → Rico), S6 (cab → city) | S1: x0.16 in 30 f (≈ -84 %/s); S6: x0.05 over ~100 f with S-curve |
| **Dolly-through into a window / object** | S2 #163–200 (into the car window) | x2.4 in 1 s, with tilt-down ≈ 1000 px |
| **Push-in + tilt-down establishing** on a building | S4 | x1.2–1.5 per s, tilt-down 220–570 px/s |
| **Whip pan between two halves of one set** (no cut) | S9→S10→S11 (Marge ↔ Rico) | ≈580 px in 15 f, roll +12°, zoom x1.08; motion-blurred |
| **Truck + push to re-frame from 2-shot to single** | S3, S5 start | x1.1–1.25 over 1–2 s, dx −300…−500 px |
| **Dutch roll during moves** | S1, S3, S6, S9/S10 | 5–19° accumulated, levels out at rest |
| **Dissolve on a moving camera** | 8 dissolves, each 5–8 frames | both outgoing and incoming plates keep moving |

Push-in rate summary: median slow push ≈ **x1.05 per second** (5 %/s); fast establishing push ≈ x1.25–1.45/s;
reveal pull ≈ x0.2–0.6 per second at peak.

## 3. Blender 5.2-style recipes (720×1280 vertical)

General setup: Output 720×1280 @ 30 fps. Camera sensor fit **Vertical**, sensor 36 mm. Characters/backgrounds are
2D plates on image planes (see visuals.md), so "zoom" can be done either by dolly (gives parallax between plates — preferred,
the source shows parallax on mesh/bars/palms) or by focal length. Use Graph Editor F-curves with the stated easing.
Values assume the main subject plane at Z-distance 10 m from the camera.

### A. Breathing push-in (default for every dialogue/explainer hold)
- Lens 50 mm. Keyframe camera Y (toward subject) 0 → +0.45 m per second for a 3 s shot (≈ x1.05/s on the subject plane at 10 m).
- Add 0.5–1.5° roll drift over the shot and ±8 px lateral drift (noise modifier, strength 0.02, scale 60 frames).
- Interpolation: Linear, or Bezier with very soft handles (no visible ease).

### B. ECU-to-MS reveal crane-out (S1, the hook)
- Lens 35 mm. Start: camera 0.6 m from the cheque plane, pitched −55° (looking down at the desk), roll +5°.
- Frame 1 → 25: move back to 3.8 m and up 1.2 m, pitch −55° → −12°, roll +5° → 0°.
- F-curve: Bezier, start handle long (fast start), end handle very long ("Ease Out" / exponential-out: 80 % of the move by f15).
- Then frames 25–105: breathing push (recipe A) at ≈ +15 %/s for the first second (magnifier entrance), then 0.

### C. Dolly-through into a window (S2 #163–200)
- Lens 35 mm. Camera starts on the WS framing; keyframe 37 frames forward 6–7 m along the camera axis, with pitch −8° and slight
  lower Z, ending framed MCU through the car window. Ease In-Out (Bezier auto-clamped), peak speed at the middle.
- Foreground plates (canopy, sign) must sit between start and end so they wipe out of the top of frame.

### D. Grand crane-out reveal (S6)
- Lens 40 mm → 28 mm (optional focal pull) while the camera rises 0 → 120 m and backs up 0 → 150 m, pitch 0° → −22°, roll 0° → +15° → 0°.
- Duration 100 frames, S-curve with long out-tail: 10 % at f15, 70 % at f50, 95 % at f80, then 30 frames of near-hold.
- Build the city as real 3D (extruded digit buildings 1–9 of decreasing height) so parallax is correct.

### E. Whip pan inside one set (S9 → S10 → S11)
- Lens 50 mm. Yaw the camera 25–35° in 12–15 frames, add roll +10–12° at the middle, dolly in ~5 %.
- Ease In (on leave) / Ease Out (on land); enable motion blur (shutter 0.5) — the source frames #1145–1160 are visibly blurred.
- Place both character set-ups on the same 3D set (desk and window ledge) so the pan passes through real geometry.

### F. Establishing push + tilt-down on a tower (S4)
- Lens 24 mm, camera low (1.5 m) pitched +28° up. Over 84 frames: pitch +28° → +8°, move forward 25 % of distance, slight orbit
  right 6°. Ease In (accelerating). Foreground palms/police car as separate planes for parallax.

### G. Dissolve on moving cameras
- Render both shots with their own camera moves overlapping by 6 frames; cross-fade 5–8 frames (linear opacity) in the compositor/AE.
