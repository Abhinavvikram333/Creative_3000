# 3D-looking assets / props — video 03

| id | file | description | frames | looks like | build suggestion |
|---|---|---|---|---|---|
| `fountain_pen` | `fountain_pen_f00003.jpg` | black lacquer fountain pen with gold nib and gold trim | #1–30 | 3D render look (specular highlights) | generate as image (transparent) or simple Blender model |
| `magnifier_eyed_digits` | `magnifier_eyed_digits_f00080.jpg` | gold-rimmed magnifying glass over the cheque; digits "87,43" magnified with googly eyes on 8 and 7 | #34–105 | 2D/3D hybrid: lens content is a scaled copy of the cheque layer | AE: circle mask + scaled duplicate; rim as image |
| `magnifier_gold` | `magnifier_gold_f01300.jpg` | Marge's large magnifying glass: thick gold rim, brown wooden handle, glint | #34–105, #1291–1413 | illustration with 3D-ish shading | generate as image (transparent); lens content done in comp |
| `bank_sign_led` | `bank_sign_led_f00140.jpg` | roadside sign: cream/terracotta "Desert State BANK" with sunset logo, "EST. 1961", "YOUR TOTAL", "DRIVE-UP BANKING", black LED panel showing "$2,000,000" | #107–200 | 3D render look | generate sign with blank LED panel; numbers as AE overlay |
| `orange_sedan` | `orange_sedan_f00140.jpg` | boxy coral-orange 1960s sedan with chrome hubcaps, window down | #109–300 | 3D render with toon outline | Blender low-poly model or image |
| `video_teller_kiosk` | `video_teller_kiosk_f00278.jpg` | beige VIDEO TELLER kiosk with screen ("TELLER 3"), teal base, yellow "SMILE!" sticker, clear pneumatic tube with orange capsule cup | #249–300 | 3D render | image; screen content composited |
| `handcuffs_spring` | `handcuffs_spring_f00278.jpg` | silver handcuffs on a coiled spring popping out of the tube cup | #273–300 | illustration | 2D sprite, spring stretched in AE |
| `police_car` | `police_car_f00355.jpg` | black-and-white police car with "POLICE" and star | #346–405 | 3D render | image or Blender |
| `tower_the_one` | `tower_the_one_f00355.jpg` | "THE ONE" tower with floor numbers 1–19; silhouette is a digit 1 | #342–872 | 3D render | Blender model (needed for S4/S6 moves) |
| `elevator_panel` | `elevator_panel_f00640.jpg` | art-deco wooden button panel "THE ONE", sunburst fan, left column bell/9…1, right column 19…10, round white enamel buttons | #430–739 | 3D/illustration | image plate; per-button glow layers in AE |
| `glass_elevator_cab` | `glass_elevator_cab_f00745.jpg` | round glass elevator cab with orange/brass ring top and base | #403–429, #737–800, #873–954 | 3D render | Blender (transparent glass cylinder) |
| `number_buildings_skyline` | `number_buildings_skyline_f00850.jpg` | row of giant digit buildings 1–9, decreasing height, pastel striped windows (Benford chart as a city) | #775–872, ghost #1253–1290 | 3D render | Blender: extrude digits 1–9 with window texture, heights ∝ Benford (30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6 %) |
| `audit_desk` | `audit_desk_f00882.jpg` | wooden desk with brass "AUDIT" plaque | #873–1220 | 3D render | image |
| `coin_board_10x10` | `coin_board_10x10_f00985.jpg` | wooden-framed green 10×10 board with round slots filled with gold heads / copper tails coins; "10 × 10" label | #955–1063 | 3D render | Blender (instanced coins) — fill animation |
| `money_sack` | `money_sack_f00966.jpg` | canvas money sack "DESERT STATE BANK $" in green print | #955–990 | illustration/3D | image |
| `gold_coin` | `gold_coin_f00900.jpg` | shiny gold coin flipped by Marge | #877–933 | illustration with glow | 2D sprite + glow |
| `accounts_payable_nameplate` | `accounts_payable_nameplate_f00045.jpg` | brass desk nameplate "ACCOUNTS PAYABLE" | #22–108 | 3D render | image (exact text) |
| `notepad_8746` | `notepad_8746_f01199.jpg` | small lined notepad with hand-written "8746" in blue ink | #1165–1220 | illustration | blank pad image + handwriting overlay animated |

## fountain_pen

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/fountain_pen_f00003.jpg
[SUBJECT] a black lacquered fountain pen with a gold nib and gold band, writing angle
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## magnifier_eyed_digits

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/magnifier_eyed_digits_f00080.jpg
[SUBJECT] a gold-rimmed magnifying glass with a wooden handle, empty clear lens
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## magnifier_gold

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/magnifier_gold_f01300.jpg
[SUBJECT] a large magnifying glass with a thick polished gold rim and a brown wooden handle, clear lens
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## bank_sign_led

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/bank_sign_led_f00140.jpg
[SUBJECT] a retro 1960s roadside bank sign: cream panel with a sunset-over-mesa logo and the words "Desert State" in red script and "BANK" below, a small red tab "EST. 1961", a black LED panel below (blank), on teal posts
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## orange_sedan

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/orange_sedan_f00140.jpg
[SUBJECT] a boxy coral-orange 1960s American sedan, side view, driver window down, white-wall tyres
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## video_teller_kiosk

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/video_teller_kiosk_f00278.jpg
[SUBJECT] a retro drive-up bank kiosk: beige box with a small video screen, teal base with the words "VIDEO TELLER", a small yellow "SMILE!" sticker, a clear pneumatic tube rising from the top with an orange capsule holder
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## handcuffs_spring

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/handcuffs_spring_f00278.jpg
[SUBJECT] a pair of silver handcuffs attached to a stretchy metal coil spring
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## police_car

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/police_car_f00355.jpg
[SUBJECT] a black-and-white 1960s police car with "POLICE" lettering and a gold star on the door, light bar on the roof
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## tower_the_one

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/tower_the_one_f00355.jpg
[SUBJECT] a retro 19-storey tower shaped like the digit 1 (cantilevered top-left wing as the flag), teal glass, terracotta frame, gold vertical band with serif floor numbers 1-19, red rooftop sign "THE ONE"
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## elevator_panel

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/elevator_panel_f00640.jpg
[SUBJECT] an art-deco wooden elevator button panel with a sunburst fan top, a brass "THE ONE" plate, two columns of round white enamel buttons: left column bell, 9, 8, 7, 6, 5, 4, 3, 2, 1 and right column 19 to 10
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## glass_elevator_cab

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/glass_elevator_cab_f00745.jpg
[SUBJECT] a round glass elevator cab with a brass-orange ring roof and floor, vertical brass ribs
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## number_buildings_skyline

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/number_buildings_skyline_f00850.jpg
[SUBJECT] a row of building-sized digits 1 2 3 4 5 6 7 8 9 standing in a desert town, each digit shorter than the previous, pastel striped facades with windows
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## audit_desk

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/audit_desk_f00882.jpg
[SUBJECT] a wooden office desk front with a brass plaque engraved "AUDIT"
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## coin_board_10x10

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/coin_board_10x10_f00985.jpg
[SUBJECT] a wooden-framed green felt board with a 10 by 10 grid of round slots, filled with a random mix of gold heads coins and copper tails coins
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## money_sack

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/money_sack_f00966.jpg
[SUBJECT] a cream canvas money sack printed "DESERT STATE BANK" and a dollar sign in green, open top
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## gold_coin

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/gold_coin_f00900.jpg
[SUBJECT] a shiny gold coin edge-on with a bright glint
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## accounts_payable_nameplate

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/accounts_payable_nameplate_f00045.jpg
[SUBJECT] a brass desk nameplate on a dark wood block engraved "ACCOUNTS PAYABLE"
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```

## notepad_8746

```
[REFERENCE] attach: library/assets_3d/03_why_humans_cant_pick_random_numbers/notepad_8746_f01199.jpg
[SUBJECT] a small white lined notepad sheet with "8746" handwritten in blue ballpoint
[POSE / EMOTION / STATE] isolated prop, clean
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom, subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
[COMPOSITION] centred, square 1024x1024 sprite, 3/4 view as in reference
[LIGHTING] soft studio light matching warm desert daylight
[BACKGROUND] transparent
[AVOID] captions, watermark, hands, characters, extra props
```
