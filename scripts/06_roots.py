"""Roots + local features: word -> (root, m quantized local axes) -> nearest other word.

Roots are general words (WordNet: many hyponyms, nouns/verbs) chosen greedily to cover all words
(facility location on cosine similarity). Each root's cluster gets its own PCA axes.
Compared with global axes (plain, split form+meaning) at equal code length in bits.
"""
import sys

import numpy as np

from common import ROOT, load_vectors, load_wordnet, word_matrix
from lib_axes import (dequantize, make_wup, nearest_other, quantize, recon_plain, recon_split,
                      remove_freq, unit)

LIST = "wordlist_en_x5.tsv"
SRC = sys.argv[1] if len(sys.argv) > 1 else "numberbatch"
CONFIGS = [(10, 3), (10, 6), (30, 3), (30, 6), (30, 9)]   # (number of roots, local axes)
NCAND = 300
BITS_PER_AXIS = np.log2(11)
SEED = 0
NSM = """i you someone something thing people body kind part this same other one two much many
little few all good bad big small think know want feel see hear say word true do happen move
touch live die time now before after moment place here above below far near side inside if
because not maybe can very more like""".split()

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

# generality of a word = number of hyponyms of its dominant-POS first synset (nouns and verbs only)
wn = load_wordnet()
tag = {"noun": "n", "verb": "v"}
general = np.zeros(n)
for i, w in enumerate(words):
    if pos[i] in tag:
        syns = wn.synsets(w, tag[pos[i]])
        if syns:
            general[i] = len(set(syns[0].closure(lambda s: s.hyponyms())))
cand = np.argsort(-general)[:NCAND]

sims_raw = X0[test] @ X0.T
sims_raw[np.arange(len(test)), test] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]
S_all = X @ X.T


def greedy_roots(R, pool):
    """Greedy facility location over candidate pool, scored on the train words."""
    best = np.full(len(train), -1.0)
    chosen = []
    for _ in range(R):
        gains = [np.maximum(best, S_all[train][:, c]).sum() - best.sum() for c in pool]
        c = pool[int(np.argmax(gains))]
        chosen.append(c)
        best = np.maximum(best, S_all[train][:, c])
    return chosen


def recon_roots(roots, m):
    assign = np.argmax(S_all[:, roots], axis=1)
    R = np.zeros_like(X)
    for r in range(len(roots)):
        members = np.flatnonzero(assign == r)
        tr = np.intersect1d(members, train)
        if len(tr) < 2:
            R[members] = X[roots[r]]
            continue
        mu = X[tr].mean(axis=0)
        _, _, vt = np.linalg.svd(X[tr] - mu, full_matrices=False)
        W = vt[:m].T
        sc = (X[members] - mu) @ W
        std = ((X[tr] - mu) @ W).std(axis=0) + 1e-9
        R[members] = dequantize(quantize(sc, std), std) @ W.T + mu
    return R, assign


def evaluate(R):
    nn = nearest_other(R[test], X, test, 1)[:, 0]
    t50 = np.mean([d in s for d, s in zip(nn, true50)])
    return mean_wup(zip(test, nn)), float(np.mean(pos[nn] == pos[test])), float(t50)


out = [f"# Корни + локальные признаки ({SRC}, {n} слов, частотность вычтена)\n",
       f"Корни выбираются жадно (покрытие всех слов по косинусу) среди {NCAND} самых общих "
       "существительных и глаголов (по числу гипонимов в WordNet). У каждого корня свои "
       "локальные оси (PCA кластера). Сравнение при одинаковой длине кода в битах: "
       f"корень = log2(R) бит, координата = {BITS_PER_AXIS:.2f} бит (11 уровней).\n",
       "| схема | биты | wup | pos | top50 |", "| :-- | --: | --: | --: | --: |"]
detail = {}
for R_, m in CONFIGS:
    roots = greedy_roots(R_, cand)
    Rr, assign = recon_roots(roots, m)
    bits = np.log2(R_) + m * BITS_PER_AXIS
    w_, p_, t_ = evaluate(Rr)
    out.append(f"| корни {R_} + {m} локальных | {bits:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    k = max(round(bits / BITS_PER_AXIS), 4)
    w_, p_, t_ = evaluate(recon_plain(X, train, k))
    out.append(f"| глобальные plain, {k} осей | {k * BITS_PER_AXIS:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    w_, p_, t_ = evaluate(recon_split(X, train, pos, k))
    out.append(f"| глобальные split (3+{k - 3}) | {k * BITS_PER_AXIS:.1f} | {w_:.3f} | {p_:.0%} | {t_:.0%} |")
    detail[(R_, m)] = (roots, assign)

for R_ in (10, 30):
    roots, assign = detail[(R_, 3)]
    out.append(f"\n## Корни R={R_} (кластеры)\n")
    for r, c in enumerate(roots):
        mem = np.flatnonzero(assign == r)
        comp = ", ".join(f"{p} {np.mean(pos[mem] == p):.0%}" for p in ("noun", "verb", "adj", "adv"))
        near = mem[np.argsort(-S_all[mem, c])][1:7]
        out.append(f"- **{words[c]}** ({len(mem)} слов; {comp}): " + ", ".join(words[i] for i in near))

# coverage: NSM primes present in the list vs greedy roots of equal number
nsm = [words.index(w) for w in dict.fromkeys(NSM) if w in set(words)]
cov = lambda ids: float(S_all[:, ids].max(axis=1).mean())
ours = greedy_roots(len(nsm), cand)
out.append(f"\n## Покрытие: NSM против жадных корней\n")
out.append(f"Примитивов NSM в списке слов: {len(nsm)} ({', '.join(words[i] for i in nsm)}).\n")
out.append(f"Среднее максимальное косинусное сходство слова с ближайшим корнем: NSM **{cov(nsm):.3f}**, "
           f"жадные {len(nsm)} корней **{cov(ours):.3f}**, случайные {len(nsm)} слов "
           f"{np.mean([cov(list(rng.choice(n, len(nsm), replace=False))) for _ in range(50)]):.3f}.")
text = "\n".join(out)
(ROOT / "data" / f"roots_{SRC}.md").write_text(text, encoding="utf-8")
print(text)
