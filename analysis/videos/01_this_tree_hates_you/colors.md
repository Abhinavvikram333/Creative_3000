# Colours — 01 "This Tree Hates You"

Sources: `metrics/palettes.json` (whole-video k-means) and `tools/palette.py` runs on representative frames and on
tight crops (character, UI). The share is the fraction of pixels.

## 1. Global palette (whole video, palettes.json)
`#182e5e` 15.8 % (night navy) · `#44495e` 13.8 % (storm/smoke grey-blue) · `#131d28` 12.6 % (near-black UI/night) ·
`#737689` 8.1 % · `#e4c094` 7.9 % (sand) · `#a29d7f` 7.9 % (shaded sand) · `#30599a` 7.3 % (night blue) · `#8fbbe4`
6.9 % (day sky) · `#dae3e1` 6.4 % (clouds / Kai head) · `#4d7f3b` 5.9 % (foliage) · `#a65250` 4.1 % (sunset / red
accents) · `#38add7` 3.3 % (turquoise sea).

**Reading:** roughly half the runtime is night/dark (navy #182e5e / #131d28 / #30599a); the rest is a bright tropical
triad: sand #e4c094, sky #8fbbe4 and foliage #4d7f3b, with turquoise sea #38add7 as the accent.

## 2. Palette per background / mood (palette.py k=6 on frames)
| Mood / plate | Frame | Dominant hexes (share order) |
|---|---|---|
| Day tree beach (bg01) | f00030 | `#e3cb96` sand · `#25532f` deep leaf · `#c6af7e` · `#66814f` leaf · `#d2eaf7` sky haze · `#8dcfec` sea |
| Day tree beach MLS (bg01) | f00400 | `#c2af8c` · `#244d2a` · `#457940` · `#868b5d` · `#d4eaf6` · `#8ac9e8` |
| Aerial island (bg02) | f00160 | `#0454a3` deep sea · `#c7e6f8` · `#7bc4ed` · `#2a8bca` · `#ead89d` sand · `#8fa644` scrub |
| Poster insert | f00205 | `#e1d8c2` paper · `#d0bfa2` · `#af977c` · `#2e1e24` ink · `#80715d` · `#79bbe4` |
| Radar UI | f00470 | `#021867` · `#08183a` · `#2d4773` · `#a59fc0` clouds · `#717991` · `#d1c9e8` |
| Storm night tree (bg03) | f00540 | `#25335c` · `#031c22` · `#112a33` · `#2c4287` · `#7d8ad3` (Kai lit) · `#f5f7f8` rain |
| Leaf macro night | f00650 / f00690 | `#12337a` · `#071f63` · `#021a42` · `#1d432b` leaf · `#a4c3f1` glow / `#17442c` · `#39724c` |
| Night bokeh CU | f00740 | `#1c448f` · `#2d54a1` · `#91a1ed` (Kai head, blue-graded) · `#0e2d76` · `#0c0b32` |
| Skin insert | f00790 | `#f0959e` pink skin · `#4d6fa6` · `#e6bb7c` fat · `#f6d7d9` · `#331e2b` outline · `#c36257` |
| Storm open beach (bg05) | f00840 | `#2e3b65` · `#142460` · `#2e428a` · `#8b96e2` · `#0f0d2e` · `#63433a` |
| Roadside car (bg06) | f00880 | `#4f4d5a` asphalt · `#2d562a` · `#6f9c4e` · `#d5e5e9` · `#60c0e2` · `#b4211e` car red |
| Sunset beach (bg07) | f00930 | `#e9cc9a` · `#db9492` pink sky · `#87639b` lilac · `#fdeecd` · `#8d9e50` · `#50682b` |
| God-ray day (bg08) | f01090 | `#dbc592` · `#cddfee` · `#7dc8fc` · `#3898ed` sky · `#3d3b4f` · `#af7b4b` |
| X-ray UI | f01250 | `#032842` · `#021529` · `#dcf2f7` bone glow · `#296078` · `#5e8aa0` · `#a2bfd0` |
| Bush day (bg09) | f01310 | `#d5c48e` · `#58863a` · `#2a5824` · `#89ab59` · `#d7eaf2` · `#8ed2ea` |
| Shallow lagoon (bg10) | f01490 | `#23bfdc` turquoise · `#d3ebf3` · `#7bd4f5` · `#336031` · `#839b51` · `#ddd3a9` |
| Log pile dusk (bg11) | f01532 | `#ad6060` salmon · `#2d2f1a` · `#504927` · `#74613f` · `#c58aa5` · `#444588` |
| Log pile night (bg11) | f01600 | `#29395c` · `#172e41` · `#384b69` · `#2643a0` · `#687cd2` · `#f4f6f7` |
| Firelit + smoke (bg11) | f01740 | `#554b5c` · `#313b47` · `#886974` · `#ba6135` fire glow · `#4650a7` · `#cca49c` |
| Dark void CU (bg12) | f01810 | `#01081c` · `#271317` · `#d1a79b` (head, warm) · `#a08584` · `#d55915` shirt · `#532e20` |
| POV fire (bg13) | f01840 | `#49323b` · `#9c7571` · `#605173` · `#a65933` · `#efa440` flame · `#decbb4` |
| Thermal UI | f01900 | `#130f2f` · `#4d2931` · `#b9bdec` head · `#faca44` hot lungs · `#978ec3` · `#c8246d` magenta |
| Final open beach (bg14) | f02020 | `#f1dba7` sand · `#8acdfb` · `#d3eafa` · `#3e9eee` sky · `#ccb582` · `#797743` |

**Mood rules:**
- **Day:** warm sand (#e3cb96–#f1dba7) + sky blue (#3e9eee–#8acdfb) + leaf greens (#25532f / #457940 / #66814f) +
  turquoise (#23bfdc–#38add7).
- **Night:** everything is pushed to navy/indigo (#142460–#2e428a) with lifted blue-violet highlights (#7d8ad3–#91a1ed).
  Kai's head becomes periwinkle (#8b96e2 / #91a1ed).
- **Sunset:** pink #db9492 + lilac #87639b + cream #fdeecd.
- **Fire:** orange glow #ba6135 / #efa440 over grey-violet smoke #554b5c / #886974.
- **UI screens:** near-black navy #040816–#07001c with one hero accent each: radar white + red pill, X-ray cyan
  #96d9e2 / #dcf2f7, thermal yellow #faca44 + magenta #c8246d.

## 3. Character colours (Kai)
| Part | Hex (neutral day) | Notes |
|---|---|---|
| Head fill | `#dce0e9` | shade `#babfcf`; MS average `#b1b4ce`. Night `#8b96e2`, sunset cream `#fef9ed` (shade `#fbeac3`), firelit `#d1a79b` |
| Outline | `#2f3d43` (day) / `#140916` (dark) | ~5–6 px MS, ~10 px CU. Warm brown `#8b6849` at sunset |
| Eyes / brows / mouth | `#1e0912` | |
| Shirt | `#e05f13`, shade `#b94a0f` | Night/blue grade turns it brick `#835d64` |
| Shirt flowers | `#f3e6d3` (warm-lit `#e69f63`) | centres `#ba190f` |
| Shirt leaf print | `#1a6747` / `#55693e` | |
| Shorts | `#3b3f6a` / `#445181` | |
| Limbs | pale tan fill with a dark outline | |
| Sandal soles | `#e0c050` | |
| Blush | `#f0a0a8` | E16 |
| Red lid patches | `#d86a6a` | E22–E24 |
| Red-hot head | `#da767a` | E18 |
| Sick tint | `#9fbf9a` | E03 |
| Sweat drop | `#6488aa` fill, dark outline, white highlight | |
| Tears | `#829aad` – `#9cc8ec` | |
| Blisters | `#e8a0b0` with a dark outline | |

## 4. Caption colours
- Fill `#FFFFFF`, stroke `#000000` (~3–4 px at 720 w), faint dark shadow. They read on every plate because they are
  always placed over a mid-tone area at y ≈ 900.

## 5. Accent colours
| Accent | Hex | Where |
|---|---|---|
| Warning red X (trunk paint) | `#e22924` / `#c83428` | trunk X (S04, S12, S15, S17), dripping edges |
| Red X marks on logs | `#cf2627` | S17, S19 |
| Severe-storm pill | `#e01436` + white text | S05 |
| Manchineel apple | `#f4f16c` (lit) / `#c4d14c` | everywhere apples appear |
| Red car | `#b4211e` | S11 |
| Anger vein | `#e03a2a` | S12 |
| Fire core / flame | `#ffe680` → `#efa440` → `#d5401a` | S17, S19 |
| Thermal hot | `#faca44` → `#c8246d` → purple `#4d2931` | S20 |
| X-ray glow | `#96d9e2` / `#dcf2f7` | S14 |
| Scent wisp | `#d8f5b0` glow | S12 |
