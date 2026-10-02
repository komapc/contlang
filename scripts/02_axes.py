"""PCA + varimax on GloVe vectors of the word list; name axes by their poles.

Usage: python 02_axes.py [k]   (default k=10, the 'nano' set)
"""
import sys
from collections import defaultdict

import numpy as np

from common import ROOT, load_glove

K = int(sys.argv[1]) if len(sys.argv) > 1 else 10
TOP = 8  # words shown at each pole
ALIVE = 1.0  # an axis is 'alive' for a word if |z-score| exceeds this


def varimax(phi, iters=100, tol=1e-6):
    p, k = phi.shape
    rot = np.eye(k)
    d = 0.0
    for _ in range(iters):
        lam = phi @ rot
        u, s, vt = np.linalg.svd(
            phi.T @ (lam ** 3 - lam @ np.diag((lam ** 2).sum(axis=0)) / p))
        rot = u @ vt
        d_new = s.sum()
        if d_new < d * (1 + tol):
            break
        d = d_new
    return phi @ rot


rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])

kv = load_glove()
X = np.stack([kv[w] for w in words])
X = X / np.linalg.norm(X, axis=1, keepdims=True)
Xc = X - X.mean(axis=0)

u, s, vt = np.linalg.svd(Xc, full_matrices=False)
var = s ** 2 / (s ** 2).sum()
load = vt[:K].T                      # (dim, K)
rot = varimax(load)                  # rotated loadings
scores = Xc @ rot
z = (scores - scores.mean(axis=0)) / scores.std(axis=0)

# order rotated axes by the variance they carry
order = np.argsort(-(scores ** 2).sum(axis=0))
z = z[:, order]

out = []
out.append(f"# Оси nano-{K} (английский, {len(words)} слов, GloVe 100d)\n")
out.append(f"Объяснённая дисперсия первых {K} компонент: **{var[:K].sum():.1%}** "
           f"(первые 3: {', '.join(f'{v:.1%}' for v in var[:3])}).\n")
out.append("Оси названы автоматически: слова на полюсах (отрицательный ← → положительный).\n")
for j in range(K):
    idx = np.argsort(z[:, j])
    neg = ", ".join(words[i] for i in idx[:TOP])
    posw = ", ".join(words[i] for i in idx[::-1][:TOP])
    out.append(f"## Ось {j + 1}\n- **−:** {neg}\n- **+:** {posw}\n")

alive = np.abs(z) > ALIVE
out.append("## Профиль применимости по частям речи\n")
out.append(f"Доля слов, у которых ось «живая» (|z| > {ALIVE}), по классам WordNet. "
           "Если части речи флюидны, различий почти нет.\n")
classes = ["noun", "verb", "adj", "adv"]
out.append("| Ось | " + " | ".join(classes) + " |")
out.append("| :-- | " + " | ".join(["--:"] * len(classes)) + " |")
for j in range(K):
    cells = [f"{alive[pos == c, j].mean():.0%}" for c in classes]
    out.append(f"| {j + 1} | " + " | ".join(cells) + " |")
n_alive = alive.sum(axis=1)
out.append("")
out.append("Среднее число живых осей на слово: " + ", ".join(
    f"{c} {n_alive[pos == c].mean():.1f}" for c in classes) + ".\n")

# how well do alive-profiles separate POS? nearest-centroid accuracy on |z|
feats = np.abs(z)
cent = {c: feats[pos == c].mean(axis=0) for c in classes}
pred = np.array([min(classes, key=lambda c: np.linalg.norm(f - cent[c])) for f in feats])
acc = (pred == pos).mean()
base = max((pos == c).mean() for c in classes)
out.append(f"Классификация POS по профилю (ближайший центроид): {acc:.0%} при базовом уровне {base:.0%}.\n")

(ROOT / "data" / f"axes_nano{K}_en.md").write_text("\n".join(out), encoding="utf-8")
print("\n".join(out))
