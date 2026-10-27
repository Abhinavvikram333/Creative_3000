# STYLE GUIDE: the series style bible (pilot videos 1–5)

This guide is for the automation pipeline and for any human making a new Short in this style. Every rule comes from the
30 fps decode of the five pilot videos. It merges the per-video reports in `analysis/videos/<slug>/`, the character
library in `library/characters/` and the research in `system/research/`.

**Citation notation.** `V3 #77` means video 03, frame 77 (30 fps, 1-based). `V1 S17` means video 01, shot 17.

| Code | Video | Slug | Length | World |
|---|---|---|---|---|
| V1 | This Tree Hates You | `01_this_tree_hates_you` | 68.1 s / 2043 f | tropical beach |
| V2 | Your Brain's Secret Idea Zone | `02_your_brains_secret_idea_zone` | 39.1 s / 1172 f | Edison stage, lab and dream |
| V3 | Why Humans Can't Pick Random Numbers | `03_why_humans_cant_pick_random_numbers` | 47.1 s / 1413 f | 1960s Arizona desert bank |
| V4 | The Scientist's Insane Time Test | `04_the_scientists_insane_time_test` | 40.0 s / 1200 f | Texas amusement park and brain room |
| V5 | The Science Behind Slot Machines | `05_the_science_behind_slot_machines` | 30.9 s / 928 f | casino |

**Delivery format, the same in all 5 videos:** 720×1280, 9:16, 30 fps, H.264. These files are YouTube re-downloads, so
render masters at 1080×1920 and keep every measurement proportional. Pixel values in this guide are given **at 720 px
width**; multiply by 1.5 for 1080 px.

---

## 1. Series STYLE LOCK

### 1.1 Universal STYLE LOCK (paste verbatim into every image or video prompt)

```
Stylised 2.5D cartoon explainer frame, vertical 9:16: flat 2D vector-style cartoon characters with very large, near-perfectly round heads in a pale warm off-white, thick uniform dark warm-brown to near-black outlines (about 1% of frame width), no nose, no ears; minimal graphic faces in the lower half of the head (small solid dot or oval eyes, hollow ring eyes with dot pupils for fear, single short thick brow strokes, tiny line mouths, a wavy line for worry, a rounded rectangle with a grid of teeth for panic); bean/capsule-shaped torsos in solid flat colours where the clothing pattern is the identity, one distinctive hair cap or hat, thin dark noodle stick limbs ending in small ball hands, flat cel colours with at most one soft shade band; composited into a richly detailed, semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines on every prop, soft global illumination, motivated cinematic lighting, gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, no photorealism in the characters.
```

How to use it:
- Prompt order: `[STYLE LOCK]` + `[SETTING ADD-ON]` (1.2) + subject.
- For a **character-only** asset on a transparent background, replace everything after "composited into…" with
  `flat even light, transparent background`. This is the approach the character library already uses.
- For an **empty background plate**, keep the whole lock and add
  `empty set, no characters, nothing in motion, keep the lower-centre area free for a character`.

### 1.2 Per-world setting add-ons (append after the lock)

| World | Add-on text (verbatim) | Evidence |
|---|---|---|
| **Tropical beach** (V1) | `World: a deserted tropical island beach with warm sand (#e3cb96), a turquoise sea (#23bfdc–#38add7), a bright blue sky (#3e9eee–#8acdfb) with white cumulus, and a dense canopy of individually ink-outlined glossy leaves. Day is high-key. Night is a navy/indigo grade (#142460–#2e428a) with blue-violet highlights. Sunset is pink #db9492 with lilac #87639b. Firelight is orange #ba6135/#efa440 inside grey-violet smoke.` | V1 colors.md §2; V1 #400, #540, #930, #1740 |
| **1960s desert bank** (V3) | `World: retro mid-century American desert (Arizona 1960s modernism: stucco, breeze-block, terracotta, teal #3ab3a9, brass), on a warm sand/terracotta/cream base. The light moves from a pale-blue noon sky (#87b8d6) to a golden sunset gradient (violet #b07996 → pink #f9a4a7 → yellow #fddea9), with venetian-blind light stripes and god-rays through panoramic windows. Numbers live on props (dot-matrix LED #f2a33a, handwritten cheques, brass plaques).` | V3 visuals §2, colors §2; #50, #150, #790, #920 |
| **Edison lab / dream** (V2) | `World: a vintage late-1800s interior with dark green panelled walls, one bare bulb throwing a visible volumetric cone, warm wood, brass and chrome, deep falloff shadows. Lab variant: amber-monochrome Menlo Park laboratory (#190904–#efc797) with bokeh practicals and floating dust. Dream variant: teal underwater column (#397e88) with god-rays over a violet band (#362e67) and a navy-black deep zone (#040b1e); a wood-panelled elevator with a purple practical (#5f457d); a lavender "deep sleep" grade (#8690c6).` | V2 visuals §2, colors §2; #45, #660, #746, #1000 |
| **Texas amusement park** (V4) | `World: a sunny Texas amusement park with an orange steel lattice free-fall tower (#ea872a), navy banners (#203278) with white lettering, yellow/black hazard stripes, a saturated blue sky (#348cd6) with puffy clouds, and a plaza with long diagonal shadows. Interiors: a cosy cream-and-wood "brain room" with porthole windows and a rainbow rug, a mint fluorescent support-group room (#9fc1a5), and a film-noir lineup room (#583323). Finale: a dusty-rose sunset deck (#e77372 / #c05b82). Danger accent red #d64444.` | V4 visuals §2, colors §2; #1, #262, #340, #870, #1104 |
| **Casino** (V5) | `World: a warm tungsten casino with glossy red slot machines (#ad1012), chrome bevels, gold marquee bulbs (#cc965b), red LED digits (#ff2a1a) on black, patterned carpet, a coffered ceiling with spotlights, soft bloom on every light. Keep it ~65 % warm red/brown/gold; the only cool colour is the hero's teal (#19bda4) or a cyan X-ray (#40a7a7→#3fd8e8).` | V5 colors §1–2, §6; #55, #370, #840 |

Inserts and documents (posters, blueprints, flipbook pages, UI screens) each have their own sub-style. Use the §7
vocabulary for them and **do not** add the world add-on.

### 1.3 What differs between the five per-video locks

The five STYLE LOCK blocks (top of each `visuals.md`) agree on everything in 1.1. They differ only in these values:

| Property | V1 | V2 | V3 | V4 | V5 | Series rule |
|---|---|---|---|---|---|---|
| Head fill | **pale lavender-grey** `#dce0e9`, shade `#babfcf` | cream-peach `#f6e1c7`, shade `#e2c2ab` | warm off-white `#f8efe6`, shade `#e9dbd9` | warm off-white `#f3eeed` | cream-white `#fcf6e7`, warm edge `#f0c6af` | **Warm off-white `#f3eeed`–`#fcf6e7`** (4 of 5). Lavender is a V1-only variant. Never pure white. |
| Outline colour | **navy-charcoal** `#2f3d43` (night `#140916`) | dark brown `#2e1d17` | near-black brown `#2a1c1a` | `#2a2024` | dark brown `#421411` / `#3a1512` | **Warm near-black brown `#2a1c1a`–`#421411`**. V1's cool navy matches its lavender head. |
| Outline weight (720 w, MS) | 5–6 px (≈10 px in CU) | 7–8 px | ≈7 px | 6–8 px | ≈6–7 px (3 % of a 300 px CU head) | **≈7 px = 1 % of frame width**, constant in MS/WS |
| Limbs | double-outlined pale-tan noodles ≈6 px, white balls in POV | single dark strokes `#1f1917` ≈7 px | single black strokes `#1e1616` ≈7 px | black ≈5 px | outline-brown thick strokes | **Single stroke in the outline colour, 5–8 px**. Kai's filled limbs are the exception. |
| Shading | one soft shadow tone on the head | soft vertical sheen on the torso, lighter top on the head | one shade band on the lit/shade side, glossy hair stripe | ≤1 shade band | warm environment rim glow on the head edge | **One soft tone, nothing more** |
| Proportions | ≈3.4 heads | ≈4 heads | ≈4.2–4.4 heads | ≈4 heads | ≈4.3 heads | **4.0–4.3 heads**. V1 is stockier. |
| Environment light | high-key day / navy night | warm spotlight / amber | golden / sunset | bright midday | tungsten | world-specific (1.2) |

Other cross-video rules:
- **Scene grades sit on top of the characters.** The head colour shifts with the mood: blue at night, cream with a
  brown outline at sunset, grey in smoke (V1 S12/S17); blue-lavender on the DEEP SLEEP floor (V2 #983–1044); a red alarm
  multiply/overlay `#d3361f` (V4 #982–1069); a red/blue police wash (V3 #285–298). Keep character base colours neutral
  and grade in compositing. Only Kai's green sick tint (V1 #67), his red-hot head (V1 #1171) and Gil's queasy lavender
  (V4 #541–600) recolour the head fill itself.
- **Hero contrast rule.** The protagonist usually carries the scene's complementary colour: Lenny's teal in a red
  casino (V5), Kai's orange shirt against turquoise/navy (V1), Theo's navy body in a warm room (V2).
- Captions are always white with a black stroke, whatever the world (§5).

---

## 2. Character construction template

### 2.1 The shared body (every human character in V1–V5 uses it)

| Part | Rule | Evidence |
|---|---|---|
| **Height** | 4.0–4.3 head-heights: head 1.0, torso 1.3–1.6, legs 1.6–1.9 (they overlap the torso bottom). Extras and small characters go down to ≈2 heads. | Rico 4.2, Marge 4.2, Dale 4.4, Theo ≈4, Dex/Klaus ≈4 (V4 visuals §1), Lenny 4.3; Kai 3.4 (V1 f00400: head 150, torso 150, shorts 40, legs 170 px) |
| **Head** | A perfect circle, or slightly egg-shaped (Kai a little wider at the top; Lenny 1.05:1). It is **wider than the torso**: torso width ≈0.85–0.9 head (Rico, Theo); head ≈1.15× torso (Kai). Sizes: MS head ≈20–25 % of frame width; CU 60–70 %; standing ≈¼ of body height, seated ≈⅓. | Kai `character.md`; V1 S1 "head ≈ 25 % frame width"; Lenny consistency notes |
| **Outline** | Uniform, no taper, the same weight on head, hair, torso and clothing; ≈1 % of frame width (7 px at 720) ≈ 3–5 % of the head diameter in MS. In CU it grows **less than proportionally** (Kai 5–6 → ≈10 px). At tiny scale it does **not** thin out (Rico in V3 S4/S6). | V2 #45; V3 visuals §7; Rico consistency notes |
| **Face placement** | Features sit in the **lower half** of the head: eye line at ≈50–60 % of head height from the top, mouth at ≈68–75 %. Eye spacing ≈0.30–0.35 head width. In 3/4 views the face slides sideways on the fixed circle; in back views there is no face (Dex V4 #857–967, Noggin V4 #252+). | Theo "face in lower 55 %"; Rico "lower 60 %"; Lenny eye spacing 0.35 |
| **Eyes** | Default: small solid dots/ovals (≈0.05–0.08 head diameter). Fear: hollow **ring eyes** (white disc, thick outline, dot pupil) ≈0.2 head diameter. Other shapes in §3. No eye whites otherwise. | all emotion libraries |
| **Brows** | Single short thick tapered strokes floating above the eyes. **They carry most of the acting.** Some characters drop them in calm faces (Dex, Lenny content). | Kai, Rico, Theo notes |
| **Mouth** | Tiny: dash, small curve, side smirk, "~" wavy line, small "o", black open shape with 4–6 white square teeth (grin), or a rounded rectangle with a teeth grid (gritted). | §3.1 |
| **No** nose, ears, cheeks or fingers | Blush and stubble dots are the only cheek marks (Kai E16; Bling's stubble dots `#77402a`). | all character sheets |
| **Hair / headwear** | A **separate cap shape** over the top 35–50 % of the head. It is the **main identity marker** (table 2.3), usually has a centre-part line and 2–4 strand lines, and has one glossy highlight band (`#8a6a56` on brown hair). | Theo, Rico, Klaus, Lenny |
| **Torso** | Upright capsule/bean, slightly wider at the bottom. The **clothing colour and pattern are the identity**: a Hawaiian print, a mustard jacket with a striped tie, a harness with dashed stitches, a teal shirt with leaf motifs. Clothing details are drawn as lines on the capsule (lapels, pocket, placket, tie, lanyard). Patterns stay small and sparse and are fixed in torso space. | Kai, Rico, Dex, Lenny consistency notes |
| **Limbs** | Noodle strokes in the outline colour, 5–8 px at 720 w, with no clothing on them. They bend as simple angles or soft curves; legs are long and straight. | Theo, Rico, Dex |
| **Hands** | Ball/blob ends ≈0.15–0.18 head diameter, black or outline colour. Held objects stick out of the ball (Rico's pen). | Rico consistency notes |
| **Feet / shoes** | Usually just stick ends or tiny forward hooks; no shoes. Footwear only as an identity gag: Kai's yellow-soled flip-flops (`#e0c050`). | Rico, Dex, Kai |
| **Contact shadow** | A soft dark ellipse under the feet, or a soft grey blob on sand. Cast shadows are rarely lit. Exception: long diagonal 3D shadows on the V4 plaza (#746–856). | V1 #400, #2040; V4 visuals §1 |

### 2.2 Checklist for designing a NEW character in-style

1. Start from the body template (2.1) at 4.2 heads. **Do not** change the head shape, outline weight or limb style.
2. Pick **one** silhouette-level identity marker for the head: a hair-cap shape (bowl, mop, bun, side fringe, bald with
   tufts) or headwear (backwards cap, police cap, beanie, cowboy hat). It must read at 60 px head size (V5 Beanie).
3. Pick **one** torso identity: a solid colour plus at most one pattern or one accessory (tie, lanyard, chain, harness,
   lab coat). Give the protagonist the complementary colour of the world (1.3).
4. Optional third marker, used sparingly: glasses (Marge, Klaus, Deb, Hank), moustache (Klaus), stubble dots (Bling),
   a prop (Marge's magnifier, Klaus's stopwatch).
5. Head fill `#f3eeed`–`#fcf6e7`, outline `#2a2024`-family, eyes/brows/mouth in the outline colour. No pure white
   (`#ffffff`) and no pure black.
6. Default face: dot eyes plus a neutral or small smirk. Decide the personality's **resting face** (Lenny = deadpan,
   Marge = knowing smirk, Klaus = neutral with moustache only, Dale = stern). It will hold most of the runtime.
7. Build the emotion set from the master vocabulary (§3). Protagonists need ~10–24 faces; a foil needs ~3–5; extras
   need 1–2.
8. Non-human characters keep the outline, the face vocabulary, the noodle limbs and the ball hands, and get a new body
   silhouette: brain blob (Noggin), almond seed (Amy), LED digits (V4 lineup), dog (Biscuit).
9. Name the character with one short, punchy name (Kai, Rico, Dex, Lenny, Bling). The narrator never says it; it is a
   production label only.
10. Validate against the master as in `chatgpt_image_prompting_2026.md` §5.6: head diameter ±2 %, outline colour,
    torso palette.

### 2.3 Every character found in the pilot

| Name | Video | Role | Identity markers (head / torso / extra) | Faces in library |
|---|---|---|---|---|
| **Kai** | V1 | sole protagonist, "you" | lavender head; 2–3 curly sprouts / orange `#e05f13` Hawaiian shirt with cream hibiscus, navy shorts / yellow flip-flops | 24 (E01–E24) |
| **Theo** | V2 | demonstrator, "you" | brown bowl cut `#694532` with centre part / plain navy pill body `#3a5080` / X-ray variant | 21 |
| **Edison** | V2 | authority cameo (Thomas Edison) | pale grey-beige swept cap `#c9bba8` / black suit, white shirt V, bow tie / same template as Theo, no beard | 4 |
| **Rico** | V3 | culprit (embezzling clerk) | dark-brown glossy bowl, centre part / mustard jacket `#d9a23f`, red-brown striped tie, blue lanyard clip / orange jumpsuit, cuffs | 21 |
| **Marge** | V3 | expert foil (auditor) | auburn top bun with red pencil / purple suit `#814eab`, lilac blouse / round glasses, gold magnifier | 5 |
| **Officer Dale** | V3 | deadpan escort | navy police cap with gold star / navy uniform, gold badge / very long legs | 2 |
| **Nina** | V3 | extra (bank teller) | brown top bun / teal uniform `#67b7ac` | 2 |
| **Dr. Klaus** | V4 | mad scientist | black bowl cut, big round glasses, toothbrush moustache, usually **no mouth** / long white lab coat, pens / stopwatch, clipboard | 3 |
| **Dex** | V4 | test subject, "you" | **backwards** red cap `#d64444` (brown mop under it) / orange harness `#dd7c21` with dashed stitches, grey buckles / CHRONO-2 on the left wrist | 11 |
| **Noggin** | V4 | the brain (artist) | pink brain blob `#f2c0c6`, green visor + pencil / sits on a stool / non-human | 5 |
| **Amy** | V4 | the amygdala | almond/seed body `#be8661` with wood-grain lines / tiny / non-human | 3 |
| **Elmer** | V4 | volunteer | bald with white side tufts / green harness, orange straps | 4 |
| **Gil** | V4 | volunteer | dark side-swept fringe / purple T-shirt, orange harness | 4 |
| **Tad** | V4 | volunteer (show-off) | black bowl with straight fringe / teal harness | 3 |
| **Gus, Carl, Deb, Ray, Mo** | V4 | support-group extras | name tags; neck brace (Gus), head bandage (Carl), grey bun and glasses (Deb), blond (Ray), beard, crutch and leg cast (Mo) | 0–1 |
| **Cooper, Hank** | V4 | bored BBQ friends | orange-brown hair, salmon shirt, red cup (Cooper) / straw cowboy hat, glasses, plaid (Hank) | 0 |
| **Biscuit** | V4 | dog cameo | brown dog `#af7a53`, pointy ears, ring eyes | 0 |
| (pigeon, "digit gang") | V4 | gag cameos | grey pigeon with purple head; LED-digit suspects `#4b1e20` with red dots | — |
| **Lenny** | V5 | gambler, "you" | messy dark clumped hair / teal shirt `#19bda4` with yellow leaf motifs / red lanyard + badge | 11 |
| **Bling** | V5 | bad-advice buddy | backwards red cap with sunglasses on it, stubble dots / cream ribbed tank top, gold chain | 4 |
| **Beanie** | V5 | background walker | mustard knit beanie | 0 |

**Cast pattern.** Every video has **one "you" stand-in** (Kai, Theo, Rico, Dex, Lenny) who suffers or tries the
premise. Most add **one calm foil** who knows better (Edison, Marge, Klaus, Bling as the wrong-advice foil), plus
**deadpan or bored extras** for reaction gags (Dale, Cooper/Hank, the support group).

---

## 3. Emotion / face system

### 3.1 Face part vocabulary (shared by all characters)

| Part | Variants (canonical part ids) |
|---|---|
| **Eyes** | `dot` (solid oval) · `ring` (white disc + outline + dot pupil; pupils can sit top, side or tiny) · `halflid` (flat upper lid cutting a dot) · `heavylid` (lid over ≥½ of the pupil) · `line_closed` (flat dash) · `arc_happy` (^ ^) · `arc_down` (closed, downward curve: sleep/dread) · `chevron` (> <) · `x` · `spiral` · `wink` (one arc + one dot) · `bloodshot_ring` (pink sclera + red vein ticks) · `realistic` (one-off photographic iris, V2 #816–858) |
| **Brows** | `none` · `level` · `raised` · `worried` (tilted up in the middle) · `v_angry` (down to the centre) · `one_raised` (asymmetric) · `low_flat` (pressed down) |
| **Mouth** | `dash` · `smile_small` · `smirk_side` · `wavy` (~) · `o` · `frown` / `pout_caret` (^) · `grin_teeth` (black shape, 4–6 white teeth) · `grid_teeth` (rounded rectangle with a grid) · `open_talk` · `none` (Klaus) |
| **Extras** (separate layer) | sweat drop (pale blue `#8cb9db`/`#a7cdd7`/`#6488aa`, dark outline, white highlight; 1 drop, or 2–3 for peak panic V3 #1380) · tear streams (two thick wavy ribbons `#829aad`–`#9cc8ec`) · blush ovals `#f0a0a8` · red puffy lid patches `#d86a6a` · anger vein `#e03a2a` · steam puffs (white) · frost zigzags · cough smoke puff (dark grey) · vibration arcs "((" · head tremble (1–3 px per frame) |
| **Head fill swaps** | sick green `#9fbf9a` (V1 #67) · queasy lavender `#9c9cbb` (V4 Gil) · red-hot `#da767a` (V1 E18) · rising red heat fill with a wavy top edge (V1 #1160–1170) |

### 3.2 Master emotion vocabulary (canonical ids)

Columns: the part combo, then which videos use the face. ✔ = at least one character in that video.

| Canonical id | Eyes | Brows | Mouth | Typical extras | V1 | V2 | V3 | V4 | V5 | Narrative use |
|---|---|---|---|---|---|---|---|---|---|---|
| `neutral` | dot | level/none | dash / tiny smile | — | ✔ | ✔ | ✔ | ✔ | ✔ | default, background presence |
| `content` | dot (looking at camera) | level | smile_small | — | | | ✔ | | ✔ | false hope, calm explaining |
| `eyes_closed_smile` | arc_happy | relaxed | smile_small | blush optional | ✔ | ✔ | ✔ | | ✔ | "things look nice", savouring |
| `serene` | line_closed | level | slight smile | — | ✔ | ✔ | | | | calm, napping on purpose |
| `asleep` | arc_down | relaxed | dash / o / wavy (stirring) | — | | ✔ | | | | sleep states |
| `drowsy` | heavylid | level | dash | — | | ✔ | | | | drifting off |
| `smug` | halflid, side-glance | one_raised | smirk_side | — | ✔ | ✔ | ✔ | ✔ | ✔ | **most common**: "I've got this", knowing |
| `sly_grin` | halflid / squint | one_raised or v | grin_teeth (side) | — | | ✔ | ✔ | | ✔ | cocky, mischievous, triumphant |
| `grin` | dot | raised | grin_teeth | — | | ✔ | ✔ | | | confident, proud |
| `big_grin_closed` | arc_happy | relaxed | grin_teeth / open laugh | — | | | ✔ | ✔ | | bragging, gleeful accents |
| `manic_grin` | ring | raised | grin_teeth (wide) | — | ✔ | ✔ | ✔ | | ✔ | eager, jackpot, eureka |
| `wink` | wink | one_raised | smirk / grin | — | | ✔ | ✔ | ✔ | ✔ | foil talks to the viewer; 2-frame gag |
| `curious` | dot looking up/side | raised | smile_small / dash | — | ✔ | | | | ✔ | hopeful, "ooh apples" |
| `pondering` | pupils at the top of the eye | level | dash / o | — | | | ✔ | | | thinking, mesmerised |
| `blissful` | arc_happy / soft arches | raised | small round smile | blush | ✔ | | | | | tasting, dreamy |
| `skeptical` | halflid (+ one squint) | one_raised | dash / o / crooked | — | ✔ | ✔ | ✔ | ✔ | ✔ | "really?", doubt |
| `suspicious` | halflid, pupils pushed sideways | v_angry | o / dash | sweat optional | | | ✔ | | ✔ | distrust, side-eye |
| `determined` | halflid | v_angry | dash / o / grid_teeth | — | | ✔ | ✔ | ✔ | ✔ | following instructions, "let's crack it open" |
| `deadpan` | heavylid over dots | low_flat / none | dash | — | ✔ | ✔ | ✔ | ✔ | ✔ | **the series' comic beat** after each disaster |
| `annoyed` | halflid side-eye | one slanted down | frown / pout | vibration arcs | ✔ | ✔ | ✔ | ✔ | | "worst nap ever", grumpy |
| `angry` | narrowed | v_angry (sharp) | grid_teeth | anger vein | ✔ | | | ✔ | | "Lesson learned", frantic brain |
| `worried` | ring or dot | worried | wavy / frown | sweat drop | ✔ | | ✔ | ✔ | | "Big mistake", dread building |
| `shocked` | ring | raised | o / wavy | sweat drop, tremble | ✔ | ✔ | ✔ | ✔ | | the "kill/caught/human" hit word |
| `terrified` | ring (tiny pupils) | raised / none | grid_teeth | sweat, tremble | ✔ | | ✔ | ✔ | | panic peak, falling |
| `wince` | chevron / squeezed lines | v or worried | grid_teeth | sweat, smoke puffs | ✔ | ✔ | | ✔ | | pain, flinch, strain |
| `eyes_shut_dread` | arc_down / line_closed | worried / level | wavy / dash | — | ✔ | | | ✔ | | "right before you die", sulking |
| `crying` | chevron or bloodshot_ring | worried | wavy / grid_teeth | tear streams, red lids, steam | ✔ | | | | | peak suffering |
| `cold` | line_closed (squeezed) | tense | grid_teeth (chatter) | frost, shiver | ✔ | | | | | freezing |
| `dizzy` | spiral | none | wavy | — | | | | ✔ | | after an impact |
| `dead_x` | x | none | wavy | head tint green | ✔ | | | | | "it can kill you" |
| `sick` | dot | level | dash / wavy | head fill swap | ✔ | | | ✔ | | nausea |
| `relieved` | one arc + one halflid, or closed curves | relaxed | smile / open grin | sweat stays on | ✔ | ✔ | ✔ | | | "phew" right before the next blow |
| `suppressed_laugh` | squeezed arc_happy | raised | wavy, pressed | — | | | ✔ | | | straight man cracking |
| `talk_open` | halflid | raised | open_talk | — | | | | | ✔ | the only lip flap (2-state) |
| `blink` | line_closed | as held face | as held face | — | ✔ | ✔ | ✔ | ✔ | ✔ | 1–3 f inside holds |
| *specials* | `hypnagogic_stare` (realistic iris), `xray_*` (translucent head, no face) | | | | | ✔ | | | | keyword "breaks" |

### 3.3 Mapping: per-character ids → canonical ids

| Canonical | Kai (V1) | Theo / Edison (V2) | Rico / Marge / Dale / Nina (V3) | Klaus / Dex / Noggin / Amy / Elmer / Gil / Tad (V4) | Lenny / Bling (V5) |
|---|---|---|---|---|---|
| `neutral` | — | Theo `neutral` | Nina `neutral` | Klaus `neutral` (moustache, no mouth); Elmer neutral (bg) | Bling `neutral` |
| `content` | — | — | Marge `pleasant_smile` | — | Lenny `content` |
| `eyes_closed_smile` | E02 content_smile | Theo `happy`, Edison `happy` | Rico `content_eyes_closed`, Marge `eyes_closed_smug` | — | Lenny `eyes_closed_smile` |
| `serene` | E01 calm | Edison `serene` | — | — | — |
| `asleep` | — | Theo `asleep`, `asleep_o_mouth`, `stirring` | — | — | — |
| `drowsy` | — | Theo `drowsy` | — | — | — |
| `smug` | E04 smug | Theo `smug` | Rico `smug_halflid`, Marge `knowing_smirk`, Nina `smug_halflid` | Klaus `smug_halflid`, Dex `smug`, Dex `smug_browraise` | Lenny `smirk`, Bling `smug_smirk` |
| `sly_grin` | — | Theo `sly_grin` | Rico `cocky_grin`, Rico `mischievous_grin` (V brows) | — | Lenny `smug_grin` |
| `grin` | — | Theo `proud` | Rico `confident_grin` | — | — |
| `big_grin_closed` | — | — | Rico `gleeful_eyes_closed` | Dex `big_grin`, Tad `big_grin`, Elmer `happy_closed`, Gil `laughing` | — |
| `manic_grin` | E15 eager_grin | Theo `excited` | Rico `manic_grin` | — | Lenny `manic_grin` |
| `wink` | — | Edison `wink`, Edison `sly_peek` (variant) | Marge `wink` | Klaus `wink` | Bling `wink_grin` |
| `curious` | E05 curious | — | — | — | Lenny `curious_brow` |
| `pondering` | — | — | Marge `pondering_eyesup`, Rico `mesmerised_lookup` | — | — |
| `blissful` | E14 dreamy_bliss, E16 blissful_blush | — | — | — | — |
| `skeptical` | E17 suspicious | Theo `skeptical` | — | Dex `skeptical`, Elmer `skeptical_halflid`, Gil `skeptical_squint` | Lenny `skeptical` |
| `suspicious` | — | — | Rico `nervous_sideglance` | — | Lenny `suspicious` |
| `determined` | — | Theo `determined` | Rico `focused` | Noggin `angry_determined` | Lenny `determined` |
| `deadpan` | E07 unimpressed | Theo `deadpan` | Dale `stern` | Dex `deadpan`, Noggin `bored_halflid` | Lenny `deadpan` |
| `annoyed` | E11 annoyed_scowl | Theo `annoyed` | Rico `annoyed`, Rico `sulky` | Tad `annoyed` | — |
| `angry` | E12 angry_vein | — | — | (Noggin `angry_determined` borderline) | — |
| `worried` | E06 worried (+ heat-fill variant) | — | Rico `worried_frown`, `uneasy_sweat`, `doubtful` | Dex `worried`, Dex `frown`, Amy `worried`, Elmer `worried_sweat`, Elmer/Gil `worried_frown` | — |
| `shocked` | E09 alarmed_o | Theo `alarmed`, `alarmed_sweat` | Rico `surprised`, `surprised_sweat`, `panic_wavy_sweat`, `panic_multi_sweat` | Dex `surprised_o`, Noggin `startled` | — |
| `terrified` | E08 shocked_gritted | — | Rico `gritted_panic` | Dex `terrified`, Amy `panic`, `panic_sweat`, Noggin `frantic` | — |
| `wince` | E10 wince, E19 strain_grimace | Theo `flinch` | — | Noggin `strain_squint` | — |
| `eyes_shut_dread` | E13 sulky_closed | — | — | Dex `dread_eyesshut` | — |
| `crying` | E18 crying_hot_red, E21 tear_wince, E22 squeeze_cry, E23 bloodshot_cry, E24 cough_cry | — | — | — | — |
| `cold` | E20 cold_chatter | — | — | — | — |
| `dizzy` | — | — | — | Dex `dizzy`, Tad `dizzy` | — |
| `dead_x` | E03 dead_x | — | — | — | — |
| `sick` | (E03 green tint) | — | — | Gil `queasy` | — |
| `relieved` | E01 relieved variant, E02 "phew" variant | Theo `relieved` | Rico `relieved_sweat` | — | — |
| `suppressed_laugh` | — | — | Dale `suppressed_laugh` | — | — |
| `talk_open` | — | — | — | — | Bling `talk_grin` |
| `blink` | `~` in-betweens | transition faces | Rico blinks | Dex in-betweens | Lenny `blink` |
| specials | — | Theo `hypnagogic_stare`, `xray_asleep`, `xray_alarmed` | — | — | — |

Cameo faces (V4, no crops): Deb `shocked` ("o" mouth), Cooper `content` → `skeptical` → `deadpan` (wide ring-eye bored
stare), Hank `deadpan` → `skeptical`, Carl `drowsy` → `skeptical`.

**Minimum set for a new protagonist** (covers ≈90 % of the holds in the pilot): `neutral`, `eyes_closed_smile`,
`smug`, `sly_grin`, `manic_grin`, `skeptical`, `deadpan`, `annoyed`, `worried`, `shocked`, `terrified`, `wince`,
`relieved`, `blink`. For a foil: `neutral`/resting face, `smug`, `wink`, `eyes_closed_smile`, `pondering`.

### 3.4 Timing statistics

Pooled from the expression timelines in every `emotions.md` (236 holds, 14 characters):

| Metric | Value | Evidence |
|---|---|---|
| Expression hold, pooled | **median 17 f (0.57 s), mean 23 f (0.76 s)**, IQR 5–33 f | all timelines |
| Hold by role | protagonists: Kai median 18 f, Rico 13 f (mean 17), Theo 9 f (mean 21); foils/straight men: Marge mean 31 f, Klaus median 30 f, Dale median 41 f; frantic brain Noggin median 6 f (2–7 f, "brain speeds up") | per-character tables |
| Long holds | 35–60 f on explanation lines (Rico 53 f V3 #628–680, Kai 54 f V1 #1072–1125); 90–160 f only for sleep/X-ray states (Theo 163 f V2 #372–534) | |
| Comic flash faces | **2 f** holds as punctuation: Dex `smug_browraise` V4 #190–191, Dex `skeptical` V4 #494–495, Klaus `wink` V4 #494–495 / #508–509, Rico `gleeful_eyes_closed` V3 #499–500. About 20 % of all holds are ≤3 f. | |
| Blink | **1–3 f, typically 2 f** (Lenny always exactly 2 f: V5 #100–101, #146–147, #233–234; Rico 1–3 f V3 #75, #184–186, #268, #519; Kai 2–3 f V1 #1174–1176, #1876–1877). About 1 blink per 2–4 s of face time, never on a stressed word. | |
| Transition faces | 42 found, median 1 f, max 6 f: half-lid, squint, one eye closed or a "slit" face between two very different emotions (Theo V2 #198, #578, #814–815; Kai `~` frames, e.g. V1 #63, #421–423, #1642–1644) | Kai, Theo, Dex tables |
| In-betweens / tweens | **V1–V4: none.** Faces hard-swap on one frame (V2 #81, #94, #405; V3 "no tweening"; V4 0–1 in-between frame). **V5: 1–2 soft blended frames** that read as a morph (#49–50, #72–76, #452–455). Body tweens exist (3–6 f) but faces do not tween. | V5 visuals §2 |
| Swap rate | one new face every **0.5–1.0 s** while a character is "acting", about one per 1–2 caption words (Kai ≈90 entries in ≈53 s of face time) | V1 script §3 |
| Alignment to speech | Swaps land **on the first frame of the stressed word** (or ≤2 f before it): "kill" V1 #64, "red x" #358, "skin" #734, "burning" #1171, "Unfortunately" #1645; "a genius" V2 #94; "human" V3 #77, "caught" #283, "different" #527, "always" #1379; "die." V4 #154; "jackpot symbols" V5 #49. Extras (sweat, tears, steam) pop **1–3 f before or together with** the face (V1 #421, #1150). | |
| Arc inside a line | The usual micro-sequence is **calm/smug → hit word → shocked/worried → deadpan button**. Kai uses `deadpan` 8 times (V1 E07), Lenny ends on it (V5 #889–928), Dex goes deadpan mid-fall (V4 #154). | |
| Lip sync | **None.** The narrator is off-screen. The only talking is Bling's 2-state lip flap (`talk_open` ↔ `smug`, irregular 2–9 f holds, V5 #287–334). | |

### 3.5 Recommended swappable-face sprite spec

The source shows **whole-face swaps**: the brows, glasses and moustache change with the face drawing (Rico, Marge,
Lenny notes), while sweat, tears and steam behave as separate layers that pop on independently (V1 #421, V3 #204). Build
it the same way.

| Item | Spec |
|---|---|
| **Layer stack** (bottom → top) | `body` (torso + limbs, posed) → `head_base` (disc fill, one shade band, outline) → **`face`** (one whole-face sprite: eyes + brows + mouth + any glasses/moustache/stubble/blush that belong to that emotion) → `hair` (cap/hat, so fringes overlap brows correctly) → `fx` (sweat/tears/steam/vein/frost, 0–n sprites) → `tint` (head-fill swap or a multiply mask clipped to the disc) |
| **Whole face vs parts** | **Whole-face sprites are the deliverable** (one PNG per canonical id). They match the source, avoid misaligned AI-generated parts and swap in one frame. For code pipelines a procedural parts renderer (eyes/brows/mouth ids → SVG, as in `face_animation_github.md` §6) may generate the same ids. |
| **Canvas** | 1024×1024 RGBA PNG, straight alpha, transparent. **Every sprite of a character uses the identical canvas.** |
| **Head geometry on the canvas** | Head disc diameter **D = 600 px**, centred at **(512, 512)**. That leaves a ~200 px margin for steam above, tears below and a sweat drop beside the rim. Eye line at y ≈ 512 + 0.05 D, mouth at y ≈ 512 + 0.22 D. A 600 px disc covers a 1080-wide CU head (≈650–750 px) at near 1:1 and MS heads at 2× oversampling. |
| **Anchor point** | The head disc centre, (0.5, 0.5) normalised. It is parented to the head bone or card. 3/4 views: shift the face layer by ±0.15 D horizontally (the face slides on the fixed circle). Back view: hide the face. |
| **Outline** | The face sprite has no head outline (the outline is on `head_base`). Face strokes use the character's outline colour at ≈0.03 D (18 px at D = 600). |
| **Generation** | Edit from the frozen `head_neutral.png` for every emotion, never chained (`chatgpt_image_prompting_2026.md` §5). Post-align: fit the circle and scale/translate to D and centre, then mask to the disc interior so `head_base` stays pixel-identical. |
| **Naming** | `library/characters/<Name>/emotions/sprites/<name>__<canonical_id>[--<variant>].png`, e.g. `rico__terrified.png`, `rico__shocked--sweat3.png`, `kai__crying--bloodshot.png`, `rico__blink.png`, `rico__squint.png` (transition face). FX: `library/overlays_ui/fx/fx_<name>.png` (e.g. `fx_sweat_drop.png`, `fx_tear_streams.png`, `fx_anger_vein.png`), on the same 1024 canvas so they share the anchor. |
| **Manifest** | `library/characters/<Name>/emotions/faces.json`: `{canvas:[1024,1024], disc_center:[512,512], disc_d:600, outline_hex, resting_face, sprites:{canonical_id:{file, source_ids:[...], default_fx:[...]}}}`. `source_ids` keep the mapping in 3.3. |
| **Timeline data** | Per shot: `[{"f0":64,"f1":90,"face":"dead_x","fx":["tint_green"]}]`. Hold keys only, no interpolation. Optional `"blend":1` adds one 50 % cross-blend frame for V5-style soft swaps. Blinks 2 f inside any hold > 60 f. Transition face (1 f) between two holds whose eye shapes differ (e.g. `smug`→`shocked`). |

---

## 4. Poses and body animation

### 4.1 Common pose vocabulary (cross-video)

| Pose id | Description | Seen in |
|---|---|---|
| `stand_neutral` | upright, arms down or hands together low | Kai P07, Rico `standing_cuffed`, Dale `standing_elevator`, Dex `standing_harness`, Lenny `stand_deadpan` |
| `stand_hand_hip` / `hands_on_hips` | confident, chest out | Kai P04, P06 |
| `seated_chair_stool` | sitting upright, knees over the seat edge, legs dangling, hands in lap or holding a prop | Theo/Edison `seated_holding_balls`, Lenny `seated_badge`, Marge `seated_coin_flip`, Dex `seated_flipbook`, Bling `seated_behind`, Noggin |
| `sit_ground` | on the ground, legs out, leaning back | Kai P02, P10, P19, P24 |
| `walk` | 3/4 walk, arms counter-swing | Kai P01, P21, Lenny `walk_cup`, Marge `walk_place_cheque`, Tad `walk_dizzy`, Dale escort |
| `run` | run cycle while translating | Kai P08 |
| `reach_press` | one stick arm extends to a prop or button | Kai P05, P16; Theo `seated_reach_side`; Rico `press_button_reach`; Dale `arm_reach_panel`; Lenny `stand_reach` |
| `hold_up_prop` | prop raised to camera at chest or head height | Kai P14, Theo `arm_raised_notepad`, Klaus `stopwatch`, `clipboard`, Marge `raise_magnifier` |
| `writing_scribble` | ball hand with a pen on paper or a wall | Rico `desk_writing`, `car_writing_cheque`, `jail_writing_wall`; Noggin; Klaus clipboard |
| `arms_out_brag` | arms wide, "it took THIS long" | Elmer, Tad |
| `shrug` | chest-up, palms up | Elmer, Gil |
| `crouch` | knees bent, low | Kai P09, P15, P22; Rico `crouch_press` |
| `lean_in` | torso tilted toward someone or a machine | Bling `lean_in_talk`, Lenny `lean_tilt`, `cu_lean_glare` |
| `fall_tumble` | whole-body rotation, limbs flung | Kai P03, Dex `pushed_off_edge`, `freefall_spread`, `tumble_horizontal`, `landed_on_net` |
| `back_view` | blank back of the head, no face | Dex `back_view`, Noggin `back_view_drawing`, Dale `back_view_front_seat` |
| `pov_hands` | first-person hands or ball hands in the foreground | Kai S19, Theo `pov_hands_balls`, Lenny `hand_insert_bill` |
| `arm_only` | only a sleeve and stick arm entering from the frame edge | Marge `arm_magnifier`, `arm_pencil_point`, Dale `arm_reach_panel` |
| gag poses | `point_back_angry`, `hold_belly`, `float_on_scent`, `waddle`, `arms_crossed_shiver`, `slam_button`, `push`, `hands_behind_back` | Kai P11–P20, Amy, Klaus, Marge |

### 4.2 Motion rules

| Aspect | Rule | Evidence |
|---|---|---|
| **Acting split** | The **face does the acting, the body mostly holds.** Many poses are "static body, face swaps only". | Edison V2 S5; Dex V4 #443–560; Lenny V5 #200–250; Dale V3 #873–954 |
| **Idle** | 1–2 px vertical bob or "breathing" while holding. The continuous camera push (§7.5) supplies most of the life. | Theo "≈1 px"; Rico 1–2 px; Dex 1–2 px; Kai P07 "tiny breathing bob" |
| **Tremble / shiver** | 1–3 px random offset per frame (AE `wiggle(15,2)`) during panic or cold | V3 #77–105, #1197–1222; V1 #1558–1587 |
| **Limb moves** | Limbs are rigid strokes rotating from the shoulder. Reach or raise in **3–6 f**, then hold (Kai P05 4 f; Dale 3 f; Klaus push 4–6 f). Slow reaches ≈15 f (Theo #215–238). Shrug-up 2 f (Elmer/Gil #913). Snap jolt 1 f (Theo `xray_front_upright` #537). | poses.md |
| **Repetitive actions** | Scribble = 2-frame alternation (Rico #184–252, Noggin 2–3 f per stroke); button presses 1 per 2 f (V3 #475–489); flipbook ≈1 page per frame (V4 #1080–1200) | |
| **Body tweens** | Pose changes use **3–6 f tweens** (Kai sit-down V1 #19–25, drops ≈40 px) or are swapped under a dissolve; sometimes a jump-cut pose pop (V5 #134) | Kai poses.md header |
| **Whole-sprite rotations** | Falls are a rigid rotation of the whole figure: Kai tip-over ≈80° in 4–6 f (V1 #73); Dex 0→90° over 30 f, then a −55° roll over the shot (V4 #1–213). Squash 10 % on landing (V4 #727–736). | |
| **Walk cycles** | Simple and on twos: Kai "2-frame-ish on twos" with head bob (V1 #1–20), run on twos translating ≈300 px; Marge 4-frame steps (V3 #1093–1150); Tad 12-frame cycle with sway (V4 #757–786); Lenny "subtle walk bob" (V5 #148–200) | |
| **Props** | Props move on smooth arcs and carry the physics: the ball drop ≈6 f with gravity (V2), a plate glides ≈11 f per arc (V2), the cap flies off on its own arc (V4 #1–30), an apple rolls in (V1 #2035–2043) | |
| **Turnarounds** | Characters never show true 3D rotation. During orbits they switch to a drawn back or 3/4 view, often hidden under an effect (Theo's orbit drawing swap under the scan line V2 #555–564; brain-room orbit V4 #229–289; Noggin's face fades as he turns V4 #252). | V4 visuals §1 |

### 4.3 AI-video-like motion vs puppet motion: evidence

| Puppet / 2.5D-compositing signature | AI image-to-video signature |
|---|---|
| Faces swap on exact frames with 0 in-betweens, with consistent parts (V1, V2 #81/#94/#405, V3, V4 #129) | Faces change through 1–2 soft blended frames (V5 #49–50, #72–76, #452–455) |
| Outline weight constant at every scale (V1 visuals §1; V3 Rico at tiny scale S4/S6) | "Head outline weight varies" and shirt-flower placement drifts between shots (toolchain E9). Contradicts Kai's sheet, which says the flowers are fixed. |
| Rigid limb rotations, 3–6 f tweens, 1–2 px bobs, 2-frame scribbles (poses.md everywhere) | Smooth organic sit-down and fall with in-betweens, head detaching (V1 #1–90, toolchain E3) |
| Back views drawn, not modelled; swap hidden under FX (V2 #555–564) | Noggin's face **fades out** while turning (V4 #252); Lenny's head turn with the hair mass swinging (V5 #784–928) |
| VFX sprites identical across shots (sweat drops, red X pop with 0→120→100 % overshoot in 3 f, V1 #1644–1680) | Smoke puffs "boil"/morph every frame (V1 #1200–1223); line boil (V4 #1180–1182); motion smear (V4 #719–726) |
| Character cast shadow is a soft blob, not lit (V1 #400) | Long diagonal lit 3D shadows on the plaza (V4 #746–856) |
| Grades applied over the character like an adjustment layer (V1 S12/S17) | Morphing objects: the strip curls into a wheel (V5 #769–774); the aerial morphs from cartoon to 3D (V1 #73–184); LED digits garble between glyphs (V4 #528–568) |

**Practical rule for replication:** dialogue, reaction, explanation and insert shots get the deterministic puppet
treatment (cards + face swaps + push-in). Falls, crane reveals, orbits through crowded sets and morphs may use I2V
with start and end frames (§8).

---

## 5. Captions (exact spec)

### 5.1 Measured per video

| | V1 | V2 | V3 | V4 | V5 |
|---|---|---|---|---|---|
| Cards / words | ≈147 / 235 | 114 / 145 | ≈120 / 164 | 117 / 143 | 95 / 112 |
| Words per card | 1–3 (avg 1.6) | 1–3 (mostly 1) | 1–3 (mostly 1–2) | 1: 80 %, 2: 17 %, 3: 3 % | 1: 82 %, 2: 18 % |
| Card hold | ≈0.45 s | avg 10.3 f | median ≈9 f | mean 10.3 f, median 10, range 2–28 | avg 9.8 f, range 2–25 |
| Cap height (720 w) | 32–36 px | 26–30 px | ≈38 px | ≈45 px | 34–40 px |
| Centre y (of 1280) | ≈900 | ≈900 (baseline) | ≈900 | 900–905 | ≈900 |
| Fill / stroke | `#FFFFFF` / black 3–4 px | `#f9fafa` / `#04050c` ≈4 px | `#ffffff` / `#0f0505` ≈4 px | `#f1ebe6` / `#0f0909` 4–5 px | `#f8f7f8` / `#000000` 4–5 px |
| Case | sentence case ("red x" lower-case) | lower-case as spoken, punctuation kept | lower-case as spoken | sentence case, punctuation | sentence case, punctuation |

### 5.2 Series caption spec

| Property | Value |
|---|---|
| **Font look** | Heavy geometric sans with a double-storey "a" and round "o" (Montserrat ExtraBold/Black class). |
| **Free fonts** | 1st: **Montserrat Black (900)**, Google Fonts, OFL; the closest match (V1, V3, V5 notes). 2nd: **Poppins ExtraBold (800)** (V2, V4). Rounder fallback: **Nunito Black**. |
| **Size** | Cap height ≈ **36 px at 720 w (5 % of frame width)**, i.e. font size ≈ **52 px @720 / 78 px @1080**. Allowed range 26–45 px cap height. One line, never wrapped; the longest observed card is ≈400 px wide (55 % of width, V1 "burns your eyes"). |
| **Position** | Centred horizontally. Card centre at **y = 70 % of frame height** (900 px @1280, 1350 px @1920). Screen-space: fixed through every camera move, dissolve and shot, over the character's chest or legs. |
| **Fill** | White `#FFFFFF` (a measured `#f1ebe6`–`#f9fafa` is compression). |
| **Stroke** | Black `#000000`, outside stroke **4 px @720 (6 px @1080) ≈ 8 % of font size**, round joins |
| **Shadow** | Soft dark drop shadow: offset ≈3 px down @720, blur ≈4 px, black 50 % |
| **Words per card** | 1 word by default; group 2–3 only when a function word is short or bound to the next word ("a tower", "to time", "than it", "really did.", "in the middle"). Pooled ≈1.35 words per card. |
| **Timing** | The card appears on the first frame of its first word and stays until the next card. **No gaps** (V4: a card on screen from f1 to f1200). Holds 2–28 f, mean ≈10 f (0.33 s). Derive from word timestamps (WhisperX / forced alignment). |
| **Text** | Exactly as spoken, sentence case, punctuation kept on the word it follows ("Apparently,", "die.", "Bro,"). Numbers as an auto-captioner writes them: digits for multi-digit numbers ("19", "100"), words for small ones when spoken that way ("two", "ten"; V3 visuals §5). Fix ASR errors to the spoken script (V1 "When night falls,"; V2 "hypnagogia"). |
| **Animation** | **None**: a hard cut between cards. No pop, scale, karaoke or colour highlight word. Always the top layer, above VFX and dissolves. |
| **Never** | emoji, coloured keywords, boxes or pills behind the text, title cards, logos, an end card or a CTA |

---

## 6. Pacing and script structure

### 6.1 Measured pacing

| Metric | V1 | V2 | V3 | V4 | V5 | Series target |
|---|---|---|---|---|---|---|
| Duration | 68.1 s | 39.1 s | 47.1 s | 40.0 s | 30.9 s | **40–60 s** (30–70 OK) |
| Words | 235 | 145 | 164 | 143 | 112 | 145–215 |
| Words / s | 3.45 (3.5 in speech) | 3.71 | 3.48 | 3.58 | 3.62 | **3.55 (≈215 wpm)** |
| Hook (first sentence) | 2.7 s, 11 words | 3.9 s, 14 w | 3.5 s, 16 w | 5.3 s, 19 w | 4.4 s, 15 w | **3–5 s, 11–19 words** |
| First visual gag / face hit | 2.1 s (#64) | 2.7 s (#81) | 2.6 s (#77) | 0 s (push at f1) | 1.6 s (#49) | **≤ 2.7 s** |
| Shots | 21 | 9 | 12 | 10 | 8 | 1 per 3.5–4 s |
| Avg / median shot | 3.24 / 2.47 s | 4.34 / 3.97 s | 3.92 / 3.25 s | 4.0 / 3.68 s | 3.87 / 3.45 s | **3.75 s pooled** (60 shots / 225 s) |
| Visual event rate | face change every 0.6–0.7 s | new action every 0.6–1.0 s | location every 3–4 s, face every 0.5–1.5 s | camera never static > 1.1 s | event every 0.5–1 s | **something changes every ≤1 s** |
| Ending | payoff + button gag, no end card | callback to opening set | hook line repeated + magnifier rhyme, hard stop | **true loop** (f1200 = f1) | deadpan hold, no CTA | **callback or loop, no CTA** |

### 6.2 Recurring narrative devices

| Device | Where |
|---|---|
| **Second-person "you"** as the protagonist; the on-screen character *is* "you" | V1, V2, V5 throughout; V3 hook/close; V4 explanation |
| **Conditional or shock hook**: "If you ever…" / "If you fall asleep…" / "A scientist dropped people…" / "You just watched…" | 3 of 5 open with "If you" |
| **"You see,"** to pivot into the mechanism | V1 #610, V2 #117, V4 #957 |
| **"But…"** turn / **"So,"** consequence connector; the last line starts with "So" | all 5 (V1 "So, if you're ever…", V2 "So you wake up…", V3 "So, no matter…", V4 "So when you replay…", V5 "So, every time…") |
| **A real science fact** behind an absurd story | manchineel, hypnagogia + Edison, Benford's law, Eagleman free-fall study, slot par sheets |
| **Escalation ladder with a deadpan button** after each step | V1 (4 misfortunes, deadpan each time), V5 (3 near misses) |
| **Twist or authority reveal** at 50–60 % | Edison (V2 #617), "same tree" (V1 #1635), "not one could tell" (V4 #857), "his checks began with 7, 8, 9" (V3 #1064), "crack it open" (V5 #495) |
| **Running visual motif** that pays off at the end | red X + apple (V1), steel balls (V2), magnifier (V3), cap/pigeon/flipbook (V4), reel 3 one click short ×4 (V5) |
| **Last line echoes the hook** (loopable) | V3 "a way to tell" ×2; V4 page = f1; V1 beach without the tree |
| No intro, title card, logo, outro or CTA | all 5 |

### 6.3 Reusable beat template (40–70 s Short)

Target 3.55 words/s. Times are for a 50 s video (≈180 words); scale proportionally.

| # | Beat | Time (50 s) | % | Words | Narration pattern | Visual strategy | Face behaviour |
|---|---|---|---|---|---|---|---|
| 1 | **Hook** | 0–4 s | 8 % | 12–18 | "If you ever [do X], [shocking consequence]." / "You just [experienced X]…" | Open **mid-action** on the most extreme literal image, in one continuous move (reveal pull-back from an ECU, or a dive). No title. | Hit-word swap by ≤2.7 s (calm → shocked/dead/manic) |
| 2 | **Setup** | 4–11 s | 14 % | 20–30 | "Imagine / picture…", name the thing, state the stakes | Establishing reveal of the world; poster, counter or UI insert for the name and number | smug/content → worried on the warning word |
| 3 | **Turn** | 11–13 s | 4 % | 4–8 | "But how?" / "Big mistake." / "Here's the weird part." / "So, let's crack it open." | Reaction shot or push-through | `deadpan` or `skeptical` button |
| 4 | **Escalation 1 (mechanism)** | 13–22 s | 18 % | 30–35 | "You see, [mechanism]…" | **Cutaway diagram or inside view** (X-ray, cross-section, brain room, machine interior); camera pushes *through* into it | swaps on every clause |
| 5 | **Escalation 2 (consequence / evidence)** | 22–30 s | 16 % | 25–30 | "Within minutes… / People who survive… swear…" | Literal gag illustration plus an exaggeration (paint bubbling off a car; a support group) | shocked → wince → `deadpan` button |
| 6 | **Twist** | 30–37 s | 14 % | 20–25 | "But [authority/evidence] …" / "Unfortunately, …" | Recurring motif returns (red X, magnifier); a cameo or foil enters; visual pun | foil `wink`/`smug`; hero `worried` → `deadpan` |
| 7 | **Explanation payoff** | 37–45 s | 16 % | 25–30 | "So, every time… / That's because…" | Diagram-as-prop (pie wheel, histogram, flipbook, skyline) with a highlight (glint, red circle, stamp, counter) | `determined` / `pondering` / foil `smug` |
| 8 | **Punchline + loop** | 45–50 s | 10 % | 12–18 | "So, if you're ever…, maybe just [absurd advice]." / restate the hook | Return to the opening set or zoom into an object that becomes frame 1; end on a held face | final `smug`, `deadpan` or `eyes_closed_smile` hold of 1–2 s; no end card |

Longer videos (60–70 s, like V1) repeat beats 4–5 as 3–4 "misfortunes", each 6–9 s with its own deadpan button. Shorter
videos (≈30 s, like V5) merge beats 2–3 and 5–6.

**Narration → visual rules**
- One sentence ≈ one location or camera phase (V3 §4). Transitions land on pivot words ("your brain" V4 #214, "People"
  #331, "If time" #616, "You see" #957).
- Every number gets a physical, diegetic counterpart (cheque, LED sign, floor buttons, digit skyline, coin board,
  stopwatch, CREDITS counter; V3 §4, V5).
- Literal illustration of every noun phrase first, then a twist on it (scent wisp pulling Kai V1 #1025; magnet car V2
  #908; a "lineup" of digits V4 #857).

---

## 7. Visual devices

### 7.1 Recurring inserts

| Insert type | Look | Occurrences | Videos (count of 5) |
|---|---|---|---|
| **Cutaway diagram / explainer prop** | Clean infographic (cross-section, depth chart, labelled leaf) or a diagram that lives *inside* the world as a 3D prop (par sheet, coin board, digit skyline) | V1 skin + leaf label (#610–813); V2 depth chart + EEG (#716–862); V3 elevator buttons, skyline, coin board, histogram; V4 blueprint (#616–711); V5 par sheet + prize wheel (#542–928) | **5/5** |
| **Document / poster / paper** | Engraved field-guide poster, blueprint on cyan paper, comic sheets, flipbook, notepad sketch, cheques, legal pad, printed list | V1 #185–252; V2 #1093; V3 #1–108, #1151; V4 #616, #1078–1200; V5 #560–768 | **5/5** |
| **Macro / ECU insert** | Object fills the frame, heavy DOF | leaf (V1 S7), eye (V2 #816, V4 #181–213), pen (V3 #1), CHRONO-2 (V4 #565–615), reels and bill acceptor (V5 #1, #341) | **5/5** |
| **Fake UI / LED screens** | Dark navy background, one glowing accent, Poppins/Inter-like HUD type, counters | radar, X-ray, thermal HUD (V1 S5, S14, S20); LED counter $0→$2,000,000 and video teller (V3 #107–130, #253); CHRONO-2 (V4); CREDITS 0→100 and progressive sign (V5 #406–414) | 4/5 |
| **X-ray / thermal / wireframe** | Translucent cyan body or wireframe, scan-line reveal | V1 X-ray skeleton + thermal; V2 X-ray Theo (#372–564); V5 cyan wireframe (#779–928) | 3/5 |
| **Inside-the-head world** | Zoom through the pupil or the head into a "control room" | V2 pupil → corkboard (#855); V4 pupil → brain room (#214), door on head (#957) | 2/5 |
| **POV** | First-person hands, or an object's POV | V1 S19, V2 S3 (#321–371), V5 machine POV (#251–340) | 3/5 |
| **Celebrity / authority cameo** in series style | Same body template, no realism | Edison (V2 #617–717) | 1/5 |

### 7.2 VFX vocabulary

| VFX | Spec | Videos | Notes |
|---|---|---|---|
| **Sweat drop** | pale-blue teardrop, dark outline, white highlight, on the upper side of the head; pops on in 0 f, may bob 1–2 px; 2–3 drops for peak panic; rises upward in free fall | V1, V2, V3, V4 (**4/5**) | V1 #421+, V2 #1030–1063, V3 #77–105, V4 #57–213 |
| **4-point sparkle / glint** | white star with glow, scale 0→1→0 over 6–15 f; or a diagonal light sweep over 6–8 f | V1, V2, V3, V4 (+ V5 sweep) (**5/5**) | V2 #238–249, V3 #1291–1390, V5 #644–650 |
| **Motion / impact lines** | short "((" vibration arcs, 3-dash shake ticks, expanding white sound arcs, 4–6 stamp tick lines, chalk speed lines | **5/5** | V1 #1267–1293, V2 #484–534, V3 #1176–1186, V4 #89–90, V5 #700–701 |
| **Full-frame colour grade shift** | adjustment layer ramp 4 f in / 4 f out (alarm), or a ≈1 s time-lapse (dusk → night) | V1, V2, V3, V4 (**4/5**) | V1 #1528–1560, V2 #983–1046, V3 #285–298, V4 #982–1069 |
| **Red annotation** | red X pop (0→120→100 % in 3 f, staggered 2 f), red ellipse, red "0/4" scrawl, red circled "x1", red stamp | V1, V3, V4, V5 (**4/5**) | V1 #1644–1680, V3 #1042, V4 #927, V5 #681 |
| **Counters / ticking numbers** | odometer ease-out, digit drum roll, LED dot-matrix | V1, V3, V4, V5 (4/5) | V3 #107–130, V5 #698–722 |
| **Smoke / dust puffs** | white sizzle puffs, dark cough puff, pink crash dust, toxic cloud | V1, V4 | V1 #735–763, #1923–1941; V4 #403–437 |
| **Tears / steam / blush / vein / blisters / frost** | face-layer sprites (§3.1) | V1 (Kai only) | V1 #1171–1221, #908–944 |
| **Dust motes / bokeh** | warm specks drifting at low opacity | V2, V3, V5 | V2 #620–715, V5 S7 |
| **Motion blur / rack focus** | directional blur on whips and spins; DOF ramps on inserts | V3, V4, V5 | V3 #1145–1160, V4 #397–402, V5 #800–856 |
| **Scan line** | bright cyan line with glow, wipes between layers | V1, V2 | V1 #631–653, V2 #373–383 |
| **Eyelid vignette / blur-out** | feathered black bands closing; a Gaussian ramp 0→25 px | V2 #331–369, V1 #1836–1868 | subjective POV |
| **Head tint** | fill swap (green, red, lavender) | V1, V4 | V1 #67, #1171; V4 #541 |
| **Not used anywhere** | lens flares as transitions, glitch, light leaks as a style, film grain, emoji stickers, shaking captions | — | |

### 7.3 Transitions

Pooled over 55 joins in 60 shots:

| Transition | Count | Share | Length / spec | Evidence |
|---|---|---|---|---|
| **Cross-dissolve on moving cameras** (incl. match-dissolves and the morph-dissolve) | 42 | **76 %** | **3–8 f, typical 5–6 f, linear**; both shots keep their camera moves through it; sometimes a double-exposure ghost | V1 16–17 (3–7 f), V2 7 (4–8 f), V3 8 (5–8 f), V4 4 (6–8 f), V5 6 (4–6 f) |
| **Zoom-through portal** (push into an object that opens onto the next scene: splat window, pupil, door drawn on a head, flipbook page, machine door) | 5 (+1 hybrid) | 9–11 % | accelerating "suction" push, exponential: ≈1.0→1.2 over ⅔ of the move, then ×2–4 in the last 8–12 f | V1 #758–770, V2 #855–863, V4 #214–228, #961–971, #1153–1179, V5 #497–547 |
| **Hard / jump cut** | 3 | 5 % | impact or "step inside" only | V3 #430, V4 #712, V5 #134 |
| **Whip pan inside one set** | 2 | 4 % | ≈580 px in 15 f, roll +12°, motion blur | V3 #1145–1160, #1209–1228 |
| **Camera move-through / crane** | 1 (+ many in-shot) | 2 % | continuous move replaces the cut | V1 #73–90 |
| **In-shot reveal wipe** | 1 | 2 % | poster rips off (paper wipe) | V1 #226–252 |
| **Match cut** | 1 | 2 % | identical prop in the new scene (stack → flipbook) | V4 #1078 |
| **Loop ending** | 1 explicit + 2 callbacks | — | last frame = first frame layout | V4 #1200 → #1; V2, V3 bookends |

Rules: never two hard cuts in a row; ≈1 join per 3.5–4 s; put the join on a narration pivot word; for match
transitions, align the outgoing subject to the incoming subject's screen position before the dissolve starts
(V1 camera.md "Transition rule").

### 7.4 In-scene text

- Legible, correctly spelled hero text is **part of the scene**, not a caption: "MANCHINEEL", "HYPNAGOGIA", "THE ONE",
  "LONE STAR THRILLS", "REEL 3: EVERY STOP", "ONE CLICK SHORT". Use bold rounded display caps for signage, serif caps
  for plaques and posters, typewriter type for lists, and handwriting for cheques, sketches and scrawls.
- UI/HUD type: Poppins/Inter SemiBold, small letter-spaced caps for headers (V1 visuals §6).
- Anything that **changes** (counters, written numbers, lit buttons) must be an overlay rendered in code, not baked
  into the plate (V3 visuals §1; V5 recommendation).

### 7.5 Camera grammar (summary, details in each `camera.md`)

| Move | Numbers | Evidence |
|---|---|---|
| **Never static** > ≈1 s; default slow push-in under narration | +1–7 %/s scale (V1 ≈+4 %/s; V3 median +5 %/s; V5 1.2–2.9 %/s calm, 7–8 %/s tension; V4 +4 %/s holds, up to +15 %/s on 2-shots), linear, slight drift toward the face | all camera.md |
| **Reveal pull-back** at shot start from an ECU detail | ×0.16–0.8 in 0.5–1.4 s, strong ease-out (≈70–80 % of the move in the first third) | V2 #9–25, V3 #1–30, V5 #1–40 |
| **Suction push** into a portal | exponential ease-in ending in a zoom-through | V4 #181–213, #857–967 |
| **Roll accents** | 5–19° during moves, levelling at rest; Dutch only on inserts and CUs | V2 S1/S5, V3, V5 S4/S5 |
| **Punch-in / recoil** | +15 % in 3 f on a reaction; −11 % recoil on an impact | V1 #748–750, V2 #1018–1030 |
| Angles | eye level for characters; high or bird's-eye to show a setup; low on monuments | all |

---

## 8. How it was likely made

### 8.1 What is certain (observed directly)

| Fact | Evidence |
|---|---|
| The files are YouTube re-downloads (720×1280, 30 fps, Lavf remux). No authoring metadata survives. | toolchain E1 |
| Captions are burned in, word-timed, in one fixed style and position, above every other layer including dissolves. | §5; all visuals.md |
| Joins are mostly 3–8 f linear crossfades in which **both** shots keep moving. Hard cuts are rare (3 in 225 s). | §7.3; toolchain E6 |
| Expressions change as discrete drawings (≤2 in-between frames), frame-aligned to stressed words. | §3.4 |
| Many camera moves show **true perspective parallax** of painted 3D-looking sets (orbits, cranes, a dolly through a car window, a skyline with dozens of independently parallaxing houses). | V3 S6 #751–840; V4 S1/S2; V5 S2; V1 S2 |
| Generative-video artifacts exist in some shots: a cartoon-to-3D morph (V1 #73–184), per-frame boiling smoke (V1 #1200–1223), garbled LED glyphs (V4 #528–568), smeared pseudo-text in small print (V5 plates; V3 background lettering #140), an undefined blob hand (V5 #345–390), a physical morph strip → wheel (V5 #769–774). | visuals.md §8/§2 |
| Big hero text in plates is crisp and correctly spelled; changing numbers are clean and monotonic. | V3 #107–130, V5 #406–414 |

### 8.2 Hypotheses, reconciled

Ranking from `system/research/toolchain_hypotheses.md` (H1 ~65 %, H2 ~20 %, H3 ~8 %, H4 ~5 %, H5 ~2 %), checked
against the per-video conclusions:

| Hypothesis | Per-video verdicts | Evidence for | Evidence against |
|---|---|---|---|
| **H1: AI stills → AI image-to-video per shot → NLE (dissolves, auto-captions, TTS)** | V4 "most likely" (whole shots); V5 "most likely"; V1 for the aerial S2 and possibly the walk/sit; V3 "either 3D or I2V" for big moves | True parallax on painted worlds (§8.1); morph and boil artifacts; garbled small text vs crisp big text (typical of GPT-image/Nano-Banana stills); V5 soft face morphs; Noggin's face fading during a turn (V4 #252); off-the-shelf 2026 products sell exactly this look (Higgsfield "Stickman Cartoon" preset, kaomei/stickman-video-director: toolchain §2) | ≈90 face swaps in V1 and ≈60 in V3 land **frame-exactly on stressed words with zero in-betweens**, which is hard to get from prompted I2V clips of 3–6 s; constant outline weight and fixed shirt pattern across poses (V1 §1, Kai sheet); identical VFX sprites reused across shots; UI counters too clean for generation |
| **H2: hybrid: AI plates + 2.5D compositing (AE 3D layers or Blender cards) with sprite face swaps; I2V only for hard shots** | V1 "2D cut-out puppet with face sprite swaps" for Kai; V2 "3D set or AI plate + 2D character cards + a camera in Blender or AE 3D"; V3 "2D vector puppets with a face-swap library" + AI plates | Hard face swaps on exact frames; brows part of a face sprite; constant line weight; soft blob shadows; grades over the character like adjustment layers; overshoot pop-ons (0→120→100 % in 3 f) and trim-path draw-ons are AE idioms; VFX sprites identical across shots; drawn back views hidden under FX | Many moves have more parallax than 3–4 planes can give (V3 S6, V4 S1); V5's face morphs; toolchain spot checks found no rigid "pin" look on the samples it checked |
| **H3: fully hand-rigged 2D** (Character Animator / Moho / AE + Duik) | none primary | swap sets explain hard face swaps; "hand-made" wording in CLAUDE.md | cost of ≈25 painted perspective-changing scenes per video; I2V artifacts present |
| **H4: Blender (Grease Pencil + image planes)** | V2 suggests Blender/Cycles-like plates; recipes in every camera.md | real camera with DOF; ink-outlined 3D sets match a Line Art/Freestyle look | no GP line or EEVEE shading tells; painted texture drift between shots (V1 canopies differ S4/S12/S17) looks generated |
| **H5: Cavalry / Rive / Spine / Toon Boom** | none | — | nothing in the footage |

### 8.3 Balanced conclusion

- **Backgrounds and props are AI-generated stills in one locked style (high confidence).** Evidence: the same tree
  redrawn differently per shot, garbled small print next to perfect hero text, and painterly-3D with ink lines.
- **Big camera moves come from image-to-video or a real 3D scene (high confidence that they are not flat 2D layer
  slides).** I2V is more likely for morphs and crowded parallax (V1 S2, V3 S6, V4 S1, V5 S7–S8).
- **Character acting is the open question, and the videos disagree.** V1–V3 (and most of V4) show sprite-style hard
  face swaps aligned to the voice: evidence for a compositing or editing layer that places faces on the narration
  timeline (H2), or an audio-aware generator. V5 shows I2V-style soft face morphs. The likeliest reading is a
  **mixed pipeline that changed per shot or over time**: AI keyframes → I2V for motion → an edit layer that adds
  dissolves, captions and, in at least some videos, face/FX overlays and counters. This is **inference**; no
  authoring data exists.
- **Captions, dissolves and counters are post-production (high confidence).**

### 8.4 What we do (replication decision)

Follow toolchain §4: GPT-image style-locked plates and character/face sprites, then deterministic 2.5D shots in code
(Remotion; Blender 5.2 when real parallax is needed) with **sprite face swaps on word timestamps** (§3.5). I2V with
start/end frames is reserved for falls, crane reveals, orbits and morphs. Captions follow §5. This reproduces every
"certain" property in 8.1 and keeps timing exact, whichever hypothesis turns out to be true. Validate output against
the reference stats with `tools/metrics.py`, `motion.py` and `palette.py`: shot length 3–4 s, push rate 1–7 %/s,
caption y = 70 %, holds median ≈17 f.
