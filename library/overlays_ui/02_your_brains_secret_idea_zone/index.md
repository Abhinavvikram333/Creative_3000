# Overlays / UI and VFX — 02_your_brains_secret_idea_zone

## `ov_caption_word`  (overlay_ui)
- Crop: `ov_caption_word_f00100.jpg` (frame 100)
- Description: Word caption: heavy rounded sans (Montserrat ExtraBold / Poppins Bold look), white fill, black outline about 4 px plus a soft shadow, centred, baseline y≈900, 1–3 words, hard-cut per word.
- How to build: Code / AE text layer driven by word timings. Not an image.
- Frames: 1–1172
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/ov_caption_word_f00100.jpg
[SUBJECT] Word caption: heavy rounded sans (Montserrat ExtraBold / Poppins Bold look), white fill, black outline about 4 px plus a soft shadow, centred, baseline y≈900, 1–3 words, hard-cut per word.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `ov_hypnagogia_title`  (overlay_ui)
- Crop: `ov_hypnagogia_title_f00830.jpg` (frame 830)
- Description: Keyword title card 'HYPNAGOGIA': heavy geometric caps, pale lavender fill #dddaf3, dark navy outline #212b4b, soft shadow, thin underline; fades in 6 frames and out 3 frames.
- How to build: AE text layer with stroke + drop shadow; opacity keys 816–822 in, 850–853 out.
- Frames: 816–853
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/ov_hypnagogia_title_f00830.jpg
[SUBJECT] Keyword title card 'HYPNAGOGIA': heavy geometric caps, pale lavender fill #dddaf3, dark navy outline #212b4b, soft shadow, thin underline; fades in 6 frames and out 3 frames.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `ov_eeg_trace`  (overlay_ui)
- Crop: `ov_eeg_trace_f00765.jpg` (frame 765)
- Description: Mint EEG line (#a2e7df) with a soft glow, drawn top→down: tight zigzag, a spiky burst inside the violet band, then slow big waves. Includes the tiny 'BRAIN WAVES' label.
- How to build: Shape path + trim paths 0→100 % over 18 frames; glow effect.
- Frames: 747–789
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/ov_eeg_trace_f00765.jpg
[SUBJECT] Mint EEG line (#a2e7df) with a soft glow, drawn top→down: tight zigzag, a spiky burst inside the violet band, then slow big waves. Includes the tiny 'BRAIN WAVES' label.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_sparkle_glint`  (vfx)
- Crop: `vfx_sparkle_glint_f00240.jpg` (frame 240)
- Description: A white 4-point star glint on chrome balls; scale 0→1→0 over 10–15 frames.
- How to build: Sprite / shape star with glow.
- Frames: 238–249, 269–280, 1149–1162
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_sparkle_glint_f00240.jpg
[SUBJECT] A white 4-point star glint on chrome balls; scale 0→1→0 over 10–15 frames.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_impact_arcs`  (vfx)
- Crop: `vfx_impact_arcs_f00500.jpg` (frame 500)
- Description: Thin white semicircle arcs above the plate, spawning every 2–3 frames and expanding/fading (the ball smash sound).
- How to build: AE ellipse strokes, scale 0→300 %, opacity 100→0, stagger 3 frames.
- Frames: 484–534
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_impact_arcs_f00500.jpg
[SUBJECT] Thin white semicircle arcs above the plate, spawning every 2–3 frames and expanding/fading (the ball smash sound).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_impact_arcs_double`  (vfx)
- Crop: `vfx_impact_arcs_double_f01030.jpg` (frame 1030)
- Description: The same arcs, doubled over both plates on the elevator crash.
- How to build: As above, two emitters.
- Frames: 1017–1047
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_impact_arcs_double_f01030.jpg
[SUBJECT] The same arcs, doubled over both plates on the elevator crash.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_scanline`  (vfx)
- Crop: `vfx_scanline_f00378.jpg` (frame 378)
- Description: X-ray scan line: a bright cyan horizontal line with glow sweeping vertically and revealing the X-ray layer above it (down at #373–383, up at #555–564).
- How to build: Linear wipe track matte + glowing solid line, 10 frames per sweep.
- Frames: 373–383, 555–564
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_scanline_f00378.jpg
[SUBJECT] X-ray scan line: a bright cyan horizontal line with glow sweeping vertically and revealing the X-ray layer above it (down at #373–383, up at #555–564).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_eyelid_vignette`  (vfx)
- Crop: `vfx_eyelid_vignette_f00355.jpg` (frame 355)
- Description: POV eyelids: near-black bands with feathered curved edges closing from the top and bottom (close, reopen a bit, close).
- How to build: Two masked solids, feather about 40 px, keyed position.
- Frames: 331–369
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_eyelid_vignette_f00355.jpg
[SUBJECT] POV eyelids: near-black bands with feathered curved edges closing from the top and bottom (close, reopen a bit, close).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_iris_zoom_through`  (vfx)
- Crop: `vfx_iris_zoom_through_f00861.jpg` (frame 861)
- Description: Zoom-through into the pupil: the face tears into fragments, the iris fills the frame, the pupil opens with torn-paper edges onto the next scene.
- How to build: Exponential scale + shatter + torn-paper alpha matte.
- Frames: 855–862
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_iris_zoom_through_f00861.jpg
[SUBJECT] Zoom-through into the pupil: the face tears into fragments, the iris fills the frame, the pupil opens with torn-paper edges onto the next scene.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_card_merge`  (vfx)
- Crop: `vfx_card_merge_f00911.jpg` (frame 911)
- Description: Two idea cards slide together, overlap with a ghost and pop into a bigger new card with a slight overshoot.
- How to build: Position keys + cross-fade + scale overshoot (110 %→100 %).
- Frames: 902–912
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_card_merge_f00911.jpg
[SUBJECT] Two idea cards slide together, overlap with a ghost and pop into a bigger new card with a slight overshoot.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_floor_scroll_blur`  (vfx)
- Crop: `vfx_floor_scroll_blur_f01053.jpg` (frame 1053)
- Description: Floors scrolling past the elevator door with vertical motion-blur streaks.
- How to build: Tall 2D strip translated in Y behind the door matte, with motion blur.
- Frames: 961–990, 1031–1057
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_floor_scroll_blur_f01053.jpg
[SUBJECT] Floors scrolling past the elevator door with vertical motion-blur streaks.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_sweat_drop`  (vfx)
- Crop: `vfx_sweat_drop_f01048.jpg` (frame 1048)
- Description: A pale-blue teardrop sweat drop with a dark outline on the forehead.
- How to build: Face-rig sprite; fades out after about 30 frames.
- Frames: 1030–1063
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_sweat_drop_f01048.jpg
[SUBJECT] A pale-blue teardrop sweat drop with a dark outline on the forehead.
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_vibration_lines`  (vfx)
- Crop: `vfx_vibration_lines_f00590.jpg` (frame 590)
- Description: Faint short parallel arcs beside the head (shaken/annoyed).
- How to build: Shape layer with wiggle.
- Frames: 550–554, 583–616
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_vibration_lines_f00590.jpg
[SUBJECT] Faint short parallel arcs beside the head (shaken/annoyed).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_water_caustics_bubbles`  (vfx)
- Crop: `vfx_water_caustics_bubbles_f00830.jpg` (frame 830)
- Description: An animated white caustic network over the character plus rising bubbles (underwater).
- How to build: AE CC Caustics / fractal noise in overlay mode, or a Blender shader; bubble particles.
- Frames: 718–862
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_water_caustics_bubbles_f00830.jpg
[SUBJECT] An animated white caustic network over the character plus rising bubbles (underwater).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_cross_dissolve_ghost`  (vfx)
- Crop: `vfx_cross_dissolve_ghost_f01092.jpg` (frame 1092)
- Description: The signature 4–8 frame cross-dissolve with the incoming shot slightly zoomed (ghost layering).
- How to build: Opacity cross-fade over 5–6 frames with a 102–105 % scale settle.
- Frames: 117–122, 317–324, 370–374, 617–622, 716–720, 943–949, 1090–1094
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_cross_dissolve_ghost_f01092.jpg
[SUBJECT] The signature 4–8 frame cross-dissolve with the incoming shot slightly zoomed (ghost layering).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_unplugged_wire`  (vfx)
- Crop: `vfx_unplugged_wire_f00420.jpg` (frame 420)
- Description: The nerve wire in its unplugged state: a dull mauve-grey zigzag hanging from the plug tag (vs. the glowing straight pale-yellow double line when plugged).
- How to build: Two shape-path versions swapped on one frame (#405, #537).
- Frames: 384–560
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_unplugged_wire_f00420.jpg
[SUBJECT] The nerve wire in its unplugged state: a dull mauve-grey zigzag hanging from the plug tag (vs. the glowing straight pale-yellow double line when plugged).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

## `vfx_red_string_draw`  (vfx)
- Crop: `vfx_red_string_draw_f00870.jpg` (frame 870)
- Description: Red string drawing from one pushpin to another (4–5 frames per string).
- How to build: Stroke path + trim paths; a slight sag curve.
- Frames: 866–906
- Prompt (only if it is generated as an image; most of these are better built as shape layers):
```
[REFERENCE] attach: library/overlays_ui/02_your_brains_secret_idea_zone/vfx_red_string_draw_f00870.jpg
[SUBJECT] Red string drawing from one pushpin to another (4–5 frames per string).
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] n/a, self-lit / flat
[BACKGROUND] transparent
[AVOID] watermark, background scenery, characters
```

