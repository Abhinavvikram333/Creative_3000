# Marge — the auditor

- **Role:** antagonist-to-Rico / expert. Forensic auditor who catches Rico with leading-digit analysis. Calm, knowing, playful (coin tricks, wink).
- **Video:** 03 (`analysis/videos/03_why_humans_cant_pick_random_numbers`). Arm only in S1 (#34–105); full character S7–S12 (#873–1413, except S10).
- **Assigned description check:** correct (auburn hair in a bun, round glasses, purple suit, magnifying glass). Additions: a red pencil stuck through the bun, pale lilac-white blouse with a V collar under the purple jacket, white cuffs at the sleeve ends in top-down inserts.

## Design spec
| part | spec |
|---|---|
| Head | perfect circle, warm off-white `#f7e7df`, a soft vertical shade band on one side in warm scenes |
| Outline | `#2a1c1a`, uniform ≈ 7 px at 720 wide |
| Hair | auburn `#a2513b` (shade `#8f462c`, highlight `#c06a48`) cap covering the top half with a centre part line, high round top bun, a red pencil `#c8463a` pushed through the bun diagonally |
| Eyes | small dots behind thin black round glasses (two circles + bridge + short temple lines); half-lid for smirk |
| Brows | thin-to-medium black strokes above the glasses |
| Mouth | small sideways smirk curve |
| Torso | capsule ≈ 1.3 heads, purple suit jacket `#814eab`–`#8353c9` with dark lapel lines forming a V, pale lilac-white blouse `#f6d5d0` showing in the V |
| Arms / hands | black stick arms, black ball hands; in close inserts the sleeve is a thick purple tube with a white cuff ring |
| Legs | black sticks, ≈ 1.8 heads, small foot hooks |
| Proportions | ≈ 4.2 heads tall |
| Props | large gold-rimmed magnifying glass with a wooden-brown handle; gold coin; fan of cheques; red pencil |

Colour list: `#f7e7df` `#2a1c1a` `#a2513b` `#8f462c` `#c06a48` `#c8463a` `#814eab` `#8353c9` `#f6d5d0` magnifier rim `#caa16f`.

## Personality
Unflappable, amused, a little theatrical; always one step ahead. Only positive/knowing faces (smirk, smile, wink, eyes-closed satisfaction, pondering).

## Master prompt
```
[REFERENCE] attach: library/characters/Marge/reference/ref_01075.jpg (+ ref_00882.jpg for the face)
[SUBJECT] Marge, cartoon forensic auditor: perfectly round warm-white head without nose or ears, auburn hair with centre part in a high top bun with a red pencil stuck through it, small round thin black glasses, half-lidded knowing eyes, small sideways smirk; capsule torso in a purple suit jacket with a V of pale lilac-white blouse; black stick arms with black ball hands holding a large gold-rimmed magnifying glass; long black stick legs; about 4.2 heads tall.
[POSE / EMOTION / STATE] character turnaround sheet plus a row of 5 faces: knowing smirk, eyes-closed smug smile, pleasant smile, wink, pondering eyes-up
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] model sheet, full body, front / 3/4 / side / back / 3/4 on one row, same scale, 1536x1024 landscape
[LIGHTING] flat even light, single soft shade band on the head's right side
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, nose, ears, fingers, 3D shading on the character
```

## Consistency notes
- Glasses are part of the face sprite (they swap with the face, eyes drawn inside the lenses).
- Bun + pencil sit on the hair layer and must stay on top of the head in every angle.
- In top-down inserts only her sleeves appear: purple tube, white cuff ring, black stick forearm, black ball hand.
