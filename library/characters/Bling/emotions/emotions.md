# Bling — emotions (video 05)

| id | Crop | Eyes | Brows | Mouth | Extras | Frame ranges | Narration trigger |
|---|---|---|---|---|---|---|---|
| wink_grin | `emo_wink_grin_f00337.png` | one eye closed (curved line), other squinting | one raised | wide open grin, upper teeth with a gap | stubble | 255–286, 335–340 | "Your buddy leans over", "warming up." |
| smug_smirk | `emo_smug_smirk_f00290.png` | half-lidded, looking right | flat / one raised | closed one-sided smile | stubble | 287–296, 304–309, 314–317, 324–325 | "says," / between talk flaps |
| talk_grin | `emo_talk_grin_f00297.png` | half-lidded | raised | open toothy mouth (talking) | stubble | 297–303, 310–313, 318–323, 326–334 | "Bro, it's just warming up" (lip flap) |
| neutral | `emo_neutral_f00499.png` | round dot eyes | none | small closed mouth | stubble | 175–188 (profile), 497–520 | background presence |

## Expression timeline
```
#175–188 neutral (profile, edge of frame)
#255–286 wink_grin   32 f
#287–296 smug_smirk  10 f
#297–303 talk_grin    7 f
#304–309 smug_smirk   6 f
#310–313 talk_grin    4 f
#314–317 smug_smirk   4 f
#318–323 talk_grin    6 f
#324–325 smug_smirk   2 f
#326–334 talk_grin    9 f
#335–340 wink_grin    6 f
#497–520 neutral     (behind Lenny)
```
Dialogue = **2-state lip flap** (talk_grin ↔ smug_smirk) with irregular 2–9 f holds, not phoneme sync; the line opens
and closes on a wink.

## Prompts (same face, transparent background)

### wink_grin
```
[REFERENCE] attach: library/characters/Bling/emotions/emo_wink_grin_f00337.png (+ library/characters/Bling/reference/ref_00290.jpg)
[SUBJECT] Bling's head only: big round cream-white head (#fdf7dd), red backwards cap with black sunglasses resting on it, brown stubble dots on the jaw, thick dark-brown outline (#531c12)
[POSE / EMOTION / STATE] cheeky wink: left eye closed as a curved line, right eye squinting, one brow raised, wide open grin showing upper teeth with a small gap; head tilted slightly
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat, faint warm rim
[BACKGROUND] transparent
[AVOID] text, logos, watermark, body, ears, nose
```

### smug_smirk
```
[REFERENCE] attach: library/characters/Bling/emotions/emo_smug_smirk_f00290.png (+ ref_00290.jpg)
[SUBJECT] Bling's head only (as above)
[POSE / EMOTION / STATE] smug: half-lidded eyes glancing right, one brow slightly raised, closed one-sided smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, logos, watermark, body
```

### talk_grin
```
[REFERENCE] attach: library/characters/Bling/emotions/emo_talk_grin_f00297.png (+ ref_00290.jpg)
[SUBJECT] Bling's head only (as above)
[POSE / EMOTION / STATE] talking: half-lidded eyes, raised brows, mouth open in a toothy grin (upper teeth visible, gap tooth)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, logos, watermark, body, tongue
```

### neutral
```
[REFERENCE] attach: library/characters/Bling/emotions/emo_neutral_f00499.png (+ ref_00290.jpg)
[SUBJECT] Bling's head only (as above)
[POSE / EMOTION / STATE] neutral: two small round dot eyes, no brows, small closed mouth, stubble dots
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, logos, watermark, body
```
