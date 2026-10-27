# Overlays, UI and VFX: video 04 (04_the_scientists_insane_time_test)

## ov_caption_style
- Crop: `ov_caption_style_f00160.jpg`, frame 160, bbox (190,860,340,90)
- Description: Word caption "Apparently,"
- How to build: Code (ASS/Remotion): heavy rounded sans (Montserrat Black / Poppins ExtraBold), white #f1ebe6, 4–5 px black #0f0909 stroke + soft shadow, cap height 45 px at 720p, centre y≈900, 1 word/card, hard swap, 117 cards

(Build in code/AE; no image prompt needed.)

## ov_sweat_drops
- Crop: `ov_sweat_drops_f00190.jpg`, frame 190, bbox (330,0,220,160)
- Description: Pale blue/white teardrops with dark outline and highlight, streaming upward during the fall
- How to build: Sprite + particle emitter (upward velocity during the fall; at the temple for Noggin/Amy/Elmer)

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_sweat_drops_f00190.jpg
[SUBJECT] Pale blue/white teardrops with dark outline and highlight, streaming upward during the fall
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_speed_lines_blueprint
- Crop: `ov_speed_lines_blueprint_f00640.jpg`, frame 640, bbox (200,540,260,360)
- Description: Chalk-white short vertical speed lines above the falling stick figure
- How to build: AE shape layers with a chalk texture

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_speed_lines_blueprint_f00640.jpg
[SUBJECT] Chalk-white short vertical speed lines above the falling stick figure
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_red_alarm_tint
- Crop: `ov_red_alarm_tint_f01000.jpg`, frame 1000, bbox full frame
- Description: Red emergency overlay with light rays from upper-left
- How to build: AE adjustment layer: Fill #d3361f in Multiply at ~55 % plus a soft-light ray layer; 4-frame ramp in (982–986) and out (1066–1069)

(Build in code/AE; no image prompt needed.)

## ov_pupil_zoom
- Crop: `ov_pupil_zoom_f00218.jpg`, frame 218, bbox (60,340,600,580)
- Description: Dex's ring eye in ECU; the pupil is a tiny Noggin
- How to build: Scale-up of the eye sprite + nested pupil comp

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_pupil_zoom_f00218.jpg
[SUBJECT] Dex's ring eye in ECU; the pupil is a tiny Noggin
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_lens_reveal
- Crop: `ov_lens_reveal_f00225.jpg`, frame 225, bbox (0,280,720,760)
- Description: Circular glass lens with a specular arc and a dark rim, revealing the brain room inside, expanding to full frame (224–228)
- How to build: AE: circle mask on the new scene, scale 30→250 % over 5 frames, white highlight arc shape

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_lens_reveal_f00225.jpg
[SUBJECT] Circular glass lens with a specular arc and a dark rim, revealing the brain room inside, expanding to full frame (224–228)
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_door_drawn_on_head
- Crop: `ov_door_drawn_on_head_f00960.jpg`, frame 960, bbox (150,320,440,520)
- Description: Black-outlined arched white door with grey hinges and a gold knob, drawn onto the back of Dex's white head
- How to build: AE trim-path stroke draw-on 957–960

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_door_drawn_on_head_f00960.jpg
[SUBJECT] Black-outlined arched white door with grey hinges and a gold knob, drawn onto the back of Dex's white head
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_door_open
- Crop: `ov_door_open_f00964.jpg`, frame 964, bbox (130,320,460,540)
- Description: The door swinging open on its left hinge, the brain room visible inside
- How to build: AE 3D layer Y-rotation 0→−110° over 961–968 + new scene behind a mask

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_door_open_f00964.jpg
[SUBJECT] The door swinging open on its left hinge, the brain room visible inside
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_detail_callout_check
- Crop: `ov_detail_callout_check_f00685.jpg`, frame 685, bbox (360,440,360,460)
- Description: Chalk callout: line from the wrist to a circle labelled "DETAIL A: DISPLAY" containing red dot-matrix "47" and a checkmark
- How to build: AE: trim-path line (668–669), circle scale (670–672), digits fade (673–675), check draw-on (681–683)

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_detail_callout_check_f00685.jpg
[SUBJECT] Chalk callout: line from the wrist to a circle labelled "DETAIL A: DISPLAY" containing red dot-matrix "47" and a checkmark
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_crash_sparkles
- Crop: `ov_crash_sparkles_f00415.jpg`, frame 415, bbox (220,620,160,220)
- Description: White 4-point sparkle stars + pink dust puffs drifting slowly
- How to build: Particle sprites at 10 % speed

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_crash_sparkles_f00415.jpg
[SUBJECT] White 4-point sparkle stars + pink dust puffs drifting slowly
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_motion_blur_smear
- Crop: `ov_motion_blur_smear_f00722.jpg`, frame 722, bbox (220,290,300,300)
- Description: Heavy vertical motion smear of the falling Dex into the net
- How to build: Directional blur / CC Force Motion Blur on the falling sprite

(Build in code/AE; no image prompt needed.)

## ov_shake_lines
- Crop: `ov_shake_lines_f01190.jpg`, frame 1190, bbox (420,60,200,180)
- Description: Three short curved ink strokes next to the head (fear tremble)
- How to build: Drawn sprite

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_shake_lines_f01190.jpg
[SUBJECT] Three short curved ink strokes next to the head (fear tremble)
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_paper_flutter
- Crop: `ov_paper_flutter_f01165.jpg`, frame 1165, bbox (0,0,720,600)
- Description: Flipbook pages flipping past camera as cream curved strips
- How to build: Blender page-flip rig or AE CC Page Turn, 1 page/frame

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_paper_flutter_f01165.jpg
[SUBJECT] Flipbook pages flipping past camera as cream curved strips
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_rubber_band_snap
- Crop: `ov_rubber_band_snap_f01066.jpg`, frame 1066, bbox (0,440,720,420)
- Description: Red rubber band snapping around the stack (1 frame stretched diagonal, then tight)
- How to build: Shape layer: 1-frame stretched polygon → tight band

```
[REFERENCE] attach: library/overlays_ui/04_the_scientists_insane_time_test/ov_rubber_band_snap_f01066.jpg
[SUBJECT] Red rubber band snapping around the stack (1 frame stretched diagonal, then tight)
[POSE / EMOTION / STATE] Isolated overlay element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024
[LIGHTING] Flat
[BACKGROUND] transparent
[AVOID] background scene, characters, captions, watermark
```

## ov_crossfade
- Crop: `ov_crossfade_f00618.jpg`, frame 618, bbox full frame
- Description: Example of the 6-frame dissolve (CHRONO-2 → blueprint)
- How to build: Editor crossfade, 6–8 frames linear

(Build in code/AE; no image prompt needed.)

## ov_led_glow_dof
- Crop: `ov_led_glow_dof_f00605.jpg`, frame 605, bbox (60,60,600,1100)
- Description: Red LED bloom + strong background DOF blur on the CHRONO-2 ECU
- How to build: Glow (threshold red) + camera lens blur

(Build in code/AE; no image prompt needed.)

