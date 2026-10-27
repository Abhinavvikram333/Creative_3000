"""python3 tools/render_swatches.py [system/color_system.json] [system/palette_swatches.png]

Renders the series colour system (core constants, grades, accents, character clothing) as a 1600 px wide swatch board.
"""
import json
import sys
import textwrap

from PIL import Image, ImageDraw, ImageFont

SRC = sys.argv[1] if len(sys.argv) > 1 else "system/color_system.json"
DST = sys.argv[2] if len(sys.argv) > 2 else "system/palette_swatches.png"
D = json.load(open(SRC))

W = 1600
BG, FG, MUTED, BORDER = "#18181b", "#f4f4f5", "#a1a1aa", "#52525b"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"
f = lambda p, s: ImageFont.truetype(p, s)
F_TITLE, F_H, F_NAME, F_TXT, F_SMALL = f(BOLD, 34), f(BOLD, 26), f(BOLD, 20), f(FONT, 16), f(FONT, 14)
F_HEX, F_HEX_S = f(MONO, 17), f(MONO, 13)

ops = []  # deferred drawing so the canvas height can be computed first
y = 0


def chip(x, y0, w, h, hexv, label=None, sub=None, hexfont=F_HEX, wrap=18):
    ops.append(("rect", (x, y0, x + w, y0 + h), hexv))
    ops.append(("text", (x, y0 + h + 4), hexv, hexfont, FG))
    yy = y0 + h + 4 + hexfont.size + 4
    for t, fnt, col in ((label, F_SMALL, FG), (sub, F_SMALL, MUTED)):
        if t:
            for line in textwrap.wrap(t, wrap)[:2]:
                ops.append(("text", (x, yy), line, fnt, col))
                yy += fnt.size + 3
    return yy


def heading(text):
    global y
    y += 18
    ops.append(("text", (24, y), text, F_H, FG))
    y += 40
    ops.append(("line", (24, y - 6, W - 24, y - 6)))


# ---------- title ----------
ops.append(("text", (24, 20), "Series colour system — pilot videos 01–05", F_TITLE, FG))
ops.append(("text", (24, 64), "Hex = measured (k-means / pixel samples on every-frame decode). B / S = mean HSV value / saturation over the grade's frames.", F_TXT, MUTED))
y = 96

# ---------- core ----------
heading("Core constants (per video 01 · 02 · 03 · 04 · 05 → series target)")
core = D["core"]
rows = [("Head fill", core["head_fill"]), ("Outline", core["outline"]), ("Limbs", core["limbs"])]
for name, c in rows:
    ops.append(("text", (24, y + 10), name, F_NAME, FG))
    x = 300
    for v, h in c["per_video"].items():
        chip(x, y, 130, 64, h, sub="video " + v)
        x += 150
    chip(x + 20, y, 170, 64, c["series_target"], label="series target")
    y += 120
# caption + shadow row
ops.append(("text", (24, y + 10), "Caption", F_NAME, FG))
ops.append(("caption", (300, y), "caption"))
chip(560, y, 90, 64, core["caption"]["fill"], label="fill")
chip(670, y, 90, 64, core["caption"]["stroke"], label="stroke ~4px")
ops.append(("text", (820, y + 10), "Cast shadow", F_NAME, FG))
x = 980
for m in core["cast_shadow"]["measured"]:
    chip(x, y, 70, 64, m["ground"], hexfont=F_HEX_S, label="ground")
    chip(x + 80, y, 70, 64, m["shadow"], hexfont=F_HEX_S, label="shadow")
    x += 170
chip(x + 10, y, 110, 64, core["cast_shadow"]["normal_blend"], label="normal blend @35-55%")
y += 130

# ---------- grades ----------
heading("Mood / lighting grades")
for gname, g in D["grades"].items():
    ty = y
    for line in textwrap.wrap(gname.replace("_", " "), 22):
        ops.append(("text", (24, ty), line, F_NAME, FG))
        ty += 26
    b, s = g["brightness"], g["saturation"]
    ops.append(("text", (24, ty + 4), f"B {b['mean']:.2f}  ({b['p10']:.2f}–{b['p90']:.2f})", F_TXT, FG))
    ops.append(("text", (24, ty + 26), f"S {s['mean']:.2f}  ({s['p10']:.2f}–{s['p90']:.2f})", F_TXT, FG))
    vids = " · ".join(sorted({u[:2] for u in g["used_in"]}))
    ops.append(("text", (24, ty + 50), "videos " + vids, F_TXT, MUTED))
    x = 300
    bottom = y
    for sw in g["swatches"]:
        bottom = max(bottom, chip(x, y, 150, 70, sw["hex"], label=sw["role"]))
        x += 160
    y = max(bottom, ty + 74) + 18

# ---------- accents ----------
heading("Accent / semantic colours")
acc = []
for k, a in D["accents"].items():
    if isinstance(a.get("hex"), str):
        acc.append((a["hex"], k.replace("_", " ")))
    elif isinstance(a.get("hex"), list):
        for i, h in enumerate(a["hex"][:3]):
            acc.append((h, k.replace("_", " ") + f" {i + 1}"))
for k, h in D["accents"]["emotion_tints"].items():
    acc.append((h, k.replace("_", " ")))
x = 24
for h, lab in acc:
    if x + 140 > W:
        x = 24
        y += 135
    chip(x, y, 130, 56, h, label=lab, wrap=16)
    x += 144
y += 140

# ---------- characters ----------
heading("Characters (head · outline · hair · clothing)")
cw, x = 390, 24
for name, c in D["characters"].items():
    if x + cw > W:
        x = 24
        y += 132
    ops.append(("text", (x, y), f"{name.replace('_', ' ')}  ({c['video']})", F_NAME, FG))
    items = [c["head"], c["outline"]]
    if c.get("hair"):
        items.append(c["hair"].split()[0])
    items += [cl["hex"] for cl in c["clothing"]][: 6 - len(items)]
    xx = x
    for h in items:
        chip(xx, y + 30, 58, 50, h, hexfont=F_HEX_S)
        xx += 63
    x += cw
y += 140

ops.append(("text", (24, y), "Source: system/color_system.json · rendered by tools/render_swatches.py", F_SMALL, MUTED))
y += 36

img = Image.new("RGB", (W, y), BG)
d = ImageDraw.Draw(img)
for op in ops:
    if op[0] == "rect":
        d.rectangle(op[1], fill=op[2], outline=BORDER)
    elif op[0] == "text":
        d.text(op[1], op[2], font=op[3], fill=op[4])
    elif op[0] == "line":
        d.line(op[1], fill=BORDER, width=2)
    elif op[0] == "caption":
        x0, y0 = op[1]
        d.rectangle((x0, y0, x0 + 240, y0 + 64), fill="#7cc8fb")
        d.text((x0 + 120, y0 + 32), op[2], font=f(BOLD, 36), fill="#ffffff", anchor="mm", stroke_width=4, stroke_fill="#000000")
img.save(DST, optimize=True)
print(DST, img.size)
