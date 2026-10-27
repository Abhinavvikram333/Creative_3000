# Camera language: series-wide grammar (pilot videos 01–05)

Synthesised on 2026-10-27 from the five pilot decodes. Per-video sources are `analysis/videos/<slug>/{shots.json, camera.md, script.md}`. Measurements come from `metrics/frame_metrics.csv`, which covers every frame at 30 fps (`tools/metrics.py`).

Counts below cover all **60 shots and 55 shot joins** of the five videos (21 + 9 + 12 + 10 + 8 shots, 230 s in total).

**Measurement conventions** (same as `tools/motion.py`):
- **zoom** is the cumulative image-scale factor. Above 1 is a push-in; below 1 is a pull-back. "%/s" means `(zoom^(30/frames) − 1)·100`.
- **dx / dy** is the *content* shift in px at 720×1280.
  - `dx > 0`: content moves right, so the camera pans or trucks left.
  - `dy > 0`: content moves down, so the camera tilts or cranes up.
- **roll** is the content rotation in degrees. `> 0` means the content turns clockwise on screen.
- **t50 / t80** is the fraction of the move's duration needed to cover 50 % / 80 % of the motion. Zoom is measured in log-scale. For an S-curve t50 = 0.5, for ease-out t50 < 0.4, for ease-in t50 > 0.6.
- **Pollution:** values over animated content, dissolves or fewer than about 250 inliers are polluted. The per-video `camera.md` files flag them (†/\*). This document only quotes clean ranges, or says so.

Scratch scripts used for the aggregate numbers (per-second classification, easing t50/t80, caption alignment) were run ad hoc. Re-run them through `tools/motion.py range …` to spot-check any figure.

---

## 0. The grammar in ten rules

1. **The camera never stops.** In 89 % of clean seconds the camera is zooming. Only 11 % are near-static (|zoom| < 1 %/s and pan < 60 px/s). No near-static hold lasts longer than about 1.7 s: 01's UI screens S5 and S9, the 01 S10 MS (1.3 s) and the 04 impact hold #712–745 (1.1 s).
2. **The default is a linear slow push-in of about +4 %/s** (IQR +2…+6 %/s), with a 20–60 px/s drift down/right toward the face.
3. **New information gets a reveal pull-back.** Start on an ECU detail, then pull back ×0.16–0.8 (median ≈×0.5) in 16–42 frames, usually with a crane-up. The move is an S-curve with a long tail.
4. **New worlds get a "suction" push and a zoom-through.** The push accelerates exponentially (t50 ≈ 0.8–0.87) into a pupil, door, page or machine. A portal or 6-frame dissolve completes the move "inside".
5. **The edit is dissolves.** 41 of 55 joins (75 %) are dissolves of 4–14 frames; 88 % of them are 5–8 frames (median 6 f, mean 6.5 f). The camera keeps moving through the dissolve on both sides. Hard, jump or match cuts are 4 of 55 joins, used only for impact or graphic matches.
6. **Big moves happen inside shots, not between them.** Crane-outs, dolly-throughs, whip pans and follow-moves replace cuts. Video 05 has 8 shots but about 20 camera phases.
7. **Shot sizes:** MS is the home size. Wides are for setup, inserts and ECUs for the explanation, and 52 % of shots change size during the shot.
8. **The angle is eye-level by default** (38 of 60 shots open at eye level). High and bird's-eye angles are for establishing or diagram shots, low angles for reactions. A **static dutch is reserved for inserts and close-ups** (3 shots). Roll otherwise appears only as a transient accent during big moves.
9. **Moves are cut to the narration.** 58 % of joins fall within ±6 frames of a phrase-opening caption (22 % would by chance). Pushes land on the keyword, and reveals open the sentence.
10. **Shots are 1–10 s long** (median 3.2 s), but some visual event occurs every 0.5–1 s: a camera phase change, face swap, prop gag or counter tick.

---

## 1. Shot-size and angle distribution (all 5 videos, 60 shots)

### 1.1 Shot size
Each shot's `shot_size` string in `shots.json` was normalised to the tokens below. "Opening size" is the size of the shot's first framing. "Size states" counts every size the shot passes through: 31 of 60 shots (52 %) change size via a camera move.

| Size | Opening size (count) | Shots containing it | Typical use |
|---|---|---|---|
| MS (incl. 2-shot / 3-shot / group) | **17** | **28** | Home size: dialogue holds and reactions, characters full-body or ¾ |
| WS | 12 | 17 | Setup/establishing, start of a push-in |
| Insert (prop / diagram / document / macro) | 8 | 13 | Explanation beats: list, cheque, device, bill acceptor |
| MLS | 5 | 7 | Character in a set (tree, bank) |
| CU | 5 | 10 | Reaction faces, often the end of a push |
| MCU | 4 | 10 | Reaction/hold after a push |
| ECU | 2 | 6 | Start of a reveal pull-back, or the end of a suction push |
| UI-screen (radar, X-ray, thermal) | 3 | 3 | Locked "data" screens (video 01 only) |
| EWS (aerial) | 2 | 3 | Destination of a crane-out (island, number city) |
| POV | 2 | 3 | Gag angle (01 S19, 02 S3; 05 S3 is also a POV) |

Per video (shots / s): 01: 21 / 68.1 s, 02: 9 / 39.1 s, 03: 12 / 47.1 s, 04: 10 / 40.0 s, 05: 8 / 30.9 s.

### 1.2 Camera angle
| Angle | Opening angle (count) | Shots containing it | Notes |
|---|---|---|---|
| Eye level (incl. flat-on diagrams) | **38** | **47** | Default for every character MS |
| High (15–35° down) | 8 | 15 | Setup wides and inserts on desks or decks |
| Low (10–25° up) | 6 | 13 | Reactions, arrivals, "you" CUs (01 S13, 03 S2, 05 S5) |
| Bird's-eye / top-down | 4 | 8 | UI screens, documents, aerial ends (01 S5, 03 S8, 04 S5) |
| POV | 3 | 3 | 01 S19 (blur-out), 02 S3 (own eyes, top-down), 05 S3 (inside the machine) |
| Dutch (static tilt) | 0 | 3 | 03 S3 (≈−6°), 05 S4 (≈−30°, insert), 05 S5 (≈+10°, CU) |
| Worm's-eye | 1 | 1 | 03 S4 (tower establishing) |

21 of 60 shots change angle during the shot. This is almost always a crane: high→eye on a push-down, or eye→high on a crane-out.

---

## 2. Measured motion profile (all clean seconds)

There are 272 one-second windows (half-overlapping) with ≥ 200 inliers. Dissolve frames are excluded. Each window is classified by its zoom:

| Class | Share | Zoom rate, median (IQR) | Pan/tilt speed, median |
|---|---|---|---|
| Slow push (+1…+10 %/s) | **41 %** | **+4.0 %/s** (+2.1…+5.7) | 40 px/s |
| Fast push (> +10 %/s) | 21 % | +19.8 %/s (+15.8…+39.3) | 198 px/s |
| Slow pull (−1…−10 %/s) | 14 % | −4.1 %/s | 69 px/s |
| Fast pull (< −10 %/s) | 13 % | −34 %/s (−52…−26) | 331 px/s |
| Near-static | 11 % | +0.2 %/s | 6 px/s |
| Pure pan/tilt (zoom ≈ 0, pan > 60 px/s) | < 1 % | — | — |

Slow-push median by video: 01 +3.6, 02 +4.0, 03 +4.3, 04 +6.7, 05 +3.4 %/s.
**Pans and tilts almost never occur without a zoom.** Every lateral or vertical move is paired with a push or pull, which is what makes the motion feel 3D.

---

## 3. Coordinate conversion: 2D measurements → Blender 5.2 camera

### 3.1 Standard rig for 720×1280
- `scene.render.resolution_x/y = 720/1280`, 30 fps. Use the `Standard` view transform (see `system/research/blender_5_2_notes.md` §3.1).
- Camera: `sensor_fit = 'VERTICAL'`, `sensor_height = 36` mm. (Equivalent: `AUTO` with `sensor_width = 36`, because AUTO fits the larger render dimension, which is the 1280 height.) The vertical FOV is `2·atan(18/f)`: 35 mm gives 54.4°, 50 mm gives 39.6°.
- **Series default lens: 35 mm** for 3D-ish sets with depth (casino, bank, brain room), and **50 mm** for flat painted plates (01's beach, UI screens). Use 16–24 mm only for fisheye/orbit and worm's-eye shots.
- **Hierarchy:** `RIG_pivot` (Empty; orbit centre, optional) → `RIG_root` (Empty; location = dolly/truck/crane, `rotation_euler.z` = pan/yaw) → `CAM`.
  - Set `CAM.rotation_mode = 'ZXY'` and `CAM.rotation_euler = (90° + tilt, 0, roll)`.
  - With this order the camera's own Z (view axis) rotation is applied first, so `.z` is a true roll.
  - At tilt 0 the camera looks along world **+Y**, with **+Z** up.
- **World layout:** layers are image planes facing the camera at `y = depth` (metres), with `x` = screen right and `z` = screen up.

### 3.2 Formulas
Notation: S = 36 mm sensor height, H = 1280 px, f = focal length in mm, d = distance from the camera to the *reference layer* in metres. The reference layer is the layer that dominates the image; motion.py's inliers come mostly from the background plate.

| Quantity | Formula | Example at 35 mm, d = 10 m |
|---|---|---|
| Pixel pitch on a plane at depth d | `p(d) = S·d / (f·H)` m/px | 8.04 mm/px; frame = 10.3 m × 5.8 m |
| **2D zoom z by dolly** | `d₁ = d₀ / z`, so the camera moves `Δ = d₀·(1 − 1/z)` forward (negative Δ = back) | z = 1.25: dolly 2.0 m in |
| Parallax that the dolly creates | A layer at `dₗ` scales by `dₗ / (dₗ − Δ)`; nearer layers grow faster | Character at 4 m with Δ = 2 m: ×2.0 while the bg grows ×1.25 |
| **2D zoom z by focal length** | `f₁ = f₀·z` (all layers scale equally, no parallax) | z = 1.25: 35 → 43.75 mm |
| Pan/tilt by rotation | `θ = atan(P·S / (f·H))`. Yaw `+θ` for `dx = +P`; pitch `+θ` for `dy = +P` | 100 px ≈ 4.6° at 35 mm, ≈ 3.2° at 50 mm |
| Truck/crane by translation | `Δx_cam = −dx·p(d)`, `Δz_cam = +dy·p(d)`, using d at the moment of the move | dy = +300 px → crane up 2.4 m |
| Roll | Blender roll (`CAM.rotation_euler.z`) = measured `roll`. Clockwise content means the camera rotates CCW about −Z, i.e. +Z local | Verify the sign once with a 30-frame render (§3.4) |
| Rate → total | `z = (1 + r)^(N/30)` | +4 %/s over 90 f: ×1.125 |

**Which to use:**
- **Dolly** when the shot has depth-separated layers. Dolly is the series default, because the reference shows parallax in almost every push.
- **Focal** for flat inserts, UI screens, punch-ins and 2D zoom-throughs.
- A measured content shift can be explained either by rotation (no parallax) or by translation (parallax). Use translation (truck/crane) for follow-moves and reveals over sets. Use rotation for whip pans and tilts down a far plate.

### 3.3 Easing: always in log-zoom space, baked per frame
- A **linear-distance dolly is not a linear zoom.** Moving the camera at constant speed toward a plane makes `log z` accelerate. That is why a constant-speed push reads as a "suction" and a constant-speed pull-back reads as ease-out.
- To hit the measured curves, compute progress `u = E(t)` with `t ∈ [0,1]`. Then set `z(t) = z_total^u`, `d(t) = d₀/z(t)` (or `f(t) = f₀·z(t)`), and pan offsets `= u·P`. Write one key per frame with **LINEAR** interpolation. Blender's own Bezier/QUART easing only approximates this for zooms within ×0.8–1.25.

| Easing id | E(t) | t50 | Where measured |
|---|---|---|---|
| `linear` | t | 0.50 | Slow push-ins (02 S2 #120–283: t50 0.50) |
| `ease_out` | 1 − (1 − t)³ | 0.21 | Dialogue push 04 S4 (#438–558, t50 0.33), crane-out to aerial (01 S2 0.33, 03 S6 0.30) |
| `ease_in` | t³ | 0.79 | Follow-tilt on a falling drop (01 #702–721, 0.79), dolly into the door (05 #497–541, 0.82) |
| `ease_in_out` | cubic in-out | 0.50 | Reveal pull-backs (median t50 0.45), insert move-through (05 #395–422) |
| `suction_in` | t⁴ | 0.84 | Suction push → zoom-through (04 #905–967: 0.87; 01 #725–758: 0.82) |
| `hold` | 0 | — | Locked frames |
| `{cubic_bezier:[x1,y1,x2,y2]}` | CSS-style | any | Late-peak reveals (05 S1 #1–40, t50 0.69): `[0.55, 0, 0.35, 1]` |

### 3.4 Reference Python (Blender 5.2; sketch, untested here because no Blender is installed in this container)
```python
import bpy, math
from bpy_extras import anim_utils
S, H = 36.0, 1280
E = {'linear': lambda t: t, 'ease_in': lambda t: t**3, 'ease_out': lambda t: 1-(1-t)**3,
     'ease_in_out': lambda t: 4*t**3 if t < .5 else 1-(-2*t+2)**3/2, 'suction_in': lambda t: t**4,
     'hold': lambda t: 0.0}

def make_rig(lens=35.0):
    sc = bpy.context.scene
    root = bpy.data.objects.new("RIG_root", None); sc.collection.objects.link(root)
    cd = bpy.data.cameras.new("CAM"); cd.lens = lens; cd.sensor_fit = 'VERTICAL'; cd.sensor_height = S
    cam = bpy.data.objects.new("CAM", cd); sc.collection.objects.link(cam)
    cam.parent = root; cam.rotation_mode = 'ZXY'; cam.rotation_euler = (math.radians(90), 0, 0)
    sc.camera = cam
    return root, cam

def bake_move(root, cam, f0, f1, zoom=1.0, dx=0.0, dy=0.0, roll=0.0, ease='linear',
              zoom_mode='dolly', pan_mode='translate', d_ref=10.0):
    """zoom/dx/dy/roll = measured 2D targets (motion.py convention) for frames f0..f1."""
    x0, y0, z0 = root.location; yaw0 = root.rotation_euler.z
    pit0, roll0, lens0 = cam.rotation_euler.x, cam.rotation_euler.z, cam.data.lens
    prev_u, x, z_ = 0.0, x0, z0
    for f in range(f0, f1 + 1):
        u = E[ease]((f - f0) / max(1, f1 - f0)); zt = zoom ** u
        d = d_ref / zt if zoom_mode == 'dolly' else d_ref
        lens = lens0 * zt if zoom_mode == 'focal' else lens0
        if zoom_mode == 'dolly': root.location.y = y0 + d_ref * (1 - 1 / zt)
        if pan_mode == 'translate':                      # truck / crane (parallax)
            pp = S * d / (lens * H); du = u - prev_u
            x -= dx * du * pp; z_ += dy * du * pp
            root.location.x, root.location.z = x, z_
        else:                                            # pan / tilt (rotation, no parallax)
            root.rotation_euler.z = yaw0 + math.atan(u * dx * S / (lens * H))
            cam.rotation_euler.x = pit0 + math.atan(u * dy * S / (lens * H))
        cam.rotation_euler.z = roll0 + math.radians(u * roll)
        cam.data.lens = lens; prev_u = u
        root.keyframe_insert('location', frame=f); root.keyframe_insert('rotation_euler', frame=f)
        cam.keyframe_insert('rotation_euler', frame=f); cam.data.keyframe_insert('lens', frame=f)
    for idb in (root, cam, cam.data):                    # 5.x: F-curves live in channelbags
        ad = idb.animation_data
        cb = anim_utils.action_ensure_channelbag_for_slot(ad.action, ad.action_slot)
        for fc in cb.fcurves:
            for k in fc.keyframe_points: k.interpolation = 'LINEAR'
```
**QA loop:**
1. Render the shot to a PNG sequence.
2. Run `tools/metrics.py` on it.
3. Compare with `python3 tools/motion.py <new csv> range a b` against the reference range.
4. Accept when zoom is within ±5 % and pan within ±15 % or ±30 px.

The same 2D targets drive a Remotion fallback directly: `scale(z(t))` about the target point, `translate(u·dx, u·dy)`, `rotate(u·roll)`. That gives no parallax.

---

## 4. The moves

Each move below lists its occurrences (video, shot, frames), the measured numbers, the easing, and a Blender 5.2 recipe for a 720×1280 camera (§3.1 rig unless stated otherwise).

### M1. Slow push-in ("breathing" push): default under narration
- **Frequency:** present in about 37 of 60 shots. It is 41 % of all clean seconds.
- **Measured:**

| Example | Frames | Zoom | Rate | Drift | Easing (t50) |
|---|---|---|---|---|---|
| 01 S17 long fire push | #1528–1792 (8.8 s) | ×1.472 | +4.5 %/s | dx −154, dy −319 | ≈linear (0.37) |
| 02 S2 stage | #120–283 | ×1.253 | +4.2 %/s | dx −101, dy −113 | linear (0.50) |
| 03 S7 3-shot | #873–954 | ×1.206 | +7.2 %/s | dx −90 | linear |
| 05 S5 dutch CU | #425–494 | ×1.024 | +1.0 %/s | ≈0 | linear |
| 05 S1 after reveal (tension) | #40–133 | ×1.275 | **+8.1 %/s** | dx −61, dy −58 | linear |
| 05 S8 wheel (tension) | #800–886 | ×1.236 | +7.7 %/s | (wheel spin pollutes the pan) | — |
| 04 S4 dialogue push (fast) | #438–558 | ×1.802 | +15.9 %/s | dy −422 | ease-out (0.33) |

- **Rates by mood:**
  - calm hold / dialogue: +1…+4 %/s
  - normal: +4…+6 %/s
  - tension or "the hook pays off": +7…+8 %/s
  - eager explanation push: +15 %/s with ease-out
- **Drift:** 20–60 px/s; the camera pans right and tilts down, toward the face.
- **Blender:**
  - Lens 35 mm (sets) or 50 mm (flat plates). Use `zoom_mode='dolly'` with `d_ref` = background depth.
  - For a 3 s calm hold at +4 %/s (×1.125) with the bg at 10 m: dolly 1.11 m in (10 → 8.89 m). Truck +0.1 m right and crane −0.1 m for the drift. LINEAR.
  - Optional life: an F-curve Noise modifier on `RIG_root` location X/Z (strength 0.003–0.01 m, scale 60 f). Its 2D equivalent is ±2–5 px.
  - **Carry the push through the outgoing dissolve.** Never ease it to zero before a join.

### M2. Punch-in (and its inverse, the impact recoil)
- **Frequency:** rare. One clean reaction punch and one recoil in 60 shots. Short "whip-zooms" also end suction pushes (M6).
- **Measured:**
  - 01 S8 #747–751: ×1.17 in 4 f (+15 % over 3 f), dx −124, dy −116. This comes right after the splat lands (reaction beat).
  - 02 S8 recoil #1018–1022: ×0.942 in 4 f, then ×0.887 by #1030 with a 1° pitch up, then the push resumes (×1.127 over #1030–1089).
  - 04 S1 #197–209: whip-zoom ×1.07 → ×2.27 in 12 f, peak ×1.159 per frame, then a hold.
- **Blender:** use `zoom_mode='focal'` (no parallax, as in the reference).
  - Punch: 35 → 41 mm over 3 f (`ease_out`), then continue the M1 push from 41 mm.
  - Recoil: 35 → 32.3 mm over 4 f (`ease_out`) and pitch +1°, then back over 8 f. An F-curve `BACK` easing gives the small overshoot.
  - Optional: a 2-frame location Noise burst (0.02 m) for the impact shake.

### M3. Reveal pull-back (± crane-up): opening a new idea
- **Frequency:** about 14 instances. It opens 4 of 5 videos at frame 1 (01 starts near-static). It is also the outro of 05.
- **Measured:**

| Example | Frames (f) | Zoom | Rate | Content shift | Roll | t50 / t80 |
|---|---|---|---|---|---|---|
| 05 S1 hook (reels → Lenny) | #1–40 (39) | ×0.248 | −66 %/s | dx +619, dy +721 | +1.6° | 0.69 / 0.82 |
| 03 S1 hook (cheque → Rico) | #1–31 (30) | ×0.161 | −84 %/s | dx +823, dy +1722 | +0.6° | 0.47 / 0.67 |
| 01 S4 poster rip | #226–249 (23) | ×0.361 | −74 %/s | dy +706 | **−27.4°** (unwinds) | 0.43 / 0.83 |
| 01 S11 car reveal | #863–893 (30) | ×0.531 | −47 %/s | dx +455, dy +431 | +5.4° | 0.57 / 0.83 |
| 02 S1 open | #9–25 (16) | ×0.790 | −36 %/s | small | −0.3° | 0.69 / 0.88 |
| 02 S5 Edison | #631–648 (17) | ×0.806 | −32 %/s | dx +183 | +6.8° | 0.35 / 0.47 |
| 02 S6 diagram | #721–746 (25) | ×0.509 | −56 %/s | dx +213 | — | 0.40 / 0.68 |
| 02 S7 board | #863–885 (22) | ×0.487 | −63 %/s | small | — | 0.55 / 0.82 |
| 04 S9 flipbook | #1078–1118 (40) | ×0.422 | −48 %/s | dy +832 | — | 0.45 / 0.70 |
| 05 S8 out of the cabinet | #781–800 (19) | ×0.598 | −56 %/s | dy +481 | — | 0.37 / 0.68 |
| 05 S8 outro to Lenny | #886–928 (42) | ×0.559 | −34 %/s | dy +699 | — | 0.36 / 0.57 |

- **Typical:** ×0.16–0.8 (median ≈ ×0.5) in 16–42 f (0.5–1.4 s). The content almost always moves down by +300…+1700 px, so the **camera cranes up while pulling back**.
- **Easing:** the per-video notes call it "ease-out", but per-frame scale shows an **S-curve**: 5–10 slow frames, a peak at 35–70 % of the move (median t50 0.45), then a long tail.
  - Example, 05 #1–40: per-frame scale 1.000 → 0.922 at #28 → 0.988 at #40.
  - Use `ease_in_out`. For the late-peak hook version use `cubic_bezier [0.55, 0, 0.35, 1]`.
  - Then hand over to M1 at +4…+8 %/s with no hold.
- **Blender** (05 S1 as the worked example):
  - Lens 35 mm. Reference layer = the slot machine plane at d₀ = 0.6 m (ECU of the reel window).
  - z = 0.248, so d₁ = 0.6 / 0.248 = 2.42 m. Dolly back 1.82 m.
  - Crane: dy +721 px at the mid distance (√(0.6·2.42) ≈ 1.2 m, p ≈ 0.96 mm/px) ≈ **+0.69 m up**. Pitch stays level.
  - Truck: dx +619 px ≈ −0.6 m (the camera moves left).
  - Roll +1.6°. Easing `cubic_bezier [0.55,0,0.35,1]` over f1–40, then M1 (+8 %/s, LINEAR) over f40–133.
  - **Resolution budget:** a ×4 pull-back needs the start framing to hold up at 4× magnification. A 1152×2048 plate gives only 288×512 source px in the ECU. Either:
    - generate the plate at 2160×3840 (good up to about ×3), or
    - put a separate high-res **detail plate** (an image-edit crop of the same area, `system/research/chatgpt_image_prompting_2026.md` §6.5) as a plane just in front of the wide plate, and fade it out between f10 and f25.

### M4. Crane-out to aerial (grand reveal)
- **Frequency:** 2 instances (01 S2 "only tree in sight", 03 S6 "number city"). Possibly I2V-generated in the original (see `toolchain_hypotheses.md` E3).
- **Measured:**
  - 01 #90–184: ×0.023 in 94 f, dx +1253, dy +2719, roll −3.7°, t50 0.33 (ease-out). The ease-in start is #73–90.
  - 03 #740–872: ×0.050 in 132 f, roll +15.8° that returns to 0, t50 0.30. Per-second ×0.47, 0.19, 0.61, 0.91, 1.00.
- **Blender:**
  - Lens 35–40 mm (optionally pull the focal to 28 mm). Use a **real 3D ground**: a large plane with the plate projected on it, plus a few extruded or card props. Image cards alone break here.
  - Start: camera 2 m from the subject at 1.2 m height, pitch 0°.
  - End: 120–160 m up, 10–150 m back, pitch −70…−88° (to top-down).
  - Easing: `ease_in_out` for the first 15 % and `ease_out` thereafter. Equivalent: a custom S-curve with 10 % at f15, 70 % at f50 and 95 % at f80, then 30 f of near-hold.
  - Optional roll 0 → +15° → 0.
  - If the plate cannot provide the aerial, **generate the aerial as its own plate and dissolve or zoom-match** at the frame where both framings agree. This is the I2V candidate in `system/PIPELINE.md`.

### M5. Suction push → zoom-through transition
- **Frequency:** 6 of 55 joins (11 %). Each one leads into a new world: eye → brain room, head door → room, page → drawing, splat → cross-section, pupil → corkboard, machine → interior.
- **Measured:**

| Example | Frames (f) | Zoom | t50 | Peak per-frame scale | Portal / join |
|---|---|---|---|---|---|
| 04 S7 → S8 (back of head) | #905–967 (62) | ×3.68 | **0.87** | ×1.215 @#966 | drawn door opens #961–971 (11 f) |
| 04 S1 → S2 (eye) | #181–213 (32) | ×2.27 | 0.72 | ×1.159 @#207 | pupil → lens circle #214–228 (15 f) |
| 05 S6 → S7 (machine) | #497–541 (44) | ×3.26 | 0.82 | ×1.084 @#541 | door swing #529–532, then a 6-f dissolve #542–547 |
| 01 S8 → S9 (splat) | #725–758 (33) | ×1.63 | 0.82 | ×1.073 @#752 | cut-away window scales up #758–770 (13 f) |
| 02 S6 → S7 (pupil) | #854–862 (8) | ×3.0 | — | ×1.495 @#858 | torn-paper reveal #855–863 (9 f) |
| 04 S9 → S10 (page) | #1147–1170 | ×1.68 | — | — | page-edge zoom-through #1153–1179 (27 f) |

- **Shape:** about 1.0 → 1.2 over the first 2/3, then ×2–4 in the last 8–12 f. Use `suction_in` (t⁴) in log space. The join takes 6–27 f (median 12): a portal shape growing past the frame edges, or a dissolve while still moving forward.
- **Blender:**
  - Lens 35 mm. `zoom_mode='dolly'` toward the portal object. Example 04 S7: d 4.0 → 1.02 m over 62 f with `suction_in`.
  - Or `'focal'` 50 → 150 mm for a flat portal (02 S6, 8 f).
  - The **next scene is rendered separately**. Composite it inside the portal with an animated alpha matte (circle, door or torn paper) that scales from the portal's size to full frame, `ease_out`, over 6–12 f.
  - The 5.2 VSE Compositor effect strip or a compositor node group can do the matte (`blender_5_2_notes.md` §2).
  - The incoming shot must **already be moving forward** (M1 at +5…+20 %/s) so the motion carries on.

### M6. Dolly-through (into a window, door or opening; stays in the shot)
- **Frequency:** about 5 instances: 03 S2 (car window), 04 S3 (dive to the table), 04 S8 (doorway), 05 S6 (opened cabinet), 01 S6 (into the canopy).
- **Measured:**
  - 03 #139–199: ×3.53 in 60 f, dy −1405 (tilt down), t50 0.62 (`ease_in_out`).
  - 04 #391–421: ×4.19 in 30 f, peak ×1.22 per frame @#399, t50 0.33 (`ease_out`), with a rack focus #397–402.
  - 05 #528–541: ×2.35 in 13 f, dy −536, `ease_in`.
  - 01 #579–607: push and tilt up ×1.37.
- **Blender:**
  - Lens 32–35 mm.
  - Foreground layers (canopy, sign, door frame) must sit **between the start and end camera positions** so that they wipe past the frame edge. This is the parallax tell of a real dolly.
  - Example 03 S2: move 6–7 m along the view axis in 37 f, pitch −8°, `ease_in_out`.
  - Example 04 S3: 3 m forward and drop to 0.3 m, pitch to 0°, `ease_out`. DOF f/1.8, focus 3 m → 0.4 m over f397–402.
  - Example 05 S6: a hinged door plane rotates 0 → 75° over 4 f (LINEAR) while the camera goes 1.0 → 0.37 m with `ease_in`.

### M7. Orbit (arc around a seated character)
- **Frequency:** 2 instances (02 S4 "wake-up", 04 S2 brain room). There are small arcs elsewhere (03 S4 ≈ 6°).
- **Measured:**
  - 02 #537–566: ≈60° arc in 25–29 f with a 15 % push (2D metrics: ×1.067).
  - 04 #229–289: ≈100° arc with a wide or fisheye lens and a crane-up. 2D: ×0.648, dx +1556 px, roll +66° (orbit parallax pollutes the roll, so read the direction only). `ease_in_out` in both.
- **Blender:**
  - Put `RIG_pivot` at the character's head and parent `RIG_root` to it at radius r.
  - Key `RIG_pivot.rotation_euler.z` −40° → +60° (04) or 0 → 60° (02) over 25–60 f, `ease_in_out`. Dolly r by −15 %.
  - Lens 40 mm (02) or 16 mm. Alternatively `cam.data.type='PANO'` with `panorama_type='FISHEYE_EQUISOLID'` (Cycles) for 04.
  - **Flat cards break in an orbit.** Either add a Track-To constraint so the card faces the camera and swap to a ¾-view pose sprite at the midpoint (hide the swap under an FX, as 02 hides it under the scan line #555–564), or route the shot to I2V.

### M8. Tilt / follow-tilt / riding a vertical prop
- **Frequency:** about 6 instances.
- **Measured:**

| Example | Frames | Content dy | Speed | Easing |
|---|---|---|---|---|
| 01 S7 follow the falling drop | #702–721 | −378 px | peak 54 px/f | `ease_in` (t50 0.79) |
| 01 S14 down the X-ray skeleton | #1224–1284 | −431 px (+2.4 %/s push) | 7 px/f average, peak 29 | `ease_in_out` |
| 05 S7 down the stamped list | #690–768 | −472 px (pull ×0.88) | ≈6 px/f, one row per stamp hit | linear, stepped |
| 04 S5 down the document | #616–676 | −170 px with ×1.38 push | — | linear |
| 03 S4 tower establishing (worm's-eye) | #346–429 | −1079 px with ×2.49 push | 220–570 px/s | `ease_in` |

- **Blender:**
  - **Rotation tilt** for far plates. 01 S14 at 50 mm: atan(431·36/(50·1280)) = **13.6° pitch down** over 60 f, `ease_in_out`.
  - **Crane** for props near the camera. 05 S7: paper at 0.45 m, 40 mm gives p = 0.32 mm/px, so 472 px ≈ 0.15 m down.
  - For a stepped ride, key one stop per action (the stamp hits at #699, 713, 722, 728, 733, 737, 740, 743, 747, 750, 753, 756, 759, 762) with LINEAR between.

### M9. Truck / follow move-through / insert move-through
- **Frequency:** about 6 instances.
- **Measured:**
  - 01 S16 waddle: dx −171 px in 44 f (≈4 px/f, 116 px/s) with a +3.6 %/s push, linear.
  - 03 S3: dx −490, ×1.33 in 44 f, roll −6°, linear.
  - 04 S6 #802–856: dx −379 in 54 f, `ease_in`.
  - **05 S2 follow-walk** #147–205: ×0.604, dy +325 (pull-back + crane up + truck right), peak 24 px/f @#156, `ease_out` (t50 0.36).
  - **05 S4 insert move-through** #395–422: ×1.16, dx −470, dy +564, roll −7.7° in 27 f, `ease_in_out` with peak ≈#405. It travels from the bill acceptor to the CREDITS display, replacing a cut.
- **Blender:**
  - Translate `RIG_root` (`pan_mode='translate'`). 05 S2: 35 mm, camera 1.6 → 2.6 m from Lenny (z 0.6), crane +0.3 m, truck +1.5 m. The character card walks on a path; keep its world speed equal to the truck speed so it stays framed.
  - Insert move-through: 28 mm, f/2.8. Aim from prop A to prop B (0.35 m up, 0.15 m right), roll −30° → −21°, `ease_in_out`. Animate the focus distance with it.

### M10. Whip pan (inside one set)
- **Frequency:** 2 joins, both in 03 (S9 → S10 → S11, Marge ↔ Rico).
- **Measured:**
  - 03 #1140–1170: dx +578 px (≈580 px of it in 15 f), peak **66 px/f** @#1158, roll +11.8°, ×1.08, motion-blurred. Starts `ease_in` (#1100–1150 t50 0.82), lands `ease_out`.
  - Landing #1209–1245: dx −474, ×0.73 (pulls back as it lands), t50 0.36.
- **Blender:**
  - 50 mm. Yaw `RIG_root` by 25–35° in 12–15 f: atan(578·36/(50·1280)) ≈ 18° for the measured on-screen part. The rest is the blur zone.
  - Roll +10…+12° at mid-move, dolly +5 %. `ease_in` on leaving, `ease_out` on landing.
  - **Motion blur on** (`scene.render.use_motion_blur = True`, shutter 0.5).
  - Both halves sit in the **same 3D set** so the pan passes real geometry. Alternatively, use a 3–4-frame directional-blur dissolve between two separately rendered shots.

### M11. POV and fisheye
- **Frequency:** 3 POV shots and 1 fisheye-like orbit.
- **Measured:**
  - 01 S19 (losing sight): ×0.949, near-static, Gaussian blur 0 → about 25 px over 1.2 s.
  - 02 S3 (looking down from own eyes): ×0.985, dy +25 (nodding bob), eyelid bands as 2D overlays.
  - 05 S3 (inside the machine): ×1.035 over 3 s, blurred reel strips occupy the bottom 25 %.
  - Fisheye: 04 S2 orbit (see M7).
- **Blender:**
  - POV = camera at the character's eye height. Foreground hand or reel cards at 0.3–1 m with DOF f/1.4–2.8, so the near layer goes soft.
  - Blur-out: compositor Blur node, size 0 → 25 px over 36 f.
  - Eyelids: two black planes (or a compositor mask) keyed `ease_in_out`.
  - Fisheye: Cycles `cam.data.type='PANO'`, `panorama_type='FISHEYE_EQUISOLID'`, `fisheye_fov` 180°, crop to 9:16. Alternatively use a compositor Lens Distortion node on a 16 mm render (EEVEE/Workbench friendly).

### M12. Dutch angle and roll accents
- **Static dutch:** 3 shots, inserts and CUs only. 05 S4 ≈ −30° (bill insert, high angle), 05 S5 ≈ +10° (low CU of Lenny glaring), 03 S3 ≈ −6° accumulated during a truck. **Character MS shots are always level.**
- **Roll accents during moves:** 01 S4 −27.4° unwinding to 0 in 23 f, 02 S5 +6.8° in 17 f, 03 S6 +15.8° → 0, 03 S9/S10 +12…+19° in the whip, 04 S1 −60° over 6 s (free fall, linear).
- **Blender:** `CAM.rotation_euler.z` (true roll with `rotation_mode='ZXY'`). For a static dutch, key it once and leave it constant. An accent uses the same easing as its move and should return to 0 by the end of the move.

### M13. Locked-off (UI screen / impact)
- **Frequency:** 11 % of clean seconds, nearly all of it 01's UI screens (S5 radar, S9 cross-section, S20 thermal), the 01 S10 MS (#819–856) and the 04 impact hold (#712–745, 1.1 s).
- **Blender:** no camera keys, or an optional +0.5 %/s. All motion comes from the UI layers (sweep, counters, scan-line wipes), which are better built in code (Remotion or text strips) for exact digits. After about 1 s, resume an M1 or M3 move.

---

## 5. Transition grammar (55 joins)

| Type | Count | Share | Length in frames: median (range) | Notes / examples |
|---|---|---|---|---|
| **Dissolve** (cross-dissolve / cross-fade) | 36 | 65 % | **6** (4–14) | Both cameras keep moving. 05 adds a ghosted double exposure or a glass-glint streak (#251–254, #340–344). 02 S4 combines it with an X-ray scan-line wipe (14 f) |
| Match dissolve (graphic / morph match) | 5 | 9 % | 6 (4–7) | Falling drop (01 #722–725), skeleton over Kai (01 #1293–1299), Theo→Edison morph (02 #617–622), porthole → rug circle (04 #331–336), card → doorway (02 #943–949). Align the outgoing and incoming subjects' screen positions first |
| **Zoom-through** (portal) | 6 | 11 % | 12 (6–27) | See M5 |
| In-camera move-through (crane, paper-wipe reveal) | 2 | 4 % | 18–27 | 01 S2 crane morph, 01 S4 poster rips away |
| Whip pan | 2 | 4 % | 16–20 | 03 only (M10) |
| Hard cut | 2 | 4 % | — | Impact or emphasis: 03 #430, 04 #712 (landing) |
| Jump cut (pose pop, same set) | 1 | 2 % | — | 05 #134 (re-pose + reframe) |
| Match cut | 1 | 2 % | — | 04 #1078 (stack = flipbook) |

- **All dissolves (41):** median 6 f, mean 6.5 f. Distribution: 4 f ×3, 5 f ×9, 6 f ×10, 7 f ×11, 8 f ×6, 9 f ×1, 14 f ×1. Video 05 runs short (4–6 f); 01–04 mostly run 5–8 f.
- **Frequency:** one join every 3.75 s on average, but camera phase changes happen every 1–1.5 s.
- **Opening:** every video starts mid-move with no title card. 04 loops (f1200 matches f1).
- **Ending:** a hard end on a hold, often a deadpan face (05) or a callback (02), with no end card.
- **Recipe (Blender or Remotion):** render each shot with **3–4 f of handles on both sides** and keep the camera curves running into the handles. Cross-fade linearly over 6 f (VSE cross strip, a compositor Mix, or ffmpeg `xfade=fade:duration=0.2`).

---

## 6. Shot length distribution (60 shots)

| Length | < 1.5 s | 1.5–3 s | 3–5 s | 5–7 s | ≥ 7 s |
|---|---|---|---|---|---|
| Shots | 5 | 20 | 22 | 7 | 6 |

- **Overall:** mean 3.75 s, median 3.23 s, min 0.93 s (01 S18), max 10.33 s (03 S5).
- **Long shots** (≥ 7 s: 01 S4, 01 S17, 02 S4, 03 S5, 04 S1, 05 S7) all carry **2–5 camera phases**, so no single framing lasts more than about 3 s.
- **Planning rule for new videos:**
  - 1 shot per 1–2 narration clauses, 2.5–4.5 s.
  - 1–2 long "explainer" shots of 6–9 s with internal moves.
  - 1–2 sub-1.5 s reaction inserts.

---

## 7. How camera moves align with narration beats

**Measured alignment:** shot joins vs phrase-opening caption cards (cards after punctuation, or starting with So/But/When/If/You/The…).

| | Median distance | Within ±6 f |
|---|---|---|
| 55 transition starts | **5 f** | **58 %** |
| Random frames (chance) | 17 f | 22 % |

Video 04's decode states that **every** transition lands on a narration pivot word: "your brain" #214, "People" #331, "So before" #438, "If time" #616, "When they landed" #712, "But when he" #857, "You see" #957, "So when you" #1078. In 05: "So" #137 (S2), "Your buddy" #251 (S3), "So" #493 (S6), "Inside" #536 (S7).

**Beat → camera mapping** (use when converting beats to `shot_plan.json`):

| Beat (script.md) | Camera move | Examples |
|---|---|---|
| Hook, frame 1 | M3 reveal pull-back from an ECU of the key object (×0.16–0.25 in about 1 s), then an M1 tension push (+7…+8 %/s) while the payoff word lands | 03 S1, 05 S1 (reels land 7·7 on "two jackpot symbols"), 04 S1 (one long 3D move) |
| Setup / place | M4 crane-out, or an M9 follow-move to the next set-piece | 01 S2 "only tree in sight", 05 S2 "machine next door" |
| Dialogue / buddy line / reaction | M1 calm push +1…+4 %/s; POV or dutch for a gag | 05 S3 POV, 05 S5 dutch CU |
| Literal action ("you put in another hundred") | Insert + M9 insert move-through to the consequence; the counter reaches its value on the stressed word | 05 S4: CREDITS 0 → 100 over #404–414 on "starting" |
| Turn ("let's crack it open", "You see,") | M5 suction push → zoom-through, timed so the portal opens on the turn word | 05 S6 → S7, 04 S7 → S8 |
| Explanation | Insert or diagram with M8 tilts and slow pushes; a camera stop or glint on each key noun | 05 S7: glint on "jackpot" #644, x1 badge on "once" #681, one stamp per beat of "over and over" |
| Keyword emphasis | Accelerating push (M1 fast or M5) that stops on the keyword | 02 S6 "hypnagogia", 04 S4 LEDs all on at #569 "way too fast" |
| Payoff / punchline | M3 pull-back to the character's deadpan reaction, ending on a hold | 05 S8 #886–928, 02 S9 |

**Micro-timing:**
- A dissolve's first frame falls within about 6 f of the new phrase's first caption card, on either side.
- Face swaps and prop events land on the stressed word itself (`library/characters/<Name>/emotions/emotions.md` timelines).
- Camera phase changes follow within 0–10 f.
