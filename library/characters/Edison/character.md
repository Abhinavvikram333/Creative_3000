# Edison — Thomas Edison cameo

- **Role:** authority cameo. "Thomas Edison was rumored to do it on purpose." He is the real-world precedent for the steel-ball nap.
- **Video:** 02 "Your Brain's Secret Idea Zone", shot S5 only (#617–717, 3.3 s), in the Menlo Park lab.
- **Assigned description check:** mostly correct (older, grey/white swept hair, dark suit with a bow tie).
  - Correction: he is drawn on the **same round-head pill-body template as Theo** — no wrinkles, moustache or beard.
  - Correction: the hair is a pale grey-beige swept cap with a centre part. The warm lab light makes it read beige-gold (`#c49779`); the neutral colour is about `#c9bba8`.
  - Addition: he holds the same steel balls over plates, mirroring Theo's setup.

## Design spec
| part | spec |
|---|---|
| Head | Perfect circle, warm cream `#f2d6b0` (warm-lit `#efc797`, shade `#be8e67`), the same size and position as Theo's. |
| Outline | Dark brown `#381b0f`, uniform about 7–8 px. |
| Hair | Pale grey-beige swept-back cap covering the top 40 % of the head (`#c9bba8` neutral / `#c49779` warm-lit), a centre part line, 4–6 fine darker strand lines `#8d6042` following the sweep. |
| Eyes / brows / mouth | The same stroke vocabulary as Theo: thick dash eyes, short brows, a small smile. |
| Torso | Pill body in a black suit `#1e0c05` with a narrow lapel V, a white shirt V `#fcd496` (warm-lit) and a small black bow tie. |
| Limbs | Dark sticks `#1f1917` with ball hands. |
| Proportions | Identical to Theo (≈ 4 heads tall). |

Colour list: `#f2d6b0` `#efc797` `#be8e67` `#381b0f` `#c9bba8` `#c49779` `#8d6042` `#1e0c05` `#fcd496` `#1f1917`.

## Personality
Calm, knowing, a little mischievous: he "naps" serenely, peeks with one eye and winks to the viewer.

## Master prompt
```
[REFERENCE] attach: library/characters/Edison/reference/ref_00700.jpg (+ ref_00630.jpg for the face)
[SUBJECT] "Edison" (cartoon Thomas Edison cameo): same template as the series' round-head characters — perfectly round warm cream head (#f2d6b0, warm-lit #efc797) with thick dark-brown outline (#381b0f), no nose, no ears; pale grey-beige swept-back hair cap (#c9bba8, warm-lit #c49779) with a centre part and fine strand lines; tall pill torso in a black suit (#1e0c05) with a white shirt V and a small black bow tie; thin dark stick limbs with ball hands
[POSE / EMOTION / STATE] character turnaround sheet: front, 3/4, side, back; plus seated-on-chair pose holding steel balls; plus 4 face expressions (serene closed dashes, one-eye sly peek, happy closed arcs, wink)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] model sheet, full body, same scale, 1536x1024 landscape
[LIGHTING] flat even light
[BACKGROUND] transparent
[AVOID] text, captions, watermark, nose, ears, beard, moustache, wrinkles, realistic portrait
```

## Consistency notes
- Do **not** make him a realistic portrait. He must stay on the series template so he can swap in place of Theo with a simple dissolve (#617–622 morph).
- He is always rendered under a warm amber grade in this video. Keep the base colours neutral and grade in compositing.
