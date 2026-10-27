# Overlays / UI / VFX — 05 "The Science Behind Slot Machines"

STYLE LOCK (verbatim): `Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.`

| id | Crop | Type | Description | Frames | How to build |
|---|---|---|---|---|---|
| o_caption_word | `o_caption_word_f00300.jpg` | overlay_ui | Word-by-word caption card (example 'Bro,') | all spoken words (95 cards) | **Code/AE text layer**: heavy rounded sans (Montserrat Black / Poppins ExtraBold), white #f8f7f8, black stroke 4–5 px @720w, soft drop shadow, centred at y≈900 of 1280, cap height ≈36 px, 1–2 words, hard cuts, no animation |
| o_x1_badge | `o_x1_badge_f00690.jpg` | overlay_ui | Red hand-drawn circle with 'x1' inside, on the jackpot row | 681–778 | AE/code: hand-drawn red (#cb1501) ring stroke + bold 'x1', cut on in 1 frame (no scale), tracked to the paper |
| o_one_click_short_stamp_imprint | `o_one_click_short_stamp_imprint_f00760.jpg` | overlay_ui | Red distressed rubber-stamp imprint: rounded rectangle border with 'ONE CLICK / SHORT' in bold condensed caps | 699–778 (accumulates) | Image sprite (distressed texture) placed per row on each stamp hit; or AE with Roughen Edges + texture matte |
| o_xray_wireframe | `o_xray_wireframe_f00840.jpg` | overlay_ui | Cyan glowing wireframe grid cage over the lower cabinet (X-ray look) | 779–928 | Blender: duplicate cabinet with Wireframe modifier + emission #3fd8e8, interior darkened, cross-fade in 6 f; or AE 3D grid |
| vfx_glint_sweep | `vfx_glint_sweep_f00647.jpg` | vfx | Diagonal gold light glint sweeping L→R over the JACKPOT row | 644–650, 669–677 | AE CC Light Sweep / gradient wipe with Add blend, 6–9 f, gold #fff2a0 core |
| vfx_stamp_impact_lines | `vfx_stamp_impact_lines_f00700.jpg` | vfx | 4–6 short dark tick lines radiating around the stamp at impact | each stamp hit (699–762), 2 f | AE shape layer burst (Repeater) 2 frames; or sprite |
| vfx_dissolve_ghost | `vfx_dissolve_ghost_f00253.jpg` | vfx | Cross-dissolve with ghosted double exposure and a bright diagonal glass streak | 251–254, 340–344, 423–428, 495–498, 542–547 | Editor cross-dissolve 4–6 f + optional light-leak/glass-streak overlay |
| vfx_dust_motes | `vfx_dust_motes_f00556.jpg` | vfx | Soft out-of-focus dust motes floating inside the cabinet | 542–778 | Particle system (Blender) or AE CC Particle World, low opacity bokeh dots, slow drift |

Also counted as overlays-in-world (see assets_3d): CREDITS digit roll (#404–414), tally counter roll x00→x14, progressive LED ticker. Recommended to drive all three from code (frame-exact numbers).

## Caption timing (exact)
See `analysis/videos/05_the_science_behind_slot_machines/script.md` §4 and frame_log.md for every card's frame range.

## Prompts (for image-built overlays)

### o_x1_badge
```
[REFERENCE] attach: library/overlays_ui/05_the_science_behind_slot_machines/o_x1_badge_f00690.jpg
[SUBJECT] a hand-drawn red marker circle with bold red 'x1' inside, slight wobble, transparent background
[POSE / EMOTION / STATE] isolated element, crisp edges
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024, straight-on
[LIGHTING] flat, no lighting
[BACKGROUND] transparent
[AVOID] background scene, extra text, watermark
```
### o_one_click_short_stamp_imprint
```
[REFERENCE] attach: library/overlays_ui/05_the_science_behind_slot_machines/o_one_click_short_stamp_imprint_f00760.jpg
[SUBJECT] a red distressed rubber-stamp imprint, rounded rectangle border, two lines of bold condensed caps 'ONE CLICK' / 'SHORT', ink texture with gaps, transparent background
[POSE / EMOTION / STATE] isolated element, crisp edges
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024, straight-on
[LIGHTING] flat, no lighting
[BACKGROUND] transparent
[AVOID] background scene, extra text, watermark
```
### o_xray_wireframe
```
[REFERENCE] attach: library/overlays_ui/05_the_science_behind_slot_machines/o_xray_wireframe_f00840.jpg
[SUBJECT] glowing cyan (#3fd8e8) wireframe grid box in perspective (cabinet volume), thin lines, transparent background
[POSE / EMOTION / STATE] isolated element, crisp edges
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024, straight-on
[LIGHTING] flat, no lighting
[BACKGROUND] transparent
[AVOID] background scene, extra text, watermark
```
