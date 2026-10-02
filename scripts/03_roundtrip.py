"""Word-level round trip: word -> k quantized axes -> nearest word.

For each embedding source and k, compares PCA, PCA+varimax and random axes.
Axes are fitted on a train split and evaluated on held-out words.
External check: Spearman correlation of axis-space cosine with WordNet Wu-Palmer
similarity on same-POS word pairs (independent of the embedding source).
"""
import sys

import numpy as np
from scipy.stats import spearmanr

from common import ROOT, SOURCES, load_wordnet, word_matrix

LIST = sys.argv[1] if len(sys.argv) > 1 else "wordlist_en_x5.tsv"
KS = [10, 30, 100]
SEED = 0
LEVELS = 5  # quantized values are -5..+5 (11 levels)
CLIP = 2.5  # z-scores are clipped to +-CLIP then mapped to +-LEVELS


def varimax(phi, iters=100, tol=1e-6):
    p, k = phi.shape
    rot, d = np.eye(k), 0.0
    for _ in range(iters):
        lam = phi @ rot
        u, s, vt = np.linalg.svd(
            phi.T @ (lam ** 3 - lam @ np.diag((lam ** 2).sum(axis=0)) / p))
        rot = u @ vt
        if s.sum() < d * (1 + tol):
            break
        d = s.sum()
    return phi @ rot


def fit_axes(method, Xtr, k, rng):
    """Orthonormal axes W (dim x k), ordered by variance carried (random: arbitrary)."""
    mean = Xtr.mean(axis=0)
    if method == "random":
        W, _ = np.linalg.qr(rng.standard_normal((Xtr.shape[1], k)))
        return mean, W
    _, _, vt = np.linalg.svd(Xtr - mean, full_matrices=False)
    W = vt[:k].T
    if method == "varimax":
        W = varimax(W)
    return mean, W


def quantize(scores, std):
    z = np.clip(scores / std, -CLIP, CLIP)
    return np.round(z / CLIP * LEVELS)


def dequantize(q, std):
    return q / LEVELS * CLIP * std


def topk_cos(R, Xn, k):
    Rn = R / np.linalg.norm(R, axis=1, keepdims=True)
    sims = Rn @ Xn.T
    return sims, np.argsort(-sims, axis=1)[:, :k]


rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / LIST)][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
rng = np.random.default_rng(SEED)
perm = rng.permutation(n)
train, test = perm[: n // 2], perm[n // 2:]

# fixed same-POS word pairs with WordNet similarity (shared by all sources)
wn = load_wordnet()
tag = {"noun": "n", "verb": "v"}
pairs, sims_wn = [], []
for _ in range(6000):
    p = rng.choice(["noun", "verb"])
    idx = np.flatnonzero(pos == p)
    i, j = rng.choice(idx, 2, replace=False)
    si, sj = wn.synsets(words[i], tag[p]), wn.synsets(words[j], tag[p])
    if si and sj:
        v = si[0].wup_similarity(sj[0])
        if v is not None:
            pairs.append((i, j)); sims_wn.append(v)
pairs, sims_wn = np.array(pairs), np.array(sims_wn)

out = [f"# Round-trip: слово → k осей (11 уровней) → слово\n",
       f"{n} слов ({len(train)} train / {len(test)} test), кандидаты для декодирования — все {n}. "
       f"Пар для WordNet-корреляции: {len(pairs)}.\n",
       "Метрики на test: **top1 / top10** — доля слов, декодированных точно / в десятке; "
       "**nn@10** — доля истинных 10 соседей слова (в полном пространстве), найденных среди "
       "10 соседей реконструкции; **wn ρ** — корреляция Спирмена косинуса в пространстве осей "
       "с WordNet Wu-Palmer (для полного пространства — в строке `full`).\n"]

for src in SOURCES:
    X = word_matrix(src, words)
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    Xtr = X[train]
    cos_full = np.sum(X[pairs[:, 0]] * X[pairs[:, 1]], axis=1)
    rho_full = spearmanr(cos_full, sims_wn).statistic
    _, true_nn = topk_cos(X[test], X, 11)           # includes the word itself
    true_nn = np.array([[j for j in row if j != t][:10] for row, t in zip(true_nn, test)])
    out.append(f"## {src}\n")
    out.append(f"`full` (без сжатия): wn ρ = {rho_full:.3f}\n")
    out.append("| k | метод | top1 | top10 | nn@10 | wn ρ |")
    out.append("| --: | :-- | --: | --: | --: | --: |")
    for k in KS:
        for method in ["pca", "varimax", "random"]:
            mean, W = fit_axes(method, Xtr, k, np.random.default_rng(SEED + k))
            std = ((Xtr - mean) @ W).std(axis=0)
            Q = quantize((X - mean) @ W, std)       # the "min-co" representation
            R = dequantize(Q, std) @ W.T + mean
            _, nn = topk_cos(R[test], X, 11)
            top1 = np.mean(nn[:, 0] == test)
            top10 = np.mean([t in row[:10] for row, t in zip(nn, test)])
            nn10 = np.mean([len(set(row_nn) & set(j for j in row if j != t) ) / 10
                            for row_nn, row, t in zip(true_nn, nn, test)])
            Rn = R / np.linalg.norm(R, axis=1, keepdims=True)
            rho = spearmanr(np.sum(Rn[pairs[:, 0]] * Rn[pairs[:, 1]], axis=1), sims_wn).statistic
            out.append(f"| {k} | {method} | {top1:.1%} | {top10:.1%} | {nn10:.1%} | {rho:.3f} |")
    out.append("")

text = "\n".join(out)
(ROOT / "data" / "roundtrip_en.md").write_text(text, encoding="utf-8")
print(text)
