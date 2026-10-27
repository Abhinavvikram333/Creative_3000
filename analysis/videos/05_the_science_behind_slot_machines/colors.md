# Colour system — 05 "The Science Behind Slot Machines"

Sources: `metrics/palettes.json` (video-wide k-means) + `tools/palette.py` (k=6) on representative frames and on the
library crops. Hex values are measured cluster centres (JPEG, so ±5 %).

## 1. Global palette (whole video, share)
| Hex | Share | Role |
|---|---|---|
| #1f1315 | 16.7 % | near-black warm shadow (casino darks, outlines) |
| #562521 | 12.7 % | deep oxblood (machine shadows, wood) |
| #744b43 | 11.9 % | warm brown mid-tone (ceiling, cabinet wood) |
| #ad1012 | 10.4 % | **machine red** (signature colour) |
| #f1f5e4 | 9.6 % | cream-white (heads, paper, reels) |
| #927768 | 7.6 % | dusty taupe (carpet, mid-ground) |
| #c4baa2 | 6.8 % | warm grey-beige (chrome highlights, tank top) |
| #27424b | 6.2 % | dark teal-slate (X-ray darks, shirt shadow) |
| #408183 | 5.3 % | teal (shirt, wireframe) |
| #d23a30 | 5.2 % | bright red (cap, stamp, wedge) |
| #cc965b | 4.0 % | gold/amber (marquee, interior) |
| #47c3b8 | 3.6 % | bright teal (Lenny's shirt) |

Overall: **warm red/brown/gold dominant (~65 %) + cream highlights + a single cool complement (teal/cyan)**
carried by Lenny's shirt and, at the end, the X-ray wireframe. Saturation stays high (mean ≈0.55–0.6).

## 2. Palette per background / mood
| Background (shots) | Frame | Palette (k=6, by share) | Mood |
|---|---|---|---|
| bg_casino_row (S1, S2, S6) | #55 | #2c0b0a · #684334 · #af2213 · #c59a60 · #f6e9d0 · #25cfa7 | warm night casino, red + gold |
| bg_pov_ceiling (S3) | #255 | #3e1712 · #6b331f · #a38372 · #685a4e · #f7e8d4 · #c55218 | dim brown, amber spots |
| bg_machine_panel_insert (S4) | #370 | #c11815 · #672822 · #2b1612 · #836755 · #bba87e · #efefd4 (+ green slot ≈#2fe07a) | hot red with green accent |
| bg_machine_dutch_cu (S5) | #440 | #3d0f0c · #a21a16 · #5d4d40 · #a47d5c · #d8b399 · #faf1e1 | red, orange rim light |
| bg_machine_interior (S7) | #550 | #80481f · #ad7238 · #f6bf5a · #e09542 · #fbf892 · #327a0c | amber monochrome + PCB green |
| par-sheet list (S7) | #640 | #fae18e · #d9ad76 · #b87b3e · #86411b · #354107 · #f5b10c | warm paper, gold highlight row |
| wheel (S7 end) | #776 | #733c1d · #f5d160 · #df873c · #a36c3e · #c91606 · #2c5d0e | gold + red wedge |
| bg_xray_machine (S8) | #840 | #261a20 · #625354 · #40a7a7 · #bfa488 · #eff4ec · #b82b2d | casino + cool cyan |

## 3. Character colours
**Lenny** (crop `emo_content_f00457`, `pose_stand_reach_f00508`)
- Head fill cream-white **#fcf6e7**, warm shading/rim **#f0c6af**, environment bloom on edge **#e09542**.
- Outline + facial strokes dark brown **#421411** (range #351518–#5a2a20); hair same family, highlight **#5f4447**.
- Shirt teal **#19bda4** (shadow #138f7d), leaf pattern mustard-yellow ≈**#e9c23a**.
- Lanyard + badge red **#cd1a15**, badge white stripe #f5efe7.
- Legs/arms = outline colour strokes; hands blob **#2a1210**.

**Bling** (crop `emo_smug_smirk_f00290`, `pose_lean_in_talk_f00290`)
- Head fill **#fdf7dd**, shading **#f4d0b7**, stubble dots **#77402a**.
- Cap red **#e83234** (shadow #b8231f), sunglasses on cap near-black #1a0e0e with white glint.
- Gold chain ≈**#d9a43a**; ribbed tank top cream **#fbedd4** / shadow **#cba78f**.
- Outline dark brown **#531c12**.

**Beanie** (background extra): white head, orange beanie ≈#e8902a.

## 4. Caption colours
- Fill white **#f8f7f8**, outline black **#000000** (~4–5 px), soft shadow black 50 %.

## 5. Accent colours (UI / explainer)
| Accent | Hex | Where |
|---|---|---|
| Jackpot highlight row | #f9e611 → #f5b015 gradient | list row #9 |
| "x1" badge | red **#cb1501** ring + text on yellow | #681+ |
| Stamp imprint / wheel wedge | **#e60f04** – #c91606 | ONE CLICK SHORT |
| Rubber stamp body | orange ≈#e8622a, knob #b81b14 | S7 |
| Paper | #fae18e (lit) / #fcd48e | list |
| LED digits | red #ff2a1a on black #1a0505 | CREDITS, progressive sign, WIN |
| Bill acceptor slot glow | green ≈#2fe07a | S4 |
| X-ray wireframe | cyan **#40a7a7 → #3fd8e8** | S8 |
| Machine signage text | gold-yellow #f2c230 on red #ad1012 | toppers, labels |
| Button colours | CASH OUT blue #6aa3d8 · BET ONE yellow #f2c230 · MAX BET orange #f08a2a · SPIN red #d61a14 | button deck |

## 6. Rules to reuse
- Keep the world warm (reds/golds/browns) and give the protagonist the only cool colour (teal) so he pops.
- Explainer accents reuse the same red (#e60f04) for "bad/house wins" and yellow-gold for "jackpot/good".
- Introduce a cool cyan only for the "x-ray / science" reveal.
