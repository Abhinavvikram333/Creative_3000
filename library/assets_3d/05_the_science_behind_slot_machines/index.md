# 3D-looking assets / props — 05 "The Science Behind Slot Machines"

STYLE LOCK (verbatim): `Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.`

| id | Crop | Description | Frames | Looks like | Suggested build |
|---|---|---|---|---|---|
| a_slot_machine_lucky7s | `a_slot_machine_lucky7s_f00508.jpg` | Hero slot machine: tall red cabinet, arched topper with marquee bulbs and gold 'LUCKY 7s' logo, WIN LED, 'PLAY 3 CREDITS ★ 1 LINE · $1 GAME ★', 3-reel window with red payline, CREDITS LED + bill acceptor at right, CASH OUT/BET ONE/MAX BET + SPIN deck, paytable panel 'LUCKY 7s PAYS', speaker grille at bottom | 1–928 (every shot) | outlined 3D render (toy-like, painted textures, ink contours) | **Build in Blender** (reused in every shot, needs a hinged front door + X-ray variant); textures from AI images |
| a_reel_window_near_miss | `a_reel_window_near_miss_f00440.jpg` | Reel window close-up showing the near miss: 7 · 7 on the payline, reel 3 with the 7 just above the line and a cherry on it; chrome bevel, red payline with arrow markers | 1–133, 236, 425–494, 870–928 | outlined 3D render | Blender (reels must spin and stop on cue) |
| a_progressive_led_sign | `a_progressive_led_sign_f00200.jpg` | Hanging black progressive sign, gold frame, header 'LUCKY 7s PROGRESSIVE', red 7-segment '$1,284,535.04' ticking up each frame, small 7 icons at the ends | 148–252, 900–928 | outlined 3D render; digits likely overlay/animated | Blender plane + text/number driver (or AE) so the amount ticks precisely |
| a_bill_acceptor_spin_button | `a_bill_acceptor_spin_button_f00370.jpg` | Black bill acceptor with glowing green slot and yellow print '$1 $5 $10 $20 $50 $100 / INSERT BILL FACE UP', next to a big glossy red dome 'SPIN' button | 341–422 | outlined 3D render | Blender (slot glow emission animates when bill enters) |
| a_dollar_bill_100 | `a_dollar_bill_100_f00370.jpg` | Cartoon green $100 bill with a round cartoon-face portrait in an oval, '100' corners, 'THE UNITED STATES OF AMERICA' microtext | 341–399 | 2D-ish flat prop in 3D space | Image (flat card) animated sliding into the slot |
| a_credits_counter | `a_credits_counter_f00418.jpg` | Red cabinet panel with yellow 'CREDITS' label above a chrome-framed red 7-segment display reading '100' | 400–424 | outlined 3D render, digits animated | Blender/AE: digits driven 0→100 in 9 frames |
| a_bar_stool | `a_bar_stool_f00508.jpg` | Casino barstool: red ribbed round cushion with buttoned top, chrome post with foot ring and round chrome base | 1–250, 495–541, 900–928 | outlined 3D render | Blender (simple lathe model) |
| a_coin_cup_777 | `a_coin_cup_777_f00290.jpg` | Paper/plastic coin cup, white with red band reading '777' | 148–340 | outlined 3D render | Image card or Blender cylinder |
| a_machine_door_open | `a_machine_door_open_f00530.jpg` | Machine front panel swinging open on a hinge (reel window, credits, acceptor attached to the door) revealing a glowing orange interior | 529–541 | true 3D (perspective-correct hinge swing) | **Blender** (hinged door, 4-frame swing) |
| a_reel_unit_pcb | `a_reel_unit_pcb_f00550.jpg` | Reel unit: 3 cream reel drums on a bracket, label plate 'LUCKY 7s REEL UNIT', green PCB with 'RNG' chip, orange wires, stepper box | 542–778 | outlined 3D render | Blender (reel 3's strip must peel/unroll) |
| a_tally_counter | `a_tally_counter_f00776.jpg` | Cream mechanical hand tally counter with a key ring, black window showing 'x14' (white digits on black drums) | 690–928 | outlined 3D render; digits animated | Blender/AE number roll (x00→x14) |
| a_rubber_stamp | `a_rubber_stamp_f00714.jpg` | Orange rectangular rubber stamp with a red ball knob, stamp face reading 'ONE CLICK SHORT' | 690–770 | outlined 3D render | Blender (simple box + sphere), slam animation 3–4 f per hit |
| a_bill_validator | `a_bill_validator_f00760.jpg` | Black internal box labelled 'BILL VALIDATOR' with a green '$' and a green light strip | 720–780 | outlined 3D render | Blender / image card |

## Prompts

### a_slot_machine_lucky7s
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_slot_machine_lucky7s_f00508.jpg
[SUBJECT] a red casino slot machine 'LUCKY 7s': arched topper with gold marquee bulbs and a big red-gold '7s' logo reading 'LUCKY 7s', small red LED 'WIN 0', header 'PLAY 3 CREDITS ★ 1 LINE · $1 GAME ★', three-reel window (7, 7, cherry) with a red payline, red 'CREDITS' LED display and black bill acceptor with green slot on the right, button deck CASH OUT (blue), BET ONE (yellow), MAX BET (orange), red dome SPIN button, lower paytable 'LUCKY 7s PAYS'
[POSE / EMOTION / STATE] front three-quarter view, whole machine
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024, centred, full object
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_reel_window_near_miss
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_reel_window_near_miss_f00440.jpg
[SUBJECT] close-up of a slot machine reel window with chrome bevel: three cream reels, two red 7s on the red payline, the third reel stopped with its red 7 just above the payline and a cherry on the line
[POSE / EMOTION / STATE] near-miss state, sharp
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024, slight dutch angle
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_progressive_led_sign
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_progressive_led_sign_f00200.jpg
[SUBJECT] a hanging casino progressive jackpot sign: black LED panel in a gold frame, header 'LUCKY 7s PROGRESSIVE' in gold letters, red seven-segment digits '$1,284,532.82', small red 7 icons at both ends
[POSE / EMOTION / STATE] front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] wide 1536x512 (crop to need)
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_bill_acceptor_spin_button
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_bill_acceptor_spin_button_f00370.jpg
[SUBJECT] a black slot-machine bill acceptor with a glowing green slot and yellow printed '$1 $5 $10 $20 $50 $100' and 'INSERT BILL FACE UP', beside a large glossy red dome push button labelled 'SPIN'
[POSE / EMOTION / STATE] high angle, slot glowing
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_dollar_bill_100
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_dollar_bill_100_f00370.jpg
[SUBJECT] a cartoon green $100 bill, flat illustrated, round cartoon face portrait in a central oval, large '100' in the corners, small seal, slight curl
[POSE / EMOTION / STATE] flat, slightly curved
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] landscape 1536x768
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_credits_counter
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_credits_counter_f00418.jpg
[SUBJECT] a red slot machine panel with a yellow 'CREDITS' label above a chrome-framed black display showing red seven-segment digits '100'
[POSE / EMOTION / STATE] close-up
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_bar_stool
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_bar_stool_f00508.jpg
[SUBJECT] a casino barstool with a red ribbed round cushion, chrome post, chrome foot ring and a round chrome base
[POSE / EMOTION / STATE] three-quarter view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_coin_cup_777
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_coin_cup_777_f00290.jpg
[SUBJECT] a white plastic casino coin cup with a red band printed '777', slightly tapered
[POSE / EMOTION / STATE] front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_machine_door_open
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_machine_door_open_f00530.jpg
[SUBJECT] a red slot machine with its whole front panel (reel window, credits display, bill acceptor) swung open on a side hinge, revealing a warm glowing orange interior with three physical reel drums
[POSE / EMOTION / STATE] door open 75°
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_reel_unit_pcb
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_reel_unit_pcb_f00550.jpg
[SUBJECT] a slot machine reel unit: three cream reel drums with red 7, BAR and cherry symbols on a metal bracket, a label plate 'LUCKY 7s REEL UNIT', below it a green circuit board with a black chip labelled 'RNG' and orange wires
[POSE / EMOTION / STATE] front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_tally_counter
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_tally_counter_f00776.jpg
[SUBJECT] a cream-coloured mechanical hand tally counter with a small ring on the left and a black window showing 'x 1 4' on rolling digit drums
[POSE / EMOTION / STATE] front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_rubber_stamp
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_rubber_stamp_f00714.jpg
[SUBJECT] an orange rectangular rubber stamp with a round red ball handle, the side label reading 'ONE CLICK SHORT'
[POSE / EMOTION / STATE] three-quarter view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
### a_bill_validator
```
[REFERENCE] attach: library/assets_3d/05_the_science_behind_slot_machines/a_bill_validator_f00760.jpg
[SUBJECT] a black box component labelled 'BILL VALIDATOR' with a green '$' symbol and a thin green glowing slot
[POSE / EMOTION / STATE] front view
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] square 1024x1024
[LIGHTING] warm tungsten casino light, soft bloom
[BACKGROUND] transparent
[AVOID] text other than the exact labels given, watermark, people, hands
```
