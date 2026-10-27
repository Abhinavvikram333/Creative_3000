# Camera language: 04 "The Scientist's Insane Time Test"

All measurements come from `tools/motion.py` on `metrics/frame_metrics.csv`, which measures content motion on every frame. "zoom xN" is the summed per-frame image scale; dx/dy are content shift in px at 720x1280; roll is content rotation.
**Caveat:** a few ranges include object motion, not only camera motion: the stack growing (968–1077), Dex filling the frame (181–213), and orbit parallax (229–330). The descriptions below are what I checked visually on the grids.

## 1. Shot table

| Shot | Frames | Dur | Transition in | Size | Angle | Move (visual) | Measured (motion.py) | Easing |
|---|---|---|---|---|---|---|---|---|
| 1 | 1–213 | 7.10 s | loop match from f1200 | WS → MS → ECU (eye) | high → bird's-eye → eye-level follow | orbit + tilt-down off the edge, dive alongside the falling Dex with a continuous roll, accelerating push into the eye | whole: zoom x3.04, dx −1202, dy −540, roll −55.4°. 1–30: x0.90, dx −462, roll −26°. 31–180: x1.49, roll −32°. 181–213: **x2.27** | ease-in on the final push |
| 2 | 214–330 | 3.90 s | zoom-through pupil (214–228) | MS → insert porthole | wide-angle eye → high | orbit L→R around Noggin + crane-up/tilt-up, push to the porthole, settle | whole: x0.69, dx +1718, dy +119, roll +76° (orbit parallax). 214–228: x1.02. 289–330: x1.06 | ease-in-out |
| 3 | 331–437 | 3.57 s | dissolve 331–336 (circle match) | WS bird's-eye → insert table | bird's-eye → high → table level | tilt-up + dolly-in, then a fast dolly forward/down to the toy cars with rack focus, then a slow-mo creep | whole: x4.39, dy −1074. 331–390: x0.94 (tilt). 391–421: **x4.19**. 421–437: x1.12 | ease-in, then a hard ease-out into slow-mo |
| 4 | 438–615 | 5.93 s | dissolve 438–444 | MS 2-shot → ECU insert | eye-level | slow push-in on the 2-shot, which then speeds up into the device ECU (DOF grows) | whole: **x3.96**, dx −499, dy −974. 438–558: x1.80. 558–615: **x2.20** | ease-out, then ease-in |
| 5 | 616–711 | 3.20 s | dissolve 616–621 | insert (document) | top-down | push + tilt-down tracking the chalk figure, slight drift back | whole: x1.28, dy −170. 616–676: x1.38 | linear |
| 6 | 712–856 | 4.83 s | **hard cut** | WS → MS group | low (ground) → eye | **locked-off** 712–745, crane-down/pull-back with tilt-up 746–801, truck right + push 802–856 | 712–745: x0.99, 0 px. 746–856: x0.61, dy +509, roll −15° | ease-in-out |
| 7 | 857–967 | 3.70 s | dissolve 857–864 | MS group → CU (back of head) | eye-level | near-static, then an exponential push-in onto Dex's head; a door is drawn and opens | 857–905: x1.07. 905–967: **x3.68**, dy −1017 | ease-in (exponential) |
| 8 | 968–1077 | 3.67 s | zoom-through door (961–971) | MS high → insert stack | high | fly-through the doorway, slow push + tilt-down onto the desk/stack | whole: x2.40, dy −589 (part of this is stack growth) | ease-out |
| 9 | 1078–1170 | 3.10 s | **match cut** (stack = flipbook) | MCU → MS group → insert | slightly low → high | pull-back reveal + tilt-up, then push + tilt-down into the flipbook | 1078–1146: **x0.56**, dy +594. 1147–1170: **x1.68**, dy −677 | ease-out / ease-in |
| 10 | 1171–1200 | 1.00 s | zoom-through into page (1153–1179) | WS drawn (bird's-eye) | high | push-in through the page edges onto the drawn tower top | x2.11, dy −640 | ease-out |

Cumulative scale curves (frame → scale since shot start), useful as keyframe targets:
- **Shot 1 final push (181–213):** 185 1.01 · 189 1.03 · 193 1.05 · 197 1.07 · **201 1.20 · 205 1.72 · 209 2.27** · 213 2.27. Almost flat, then a whip-zoom over 12 frames, then a hold.
- **Shot 4 (438–615):** 453 1.10 · 468 1.25 · 483 1.39 · 498 1.51 · 513 1.63 · 528 1.72 · 543 1.77 · 558 1.80 (easing out), then 573 1.91 · **588 2.73 · 603 3.33 · 615 3.96** (second push).
- **Shot 7 (857–967):** 877 1.01 · 897 1.05 · 917 1.12 · 937 1.23 · 947 1.40 · **957 1.92 · 967 3.93** (exponential "suction" into the head).
- **Shot 9 (1078–1170):** 1088 0.86 · 1098 0.60 · 1108 0.48 · 1118 0.42 · 1128 0.42 (hold) · 1138 0.47 · 1148 0.60 · 1158 0.71 · 1168 0.91.
- **Shot 10 (1171–1200):** 1176 1.29 · 1181 1.63 · 1186 1.91 · 1191 1.98 · 1200 2.11.

## 2. Recurring moves (the camera grammar of this channel)

1. **Continuous slow push-in on dialogue/explanation.** About **+15 %/s** image scale on the 2-shot (438–558: x1.80 over 4 s, easing out from ~+25 %/s to ~+5 %/s). A very slow variant of about **+4 %/s** is used for "hold" moments (lineup 857–905, porthole 289–330).
2. **Accelerating "suction" push = transition into a new world.** It always ends in a zoom-through: into the eye (181–213), the back of the head (905–967), the flipbook page (1147–1200). The scale curve is exponential: about 1.0→1.2 over the first ~2/3 of the move, then 1.2→2.3–3.9 in the last 8–12 frames.
3. **Zoom-through portals** (eye pupil → lens circle, drawn door on the head, page edges). The portal object grows past the frame edges and the new scene is already inside it.
4. **Orbit around a seated character** (brain room, 229–289) with a wide fisheye-like lens, combined with a crane-up to reveal windows.
5. **Bird's-eye → tilt-up + dolly** to establish a room (331–390), then a **dive to table level with rack focus** (397–402) for an insert gag.
6. **Locked-off "impact" frame** before a move: 712–745 holds still while Dex drops in, then the camera cranes away.
7. **Pull-back reveal** of the audience/setting (746–801, 1078–1146), often combined with a **truck** that follows walking characters (802–856).
8. **Roll** is used only for the free-fall (−55° over 7 s) to sell weightlessness.
9. **DOF/rack focus** marks an insert: toy cars (397–402) and the CHRONO-2 (565–615). In both the background goes to a heavy blur.
10. Cuts: 4 dissolves of 6–8 frames, 1 hard cut, 1 match cut. There are no whip pans.

## 3. Blender 5.x camera recipes (vertical 720x1280 / 1080x1920)

Common setup: Output 1080x1920 (or 720x1280), 30 fps. Camera Sensor Fit = **Vertical**, sensor 36 mm. Scene units in metres; characters are about 1.8 m tall (≈ 4.5 head-heights). Dolly target distance d_new = d_old / scale, or use focal length f_new = f_old × scale for a pure zoom (the video reads as a dolly because perspective changes, so prefer dolly).

### A. Slow dialogue push-in (shot 4, part 1)
- Lens 35 mm, camera at eye height 1.6 m, 6.0 m from the 2-shot. No DOF.
- Keys: f438 Y = −6.0 → f558 Y = −3.33 (= 6.0/1.80). Interpolation Bezier with an **ease-out** handle (fast start, gentle end). Optional Z −0.15 m drift (content dy −422 px = slight tilt-down).

### B. "Suction" push into an object (shots 1 end, 4 part 2, 7, 9 end)
- Lens 35–50 mm. Target = eye, device, or back of head.
- Keys for shot 7 (start 4.0 m from the head): f857 d 4.0 · f905 3.73 · f937 3.25 · f947 2.86 · f957 2.08 · f967 1.02 (that is 4.0/3.93). Use an exponential ease-in (F-curve "Exponential", ease In), or custom handles.
- Switch to the next scene on the frame where the portal fills the frame (door at f968). Animate the drawn door opening 961–968 (hinge rotation 0→−110°).
- For shot 4 part 2: lens 50 mm, f/2.0 DOF focused on the device, focus distance animated with the dolly. Background blur rises from 0 at f558 to max at f590. Add a red glow (Bloom/Glare node, threshold 0.8) from f598.

### C. Free-fall follow with roll (shot 1)
- Lens 24 mm (strong perspective on the lattice tower). Parent the camera to an Empty that falls with Dex (constant −Z velocity), so the ground recedes rather than approaches. The tower scrolls past via the Empty's translation.
- Roll: camera local Z rotation 0° at f1 → −26° at f30 → −58° at f180 (linear), then hold.
- Orbit off the edge (f1–30): Empty rotation X from 30° (high angle on the deck) to 90° (looking straight down the side), ease-in-out.
- Final push 181–213: dolly from 2.5 m to 1.1 m from Dex's face over f197–209 (ease-in), hold f209–213 on the eye.

### D. Orbit + crane (brain room, shot 2)
- Lens **16 mm** (fisheye feel; optionally Panoramic Fisheye Equisolid at 180° FOV, then crop).
- Pivot Empty at Noggin's head: Z rotation −40° → +60° over f229–289 (ease-in-out). Camera height 1.2 → 2.0 m, pitch +10° → +25° (looking up toward the portholes). Then a short push toward the porthole f289–330 (+6 %).

### E. Bird's-eye establish → table dive (shot 3)
- Lens 24 mm. f331: camera 6 m above the rug, pitch −90°. f390: pitch −35°, height 2.2 m, ease-in-out (the tilt-up shows the banner and ceiling).
- f390–402: dolly 3.0 m forward and drop to 0.3 m (table level), pitch 0°, **ease-in**. Rack focus f397–402 (focus 3 m → 0.4 m, f/1.8).
- f403–437: camera creeps +4 % while the physics/props play at about 10 % speed (slow-mo). Keep the camera moving so it doesn't read as frozen.

### F. Locked-off impact → crane reveal + truck (shot 6)
- Lens 28 mm, camera 0.5 m above ground at the net rail, static f712–745.
- f746–801: dolly back 1.6× and lower to 0.3 m while pitching up 10° (ease-in-out).
- f802–856: truck +X 2.5 m following the walkers, slight push-in (+18 %) then back (ease-in-out).

### G. Pull-back reveal → push into a prop (shot 9)
- Lens 35 mm. f1078 camera 1.0 m from the flipbook (MCU of Dex holding it) → f1118 2.4 m (= 1/0.42), ease-out, slight tilt-up 5°. Hold f1118–1130.
- f1147–1170: dolly back toward the flipbook with a pitch down of 25°, ease-in. Hand off to shot 10 (a 2D page plate) on the frame where the page fills the screen.

### H. Zoom into a drawn plate (shot 10, 2D)
- Easier in After Effects or Blender's 2D compositor: scale the page plate 100 → 211 % over 30 frames, ease-out (most growth in the first 15 frames: 129 % at +5 f, 163 % at +10 f). Add 3 frames of "line boil" (wiggle displacement 2 px, 12 fps, posterised) at 1180–1182.

## 4. Practical rules

- Never hold a shot fully static for more than about 1 s. A default creep of +4 %/s is the baseline.
- A transition into a new location is a **push-through a portal** or a **6–8-frame dissolve**. Hard cuts are reserved for impact (the landing, f712).
- Pushes into a prop sync to its "reveal" word (the device's all-LEDs-on at #569 on "way"; the PANIC slam #981 on "frightened").
- A zoom-through gets one new world per explanation beat: eye → brain room (claim), head door → brain room (explanation), page → drawn opening (loop).
