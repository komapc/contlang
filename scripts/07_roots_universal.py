"""Roots + UNIVERSAL axes (+ at most one local axis per root).

Code of a word: root (log2 R bits) + 3 form axes + u universal meaning axes + 0/1 local axis.
Form and meaning axes are fitted on the pooled deviations of words from their root-cluster mean,
so they mean the same thing for every root. Variant 'mask': each root uses only its a most
active universal axes (the others are not coded).
Compared with global axes (plain, split form+meaning) at equal bits per word.
"""
import sys

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import RAW, ROOT, load_vectors, word_matrix
from lib_axes import (dequantize, fit_axes, generality, greedy_roots, make_wup, nearest_other,
                      quantize, recon_plain, recon_split, remove_freq, unit)

LIST = "wordlist_en_x5.tsv"
SRC = sys.argv[1] if len(sys.argv) > 1 else "numberbatch"
# (roots, universal meaning axes, local axes 0/1, active axes per root or None)
CONFIGS = [(10, 3, 0, None), (10, 6, 0, None), (30, 3, 0, None), (30, 6, 0, None),
           (30, 6, 1, None), (30, 9, 0, None), (30, 9, 1, None), (30, 9, 0, 4), (30, 12, 0, 4)]
NFORM = 3
NCAND = 300
BITS = np.log2(11)
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
cand = np.argsort(-generality(words, pos, RAW / "generality_x5.npy"))[:NCAND]
S_all = X @ X.T

sims_raw = X0[test] @ X0.T
sims_raw[np.arange(len(test)), test] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]


def evaluate(R):
    nn = nearest_other(R[test], X, test, 1)[:, 0]
    t50 = np.mean([d in s for d, s in zip(nn, true50)])
    return mean_wup(zip(test, nn)), float(np.mean(pos[nn] == pos[test])), float(t50)


def recon(R_, u, local, active):
    roots = greedy_roots(S_all, train, cand, R_)
    assign = np.argmax(S_all[:, roots], axis=1)
    mu = np.stack([X[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0)
                   if len(np.intersect1d(np.flatnonzero(assign == r), train)) else X[roots[r]]
                   for r in range(R_)])
    E = X - mu[assign]                                  # deviation from the root cluster
    lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(E[train], pos[train])
    F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
    f = E @ F
    Er = E - f @ F.T
    mean_r, W = fit_axes("varimax", Er[train], u, np.random.default_rng(SEED))
    M = (Er - mean_r) @ W
    sf, sm = f[train].std(axis=0), M[train].std(axis=0)
    Qm = dequantize(quantize(M, sm), sm)
    if active:                                          # each root keeps its `active` busiest axes
        mask = np.zeros((R_, u))
        for r in range(R_):
            tr = np.intersect1d(np.flatnonzero(assign == r), train)
            if len(tr) < 2:
                mask[r, :active] = 1
            else:
                mask[r, np.argsort(-M[tr].std(axis=0))[:active]] = 1
        Qm = Qm * mask[assign]
    Rec = mu[assign] + dequantize(quantize(f, sf), sf) @ F.T + Qm @ W.T + mean_r
    if local:                                           # one extra axis per root, from what is left
        left = Er - (M @ W.T)
        for r in range(R_):
            mem = np.flatnonzero(assign == r)
            tr = np.intersect1d(mem, train)
            if len(tr) < 3:
                continue
            _, _, vt = np.linalg.svd(left[tr] - left[tr].mean(axis=0), full_matrices=False)
            w = vt[0]
            s = left[mem] @ w
            sd = (left[tr] @ w).std() + 1e-9
            Rec[mem] += np.outer(dequantize(quantize(s, sd), sd), w)
    return Rec, roots


out = [f"# Корни + универсальные оси ({SRC}, {n} слов, частотность вычтена)\n",
       "Код слова: корень (log2 R бит) + 3 оси формы + u универсальных смысловых осей + 0/1 локальная "
       "ось на корень. Универсальные оси найдены по отклонениям слов от центра своего корня (пулом по всем "
       "корням), поэтому значат одно и то же для любого корня. `mask a` — корень использует только "
       "a наиболее активных универсальных осей (остальные не кодируются). Сравнение с глобальными осями "
       "при той же длине кода в битах.\n",
       "«Осей в языке» — сколько разных осей надо определить: форма + универсальные + локальные "
       "(по одной на корень).\n",
       "| схема | биты на слово | осей в языке | wup | pos | top50 |", "| :-- | --: | --: | --: | --: | --: |"]
for R_, u, local, active in CONFIGS:
    Rec, roots = recon(R_, u, local, active)
    coded = (active or u) + NFORM + local
    bits = np.log2(R_) + coded * BITS
    n_axes = NFORM + u + local * R_
    name = f"корни {R_} + форма 3 + универс. {u}" + (f" (mask {active})" if active else "") \
        + (" + локальная 1" if local else "")
    w_, p_, t_ = evaluate(Rec)
    out.append(f"| {name} | {bits:.1f} | {n_axes} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    k = max(round(bits / BITS), 4)
    w_, p_, t_ = evaluate(recon_plain(X, train, k))
    out.append(f"| — глобальные plain, {k} осей | {k * BITS:.1f} | {k} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    w_, p_, t_ = evaluate(recon_split(X, train, pos, k))
    out.append(f"| — глобальные split (3+{k - 3}) | {k * BITS:.1f} | {k} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
text = "\n".join(out)
(ROOT / "data" / f"roots_universal_{SRC}.md").write_text(text, encoding="utf-8")
print(text)
