"""Per-frame measurements over EVERY frame (30 fps): cuts, global camera motion, colour.

usage: python3 metrics.py <work_dir/vNN> <out_dir>
writes out_dir/frame_metrics.csv, out_dir/shots.json, out_dir/palettes.json, out_dir/motion_plot.png
"""
import csv
import json
import os
import sys

import cv2
import numpy as np
from sklearn.cluster import KMeans

FPS = 30
wd, out = sys.argv[1], sys.argv[2]
os.makedirs(out, exist_ok=True)
fdir = os.path.join(wd, "frames")
names = sorted(os.listdir(fdir))

orb = cv2.ORB_create(1500)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

rows = []
prev_small = prev_kp = prev_des = prev_hist = None
for idx, name in enumerate(names, start=1):
    img = cv2.imread(os.path.join(fdir, name))
    small = cv2.resize(img, (360, 640))
    gray = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(small, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [32, 16], [0, 180, 0, 256])
    cv2.normalize(hist, hist)
    kp, des = orb.detectAndCompute(gray, None)
    r = {"frame": idx, "time": round((idx - 1) / FPS, 3),
         "brightness": round(float(hsv[..., 2].mean()) / 255, 4),
         "saturation": round(float(hsv[..., 1].mean()) / 255, 4),
         "diff": 0.0, "hist_dist": 0.0, "dx": 0.0, "dy": 0.0, "scale": 1.0, "rot_deg": 0.0, "inliers": 0}
    if prev_small is not None:
        r["diff"] = round(float(np.mean(cv2.absdiff(small, prev_small))) / 255, 4)
        r["hist_dist"] = round(float(cv2.compareHist(prev_hist, hist, cv2.HISTCMP_BHATTACHARYYA)), 4)
        if des is not None and prev_des is not None and len(kp) > 8 and len(prev_kp) > 8:
            m = bf.match(prev_des, des)
            if len(m) >= 8:
                p0 = np.float32([prev_kp[x.queryIdx].pt for x in m])
                p1 = np.float32([kp[x.trainIdx].pt for x in m])
                M, inl = cv2.estimateAffinePartial2D(p0, p1, method=cv2.RANSAC, ransacReprojThreshold=2.0)
                if M is not None:
                    s = float(np.hypot(M[0, 0], M[1, 0]))
                    # report translation in full-res (720x1280) pixels
                    r.update(dx=round(float(M[0, 2]) * 2, 2), dy=round(float(M[1, 2]) * 2, 2),
                             scale=round(s, 5), rot_deg=round(float(np.degrees(np.arctan2(M[1, 0], M[0, 0]))), 3),
                             inliers=int(inl.sum()))
    rows.append(r)
    prev_small, prev_kp, prev_des, prev_hist = small, kp, des, hist

with open(os.path.join(out, "frame_metrics.csv"), "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# --- cut detection: histogram jump OR large pixel jump with few motion inliers ---
cuts = [1]
for r in rows[1:]:
    hard = r["hist_dist"] > 0.35 or (r["diff"] > 0.12 and r["inliers"] < 40)
    if hard and r["frame"] - cuts[-1] >= 4:
        cuts.append(r["frame"])
shots = []
for i, start in enumerate(cuts):
    end = (cuts[i + 1] - 1) if i + 1 < len(cuts) else len(rows)
    seg = rows[start:end]  # transitions inside shot (exclude first frame)
    tot_scale = float(np.prod([x["scale"] for x in seg])) if seg else 1.0
    tot_dx = float(sum(x["dx"] for x in seg))
    tot_dy = float(sum(x["dy"] for x in seg))
    tot_rot = float(sum(x["rot_deg"] for x in seg))
    moves = []
    if tot_scale > 1.02: moves.append(f"push-in/zoom-in x{tot_scale:.3f}")
    if tot_scale < 0.98: moves.append(f"pull-out/zoom-out x{tot_scale:.3f}")
    if abs(tot_dx) > 15: moves.append(f"content moves {'right' if tot_dx > 0 else 'left'} {abs(tot_dx):.0f}px (camera pans {'left' if tot_dx > 0 else 'right'})")
    if abs(tot_dy) > 15: moves.append(f"content moves {'down' if tot_dy > 0 else 'up'} {abs(tot_dy):.0f}px (camera tilts {'up' if tot_dy > 0 else 'down'})")
    if abs(tot_rot) > 1: moves.append(f"roll {tot_rot:.1f} deg")
    shots.append({"shot": i + 1, "start_frame": start, "end_frame": end,
                  "start_time": round((start - 1) / FPS, 3), "end_time": round(end / FPS, 3),
                  "frames": end - start + 1, "duration_s": round((end - start + 1) / FPS, 3),
                  "measured_camera": moves or ["static (or motion below threshold)"],
                  "total_scale": round(tot_scale, 4), "total_dx_px": round(tot_dx, 1),
                  "total_dy_px": round(tot_dy, 1), "total_roll_deg": round(tot_rot, 2),
                  "mean_brightness": round(float(np.mean([x["brightness"] for x in rows[start - 1:end]])), 3)})

# --- palettes: per shot (middle frame) + whole video ---
def palette(img, k=6):
    px = cv2.cvtColor(cv2.resize(img, (90, 160)), cv2.COLOR_BGR2RGB).reshape(-1, 3).astype(np.float32)
    km = KMeans(n_clusters=k, n_init=4, random_state=0).fit(px)
    counts = np.bincount(km.labels_, minlength=k)
    order = np.argsort(-counts)
    return [{"hex": "#%02x%02x%02x" % tuple(int(c) for c in km.cluster_centers_[j]),
             "share": round(float(counts[j]) / len(px), 3)} for j in order]

pal = {"shots": []}
allpx = []
for s in shots:
    mid = (s["start_frame"] + s["end_frame"]) // 2
    img = cv2.imread(os.path.join(fdir, names[mid - 1]))
    s["palette_mid_frame"] = mid
    s["palette"] = palette(img)
    pal["shots"].append({"shot": s["shot"], "frame": mid, "palette": s["palette"]})
    allpx.append(cv2.resize(img, (45, 80)))
pal["video"] = palette(np.vstack(allpx), k=12)

with open(os.path.join(out, "shots_measured.json"), "w") as f:
    json.dump({"fps": FPS, "frames": len(rows), "shot_count": len(shots), "shots": shots}, f, indent=1)
with open(os.path.join(out, "palettes.json"), "w") as f:
    json.dump(pal, f, indent=1)

# palette strip image for the whole video
strip = np.zeros((80, 960, 3), np.uint8)
x = 0
for c in pal["video"]:
    w = max(1, int(round(c["share"] * 960)))
    rgb = tuple(int(c["hex"][i:i + 2], 16) for i in (1, 3, 5))
    strip[:, x:x + w] = rgb[::-1]
    x += w
cv2.imwrite(os.path.join(out, "palette_video.png"), strip)
print(f"{wd}: {len(rows)} frames, {len(shots)} shots")
