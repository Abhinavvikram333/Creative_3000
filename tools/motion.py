"""Helpers over frame_metrics.csv (measured on every frame).

python3 motion.py <frame_metrics.csv> range <start_frame> <end_frame>
    -> summed camera motion for that frame range (zoom factor, pan px, tilt px, roll deg) + per-second breakdown
python3 motion.py <frame_metrics.csv> candidates
    -> frames where the image changes sharply (candidate cuts / transitions), grouped into windows
"""
import csv
import sys

rows = list(csv.DictReader(open(sys.argv[1])))
for r in rows:
    for k in r:
        r[k] = float(r[k])

if sys.argv[2] == "range":
    a, b = int(sys.argv[3]), int(sys.argv[4])
    seg = [r for r in rows if a < r["frame"] <= b]

    def summ(s):
        sc = 1.0
        for r in s:
            sc *= r["scale"]
        return sc, sum(r["dx"] for r in s), sum(r["dy"] for r in s), sum(r["rot_deg"] for r in s)

    sc, dx, dy, rot = summ(seg)
    print(f"frames {a}-{b}: zoom x{sc:.4f} ({'in' if sc > 1.005 else 'out' if sc < 0.995 else 'none'}), "
          f"content dx {dx:+.0f}px (camera pans {'left' if dx > 0 else 'right'}), "
          f"content dy {dy:+.0f}px (camera tilts {'up' if dy > 0 else 'down'}), roll {rot:+.2f} deg")
    print("per-second (frame: zoom, dx, dy, min_inliers):")
    for s in range(a, b, 30):
        part = [r for r in seg if s < r["frame"] <= min(s + 30, b)]
        if part:
            z, x, y, _ = summ(part)
            print(f"  {s}-{min(s + 30, b)}: x{z:.4f} {x:+.0f} {y:+.0f} {int(min(r['inliers'] for r in part))}")
else:
    hits = [r for r in rows[1:] if r["hist_dist"] > 0.22 or r["diff"] > 0.09 or r["inliers"] < 30]
    win = []
    for r in hits:
        f = int(r["frame"])
        if win and f - win[-1][-1] <= 3:
            win[-1].append(f)
        else:
            win.append([f])
    for w in win:
        print(f"frames {w[0]}-{w[-1]}  (t={(w[0]-1)/30:.2f}s)")
