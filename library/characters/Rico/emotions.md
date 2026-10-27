# Rico — emotions (video 03)

Face-only crops: `emo_<emotion>_f<frame>.png`. Every emotion is a whole-face drawing that is swapped in one frame (no tweening); brows are part of the face sprite; sweat drops are separate sprites.

| emotion | eyes | brows | mouth | extras | frame ranges (30 fps) | narration trigger |
|---|---|---|---|---|---|---|
| `confident_grin` | small solid black ovals, open | thick, level (one may be raised) | wide open grin, black mouth with 5–6 white square teeth | — | #17–53, #57–74, #130–162, #571–602, #606–625, #684–697, #700–711 | 'ever fake a number', 'two million', 'floor one and ten', 'that's more' |
| `smug_halflid` | half-lidded ovals (flat upper lid), looking sideways | one brow raised, other flat | small closed smirk curve | — | #27–30, #109–128, #163–183, #242–272, #459–464, #501–526, #568–570, #628–680, #712–713, #1325–1333, #1359–1378 (in lens) | 'look totally random', 'all start with a one', 'yours' |
| `panic_wavy_sweat` | large hollow circles with small dot pupils | raised, curved up | wavy zig-zag "~" line | blue sweat drop top-right; head tremble | #77–108, #937–954 (no sweat), #1177–1195 | 'a human made it up', 'streaky', 'to make them' |
| `focused` | solid ovals, slightly narrowed | angled down toward the centre (concentration) | tiny round "o" | — | #187–206, #1151–1172 | 'made every', 'he avoided' |
| `uneasy_sweat` | half-lidded | one cocked up, one flat | wavy moustache-like "~" | sweat drop on the left | #207–236 | 'every amount look' |
| `doubtful` | small dots | flat, slightly lifted | wavy "~" | no sweat | #76, #714, #934–936, #1173–1176 | 'doubles' (before panic) |
| `relieved_sweat` | closed, gently curved lines | relaxed | open satisfied grin | sweat drop still on | #238–241 | 'totally' (after the rewrite) |
| `nervous_sideglance` | solid dots looking sideways/up | one angled down | small flat smirk | sweat drop on the left | #273–282 | 'got' (handcuffs drop) |
| `surprised_sweat` | hollow circles with dot pupils | raised | tiny downturned frown | sweat drop; red/blue police wash over the face | #283–303, #876 | 'caught.' |
| `annoyed` | solid dots, side-eye at camera | angled down (frown) | small flat downturned line | — | #304–342, #873–875, #877–902, #1291–1324 | 'But how? Well, picture' |
| `sulky` | solid dots | slanted up in the middle (pouty) | small "^" pout | — | #430–454 | 'and look at the buttons' |
| `content_eyes_closed` | closed lines | relaxed | small closed smile | — | #455–458, #1355–1358 | 'buttons.' / 'yours,' |
| `mischievous_grin` | solid dots | angled down toward the centre (devious) | toothy grin | — | #466–498 | 'floors two through nine' |
| `gleeful_eyes_closed` | both closed as short lines | level | open toothy grin | — | #499–500, #567, #603–605, #626–627, #681–683, #698–699, #1196 | beat-accent blinks on 'each', 'up', 'that's' |
| `surprised` | hollow circles with dot pupils | neutral/high | tiny "o" or short line | — | #527–537 | 'different number' |
| `manic_grin` | hollow circles with dot pupils | high | wide toothy grin | — | #538–566 | 'number. But floor one' |
| `worried_frown` | hollow circles with dot pupils | raised | small "^" frown | small sweat mark on the hair | #715–800 | 'buttons. Real numbers work like that elevator' |
| `mesmerised_lookup` | hollow circles with pupils at the top (looking up) | neutral | tiny "o" | — | #903–933 | 'real randomness is streaky' (coin flips) |
| `gritted_panic` | hollow circles with small pupils | raised | rectangle of gritted teeth (grid) | sweat mark on hair; tremble | #1197–1222 | 'random. But' |
| `cocky_grin` | half-lidded | flat/low | toothy grin | — | #1334–1354 | 'to make yours,' |
| `panic_multi_sweat` | hollow circles with tiny pupils | raised | wavy "~" | 2–3 sweat drops on the forehead (seen magnified in the lens) | #1379–1413 | 'always a way to tell.' |

## confident_grin

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_confident_grin_f00045.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] confident grin: eyes small solid black ovals, open; brows thick, level (one may be raised); mouth wide open grin, black mouth with 5–6 white square teeth; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## smug_halflid

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_smug_halflid_f00640.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] smug halflid: eyes half-lidded ovals (flat upper lid), looking sideways; brows one brow raised, other flat; mouth small closed smirk curve; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## panic_wavy_sweat

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_panic_wavy_sweat_f00080.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] panic wavy sweat: eyes large hollow circles with small dot pupils; brows raised, curved up; mouth wavy zig-zag "~" line; extras: blue sweat drop top-right; head tremble
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## focused

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_focused_f00200.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] focused: eyes solid ovals, slightly narrowed; brows angled down toward the centre (concentration); mouth tiny round "o"; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## uneasy_sweat

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_uneasy_sweat_f00210.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] uneasy sweat: eyes half-lidded; brows one cocked up, one flat; mouth wavy moustache-like "~"; extras: sweat drop on the left
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## doubtful

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_doubtful_f01174.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] doubtful: eyes small dots; brows flat, slightly lifted; mouth wavy "~"; extras: no sweat
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## relieved_sweat

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_relieved_sweat_f00240.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] relieved sweat: eyes closed, gently curved lines; brows relaxed; mouth open satisfied grin; extras: sweat drop still on
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## nervous_sideglance

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_nervous_sideglance_f00278.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] nervous sideglance: eyes solid dots looking sideways/up; brows one angled down; mouth small flat smirk; extras: sweat drop on the left
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## surprised_sweat

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_surprised_sweat_f00290.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] surprised sweat: eyes hollow circles with dot pupils; brows raised; mouth tiny downturned frown; extras: sweat drop; red/blue police wash over the face
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## annoyed

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_annoyed_f00320.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] annoyed: eyes solid dots, side-eye at camera; brows angled down (frown); mouth small flat downturned line; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## sulky

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_sulky_f00440.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] sulky: eyes solid dots; brows slanted up in the middle (pouty); mouth small "^" pout; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## content_eyes_closed

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_content_eyes_closed_f00458.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] content eyes closed: eyes closed lines; brows relaxed; mouth small closed smile; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## mischievous_grin

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_mischievous_grin_f00495.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] mischievous grin: eyes solid dots; brows angled down toward the centre (devious); mouth toothy grin; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## gleeful_eyes_closed

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_gleeful_eyes_closed_f00604.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] gleeful eyes closed: eyes both closed as short lines; brows level; mouth open toothy grin; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## surprised

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_surprised_f00531.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] surprised: eyes hollow circles with dot pupils; brows neutral/high; mouth tiny "o" or short line; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## manic_grin

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_manic_grin_f00548.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] manic grin: eyes hollow circles with dot pupils; brows high; mouth wide toothy grin; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## worried_frown

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_worried_frown_f00730.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] worried frown: eyes hollow circles with dot pupils; brows raised; mouth small "^" frown; extras: small sweat mark on the hair
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## mesmerised_lookup

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_mesmerised_lookup_f00912.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] mesmerised lookup: eyes hollow circles with pupils at the top (looking up); brows neutral; mouth tiny "o"; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## gritted_panic

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_gritted_panic_f01199.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] gritted panic: eyes hollow circles with small pupils; brows raised; mouth rectangle of gritted teeth (grid); extras: sweat mark on hair; tremble
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## cocky_grin

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_cocky_grin_f01346.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] cocky grin: eyes half-lidded; brows flat/low; mouth toothy grin; extras: —
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## panic_multi_sweat

```
[REFERENCE] attach: library/characters/Rico/emotions/emo_panic_multi_sweat_f01395.png
[SUBJECT] Rico, cartoon office clerk: perfectly round warm-white head (#f8efe6), dark-brown glossy bowl haircut with centre part line, no nose/ears, mustard-yellow jacket (#d9a23f) on a capsule torso, white collar, narrow red-brown tie with cream diagonal stripes, blue lanyard clip, black stick limbs with black ball hands — FACE/HEAD ONLY, same head shape, hair and outline as the reference
[POSE / EMOTION / STATE] panic multi sweat: eyes hollow circles with tiny pupils; brows raised; mouth wavy "~"; extras: 2–3 sweat drops on the forehead (seen magnified in the lens)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] head only, front view, centred, head fills 80% of a square 1024x1024 sprite, identical position and scale for every emotion so faces can be swapped
[LIGHTING] flat even light, single soft shade band on the right side of the head
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, background scenery, nose, ears, fingers
```

## Expression timeline (frame → emotion, hold length)

| frames | emotion | hold (frames) |
|---|---|---|
| 17–53 | confident_grin (27–30 smug flicker) | 37 |
| 54–56 | squint (blink) | 3 |
| 57–74 | confident_grin (brow raised) | 18 |
| 75 | blink | 1 |
| 76 | doubtful | 1 |
| 77–108 | panic_wavy_sweat | 32 |
| 109–128 | smug_halflid (tiny, in car) | 20 |
| 130–162 | confident_grin | 33 |
| 163–183 | smug_halflid | 21 |
| 184–186 | blink | 3 |
| 187–206 | focused (sweat appears #204) | 20 |
| 207–236 | uneasy_sweat | 30 |
| 238–241 | relieved_sweat | 4 |
| 242–267 | smug_halflid | 26 |
| 268 | blink | 1 |
| 269–272 | smug_halflid | 4 |
| 273–282 | nervous_sideglance (sweat from #279; wince #282) | 10 |
| 283–303 | surprised_sweat | 21 |
| 304–342 | annoyed (blink 310–311) | 39 |
| 430–454 | sulky | 25 |
| 455–458 | content_eyes_closed | 4 |
| 459–465 | smug_halflid | 7 |
| 466–498 | mischievous_grin | 33 |
| 499–500 | gleeful_eyes_closed | 2 |
| 501–518 | smug_halflid | 18 |
| 519 | blink | 1 |
| 520–526 | smug_halflid | 7 |
| 527–537 | surprised | 11 |
| 538–566 | manic_grin | 29 |
| 567 | gleeful_eyes_closed | 1 |
| 568–570 | smug_halflid | 3 |
| 571–602 | confident_grin | 32 |
| 603–605 | gleeful_eyes_closed | 3 |
| 606–625 | confident_grin | 20 |
| 626–627 | gleeful_eyes_closed | 2 |
| 628–680 | smug_halflid | 53 |
| 681–683 | gleeful_eyes_closed | 3 |
| 684–697 | confident_grin | 14 |
| 698–699 | gleeful_eyes_closed | 2 |
| 700–711 | confident_grin (brow raised) | 12 |
| 712–713 | smug_halflid | 2 |
| 714 | doubtful | 1 |
| 715–800 | worried_frown (small in the cab from #740) | 86 |
| 873–875 | annoyed | 3 |
| 876 | surprised_sweat | 1 |
| 877–902 | annoyed | 26 |
| 903–933 | mesmerised_lookup | 31 |
| 934–936 | doubtful | 3 |
| 937–954 | panic_wavy (no sweat) | 18 |
| 1151–1172 | focused | 22 |
| 1173–1176 | doubtful | 4 |
| 1177–1183 | panic_wavy_sweat | 7 |
| 1184–1185 | wince (half-lid) | 2 |
| 1186–1195 | panic_wavy_sweat | 10 |
| 1196 | gleeful_eyes_closed (sheepish) | 1 |
| 1197–1222 | gritted_panic | 26 |
| 1291–1324 | annoyed (profile, writing) | 34 |
| 1325–1333 | smug_halflid | 9 |
| 1334–1354 | cocky_grin | 21 |
| 1355–1358 | content_eyes_closed | 4 |
| 1359–1378 | smug_halflid (in the lens from #1372) | 20 |
| 1379–1413 | panic_multi_sweat (drops appear #1380) | 35 |

**Switch statistics (Rico):** ≈ 62 face holds over ≈ 1080 on-screen frames → mean hold ≈ 17 frames (0.58 s), median ≈ 12 frames.
Blinks/eye-closed accents are 1–3 frames. Emotional holds are 10–40 frames; the longest holds are 53 (smug while explaining)
and 86 frames (worried, partly tiny in the wide shot). Shock swaps land exactly on the stressed word (#77 "human",
#283 "caught", #527 "different", #1379 "always"). The system needed: per-character face atlas of ~20 faces + blink frame,
swapped on integer frames with no interpolation, plus independent sweat-drop and tremble layers.

