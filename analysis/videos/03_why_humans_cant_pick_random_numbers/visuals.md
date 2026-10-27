# 03 — Visual analysis

## STYLE LOCK (reuse verbatim in every prompt for this video)
```
Stylised 2.5D cartoon explainer frame: flat 2D vector characters with large perfectly round warm-white heads, thick
uniform dark-brown/black outlines (about 1% of frame width), minimal faces (dot or hollow-circle eyes, single thick
brow strokes, simple line mouths), capsule/bean-shaped torsos in solid flat colours, black noodle stick limbs ending
in black ball hands, no noses; composited into a richly detailed semi-realistic 3D-rendered retro mid-century
American desert world (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal, brass) with painted
textures and thin dark ink contour lines, soft global illumination, warm golden or sunset light, gentle bloom,
subtle depth of field on far layers, clean digital finish, no film grain, no photo-realism in characters.
```

## 1. Art style overview
- **Two layers of rendering style.** (a) Characters are flat 2D cel drawings: one fill colour per part, a thick dark outline
  (≈7 px at 720 wide), one soft shading band on the head (lit side / shade side split, e.g. Marge #1075, #1300) and a glossy
  highlight stripe on hair caps. (b) Environments and props look 3D-rendered: correct perspective, soft GI shadows, specular
  glints on car paint and brass, volumetric light shafts, depth-of-field blur — but every edge also carries a thin ink line
  ("toon outline over 3D", like Blender Line Art/Freestyle or an AI image that imitates it).
- **Character construction** (all characters share one rig): circle head ≈ 1.0 head-unit wide; capsule torso ≈ 1.3 heads tall;
  stick legs ≈ 1.6–1.8 heads; total ≈ 4–4.3 heads tall. Limbs are single black strokes with a ball hand (a black circle
  ≈ 0.18 head). Clothing is drawn on the capsule (lapels as lines, a tie, a pocket, a lanyard clip). Hair is a separate cap
  shape with a centre part line.
- **Faces** are tiny and graphic, placed in the lower-middle of the head: eyes = dots (neutral), half-lidded dots (smug),
  hollow circles with small pupils (shock/worry), curved lines (eyes closed); brows = single thick strokes that carry most of
  the emotion; mouths = tiny line, "~" wavy line (worry), open teeth grin (rectangle with 4–6 teeth), gritted grid (panic).
  Faces switch as whole drawings (face-swap), no tweening.
- **Text inside the scene** is real, legible typography placed on props: cheque serif caps "DESERT STATE TREASURY / PHOENIX, ARIZONA",
  handwritten blue-ink amounts ("87,439.12", "100,000.00", "874"→"8746"), brass plaques with engraved serif caps ("ACCOUNTS PAYABLE",
  "AUDIT"), LED dot-matrix numerals on the bank sign, art-deco "THE ONE" on the button panel, hand-scrawled 7/8/9 on the jail wall,
  pencil handwriting "HHTHHHHHHT… flips — longest run?" on a legal pad. Numbers that change over time (LED counter, written
  amounts, lit buttons) are animated overlays, not baked into the plate.

## 2. Lighting moods (in story order)
| scene | mood |
|---|---|
| AP office (S1) | warm afternoon daylight, venetian-blind diagonal light stripes on desk/characters |
| Bank drive-through (S2) | bright desert noon, pale-blue gradient sky, sun flare top-left; police strobe wash red/blue #285–298 |
| Police car (S3) | flat cool interior daylight |
| Tower exterior (S4) | saturated midday blue sky, cumulus |
| Elevator interior (S5) | soft bright daylight through glass; turns golden with bloom at #693 (narrative light change) |
| Facade / number city (S6) | golden-hour sunset gradient violet→pink→peach→yellow, haze |
| 19th-floor audit office (S7–S11) | sunset through a panoramic window, strong god-rays, warm lamp |
| Jail (S12) | amber back-window light, cool steel bars |

The day progresses **noon → sunset** across the story (crime by day, judgement at sunset).

## 3. Depth / parallax layers seen
- S1: cheque+pen (near) / Rico + desk (mid) / window, frames, cabinets (far).
- S2: bank sign & canopy (near, wipes out during the dolly) / car + Rico (mid) / building, palm, sky (far).
- S3: chain-link cage + mesh over the lens (near, moves fastest) / Rico (mid) / rear window desert (far).
- S4: palms, police car, low wing (near) / tower (mid) / sky, clouds (far) — orbit parallax visible.
- S5: Dale cut by frame edge (near) / Rico + panel (mid) / glass wall with ghost reflection + outside (far, blurred).
- S6: rooftop corner (near, from #829) / tower "1" + number buildings + strip mall (mid) / desert, mesas, clouds (far) — true 3D.
- S7: desk + plaque (near) / Marge (mid-near) / Dale, Rico, elevator cab (mid) / window sky (far, blurred).
- S12: bars (near) / Marge outside bars (near-mid) / Rico (mid) / brick wall with scribbles (far).

## 4. VFX inventory
| VFX | frames | look | build |
|---|---|---|---|
| Sweat drop | #77–105, #204–240, #279–303, #1177–1188, #1380–1413 | light-blue teardrop (#8cb9db) with white highlight + dark outline, on the side of the head; 1 drop (or 3 in the lens) | 2D sprite, pops on (0 frames in), slides/bobs 1–2 px |
| Head tremble | #77–105, #1197–1222 | 1–3 px random offset per frame | AE wiggle (freq 15, amp 2) |
| Sparkle glint | #47–52, #1291–1390, lens rim, coin | white 4-point star with soft glow | sprite, scale 0→1→0 over 6 frames |
| Googly eyes on digits | #49–105 | small white circle eyes with dot pupils on the "8" and "7" inside the magnifier | 2D sprites parented to the cheque layer |
| LED counter | #107–130 | orange dot-matrix numerals on black, $0 → $2,000,000, ≈+90 k per frame then ease-out | code/AE expression (number text + dot-matrix effect) |
| Cash sparkles | #125–150 | green "$" bits/sparkles around the capsule | particles |
| Police light wash | #285–298 | full-frame tint alternating blue (#a87387 mix) and red (#ca6d68 mix) every ≈5 frames | solid colour layers, blend Color/Overlay at ~35 % |
| Rainbow button glow | #475–700 | each button 2–9 lights a different hue (red, orange, yellow-green, teal, blue, violet, magenta, pink) with a soft halo | AE glow on per-button colour layers, 2 frames per button |
| Gold button glow + bloom | #553–736 | 1 and 10–19 light identical gold; at #693 the whole panel blooms and warms the frame | glow + global warm grade |
| Glass reflection ghost | #465–736 | faint mirrored Rico on the glass wall (left) | duplicate character layer, flipped, 15 % opacity, blurred |
| Coin strobe trail | #903–933 | vertical stack of 8–12 glowing coin after-images | echo effect / particle trail |
| Dust motes | S7–S8 | floating white specks | particle layer |
| Coin pour | #955–985 | coins tumble and settle into slots | 3D rigid body or AE sprite animation |
| 6-run highlight | #1021–1060 | coins light one by one with yellow glow + white sparkle, then a red outlined ellipse (#1042) | glow + shape layer (ellipse stroke) |
| Pen vibration marks | #1176–1186 | 2–3 curved "((" lines beside the pen | 2D sprites, flicker |
| Defocus + double exposure | #1253–1290 | full-frame lens blur ramp; number-skyline ghosted over the cheque stacks at ≈40 % | camera lens blur + opacity layer |
| Magnifier lens | #34–105, #1360–1413 | gold-rimmed lens showing a scaled-up copy of what's behind it (true magnification), sparkle on rim | AE: duplicate layer scaled 1.6–2×, masked by circle |
| Motion blur | #267–270 (capsule), #1145–1160 & #1209–1228 (whip pans) | directional blur | render motion blur / CC Force Motion Blur |

## 5. Captions
- **Font look:** heavy geometric sans, all lower-case as spoken (numbers as digits: "19", "ten"/"two" as words when spoken), similar to
  Montserrat Black / Gilroy Heavy. White fill (#ffffff), black outline ≈ 4 px, plus a soft dark drop-shadow (≈ 3 px down, 50 %).
- **Size:** x-height ≈ 28 px, cap height ≈ 38 px on a 720-wide frame (≈ 5 % of width), single line.
- **Position:** horizontally centred, baseline ≈ y 920 (centre ≈ y 900, i.e. 70 % of frame height) for the whole video.
- **Words per card:** 1–3 (≈120 cards in 47 s); each card held 3–20 frames, switched on the spoken word (hard cut, no pop, no
  colour highlight, no animation).
- Captions sit over everything (top layer), including VFX and dissolves.

## 6. Transitions
| type | count | frames | notes |
|---|---|---|---|
| Cross-dissolve on moving cameras | 8 | 106–112, 298–303, 342–348, 737–741, 869–876, 952–957, 1060–1066, 1287–1294 | 5–8 frames, linear; at #106–112 the incoming LED sign is visible over Rico's face |
| Hard cut | 1 | 430 | exterior → elevator interior ("Step into the elevator") |
| Camera move-through / whip pan | 2 | 1145–1160, 1209–1228 | same set, motion blur, roll |
| In-shot move-through | 2 | 163–200 (dolly into car), 751–840 (crane-out to city) | replace a cut |

## 7. How each element was most likely made (hypotheses + evidence)
| element | hypothesis | evidence |
|---|---|---|
| Characters | 2D vector puppets (Adobe Animate / AE with Duik / Moho) with a face-swap library | identical line weight at every scale; faces switch in one frame with no in-betweens; ball hands & stick limbs bend like simple IK; same rig for Rico, Marge, Dale, Nina |
| Faces | drawn sprite sheet per character, swapped per frame | expression holds of 3–60 frames, blink = 1–2-frame swap (#268, #310, #519) |
| Environment plates (office, bank, elevator, audit office, jail) | AI-generated stills in a consistent "3D toon" style, then layered for 2.5D parallax | painterly-3D look with ink lines; tiny text glitches in background lettering (e.g. the bank façade lettering behind the tube #140) while foreground hero text is crisp (overlaid) |
| Big camera moves (S2 dolly, S6 crane-out, S4 orbit) | either real 3D scenes (Blender) or AI image-to-video on the plate | continuous parallax of many depth layers, perspective change of buildings, consistent lighting through the move; S6 has dozens of independently parallaxing houses — hard to fake with 3–4 planes |
| Number skyline 1–9, tower "1" | 3D (extruded digit buildings) or AI image with 3D-looking digits | digits change perspective correctly during the crane |
| LED counter, written cheque amounts, lit buttons, 6-run glow | After Effects text/shape layers over the plate | numbers change per frame with perfect legibility; glows are additive and clean |
| Coin board pour | 3D rigid-body sim or AI video | coins tumble with perspective and shadows |
| Captions | auto-caption tool (CapCut / Submagic-style) or AE text from SRT | 1–3 words per card, consistent font, timing matches the SRT |
| Colour grade | global warm grade per scene + bloom | identical warm cast on characters and backgrounds in sunset scenes |
