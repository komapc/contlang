"""Print what the top PCA axes of the machine baseline look like: extreme common words at each end + a few words placed.
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size1/pca_axes.py   (run from the repo root)
"""
import gzip, sys
import numpy as np
sys.path.insert(0, "data/eval/runs/size1")
from run import brown_counts
c = brown_counts(); tot = {w: sum(v.values()) for w, v in c.items()}
order = sorted(tot, key=lambda w: -tot[w]); want = set(order)
vec = {}
with gzip.open("data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
    next(f)
    for line in f:
        w, rest = line.split(" ", 1)
        if w in want:
            v = np.array(rest.split(), dtype=np.float32); vec[w] = v / np.linalg.norm(v)
words = [w for w in order if w in vec]
X = np.stack([vec[w] for w in words]); Xc = X - X.mean(0)
_, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
Z = Xc @ Vt[:5].T
freq = np.array([tot[w] for w in words])
common = freq >= 20
print("words:", len(words), "; common (>=20 in Brown):", common.sum())
for a in range(5):
    z = Z[:, a]; idx = np.flatnonzero(common)
    s = idx[np.argsort(z[idx])]
    print(f"\naxis {a+1}: var share {sv[a]**2/(sv**2).sum():.1%}")
    print("  − end:", ", ".join(words[i] for i in s[:12]))
    print("  + end:", ", ".join(words[i] for i in s[-12:][::-1]))
for w in ["dog", "house", "run", "happy", "money", "water", "king", "computer"]:
    if w in vec:
        i = words.index(w); print(w, np.round(Z[i, :3] / np.abs(Z[:, :3]).max(0) * 5, 1))
