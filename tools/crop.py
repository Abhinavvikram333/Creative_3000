"""python3 crop.py <frame.jpg> <x> <y> <w> <h> <out.(jpg|png)>   (pixel coords on the 720x1280 frame)"""
import sys

from PIL import Image

src, x, y, w, h, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
im = Image.open(src).convert("RGB")
x, y = max(0, x), max(0, y)
im.crop((x, y, min(im.width, x + w), min(im.height, y + h))).save(out, quality=92)
print(out)
