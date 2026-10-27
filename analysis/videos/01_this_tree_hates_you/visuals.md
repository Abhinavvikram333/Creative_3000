# Visuals — 01 "This Tree Hates You"

## STYLE LOCK (reuse verbatim in every prompt)
```
Stylised 2.5D cartoon explainer frame: flat 2D vector-style stick-figure character with a very large round pale-lavender head, thick uniform dark navy-charcoal outline (~5–6 px at 720 px width), minimal face (dot or ring eyes, single-stroke brows, tiny line mouth), noodle stick limbs, flat cel colours with one soft shadow tone, composited into a richly painted semi-realistic tropical environment (painterly / 3D-rendered look, soft depth of field, thin dark ink contour lines on props), saturated turquoise sea and bright blue sky by day, deep blue-navy by night, clean digital finish, no grain.
```

## 1. Art style
| Element | Look | Evidence (frames) |
|---|---|---|
| Character (Kai) | Flat 2D vector cut-out: solid fills, **one** soft shadow tone on the head, thick uniform dark outline (~5–6 px in MS, ~10 px in CU), stick limbs drawn as outlined strokes. No texture. | f00400, f01100, f01805 |
| Environments | Painterly / semi-3D illustration: volumetric canopy with hundreds of individually outlined leaves, soft ambient occlusion, sand texture, shallow depth of field (blurred far sea, blurred foreground grass). Thin dark **ink contour lines** on the trunk, branches, logs and bush keep it "cartoon". | f00400 tree, f01300 bush, f01600 logs |
| Inserts | Clean flat infographic/medical illustration (skin cross-section, leaf diagram, X-ray skeleton, thermal lungs) with glows and simple gradients. | f00805, f00660, f01250, f01900 |
| Poster | Vintage engraving + serif typography on aged paper (pastiche of a botanical field-guide plate). | f00200 |
| Aerial | Soft photoreal-ish 3D render / generated video: real perspective parallax, fine grain, slightly mushy detail. | f00095–f00184 |
| Car | Glossy semi-3D cartoon car (cel-shaded reflections, chrome highlights, ink outlines). | f00900 |

**Layering = 2.5D.** The flat character sits on top of a deep painted plate. You can see it in: (a) the character's
outline weight never changes with depth; (b) Kai's cast shadow is a soft grey blob on the sand (f00400, f02040), not a
lit shadow; (c) scene grades are applied over the character (blue at night, cream/warm at sunset, grey in smoke,
orange in firelight), as in a comp adjustment layer.

## 2. Lighting moods
| Mood | Shots | Notes |
|---|---|---|
| Bright tropical midday | S01, S02, S04, S09-bush (S15), S16, S21 | High-key, turquoise sea, white cumulus. The neutral grade on Kai. |
| God-ray day | S13 | Crepuscular rays from the top-left, floating bokeh orbs on "sweet". |
| Storm night | S06, S10 | Desaturated navy/teal, white rain streaks, 2–3 frame lightning flashes (#575–577, #835–838). |
| Night macro | S07, S08 | Deep blue bokeh, glossy specular highlights on the leaf and drops. |
| Sunset/dawn | S12 | Pink-magenta sky, lilac clouds; the character is graded warm (cream head, brown outline). |
| Dusk → night time-lapse | S17 (1528–1560) | **Animated colour grade** in ~1 s: salmon → purple → blue; stars appear. |
| Firelight | S17 (1725–1795), S19 | Warm orange key from the fire, light pool on the sand, then a grey-brown smoke haze. |
| Dark void CU | S18 | Near-black navy with an orange under-glow from below (the fire off-screen). |
| UI screens | S05, S14, S20 | Dark navy/teal backgrounds with self-lit glow graphics. |

## 3. Depth / parallax layers seen
- **Far:** sky + clouds, sea/horizon (often blurred). **Mid:** tree trunk + canopy, log pile, car, bush. **Near:** Kai,
  hanging apples, foreground grass tufts (S15), blurred foreground leaves (S07), POV hands (S19).
- Parallax is mild. Most moves read as a 2D scale/drift of a flattened plate plus a character card, except the S02
  aerial (true 3D) and S04's pull-back (the trunk rolls/rotates as one plane).

## 4. VFX catalogue
| VFX | Frames | Build hint |
|---|---|---|
| Blue sweat drop (teardrop, dark outline, white highlight) | 421+, 546, 723–763, 1150+, 1425+, 1797–1820, 1869–1949 | Sprite on the face layer; pops in 1 frame |
| Blue tear streams (two thick wavy ribbons) | 1171–1221, 1756–1822, 1869–1949 | Sprite, 2-frame wobble |
| Steam columns (white cartoon puffs rising from the head) | 1177–1221 | Particle/puff sprites, rise + scale |
| Sizzle smoke puffs (small white puffs + bubbles) | 735–763, 815–845, 1462–1477, 1516–1525 | Puff sprite sequence |
| Pink blisters (glossy balls on the head) | 815–859, 1457–1477 | Scale-pop one by one (2 f each) |
| Anger vein (red cross mark) | 908–944 | Sprite, fades 944–945 |
| Red heat fill rising in the head | 1160–1170 | Masked solid with a wavy top edge, animated up |
| Whole head red | 1171–1221 | Fill colour swap |
| Green sick tint | 67–90 | Fill colour swap |
| Frost zigzags on the forehead | ~1560–1718 | Sprite |
| Scent wisp (glowing wavy line + sparkles) | 1025–1057 | Animated stroke (trim path) + glow |
| 4-point sparkles / light motes | 1014–1034, 1098–1126, 1389–1402 | Particles |
| Raindrops + sap drops + splash ellipses | 515–610, 687–734 | Sprite drops, splat sprite |
| Lightning flash | 575–577, 835–838 | Bolt sprite + 2–3 frame exposure lift |
| X-ray scan line (glowing diagonal) | 631–653 | Masked wipe with a glow edge |
| Thermal scan line (horizontal) | 1868–1876 | Masked wipe |
| Dark toxic smoke cloud | 1764–1795 | Soft volumetric smoke (stock element / AI) over the plate |
| Cough smoke puff | 1923–1941 | Dark radial puff sprite |
| Red X pop-ons (logs) | 1644–1680 | Sprite, scale overshoot 0 → 120 → 100 % in 3 f, staggered ~2 f |
| Shake ticks (3 yellow dashes) | 1267–1293 | Shape layer, jitter |
| Radar sweep + precipitation reveal | 458–515 | Rotating line + radial wipe mask revealing coloured blobs |
| Blur ramp (vision loss) | 1836–1868 | Gaussian blur keyframes |
| Paper fly-off | 226–252 | Card with 3D rotation + motion blur |
| Zoom-through cut-away window | 760–770 | Framed rectangle scaling to full frame |
| Butterfly | 242–270 | Tiny sprite on the head |
| Crab | 905–1034 | Tiny sprite scuttling |
| Apple roll-in | 2035–2043 | Sprite translate + rotation |

## 5. Captions
- **Font look:** heavy geometric sans, Montserrat ExtraBold/Black-like (double-storey a, round o), **white #FFFFFF
  fill with a ~3–4 px black stroke** and a faint dark drop shadow. Sentence case as spoken; "red x" was typed in lowercase.
- **Size:** cap height ≈ 32–36 px on the 720 px-wide frame (≈ 4.7 % of width). Longest card "burns your eyes" ≈ 400 px wide.
- **Position:** horizontally centred, baseline at y ≈ 920. The card's centre sits at **y ≈ 900 px (70 % down the
  frame)**, the same in every shot, and it overlaps the character's chest/legs.
- **Words per card:** 1–2 (sometimes 3: "burns your eyes"). Cards change exactly on the spoken word (≈ every 0.45 s).
- **Animation:** none visible. Each card hard-cuts to the next, with no pop, scale, colour highlight or karaoke.
- Sample crop: `library/overlays_ui/01_this_tree_hates_you/caption_sample_f00400.jpg`.

## 6. In-scene text / labels
- **Radar header:** "SATELLITE · LIVE" (small teal caps, letter-spaced, #7fd8c8) over "NIGHT 1 · 9:42 PM" (white bold
  geometric sans). Bottom pill: red #e01436 rounded capsule, white "⚠ SEVERE STORM" with a yellow warning triangle.
  Map label "YOU" (white tiny caps) next to a red dot in a white ring.
- **Leaf label:** "MILKY SAP" in white bold caps with a thin white leader line.
- **Skin insert:** "INSIDE YOUR SKIN" in white bold small caps, top centre.
- **X-ray HUD:** "X-RAY" (light teal #96d9e2), "THROAT: ON FIRE" (orange #e8643c) → "GUT: INCOMING" (amber), "R" marker,
  "PATIENT: YOU / AP VIEW · 1:1" (small white), corner brackets, ruler ticks.
- **Thermal HUD:** "THERMAL" (golden #dbc87a), "LUNGS: 99°F … 451°F" (white), "● REC" (red dot + white), corner
  brackets, vertical scale bar (white→yellow→orange→magenta→purple) labelled "500°F"/"60°F", crosshair + temp tag.
- **Poster:** serif "MANCHINEEL", italic "Hippomane mancinella", red '("little apple of death")'.
- UI type looks like **Poppins / Inter SemiBold**: clean, geometric, slightly rounded.

## 7. Transitions
- **Dissolve** (3–7 frames) is the workhorse: 16 of 20 transitions. The camera keeps moving through it.
- **Match-dissolves**: drop → head (S07→S08), skeleton → crouching Kai (S14→S15), face → fire (S18→S19).
- **Camera move-through**: S01→S02 crane through the canopy edge.
- **In-shot reveal wipe**: the poster rips off (S03→S04).
- **Zoom-through**: a cut-away window opens in the splat (S08→S09).
- No hard cuts, whip pans or slides.

## 8. How each element was most likely made (hypotheses)
| Element | Likely method | Evidence |
|---|---|---|
| Backgrounds (beach, storm, sunset, bush, lagoon, log pile, final beach) | **AI image generation** in one consistent "painterly-3D cartoon" style, 9:16, then a slight camera move in a compositor | Dense, slightly inconsistent leaf detail; ink lines on painted volumes; the same tree redesigned differently between shots (S04 vs S12 vs S17 canopies differ) |
| Aerial S02 | **AI image-to-video** (e.g. Kling/Veo/Runway) from the S01 plate as the first frame | Continuous morph from cartoon to 3D, grain and mushy detail, true parallax |
| Kai body + face | **2D cut-out puppet** (After Effects with Duik/Joysticks, or Moho) with **face sprite swaps** | Faces swap as hard cuts on exact frames with consistent parts; outlines don't scale with depth; limbs are clean strokes; tweens are short (3–6 f) |
| Kai movement in some shots (S01 sit/fall, S16 waddle) | Possibly also AI image-to-video over a puppet keyframe | Smooth secondary motion and slight line wobble; less certain |
| Grades (night, sunset, firelight, smoke) | Compositor adjustment layers (Curves/Tint/Colorama) over the whole frame including Kai | Kai's head colour shifts with every mood |
| UI screens (radar, X-ray, thermal), labels, HUD counters | **Motion design in AE** (shape layers, text layers with a counter expression, masks/wipes, glow) | Crisp vector type, exact counters (99→451), rotating sweep, scan-line wipes |
| Inserts (skin cross-section, leaf, poster) | AI image or illustration as a base + AE animation (wipes, growing tendrils, blister scale) | Clean infographic look; parts animate separately (blister dome inflates, tendrils grow) |
| Captions | Auto-caption tool (CapCut / Submagic-style) or AE text with word timing | One–two-word hard cards, consistent position and stroke |
| VFX (sweat, tears, steam, smoke puffs, blisters) | 2D sprite library in AE | Identical sprites reused across shots |
