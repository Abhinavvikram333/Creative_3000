# Bling

- **Role**: the buddy / neighbour at the next machine who says "Bro, it's just warming up" (the gambler's-fallacy voice).
- **Video(s)**: 05 "The Science Behind Slot Machines" — frames 175–188 (edge), 255–340 (POV dialogue), 497–520 (behind Lenny).
- **Assigned description check**: correct — red backwards cap, gold chain, white tank top. Refinements: the cap has a
  pair of black sunglasses perched on it (on the back/brim area), the tank top is cream and ribbed, and he has stubble dots
  on the lower face.

## Design spec
| Part | Spec |
|---|---|
| Head | Same family as Lenny: big round cream-white head **#fdf7dd**, warm shading **#f4d0b7**, no ears/nose. |
| Outline | Thick dark brown **#531c12**, same weight as Lenny. |
| Hair/headwear | Red **#e83234** baseball cap worn backwards (strap/adjuster band with small white dots at the front), black sunglasses resting on the cap. No hair visible. |
| Eyes | Small dark ovals, usually half-lidded/sly; wink variant (one closed curve). |
| Brows | thin single strokes, often one raised. |
| Mouth | sly side smile; open grin showing upper teeth (with a gap) when talking. |
| Cheeks/chin | 4–6 brown stubble dots **#77402a** on the jaw. |
| Body | Bean torso in a cream ribbed tank top **#fbedd4** (shadow #cba78f), thin straps. |
| Accessories | Chunky gold chain **#d9a43a** with links, hanging to mid-chest. |
| Limbs | Noodle strokes, blob hands. |
| Proportions | ≈4.3 head-heights like Lenny. |

Colour list: #fdf7dd · #f4d0b7 · #531c12 · #e83234 · #b8231f · #1a0e0e · #77402a · #fbedd4 · #cba78f · #d9a43a

## Personality
Over-confident casino bro: sly winks, leans in too close, gives terrible advice with total conviction. Talks with
big toothy grins.

## Reference crops
- `reference/ref_00290.jpg` — lean-in, head + torso (cap, sunglasses, chain, tank top all visible)
- `reference/ref_00499.jpg` — seated behind Lenny, more of the body + stool

## Master prompt
```
[REFERENCE] attach: library/characters/Bling/reference/ref_00290.jpg
[SUBJECT] "Bling", a simple cartoon casino bro: very large round cream-white head (#fdf7dd) with no ears/nose, red (#e83234) baseball cap worn backwards with black sunglasses resting on it, small sly half-lidded dot eyes, a few brown stubble dots on the jaw, bean-shaped torso in a cream ribbed tank top (#fbedd4), chunky gold chain (#d9a43a), noodle arms/legs as thick dark-brown strokes, blob hands, thick uniform dark-brown outline (#531c12)
[POSE / EMOTION / STATE] turnaround front, 3/4, side, back; relaxed standing; plus head-only expressions: smug smirk, talk grin, wink grin, neutral
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] character sheet, full body, 1536x1024
[LIGHTING] flat even light
[BACKGROUND] transparent
[AVOID] text, logos on cap, watermark, extra characters, ears, nose, fingers, hair
```

## Consistency notes
- Cap always backwards and red; sunglasses always on the cap, never on the eyes.
- Stubble dots are his only facial texture — keep them.
- Same outline weight and head size as Lenny so they read as the same world.
