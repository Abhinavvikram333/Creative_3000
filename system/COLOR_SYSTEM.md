# Series colour system (pilot 01–05)

Machine-readable twin: [`color_system.json`](color_system.json). Swatch board: [`palette_swatches.png`](palette_swatches.png)
(re-render with `python3 tools/render_swatches.py` after editing the JSON).

**Sources.** All five pilot videos were decoded at 30 fps. The numbers come from:
- per-frame `brightness` (mean HSV V, 0–1) and `saturation` (mean HSV S, 0–1) in `analysis/videos/*/metrics/frame_metrics.csv`, aggregated over every frame of each grade's shot ranges;
- the k-means palettes in `palettes.json`;
- the per-video `colors.md` and `library/characters/*/character.md`;
- new checks for this document: `tools/palette.py` (k=8) on 28 representative full-res frames, pixel medians on characters (support group f00380, BBQ f01125, Kai f00400), and caption fill/stroke measured on one frame per video.

Palette hexes are k-means centroids of JPEG frames, so they are slightly desaturated averages. Paint flat fills a little cleaner than the listed value.

---

## 1. Core constants (shared by every video)

The characters follow one template, and their colours are almost locked. Each video picks one **head fill** and one
**outline** and keeps them for every character in that video. The scene grade is applied on top (§6). The
characters are never repainted per shot.

| Constant | 01 Tree | 02 Brain | 03 Numbers | 04 Time | 05 Slots | **Series target** | Variation (CIE dE76) |
|---|---|---|---|---|---|---|---|
| Head fill | `#dce0e9` cool lavender-white | `#f6e1c7` cream-peach | `#f8efe6` | `#f3eeed` | `#fcf6e7` | **`#f7ede0`** | L\* 89–97. 03/05/04 sit within dE 2–6 of the target; 02 is peachier (dE 9); 01 is the cool outlier (dE 13, b\* −5). |
| Head shade | `#babfcf` | `#e2c2ab` | `#e9dbd9` | (flat) | `#f0c6af` | ~8–12 % darker, same hue | One soft shade band at most, on the side away from the key. |
| Outline | `#2f3d43` navy-charcoal (night `#140916`) | `#2e1d17` (Edison `#381b0f`) | `#2a1c1a` | `#2a2024` | `#421411` (Bling `#531c12`) | **`#2a1c1a`** | L\* 12–14 in 02–05 (dE ≤ 5 among 02/03/04). 01 is lighter and cool (L\* 25); 05 is redder (a\* 22). Max pair dE 34 (01 vs 05). |
| Outline weight | ≈ 1 % of frame width: 6–8 px at 720 w on an MS head, ~10 px in CU, uniform, no taper | | | | | | Constant in all videos. |
| Limbs (noodle strokes + ball hands) | `#362337` (measured, violet-brown) | `#1f1917` | `#1e1616` | `#2a2024` | `#421411` (hands `#2a1210`) | **`#2b1919`** | L\* 8–17. Same family as the outline (it *is* the outline colour in 04/05). |
| Face lines (eyes, brows, mouth) | `#1e0912` | `#3b2418` | = outline | = outline | = outline | = outline | — |
| Caption fill | `#ffffff` | `#ffffff` | `#ffffff` | `#ffffff` | `#ffffff` | **`#FFFFFF`** | Measured 253–255 per channel in all five. |
| Caption stroke | `#000000` | `#000000` | `#000000` | `#000000` | `#000000` | **`#000000`**, ~4 px at 720 w, plus a soft 50 % black drop shadow | Measured ≤ 4/255. Identical in every video. One word or phrase at a time, centred at y ≈ 860–950 of 1280. |
| Cast / contact shadow | sand `#c1aa8b` → `#867770` | — | — | deck `#ad825a` → `#64453c` | — | **`#2a2035` at 35–55 % (normal)** ≈ multiply `#a39ebd` | A soft blurred ellipse. It darkens the ground by 30–45 % and shifts it cool/violet, never toward neutral grey. |
| Sweat drop | `#6488aa` | `#a7cdd7` | `#8cb9db` | `#9fd3f0` | — | light blue + white highlight + outline | — |
| Tears | `#829aad`–`#9cc8ec` | | | | | | |

**Rules.**
- Heads and fills are never pure white `#ffffff`, and outlines are never pure black. The only pure white and pure black in the frame are the caption.
- The head is the largest bright, low-saturation shape in the frame. Keep head V ≥ 0.86 before grading.
- Use one outline colour per video for everything drawn: characters, limbs, hair strokes, faces. Environment contour lines are thinner and slightly lighter.
- Default for new videos: head `#f7ede0`, outline `#2a1c1a`, limbs `#2b1919`. 01's cool head and outline was a one-off that suited its blue-night story. Only do the same when most of the video is a cool grade.

---

## 2. Mood / lighting grades

Each grade is a reusable look: a background palette plus a full-frame colour treatment. The characters sit
*under* it. B and S are the mean HSV value and saturation over every frame of the listed ranges, with the p10–p90
range in brackets.

### 2.1 Day exterior
| Swatch | Role |
|---|---|
| `#348cd6` | sky zenith |
| `#bfe0f6` | sky horizon / haze |
| `#f5dfab` | key light (sun-lit sand, facade) |
| `#ceb683` | ground mid (sand, paving) |
| `#867770` | cast shadow |
| `#487440` | foliage |
| `#1f4c2c` | deep foliage / darkest shade |
| `#38add7` | accent: turquoise sea (04 uses safety orange `#ea872a`; 03 uses a coral car `#d98d6c`) |

**B 0.72 (0.58–0.87), S 0.42 (0.32–0.54)**, measured over 1,759 frames.
**Used in:**
- 01 S1–S4, S11, S13, S15, S16, S21 (f1–457, 860–904, 1060–1221, 1296–1525, 1950–2043)
- 03 S2, S4 (f109–300, 346–429)
- 04 S1, S4, S6 (f1–213, 438–615, 712–856)

**Character:** high-key. A blue sky meets warm cream ground, and one saturated accent sits in the mid-ground.

### 2.2 Golden hour / sunset
| Swatch | Role |
|---|---|
| `#a8709a` | sky zenith (lilac-violet) |
| `#ea8f98` | sky mid (pink-rose) |
| `#fad593` | horizon gold / key light |
| `#feefce` | rim light / highlight cream |
| `#d9a878` | ground lit (peach-honey) |
| `#6e4f5c` | shadow (mauve-brown) |
| `#e77372` | accent (sunset rose, string lights) |

**B 0.77 (0.70–0.85), S 0.40 (0.37–0.45)**, measured over 725 frames.
**Used in:**
- 01 S12 (f905–1059) and the S17 dusk opening (f1526–1560)
- 03 S6–S11 (f740–954, 1064–1290)
- 04 S9 (f1078–1170)

**Character:** the sky runs as a vertical gradient: violet → pink → yellow horizon (03: `#b07996` → `#f9a4a7` → `#fddea9`). It is the brightest grade but not very saturated. Characters get a warm rim. 01's sunset turns Kai's head cream `#fef9ed` and his outline warm brown `#8b6849`.

### 2.3 Night (moonlit blue)
| Swatch | Role |
|---|---|
| `#25325c` | sky / ambient navy |
| `#0c0b32` | deepest shadow (indigo-black) |
| `#082329` | foliage shadow (teal-black) |
| `#1d448f` | lit mid-tone blue |
| `#2c54a1` | bokeh / secondary blue |
| `#7d8ad3` | key / rim (periwinkle moon) |
| `#94a5f1` | head under the night grade |
| `#f5f7f8` | rain / lightning highlight |

**B 0.40 (0.28–0.49), S 0.67 (0.56–0.79)**, measured over 443 frames.
**Used in:** 01 S6–S8, S10 (f516–763, 814–859) and S17 night (f1580–1728).

**Character:** dark but *highly saturated*: the blue is pushed, not desaturated. The grade covers the character: Kai's head becomes `#8b96e2`–`#91a1ed` and the orange shirt goes brick `#835d64`. Lightning flashes are 2–4 frame white-outs (f575–577, f835–838).

### 2.4 Firelight / tungsten interior
| Swatch | Role |
|---|---|
| `#ffe680` | flame core / bare bulb |
| `#efa440` | key light (flame / tungsten amber) |
| `#c06436` | warm bounce glow |
| `#683a1c` | amber mid-tone (wood) |
| `#836673` | smoke / haze (grey-violet) |
| `#2a1c16` | shadow (warm brown) |
| `#0e0c0d` | falloff black / vignette |
| `#4650a8` | cool counter-fill (night, window, character body) |

**B 0.45 (0.29–0.77), S 0.47 (0.35–0.66)**, measured over 1,243 frames.

Sub-looks, with (B, S):
- 01 campfire (0.45, 0.44)
- 02 spotlit stage (0.31, 0.39)
- 02 Menlo Park amber (0.30, 0.70)
- 03 jail (0.54, 0.36)
- 04 lineup noir (0.44, 0.46)
- 05 machine interior (0.78, 0.61)

**Used in:**
- 01 S17 fire to S19 (f1729–1867)
- 02 S1–S5, S8 warm part, S9
- 03 S12
- 04 S7
- 05 S7

**Character:** one warm practical source with steep falloff into warm brown and black, and one small cool counter-colour (Theo's navy body, the lineup room's cold window `#e0e3e1`, the moonlit fill around the campfire). The amber "monochrome" variant (02 Menlo, 05 interior) reaches S ≥ 0.6.

### 2.5 Casino neon
| Swatch | Role |
|---|---|
| `#280a09` | shadow (near-black oxblood) |
| `#562521` | deep oxblood mid-shadow |
| `#ad1012` | machine red (dominant, 10 % of all pixels) |
| `#d23a30` | bright red accent (cap, stamp) |
| `#744b43` | warm brown mid (ceiling, wood) |
| `#e8bd42` | gold key light / marquee |
| `#f6ead3` | cream highlight (reels, heads) |
| `#24cfa8` | teal complement (the hero's shirt) |

**B 0.52 (0.45–0.57), S 0.59 (0.50–0.69)**, measured over 691 frames.
**Used in:** 05 S1–S6 (f1–541) and S8 (f779–928, under the x-ray overlay).

**Character:** about 65 % warm red, brown and gold. The *only* cool hue belongs to the protagonist (Lenny's teal `#19bda4`), so he pops. There is orange rim light from the machines on the head (`#e09542`), plus bloom on the chrome and LEDs.

### 2.6 Dream / underwater
| Swatch | Role |
|---|---|
| `#081129` | abyss navy |
| `#182443` | deep water |
| `#295b72` | water mid |
| `#53838d` | water light / god ray |
| `#362e67` | hypnagogia violet band |
| `#8690c6` | DEEP SLEEP lavender cast |
| `#9eb4cb` | head under the water grade |
| `#e7eff6` | caustics / bubble highlight |

**B 0.35 (0.17–0.55), S 0.47 (0.34–0.59)**, measured over 207 frames. Sub-looks: underwater (0.42, 0.48); DEEP SLEEP (0.18, 0.47).
**Used in:** 02 S6 depth chart (f718–862) and 02 S8 DEEP SLEEP grade (f983–1044).

**Character:** teal fades down into navy, and a violet band marks the "halfway" state. It holds the darkest moment of the series (02 at 33 s, B 0.17).

### 2.7 UI / X-ray / thermal / blueprint screens
All UI screens share a **near-black blue base** (`#021529`–`#130f2f`), corner vignettes, and **one hot accent ramp**.
They are the most saturated moments of a video (S 0.6–0.8) at mid-low brightness.

| Screen | Swatches (role) | B | S | Used in |
|---|---|---|---|---|
| **Radar** | `#021767` base · `#030f3a` vignette · `#2a4576` grid · `#898aa5` cloud mass · `#d9d1ef` sweep · `#e01436` alert pill · `#ffffff` text | 0.49 (0.43–0.55) | 0.63 (0.53–0.77) | 01 S5 f458–515 |
| **X-ray** | `#021529` base · `#032842` field · `#285f78` organs · `#558ba4` soft tissue · `#96d9e2` glow · `#dcf2f7` bone · `#3fd8e8` wireframe (05) · `#cf6f43` hot label | 0.38 (0.35–0.39) | 0.76 (0.76–0.81) | 01 S14 f1222–1295 (full screen); 02 S4 Theo X-ray layer (`#6faac8`/`#306a87`, outline `#a8d8ef`); 05 S8 wireframe `#40a7a7`→`#3fd8e8` |
| **Thermal** | `#130f2f` base · `#4c2830` cold · `#acb3ea` cool body · `#b30a86` magenta · `#ef7b2b` orange · `#fcd84c` hottest · `#fbf6e9` white-hot | 0.45 (0.42–0.45) | 0.61 (0.58–0.64) | 01 S20 f1868–1949 |
| **Blueprint** | `#2e4272` paper · `#445987` grid · `#19254b` edge vignette · `#becde9` chalk line · `#aca7a9` faded chalk · `#996946` clipboard · `#6f4628` wood shadow | 0.49 (0.47–0.51) | 0.64 (0.49–0.70) | 04 S5 f616–711 |

Cyan means "science / look inside" in every video where it appears (01, 02, 05).

### 2.8 Extra grades found in the pilot
| Grade | Swatches (role) | B | S | Used in |
|---|---|---|---|---|
| **Daylight interior** | `#f2e8da` cream wall/key · `#90bbe1` window/porthole sky · `#c79e71` brass/honey wood · `#a7523a` red-brown wood · `#5e3f2d` shadow · `#528385` teal wall/glass · `#9fc1a5` mint wall (fluorescent) · `#dad3ae` beige floor | 0.73 (0.60–0.81) | **0.33** (0.24–0.39) | 03 S1, S5; 04 S2, S3, S8 (normal) |
| **Red alarm** | `#f3bea0` lit peach · `#d2351e` red overlay · `#ea6934` orange ray · `#ea7275` pink falloff · `#761f15` deep-red shadow · `#958ddc` sky shifted lilac · `#f3e9f1` highlight | 0.84 | 0.52 | 04 S8 f982–1066 |
| **Paper insert** | `#e1d8c2` paper · `#d0bfa2` shade · `#2e1e24` ink · `#fae18e` warm-lit paper · `#ab6d3f` cork · `#e5c093` card · `#c0392b` red ink/string · `#f9e611` highlighter | 0.70 (0.62–0.82) | 0.43 (0.25–0.61) | 01 S3, S9; 02 S7; 04 S10; 05 S7 par sheet |

Grade ranking by brightness: red alarm 0.84 > sunset 0.77 > daylight interior 0.73 ≈ day exterior 0.72 > paper 0.70 >
casino 0.52 > blueprint/radar 0.49 > firelight 0.45 = thermal > night 0.40 > x-ray 0.38 > dream 0.35.
Grade ranking by saturation: x-ray 0.76 > night 0.67 > blueprint 0.64 > radar 0.63 > thermal 0.61 > casino 0.59 > …
> day 0.42 > sunset 0.40 > daylight interior 0.33.
**Dark grades are the saturated ones.** Bright daylight grades stay at S ≈ 0.33–0.42.

---

## 3. Accent / semantic colours

| Meaning | Hex | Range seen | Where |
|---|---|---|---|
| **Danger / wrong / "house wins"** | **`#e0302a`** | `#e22924` `#d64444` `#d3361f` `#e60f04` `#d2412b` | 01 trunk X, 03 circling ellipse, 04 cap/PANIC/alarm, 05 stamp and wedge |
| Alert pill | `#e01436` + white text | — | 01 severe-storm pill |
| LED red | `#ff2a1a` on `#1a0505` | `#e94d42` `#f15f4f` | 04 CHRONO-2, 05 CREDITS/WIN |
| LED amber | `#f2a33a` on `#2a1f1c` | — | 03 dot-matrix counter |
| **Warning / hazard** | **`#f4c33a`** + `#2a2024` stripes | — | 04 deck edge, PANIC box, harness lining |
| Safety orange | `#ea872a` | `#e7722b` `#dd7c21` | 04 tower / ride world |
| **Highlight / answer / jackpot** | **`#f6c75a`** → glow `#ffe9a8` | `#f9e611`→`#f5b015`, `#f2c230`, `#faca44` | 03 "starts with 1" buttons, 05 jackpot row, signage |
| Glow / glint / revelation | `#fffaf0` | `#fff79e` `#f6eceb` | 02 impact arcs, 03 six-heads glow |
| **Money green** | **`#8fcf8a`** | `#5c9272`, slot glow `#2fe07a` | 03 cash, 05 bill acceptor |
| Science cyan | `#3fd8e8` | `#40a7a7` `#96d9e2` `#6faac8` | X-ray / wireframe |
| Data mint | `#a2e7df` | — | 02 EEG trace |
| Cool counter teal | `#3ab3a9` | `#41918b` `#19bda4` | 03 chairs and kiosk, 05 hero |
| Brand navy | `#203278` | `#243064` | 04 banners, blueprint |
| Police wash | red `#ca6d68` / blue `#7f8fd0` | — | 03 alternating overlay |
| Fire ramp | `#ffe680` → `#efa440` → `#d5401a` | — | 01 |
| Thermal ramp | `#fbf6e9` → `#fcd84c` → `#ef7b2b` → `#b30a86` → `#4c2830` → `#130f2f` | — | 01 |
| Categorical set (8) | `#e25b5b` `#f08a3c` `#b9c64a` `#5cc2b0` `#7da8ee` `#9a7ae0` `#d385c3` `#e48fb5` | — | 03 floor buttons 2–9 |
| Coins | gold `#e8bf67` / copper `#895a32` | — | 03 |
| **Emotion tints (head fill swaps)** | blush `#f0a0a8` · red-hot `#da767a` · anger vein `#e03a2a` · sick `#9fbf9a` · queasy `#9c9cbb` · under-eye red `#d86a6a` · blisters `#e8a0b0` | — | 01 Kai, 04 Gil |

Rules:
- Red always means danger, wrong or loss. Yellow-gold always means the answer, the good outcome or the jackpot.
- One red accent per scene at most.
- A whole-head tint is the only time a character's base colour changes (queasy, sick, red-hot).

---

## 4. Character clothing palette

**Rule.** Each torso is one **solid, saturated mid-tone** (HSV S 0.45–0.92, V 0.47–0.91, measured over the 22
clothed characters). Pick its hue to *contrast with that character's main background*. It is usually complementary or
at least 90° of hue away:

| Hero on background | Torso | Background |
|---|---|---|
| Kai on sky, sea and navy night | orange `#e05f13` | blues |
| Theo on the brown stage | navy `#3a5080` | warm browns |
| Rico on the desert | mustard `#d9a23f` | teal / sky-blue accents |
| Marge on the sunset | purple `#814eab` | peach-gold sunset |
| Dex on the sky | orange/yellow `#dd7c21`/`#e8ae2d` | blue sky |
| Lenny in the casino | teal `#19bda4` | red / gold casino |

- Role costumes (Klaus's white coat, Edison's black suit, Bling's cream tank top) separate from the background by **value** instead of hue.
- In group shots, give every person a different hue family (04 support group: red, blue, pink, red, purple; harness riders: orange, green, purple, teal).
- Patterns are a second colour at low coverage: Kai's flowers, Lenny's yellow leaves.
- Hair is a dark-to-mid brown cap (`#32201e`–`#a2513b`), or the outline colour.

| Character | Video | Head | Outline | Hair | Clothing (part) |
|---|---|---|---|---|---|
| Kai | 01 | `#dce0e9` | `#2f3d43` | outline (curly sprouts) | shirt `#e05f13` (shade `#b94a0f`) · flowers `#f3e6d3` · flower centres `#ba190f` · leaf print `#1a6747` · shorts `#3b3f6a` · sandal soles `#e0c050`; limbs `#362337` |
| Theo | 02 | `#f6e1c7` | `#2e1d17` | `#694532` | pill torso `#3a5080` · shade `#2d3d5f` · sheen `#5a6fa0` |
| Edison | 02 | `#f2d6b0` | `#381b0f` | `#c9bba8` (warm-lit `#c49779`) | black suit `#1e0c05` · shirt V `#fcd496` · bow tie `#1a0c06` |
| Rico | 03 | `#f8efe6` | `#2a1c1a` | `#3b2820` | mustard jacket `#d9a23f` · tie `#88422e` · lanyard clip `#4a6fb3` · jail jumpsuit `#e0631f` |
| Marge | 03 | `#f7e7df` | `#2a1c1a` | `#a2513b` | purple suit `#814eab` · blouse `#f6d5d0` · pencil `#c8463a` · magnifier `#caa16f` |
| Officer Dale | 03 | `#f9efe6` | `#2a1c1a` | `#32201e` | uniform `#314579` · cap `#36517e` · star `#ebca60` · badge `#c2922b` |
| Nina | 03 | `#f8efe6` | `#2a1c1a` | `#6b4630` | teal uniform `#67b7ac` |
| Dex | 04 | `#f3eeed` | `#2a2024` | `#6c4d3e` | harness `#dd7c21` · lining `#f4c33a` · T-shirt `#e8ae2d` · cap `#d64444` |
| Dr Klaus | 04 | `#f3eeed` | `#2a2024` | `#2a2024` | lab coat `#e6eaee` (shade `#c9ced6`) · tie `#7a2a2a` · pens `#d04a3e` / `#3b6fd0` |
| Noggin | 04 | brain `#f2c0c6` | `#2a2024` | — | visor `#8bd391` · gyri `#d2979e` · pencil `#f2c94c` |
| Amy | 04 | body `#be8661` | `#2a2024` | — | light side `#e3b17b` · grain `#654d39` |
| Elmer | 04 | `#f3eeed` | `#2a2024` | tufts `#f4f1ee` | harness `#4e9c5a` · straps `#ec9928` |
| Gil | 04 | `#f3eeed` (queasy `#9c9cbb`) | `#2a2024` | `#2a2024` | T-shirt `#7a58a8` · harness `#dc7745` |
| Tad | 04 | `#f3eeed` | `#2a2024` | `#2a2024` | harness `#3e9a8c` · straps `#ed9223` |
| Gus | 04 | `#f3eeed` | `#2a2024` | `#c36f48`\* | red shirt `#d65a50`\* · neck brace `#f1f1f1` |
| Carl | 04 | `#f3eeed` | `#2a2024` | `#544231`\* | blue shirt `#4a6ac0`\* · bandage `#f1f1f1` + dot `#d0483d` |
| Deb | 04 | `#f3eeed` | `#2a2024` | grey `#cfc0b9`\* | pink top `#e66ba1`\* |
| Ray | 04 | `#f3eeed` | `#2a2024` | `#ddc283`\* | red shirt `#c9594b`\* |
| Mo | 04 | `#f3eeed` | `#2a2024` | `#423731`\* (hair + beard) | purple shirt `#6e4fb0` · leg cast `#f1f1f1` |
| Cooper | 04 | `#f3eeed` | `#2a2024` | `#c35a36`\* | salmon shirt `#d49a72` (sunset-lit `#f3916c`\*, shade `#c65c3f`) · red cup `#d23a30` |
| Hank | 04 | `#f3eeed` | `#2a2024` | (hat) | plaid shirt `#7e87a7`\* · straw hat `#f6d488` · band `#a55e31`\* |
| Biscuit (dog) | 04 | fur `#af7a53` | `#4f2928` | — | — |
| Lenny | 05 | `#fcf6e7` | `#421411` | `#351518` | teal shirt `#19bda4` (shadow `#138f7d`) · leaf print `#e9c23a` · lanyard `#cd1a15` |
| Bling | 05 | `#fdf7dd` | `#531c12` | (cap) | tank top `#fbedd4` (shadow `#cba78f`) · cap `#e83234` · gold chain `#d9a43a` |
| Beanie | 05 | cream | `#3a1512` | (beanie) | beanie `#e8a42a` · dark jacket ≈`#2a1c1a` |

\* new pixel samples for this document. They fill gaps in the character sheets: 04 f00380 for the support group, f01125 for the BBQ. Sunset-lit values are marked.

---

## 5. Contrast rules

1. **Value separation first.**
   - The cream head (V ≈ 0.9–0.98) is always lighter than the background behind it.
   - On bright plates (sky, cream walls, sunset), the thick dark outline does the separating.
   - On dark plates (02 stage, 05 casino, 01 night), the head is the brightest thing in frame apart from practical lights.
   - Never put a head on a background lighter than the head without a dark outline and a darker halo or shadow.
2. **Hue separation for the torso** (§4). The torso hue is complementary to the dominant background hue. The hero owns the scene's one counter-colour.
3. **Rim light.** Warm grades add a 2–6 px rim of the key-light colour on the head edge:
   - 05 machines `#e09542`
   - 03 sunset on Marge
   - 01 sunset `#fef9ed`
   
   Night grades use a cool periwinkle `#7d8ad3`. The rim sits *inside* the outline.
4. **Vignette.**
   - Present on interior and UI shots: 02 stage closes to black (S3 POV); 04 blueprint has a soft edge vignette; UI screens have dark corners.
   - Exterior day shots have little or none.
   - Measured corner/centre luminance ratios (these include scene content, so read them as an upper bound on the vignette itself):
     - spotlit or noir interiors (02 f45, f660; 04 f870): 0.28–0.35
     - casino (05 f55): 0.69
     - UI screens (01 f1250, f1900): 0.11–0.22
     - day exteriors (01 f30, f2020; 03 f380; 04 f451): 0.66–0.83
     - sunset (03 f850): 0.95
   - Build the vignette into interior and UI plates, and keep day exteriors open.
5. **Depth.** Far layers lose contrast and gain haze colour (`#bfe0f6` by day, `#feefce` at sunset, smoke `#836673` at night). Depth-of-field blur on far layers is constant. Characters stay sharp.

## 6. Colour-grading notes

- **Grade over, don't repaint.** The scene grade is an adjustment layer over the whole composite, characters included. Examples:
  - Kai's head goes `#8b96e2` at night, `#d1a79b` firelit and `#fef9ed` at sunset.
  - Theo's goes `#9eb4cb` underwater.
  - Edison is always amber.
  
  Keep the base character colours neutral (§1) and let the grade tint them.
- **Warm/cool split.** Almost every scene has a warm key and a cool fill or counter-colour:
  - 01 fire against the navy night
  - 02 amber stage against Theo's navy body
  - 03 terracotta/brass against teal
  - 04 tungsten pendant against the cold window
  - 05 red/gold casino against the teal hero and the x-ray cyan
- **Bloom.**
  - Soft bloom on every practical light: bulbs, LEDs, chrome, fire, sun flares.
  - Strong bloom only on "revelation" beats: 03 gold bloom on the panel f693+, 05 machine opening, 02 bulb.
  - Glints are `#fffaf0` stars.
- **Mood shifts are full-frame.** Emotional state changes are shown with a full-frame grade shift, applied over about 0.3–1 s:
  - 04 red alarm
  - 02 DEEP SLEEP lavender
  - 01 dusk → night → firelight, animated inside one shot (S17)
  
  Characters are not recoloured. The exception is the head-tint emotions in §3.
- **Brightness and saturation work against each other.**
  - Danger and "inside the problem" beats go darker and *more* saturated: navy night, neon UI, casino red.
  - Relief and "answer" beats go brighter and *less* saturated: daylight, sunset, cream paper.
  - Correlation of brightness with saturation over all frames:
    - 01: −0.63
    - 04: −0.44
    - 02, 03, 05: about 0 (each stays inside one family of grades)
- **Lightning and flash frames:** 2–4 frames near white (01 f575–577, f835–838).

## 7. Per-video brightness / saturation over time

Values are 1-second means of the per-frame metrics (×100). The full per-second arrays are in `color_system.json → videos`.

### 01 This Tree Hates You (68 s): mean B 0.61 (σ 0.19), S 0.51. Brightness swings the most of any video.
```
t(s)  0    5    10   15   20   25   30   35   40   45   50   55   60   65
B     72 71 69 77 79 78 71 70 62 62 57 63 64 64 63 50 52 32 28 28 34 42 40 40 56 73 82 49 48 51 79 83 82 82 82 86 88 88 87 86 72 38 36 60 64 64 68 64 63 81 77 41 37 37 38 39 40 44 50 44 37 50 43 44 48 91 92 93 92
S     40 40 44 49 60 69 30 31 43 46 49 44 42 42 41 63 60 64 72 71 77 80 80 77 71 49 41 60 54 39 35 37 37 37 37 38 41 41 41 44 49 77 81 47 49 49 44 48 48 53 54 48 57 57 57 56 56 43 37 39 62 41 56 63 56 44 39 38 38
```
| Time (s) | Beat | Look |
|---|---|---|
| 0–7.5 | Hook | Bright day; the aerial sea peaks at S 0.69. |
| 7.5–15 | "Harmless… red X" | Day, slowly dimming to 0.57–0.64. |
| 15 | Storm | Radar UI. |
| 17–24 | "Big mistake" | **Trough of the video**: navy night, B 0.22–0.34 with S up to 0.80. |
| 25–27 | Blisters | Flat diagram flash, B 0.82. |
| 30–40 | "Next morning / apples smell incredible" | Sunset and god-ray day, B 0.82–0.88 at low S: a false relief. |
| 41–42 | "Fire" | X-ray dip, B 0.36, S 0.81. |
| 43–50 | Leaves / lagoon | Mid-bright. |
| 51–65 | Night + smoke + thermal lungs | Long low plateau, B 0.37–0.50. |
| 65–68 | Punchline "just sit in the sand" | **Brightest frames of the video**, B 0.93. |

Pattern: each new danger takes the frame down into a saturated blue or neon look; the payoff ends in high-key daylight.

### 02 Your Brain's Secret Idea Zone (39 s): mean B 0.34 (σ 0.11), S 0.46. The darkest video.
```
B  32 28 30 34 28 31 30 30 30 32 36 28 24 28 28 30 30 28 32 34 38 30 28 30 31 28 44 53 60 62 63 49 28 17 20 35 35 32 27 27
S  36 40 39 34 38 39 38 37 37 36 40 49 45 47 47 46 45 45 39 34 42 72 74 66 51 60 54 36 42 61 60 57 57 46 49 59 43 36 35 35
```
| Time (s) | Beat | Look |
|---|---|---|
| 0–20 | Setup and experiment | Flat low-key spotlit stage, B ≈ 0.30. The X-ray section (12–20 s) raises S to about 0.47. |
| 21–23 | Edison | Saturation spike to S 0.74 (amber Menlo Park) at the same low brightness. |
| 24–29 | Hypnagogia | Underwater, B rising 0.31 → 0.53. |
| 29–31 | Ideas | Corkboard, the **only bright section** (B 0.60–0.63). |
| 33 | Deep sleep | DEEP SLEEP lavender, the **darkest frame of the series** (B 0.17). |
| 36–39 | Wake up | Back to the opening stage (bookend, B 0.27–0.35). |

Pattern: brightness = "idea light". It peaks exactly on the idea beat and bottoms out on deep sleep.

### 03 Why Humans Can't Pick Random Numbers (47 s): mean B 0.71 (σ 0.09), S 0.37. The flattest curve. The whole video sits in one warm, desaturated desert family.
```
B  57 57 60 66 76 75 74 72 72 71 67 71 72 73 73 73 73 73 73 74 75 76 77 80 80 81 79 80 81 72 73 70 56 54 55 73 85 85 81 75 79 83 82 55 54 55 54 54
S  40 39 34 30 28 31 33 34 33 30 20 24 32 32 32 33 35 35 35 35 37 38 36 36 39 41 37 37 38 42 42 42 44 46 43 40 39 39 42 46 43 40 40 35 35 36 37 37
```
| Time (s) | Beat | Look |
|---|---|---|
| 0–4 | Office | B 0.57. |
| 4–10 | Noon heist | B 0.72–0.76. |
| 10 | Police car | Grey dip, S 0.20, the least saturated second of the series. |
| 14–25 | Elevator explanation | Steady warm climb, 0.72 → 0.80. |
| 25–29 | Sunset "number city" | B ≈ 0.80. |
| 32–35 | Coin board | Dip, B 0.55. |
| 36–43 | Window-ledge sunset reveal | Peak, B 0.85. |
| 43–47 | Jail | Amber, B 0.54. |

Pattern: the clock moves from noon to sunset as the explanation unfolds. The verdict (jail) drops the brightness.

### 04 The Scientist's Insane Time Test (40 s): mean B 0.68 (σ 0.13), S 0.41.
```
B  67 73 77 82 79 78 77 79 81 79 81 77 74 71 68 60 57 56 55 56 59 49 48 54 66 70 78 78 62 38 41 47 75 85 84 81 72 69 75 71
S  44 38 32 23 32 33 31 21 34 30 24 25 26 28 28 41 39 38 36 47 49 65 70 66 59 55 51 50 47 50 48 43 42 55 52 45 43 46 37 26
```
| Time (s) | Beat | Look |
|---|---|---|
| 0–14 | Hook, brain room, support group | High-key and low-saturation: day, cream room, fluorescent; B 0.74–0.82, S 0.21–0.34. |
| 15–20 | Platform | Darker steel deck, B 0.56. |
| 21–23 | Blueprint hypothesis | Saturation peak, S 0.70, B 0.48. |
| 24–28 | Landing | Hard sun. |
| 29–32 | "Not one of them could tell him" | **Trough**: lineup-room noir, B 0.38. |
| 33–36 | "Frightened brain" | Red alarm, **peak**, B 0.85 (bright *and* red). |
| 36–39 | Sunset BBQ | B 0.72. |
| 39–40 | Flipbook | Paper, low S 0.26. |

Pattern: the failed-result beat is the darkest; the explanation beat is the most intense colour.

### 05 The Science Behind Slot Machines (31 s): mean B 0.58 (σ 0.13), S 0.60. The most saturated video; saturation is nearly constant (σ 0.06).
```
B  59 50 54 51 49 43 44 46 47 51 51 55 56 56 55 54 52 54 70 82 82 82 82 77 77 75 52 51 53 53 47
S  57 65 66 65 63 68 69 69 60 54 54 55 57 56 62 62 60 66 66 56 56 56 56 63 64 64 50 51 49 49 56
```
| Time (s) | Beat | Look |
|---|---|---|
| 0–18 | Losing streak, buddy, "teasing you" | Dark red casino, B 0.43–0.56; the low point is the second near-miss at 5.7 s. |
| 18–26 | "Crack it open" | The machine opens into the amber interior and par sheet: B jumps to 0.82, the **answer is literally lit**. |
| 26–31 | Verdict | Back to the casino plus cool x-ray cyan, B 0.50. |

Pattern: brightness marks understanding; saturation stays high throughout to keep the casino's sensory overload.

### Cross-video template for new scripts
| Beat | B | S | Grade |
|---|---|---|---|
| Hook | 0.55–0.75 | 0.35–0.5 | the video's home grade |
| Problem / danger | B ↓ to 0.25–0.45 | S ↑ to 0.6–0.8 | night, neon, UI, casino |
| Explanation / insight | B ↑ to 0.75–0.85 | — | sunset, paper or a "lit inside" — often the brightest beat |
| Verdict / twist | B ↓ about 0.2 | — | a short dip (jail, lineup, casino) |
| Final button | — | — | either a bookend of the opening look (02, 05) or a high-key release (01 B 0.93, 04 sunset) |
