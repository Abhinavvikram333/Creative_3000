"""Extract every frame at native 30 fps and build one numbered grid per second.

usage: python3 extract.py <video.mp4> <out_dir>
out_dir/frames/f00001.jpg ...   (full-res, 1-based frame number)
out_dir/grids/sec_000.jpg ...   (6x5 grid = 30 frames, labelled with frame# and timecode)
"""
import os
import subprocess
import sys

from PIL import Image, ImageDraw, ImageFont

FPS = 30
COLS, ROWS = 6, 5
TW, TH = 216, 384  # thumb size (0.3x of 720x1280)

video, out = sys.argv[1], sys.argv[2]
fdir = os.path.join(out, "frames")
gdir = os.path.join(out, "grids")
os.makedirs(fdir, exist_ok=True)
os.makedirs(gdir, exist_ok=True)

if not os.listdir(fdir):
    subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-fps_mode", "passthrough",
                    "-q:v", "2", os.path.join(fdir, "f%05d.jpg")], check=True)

frames = sorted(os.listdir(fdir))
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)

for sec in range(0, (len(frames) + FPS - 1) // FPS):
    chunk = frames[sec * FPS:(sec + 1) * FPS]
    grid = Image.new("RGB", (COLS * TW, ROWS * TH), (20, 20, 20))
    d = ImageDraw.Draw(grid)
    for i, name in enumerate(chunk):
        n = int(name[1:6])
        im = Image.open(os.path.join(fdir, name)).convert("RGB").resize((TW, TH))
        x, y = (i % COLS) * TW, (i // COLS) * TH
        grid.paste(im, (x, y))
        t = (n - 1) / FPS
        label = f"#{n}  {int(t // 60):02d}:{t % 60:05.2f}"
        d.rectangle([x, y, x + TW, y + 24], fill=(0, 0, 0))
        d.text((x + 4, y + 2), label, fill=(255, 255, 0), font=font)
        d.rectangle([x, y, x + TW - 1, y + TH - 1], outline=(90, 90, 90))
    grid.save(os.path.join(gdir, f"sec_{sec:03d}.jpg"), quality=88)

print(f"{video}: {len(frames)} frames, {sec + 1} grids")
