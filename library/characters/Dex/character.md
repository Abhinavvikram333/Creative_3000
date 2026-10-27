# Dex

- **Role:** The volunteer who gets dropped off the free-fall tower; the story is his memory (flipbook) of the fall.
- **Video:** 04 "The Scientist's Insane Time Test" (analysis/videos/04_the_scientists_insane_time_test)
- **Personality:** An ordinary, slightly gullible everyman. Terrified in the moment, then deadpan or smug, and finally a proud storyteller who bores his friends with the "slow-motion" fall.

## Design spec

| Part | Spec |
|---|---|
| Head | Perfect circle, warm off-white #f3eeed, outline #2a2024 about 6–8 px at 720p (≈1 % of frame width). No nose, no ears |
| Hair | Brown #6c4d3e mop with a side part. Fully visible only when the cap flies off (fall 1–213, landing 719–856) |
| Cap | Red baseball cap #d64444 (shade #c6443c), **worn backwards**: the dark strap opening sits over the forehead, red top button. It flies off at f1 and is back on in shots 4 and 7–9 |
| Eyes | Calm: small black dots or half-lid lines. Scared: big hollow **ring eyes** (white circle, thick outline, black dot pupil) |
| Brows | Single thick dark strokes, only drawn when acting |
| Mouth | Line, wavy line, "o", or a rectangular **grid of teeth** (terrified grimace) |
| Torso | Bean/capsule. Mustard-yellow T-shirt #e8ae2d (final scene) under an **orange safety harness vest** #dd7c21 with yellow lining #f4c33a, white/orange dashed stitch lines and two grey square buckles at chest and belly |
| Props | CHRONO-2 wrist display (dark maroon housing #3a1b1f, red LEDs #e94d42) on the left wrist. Holds the rubber-banded flipbook in the finale |
| Limbs | Black noodle arms and legs (~5 px), black ball hands, legs end in simple tips (no shoes drawn) |
| Proportions | About 4 head-heights: head 1, torso 1.3, legs 1.6 |
| Drawn variant | On the blueprint (616–711) he is a chalk stick figure with a cap and harness. On the flipbook page (1171–1200) he is ink-and-flat-colour |


## Colour hex list
#f3eeed head · #2a2024 outline/limbs · #d64444 cap · #c6443c cap shade · #6c4d3e hair · #e8ae2d shirt · #dd7c21 harness · #f4c33a harness lining · #9a9aa0 buckles · #3a1b1f device · #e94d42 LED

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Dex/reference/ref_00480.jpg
[SUBJECT] Dex: a cartoon young man with a perfectly round warm off-white head (#f3eeed), thick dark-brown/black outline (#2a2024), red baseball cap (#d64444) worn BACKWARDS so the brown strap opening shows over the forehead and a small red button sits on top, a little brown hair (#6c4d3e) peeking out, no nose, no ears; bean-shaped torso in a mustard-yellow T-shirt (#e8ae2d) under an orange safety harness vest (#dd7c21) with yellow lining (#f4c33a), dashed stitch lines and grey square buckles, a dark-maroon wrist display with red LEDs on the left wrist, thin black noodle arms with black ball hands, thin black noodle legs.
[POSE / EMOTION / STATE] Character turnaround sheet: front, 3/4, side and back views standing neutral with arms at sides, plus a small row of 6 face expressions (terrified ring eyes + grid teeth, deadpan half-lid, smug smirk, worried ring eyes, dizzy spiral eyes, big closed-eye grin)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024 sheet, evenly spaced views, full body, same scale
[LIGHTING] Flat even light, no cast shadow
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, nose, ears, realistic skin, gradients on the head, 3D-rendered character body
```

## Consistency notes
Keep the cap BACKWARDS with the strap opening visible over the forehead. Keep the ring eyes for any fear state. The harness always has the dashed stitches and grey buckles. Without the cap he must show the brown mop hair. The wrist device is on his left wrist.
- References: ref_00070.jpg, ref_00480.jpg, ref_01085.jpg in `reference/`.
- Poses: see `poses/poses.md`. Emotions: see `emotions/emotions.md`.
