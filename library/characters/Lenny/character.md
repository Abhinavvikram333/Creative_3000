# Lenny

- **Role**: the gambler / "you" of the narration — the viewer's stand-in who gets teased by the slot machine.
- **Video(s)**: 05 "The Science Behind Slot Machines" (`analysis/videos/05_the_science_behind_slot_machines`), frames
  21–133, 134–340, 345–390 (hand only), 423–541, 784–928.
- **Assigned description check**: correct — white round head, messy hair (very dark brown, reads black), teal shirt
  with yellow leaf pattern, red lanyard + red badge. Added: stick legs/noodle arms in the outline colour, blob hands.

## Design spec
| Part | Spec |
|---|---|
| Head | Large near-circle, slightly wider than tall (≈1.05:1), cream-white **#fcf6e7**, warm edge shading **#f0c6af**, takes warm rim glow from the scene. No ears, no nose. |
| Outline | Uniform thick dark brown **#421411** (≈8–10 px on a 300 px head ≈3 %), slightly wobbly hand-drawn line. |
| Hair | Messy cap of dark brown-black **#351518** clumps sweeping right-to-left over the top third of the head, 4–6 spiky tufts, soft purple-grey sheen **#5f4447**; a thick swoop hangs behind the head in 3/4 view. |
| Eyes | Default: two small solid dark-brown ovals spaced ~0.35 head width; variants: heavy-lidded half ovals, closed lines, big ring "O" eyes. |
| Brows | Single short thick strokes, used heavily for emotion (flat, angled, V). |
| Mouth | Tiny: small curve, small "o", or a rectangle of teeth (grit/grin). |
| Cheeks | none. |
| Body | Soft capsule/bean torso ≈1.6 head-heights tall, same width as the head, teal **#19bda4** shirt (collar visible, no visible buttons) with scattered mustard-yellow **#e9c23a** leaf/banana-shaped motifs. |
| Accessories | Red **#cd1a15** lanyard strap down the chest with a small rectangular red badge (white/yellow stripe detail). |
| Limbs | Noodle arms and legs drawn as single thick outline-colour strokes, no clothing on them; hands are dark blobs (no fingers). |
| Shoes | none visible (legs end in points / hidden by stool). |
| Proportions | ≈4.3 head-heights total: head 1, torso 1.6, legs ≈1.7. |

Colour list: #fcf6e7 · #f0c6af · #421411 · #351518 · #5f4447 · #19bda4 · #138f7d · #e9c23a · #cd1a15 · #f5efe7

## Personality
Hopeful-then-jaded everyman gambler: gets excited fast (manic grin at the two 7s), turns skeptical and deadpan, gets
suspicious ("teasing me on purpose"), then determined enough to rip the machine open. Ends utterly unimpressed.
Default resting face = deadpan.

## Reference crops
- `reference/ref_00230.jpg` — seated full body, content face (clearest overall design)
- `reference/ref_00038.jpg` — seated full body, early content face
- `reference/ref_00457.jpg` — face close-up with rim light (best face detail)
- `reference/ref_00914.jpg` — standing 3/4 turn, deadpan (hair mass behind head)

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Lenny/reference/ref_00230.jpg (+ ref_00914.jpg for the 3/4 view)
[SUBJECT] "Lenny", a simple cartoon man: very large round cream-white head (#fcf6e7) with no ears and no nose, messy
dark brown-black hair (#351518) in spiky clumps sweeping over the top of the head, two small dark-brown oval dot eyes,
short thick single-stroke eyebrows, tiny curved mouth; bean-shaped torso in a teal (#19bda4) short-sleeve shirt with
small mustard-yellow (#e9c23a) leaf motifs, red (#cd1a15) lanyard with a small red ID badge on the chest; arms and legs
are thin dark-brown noodle strokes, hands are small dark blobs; thick uniform dark-brown outline (#421411).
[POSE / EMOTION / STATE] character turnaround: front, 3/4 left, side, 3/4 back; neutral relaxed standing pose, neutral
deadpan face (half-lidded eyes, flat small mouth); plus a row of 6 head-only expressions: content, manic grin, skeptical,
suspicious, determined (gritted teeth), deadpan.
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] character sheet, evenly spaced, full body, 1536x1024 landscape, orthographic-feeling eye-level view
[LIGHTING] flat even light, no cast shadows
[BACKGROUND] transparent
[AVOID] text, labels, captions, watermark, extra characters, ears, nose, fingers, realistic anatomy, gradients on the clothes
```

## Consistency notes
- Head size must stay huge (≈1/4 of total height standing, ≈1/3 seated) — this is the style's signature.
- Outline colour is dark *brown*, not black; limbs are the same brown strokes.
- Hair always covers the top third of the head and overhangs to the left in front view.
- Leaf motifs are small, sparse and scattered; never stripes.
- The lanyard + badge is always present (even in the X-ray finale).
- Faces are swapped as whole sprites (eyes+brows+mouth) — keep head shape and hair identical across emotions.
