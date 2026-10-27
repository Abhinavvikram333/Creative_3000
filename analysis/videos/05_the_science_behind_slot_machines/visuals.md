# Visual analysis — 05 "The Science Behind Slot Machines"

## STYLE LOCK (reuse verbatim in every prompt)
```
Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick
uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny
mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed
semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino
lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain,
vertical 9:16.
```

## 1. Art style
- **Two layers of style that are deliberately mismatched**:
  1. *Characters* — Cyanide-&-Happiness-like simplicity: oversized round head (≈1/3 of the full body height), no ears/nose,
     faces built from 2–4 strokes, thick dark-brown outline (#351518–#421411) of constant weight, bodies are a soft
     capsule (shirt) with stick legs and noodle arms ending in blob hands. Flat fills (head #fcf6e7, shirt teal #19bda4
     with yellow leaf motifs) with *one* lighting effect: a warm orange rim/bloom from the environment on the head edge
     (very visible in S5 #425–494).
  2. *World & props* — dense, glossy, almost toy-like 3D: slot machines with chrome bevels, LED digits, marquee bulbs,
     ribbed red stool cushions, patterned carpet, coffered ceiling with spotlights. Everything carries a thin dark
     contour line (ink-outlined render) and painted texture, with real perspective, depth of field and parallax.
- The explainer props (par-sheet strip, stamp, tally counter, prize wheel) are rendered in the same outlined-3D look,
  not as flat motion graphics — the diagram lives *inside* the machine.
- Text inside the scene (machine labels, "REEL 3: EVERY STOP", "ONE CLICK SHORT") is part of the render: bold rounded
  display caps for signage (yellow on red), typewriter/monospace for the printed list, rubber-stamp distressed red caps
  for the imprint.

## 2. How each element was most likely made (hypotheses + evidence)
| Element | Most likely method | Evidence |
|---|---|---|
| Whole shots incl. characters | **AI image-to-video** (start frame + motion prompt, possibly start/end frames), one generation per shot, chained with dissolves | Faces change through soft blended in-betweens, not clean sprite swaps (#49–50, #72–76, #452–455); the stamped strip *morphs* physically into a wheel (#769–774); big words render correctly but small print is smeared/pseudo-text (REEL UNIT plate fine print, PCB labels, bill microtext, paytable mini-icons); Lenny's hand in the insert is an undefined blob (#345–390); dissolves contain ghosted double exposures typical of clip-to-clip crossfades. |
| Key frames / shot start images | **AI image** (ChatGPT image / similar) from a character reference sheet + set description | Consistent character design across very different angles (POV, dutch CU, 3/4 final turn #906–928) that a 2D rig would not give; painterly 3D environments with ink lines. |
| Camera moves | Prompted camera motion inside the AI clips (dolly/crane/pull-back), possibly guided by a 3D blockout | Parallax is physically consistent (high inlier counts 250–900), moves have natural ease-out; door hinge swing in true perspective (#529–532). |
| Counters (CREDITS 0→100, tally x01→x14, progressive LED) | Generated inside the clip *or* AE/text overlay composited on the screen face | Digits are clean and monotonic at every frame, roll mechanically with in-between frames (#698, #713) — good candidates to rebuild as code/AE overlays for control. |
| Captions | Post (CapCut/AE auto-captions) | Perfectly crisp, identical style, word-timed, sit above everything incl. dissolves. |
| X-ray wireframe | Either AI "x-ray" style frame + crossfade, or AE wireframe overlay; replicable as Blender wireframe modifier + emission | Cyan grid lines follow the cabinet's perspective while the camera moves (#781–928). |

Rebuild recommendation: generate plates/characters as images, animate with an AI video model *or* build the
machines in Blender (simple geometry + toon outline) and composite the 2D character cards and face sprites; do
counters, captions, badge pop and glints as overlays for exact timing.

## 3. Lighting moods
- **Casino warm** (S1, S2, S5, S6, S8): tungsten/amber key from above, red LED/neon spill, gold marquee bulbs, soft bloom.
- **Machine POV** (S3): darker, warm spotlights in a coffered ceiling, glass reflection, very shallow DOF foreground.
- **Insert red** (S4): saturated red cabinet with green self-illuminated slot (complementary accent).
- **Cabinet interior** (S7): monochrome amber/orange "inside the box" light, dust motes drifting, glints on paper.
- **X-ray** (S8): casino warm + cool cyan emissive grid (only cool light in the video).

## 4. Depth / parallax layers seen
- Casino row: far = ceiling, progressive LED sign, distant machines; mid = machine row; near = character + barstools +
  carpet. Strong parallax during S2's follow-move.
- POV: near = blurred reel strips + glass frame (foreground occlusion), mid = Bling + Lenny, far = ceiling/machines/
  walking extra (Beanie).
- Interior: near = paper strip/stamp/counter, mid = PCB/wires, far = back wall of the cabinet.

## 5. VFX inventory
| VFX | Frames | Look | Build |
|---|---|---|---|
| Glint sweep | #644–650, #669–677 | diagonal gold light streak passing L→R over the JACKPOT row | AE: gradient wipe / CC Light Sweep, 6–8 f |
| Badge pop | #681 | red hand-drawn circled "x1" appears on one frame | sprite cut-on, no scale |
| Stamp impact lines | #700–701, each hit | 4–6 short dark tick lines radiating from the stamp | 2-f shape layer burst |
| Counter roll | #698, #713, #722… | digit drum rolls between values | number wheel animation |
| Dust motes | S7 | soft bokeh dots drifting | particle system, low opacity |
| Dissolve ghosting | #251–254, #340–344 | double exposure with bright diagonal glass streak | 4–6 f cross-dissolve + light leak |
| X-ray wireframe | #779–928 | cyan (#40a7a7→#3fd8e8) grid on the lower cabinet | wireframe modifier/emission or AE grid |
| Motion blur | wheel spin #800–856, reels | directional blur on spinning objects | native |
| Morph | #769–774 | strip curls into wheel | AI video or AE bend/polar-coordinates morph |
No sweat drops, tears, smoke, speed lines or sparkles in this video.

## 6. Caption style
- Font: heavy rounded geometric sans (Montserrat Black / Poppins ExtraBold look), sentence case as spoken, punctuation
  kept ("short.", "Bro,").
- Colour white #f8f7f8, thick black outline (~4–5 px at 720 w) + soft dark drop shadow.
- Size: cap height ≈34–40 px on 720×1280 (≈3 % of height); centred horizontally, baseline ≈y 910 (centre ≈y 900).
- 1–2 words per card (95 cards: 78 single, 17 double), avg 0.33 s; hard cut between cards, no pop/scale animation,
  no highlight colour.
- Stays fixed through all camera moves and dissolves.

## 7. Transitions
Mostly *invisible*: one jump cut (#134), five short dissolves (4–6 f), and long camera move-throughs inside shots
(S2 walk, S4 acceptor→CREDITS, S6 dolly into the machine, S7 tilt down the list, S8 pull-out). The edit feels like one
continuous camera exploring the machine.

## 8. In-scene text (exact)
- Machine: "LUCKY 7s", "PLAY 3 CREDITS", "★ 1 LINE · $1 GAME ★", "WIN 0", "CASH OUT", "BET ONE", "MAX BET", "SPIN",
  "CREDITS", "LUCKY 7s PAYS", "777 = JACK $1,000", "$200 $100 $50 $2", "ANY", "GOLD RUSH", "DIAMOND…" (blue machine).
- Sign: "LUCKY 7s PROGRESSIVE" "$1,284,5xx.xx" (ticking).
- Acceptor: "$1 $5 $10 $20 $50 $100", "INSERT BILL FACE UP". Bill: "100", "THE UNITED STATES OF AMERICA".
- Interior: "LUCKY 7s REEL UNIT", "RNG", "HIGH VOLTAGE", "BILL VALIDATOR", "$".
- List: "LUCKY 7s · PAR SHEET · REV B", "REEL 3: EVERY STOP", "ROW STOP SYMBOL", "#1 BAR, #2 BLANK, #3 CHERRY, #4 BLANK,
  #5 BELL, #6 BLANK, #7 BAR, #8 BLANK, #9 7 JACKPOT, #10… BLANK", stamps "ONE CLICK SHORT", badge "x1", counter "x00…x14".
- Wheel: "ONE CLICK SHORT", "JACKPOT", hub "LUCKY 7s · EVERY STOP".
