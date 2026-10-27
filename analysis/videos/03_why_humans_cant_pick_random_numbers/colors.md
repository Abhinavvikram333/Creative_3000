# 03 — Colour system

Sources: `metrics/palettes.json` (video-wide k-means) + `tools/palette.py` (k=6) on representative frames + 5×5 median pixel
samples on characters. Shares in brackets.

## 1. Global palette (whole video, from palettes.json)
`#d1c9b7` (11 %) · `#cf9362` (11 %) · `#c4a593` (10 %) · `#5e6356` (10 %) · `#764c31` (10 %) · `#e8e5d7` (10 %) ·
`#eebc90` (9 %) · `#948483` (8 %) · `#a16a4c` (8 %) · `#84afb3` (6 %) · `#3d2c2b` (5 %) · `#517c9d` (4 %)

Read: a **warm sand/terracotta/cream base** (desert modernism) with **teal/turquoise** as the cool counter-colour and
**dark chocolate-brown** for outlines, hair and wood. Saturation is moderate (mean 0.28); highlights are cream, never pure white
(except caption fill and sweat-drop highlights).

## 2. Palette per background / mood
| background (shots) | frame | palette (k=6, share order) | mood |
|---|---|---|---|
| AP office (S1) | #50 | `#73432d` `#e7e4e1` `#392422` `#beb2a8` `#528385` `#a67c54` | warm wood + teal wall, daylight |
| Bank drive-through (S2a) | #150 | `#cea28c` `#a9d3e2` `#e9e4d7` `#7cb0c8` `#7d6e62` `#4c3730` | noon: sky blue + coral car + cream stucco |
| Car window (S2b) | #230 | `#d98d6c` `#d8c3a8` `#d2e3e2` `#9a9a99` `#7d6350` `#412a26` | coral-orange car body dominates |
| Police backseat (S3) | #320 | `#686168` `#f3e6d4` `#ccbea9` `#96939a` `#302d36` `#d9a167` | cool greys + mustard |
| Tower exterior (S4) | #380 | `#dcd2bd` `#c8a284` `#8a7b72` `#83a9b9` `#477bbb` `#56504a` | midday blue `#477bbb` sky |
| Elevator interior (S5) | #600 | `#d9bf9a` `#c79e71` `#ded9cc` `#6eb4ac` `#a36b41` `#472c22` | brass + teal glass |
| Elevator gold bloom (S5 end) | #720 | `#d4b98f` `#eedeb1` `#9bc3bb` `#a57340` `#eba851` `#512d14` | warmed, glowing |
| Facade / number city sunset (S6) | #790 / #850 | `#f4cb98` `#db9d84` `#b0775f` `#705250` / `#e4b38e` `#fad693` `#ce997b` `#7e5c5b` | peach-gold haze |
| Audit office (S7) | #920 | `#eeb894` `#8b584e` `#c5875f` `#f6e3ce` `#583226` `#708bac` | sunset interior, god-rays |
| Coin board top-down (S8) | #1000 | `#5e6c4f` `#80512f` `#dca354` `#51442a` `#a5723f` `#f1cd80` | olive felt + gold/copper coins |
| Window ledge (S9/S11) | #1090 / #1240 | `#f1be96` `#b46853` `#f5edce` `#c87ca3` `#d2966d` `#663b47` / `#f4c294` `#bb755a` `#e39697` `#eee7d1` `#9a769a` `#8a4438` | pink-magenta sunset |
| Audit desk high-angle (S10) | #1180 | `#eeba8b` `#c48e66` `#804f41` `#583024` `#f9edca` `#3ab3a9` | warm + teal chair accent |
| Jail cell (S12) | #1320 | `#9f7050` `#554b52` `#3c2a2b` `#d3a37a` `#f7ddbe` `#867489` | amber wall + steel grey bars |

Key sky gradients: noon `#87b8d6` (top) → `#a9d3e2`; sunset `#b07996` (violet top) → `#f9a4a7` (pink) → `#fddea9` (yellow
horizon); number city `#db8e84` → `#ffd080`.

## 3. Character colours
| character | head | outline | hair | clothes | accents |
|---|---|---|---|---|---|
| **Rico** | `#f8efe6` (lit) / `#e9dbd9` (shade) | `#2a1c1a`–`#333233` | dark brown `#3b2820`–`#412b20`, highlight band `#8a6a56` | mustard jacket `#d9a23f` (shade `#bf7f27`, lit `#e3c99e`), red-brown tie `#88422e` with cream stripes; jail: orange jumpsuit `#e0631f` (lit) | blue lanyard clip `#4a6fb3`; limbs/hands `#1e1616` |
| **Marge** | `#f7e7df` | same | auburn `#a2513b` (shade `#8f462c`, hi `#c06a48`), bun with red pencil `#c8463a` | purple suit `#814eab`–`#8353c9`, white/lilac blouse `#f6d5d0` | round black glasses `#2a1c1a`; gold magnifier rim `#caa16f` |
| **Officer Dale** | `#f9efe6` | same | dark brown `#32201e` | navy cap + uniform `#36517e` / `#314579` | gold star & badge `#ebca60` / `#c2922b` |
| **Nina** (teller) | `#f8efe6` | same | brown bun `#6b4630` | teal uniform `#67b7ac` | — |

Universal: character outline is near-black dark brown; heads are warm off-white, never pure white; sweat drop `#8cb9db` with
white highlight.

## 4. Caption colours
Fill `#ffffff`, outline `#0f0505` (≈ 4 px), drop-shadow black 50 %.

## 5. Accent / signal colours
| use | hex |
|---|---|
| LED counter numerals (warm orange dot-matrix) | `#f2a33a` on `#2a1f1c` |
| Rainbow buttons 2–9 (leading digits that "differ") | red `#e25b5b`, orange `#f08a3c`, yellow-green `#b9c64a`, teal `#5cc2b0`, blue `#7da8ee`, violet `#9a7ae0`, magenta `#d385c3`, pink `#e48fb5` |
| Gold "starts with 1" buttons / bloom | `#f6c75a` → glow `#ffe9a8` |
| 6-heads-in-a-row glow / red ellipse | glow `#fff79e`, ellipse stroke `#d2412b` |
| Police wash | red tint `#ca6d68`, blue tint `#7f8fd0` (blend) |
| Heads coin / tails coin | gold `#e8bf67` / copper `#895a32` |
| Cash green | `#8fcf8a` |
| Teal accent (chairs, posts, kiosk) | `#3ab3a9` / `#41918b` |
