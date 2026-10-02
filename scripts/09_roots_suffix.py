"""Roots chosen by meaning only + Esperanto-style POS suffix (-o noun, -i verb, -a adj, -e adv).

Form subspace F (3 LDA directions) is projected out before choosing roots, so roots are
POS-neutral concepts. A word is coded as root + suffix (2 bits) + u universal meaning axes.
The suffix is reconstructed as the mean position of its POS class in the form subspace.
Compared with the earlier scheme (07): root + 3 continuous form axes + u universal axes,
and with global axes, at equal bits per word.
"""
import os
import sys

import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import RAW, ROOT, load_vectors, word_matrix
from lib_axes import (dequantize, fit_axes, generality, greedy_roots, make_wup, nearest_other,
                      quantize, recon_plain, recon_split, remove_freq, unit)

SRC = sys.argv[1] if len(sys.argv) > 1 else "numberbatch"
MODE = sys.argv[2] if len(sys.argv) > 2 else "word"   # "word": one vector per word; "sense": POS entries
HOMOGRAPHS = ["march", "rent", "issue", "point", "order", "close", "work", "play", "love", "pretty"]
CONFIGS = [(10, 3), (10, 6), (30, 3), (30, 6), (30, 9)]   # (roots, universal meaning axes)
SUFFIX = {"noun": "-o", "verb": "-i", "adj": "-a", "adv": "-e"}
NFORM, NCAND, SEED = 3, 300, 0
BITS = np.log2(11)
FIXED_WORDS = [w for w in os.environ.get("ROOTS_WORDS", "").split(",") if w]   # fixed root list instead of greedy
TAG = os.environ.get("ROOTS_TAG", "")
# gradient roots: "good:bad,big:small" = root word, opposite pole; one local axis from pole to pole
GRADIENT = [g.split(":") for g in os.environ.get("ROOTS_GRADIENT", "").split(",") if g]

if MODE == "sense":
    rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_sense.tsv")][1:]
    gen = np.array([float(r[3]) for r in rows])
    conv = np.unique([r[4] for r in rows], return_inverse=True)[1]   # WordNet-linked entries share an id
else:
    rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
group = np.unique(words, return_inverse=True)[1]          # entries of one word share a group
rng = np.random.default_rng(SEED)
gperm = rng.permutation(group.max() + 1)
train = np.flatnonzero(np.isin(group, gperm[: len(gperm) // 2]))
test = rng.permutation(np.flatnonzero(np.isin(group, gperm[len(gperm) // 2:])))[:600]

glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X0 = unit(np.load(RAW / "sense_numberbatch.npy")) if MODE == "sense" else unit(word_matrix(SRC, words))
X = remove_freq(X0, logfreq, train)
_, mean_wup = make_wup(words, pos)
if FIXED_WORDS:
    first = {}
    for i, w in enumerate(words):
        first.setdefault(w, i)
    FIXED = [first[w] for w in FIXED_WORDS if w in first]
    print("fixed roots found:", [words[i] for i in FIXED], "| missing:", [w for w in FIXED_WORDS if w not in first])
    CONFIGS = [(len(FIXED), 6), (len(FIXED), 9)]
NR = CONFIGS[-1][0]
cand = np.argsort(-(gen if MODE == "sense" else generality(words, pos, RAW / "generality_x5.npy")))[:NCAND]

sims_raw = X0[test] @ X0.T
sims_raw[group[None, :] == group[test][:, None]] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]


def evaluate(R):
    nn = nearest_other(R[test], X, test, 1, group)[:, 0]
    t50 = np.mean([d in s for d, s in zip(nn, true50)])
    return mean_wup(zip(test, nn)), float(np.mean(pos[nn] == pos[test])), float(t50)


# form subspace and POS-neutral meaning space
mean0 = X[train].mean(axis=0)
Xc = X - mean0
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(Xc[train], pos[train])
F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
f = Xc @ F
Xm = Xc - f @ F.T
Xm_n = unit(Xm)
S_m = Xm_n @ Xm_n.T
f_class = {p: f[train][pos[train] == p].mean(axis=0) for p in SUFFIX}
form_offset = np.stack([f_class[p] for p in pos]) @ F.T          # what the suffix contributes


LAST = {}   # (roots, axes) -> meaning scores of all entries, for printing axis poles


def recon_suffix(R_, u):
    roots = list(FIXED) if FIXED_WORDS else greedy_roots(S_m, train, cand, R_)
    if MODE == "sense":
        # entries linked as conversions (work-o / work-i) are assigned to one root by their mean vector
        G = np.zeros_like(Xm_n)
        np.add.at(G, conv, Xm_n)
        G = unit(G)[conv]
        assign = np.argmax(G @ Xm_n[roots].T, axis=1)
    else:
        assign = np.argmax(S_m[:, roots], axis=1)
    mu = np.stack([Xm[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0)
                   for r in range(R_)])
    Er = Xm - mu[assign]
    local = np.zeros_like(Er)       # reconstructed position on each root's own gradient axis
    if GRADIENT and FIXED_WORDS:
        for w1, w2 in GRADIENT:
            if w1 not in first or w2 not in first or first[w1] not in roots:
                continue
            r = roots.index(first[w1])
            g = Xm[first[w1]] - Xm[first[w2]]
            g /= np.linalg.norm(g)
            mem = np.flatnonzero(assign == r)
            c = Er[mem] @ g
            sd = c[np.isin(mem, train)].std()
            cq = dequantize(quantize(c[:, None], np.array([sd])), np.array([sd]))[:, 0]
            Er[mem] -= np.outer(c, g)
            local[mem] += np.outer(cq, g)
    mean_r, W = fit_axes("varimax", Er[train], u, np.random.default_rng(SEED))
    M = (Er - mean_r) @ W
    sm = M[train].std(axis=0)
    order = np.argsort(-sm)
    LAST[(R_, u)] = M[:, order]
    return mu[assign] + local + dequantize(quantize(M, sm), sm) @ W.T + mean_r + form_offset + mean0, roots, assign


def recon_continuous(R_, u):
    """Earlier scheme (07, local axes = 0): roots chosen on full vectors, 3 continuous form axes."""
    S = X @ X.T
    roots = list(FIXED) if FIXED_WORDS else greedy_roots(S, train, cand, R_)
    assign = np.argmax(S[:, roots], axis=1)
    mu = np.stack([X[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0)
                   for r in range(R_)])
    E = X - mu[assign]
    lda2 = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(E[train], pos[train])
    F2, _ = np.linalg.qr(lda2.scalings_[:, :NFORM])
    f2 = E @ F2
    Er = E - f2 @ F2.T
    mean_r, W = fit_axes("varimax", Er[train], u, np.random.default_rng(SEED))
    M = (Er - mean_r) @ W
    sf, sm = f2[train].std(axis=0), M[train].std(axis=0)
    return (mu[assign] + dequantize(quantize(f2, sf), sf) @ F2.T +
            dequantize(quantize(M, sm), sm) @ W.T + mean_r)


out = [f"# Корни по смыслу + суффикс части речи ({SRC}, режим {MODE}, {len(words)} записей)\n",
       "Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. "
       "Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. "
       "Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же "
       "длине кода.\n",
       "| схема | биты на слово | wup | pos | top50 |", "| :-- | --: | --: | --: | --: |"]
keep = {}
for R_, u in CONFIGS:
    Rs, roots, assign = recon_suffix(R_, u)
    bits_s = np.log2(R_) + 2 + u * BITS
    w_, p_, t_ = evaluate(Rs)
    out.append(f"| **корни {R_} + суффикс + {u} осей** | {bits_s:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    bits_c = np.log2(R_) + (NFORM + u) * BITS
    w_, p_, t_ = evaluate(recon_continuous(R_, u))
    out.append(f"| корни {R_} + 3 непрерывные формы + {u} осей | {bits_c:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    k = max(round(bits_s / BITS), 4)
    w_, p_, t_ = evaluate(recon_plain(X, train, k))
    out.append(f"| глобальные plain, {k} осей | {k * BITS:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    w_, p_, t_ = evaluate(recon_split(X, train, pos, k))
    out.append(f"| глобальные split (3+{k - 3}) | {k * BITS:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    keep[(R_, u)] = (roots, assign)

roots, assign = keep[(NR, 6)]
names = lambda r: words[roots[r]].upper()
if MODE == "sense":
    out.append("\n## Омонимы и конверсии: корень и суффикс записи\n")
    for w in HOMOGRAPHS:
        ids = [i for i in range(n) if words[i] == w]
        out.append(f"- **{w}**: " + "; ".join(f"{pos[i]} → {names(assign[i])}{SUFFIX[pos[i]]}" for i in ids))
out.append(f"\n## Корни ({NR}), выбранные по смыслу, и их формы\n")
out.append("Для каждого корня — ближайшие слова каждого суффикса.\n")
for r in np.argsort(-np.bincount(assign, minlength=NR))[:NR]:
    mem = np.flatnonzero(assign == r)
    parts = []
    for p, suf in SUFFIX.items():
        mp = mem[pos[mem] == p]
        mp = mp[np.argsort(-S_m[mp, roots[r]])][:3]
        if len(mp):
            parts.append(f"`{suf}` " + ", ".join(words[i] for i in mp))
    out.append(f"- **{words[roots[r]].upper()}** ({len(mem)}): " + "; ".join(parts))
out.append("\n## Универсальные смысловые оси (30 корней, 9 осей)\n")
out.append("Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. "
           "Знак и порядок осей нестабильны между запусками.\n")
M9 = LAST[(NR, 9)]
for j in range(M9.shape[1]):
    idx = np.argsort(M9[:, j])
    out.append(f"- M{j + 1}: **−** " + ", ".join(words[i] for i in idx[:7]) +
               "  /  **+** " + ", ".join(words[i] for i in idx[::-1][:7]))
text = "\n".join(out)
(ROOT / "data" / f"roots_suffix_{SRC}_{MODE}{TAG}.md").write_text(text, encoding="utf-8")
print(text)
