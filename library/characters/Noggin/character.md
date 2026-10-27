# Noggin

- **Role:** The brain inside Dex's head: a frantic artist at a drawing desk who "records" the fall frame by frame.
- **Video:** 04 "The Scientist's Insane Time Test" (analysis/videos/04_the_scientists_insane_time_test)
- **Personality:** Hard-working, overwhelmed, frantic when the alarm goes off. A comic stand-in for the brain's memory system.

## Design spec

| Part | Spec |
|---|---|
| Body/head | One pink brain blob (#f2c0c6), wider than tall (≈1.4:1), flattened dome. Darker pink gyri squiggles (#d2979e). Outline #2a2024 |
| Accessory | Light-green translucent **visor band** (#8bd391, darker edge #4f9a63) around the middle with a front brim, plus a yellow pencil tucked into it |
| Face | On the lower front of the brain. Eyes: flat half-lids / hollow ring eyes / squint lines. Brows: thick strokes (V when angry). Mouth: wavy line or grid of teeth. Pale-blue sweat drop on the right temple when stressed |
| Limbs | Black noodle arms with ball hands (one holds a pencil). Legs are hidden by the stool |
| Seat | Small round wooden stool, warm brown #a7523a |
| Scale | Seated, about 0.45 frame height in MS. Appears tiny inside Dex's pupil (214–223) |
| Set | Round brain room: cream walls, wood floor, rainbow rug, bookshelf, porthole windows, green desk lamp, drawing desk, PANIC button box, red alarm dome light |


## Colour hex list
#f2c0c6 brain · #d2979e gyri · #2a2024 outline · #8bd391 visor · #4f9a63 visor edge · #f2c94c pencil · #9fd3f0 sweat drop

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Noggin/reference/ref_00238.jpg
[SUBJECT] Noggin: a cartoon brain character, a pink brain blob (#f2c0c6) wider than tall, flattened dome, darker pink wavy gyri lines (#d2979e), thick dark outline (#2a2024), a light-green translucent visor/headband (#8bd391) wrapped around its middle with a short brim at the front, a yellow pencil tucked in the band, simple face on the lower front (eyes + mouth, no nose), thin black noodle arms with ball hands, sits on a small round wooden stool.
[POSE / EMOTION / STATE] Character sheet: front, 3/4, side and back views (seated on stool and standing), plus face expressions (bored half-lid, startled, squint strain, frantic, angry determined)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
[COMPOSITION] Square 1024x1024, full body, same scale
[LIGHTING] Flat even light
[BACKGROUND] transparent
[AVOID] text, captions, watermark, extra characters, realistic skin, gradients on the head, 3D-rendered character body
```

## Consistency notes
The visor band and pencil are always present. The face sits low on the brain front. When turning away the face fades out completely (back view = only gyri and visor).
- References: ref_00238.jpg in `reference/`.
- Poses: see `poses/poses.md`. Emotions: see `emotions/emotions.md`.
