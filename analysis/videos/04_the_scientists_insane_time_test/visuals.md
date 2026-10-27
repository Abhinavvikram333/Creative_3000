# Visual analysis: 04 "The Scientist's Insane Time Test"

## STYLE LOCK (reuse verbatim in every prompt for this video)
```
Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with large perfectly round warm-white heads,
thick uniform dark-brown/near-black outlines (#2a2024, about 1% of frame width), minimal faces (black dot or hollow
ring eyes, single thick brow strokes, simple line mouths or a small grid of teeth), bean/capsule torsos in solid flat
colours, thin black noodle stick limbs ending in black ball hands, no noses or ears; composited into a bright,
richly detailed semi-realistic 3D-rendered world (sunny Texas amusement park, orange steel lattice, navy banners,
blue sky with puffy clouds) with painted textures and thin dark ink contour lines, soft global illumination,
gentle bloom, shallow depth of field on far layers, clean digital finish, no film grain, vertical 9:16.
```

## 1. Art style

- **Two render styles mixed on purpose.**
  1. **Characters**: flat 2D cel drawings. Each part is one fill colour plus at most one soft shade band, outlined with a thick dark-brown/black line (~6–8 px at 720p, constant weight). Heads are near-perfect circles, about 1/3 of body height for adults (Klaus, Dex) and up to 1/2 for small extras. Faces are just eyes (dots, hollow rings, flat half-lids, ^ ^ arcs, spirals), brow strokes and a mouth (line, wavy line, "o", grid of teeth). Torsos are capsules/beans. Limbs are black noodles with ball hands. Clothes are flat colour blocks with stitched-line details (Dex's harness has dashed stitch lines and grey buckle squares).
  2. **Worlds**: 3D-looking scenes with real perspective, soft GI and painted textures, plus thin ink contour lines on the 3D objects. Examples: the orange lattice tower and grated deck, parking lot with tiny cars, net, Ferris wheel and coaster, brain room with wood floor and bookshelves, support-group room, lineup room, BBQ deck.
- **Insert styles** (break from the world style for "document" moments):
  - Blueprint: chalk-white line drawing on cyan-blue paper with a grid, hand-lettered CAD font.
  - Brain comic sheets: colour pencil/ink cartoon on cream paper.
  - Flipbook page: ink line art with flat colours on cream paper texture, and visible line boil at 1180–1182.
- **2D characters inside 3D space**: characters always face camera or 3/4. When the camera orbits (the brain room), the character turns to a back view rather than showing true 3D rotation, so the turnaround is drawn, not modelled. Contact shadows are soft dark ellipses. Cast shadows on the plaza are long diagonal 3D shadows (746–856).
- Overall feel: Cyanide-&-Happiness-style characters in a Pixar-lite 3D world with storybook painterly texture.

## 2. Lighting moods

| Mood | Shots / frames | Notes |
|---|---|---|
| Bright midday exterior | 1, 4, 6 (1–213, 438–615, 712–856) | Saturated blue sky (#348cd6), puffy white clouds, hard sun, long shadows on the plaza |
| Warm cosy interior (daylight through portholes) | 2, 8 before 982 | Cream walls, wood, rainbow rug, green lamp |
| **Red emergency alarm** | 982–1066 | Whole frame red-tinted (multiply/overlay #d3361f), light rays from upper-left, porthole sky shifts purple. Fades out 1066–1069 |
| Flat cool fluorescent | 3 (support group) | Mint wall, ceiling panels, soft even light |
| Film-noir lineup | 7 | Dark warm-brown room, a single cone pendant lamp with warm bloom, a cold white backlit window |
| Golden-hour sunset | 9 | Pink-orange-purple sky, backlight bloom, string lights, warm rim on characters |
| Paper | 5, 10 | Flat even light on paper texture plus a soft vignette |

## 3. Depth / parallax layers

- **Tower top**: far city skyline and haze | mid parking lot, plaza, trees | near tower lattice, deck, banners | characters.
- **Brain room**: far porthole view (sky, tower, pigeon) | mid walls, bookshelf, lamp | near desk, drawings, stool, Noggin | foreground desk edge and papers.
- **Support group**: wall and banner | chairs in a circle | table with toys | foreground sign-in table and cookie.
- **Landing net**: sky, Ferris wheel and coaster | trees | tower legs | net | front rail, yellow curb, plaza.
- **Lineup**: ceiling | glass window with height chart and digit suspects | counter/ledge | witnesses (chest-up in front).
- **BBQ**: sunset sky and clouds | fence, house, power pole, pickup | deck boards | chairs, Dex, friends | the dog Biscuit in the near foreground.

All camera moves show true perspective parallax (not flat layer slides), so each scene needs either a real 3D set or an AI image-to-video move.

## 4. VFX inventory

| VFX | Frames | Look | Build |
|---|---|---|---|
| Sweat drops (rising) | 57–213, Noggin 231–251, Amy 972–1026, Elmer 541–560 | White/pale-blue teardrops with dark outline and a highlight. During the fall they stream *upward* | 2D sprite; particle emitter in AE/Blender with an upward velocity |
| Motion lines / swoosh | 89–90, blueprint 631–711 | Thin white arcs; chalk speed lines above the falling figure | Shape layers / drawn |
| Heavy motion blur | 61–200 background, 719–726 Dex landing smear | Directional blur | Camera motion blur (Blender) or AE CC Force Motion Blur |
| Pupil-lens reveal | 214–228 | Pupil → glossy glass circle with a specular arc → iris ring grows to fill the frame | AE: circular mask + scale, plus highlight shape |
| Rack focus / DOF | 397–437, 565–615, 1078–1110 | Strong background gaussian blur | Blender DOF / AE Camera Lens Blur |
| Crash sparkles + pink dust | 403–437 | White 4-point stars + pink puff clouds, slow-mo | Sprite particles at 10 % speed |
| LED glow/bloom | 569–615 | Red bloom around the CHRONO-2 | Glow effect, threshold on red |
| Callout circle + check | 668–697 | White chalk line draws on, circle scales up, red dot-matrix "47" fades in, check draws on | AE trim paths + scale |
| Door drawn on head | 957–968 | Black outline draws on the white head, door with knob swings open on a hinge | AE trim path + 3D layer rotate |
| Red alarm tint + rays | 982–1069 | Red overlay ramp of ~4 frames in and ~4 frames out, god-ray sweep | Adjustment layer (Tint/Fill, blend Multiply/Overlay) + light-ray layer |
| Paper slap/stack, rubber band snap | 1004–1068 | Sheets fly onto the pile every 2–3 frames; a red band snaps on in 1 frame | 3D cards (Blender) or AI video |
| Paper flutter (flipbook) | 1080–1200 | Pages flip at about 1 page/frame with curl | Blender page-curl rig or AI video |
| Shake lines | 1183–1200 | Three short curved black strokes next to Dex's head (drawn page) | Drawn |
| Dizzy spirals | Dex 731–745, Tad 757–786 | Eyes replaced by black spirals | Face swap |
| Line boil | 1180–1182 | Ink outline jitter on the drawn tower | Wiggle/turbulent displace, posterised to 12 fps |
| Queasy skin tint | Gil 541–600 | Face fill turns lavender/blue-grey (#9c9cbb) | Colour swap of the head fill |

## 5. Captions

- Font look: **heavy rounded geometric sans** (Montserrat/Poppins ExtraBold–Black class), sentence case, natural punctuation ("Apparently,", "die.").
- **White fill (#f1ebe6), thick black outline (~4–5 px at 720p, #0f0909)** plus a soft dark drop shadow.
- Size: cap height about 45 px at 720x1280 (≈3.5 % of frame height). A single word is about 120–330 px wide.
- Position: centred horizontally, centre at **y ≈ 900–905 px (70 % down)**, fixed for the whole video. The same position is used over every background, including the busy blueprint and the red alarm.
- Content: 117 cards. **1 word per card for 80 %**, 2 words for 17 %, 3 words for 3%. Card length follows the spoken word, 2–28 frames (mean 10.3). No gaps.
- Animation: **hard swap per word** with no scale-pop, fade or colour highlight. The card stays put through transitions and dissolves.

## 6. Transitions

| Type | Count | Frames | Detail |
|---|---|---|---|
| Dissolve (crossfade) | 4 | 331–336, 438–444, 616–621, 857–864 | 6–8 frames, linear. The first is a graphic match (porthole circle → rug circle) |
| Zoom-through portal | 3 | 214–228 (pupil), 961–971 (door on head), 1153–1179 (flipbook page) | Push into an object that opens onto the next scene |
| Hard cut | 1 | 712 | Impact cut to the landing |
| Match cut | 1 | 1078 | Rubber-banded stack → identical flipbook in Dex's hands |
| Loop | 1 | 1200 → 1 | The drawn page equals the opening layout |

## 7. Text and labels inside the scene

All in-scene text is clean, stable and readable, which suggests image-model text rendering or designed overlays.
- "LONE STAR THRILLS" (white bold sans + star on a navy banner with a red/white stripe). Vertical "FREEFALL" banner (white letters on navy). "100 FT" small yellow sign on the tower.
- "CHRONO-2" (navy hand lettering on a cream masking-tape label). "OFF ON" (white small caps on the device).
- "CRASH SURVIVORS · TUESDAYS 7PM" banner (navy + red, car icon). "ONE MILE AT A TIME" poster. "DONUTS" sign. Name tags GUS, CARL, DEB, RAY, MO. "SIGN-IN" clipboard. "STOP" on the playmat. Texas plate "SLOMO".
- Blueprint: "HYPOTHESIS", "FIG. 1", "SUBJECT 7", "IF TIME SLOWS → CAN READ #", "DROP: 100 FT", "DETAIL A: DISPLAY", "PROJECT: TIME TEST / LONE STAR THRILLS – DALLAS TX / DWG NO. 7 / SCALE 1:200 / DRAWN: DR. K / SHEET 7/14".
- "DROP-OFF NET" sign (red letters on white). Stopwatch "2.49".
- Lineup: height lines 3′–6′, placards A–F, "CASE 07". Clipboard red "0/4".
- "PANIC" (red on a yellow/black hazard box). "NORMAL TUESDAY" (black on a yellow sticky note). Comic sheets numbered "FR 0047".

## 8. How each element was most likely made (hypotheses + evidence)

| Element | Most likely | Evidence |
|---|---|---|
| Overall shots | **AI image-to-video from style-locked keyframes** (see `system/research/toolchain_hypotheses.md` H1) | Long continuous 3D moves through painted worlds with true perspective change (the tower dive with roll, the orbit around Noggin). Props change perspective consistently. Characters stay 2D-flat but move smoothly |
| CHRONO-2 digits | AI video (generative) | Readable numbers ("47", "19", "30", "48"…) alternate with **garbled noisy LED frames** (541–547, 553–560, 528–534). A coded LED display would switch cleanly; a generative model morphs between glyphs |
| Character faces | Swapped expressions (could be I2V-prompted, or AE face-swap) | Expressions change in 0–1 inbetween frames (#129, #1122) and 2-frame gags (#190–191, #494–495). These read as deliberate swaps, not morphs. To replicate, use a face-sprite swap system |
| Captions | Editor auto-captions (CapCut-class) | Fixed position, one word, no styling variation |
| Dissolves | Editor | Uniform 6–8-frame linear crossfades |
| Blueprint / flipbook page / comic sheets | AI image (GPT-image-class) with exact text | Perfectly legible small text in title blocks. The page "line boil" at 1180–1182 suggests I2V on a drawn plate |
| Red alarm tint | Editor adjustment layer *or* prompted in I2V | Uniform tint over every element including the porthole; smooth 4-frame ramp |
| Brain-room characters (Noggin, Amy) | AI image + I2V | Same painted lighting on characters and set; Noggin's face fades out as he turns (#252), typical of I2V |
| Zoom-through portals | Probably I2V first/last-frame (start = eye ECU, end = brain room), or AE masks | Smooth continuous growth of the pupil into a lens. Door drawn with trim-path-like strokes (#957–960) |

**Replication suggestion:** generate keyframe stills per shot with the STYLE LOCK, animate with start/end-frame I2V for the camera-heavy shots (1, 2, 3, 6, 8, 9), and build the deterministic parts in code/AE (captions, dissolves, red tint, callout, LED digits, face swaps on the 2D-flat dialogue shots 4 and 7).
