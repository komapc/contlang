"""Remove frequency/style artifacts from the embedding before axis discovery and compare.

Variants of the vectors:
  raw    original vectors
  freq   direction that predicts log word frequency (ridge regression on train) projected out
  abtt   "all-but-the-top": mean removed, top D principal components projected out
  both   freq then abtt
Per variant and k: correlation of axes with frequency, coherence of axis poles (measured in the
RAW space so variants are comparable), and the round trip (wup / POS / top50 in the raw space).
"""
import sys

import numpy as np
from scipy.stats import spearmanr

from common import ROOT, load_vectors, word_matrix
from lib_axes import dequantize, fit_axes, make_wup, nearest_other, quantize

LIST = "wordlist_en_x5.tsv"
SRC = sys.argv[1] if len(sys.argv) > 1 else "numberbatch"
KS = [10, 30]
D = 3          # components removed by abtt
RIDGE = 10.0
POLE = 10      # words per pole for coherence
SEED = 0

rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / LIST)][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
rng = np.random.default_rng(SEED)
perm = rng.permutation(n)
train, test = perm[: n // 2], perm[n // 2:][:600]

glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))  # higher = more frequent
logfreq = (logfreq - logfreq.mean()) / logfreq.std()

X0 = word_matrix(SRC, words)
X0 = X0 / np.linalg.norm(X0, axis=1, keepdims=True)
_, mean_wup = make_wup(words, pos)


def unit(X):
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def remove_freq(X):
    mu = X[train].mean(axis=0)
    Xc = X[train] - mu
    w = np.linalg.solve(Xc.T @ Xc + RIDGE * np.eye(X.shape[1]), Xc.T @ logfreq[train])
    u = w / np.linalg.norm(w)
    return unit(X - np.outer(X @ u, u))


def abtt(X):
    mu = X[train].mean(axis=0)
    _, _, vt = np.linalg.svd(X[train] - mu, full_matrices=False)
    P = vt[:D]
    Xc = X - mu
    return unit(Xc - Xc @ P.T @ P)


variants = {"raw": X0, "freq": remove_freq(X0), "abtt": abtt(X0)}
variants["both"] = abtt(remove_freq(X0))

# reference quantities in the RAW space
sims_raw = X0[test] @ X0.T
sims_raw[np.arange(len(test)), test] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]
rand_idx = [rng.choice(n, POLE, replace=False) for _ in range(200)]
rand_coh = np.mean([(X0[i] @ X0[i].T)[np.triu_indices(POLE, 1)].mean() for i in rand_idx])


def coherence(scores):
    """Mean pairwise raw-space cosine of the POLE extreme words at each end of each axis."""
    vals = []
    for j in range(scores.shape[1]):
        idx = np.argsort(scores[:, j])
        for ids in (idx[:POLE], idx[::-1][:POLE]):
            vals.append((X0[ids] @ X0[ids].T)[np.triu_indices(POLE, 1)].mean())
    return float(np.mean(vals))


out = [f"# Чистка осей ({SRC}, {n} слов)\n",
       "Варианты векторов: **raw** — как есть; **freq** — вычтено направление частотности; "
       f"**abtt** — вычтены среднее и {D} главные компоненты; **both** — оба.\n",
       "- **|ρ| freq** — средняя / максимальная |корреляция Спирмена| оси с частотностью слова (ранг в GloVe);\n"
       f"- **coherence** — средний косинус (в raw-пространстве) между {POLE} крайними словами на полюсах; "
       f"для случайных слов {rand_coh:.3f};\n"
       "- **wup / pos / top50** — round trip (слово → k осей → ближайшее другое слово): WordNet-сходство, "
       "совпадение части речи, попадание в 50 истинных соседей по raw-пространству.\n",
       "| вариант | k | \\|ρ\\| freq (сред / макс) | coherence | wup | pos | top50 |",
       "| :-- | --: | :-- | --: | --: | --: | --: |"]
poles_out = {}
for name, X in variants.items():
    for k in KS:
        mean, W = fit_axes("varimax", X[train], k, np.random.default_rng(SEED + k))
        scores = (X - mean) @ W
        order = np.argsort(-scores.std(axis=0))
        scores, W = scores[:, order], W[:, order]
        rho = np.array([abs(spearmanr(scores[:, j], logfreq).statistic) for j in range(k)])
        std = scores[train].std(axis=0)
        R = dequantize(quantize(scores[test], std), std) @ W.T + mean
        nn = nearest_other(R, X, test, 1)[:, 0]
        t50 = np.mean([d in s for d, s in zip(nn, true50)])
        out.append(f"| {name} | {k} | {rho.mean():.2f} / {rho.max():.2f} | {coherence(scores):.3f} | "
                   f"{mean_wup(zip(test, nn)):.3f} | {np.mean(pos[nn] == pos[test]):.0%} | {t50:.0%} |")
        if k == 10:
            lines = []
            for j in range(k):
                idx = np.argsort(scores[:, j])
                lines.append(f"{j + 1}. **−** " + ", ".join(words[i] for i in idx[:8]) +
                             "  /  **+** " + ", ".join(words[i] for i in idx[::-1][:8]))
            poles_out[name] = lines

out.append("")
for name in ("raw", "both"):
    out.append(f"## Оси nano-10, вариант {name}\n")
    out.extend(poles_out[name])
    out.append("")
text = "\n".join(out)
(ROOT / "data" / f"clean_axes_{SRC}.md").write_text(text, encoding="utf-8")
print(text)
