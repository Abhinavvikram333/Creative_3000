# Camera — 01 "This Tree Hates You"

All values are measured with `tools/motion.py` on `metrics/frame_metrics.csv` over **clean ranges** (dissolve frames
excluded). Zoom factor < 1 = pull-out, > 1 = push-in. "dx/dy" = content shift in px at 720x1280 (content dx + means
the camera pans left; dy + means the camera tilts up). Low `min_inliers` (< 250) = measurement polluted by character
or VFX motion. These are marked †.

## Shot table
| Shot | Frames | Dur s | Size | Angle | Motion | Measured (motion.py, clean range) | Easing |
|---|---|---|---|---|---|---|---|
| S01 | 1–72 | 2.4 | MS | eye | Near-static with a gentle drift: tiny pull 1–31 then a slow push-in 31–61 (x1.125 in 1 s) toward Kai as he sits. | frames 1-72: zoom x1.0851 (in), content dx +3px (camera pans left), content dy -31px (camera tilts down), roll +0.90 deg | linear, subtle |
| S02 | 73–184 | 3.73 | EWS | high → bird's-eye | Huge accelerating crane-up + pull-back from the fallen Kai to a top-down aerial of a tiny island; eases out 150–184. | frames 73-184: zoom x0.0094 (out), content dx +1532px (camera pans left), content dy +3619px (camera tilts up), roll -5.25 deg ; frames 90-184: zoom x0.0227 (out), content dx +1253px (camera pans left), content dy +2719px (camera tilts up), roll -3.70 deg | ease-in-out (slow start 73–80, fastest 90–150, settles 150–184) |
| S03 | 185–225 | 1.37 | insert | eye | Slow push-in on the poster (x1.089 over 190–220), then a tiny settle-back. | frames 190-225: zoom x0.9748 (out), content dx +15px (camera pans left), content dy -3px (camera tilts down), roll +0.92 deg | linear |
| S04 | 226–457 | 7.73 | MLS | eye | Fast pull-back/roll-out from the trunk (226–249: zoom x0.36, roll −27°), ease-out by ~280, then a slow push-in 310–430 (≈ +5 %/s) holding on Kai beside the trunk. | frames 226-249: zoom x0.3608 (out), content dx +2px (camera pans left), content dy +706px (camera tilts up), roll -27.42 deg ; frames 250-455: zoom x0.9488 (out), content dx -40px (camera pans right), content dy +21px (camera tilts up), roll -3.06 deg | ease-out on the pull-back, then linear slow push |
| S05 | 458–515 | 1.93 | UI-screen | bird's-eye | Locked camera; the UI animates (sweep rotates clockwise ~1 rev/2 s, clouds drift right). Push-through blur at the end. | frames 462-512: zoom x1.0047 (none), content dx -2px (camera pans right), content dy +1px (camera tilts up), roll +0.11 deg | none |
| S06 | 516–609 | 3.13 | WS → MLS | eye → slight low | Strong push-in and pan right toward the trunk (519–549 x1.56), slows 549–579, then push + tilt up into the canopy 579–607 (x1.37). | frames 519-607: zoom x2.2909 (in), content dx -741px (camera pans right), content dy -248px (camera tilts down), roll -23.62 deg | ease-in-out per phase |
| S07 | 610–722 | 3.77 | insert (macro) | eye | Locked macro on the leaf; at the end a tilt-down follows the falling drop (702–721: dy −378 px). | frames 612-721: zoom x1.0051 (in), content dx +8px (camera pans left), content dy -373px (camera tilts down), roll -0.80 deg | locked, then ease-in tilt |
| S08 | 723–763 | 1.37 | CU → ECU | eye | Continuous push-in on the head (725–755 x1.46) with a short punch #748–750, tracking to the splat. | frames 725-758: zoom x1.6305 (in), content dx -348px (camera pans right), content dy -386px (camera tilts down), roll -9.31 deg | ease-in (accelerating into the zoom-through) |
| S09 | 764–813 | 1.67 | insert (cross-section) | eye | Locked (x1.0002). | frames 771-812: zoom x1.0002 (none), content dx +0px (camera pans left), content dy -0px (camera tilts down), roll +0.02 deg | none |
| S10 | 814–859 | 1.53 | MS | eye | Near-static (x0.994). | frames 819-856: zoom x0.9975 (none), content dx -11px (camera pans right), content dy +16px (camera tilts up), roll -0.75 deg | none |
| S11 | 860–904 | 1.5 | CU → WS | eye | Pull-back + pan left/tilt up revealing the whole car (863–893: zoom x0.53), ease-out 893–902. | frames 863-902: zoom x0.4963 (out), content dx +503px (camera pans left), content dy +478px (camera tilts up), roll +6.26 deg | ease-out |
| S12 | 905–1059 | 5.17 | MS | eye | Slow push-in (≈ +3 %/s in the first second, then nearly static). | frames 907-1056: zoom x1.0368 (in), content dx -12px (camera pans right), content dy -15px (camera tilts down), roll -0.80 deg | linear |
| S13 | 1060–1221 | 5.4 | MCU | slight low | Slow push-in (1092–1212 ≈ +3–7 %/s) with a slight drift; Kai sways left→centre. | frames 1062-1219: zoom x1.1378 (in), content dx -35px (camera pans right), content dy -77px (camera tilts down), roll -0.07 deg | linear |
| S14 | 1222–1295 | 2.47 | UI-screen (X-ray) | eye | Tilt down the skeleton (1224–1284: dy −431 px), slight push. | frames 1224-1292: zoom x1.0484 (in), content dx -17px (camera pans right), content dy -431px (camera tilts down), roll -0.04 deg | ease-in-out |
| S15 | 1296–1474 | 5.97 | MS | eye | Slow push-in + slight rise (peaks 1359–1389 x1.069/s). | frames 1299-1472: zoom x1.1672 (in), content dx -64px (camera pans right), content dy -132px (camera tilts down), roll +0.27 deg | ease-in-out |
| S16 | 1475–1525 | 1.7 | MS | eye | Pan/track right with Kai (dx −163 px in 1 s), slight push. | frames 1479-1523: zoom x1.0529 (in), content dx -171px (camera pans right), content dy +8px (camera tilts up), roll -8.42 deg | linear |
| S17 | 1526–1795 | 9.0 | WS → MS | eye | Long continuous slow push-in (≈ +4–7 %/s every second, x1.47 total) drifting toward Kai and the fire. | frames 1528-1792: zoom x1.4722 (in), content dx -154px (camera pans right), content dy -319px (camera tilts down), roll -1.30 deg | linear (constant) |
| S18 | 1796–1823 | 0.93 | CU | eye | Slow push-in (x1.10 in 0.8 s). | frames 1798-1821: zoom x1.1016 (in), content dx -23px (camera pans right), content dy -76px (camera tilts down), roll +0.58 deg | linear |
| S19 | 1824–1867 | 1.47 | POV | POV | Slight pull/drift (x0.949) + progressive Gaussian blur to simulate losing sight. | frames 1828-1865: zoom x0.9492 (out), content dx +13px (camera pans left), content dy +36px (camera tilts up), roll +0.19 deg | linear blur ramp |
| S20 | 1868–1949 | 2.73 | UI-screen (thermal) / MS | eye | Near-locked; tiny push then settle (x1.03 / x0.95). | frames 1870-1945: zoom x0.9658 (out), content dx +0px (camera pans left), content dy +28px (camera tilts up), roll -0.77 deg | none |
| S21 | 1950–2043 | 3.13 | WS | eye | Slow push-in ≈ +3 %/s (x1.096 total) with a slight tilt. | frames 1953-2043: zoom x1.0963 (in), content dx -14px (camera pans right), content dy -83px (camera tilts down), roll +1.57 deg | linear |
† Unreliable segments: S02 90–150 (inliers 241–278; generated-video parallax), S06 519–607 (rain + dark, inliers
202–279), S08 725–755 (inliers 101: the face fills the frame and animates), S19 (blur ramp, inliers 18), S13
1182–1219 (steam + red head). For these, read the direction and magnitude from the grids rather than the numbers.
S03's "x0.975" is a push x1.089 (190–220) followed by the first frames of the poster ripping away (220–225).

## Camera language of this video
1. **Constant slow push-in is the default "dialogue camera."** 15 of 21 shots creep in. Measured per-second rates:
   S04 310–430 +2.5…+11 %/s; S12 +3 %/s then ~0; S13 +3…+7 %/s; S15 +0.5…+6.9 %/s; **S17 a steady +4.4…+7.4 %/s
   for 9 s**; S18 +10 %/s; S21 +2.6…+3.9 %/s. **Typical push-in ≈ +4 % scale per second** (≈ x1.04/s), linear, with
   a few px of drift down/right (the camera tilts slightly down toward the character's face).
2. **Big eased reveal pull-backs** open a new idea: S02 crane-up to the island (x0.02 over 3 s, ease-in-out), S04
   pull-back after the poster rip (x0.36 in 0.8 s with −27° roll that untwists, ease-out), S11 car reveal (x0.53 in
   1 s, ease-out).
3. **Push-through into an insert**: S08 accelerating push onto the splat → a cut-away window scales up to full frame
   (S09); S05 radar push + blur → storm; S06 push + tilt up into the canopy → leaf macro (S07). The camera "enters"
   the next image instead of cutting.
4. **Follow-tilts on falling/descending things**: S07 tilts down after the sap drop (−378 px in 0.6 s); S14 tilts
   down the X-ray skeleton from the throat to the legs (−431 px in 2 s).
5. **Lateral track with a walking character**: S16 pans right (≈ −163 px/s) with the waddle.
6. **POV with a blur ramp**: S19 the camera is Kai's eyes (hands in the foreground); Gaussian blur rises 0 → ~25 px
   over 1.2 s.
7. **Locked UI screens**: S05 radar, S09 skin, S20 thermal. The graphics animate and the camera does not move.
8. **Punch-in for a reaction**: S08 a quick +15 % scale punch over 3 frames (#748–750) right after the splat.
9. **Angles**: almost everything is eye-level, straight-on. Exceptions: the aerial (high → bird's-eye), the apple MCU
   (slightly low), and the POV. There is no Dutch angle apart from the transient roll in the S04 reveal.
10. **No hard cuts.** Shots join with 3–7 frame dissolves while the camera keeps moving, so the motion reads as one
   continuous drift.

## Blender 5.2 camera recipes (9:16, render 1080x1920, scaled from 720x1280)
Scene setup for every recipe: Camera *Perspective*, Sensor Fit **Vertical**, sensor 36 mm, **focal 50 mm** (the
plates show little perspective; 50–65 mm matches). The background plate is an image plane at Z = −10 m sized to fill
the frame at 50 mm (height ≈ 2 × 10 × tan(fov/2) ≈ 7.2 m). The character is a second plane at Z = −6 m (cut-out
puppet). Props/VFX go on planes in between for mild parallax. Use F-curve **Linear** interpolation unless noted.
Frame rate 30.

### R1 — Slow dialogue push-in (default)
- Keys: f0 `focal 50 mm` → f(N) `focal 50 × 1.04^(N/30)` (≈ 52.0 mm after 1 s, 56.2 mm after 3 s, 71 mm after 9 s for an
  S17-length shot). Alternatively dolly `loc.z` toward the plates: z(t) = z0 − (z0 − z_char) × (1 − 1/1.04^t).
- Add a drift of −2…−10 px/s down and right (camera `loc.x` +0.01 m/s, `loc.y` −0.01 m/s) toward the face.
- Interpolation: Linear. **Never stops**: carry the motion through the dissolve into the next shot.

### R2 — Eased reveal pull-back (S04 / S11 style)
- f0: focal 135 mm (tight on the detail: poster, paint spot), rot.z −27° (S04) or 0°.
- f24: focal 50 mm, rot.z 0°. Ease **Out** (Bezier, handles: in 0.0, out 0.7 — fast start, soft landing).
- Then hand over to R1 (+4 %/s) from about f40.

### R3 — Crane-up to aerial (S02)
- Best built as an image-to-video generation (see visuals.md). In Blender: camera parented to an empty. f0 loc
  (0, −2, 1.2) looking at the tree, rot.x 90°. f30 loc (0, −20, 30), rot.x 50°. f110 loc (0, −10, 160), rot.x 5°
  (near top-down). Ease In-Out (Bezier). Focal 35 mm. Needs a 3D island plane with the tree card at its centre.

### R4 — Push-through into an insert (S08 → S09)
- f0 focal 50 → f30 focal 110 mm (ease **In**: accelerating), aimed at the target spot (the splat).
- f30–f40: the insert is a plane inside a framed window parented to the head plane. Scale it 0.15 → 1.0 (ease out)
  while a quick 3–5 frame dissolve swaps to the full-frame insert. Optional punch: +15 % focal over 3 frames on the
  reaction beat.

### R5 — Follow-tilt (S07 / S14)
- Animate `rot.x` (or `loc.y` for a 2D-style "pan down") so the content moves up 380–430 px at 720p. At 50 mm on a plate
  10 m away that is ≈ 2.1–2.4 m of camera `loc.y` travel (or ≈ 12° tilt). S07: 18 frames, ease In. S14: 60 frames,
  ease In-Out.

### R6 — Lateral track (S16)
- `loc.x` +0.33 m per second (≈ 160 px/s at 720p on the background plane) plus a +3 %/s push. Linear.

### R7 — POV blur-out (S19)
- Camera static at Kai's eye height. Hand cards in the foreground (Z = −1 m) with a 1–2 px sway. Compositor Blur node
  size 0 → 25 px from f8 to f40 (Linear), and lower the fire's emission 10 %.

### R8 — Locked UI screen (S05, S09, S20)
- No camera move (optional +0.5 %/s). All motion comes from the UI layers (sweep rotation, counters, scan-line
  wipes). Build these in AE/code rather than Blender.

### Transition rule
- Dissolve length 3–7 frames (median 5). Keep **both** shots' camera moves running during the dissolve. For match
  transitions, align the outgoing subject (drop, skeleton, face) with the incoming subject's screen position before
  the dissolve starts.
