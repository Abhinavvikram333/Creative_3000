# Overlays / UI / VFX — 01_this_tree_hates_you

Exact on-screen text is quoted. Fonts: captions = heavy geometric sans (Montserrat ExtraBold-like) white + black stroke;
UI = Poppins/Inter SemiBold-like. For UI, generate only the graphic base (no text) and set the text in AE/code.

## radar_screen — Satellite storm radar app (overlay_ui)
- **Crop:** `radar_screen_f00485.jpg (+ radar_header_f00485.jpg, severe_storm_pill_f00485.jpg)`
- **Description / text:** Dark navy ocean map, dark-green island silhouette, 'YOU' marker (red dot in a white ring + tiny white label), faint concentric range rings, white sweep line rotating clockwise (~0.5 rev/s), white-lavender satellite cloud band drifting right, coloured precipitation echoes (green→yellow→orange→magenta) revealed behind the sweep. Header: 'SATELLITE · LIVE' (teal #7fd8c8 tiny caps, letter-spaced) and 'NIGHT 1 · 9:42 PM' (white bold geometric sans). Bottom pill (#e01436): '⚠ SEVERE STORM' (white bold, yellow triangle) fades in #478.
- **Frames:** [[458, 515]]
- **How to build:** Build in AE/code: map image as an AI plate (no text), sweep = rotating shape layer + radial wipe mask revealing a precipitation layer, clouds = fractal-noise layer panning right, text layers in Poppins SemiBold, pill = rounded rectangle with an opacity fade.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/radar_screen_f00485.jpg
[SUBJECT] satellite-style map at night: dark navy ocean, a small dark-green island silhouette in the centre, faint concentric radar range rings, a soft white-lavender cloud band sweeping in from the left
[POSE / EMOTION / STATE] no text (add UI text in compositing)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] full scene
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## xray_screen — X-ray HUD with Kai's skeleton (overlay_ui)
- **Crop:** `xray_screen_f01250.jpg (+ xray_header_f01250.jpg, xray_gut_header_f01280.jpg, xray_skeleton_legs_f01280.jpg)`
- **Description / text:** Glowing cyan cartoon skeleton of Kai (round skull with big sockets + teeth grid, ribcage, pelvis, stick bones), translucent pink oesophagus/stomach/intestines, yellow-orange fire spark travelling down; dark teal-navy background. HUD: 'X-RAY' (#96d9e2, top-left), 'THROAT: ON FIRE' (orange #e8643c, top-right) → 'GUT: INCOMING' (amber) at #1260, 'R' marker, corner brackets, ruler ticks right, 'PATIENT: YOU' / 'AP VIEW · 1:1' bottom-left; legs cross knock-kneed with 3 yellow shake ticks each side 1267–1293.
- **Frames:** [[1222, 1295]]
- **How to build:** Skeleton = AI image or vector drawing; HUD = AE text + shape layers; fire spark = glow sprite on a motion path; label swap = a hard text change.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/xray_screen_f01250.jpg
[SUBJECT] cartoon x-ray of a stick-figure character with a huge round skull: glowing cyan bones (big round eye sockets, grid of teeth, simple ribcage, pelvis, thin stick limb bones), translucent pink oesophagus, stomach and intestines, on a dark teal-navy background
[POSE / EMOTION / STATE] no text (HUD text added in compositing)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] full scene
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## thermal_screen — Thermal camera HUD with lungs (overlay_ui)
- **Crop:** `thermal_screen_f01900.jpg (+ thermal_header_f01900.jpg)`
- **Description / text:** Kai front view; torso replaced by a thermal-palette view of lungs/trachea (magenta→orange→yellow as the temperature climbs). HUD: 'THERMAL' (golden #dbc87a, top-left), 'LUNGS: 99°F' → counts up to '451°F' (white, top-right; counter 1883–1902), '● REC' red dot blinking, corner brackets, vertical scale bar (white-yellow-orange-magenta-purple) with '500°F' / '60°F', crosshair + temperature tag on the right lung. A horizontal scan line wipes down 1868–1876.
- **Frames:** [[1868, 1949]]
- **How to build:** AE: Kai puppet + lungs illustration with a Colorama/gradient-map driven by a slider; the counter is a text expression linked to the same slider (ease-in curve 99→451 over 20 frames); scan line = masked wipe.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/thermal_screen_f01900.jpg
[SUBJECT] cartoon thermal-camera view of a torso: lungs, trachea and bronchi rendered in a thermal heat palette (yellow-white hot core, orange, magenta edges, purple background tissue), speckled heat texture
[POSE / EMOTION / STATE] no text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] full scene
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## red_x_trunk — Red spray-painted X (overlay_ui)
- **Crop:** `red_x_trunk_f00400.jpg`
- **Description / text:** Bright red (#e22924) spray-paint X with drips, on the trunk. The motif reappears as clean red X marks on the log ends (red_x_marks_logs_f01680.jpg, #cf2627, 1644–1867).
- **Frames:** [[226, 1867]]
- **How to build:** Image/vector sprite; for the log cascade, a scale-pop 0→120→100 % in 3 frames, staggered every ~2 frames.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/red_x_trunk_f00400.jpg
[SUBJECT] a bright red spray-painted X with paint drips running down
[POSE / EMOTION / STATE] no text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## milky_sap_label — 'MILKY SAP' callout (overlay_ui)
- **Crop:** `milky_sap_label_f00680.jpg`
- **Description / text:** White bold caps 'MILKY SAP' with a thin white leader line to a glossy sap bead.
- **Frames:** [[671, 704]]
- **How to build:** AE text + line shape layer, 3-frame fade in/out.

## skin_cutaway_window — Cut-away window (overlay_ui)
- **Crop:** `skin_cutaway_window_f00764.jpg`
- **Description / text:** A small rectangle with a thick dark outline opens in the splat on the head and shows skin cells, then scales up to fill the frame.
- **Frames:** [[760, 770]]
- **How to build:** AE: precomp of the skin insert inside a masked, stroked rectangle; scale 15→100 % over 6–10 frames (ease in).

## caption_sample — Caption style (overlay_ui)
- **Crop:** `caption_sample_f00400.jpg`
- **Description / text:** White heavy geometric sans (Montserrat ExtraBold-like) with a ~3–4 px black stroke, centred at y≈900, 1–2 words per card, hard cuts.
- **Frames:** [[2, 2043]]
- **How to build:** Auto-caption tool or AE text with word timings.

## sweat_drop — Sweat drop (vfx)
- **Crop:** `sweat_drop_f01805.jpg`
- **Description / text:** Blue teardrop (#6488aa) with a dark outline and a white highlight at the upper right of the head.
- **Frames:** [[421, 456], [546, 610], [723, 763], [1150, 1170], [1425, 1510], [1797, 1949]]
- **How to build:** Sprite on the face layer.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/sweat_drop_f01805.jpg
[SUBJECT] a single cartoon sweat drop: light-blue teardrop with a bold dark outline and a white highlight
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## tear_streams — Tear streams (vfx)
- **Crop:** `tear_streams_f01805.jpg`
- **Description / text:** Two thick light-blue wavy ribbons running from the eyes down the cheeks.
- **Frames:** [[1171, 1221], [1756, 1822], [1869, 1949]]
- **How to build:** Sprite with a 2-frame wobble loop.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/tear_streams_f01805.jpg
[SUBJECT] two thick light-blue cartoon tear streams flowing straight down, wavy edges, thin dark outline
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## bloodshot_eyes — Bloodshot eyes (vfx)
- **Crop:** `bloodshot_eyes_f01805.jpg`
- **Description / text:** Ring eyes with pink-red whites, red vein ticks and dark pupils; red lower lids.
- **Frames:** [[1801, 1920]]
- **How to build:** Face-part sprite.

## steam_columns — Steam columns (vfx)
- **Crop:** `steam_columns_f01190.jpg`
- **Description / text:** White cartoon puff clouds rising in columns from both sides of a red head.
- **Frames:** [[1177, 1221]]
- **How to build:** Puff sprites rising and scaling (particle emitter).

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/steam_columns_f01190.jpg
[SUBJECT] white cartoon steam puff clouds stacked into a rising column, thin grey outline
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## sizzle_smoke — Sizzle smoke puffs + splat (vfx)
- **Crop:** `sizzle_smoke_f00740.jpg`
- **Description / text:** Small white puffs + tiny bubbles rising from a white splat.
- **Frames:** [[735, 763], [815, 845], [1462, 1477], [1516, 1525]]
- **How to build:** Puff sprite sequence.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/sizzle_smoke_f00740.jpg
[SUBJECT] small white cartoon smoke puffs with tiny round bubbles rising
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## sap_splat — Milky sap splat (vfx)
- **Crop:** `sap_splat_f00736.jpg`
- **Description / text:** Flat white irregular splat with a dark outline on top of the head, dotted drops around it.
- **Frames:** [[734, 763]]
- **How to build:** Sprite.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/sap_splat_f00736.jpg
[SUBJECT] a flat white irregular liquid splat with a dark outline and small droplets around it
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## anger_vein — Anger vein (vfx)
- **Crop:** `anger_vein_f00935.jpg`
- **Description / text:** Red anime 'cross-popping vein' mark.
- **Frames:** [[908, 944]]
- **How to build:** Sprite, 2-frame fade-out.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/anger_vein_f00935.jpg
[SUBJECT] a red anime anger-vein symbol (four curved strokes forming a cross)
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## blisters — Blisters (vfx)
- **Crop:** `blisters_f00830.jpg`
- **Description / text:** Pink glossy balls with dark outlines dotted over the head.
- **Frames:** [[815, 859], [1457, 1477]]
- **How to build:** Sprites popped on one by one.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/blisters_f00830.jpg
[SUBJECT] small glossy pink round blisters with thin dark outlines and white highlights
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## frost_marks — Frost marks (vfx)
- **Crop:** `frost_marks_f01660.jpg`
- **Description / text:** Small pale-blue zigzag icicle marks on the forehead.
- **Frames:** [[1560, 1718]]
- **How to build:** Sprite.

## heat_fill_head — Rising red heat fill (vfx)
- **Crop:** `heat_fill_head_f01165.jpg`
- **Description / text:** Red-pink liquid level with a wavy top rising inside the head, ending fully red.
- **Frames:** [[1160, 1221]]
- **How to build:** Masked solid with an animated wavy edge, then a fill colour swap.

## scent_wisp — Scent wisp (vfx)
- **Crop:** `scent_wisp_f01040.jpg`
- **Description / text:** Glowing green-white wavy line with sparkles curling from the tree to Kai's nose.
- **Frames:** [[1014, 1057]]
- **How to build:** Trim-path stroke + glow + sparkle particles.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/scent_wisp_f01040.jpg
[SUBJECT] a glowing pale-green wavy aroma trail with small white four-point sparkles
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## light_orbs — Soft light orbs (vfx)
- **Crop:** `light_orbs_f01100.jpg`
- **Description / text:** Soft white bokeh orbs floating up.
- **Frames:** [[1098, 1126]]
- **How to build:** Particles with blur.

## lightning_rain — Rain + lightning flash (vfx)
- **Crop:** `lightning_rain_f00576.jpg`
- **Description / text:** White diagonal rain streaks; 2–3 frame lightning flashes (bolt + exposure lift).
- **Frames:** [[515, 610], [575, 577], [835, 838]]
- **How to build:** Particle rain + a bolt sprite + an exposure keyframe.

## toxic_smoke_cloud — Toxic smoke cloud (vfx)
- **Crop:** `toxic_smoke_cloud_f01780.jpg`
- **Description / text:** Dark grey-brown volumetric smoke billowing up from the fire over the tree and Kai.
- **Frames:** [[1711, 1795]]
- **How to build:** Stock smoke element or an AI-generated smoke loop, screen/multiply over the plate.

- **Prompt (graphic base):**

```
[REFERENCE] attach: library/overlays_ui/01_this_tree_hates_you/toxic_smoke_cloud_f01780.jpg
[SUBJECT] dark grey-brown billowing smoke cloud, soft volumetric, isolated
[POSE / EMOTION / STATE] isolated element
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] vertical 9:16 1024x1536 for screens, square 1024x1024 for sprites
[LIGHTING] self-lit / flat
[BACKGROUND] transparent
[AVOID] captions, watermark, characters (unless stated), UI text unless exact text is given
```

## cough_smoke — Cough smoke puff (vfx)
- **Crop:** `cough_smoke_f01935.jpg`
- **Description / text:** Dark grey soft puff at the mouth corner.
- **Frames:** [[1923, 1941]]
- **How to build:** Radial blurred sprite, scale up + fade.

## shake_ticks — Shake ticks (vfx)
- **Crop:** `shake_ticks_f01280.jpg`
- **Description / text:** 3 short yellow dashes on each side of the knees (jitter).
- **Frames:** [[1267, 1293]]
- **How to build:** AE shape layer with a wiggle expression.
