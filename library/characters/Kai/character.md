# Kai — the castaway

- **Role:** sole on-screen character and stand-in for the viewer ("you") in video 01 *This Tree Hates You*
  (`1/This Tree Hates You.mp4`). Every misfortune the narrator describes happens to Kai.
- **Screen time:** visible in 15 of 21 shots (and as an X-ray skeleton, a POV pair of hands and a thermal-camera
  figure). Not visible in S02 (aerial; only a speck), S03 (poster), S05 (radar), S07 (leaf), S09 (skin), S11 (car).
- **Assigned name check:** the assigned description is correct, with these corrections and additions:
  - The head is very pale **lavender-grey/white** (#dce0e9 lit, #b1b4ce–#babfcf shaded). It reads "lavender" in
    shade and blue at night because of the scene grade.
  - The hair is 2–3 thin curly sprouts on the crown, not a solid tuft.
  - Shirt flowers are cream/white 5-petal hibiscus-like flowers with **red centres** and **dark-green leaves** on
    orange (#e05f13).
  - The sandals are thin flip-flops with yellow soles.
  - A dark diagonal stroke runs across the shirt front in most poses (the near arm drawn across the torso).
  - The head and outline take on the scene grade: cream with a warm brown outline at sunset (S12), blue at night
    (S17), and grey inside smoke.

## Design spec
| Part | Spec |
|---|---|
| Proportions | ~3.4 head-heights tall (measured f00400: head 150 px, shirt torso 150 px, shorts 40 px, legs 170 px). Head ≈ 1.0, torso ≈ 1.0, shorts ≈ 0.25, legs ≈ 1.15. Head width ≈ 1.15 × torso width. |
| Head | Big, slightly egg-shaped circle (a little wider at the top), flat fill #dce0e9 with one soft shadow tone #babfcf on the lower/back side; tiny light rim. No ears, no nose. |
| Outline | Thick, uniform, dark navy-charcoal #232838–#2f3d43 (~5–6 px at 720 px width on an MS head; ~10 px in CU). Slightly darker/heavier than the environment's contour lines. Night: #140916. |
| Hair | 2–3 thin dark curly sprouts (single strokes) on the crown, slightly off-centre. |
| Eyes | Default: small solid dark dots (#1e0912). Alternatives: ring eyes (open circle + dot pupil), closed arcs, flat half-lid lines, `><` chevrons, X's. |
| Brows | Single short dark strokes (curved or angled), float high on the head. They drive most of the acting. |
| Mouth | Tiny line or curve; alternatives: wavy "moustache" mouth, rounded-rectangle gritted teeth with a grid, small "o", toothy grin. |
| Cheeks | Pink blush ovals (#f0a0a8) only in E16 and under-eye red patches (#d86a6a) in E22–E24. |
| Torso | Elongated rounded capsule/bean, wider at the bottom, filled by the shirt. |
| Shirt | Short-sleeve Hawaiian shirt, orange #e05f13 (shadow #b94a0f), cream flowers #f3e6d3 (warm-lit #e69f63), flower centres red #ba190f, leaves dark green #1a6747 / #55693e. A centre placket line runs down the front. |
| Shorts | Navy #3b3f6a / #445181, short and boxy. |
| Limbs | Thin noodle sticks (a double outline with a pale tan fill, ~6 px wide). The hands are tiny ball/blob ends (white balls in POV). No fingers except rare grasp shapes. |
| Shoes | Thin flip-flop sandals with yellow soles (#e0c050). |
| Extras (VFX on the head) | Blue sweat drop (#6488aa outline dark), blue tear streams (#829aad), pink blisters (#e8a0b0 balls), red anger vein, frost zigzags, red heat fill, green sick tint (#9fbf9a). |

## Colour hex list
`#dce0e9` head lit · `#babfcf` head shade · `#b1b4ce` head (day MS average) · `#2f3d43` outline day · `#140916`
outline night · `#1e0912` eyes/brows · `#e05f13` shirt · `#b94a0f` shirt shade · `#f3e6d3` flower · `#ba190f`
flower centre · `#1a6747` leaf print · `#3b3f6a` shorts · `#445181` shorts light · `#e0c050` sandal sole ·
`#6488aa` sweat · `#829aad` tears · `#da767a` red-hot head · `#e8a0b0` blisters · `#f0a0a8` blush.

## Personality
He's an easy-going, gullible beach tourist: happy closed-eye smiles and smug smirks until something goes wrong, then
deadpan "of course" looks. He's resilient and keeps trying the next idea (shelter → apple → leaves → fire). The
comedy comes from the **deadpan beat after each disaster** (E07 unimpressed appears 7 times).

## Master prompt (character sheet / turnaround)
```
[REFERENCE] attach: library/characters/Kai/reference/ref_00400.jpg (+ ref_01805.jpg for the face)
[SUBJECT] Kai, a cartoon castaway stick-figure: very large round pale-lavender-white head (#dce0e9) with a soft
lavender shadow (#babfcf), thick uniform dark navy-charcoal outline, 2–3 thin curly hair sprouts on top, tiny dot
eyes, single-stroke eyebrows, small line smile, no nose, no ears; elongated capsule torso wearing a short-sleeve
orange (#e05f13) Hawaiian shirt with cream 5-petal flowers with red centres and dark-green leaves, navy boxy shorts
(#3b3f6a), thin noodle stick arms and legs with tiny ball hands, thin yellow-soled flip-flops. Total height about
3.4 head-heights.
[POSE / EMOTION / STATE] character turnaround sheet: front, 3/4, side, back, all standing relaxed with arms down, neutral
calm face (dot eyes, small smile); plus 4 small head-only expression thumbnails (happy closed eyes, worried ring
eyes with sweat drop, unimpressed half-lidded, wincing >< with gritted teeth)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
[COMPOSITION] 16:9 1536x1024 sheet, evenly spaced, same scale for every view, orthographic, eye-level
[LIGHTING] flat even light, single soft shadow tone, no cast shadows
[BACKGROUND] transparent
[AVOID] text, labels, captions, watermark, extra characters, realistic anatomy, fingers, nose, ears, gradients on clothes, thin or sketchy outlines
```

## Consistency notes
- Keep the **head colour and outline weight** constant. Scene mood comes only from a colour grade over the composited
  character (day: neutral; sunset: warm cream + brown outline; night: blue multiply; smoke: grey haze; fire: orange rim).
- The face is a separate swappable layer (eyes + brows + mouth + extras) on a fixed head. The 24 emotions (see
  `emotions/emotions.md`) are combinations from a small set of parts: eyes {dot, ring+dot, arc closed, flat half-lid,
  `><`, X, bloodshot ring}, brows {neutral, raised, angled-down, worried-up, one-raised}, mouth {small smile,
  flat, wavy, gritted rect, o, toothy grin}, extras {sweat drop, tears, blush, red lid patches, vein, blisters,
  frost, steam, red fill, green tint}.
- Body poses are simple rigid-limb puppets (AE/Moho-style bones). Limbs are drawn as strokes, so they bend freely.
- Shirt flowers stay fixed in torso space; they do not re-pattern between poses.
- In CU shots (S08, S18, S20) the head fills 60–70 % of the frame width and the outline scales with it.
