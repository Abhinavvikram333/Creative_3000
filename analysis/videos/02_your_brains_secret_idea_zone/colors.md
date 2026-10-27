# Colour system — 02 "Your Brain's Secret Idea Zone"

Sources: `metrics/palettes.json` (video and per-shot), `tools/palette.py` on frames 45, 160, 300, 400, 590, 660, 746, 790, 830, 900, 930, 960, 1000, 1065 and 1141, plus pixel samples on character parts.

## 1. Global palette (metrics/palettes.json, video level)
`#473025` 18 % · `#120c0f` 17 % · `#2c1c17` 17 % · `#6d4634` 11 % · `#966647` 9 % · `#405272` 6 % · `#45799b` 5 % · `#2e3049` 5 % · `#b79376` 4 % · `#dec1a5` 3 % · `#6da7cf` 3 % · `#caeff3` 1 %

The video is a dark warm-brown base (more than 60 % of pixels are under 30 % brightness). The cream head and the navy body are the brightest recurring accents. Cool blues/teals take over in the "sleep" sections.

## 2. Per background / mood

| Background | Frame | Dominant (palette.py, k=6) | Notes |
|---|---|---|---|
| Stage (warm spotlight) | 45 / 160 | `#34241b` `#120f0e` `#674e3a` `#b1835c` `#e3cfc2` `#40547d` | wall green-black `#252720`; rug light `#d3b28b`, rug dark `#2d1811`; bulb `#f4f1de` |
| Stage close (MS) | 300 / 590 | `#261f19` `#49382b` `#e6cab8` `#855f44` `#3c5077` `#b58b66` | head and body dominate |
| X-ray stage | 400 | `#0c080a` `#331e16` `#8b674b` `#6faac8` `#d8c7be` `#306986` | X-ray blue `#6faac8` / `#306986` |
| Menlo Park lab | 660 | `#190904` `#31170b` `#4e2713` `#6b3d1f` `#efc797` `#a87b56` | amber monochrome; highest saturation |
| Depth chart | 746 | `#100f18` `#2d6c7a` `#2e3f63` `#131f3d` `#568b90` `#c9cfda` | water `#397e88`, violet band `#362e67`, deep `#040b1e`, air `#211718` |
| Underwater CU | 790 / 830 | `#0d1731` `#4d808b` `#2e6477` `#2f3663` · `#a1b5c8` `#232d49` `#467384` `#8292aa` `#dfe9f7` | the face turns `#9eb4cb` under the water grade |
| Corkboard | 900 / 930 | `#985b30` `#a96e42` `#7b4525` `#e8c69d` `#cb9b74` `#4b2513` | cork `#ab6d3f`; card `#e5c093` / `#f3dcb2` |
| Elevator (warm) | 960 / 1065 | `#3e2720` `#30150d` `#7c2a24` `#55437a` `#9d7659` `#ebe5e4` | carpet `#842425`, wood `#4a2816`, purple floor `#472e65`, brass `#714f2e` |
| Elevator (DEEP SLEEP grade) | 1000 | `#1f171a` `#0f090a` `#431a21` `#434255` `#8690c6` `#f7f6f7` | lavender cast `#8690c6` |
| Stage ending | 1141 | `#171110` `#322a22` `#634836` `#e0c6b5` `#947560` `#3d4f77` | same as the opening (bookend) |

## 3. Characters

| Part | Theo | Edison |
|---|---|---|
| Head / skin (lit) | `#f6e1c7` (palette `#f0d3bc`) | `#efc797` (golden-lit; true base about `#f2d6b0`) |
| Skin shade | `#e2c2ab` / `#d9b8a7` | `#be8e67` |
| Outline | dark brown `#2e1d17` (samples `#322a24` – `#372d26`) | `#381b0f` |
| Hair | `#694532` base, `#8a6a56` highlight | pale grey-beige `#c49779` under warm light (neutral: `#c9bba8`), strand lines `#8d6042` |
| Torso | navy-blue `#3a5080`, shade `#2d3d5f`, sheen `#5a6fa0` | black suit `#1e0c05`, white shirt V `#fcd496` (lit), bow tie `#1a0c06` |
| Limbs / hands | `#1f1917` | `#1f1917` |
| Face lines (eyes/brows/mouth) | `#3b2418` | `#4b2a17` |
| X-ray variant | body `#6faac8`, inner `#306a87`, outline `#a8d8ef`, brain `#e493a9`, wire glow about `#f2e8b0`, dead wire `#807d93`, plug tag `#f4f1ea` | — |
| Hypnagogic eyes | iris `#2e85cb` / `#3390db`, catchlight white, lids `#1b1d2a` | — |

## 4. Caption colours
- Fill `#f9fafa` (white), outline/shadow `#04050c` (black).
- On-screen labels: white `#ffffff`; DEEP SLEEP lavender `#aeb7d9`; HYPNAGOGIA title fill `#dddaf3` with outline `#212b4b` / `#304675`.

## 5. Accents
- Steel ball chrome: `#e8e8ea` highlights, `#2a2524` dark reflections.
- Glint and impact arcs: `#fffaf0` / `#f6eceb`.
- EEG trace: mint `#a2e7df`.
- Sweat drop: `#a7cdd7`.
- Corkboard: red string/pins `#a8452d`; truck green `#5c9272`; magnet red `#b43f2b`; "!!" red `#d23a2a`; yellow pin `#e0b33a`.
- Notepad handwriting: red `#c0392b` (approx.).
- Elevator: purple hypnagogia light `#5f457d`; DEEP SLEEP fascia brick `#5a2a22` with white caps.
