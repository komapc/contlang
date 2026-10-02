"""Separate form (part-of-speech-like directions) from meaning axes.

Form:    3 LDA directions fitted on the dominant-POS labels (4 classes), train split.
Meaning: PCA+varimax in the orthogonal complement of the form subspace.
Vectors are frequency-cleaned first (see 04_clean_axes.py).

Compared at equal code length: split (3 form + k-3 meaning) vs plain varimax with k axes.
'POS leakage' = nearest-centroid POS accuracy from the meaning coordinates only (lower = cleaner).
"""
import sys

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import ROOT, load_vectors, word_matrix
from lib_axes import (dequantize, fit_axes, make_wup, nearest_other, quantize, remove_freq,
                      unit)

LIST = "wordlist_en_x5.tsv"
SRC = sys.argv[1] if len(sys.argv) > 1 else "numberbatch"
TOTALS = [10, 30]
NFORM = 3
POLE = 10
SEED = 0

rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / LIST)][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
rng = np.random.default_rng(SEED)
perm = rng.permutation(n)
train, test = perm[: n // 2], perm[n // 2:][:600]

glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()

X0 = unit(word_matrix(SRC, words))
X = remove_freq(X0, logfreq, train)
_, mean_wup = make_wup(words, pos)
classes = sorted(set(pos))

sims_raw = X0[test] @ X0.T
sims_raw[np.arange(len(test)), test] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]


def pos_accuracy(F):
    """Nearest-centroid POS accuracy on test using coordinates F (standardized on train)."""
    mu, sd = F[train].mean(axis=0), F[train].std(axis=0) + 1e-9
    Z = (F - mu) / sd
    cent = {c: Z[train][pos[train] == c].mean(axis=0) for c in classes}
    pred = np.array([min(classes, key=lambda c: np.linalg.norm(z - cent[c])) for z in Z[test]])
    return float(np.mean(pred == pos[test]))


def coherence(scores):
    vals = []
    for j in range(scores.shape[1]):
        idx = np.argsort(scores[:, j])
        for ids in (idx[:POLE], idx[::-1][:POLE]):
            vals.append((X0[ids] @ X0[ids].T)[np.triu_indices(POLE, 1)].mean())
    return float(np.mean(vals))


def evaluate(R, nn_pool=X):
    nn = nearest_other(R[test], nn_pool, test, 1)[:, 0]
    t50 = np.mean([d in s for d, s in zip(nn, true50)])
    return mean_wup(zip(test, nn)), float(np.mean(pos[nn] == pos[test])), float(t50)


def poles(scores, names=None, top=8):
    lines = []
    for j in range(scores.shape[1]):
        idx = np.argsort(scores[:, j])
        lines.append(f"{j + 1}. **−** " + ", ".join(words[i] for i in idx[:top]) +
                     "  /  **+** " + ", ".join(words[i] for i in idx[::-1][:top]))
    return lines


# form subspace: LDA directions on train, orthonormalized
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(X[train], pos[train])
Fdir, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
mean0 = X[train].mean(axis=0)
Xc = X - mean0
fscores = Xc @ Fdir
Xr = Xc - fscores @ Fdir.T                    # meaning residual, orthogonal to the form subspace

out = [f"# Форма и смысл ({SRC}, {n} слов, частотность вычтена)\n",
       f"Форма: {NFORM} LDA-направления по частям речи (train). Смысл: PCA+varimax в ортогональном "
       "дополнении к форме. Сравнение при одинаковой длине кода.\n",
       f"Форма сама по себе предсказывает часть речи на test: **{pos_accuracy(fscores):.0%}** "
       f"(базовый уровень {max((pos == c).mean() for c in classes):.0%}).\n",
       "- **leakage** — точность предсказания части речи только по смысловым координатам (меньше = чище);\n"
       "- **coherence** — связность полюсов смысловых осей (в raw-пространстве; случайные слова ≈ 0.04);\n"
       "- **wup / pos / top50** — round trip по всему коду (форма + смысл).\n",
       "| схема | длина кода | leakage | coherence | wup | pos | top50 |",
       "| :-- | --: | --: | --: | --: | --: | --: |"]
examples = {}
for total in TOTALS:
    # plain: total axes, no form split
    mean, W = fit_axes("varimax", X[train], total, np.random.default_rng(SEED + total))
    S = (X - mean) @ W
    std = S[train].std(axis=0)
    R = dequantize(quantize(S, std), std) @ W.T + mean
    w_, p_, t_ = evaluate(R)
    out.append(f"| plain | {total} | {pos_accuracy(S):.0%} | {coherence(S):.3f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    if total == 10:
        examples["plain"] = poles(S)
    # split: NFORM form + (total - NFORM) meaning
    k = total - NFORM
    mean_r, Wm = fit_axes("varimax", Xr[train], k, np.random.default_rng(SEED + total))
    M = (Xr - mean_r) @ Wm
    order = np.argsort(-M.std(axis=0))
    M, Wm = M[:, order], Wm[:, order]
    sf, sm = fscores[train].std(axis=0), M[train].std(axis=0)
    R = (dequantize(quantize(fscores, sf), sf) @ Fdir.T +
         dequantize(quantize(M, sm), sm) @ Wm.T + mean0 + mean_r)
    w_, p_, t_ = evaluate(R)
    out.append(f"| split ({NFORM}+{k}) | {total} | {pos_accuracy(M):.0%} | {coherence(M):.3f} | "
               f"{w_:.3f} | {p_:.0%} | {t_:.0%} |")
    if total == 10:
        examples["split"] = poles(M)
        examples["form"] = poles(fscores)

out.append("")
out.append("## Форма: 3 оси (слова на полюсах)\n")
out.extend(examples["form"])
out.append("\n## Смысловые оси при коде 10 (7 осей смысла)\n")
out.extend(examples["split"])
out.append("\n## Для сравнения: plain, 10 осей\n")
out.extend(examples["plain"])
text = "\n".join(out)
(ROOT / "data" / f"form_meaning_{SRC}.md").write_text(text, encoding="utf-8")
print(text)
