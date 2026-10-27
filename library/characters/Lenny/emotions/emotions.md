# Lenny — emotions (video 05)

Face-only crops (PNG) from full-res frames. All emotions share the same head shape, hair and outline; only eyes,
brows and mouth change → build as **swappable face sprites** (eyes / brows / mouth layers or whole-face sprites).

| id | Crop | Eyes | Brows | Mouth | Extras | Frame ranges (30 fps) | Narration trigger |
|---|---|---|---|---|---|---|---|
| content | `emo_content_f00457.png` | round dark dots (highlights in CU) | none/neutral | small upward curve | — | 27–41, 45–48, 223–232, 456–458 | "You just watched…", "the exact same thing", "teasing" (false hope) |
| eyes_closed_smile | `emo_eyes_closed_smile_f00043.png` | two flat closed lines | — | small smile | — | 42–44 | "jackpot" (savouring) |
| manic_grin | `emo_manic_grin_f00060.png` | big ring "O" eyes with small pupils | — | wide open grin, row of teeth | — | 49–71 | "jackpot symbols land" |
| smug_grin | `emo_smug_grin_f00074.png` | half-lidded / line eyes | flat | wide flat toothy grin | — | 72–76 (morph), 529–531 | transition after "land."; "crack it open" (yank) |
| skeptical | `emo_skeptical_f00077.png` | half-lidded ovals | one brow raised/angled | small "o" | — | 77–99, 102–145, 241–250, 311–340 | "the third one stopped one click short", "Bro, it's just warming up" (side-eye) |
| blink | `emo_blink_f00100.png` | closed lines | flat | small "o" | — | 100–101, 146–147, 233–234, 452–453, 461–462 | — (2-frame blinks) |
| deadpan | `emo_deadpan_f00150.png` | heavy half-lids over pupils | flat, slightly raised | tiny flat line | — | 148–216, 235–240, 251–310, 806–813, 889–928 | "you moved to the machine next door", buddy's line, final "than on the jackpot" |
| smirk | `emo_smirk_f00222.png` | half-lidded | flat | small side smile | — | 217–222 | "same" (wry hope) |
| curious_brow | `emo_curious_brow_f00455.png` | round, big | one brow raised high | small smile | — | 454–455, 459–460 | "teasing" (flicker of hope) |
| suspicious | `emo_suspicious_f00440.png` | half-lidded, pupils pushed to the side | V-furrowed | small "o" | — | 423–451, 463–494 | "the machine is teasing you on purpose" |
| determined | `emo_determined_f00508.png` | half-lidded, stern | strong V | rectangle of gritted teeth | — | 495–528 | "So, let's crack it open" |

No sweat drops, tears, blush or vein marks in this video.

## Expression timeline (frame → emotion, hold length)
```
#21–26   (face not yet in frame)
#27–41   content            15 f
#42–44   eyes_closed_smile   3 f
#45–48   content             4 f
#49–50   morph → manic       2 f
#51–71   manic_grin         21 f
#72–76   smug_grin (morph)   5 f
#77–99   skeptical          23 f
#100–101 blink               2 f
#102–145 skeptical          44 f   (jump cut + re-pose at #134, same face)
#146–147 blink               2 f
#148–216 deadpan            69 f
#217–222 smirk               6 f
#223–232 content            10 f
#233–234 blink               2 f
#235–240 deadpan             6 f
#241–250 skeptical          10 f
#251–310 deadpan            60 f   (POV shot)
#311–340 skeptical          30 f   (side-eye at Bling)
#341–422 (hand / not visible)
#423–451 suspicious         29 f
#452–453 blink               2 f
#454–455 curious_brow        2 f
#456–458 content             3 f
#459–460 curious_brow        2 f
#461–462 blink               2 f
#463–494 suspicious         32 f
#495–528 determined         34 f
#529–531 smug_grin           3 f
#532–805 (not visible / body only)
#806–813 deadpan             8 f
#814–888 (head out of frame)
#889–928 deadpan            40 f
```
**Switch speed**: 26 face changes in ~19 s of visible face. Main holds 20–70 f (0.7–2.3 s), "flicker" sequences use
2–6 f holds (#42–48, #452–462), blinks are always exactly 2 f. Changes are cuts with 1–2 soft in-between frames
(morph look), not eased tweens → a face-swap system needs: sprite cut + optional 1-frame cross-blend, a blink layer
(2 f), and the ability to sequence 2-frame holds.

## Prompts (same face, transparent background)
Every prompt: `[REFERENCE] attach: library/characters/Lenny/reference/ref_00457.jpg` **plus** the emotion crop.

### content
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_content_f00457.png (+ library/characters/Lenny/reference/ref_00457.jpg)
[SUBJECT] Lenny's head only: huge round cream-white (#fcf6e7) head, no ears/nose, messy dark brown-black hair clumps over the top third, thick dark-brown outline (#421411)
[POSE / EMOTION / STATE] content: two round dark-brown dot eyes with a tiny white highlight, no brows, small upward-curved smile; front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, centred, 1024x1024, eye level
[LIGHTING] flat, very faint warm rim
[BACKGROUND] transparent
[AVOID] text, watermark, body, ears, nose, cheeks blush, extra characters
```

### eyes_closed_smile
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_eyes_closed_smile_f00043.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only (as in content)
[POSE / EMOTION / STATE] blissful: eyes are two short flat closed lines, no brows, small soft smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body, ears, nose
```

### manic_grin
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_manic_grin_f00060.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] manic excitement: big ring-shaped "O" eyes (outline circles with small dark pupils), very wide open grin showing a row of square teeth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body, ears, nose, tongue
```

### smug_grin
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_smug_grin_f00074.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] smug: half-lidded flat eyes (straight upper lids), wide flat grin with a thin strip of teeth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### skeptical
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_skeptical_f00077.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] skeptical: half-lidded oval eyes, left brow flat, right brow angled up, small round "o" mouth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### blink
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_blink_f00100.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] blink: eyes as two straight closed lines, flat short brows, small "o" mouth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### deadpan
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_deadpan_f00150.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] deadpan/bored: heavy half-closed lids covering the top half of the pupils, flat slightly raised brows, tiny flat mouth line
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### smirk
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_smirk_f00222.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] wry smirk: half-lidded eyes, flat brows, small one-sided smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### curious_brow
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_curious_brow_f00455.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] curious/hopeful: big round eyes, one brow raised high in an arch, small smile
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat, warm rim
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### suspicious
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_suspicious_f00440.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only, turned slightly to his right
[POSE / EMOTION / STATE] suspicious glare: brows angled down into a V, half-lidded eyes with pupils pushed to the side, small round "o" mouth
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] warm orange rim on one side
[BACKGROUND] transparent
[AVOID] text, watermark, body
```

### determined
```
[REFERENCE] attach: library/characters/Lenny/emotions/emo_determined_f00508.png (+ ref_00457.jpg)
[SUBJECT] Lenny's head only
[POSE / EMOTION / STATE] determined/angry: strong V brows, stern half-lidded eyes, mouth a small rectangle of gritted teeth (grid of 4–6 teeth)
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] head-only sprite, 1024x1024
[LIGHTING] flat
[BACKGROUND] transparent
[AVOID] text, watermark, body
```
