# Theo — the sleeper (Edison-nap demonstrator)

- **Role:** protagonist / demonstrator. He acts out the steel-ball nap trick, sleeps, gets X-rayed, sinks through the sleep-stage chart, rides the dream elevator and wakes up holding his MAGNET CAR idea.
- **Video:** 02 "Your Brain's Secret Idea Zone" (`analysis/videos/02_your_brains_secret_idea_zone`). On screen in S1–S4, S6, S8 and S9 (S3 as POV); absent in S5 (Edison) and S7 (corkboard).
- **Assigned description check:** correct (cream/peach round head, brown swoopy bowl hair, long navy-blue pill body, wooden chair, steel balls over metal plates, a translucent blue X-ray version with a brain).
  - Additions: the X-ray version shows a **white plug tag** on the brain and a **glowing "wire" nerve**, not an anatomical nervous system.
  - Additions: an underwater tinted version (S6) and a lavender-graded version (S8, DEEP SLEEP floor).

## Design spec
| part | spec |
|---|---|
| Head | Perfect circle, cream-peach `#f6e1c7` (shade side `#e2c2ab`, a lighter top highlight). 1 head-unit; the face sits in the lower 55 %. |
| Outline | Dark brown `#2e1d17`, uniform about 7–8 px at 720 wide (≈ 4 % of the head diameter), no taper, on the head, torso and hair. |
| Hair | Brown `#694532` bowl / helmet cap covering the top 40 % of the head, a small swoop at the front, a centre part line, 2–3 darker strand lines, a lighter band `#8a6a56`. |
| Eyes | Default: solid dark-brown dots. Variants are in emotions.md. No eye whites except the "alarmed" hollow circles. |
| Brows | Short thick tapered dark-brown strokes, highly mobile. |
| Mouth | Small dash / curve; toothy grin = a black shape with 4–6 white teeth; worry = wavy "~". |
| Nose / ears / cheeks | None. |
| Torso | Tall rounded pill / capsule, about 1.5 heads tall and 0.9 head wide, navy-blue `#3a5080` (shade `#2d3d5f`, vertical sheen `#5a6fa0`). No clothing details. |
| Arms | Single dark strokes `#1f1917`, about 7 px, attached at the upper torso sides; elbows bend as simple angles; small ball hands (≈ 0.15 head). |
| Legs | Two dark sticks about 1.6 heads long; sit with knees as sharp angles; small foot ends. |
| Proportions | About 4 heads tall standing (head 1, torso 1.5, legs 1.6 with overlap). |
| X-ray variant | Translucent light-blue body `#6faac8` with a lighter outline `#a8d8ef` and darker inner "water" `#306a87`; pink brain `#e493a9`; white plug tag `#f4f1ea` with a socket icon; nerve wire = double pale-yellow glow line `#f2e8b0` (unplugged: mauve-grey zigzag `#807d93`); legs drawn as blue outline step lines. |

Colour list: `#f6e1c7` `#e2c2ab` `#2e1d17` `#694532` `#8a6a56` `#3a5080` `#2d3d5f` `#5a6fa0` `#1f1917` `#3b2418` · X-ray `#6faac8` `#306a87` `#a8d8ef` `#e493a9` `#f2e8b0` `#807d93` · sweat `#a7cdd7`.

## Personality
An everyman "guinea pig": calm and determined when following instructions, drowsy, then alarmed or annoyed at the rude awakening, and finally smug and proud when the trick pays off. He reacts on almost every clause.

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Theo/reference/ref_00100.jpg (+ ref_00045.jpg for the seated pose, ref_01141.jpg for the grin)
[SUBJECT] "Theo", a cartoon man: perfectly round cream-peach head (#f6e1c7, shade #e2c2ab) with a thick uniform dark-brown outline (#2e1d17), no nose, no ears; glossy brown bowl haircut (#694532) with a centre part line and 2-3 strand lines; tall rounded navy-blue pill-shaped torso (#3a5080) with a soft vertical sheen; thin dark-brown stick arms and legs (#1f1917) ending in small ball hands and simple feet
[POSE / EMOTION / STATE] character turnaround sheet: front, 3/4 left, side, back, 3/4 right, standing neutral; plus one seated-on-a-wooden-chair pose and a small row of 8 face expressions (asleep, alarmed hollow-circle eyes with wavy mouth, smug half-lid side smile, determined, happy closed arcs, drowsy, annoyed, excited toothy grin)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] model sheet, figures evenly spaced on one row, full body, same scale, 1536x1024 landscape
[LIGHTING] flat even light, soft top highlight on head, vertical sheen on torso
[BACKGROUND] transparent
[AVOID] text, captions, watermark, nose, ears, clothing details, realistic skin, extra characters
```

## X-ray variant prompt
```
[REFERENCE] attach: library/characters/Theo/reference/ref_00400.jpg
[SUBJECT] X-ray version of Theo seated on a wooden chair in 3/4 side view facing left
[POSE / EMOTION / STATE] translucent light-blue glassy body and round head with lighter blue outline and darker inner water-like shading, a pink cartoon brain inside the head, a small white rectangular plug tag with a socket icon plugged into the back of the brain, a glowing pale-yellow double wire running from the plug down the back into the hand, legs drawn as blue outline right-angle step lines, holding a chrome steel ball under the seat
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D cartoon characters with large perfectly round cream-peach heads, thick uniform dark-brown outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, short thick brow strokes, simple line mouths, no nose, no ears), long pill/capsule torsos in solid colour with a soft vertical sheen, thin dark noodle stick limbs ending in small ball hands; composited into a richly detailed, semi-realistic 3D-rendered vintage interior with painted textures, warm cinematic spotlight lighting, deep falloff shadows, soft bloom and light haze, gentle depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
[COMPOSITION] full body + chair, square 1024x1024
[LIGHTING] glowing cyan-blue rim, dark surroundings
[BACKGROUND] transparent
[AVOID] text, captions, watermark, realistic anatomy, skeleton
```

## Consistency notes
- The head is always a perfect circle, and the outline weight is constant for the head, body and hair. The face never rotates more than 3/4; profile views are only used in the X-ray variant.
- Edison (same video) uses exactly the same body template, so **re-skin the template rather than redraw it**. Keep Theo's hair brown and his body navy so the two stay distinguishable.
- Under scene grades (underwater blue, DEEP SLEEP lavender), recolour the character with an adjustment layer. Do not repaint him.
- The faces are swapped sprites, so generate every emotion on the same head template (emotions.md).
