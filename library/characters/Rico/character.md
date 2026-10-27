# Rico — the embezzling clerk

- **Role:** protagonist / culprit. Accounts-payable clerk who forges cheques with "random-looking" amounts, steals $2,000,000,
  gets caught by Benford's-law analysis and ends in jail.
- **Video:** 03 "Why Humans Can't Pick Random Numbers" (`analysis/videos/03_why_humans_cant_pick_random_numbers`). On screen in
  every shot except S8, S9, S11 (≈ 75 % of the runtime).
- **Assigned description check:** correct (white round head, short black/dark-brown hair, mustard-yellow jacket, red striped tie,
  accounts-payable desk, writes fake checks). Additions: blue lanyard/ID clip on the left chest, breast pocket, orange prison
  jumpsuit in the final scene, cuffs on his wrists from #283 on.

## Design spec
| part | spec |
|---|---|
| Head | perfect circle, warm off-white `#f8efe6` (shade side `#e9dbd9`), ≈ 1 head-unit; face sits in the lower 60 % |
| Outline | near-black dark brown `#2a1c1a`, uniform ≈ 7 px at 720-wide frame (≈ 4 % of head diameter), no taper |
| Hair | dark brown `#3b2820` bowl/helmet cap covering the top 40 % of the head, one vertical part line in the centre front, a soft lighter highlight band `#8a6a56` following the curve (glossy) |
| Eyes | neutral: small solid black ovals; smug: half-lidded (flat top lid line); shock: hollow black circles with dot pupils; closed: short horizontal lines |
| Brows | thick short black strokes, highly mobile (carry the emotion) |
| Mouth | tiny line / smirk curve; grin = black open shape with 4–6 white square teeth; worry = wavy "~" (moustache-like) line; panic = gritted rectangle grid |
| Nose / ears / cheeks | none |
| Torso | upright capsule/bean ≈ 1.3 heads tall, ≈ 0.85 head wide; mustard-yellow jacket `#d9a23f` (shade `#bf7f27`, lit `#e3c99e`), lapel V lines, white shirt collar, breast pocket outline on the right chest, blue lanyard clip `#4a6fb3` on the left |
| Tie | narrow red-brown `#88422e` tie with diagonal cream stripes, long (reaches ≈ 70 % of the torso) |
| Arms | single black strokes (≈ 7 px), elbows bend as simple angles, black ball hands ≈ 0.18 head; when cuffed: silver ring cuffs at wrists |
| Legs | two black sticks ≈ 1.7 heads long from the bottom of the capsule, tiny forward foot hooks |
| Proportions | total ≈ 4.2 heads tall (head 1, torso 1.3, legs 1.8 incl. overlap) |
| Alternate outfit | orange prison jumpsuit `#e0631f` (S12) |

Colour list: `#f8efe6` `#e9dbd9` `#2a1c1a` `#3b2820` `#8a6a56` `#d9a23f` `#bf7f27` `#88422e` `#f3e6d4` `#4a6fb3` `#1e1616` `#e0631f` sweat `#8cb9db`.

## Personality
Smug, cocky, sure he's clever; flips instantly to sweaty panic when exposed. Mostly grins and smirks; panics on key words.

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Rico/reference/ref_00640.jpg (+ ref_00045.jpg for the face)
[SUBJECT] "Rico", a cartoon office clerk: perfectly round warm-white head with no nose or ears, dark-brown glossy bowl haircut with a centre part line, small black oval eyes, thick short black brows, tiny smirk; capsule-shaped torso in a mustard-yellow jacket with lapel lines, white collar, narrow red-brown tie with diagonal cream stripes, breast pocket, blue lanyard clip; black stick arms with black ball hands; long black stick legs; total height about 4.2 heads.
[POSE / EMOTION / STATE] character turnaround sheet: front, 3/4 left, side, back, 3/4 right; neutral smug expression; arms relaxed; plus a small row of 6 face expressions (smug half-lid, toothy grin, hollow-circle shocked eyes with wavy mouth and sweat drop, focused, eyes-closed grin, gritted panic).
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] model sheet, characters evenly spaced on one row, full body, same scale, 1536x1024 landscape
[LIGHTING] flat even light, single soft shade band on the head's right side
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, nose, ears, fingers, gradients on clothes, 3D shading on the character
```

## Consistency notes
- Outline weight must stay constant regardless of scale (it does in the source even at tiny scale in S4/S6) → scale the drawing, then re-stroke, or keep vector strokes non-scaling.
- Face is a separate swappable layer; brows are part of the face sprite. Sweat drop is a separate sprite at the upper-left or upper-right of the head.
- Head stays a circle in every view; only the hair cap and face position rotate around it (the face moves to the side in 3/4 views).
- Hands are always balls (no fingers), even when holding a pen (pen sticks out of the ball).
