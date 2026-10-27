# Camera — 02 "Your Brain's Secret Idea Zone"

Measured values come from `tools/motion.py` on `metrics/frame_metrics.csv`. "zoom ×" is the cumulative scale factor (above 1 is a push-in, below 1 a pull-back). "dx/dy" are content shifts in px at 720×1280: positive dy means the content moves down, which reads as the camera tilting up.
The values are unreliable inside dissolves, the zoom-through and the X-ray orbit (inliers under 50).

## 1. Shot table

| Shot | Frames | Size | Angle | Move | Measured (whole shot) | Key sub-moves (measured) |
|---|---|---|---|---|---|---|
| S1 | 1–119 | CU→WS→MCU | eye-low → high → eye | Pull-back + crane up, hold, then push-in + crane down | zoom ×0.905, dx +3, dy +65, roll −1.71° | 1–9: ×1.047, roll −4.47° (roll settle) · 9–25: **×0.790** (fast reveal) · 79–112: **×1.140**, dy +71 |
| S2 | 120–320 | WS→MS | high → eye | Slow push-in, then faster push + crane down | ×1.604, dx −175, dy −181, roll −0.16° | per second ×1.05, 1.04, 1.02, 1.00, 1.04 · 283–300: **×1.132** |
| S3 | 321–371 | POV | top-down | Static, with a nodding bob | ×0.985, dy +25, roll −0.71° | eyelid bands are 2D overlays |
| S4 | 372–619 | MLS→CU | eye, side → front-3/4 | Static/slow push; pull-back; orbit ~60° + push; slow push to CU | ×1.115, dx −11, dy +56, roll +0.11° | per second ×0.99, 1.01, 1.02, 1.01, 0.95 (pull-back), 1.08, 1.04 · 541–566 orbit: ×0.997, dx +31, dy +87 |
| S5 | 620–717 | MCU→WS→MS | eye → slightly high | Fast pull-back + crane up with roll, then slow push | ×0.797, dx +182, dy +83, roll +6.41° | 631–648: **×0.806**, roll +6.8° · 660–715: ×1.03–1.05/s |
| S6 | 718–862 | WS→CU→ECU | flat side-section | Reveal zoom-out, hold, accelerating push, zoom-through | ×3.933, dy −1192 | 721–746: **×0.510** · 763–810: **×2.090** · 854–862: **×3.005 in 8 frames** |
| S7 | 863–946 | insert | flat-on | Pull-back, then push-in toward the merged card | ×0.724, dy −562 | 863–885: **×0.487** · 885–900: ×0.827 · 912–930: **×1.439** |
| S8 | 947–1092 | WS→MLS | eye | Very slow push; recoil on the crash; push-in | ×1.064, dx −143, roll −6.22° (*) | per second ×1.01, 1.04 · 1010–1030: **×0.887**, dy +129 (recoil) · 1030–1089: ×1.127 |
| S9 | 1093–1172 | MCU→MS | low → eye | Slow push, then pull-back + crane | ×0.975, dx +14, dy −79, roll −1.95° | 1125–1150: ×0.949, dy −54 |

(*) The S8 roll value is almost certainly a measurement artefact: the elevator floor scrolling through the doorway is read as image motion. Visually the camera does not roll.

## 2. Recurring camera language

1. **Reveal pull-back at shot start.** S1 #9–25, S5 #631–648, S6 #721–746 and S7 #863–885 all start close on the subject and pull back fast to the wide in 0.5–0.8 s (×0.49–×0.81), with a strong ease-out. This is the series' "here's the world" move.
2. **Constant slow push-in while talking.** Holds are never fully locked: they creep at ×1.01–1.05 per second (S2, S4, S5, S8).
3. **Accelerating push-in into the key term.** S6 #763–810 pushes ×2.09 in 1.6 s, then lands on a near-static CU for the keyword ("hypnagogia").
4. **Zoom-through as a scene change.** S6 → S7 punches into the pupil, ×3.0 in 8 frames, with torn-paper fragments, and comes out inside the new world.
5. **Crane up/down paired with zoom.** The angle changes along with size: high-angle when showing the setup, eye level for reactions (S1, S2, S9).
6. **Orbit for the "wake-up" moment.** S4 #537–566 arcs about 60° around the seated character while the scan line restores him.
7. **Impact recoil.** S8 #1018–1030: a quick pull-back of ×0.89 on the crash, then the push resumes.
8. **Roll accents** of 5–7° on the opening CU and the Edison reveal (S5 +6.8°) give a hand-held "swing".

**Typical rates:** slow push about ×1.02–1.05/s; fast push ×1.13–1.45 per 0.5–0.6 s; reveal pull ×0.5–0.8 over 0.5–0.8 s.

## 3. Blender 5.2-style recipes (720×1280 vertical)

Shared setup:
- Output 720×1280 at 30 fps. Camera sensor fit Vertical, 36 mm sensor.
- Characters are 2D planes (image cards) placed in a 3D set, with the face/eye/mouth sprites as separate card layers in front of the head.
- Use the Graph Editor with Bezier keys and the auto-clamped handle types named below.

### R1 — Reveal pull-back + crane (S1 #9–25, S5 #631–648)
- Lens **50 mm**.
- Key 1 (f9): camera 0.8 m in front of the head, Z = head height, rotation X 90°, Y-roll −5°.
- Key 2 (f25): camera 4.2 m back, Z +1.6 m, pitched down 18°, roll 0°.
- Easing: key 1 handle "Vector"/fast-out, key 2 long "Auto-clamped" ease-in (an exponential-out feel); about 70 % of the distance is covered in the first 6 frames.
- Optional: add a +6° roll at the start for the Edison version.

### R2 — Slow talking push (S2, S5, S8 holds)
- Lens **35–40 mm**. Dolly forward 4–5 % of the subject distance per second.
- Linear interpolation (or a very soft ease) so it never stops. Add a Noise modifier on location X/Z, strength 0.003, scale 60 frames, for life.

### R3 — Accelerating push to the keyword (S6 #763–810)
- Lens **35 mm** → keep it. Dolly from 6 m to 2.8 m (scale ×2.1) over 48 frames.
- Ease-in (slow start, fast end), then a hard stop and a 30-frame ×1.02 creep on the CU.
- Tilt down 8° during the move to follow the sinking character.

### R4 — Zoom-through into the eye (S6 #854–862)
- Animate the focal length 50 mm → 150 mm (×3) over 8 frames, with an exponential F-curve (ease-in), centred on the screen-left pupil.
- At f859 switch to the iris texture card. At f862 cut the pupil open with an animated torn-paper alpha matte that reveals the corkboard scene (a separate scene comped behind it).
- Do the matte in the compositor, or in AE.

### R5 — Orbit around the seated character (S4 #541–566)
- Lens **40 mm**. Parent the camera to an Empty at the chair centre and rotate the Empty Z by 60° over 25 frames (ease-in-out), while dollying in 15 %.
- Because the characters are 2D, either use a 3D-modelled Theo for this shot or billboard the body and swap to a "front-3/4" drawing at the midpoint (hidden under the scan line #555–564).

### R6 — Impact recoil (S8 #1018–1030)
- Two keys: f1018 at the current distance, f1022 pulled back 11 % with a 1° pitch up, then ease back over 8 frames.
- Use a "Back" or elastic F-curve modifier for a small overshoot.

### R7 — Ending pull-back + crane (S9 #1125–1150)
- Lens **40 mm**, starting low (camera at seat height, pitched up 10°).
- Dolly back 5 % and crane up to eye level, pitch 0°, over 25 frames, ease-in-out.
