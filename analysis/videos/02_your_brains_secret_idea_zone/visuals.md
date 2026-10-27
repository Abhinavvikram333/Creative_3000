# Visual analysis — 02 "Your Brain's Secret Idea Zone"

## STYLE LOCK (reuse verbatim in every prompt for this series/video)

```
Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
```

## 1. Art style

| Layer | Look | Evidence (frames) | Most likely made with |
|---|---|---|---|
| **Characters** (Theo, Edison) | Flat 2D cartoon. Round head; **dark-brown uniform outline** of about 7–8 px at 720 wide; flat fill with a soft gradient sheen (a lighter vertical band on the navy torso, a lighter top on the head); separate flat hair cap with 2–4 strand lines; stick limbs with no outline variation. | #45, #100, #160, #1141 | Drawn 2D art (vector or AI image cleaned to flat colour) used as **cut-out puppet layers**. The faces are **swapped sprites**: the eyes/brows/mouth change in one frame with no in-betweens (#81, #94, #199, #405, #1019) |
| Faces | Eyes are dots, hollow circles with dots (shock), closed arcs (happy), flat lines (deadpan/asleep) or half-lid dots (smug/drowsy). Brows are short thick tapered strokes. Mouths: dash, side smile, "~" wavy (worry), toothy grin (white teeth in a black shape), small "o" (sleep). | emotions library | 2D face-sprite library; the same set is used for Theo and Edison |
| **Realistic eye insert** | Glossy, photographic-detail blue irises in the cartoon face. | #816–854 | AI image or a painted/3D eye texture composited onto the face; this is a one-off stylistic "break" for the keyword |
| **Environments** | Semi-realistic, warmly lit, detailed 3D-looking interiors: wood grain, panelling, glossy chrome balls with reflections, a brass gramophone horn, bokeh practicals. Thin dark contour lines appear on the props (chair, stools), so the props sit between the toon world and render. | #45, #660, #960 | **3D render (Blender/Cycles-like) or AI image** for the plates; props such as the chair/stools/balls behave like real 3D in the S4 orbit (#541–566 parallax). |
| Diagrams | Clean graphic overlays: white bold caps labels, dashed wave lines, an EEG line with glow, a depth ruler. | #746–790 | Vector shape layers (AE or code) over a painted water plate |
| Corkboard | Photo-real cork texture, cream paper cards with black line icons, red pins, animated red strings. | #863–946 | AI/photo cork plate + vector cards + animated stroke paths (AE trim paths) |

**2D vs 2.5D vs 3D.**
- Characters are 2D layers with a small 3D turn: S4 shows the same character from the side and then 3/4 front, with a different drawing hidden under the scan line.
- Backgrounds are rendered or painted 3D-looking stills, moved with a virtual camera:
  - zoom/pan/crane: S1, S2, S5, S9;
  - true parallax with set pieces: the S4 orbit and the S1 crane, where the stools shift relative to each other.
- The pipeline that best fits this is **3D set (or AI plate with depth) + 2D character cards + a camera in Blender or AE 3D**.

## 2. Lighting moods

| Mood | Shots | Description |
|---|---|---|
| Warm spotlight stage | S1, S2, S3, S9 | One bare bulb with a visible volumetric cone. The dark green walls fall to near-black, and the warm pool of light is on the ring rug and chair. |
| Dark X-ray stage | S4 | The same set, darker. The X-ray character glows cyan/blue against the dark. Normal warm light returns at the end. |
| Golden lab | S5 | Amber tungsten, many bokeh practicals, floating dust sparkles, strong warm grade (saturation 0.70, the highest in the video). |
| Underwater diagram | S6 | Teal water with god-rays above a violet glow band and a navy-black deep zone; caustic net on the character. |
| Corkboard | S7 | Bright, even warm light (brightness 0.63, the brightest section). |
| Elevator | S8 | Warm wood interior with a purple practical spill from the doorway. While "at DEEP SLEEP" the whole frame is graded blue-lavender (#983–1044). |

## 3. Depth / parallax layers

- **Stage**: far = green panelled wall, oval portrait, light switch; mid = stools ring, bulb + cone; near = chair, character, plates, ring rug (a strong floor plane for crane moves).
- **Lab**: far = MENLO PARK sign, organ pipes, windows; mid = bottle shelves, gramophone; near = stools, chair, Edison, floor planks; FX layer = floating dust.
- **Depth chart**: an air strip (bokeh), the water surface line, the water column with rays, the violet band, the deep zone; the ruler, labels and EEG overlays sit on top.
- **Elevator**: near = car interior (walls, carpet, chair, Theo); mid = door frame + scissor gate (foreground matte); far = a **scrolling floor strip** behind the doorway (HYPNAGOGIA floor, brick fascia, black shaft), animated vertically.

## 4. VFX inventory

| VFX | Frames | Look | Build |
|---|---|---|---|
| 4-point star glint | 238–249, 269–280, 1149–1162 | White 4-point sparkle on the steel balls, 10–15 frames each | Sprite or AE shape, scale-in/out |
| Eyelid vignette | 331–369 | Near-black bands with feathered curved edges closing from the top and bottom | Two animated masks with high feather |
| X-ray scan line | 373–383 (down), 555–564 (up) | Bright cyan horizontal line with glow and a soft trailing band; reveals the other layer | Linear wipe (track matte) + glow line |
| Nerve wire plugged / unplugged | 384–404 / 405–536 / 537+ | Double pale-yellow glowing line vs a dull mauve zigzag | Shape layer paths swapped (no tween) |
| Impact / sound arcs | 484–534, 1017–1047 | Thin white semicircle arcs expanding and fading | Shape layer rings, scale + opacity |
| Vibration lines | 550–554, 583–616 | Short faint parallel arcs beside the head | Shape layer, jitter |
| Sweat drop | 1030–1063 | Small pale-blue teardrop with an outline on the forehead | Sprite on the face rig |
| Water caustics + bubbles | 718–862 | White wavy caustic network crawling over the character, bubbles rising | AE "Caustics"/fractal noise as an overlay, or Blender shader |
| EEG trace draw-on | 751–772 | Mint line with glow drawn top→down | Trim-path stroke |
| Zoom-through tear | 855–862 | Face layer breaks into fragments; pupil tears open with paper edges | Shatter + torn alpha matte |
| String draw-on | 866–906 | Red string grows pin to pin, 4–5 frames each | Trim paths |
| Card merge pop | 908–912 | Two cards overlap, ghost, scale overshoot into the new card | Dissolve + scale keyframes (overshoot) |
| Floor scroll + motion blur | 961–990, 1031–1057 | Vertical blur streaks on the floors passing the door | 2D layer translate with motion blur |
| Colour grade shift | 983–1046 | Blue-lavender grade on the whole elevator interior | Adjustment layer, colour balance keyed |
| Floating dust / bokeh | 620–715 | Warm specks drifting | Particle layer |
| Morph dissolve | 617–622 | Theo → Edison in identical framing | Simple cross-dissolve (identical pose/framing makes it read as a morph) |

## 5. Captions

- **Font look**: heavy rounded geometric sans, white fill, about 4 px black outline plus a soft dark drop shadow. It looks like "Montserrat ExtraBold" / "Poppins Bold". Lower-case as spoken, punctuation kept ("a genius,", "awake.").
- **Size**: cap height about 26–30 px at 720×1280 (≈ 42–46 px font); the longest card ("into the plates") is about 280 px wide.
- **Position**: horizontally centred; baseline at about y ≈ 900 px (≈ 70 % of frame height), over the torso. It stays fixed while the camera moves (screen-space).
- **Animation**: hard cut word-to-word, synced to the voice. No pop or scale. 1–3 words per card, average 10.3 frames.
- **In-scene text** (diegetic):
  - white bold caps diagram labels (AWAKE, LIGHT SLEEP, BRAIN WAVES, "? ? ?");
  - the lavender "DEEP SLEEP" label;
  - the "HYPNAGOGIA" title card (heavy caps, lavender fill, navy outline, underline);
  - the corkboard card labels (black caps under a thin rule);
  - the signs MENLO PARK : LABORATORY (gold serif caps) and HYPNAGOGIA / DEEP SLEEP (white caps on the walls);
  - the red italic handwriting "MAGNET CAR!" on the notepad.

## 6. Transitions

- 7 **cross-dissolves**, 4–8 frames each (117–122, 317–324, 370–374, 617–622 morph, 716–720, 943–949 match, 1090–1094).
- 1 **zoom-through** (855–863).
- Internal "scene changes" without a cut:
  - X-ray scan-line wipes;
  - the elevator floor scrolling past the door.
- No hard cuts at all.
