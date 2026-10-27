"""python3 palette.py <image> [k]  -> dominant colours (hex + share), largest first."""
import sys

import cv2
import numpy as np
from sklearn.cluster import KMeans

img = cv2.imread(sys.argv[1])
k = int(sys.argv[2]) if len(sys.argv) > 2 else 6
px = cv2.cvtColor(cv2.resize(img, (90, 160)), cv2.COLOR_BGR2RGB).reshape(-1, 3).astype(np.float32)
km = KMeans(n_clusters=k, n_init=4, random_state=0).fit(px)
counts = np.bincount(km.labels_, minlength=k)
for j in np.argsort(-counts):
    print("#%02x%02x%02x" % tuple(int(c) for c in km.cluster_centers_[j]), round(float(counts[j]) / len(px), 3))
