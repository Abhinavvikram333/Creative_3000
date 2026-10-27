# Kai — emotions (face library)

Face-only crops in this folder (`emo_<id>_<name>_f<frame>.png`). There are 24 distinct expressions in video 01. Same face = same id;
variants (heat fill, relieved, hopeful) are noted under their parent id. Frame ranges are inclusive and come from the
30 fps review (`analysis/videos/01_this_tree_hates_you/frame_log.md`).

Shared swap parts: eyes {dot, ring+dot, closed arc, flat lid line, half-lid+pupil, `><`, X, bloodshot ring}, brows
{neutral, raised, worried-up, angled-down, one-raised}, mouth {small smile, flat, wavy, gritted rect, o, toothy grin},
extras {sweat drop, tears, blush, red lid patches, anger vein, blisters, frost, steam, red heat fill, green tint}.

## E01 calm
- **Crop:** `emo_E01_calm_f00008.png (+ emo_E01_calm_f02040.png, emo_E01_calm_relieved_f01520.png)`
- **Description:** Relaxed half-closed eyes drawn as flat lid lines (upper lid line + short lower line), neutral slightly raised brows, small closed smile or tiny flat mouth. It reads as calm and content, a little smug.
- **Frames:** 1–8, 1511–1523 (relieved in the water), 2011–2043 (final sit)
- **Narration trigger:** Opening walk-in 'If you…'; 'place.' (relief in the water); closing 'sit in the sand.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E01_calm_f00008.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] calm half-closed eyes drawn as two flat lid lines, relaxed brows, tiny content smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E02 content_smile
- **Crop:** `emo_E02_content_smile_f00340.png (+ f01395)`
- **Description:** Eyes closed as upward arcs (^ ^), soft smile; a pale pink blush sometimes appears (35–62). The relieved 'phew' variant at 550–561 has a slightly wavy smile.
- **Frames:** 9–11, 19–62, 233–270, 319–349, 550–561 (phew), 1069–1071 (chewing), 1389–1402, 1719–1760, 1953–2010
- **Narration trigger:** Things look nice: 'sit under this tree', 'harmless', 'branches', 'for cover' (false relief), 'soft leaves', fire 'catches', final 'stranded on a beach'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E02_content_smile_f00340.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] eyes closed as happy upward arcs, gentle closed smile, relaxed brows
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E03 dead_x
- **Crop:** `emo_E03_dead_x_f00066.png`
- **Description:** Two X's for eyes, wavy mouth, no brows; from #67 the whole head is tinted sick green (#9fbf9a).
- **Frames:** 64–90
- **Narration trigger:** 'it can **kill** you.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E03_dead_x_f00066.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] X-shaped eyes, small wavy mouth, head tinted pale sick green (#9fbf9a) — comic 'dead' face
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E04 smug
- **Crop:** `emo_E04_smug_f00280.png`
- **Description:** Half-lidded eyes with dot pupils looking sideways, one brow raised, lopsided smirk.
- **Frames:** 274–290, 350–356, 1350–1352
- **Narration trigger:** 'little green apples' (pleased with himself), 'there's a big…' (before the reveal), relief after the bush
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E04_smug_f00280.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] half-lidded eyes looking to the side, one eyebrow raised, lopsided confident smirk
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E05 curious
- **Crop:** `emo_E05_curious_f01360.png (+ emo_E05_curious_f01590.png hopeful variant)`
- **Description:** Small dot eyes looking up/sideways, brows raised, tiny smile or flat mouth. Covers neutral (1528–1557) and hopeful (1588–1641).
- **Frames:** 12–18, 291–318, 1353–1388, 1528–1557, 1588–1641
- **Narration trigger:** 'apples hanging from the branches', 'handful of big soft', 'night falls', 'Fortunately, you have plenty of wood'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E05_curious_f01360.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] small round dot eyes looking up to the side, both brows raised, tiny hopeful smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E06 worried
- **Crop:** `emo_E06_worried_f00365.png (+ f01445; heat-fill variant emo_E06_worried_heatfill_f01165.png)`
- **Description:** Ring eyes (open circles with dot pupils), brows tilted up in the middle, wavy 'moustache' mouth; usually a blue sweat drop. Variant: red liquid fill rising inside the head (1160–1170).
- **Frames:** 357–375, 515–548, 564–570, 572–610, 723–731, 1156–1170, 1431–1454, 1645–1677
- **Narration trigger:** 'red x', 'you run under the tree', 'Big mistake', 'your mouth starts', 'Same sap', 'Unfortunately'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E06_worried_f00365.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] open ring eyes with small dot pupils, worried brows tilted up in the middle, wavy wobbly mouth, one blue sweat drop at the upper right of the head
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E07 unimpressed
- **Crop:** `emo_E07_unimpressed_f00400.png (+ f01415)`
- **Description:** Flat straight brows low over half-lidded eyes with dot pupils, flat or slightly wavy mouth. This is the deadpan 'of course' beat after each disaster.
- **Frames:** 376–423, 441–443, 747–763, 838–856, 958–960, 1011–1034, 1405–1428, 1678–1718
- **Narration trigger:** 'painted on its trunk', after the sap splat, after the blisters, 'Yeah.', 'it's from the same tree'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E07_unimpressed_f00400.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] deadpan: half-lidded eyes with dot pupils, flat straight brows pressed low, flat expressionless mouth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E08 shocked_gritted
- **Crop:** `emo_E08_shocked_gritted_f00430.png (+ f01310)`
- **Description:** Big ring eyes with dot pupils, brows up, rounded-rectangle mouth showing gritted teeth (grid lines), sweat drop.
- **Frames:** 424–440, 1296–1326
- **Narration trigger:** 'find out why', 'The only thing around to use' (behind the bush)
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E08_shocked_gritted_f00430.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] wide open ring eyes with dot pupils, raised brows, rounded-rectangle gritted-teeth mouth with grid lines, blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E09 alarmed_o
- **Crop:** `emo_E09_alarmed_o_f00452.png`
- **Description:** Ring eyes, raised brows, small round 'o' mouth, sweat drop.
- **Frames:** 444–456
- **Narration trigger:** 'The first night' (anticipation)
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E09_alarmed_o_f00452.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] open ring eyes with dot pupils, raised brows, small round o-shaped mouth, blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E10 wince
- **Crop:** `emo_E10_wince_f00740.png (+ f01465 with blisters)`
- **Description:** Eyes squeezed as `>` `<` chevrons, angled brows, gritted-teeth rectangle mouth; sweat; often with blisters or sizzle smoke.
- **Frames:** 734–746, 815–824, 1456–1477, 1497–1510
- **Narration trigger:** 'skin.' (sap splat), blistered on the beach, 'blisters.' (leaves), 'worse place'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E10_wince_f00740.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] eyes squeezed shut as > < chevrons, pained angled brows, gritted-teeth rectangle mouth with grid lines, blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E11 annoyed_scowl
- **Crop:** `emo_E11_annoyed_scowl_f00830.png (+ f00985)`
- **Description:** Brows angled down toward the centre, half-lidded eyes with pupils glancing sideways, wavy frown; sweat curl.
- **Frames:** 825–836, 970–1008
- **Narration trigger:** 'sap is so strong', 'you're starving'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E11_annoyed_scowl_f00830.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] scowl: eyebrows angled down to the centre, half-lidded eyes glancing sideways, wavy frowning mouth, small sweat curl
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E12 angry_vein
- **Crop:** `emo_E12_angry_vein_f00935.png`
- **Description:** Angled furious brows, narrowed eyes, gritted-teeth mouth, red anime anger-vein cross mark on the upper side of the head.
- **Frames:** 908–948 (vein fades 944–945)
- **Narration trigger:** 'Lesson learned.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E12_angry_vein_f00935.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] furious: sharply angled brows, narrowed eyes, gritted-teeth rectangle mouth, red anime anger-vein symbol on the upper right of the head
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E13 sulky_closed
- **Crop:** `emo_E13_sulky_closed_f00955.png`
- **Description:** Eyes closed as flat straight lines, flat brows, small wavy/flat mouth. He sulks with his eyes shut.
- **Frames:** 949–957, 961–969, 1009–1010
- **Narration trigger:** 'By the next morning though'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E13_sulky_closed_f00955.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] eyes closed as flat straight lines, flat brows, small flat slightly wavy mouth — sulking
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E14 dreamy_bliss
- **Crop:** `emo_E14_dreamy_bliss_f01050.png`
- **Description:** Closed eyes as soft arched lids, relaxed raised brows, small 'o'/smile mouth — entranced by the smell.
- **Frames:** 1035–1057
- **Narration trigger:** 'smell incredible.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E14_dreamy_bliss_f01050.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] dreamy: eyes closed as soft arches, relaxed raised brows, small rounded smiling mouth, entranced
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E15 eager_grin
- **Crop:** `emo_E15_eager_grin_f01065.png`
- **Description:** Big ring eyes with pupils, raised brows, wide toothy grin with teeth lines.
- **Frames:** 1060–1068
- **Narration trigger:** 'One bite'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E15_eager_grin_f01065.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] excited: big ring eyes with dot pupils, raised brows, wide open toothy grin with teeth lines
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E16 blissful_blush
- **Crop:** `emo_E16_blissful_blush_f01100.png`
- **Description:** Closed happy arcs, curved smile, pink blush ovals on both cheeks.
- **Frames:** 1072–1125
- **Narration trigger:** 'tastes sweet for about a second'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E16_blissful_blush_f01100.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] blissful: eyes closed as happy upward arcs, curved smile, soft pink blush ovals on both cheeks
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E17 suspicious
- **Crop:** `emo_E17_suspicious_f01140.png`
- **Description:** One brow raised with a small crease mark, other brow flat, half-lidded eyes with pupils, small flat mouth.
- **Frames:** 1127–1155
- **Narration trigger:** 'a second. Then'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E17_suspicious_f01140.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] suspicious: one eyebrow raised with a small crease line, the other flat, half-lidded eyes with dot pupils, small flat mouth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E18 crying_hot_red
- **Crop:** `emo_E18_crying_hot_red_f01190.png`
- **Description:** Whole head salmon-red (#da767a), ring eyes, thick blue tear streams down both cheeks, wavy mouth, sweat; white steam columns rise from both sides of the head.
- **Frames:** 1171–1221
- **Narration trigger:** 'burning and it feels like you swallowed fire'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E18_crying_hot_red_f01190.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] head flushed solid salmon red (#da767a), open ring eyes with dot pupils, thick light-blue tear streams running down both cheeks, wavy mouth, blue sweat drop, white cartoon steam puffs rising from both sides of the head
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E19 strain_grimace
- **Crop:** `emo_E19_strain_grimace_f01340.png (+ f01490)`
- **Description:** Furrowed brows angled down, half-lidded eyes with pupils, gritted-teeth rectangle mouth, sweat. He is straining or in pain while walking.
- **Frames:** 1331–1347, 1478–1496
- **Narration trigger:** 'is a handful' (straining behind the bush), 'Just in a much' (waddling)
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E19_strain_grimace_f01340.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] straining grimace: brows angled down hard, half-lidded eyes with dot pupils, gritted-teeth rectangle mouth with grid lines, blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E20 cold_chatter
- **Crop:** `emo_E20_cold_chatter_f01570.png`
- **Description:** Squeezed flat eyes, gritted chattering teeth, small blue frost zigzag marks on the forehead; night-blue grade.
- **Frames:** 1558–1587
- **Narration trigger:** 'you're freezing.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E20_cold_chatter_f01570.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] freezing: eyes squeezed into flat lines, brows tense, chattering gritted-teeth mouth, small icy zig-zag frost marks on the forehead
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E21 tear_wince
- **Crop:** `emo_E21_tear_wince_f01765.png`
- **Description:** Eyes `>` `<`, downturned wavy frown, blue tears; no red lids. Head greyed by smoke.
- **Frames:** 1756–1795
- **Narration trigger:** 'turns toxic.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E21_tear_wince_f01765.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] eyes squeezed as > < chevrons, downturned wavy frown, light-blue tears streaming down, slight grey smoky tint
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E22 squeeze_cry
- **Crop:** `emo_E22_squeeze_cry_f01820.png`
- **Description:** Eyes `>` `<` inside soft red puffy patches (irritated lids), angled brows, wavy frown, thick blue tear streams, sweat drop.
- **Frames:** 1797–1800, 1816–1822, 1869–1875
- **Narration trigger:** 'burns your eyes', 'can't', 'breath'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E22_squeeze_cry_f01820.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] eyes squeezed as > < chevrons sitting on soft red puffy eyelid patches, worried brows, wavy frown, thick light-blue tear streams, big blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E23 bloodshot_cry
- **Crop:** `emo_E23_bloodshot_cry_f01805.png (+ f01885)`
- **Description:** Ring eyes with pink-red sclera, short red vein ticks, dot pupils, red lower lids, thick blue tear streams, wavy mouth, worried brows, sweat drop.
- **Frames:** 1801–1815, 1878–1898, 1902–1920
- **Narration trigger:** 'burns your eyes until', 'scorches your lungs.'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E23_bloodshot_cry_f01805.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] bloodshot eyes: open ring eyes with pinkish-red whites, short red vein lines and dot pupils, red lower lids, thick light-blue tear streams, worried brows, wavy mouth, big blue sweat drop
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

## E24 cough_cry
- **Crop:** `emo_E24_cough_cry_f01935.png`
- **Description:** Like E22 (red-lid `><`, tears, sweat) but with a gritted-teeth rectangle mouth and a dark grey smoke puff coughed out at the mouth corner.
- **Frames:** 1921–1949
- **Narration trigger:** 'So, if you're ever'
- **Prompt:**

```
[REFERENCE] attach: library/characters/Kai/emotions/emo_E24_cough_cry_f01935.png (+ library/characters/Kai/reference/ref_01805.jpg for head shape)
[SUBJECT] Kai's head only: a very large round pale-lavender-white head (#dce0e9, soft shadow #babfcf), thick dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, no nose, no ears; same head shape, size and outline as the reference
[POSE / EMOTION / STATE] coughing: eyes squeezed > < on red puffy lid patches, gritted-teeth rectangle mouth with grid lines, light-blue tear streams, blue sweat drop, a small dark grey smoke puff escaping from the mouth corner
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] square 1024x1024, head centred filling ~80% of the frame, straight-on front view, eye level
[LIGHTING] flat even light, one soft lavender shadow tone on the lower-left of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, body, neck, extra characters, nose, ears, realistic skin, gradients, background scenery
```

---

## Expression timeline (frame → emotion, hold length in frames)
Only frames where Kai's face is visible. `~` marks 1–3 frame in-between frames (blink, squint, mouth change); they are
drawn as separate swap frames rather than tweened.

| Frames | Emotion | Hold (f) | Line |
|---|---|---|---|
| 1–8 | E01 calm | 8 | If you |
| 9–11 | E02 | 3 | ever |
| 12–18 | E05 | 7 | ever |
| 19–62 | E02 (+blush 35–62) | 44 | sit under this tree, it can |
| 63 | ~ | 1 | kill |
| 64–90 | E03 dead_x (green from 67) | 27 | kill you. Imagine |
| 233–270 | E02 | 38 | looks completely harmless |
| 271–273 | ~ blend | 3 | with |
| 274–290 | E04 | 17 | little green |
| 291–318 | E05 | 28 | apples hanging from |
| 319–349 | E02 | 31 | branches. But there's |
| 350–356 | E04 | 7 | a big |
| 357–375 | E06 | 19 | red x |
| 376–420 | E07 | 45 | painted on its trunk, and you're about |
| 421–423 | ~ (sweat on, wavy mouth) | 3 | to find |
| 424–440 | E08 | 17 | out why. |
| 441–443 | ~ (nervous half-lid) | 3 | why. |
| 444–456 | E09 | 13 | The first |
| 515–548 | E06 | 34 | you run under the tree for |
| 549–561 | E02 (relieved "phew") | 13 | cover. |
| 562–563 | ~ squint | 2 | Big |
| 564–570 | E06 | 7 | Big |
| 571 | ~ E07 glance | 1 | mistake. |
| 572–610 | E06 | 39 | mistake. You see, every |
| 723–731 | E06 | 9 | onto your |
| 732–733 | ~ squint/shut | 2 | your |
| 734–746 | E10 | 13 | skin. |
| 747–763 | E07 | 17 | Within minutes, |
| 815–824 | E10 (blisters) | 10 | This sap is |
| 825–836 | E11 | 12 | so strong, |
| 837 | ~ frown | 1 | strong |
| 838–856 | E07 | 19 | it |
| 908–948 | E12 (vein off at 945) | 41 | Lesson learned. By the next |
| 949 | ~ squeeze | 1 | morning |
| 950–957 | E13 | 8 | morning, |
| 958–960 | E07 | 3 | though, |
| 961–969 | E13 | 9 | though, |
| 970–1008 | E11 | 39 | you're starving. And those |
| 1009–1010 | E13 | 2 | little |
| 1011–1034 | E07 | 24 | apples smell |
| 1035–1057 | E14 | 23 | incredible. |
| 1060–1067 | E15 | 8 | One |
| 1068 | ~ glance | 1 | bite |
| 1069–1071 | E02 chewing | 3 | bite |
| 1072–1125 | E16 | 54 | actually tastes sweet for about a |
| 1126 | ~ | 1 | second |
| 1127–1149 | E17 | 23 | a second. Then |
| 1150–1155 | ~ E17 + sweat, squint | 6 | your mouth |
| 1156–1170 | E06 + heat fill | 15 | your mouth starts |
| 1171–1221 | E18 (blinks 1174–1176, 1181–1183) | 51 | burning and it feels like you swallowed |
| 1296–1326 | E08 | 31 | The only thing around to use |
| 1327–1330 | ~ squint/strain | 4 | to use |
| 1331–1347 | E19 | 17 | is a handful |
| 1348–1349 | ~ shut | 2 | handful |
| 1350–1352 | E04 (relieved smirk) | 3 | handful |
| 1353–1383 | E05 | 31 | of big soft |
| 1384–1385 | ~ squint | 2 | soft |
| 1386–1388 | E05 | 3 | leaves |
| 1389–1402 | E02 | 14 | leaves. |
| 1403–1404 | ~ | 2 | Yeah. |
| 1405–1428 | E07 | 24 | Yeah. Same |
| 1429–1430 | ~ squint | 2 | Same |
| 1431–1454 | E06 | 24 | sap, same |
| 1455 | ~ | 1 | blisters |
| 1456–1477 | E10 (+blisters) | 22 | blisters. |
| 1478–1496 | E19 | 19 | Just in a much |
| 1497–1510 | E10 | 14 | worse place |
| 1511–1523 | E01 relieved | 13 | place. |
| 1528–1557 | E05 neutral | 30 | night falls, you're |
| 1558–1587 | E20 | 30 | freezing. |
| 1588–1641 | E05 hopeful | 54 | Fortunately, you have plenty of wood. Unfor- |
| 1642–1644 | ~ smile/squint/wavy | 3 | -tunately |
| 1645–1677 | E06 (squint 1662–1663) | 33 | Unfortunately, it's from the same |
| 1678–1718 | E07 | 41 | same tree. The second it |
| 1719–1755 | E02 | 37 | catches, the smoke |
| 1756–1760 | E02 + tears | 5 | turns |
| 1761–1795 | E21 | 35 | toxic. It burns |
| 1797–1800 | E22 | 4 | burns your eyes |
| 1801–1814 | E23 | 14 | burns your eyes until |
| 1815 | ~ half-lid | 1 | until |
| 1816–1822 | E22 | 7 | you can't |
| 1869–1875 | E22 | 7 | breath |
| 1876–1877 | ~ blink | 2 | breath |
| 1878–1898 | E23 | 21 | scorches your |
| 1899–1901 | ~ blink | 3 | lungs |
| 1902–1918 | E23 | 17 | your lungs. |
| 1919–1920 | ~ half-lid | 2 | So |
| 1921–1949 | E24 | 29 | So, if you're ever |
| 1953–2010 | E02 | 58 | stranded on a beach, maybe just sit in |
| 2011–2043 | E01 | 33 | the sand. |

**Face-swap system stats:** 90 timeline entries (holds + in-betweens) across ≈1 600 face-visible frames. Most expression holds run 7–58 frames (a few emotions flash for only 2–3 frames, e.g. E13 #1009–1010, E04 #1350–1352)
(median ≈ 20 f ≈ 0.67 s, so about one face change per 1–2 caption words). In-between frames are 1–3 frames (blinks,
squints, mouth shapes). Swaps are **hard cuts** (no tween), mostly on the first frame of the stressed word: #64
"kill", #358 "red x", #424 "out why", #734 "skin", #1072 "bite", #1171 "burning", #1456 "blisters", #1558
"freezing", #1645 "Unfortunately". Extras (sweat drop, tears, steam, blisters) pop on 1–3 frames **before or with**
the face change and stay on as separate layers. Build it as: head base layer + an eyes/brows/mouth sprite-sheet
layer (one frame per emotion id) + an extras layer, switched by hold keyframes in AE (time-remap) or a
Blender/Grease-Pencil image-sequence strip.
