# Camera language — 05 "The Science Behind Slot Machines"

Measured with `tools/motion.py` on `metrics/frame_metrics.csv` (zoom = cumulative scale factor; dx/dy = content shift in
full-res px; positive dx → camera pans left, positive dy → camera tilts/cranes up). Values inside S7 (unrolling strip,
morph) and S8 800–886 (spinning wheel → fake roll) are polluted by animated content; read them as direction only.

This video is built from **8 shots but ~20 camera phases**: the editor prefers *continuous camera moves through the
set* (follow-moves, move-throughs, zoom-throughs) over cuts. Real joins are 4–6-frame dissolves.

## 1. Shot table

| Shot | Frames | Size | Angle | Camera move (phases) | Measured | Easing |
|---|---|---|---|---|---|---|
| S1 | 1–133 | ECU → MS | eye | 1–40 fast pull-back + crane up (reveal) · 40–133 slow push-in | 1–40: zoom x0.248, dx +619, dy +721, roll +1.65° · 40–134: x1.277, dx −59, dy −60 (≈8.1 %/s) | ease-out reveal (≈60 % of the pull happens in f1–20), then linear |
| S2 | 134–250 | MS → WS → MS | eye | jump cut · 134–147 hold · 147–205 pull-back + crane up + truck right (follow walk) · 205–250 slow push | 135–147: x0.944 · 147–205: x0.604, dy +325 · 205–252: x1.039 (≈2.6 %/s) | ease-in-out follow, linear push |
| S3 | 251–340 | MS two-shot | POV (inside machine), eye level | near-static micro push | 253–341: x1.035, dx +1, dy −24 (≈1.2 %/s) | linear |
| S4 | 341–422 | insert ECU | high + dutch ≈−30° | 342–395 slow push on bill · 395–422 move-through: tilt up + truck right + roll toward level to CREDITS | 342–395: x1.053, dx −65 · 395–424: x1.135, dx −474, dy +592, roll −8.5° | ease-in-out (peak speed ≈#405) |
| S5 | 423–494 | CU | low + dutch ≈+10° | near-static micro push | 425–496: x1.030, dx −11, dy −20 (≈1.2 %/s) | linear |
| S6 | 495–541 | MS → CU | eye, slightly low | 497–528 push-in + tilt down · 528–541 fast dolly through the opened door | 497–528: x1.388, dy −176 (≈37 %/s) · 528–543: x2.72, dx −172, dy −634 | ease-in (accelerates into the machine) |
| S7 | 542–778 | insert / diagram | eye → high | 544–560 push + truck right · 560–640 tilt down + push along list · 640–690 hold/slight pull · 690–768 pull-back + steady tilt down following the stamps · 768–778 morph | 544–560: x1.443, dx −240, dy −304 · 560–640: x2.88, dy −1953* · 640–690: x0.934 · 690–768: x0.878, dy −472 · 768–780: x0.737* | linear drifts; tilt-down speed ≈6 px/f during stamping |
| S8 | 779–928 | MS (machine) → MS (Lenny) | eye | 781–800 pull-back + crane up out of cabinet · 800–886 static then slow push on wheel · 886–928 pull-back + crane up to Lenny | 781–800: x0.598, dy +481 · 800–886: x1.236 (≈7.7 %/s), roll* · 886–928: x0.559, dy +699 | ease-out pull-backs |

`*` = content-animation pollution.

## 2. Recurring moves (the camera grammar)
1. **Reveal pull-back + crane up** (S1 open, S8 781–800, S8 886–928): start tight on an object, pull back 1.7–4× while
   rising, ease-out, 0.7–1.4 s. Used to open and to close.
2. **Follow move-through** (S2 147–205): camera trucks with the character to the next set-piece instead of cutting.
3. **Slow push-in on holds**: dialogue/reaction holds 1–3 %/s (S2, S3, S4, S5); "tension" holds 7–8 %/s (S1 after the
   reveal, S8 wheel).
4. **Insert move-through** (S4 395–422): a 1-second tilt/truck/roll from one prop (bill acceptor) to the next (CREDITS).
5. **Dolly-into-object / zoom-through** (S6 → S7): accelerating push (×1.4 then ×2.7 in 0.5 s) into an opening, then a
   dissolve finishes the move inside.
6. **Tilt down a vertical prop** (S7): the 9:16 frame rides a long paper strip top-to-bottom, following an action
   (stamp) row by row.
7. **Dutch angles** only on inserts/close-ups (S4 −30°, S5 +10°); all character MS shots are level eye-level.
8. **Machine POV** (S3): camera placed inside the machine, foreground reels blurred — a one-off gag angle.

Typical slow push-in rate: **≈1.2–2.9 %/s** for calm holds, **≈8 %/s** for the hook and payoff holds.
Typical pull-back: **×0.25–0.6 over 20–60 f**, ease-out.

## 3. Blender 5.2-style camera recipes (720x1280 vertical)
Render: Resolution 720×1280 (or 1080×1920), 30 fps, Sensor Fit = Vertical? → use **Sensor Fit Auto, sensor 36 mm**;
Depth of Field ON with F-stop 2.8–4 for inserts. Characters are flat cards (Image as Plane, emission shader) placed in
the 3D set; keep them facing camera (Track To constraint) or bake their angle per shot.

### R1 — Reveal pull-back + crane up (S1 1–40)
- Focal 35 mm. Target = reel window centre (Empty "TGT_reels", camera Track-To).
- f1: cam at (0, −0.45 m, 1.05 m) i.e. 0.45 m in front of the reels, slightly below them, roll 1.5°.
- f40: cam at (−0.25, −1.8 m, 1.35 m) — 4× the distance (matches x0.25 scale), 0.3 m higher; roll 0°; retarget the
  Empty from reels to Lenny's chest between f20–f40.
- Interpolation: Bezier, f1 handle "Fast start" (Ease Out, exponential) — 60 % of the travel by f20.
- f40→f133: continue dolly-in 0.25 m (x1.28 over 94 f) linear.

### R2 — Follow move-through (S2 147–205)
- Focal 35 mm. Parent camera to an Empty that follows the character path (Follow Path), plus a separate dolly-back.
- f147: cam 1.6 m from Lenny, height 1.3 m. f205: 2.6 m from Lenny (x0.6), height 1.6 m (crane up to frame the LED sign),
  trucked 1.5 m right to the next machine. Ease In-Out (Bezier auto-clamped).
- f205→f250: push in 0.07 m (≈2.6 %/s), linear.

### R3 — Slow push on a hold (S3, S5, S4 342–395)
- Focal 50 mm (S3, S5) / 28 mm (S4 insert).
- Dolly-in along view axis: distance × (1 − 0.012…0.03 per second). Example S5 (2.4 s): from 0.80 m to 0.78 m. Linear.
- Dutch: set camera roll +10° (S5) / −30° (S4) on the first key and keep constant.

### R4 — Insert move-through (S4 395–422)
- Focal 28 mm, F-stop 2.8, focus distance animated from the bill acceptor to the CREDITS display.
- f395: aimed at acceptor slot, roll −30°. f422: aimed at CREDITS LED 0.35 m higher and 0.15 m right, roll −21°
  (measured −8.5° change), 13 % closer. Bezier Ease In-Out, peak speed at f405.

### R5 — Dolly into the machine (S6 497–541 → S7)
- Focal 32 mm. f497: 1.4 m from the machine face. f528: 1.0 m (x1.39), tilt down 6°. f541: 0.37 m (x2.7 more), aimed at
  the reels, Ease In (slow start, fast end). Door object: hinge rotation 0°→75° over f529–532 (4 frames, linear).
- Dissolve f542–547 to the interior camera already moving forward (continuity of motion hides the cut).

### R6 — Tilt down a vertical prop (S7 560–768)
- Focal 40 mm, camera 0.45 m from the paper strip, high angle 10–20°.
- Animate camera Z downward with the action: ≈6 px/frame on screen ≈ 1 row per stamp. Key one row per stamp hit and
  shorten the spacing (14 f → 3 f) to match the accelerating counter; F-curve linear between keys.

### R7 — Payoff pull-back (S8 781–800 and 886–928)
- Focal 35 mm. f781: 0.9 m from the cabinet front (inside wireframe), f800: 1.5 m (x0.6), crane up 0.25 m, Ease Out.
- f800–886: push in 0.1 m (≈7.7 %/s), linear. f886: 1.4 m → f928: 2.5 m (x0.56), crane up 0.35 m and pan left to frame
  Lenny standing at right; Ease Out (settles into the final hold).

## 4. Transitions (frame-exact)
| Join | Frames | Type |
|---|---|---|
| S1→S2 | #133/#134 | jump cut (pose pop + reframe), no dissolve |
| S2→S3 | #251–254 | 4-f dissolve, ghosted double exposure |
| S3→S4 | #340–344 | 5-f dissolve with diagonal glass-glint streak |
| S4→S5 | #423–428 | 6-f dissolve |
| S5→S6 | #495–498 | 4-f dissolve |
| S6→S7 | #542–547 | 6-f dissolve during a forward dolly (zoom-through) |
| S7→S8 | #779–784 | 6-f cross-fade into the cyan X-ray wireframe while the camera pulls back (move-through) |
