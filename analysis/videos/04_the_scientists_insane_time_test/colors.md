# Colour system: 04 "The Scientist's Insane Time Test"

Sources: `metrics/palettes.json` (video-wide and per auto-shot k-means), plus my own `tools/palette.py` runs on representative frames and on the verified library crops. Hex values are k-means centroids, so they are slightly desaturated averages. Treat them as targets and keep pure fills a little cleaner.

## 1. Global palette (whole video, `palettes.json` → video)

| Hex | Share | Role |
|---|---|---|
| #f1e6db | 15.2 % | warm off-white: heads, paper, cream walls |
| #c1c3bc | 13.3 % | light warm grey: plaza, haze, paper shadow |
| #5a3830 | 9.1 % | dark warm brown: wood, lineup room, outlines |
| #57606b | 8.8 % | slate grey: steel grating deck |
| #8d5548 | 8.6 % | brick/red-brown: landing net, desk, deck |
| #9e9276 | 7.4 % | khaki: grass, paper texture |
| #e58f66 | 7.4 % | warm orange-peach: tower, harness, sunset |
| #3874c8 | 6.8 % | sky blue |
| #d05534 | 6.7 % | red-orange: cap, alarm, LED |
| #1d3f70 | 6.3 % | navy: banners, blueprint |
| #7196c4 | 5.8 % | light blue: sky/haze |
| #281a19 | 4.7 % | near-black brown: outlines, dark room |

Read: the video is a **warm-cream + sky-blue + safety-orange** scheme. Navy is the "brand" colour of the ride, and red is the accent for danger (the cap, LEDs, PANIC, alarm).

## 2. Palette per background / mood (palette.py k=6 on the frame)

| Background (frame) | Hex (largest first) | Mood |
|---|---|---|
| Tower top, high angle (f1) | #332831 #ea872a #e5e1da #665247 #9ca655 #4b9bd4 | day exterior, safety orange + grass + sky |
| Tower side fall (f125) | #ede2d9 #9cb4ca #8c946b #4b4e3d #e47d3d #203278 | pale plaza far below, navy banner |
| Brain room (f262) | #f8efdd #dfc8b8 #d5914d #a7523a #5c84b0 #51362c | warm cream + wood + porthole blue |
| Support group, bird's-eye (f340) | #dad3ae #9fc1a5 #ae8b66 #e4e6db #5c422c #576480 | mint wall, beige floor, fluorescent |
| Tower platform 2-shot (f451) | #378fd5 #2a2d38 #54575c #dbe7ec #a4ad86 #e7722b | blue sky, dark steel grating |
| CHRONO-2 ECU (f600) | #614757 #4489d2 #632327 #ec5044 #c59276 #f0d8ca | maroon housing, LED red, blurred blue |
| Blueprint (f625) | #304474 #4b5f8c #a09da5 #8d5f3d #1d294e #bcc9e3 | cyan-navy paper, chalk white lines |
| Landing net (f715) | #814931 #39292e #388ad3 #e49227 #8fb2c6 #e9ebe1 | red-brown net, orange steel, sky |
| Plaza, tower base (f800) | #2f78ce #eeddc7 #7c543a #e9922b #373138 #8b95aa | sky + bright paving + orange |
| Lineup room (f870) | #27140d #583323 #695953 #e0e3e1 #91979f #c98658 | dark warm brown + cold white window |
| Brain room, high (f975) | #f2e8da #b7714e #e2ad75 #5e3f2d #90bbe1 #728d81 | cream + wood desk |
| **Brain room red alarm (f1000)** | #f3ba9f #d3361f #e66b50 #762b20 #f3e9f1 #958cdb | red overlay, porthole turns lilac |
| BBQ deck sunset (f1104) | #985d58 #be935d #654236 #e7b084 #e77372 #f3e7d3 | dusty rose, honey wood, peach light |
| Flipbook page (f1190) | #c7c59e #e3d8c1 #555355 #858372 #e28937 #422a1a | cream paper, grey ink, orange tower |

Specific sampled surfaces: sky #348cd6–#3a98df. Tower orange #ea872a / #e7722b. Ride banner navy #203278–#243064. Steel grating #2a2d38 / #54575c. Grass #9ca655. Support-room mint wall #93c5a7–#9fc1a5 and floor #dad3ae. Lineup window #e0e3e1 and wall #583323. Sunset sky #c05b82 / #e77372.

## 3. Character colours

| Character | Element | Hex |
|---|---|---|
| **All humans** | Head/skin fill (warm off-white) | **#f3eeed** (range #f1ebec–#fffcf9) |
| | Outline (dark warm brown-black) | **#2a2024** (range #33242f–#352424) |
| | Limbs / ball hands | #2a2024 |
| **Dex** | Cap red / cap shade | **#d64444** / #c6443c (button on top darker #8a2a2a) |
| | Harness orange / harness yellow lining | **#dd7c21** (#e6843d) / **#f4c33a** |
| | T-shirt yellow (final scene) | #e8ae2d |
| | Hair (brown, seen when the cap is off) | #6c4d3e |
| | Wrist device housing / LED | #3a1b1f / #e94d42 |
| **Dr. Klaus** | Hair (black bowl cut) / moustache | #2a2024 / #2a2024 |
| | Glasses rims | #2a2024 (lenses tinted pale grey-blue #9abccc when catching sky) |
| | Lab coat white / coat shade | #e6eaee / #c9ced6 |
| | Pocket pens | red #d04a3e, blue #3b6fd0 |
| **Noggin** | Brain pink / gyri lines | **#f2c0c6** / #d2979e |
| | Visor band green | **#8bd391** (darker edge #4f9a63) |
| | Pencil | yellow #f2c94c, pink eraser |
| **Amy** | Almond body / wood-grain lines | **#be8661** (light side #e3b17b) / #654d39 |
| **Elmer** | Harness green + orange straps | ≈#4e9c5a / #ec9928 |
| | White side tufts | #f4f1ee |
| **Gil** | Shirt purple / harness orange | ≈#7a58a8 / #dc7745 |
| | Queasy face tint (541–600) | **#9c9cbb** |
| **Tad** | Harness teal + orange straps | ≈#3e9a8c / #ed9223 |
| | Hair | #2a2024 |
| **Gus / Carl / Deb / Ray / Mo** | Shirts red / blue / pink / red / purple | ≈#d0483d / #3b5fc4 / #e46aa4 / #d0483d / #6e4fb0 |
| | Carl's bandage, Gus's neck brace | white #f1f1f1 with red dot #d0483d |
| **Cooper** | Salmon shirt / hair | #d49a72–#c65c3f / #c0703f |
| **Hank** | Straw hat / plaid shirt | #f6d488 / #81809b |
| **Biscuit** | Fur / outline | #af7a53 / #4f2928 |
| **Digit Gang** | LED body / dot highlights | #4b1e20 / #c4313a, bright dots #f15f4f |
| **Pigeon** | Body grey / head purple / eye | #9b9db3 / #7a6aa8 / #dd894f |

## 4. Caption colours
- Fill **#f1ebe6** (rendered white). Outline/shadow **#0f0909**. No colour highlight words.

## 5. Accent colours (meaning)

| Accent | Hex | Used for |
|---|---|---|
| Danger red | #d64444 / #e94d42 / #d3361f | Dex's cap, CHRONO-2 LEDs, PANIC button, alarm tint, "0/4" scrawl, rubber band |
| Safety orange | #ea872a | The tower and harnesses (the "ride" world) |
| Hazard yellow/black | #f4c33a / #2a2024 | Deck edge stripes, PANIC box |
| Navy | #203278 | Ride branding (LONE STAR THRILLS, FREEFALL), blueprint paper |
| Sky blue | #348cd6 | Daylight / normal time |
| Lilac/purple | #958cdb / #7a58a8 | Alarm-shifted sky, Gil, pigeon head |
| Mint | #9fc1a5 | Support-group room |
| Sunset rose | #e77372 / #c05b82 | Final "story time" warmth |

## 6. Rules to reuse
- Characters never use pure white or pure black: heads are warm off-white (#f3eeed) and outlines are warm near-black (#2a2024).
- Each scene keeps one dominant hue family and one red accent.
- The emotional state change is shown with a **full-frame colour shift** (red alarm), not by recolouring characters. The exception is Gil's queasy face tint.
