# Overlays / UI / VFX — video 03

| id | file | what | frames | how to build |
|---|---|---|---|---|
| `caption_card` | `caption_card_f00045.jpg` | caption word card "there's" | all | code/AE text: heavy geometric sans (Montserrat Black-like), white #ffffff, 4 px black outline, soft 50 % drop shadow, ≈38 px cap height, centre y≈900, 1–3 words, hard cut per word group |
| `vfx_sweat_drop` | `vfx_sweat_drop_f00080.jpg` | blue sweat drop with highlight | #77–105, #204–240, #279–303, #1177–1188, #1380–1413 | 2D sprite (prompt) parented to head |
| `vfx_police_wash_red` | `vfx_police_wash_red_f00290.jpg` | full-frame red tint (police lights) | #289–293 | AE solid red #ff3b3b, blend Overlay/Color 35 %, alternating with blue every ≈5 frames |
| `vfx_police_wash_blue` | `vfx_police_wash_blue_f00286.jpg` | full-frame blue tint | #285–288, #295–298 | AE solid blue #3b6bff, same blend |
| `vfx_coin_trail` | `vfx_coin_trail_f00912.jpg` | stroboscopic stack of glowing coin after-images | #903–933 | AE Echo (8–12 echoes, decay 0.8) + glow on the coin layer |
| `vfx_rainbow_button_glow` | `vfx_rainbow_button_glow_f00495.jpg` | per-button rainbow glow 2–9 | #475–700 | AE: coloured circle layers + Glow, switched on 2 frames apart |
| `vfx_gold_bloom` | `vfx_gold_bloom_f00720.jpg` | gold glow on 1 and 10–19 + warm bloom | #553–736 | AE glow + global warm grade (Lumetri temp +20, highlights bloom) |
| `ui_glow_run_ellipse` | `ui_glow_run_ellipse_f01050.jpg` | 6 glowing heads coins + red ellipse outline | #1021–1060 | AE: per-coin glow on 3-frame steps + ellipse shape layer stroke #d2412b 4 px with trim-path draw-on |
| `vfx_vibration_lines` | `vfx_vibration_lines_f01182.jpg` | "((" tremble marks beside the pen | #1176–1186 | 2D sprite, flicker every 2 frames |
| `ui_led_counter` | `ui_led_counter_f00115.jpg` | LED dot-matrix counter $0 → $2,000,000 | #107–130 | code/AE: text expression counting with ease-out over 22 frames + dot-matrix (CC Ball Action or LED font), orange #f2a33a on black |
| `vfx_defocus_double_exposure` | `vfx_defocus_double_exposure_f01275.jpg` | lens defocus + ghost number skyline | #1253–1290 | camera lens blur ramp 0→12 px over 6 frames; number-skyline layer 40 % opacity Screen |
| `trans_dissolve` | `trans_dissolve_f00109.jpg` | example of a 7-frame cross-dissolve (Rico face + bank LED $0) | #106–112 | linear opacity cross-fade 5–8 frames |
| `vfx_sparkle_glint` | `vfx_sparkle_glint_f00050.jpg` | white 4-point sparkle on the magnifier rim | #47–52, #1291–1390 | 2D sprite, scale 0→1→0 over 6 frames, slight rotation |
| `vfx_lens_magnified_face` | `vfx_lens_magnified_face_f01395.jpg` | magnifier showing Rico's face enlarged with 3 sweat drops | #1372–1413 | AE: duplicate of Rico layer scaled ≈1.8×, masked by the lens circle, + face swap inside |

Only sprite-type items need an image prompt; the rest are built in code/AE as described.

## vfx_sweat_drop

```
[REFERENCE] attach: library/overlays_ui/03_why_humans_cant_pick_random_numbers/vfx_sweat_drop_f00080.jpg
[SUBJECT] a single cartoon sweat drop, light blue #8cb9db with a white highlight and dark outline
[POSE / EMOTION / STATE] isolated sprite
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, captions, watermark, characters
```

## vfx_vibration_lines

```
[REFERENCE] attach: library/overlays_ui/03_why_humans_cant_pick_random_numbers/vfx_vibration_lines_f01182.jpg
[SUBJECT] three small curved black motion lines like brackets
[POSE / EMOTION / STATE] isolated sprite
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, captions, watermark, characters
```

## vfx_sparkle_glint

```
[REFERENCE] attach: library/overlays_ui/03_why_humans_cant_pick_random_numbers/vfx_sparkle_glint_f00050.jpg
[SUBJECT] a white four-pointed sparkle star with soft glow
[POSE / EMOTION / STATE] isolated sprite
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, captions, watermark, characters
```
