# Unique images — 05 "The Science Behind Slot Machines"

STYLE LOCK (verbatim): `Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.`

| id | Crop | Description | Exact text | Frames |
|---|---|---|---|---|
| u_paytable | `u_paytable_f00230.jpg` | Lower-cabinet paytable | '★ LUCKY 7s PAYS ★' · 777 = JACK $1,000 · ◆◆◆ = $200 · 🔔🔔🔔 = $100 · BAR BAR BAR = $50 · ANY 🍒 = $2 | 1–250, 495–541 |
| u_par_sheet_reel3 | `u_par_sheet_reel3_f00588.jpg` | Printed paper strip unrolled from reel 3 (the 'list of every stop') | 'LUCKY 7s · PAR SHEET · REV B' / 'REEL 3: EVERY STOP' / 'ROW STOP SYMBOL' / '#1 BAR, #2 BLANK, #3 CHERRY, #4 BLANK, #5 BELL, #6 BLANK, #7 BAR, #8 BLANK, #9 7 JACKPOT (highlighted yellow-orange), #10–#22 BLANK, #23–#25 CHERRY, #26 BLANK, #27 BAR' | 561–690 |
| u_par_sheet_stamped | `u_par_sheet_stamped_f00765.jpg` | Same strip after stamping: every BLANK row from #10 to #21 carries a red 'ONE CLICK SHORT' rubber-stamp imprint | list as above + 12–14 red stamps 'ONE CLICK SHORT' | 699–770 |
| u_one_click_short_wheel | `u_one_click_short_wheel_f00776.jpg` | Prize wheel / pie chart made from the strip: ~70 cream segments with tiny symbols, one large red wedge 'ONE CLICK SHORT' (~60°), a thin yellow 'JACKPOT 7' sliver next to it, gold hub ring 'LUCKY 7s · EVERY STOP', red pointer at 12 o'clock, gold studded rim | 'ONE CLICK SHORT', 'JACKPOT', 'LUCKY 7s', 'EVERY STOP' | 769–928 |

Note: these read as *in-world* outlined-3D props (paper with curl and shadow, wheel with rim depth), not flat infographics. The strip→wheel morph (#769–774) is best done in AE (bend + polar coordinates) or as an AI-video morph between the two images.

## Prompts

### u_paytable
```
[REFERENCE] attach: library/unique_images/05_the_science_behind_slot_machines/u_paytable_f00230.jpg
[SUBJECT] a red slot machine paytable panel with gold border: header '★ LUCKY 7s PAYS ★'; rows: three red 7s '= JACK $1,000', three blue diamonds '= $200', three gold bells '= $100', three BAR symbols '= $50', 'ANY' cherry '= $2'
[POSE / EMOTION / STATE] clean, fully legible text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536 (strip) / square 1024x1024 (wheel, paytable), straight-on
[LIGHTING] warm amber light, soft paper shading
[BACKGROUND] transparent
[AVOID] any text other than given, misspellings, watermark, captions, people
```
### u_par_sheet_reel3
```
[REFERENCE] attach: library/unique_images/05_the_science_behind_slot_machines/u_par_sheet_reel3_f00588.jpg
[SUBJECT] a long cream paper strip printed in dark-brown typewriter font: small header 'LUCKY 7s   PAR SHEET   REV B', title 'REEL 3: EVERY STOP', column labels 'ROW  STOP  SYMBOL', then rows each with a row number, a tiny reel-window icon with a red payline and the symbol name: #1 BAR, #2 BLANK, #3 CHERRY, #4 BLANK, #5 BELL, #6 BLANK, #7 BAR, #8 BLANK, #9 7 JACKPOT (row highlighted in a yellow-orange gradient bar), #10 BLANK, #11 BLANK, #12 BLANK, #13 BLANK; BLANK icons show the neighbouring symbol peeking at the edge
[POSE / EMOTION / STATE] clean, fully legible text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536 (strip) / square 1024x1024 (wheel, paytable), straight-on
[LIGHTING] warm amber light, soft paper shading
[BACKGROUND] transparent
[AVOID] any text other than given, misspellings, watermark, captions, people
```
### u_par_sheet_stamped
```
[REFERENCE] attach: library/unique_images/05_the_science_behind_slot_machines/u_par_sheet_stamped_f00765.jpg
[SUBJECT] the same cream par-sheet strip with rows #10 to #21 all marked 'BLANK' and each one stamped at the right with a red distressed rubber-stamp box reading 'ONE CLICK SHORT'; rows #23–#25 CHERRY, #27 BAR
[POSE / EMOTION / STATE] clean, fully legible text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536 (strip) / square 1024x1024 (wheel, paytable), straight-on
[LIGHTING] warm amber light, soft paper shading
[BACKGROUND] transparent
[AVOID] any text other than given, misspellings, watermark, captions, people
```
### u_one_click_short_wheel
```
[REFERENCE] attach: library/unique_images/05_the_science_behind_slot_machines/u_one_click_short_wheel_f00776.jpg
[SUBJECT] a carnival prize wheel used as a pie chart: gold studded rim, about 70 thin cream segments each with a tiny slot symbol, one big red wedge (60 degrees) with bold white text 'ONE CLICK SHORT', a very thin yellow segment labelled 'JACKPOT' with a red 7 directly beside it, central gold hub ring with small text 'LUCKY 7s' and 'EVERY STOP', red pointer at the top
[POSE / EMOTION / STATE] clean, fully legible text
[STYLE LOCK] Stylised 2.5D cartoon explainer frame: flat 2D vector-style characters with very round cream-white heads, thick uniform dark-brown outlines (#3a1512, ~6 px at 1080p), minimal faces (dot or lidded eyes, single-line brows, tiny mouths), noodle stick limbs, flat cel colours with only a soft warm rim glow; placed inside a richly detailed semi-realistic 3D-rendered environment with painted textures and thin dark ink contour lines, warm tungsten casino lighting, glossy reds and golds, soft bloom on lights, shallow depth of field, clean digital finish, no grain, vertical 9:16.
[COMPOSITION] 9:16 1024x1536 (strip) / square 1024x1024 (wheel, paytable), straight-on
[LIGHTING] warm amber light, soft paper shading
[BACKGROUND] transparent
[AVOID] any text other than given, misspellings, watermark, captions, people
```
