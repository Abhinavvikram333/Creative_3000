# Backgrounds — 05 "The Science Behind Slot Machines"

STYLE LOCK (verbatim, from `analysis/videos/05_the_science_behind_slot_machines/visuals.md`):
`Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.`

All crops are full 720x1280 frames (the plate is the whole frame); characters cannot be avoided in most of them —
prompts ask for a clean plate.

| id | Crop(s) | Description | Time of day | Parallax layers (far / mid / near) | Palette | Shots |
|---|---|---|---|---|---|---|
| bg_casino_row | `bg_casino_row_wide_f00176.jpg` (widest, LED sign + full row), `bg_casino_row_f00205.jpg` | Casino floor: row of red "LUCKY 7s" slot machines with arched marquee-bulb toppers, a "GOLD RUSH" machine at left and a blue "DIAMOND" machine at right, red ribbed barstools on chrome posts, swirl-pattern dark carpet, wooden coffered ceiling with spotlights, big black "LUCKY 7s PROGRESSIVE $1,284,5xx.xx" red-LED sign hanging above | night/interior | far: ceiling + spotlights + LED sign · mid: machine row · near: stools, carpet | #2c0b0a #684334 #af2213 #c59a60 #f6e9d0 | S1, S2, S6, S8 (end) |
| bg_pov_ceiling | `bg_pov_ceiling_f00255.jpg` | View from inside a slot machine looking out: dark glass frame edges left/right, defocused reel strips across the bottom 25 %, coffered wooden ceiling with warm spotlights, distant blurred machines and patrons | night/interior | far: ceiling/machines · mid: characters · near: blurred reels + glass frame | #3e1712 #6b331f #a38372 #685a4e #f7e8d4 | S3 |
| bg_machine_panel_insert | `bg_machine_panel_insert_f00405.jpg` | High dutch close-up of the machine's red button deck: reel window edge with red payline, black bill acceptor with glowing green slot and "$20 $50 $100 / INSERT BILL FACE UP", red SPIN dome button, coloured small buttons, CREDITS LED top-right, red stool cushion and carpet blurred bottom-left | interior | far: carpet/stools · mid: deck · near: acceptor/SPIN | #c11815 #672822 #2b1612 #836755 #efefd4 | S4 |
| bg_machine_dutch_cu | `bg_machine_dutch_cu_f00440.jpg` | Dutch low-angle close-up of a LUCKY 7s machine face: big "LUCKY 7s" topper, WIN "0", "PLAY 3 CREDITS ★ 1 LINE · $1 GAME ★", reel window (7 · 7 · 7-above/cherry), CASH OUT / BET ONE / MAX BET, SPIN, paytable top edge, red stool top; neighbouring topper and ceiling light at right | interior | far: ceiling · mid: machine face · near: stool cushion | #3d0f0c #a21a16 #5d4d40 #a47d5c #faf1e1 | S5 |
| bg_machine_interior | `bg_machine_interior_f00550.jpg` | Inside the slot cabinet: warm amber plywood box with rivets and ink outlines, light strip at top, reel unit (3 cream drums, "LUCKY 7s REEL UNIT" plate), green PCB with "RNG" chip, orange wires, black stepper/speaker box, yellow warning labels, blue ribbon cable, barcode sticker, dust motes | interior | far: back wall · mid: reel unit/PCB · near: (paper strip, stamp, counter added per beat) | #80481f #ad7238 #f6bf5a #e09542 #fbf892 #327a0c | S7 |
| bg_xray_machine | `bg_xray_machine_f00840.jpg` | A LUCKY 7s machine where the upper half renders normally (reels, buttons) and the lower cabinet is an X-ray: dark interior with a cyan wireframe cage outlining the cabinet volume, wheel inside; neighbouring machines and carpet normal | interior | far: neighbouring machines · mid: wireframe machine · near: character | #261a20 #625354 #40a7a7 #bfa488 #eff4ec #b82b2d | S8 |

## Prompts

### bg_casino_row
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_casino_row_wide_f00176.jpg
[SUBJECT] casino floor plate: a row of glossy red "LUCKY 7s" three-reel slot machines with arched gold marquee-bulb toppers, one "GOLD RUSH" machine at far left, a blue "DIAMOND" machine at far right, red ribbed barstools on chrome posts in front of each machine, dark carpet with swirling gold/teal pattern, warm wooden coffered ceiling with round spotlights, a large black progressive jackpot sign with red LED digits "$1,284,532.82" and the header "LUCKY 7s PROGRESSIVE" hanging above
[POSE / EMOTION / STATE] empty, no people; reels showing 7 7 and a cherry
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, eye level from 2.5 m, machines filling the middle band, sign in the top fifth, empty floor space in the lower third for characters
[LIGHTING] warm tungsten spots, red LED glow, soft bloom on bulbs
[BACKGROUND] full scene
[AVOID] people, characters, captions, watermark, real casino brands (text only as given)
```

### bg_pov_ceiling
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_pov_ceiling_f00255.jpg
[SUBJECT] point of view from inside a slot machine looking out through its glass: dark glass frame edges at left and right, heavily blurred spinning reel strips across the bottom quarter, beyond the glass a warm wooden coffered casino ceiling with round spotlights and rows of distant blurred slot machines
[POSE / EMOTION / STATE] empty, no people
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, slightly low eye-level, empty middle band for two characters
[LIGHTING] dim warm, spotlights, faint glass reflections
[BACKGROUND] full scene
[AVOID] people, captions, text, watermark
```

### bg_machine_panel_insert
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_machine_panel_insert_f00405.jpg
[SUBJECT] extreme close-up of a red slot machine button deck: edge of the reel window with a red payline, a black bill acceptor with a glowing green slot and yellow printed "$1 $5 $10 $20 $50 $100" and "INSERT BILL FACE UP", a large glossy red dome button labelled "SPIN", small yellow/orange/blue buttons, a CREDITS red LED display at the top right, a red stool cushion and patterned carpet blurred in the lower left
[POSE / EMOTION / STATE] empty
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, high angle, dutch tilt about -30°, shallow depth of field
[LIGHTING] warm red, green self-glow from the slot
[BACKGROUND] full scene
[AVOID] hands, people, money, captions, watermark
```

### bg_machine_dutch_cu
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_machine_dutch_cu_f00440.jpg
[SUBJECT] close-up of the face of a red "LUCKY 7s" slot machine: big gold-outlined "LUCKY 7s" topper with marquee bulbs, WIN LED "0", "PLAY 3 CREDITS ★ 1 LINE · $1 GAME ★", reel window showing 7, 7 and a 7 just above the red payline with a cherry on it, CASH OUT (blue), BET ONE (yellow), MAX BET (orange) buttons, red SPIN button, top of a red ribbed stool cushion at the bottom
[POSE / EMOTION / STATE] empty, right third left clear for a character head
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, slightly low angle, dutch tilt +10°
[LIGHTING] warm orange, red glow, bloom on bulbs
[BACKGROUND] full scene
[AVOID] people, captions, watermark
```

### bg_machine_interior
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_machine_interior_f00550.jpg
[SUBJECT] inside of an opened slot machine cabinet: warm amber plywood box with rivets and dark ink outlines, a light strip along the top, a reel unit with three cream reel drums (7, BAR, cherry symbols) above a label plate "LUCKY 7s REEL UNIT", below it a green circuit board with a black chip labelled "RNG", orange wires, a black stepper motor box, yellow warning stickers, a blue ribbon cable, floating dust motes
[POSE / EMOTION / STATE] empty
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, eye level, reel unit in the upper-middle third
[LIGHTING] warm amber top light, soft glow
[BACKGROUND] full scene
[AVOID] people, paper strip, captions, watermark
```

### bg_xray_machine
```
[REFERENCE] attach: library/backgrounds/05_the_science_behind_slot_machines/bg_xray_machine_f00840.jpg
[SUBJECT] a red LUCKY 7s slot machine in a casino row where the upper part (reel window, buttons) is rendered normally but the lower cabinet is shown as an X-ray: dark see-through interior outlined by a glowing cyan (#3fd8e8) wireframe grid box, an empty round wheel mount inside; neighbouring red machines and patterned carpet rendered normally
[POSE / EMOTION / STATE] empty
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536, eye level, machine centred and filling the frame height
[LIGHTING] warm casino + cool cyan emissive lines
[BACKGROUND] full scene
[AVOID] people, captions, watermark
```
