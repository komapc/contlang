"""Choose K root words to maximize similarity of words to their root (axes ignored).

Task A: plain coverage, gradient words (good/bad, big/small, ...) excluded from the pool.
Task B: gradient words allowed; a root with an antonym pole gets one free axis, i.e. similarity
        is measured after projecting out the pole direction (the axis is ignored, as it is coded separately).
Objective: mean over words of the best cosine to a root (form-removed, frequency-removed space).
Roots are chosen on train words only; coverage is reported on held-out words.
Algorithms: greedy over 300 general candidates (previous method), greedy over all train words,
greedy + swap local search (k-medoids style), and k-means centroids as an upper bound.
"""
import sys

import numpy as np
from sklearn.cluster import KMeans
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import RAW, ROOT, load_vectors, word_matrix
from lib_axes import generality, remove_freq, unit

KS = [30, 36]
SEEDS = [0, 1, 2, 3, 4]
NFORM = 3
PAIRS = [p.split(":") for p in ("good:bad big:small near:far above:below live:die same:different maybe:true "
         "hot:cold fast:slow strong:weak rich:poor happy:sad love:hate win:lose increase:decrease open:close "
         "many:few always:never early:late high:low easy:difficult").split()]
POLES = {w for p in PAIRS for w in p}

rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
idx = {w: i for i, w in enumerate(words)}
pairs = [(idx[a], idx[b]) for a, b in PAIRS if a in idx and b in idx]
group = np.unique(words, return_inverse=True)[1]
glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X0 = unit(word_matrix("numberbatch", words))
gen = generality(words, pos, RAW / "generality_x5.npy")
general_pool = np.argsort(-gen)[:300]


def similarity(seed, task):
    rng = np.random.default_rng(seed)
    gperm = rng.permutation(group.max() + 1)
    train = np.flatnonzero(np.isin(group, gperm[: len(gperm) // 2]))
    test = np.setdiff1d(np.arange(n), train)
    X = remove_freq(X0, logfreq, train)
    Xc = X - X[train].mean(axis=0)
    lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(Xc[train], pos[train])
    F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
    Xm = Xc - (Xc @ F) @ F.T
    Xn = unit(Xm)
    S = Xn @ Xn.T
    if task == "B":                     # a pole word as root: its axis is free (projected out)
        for a, b in pairs:
            d = Xm[a] - Xm[b]
            d /= np.linalg.norm(d)
            P = unit(Xm - np.outer(Xm @ d, d))
            line = P @ P[a]
            S[:, a] = line
            S[:, b] = line
    return S, train, test, Xn


def objective(S, rows_, R):
    return S[np.ix_(rows_, R)].max(axis=1).mean()


def greedy(S, train, pool, K):
    best = np.full(len(train), -1.0)
    chosen = []
    St = S[train]
    for _ in range(K):
        gains = np.maximum(best[:, None], St[:, pool]).sum(axis=0)
        c = pool[int(np.argmax(gains))]
        chosen.append(c)
        best = np.maximum(best, St[:, c])
    return chosen


def swap_search(S, train, pool, R, max_pass=20):
    R = list(R)
    St = S[train]
    cur = objective(S, train, R)
    for _ in range(max_pass):
        improved = False
        for j in range(len(R)):
            others = [r for k_, r in enumerate(R) if k_ != j]
            B = St[:, others].max(axis=1)
            vals = np.maximum(B[:, None], St[:, pool]).mean(axis=0)
            c = int(np.argmax(vals))
            if vals[c] > cur + 1e-9 and pool[c] not in others:
                R[j] = pool[c]
                cur = vals[c]
                improved = True
        if not improved:
            break
    return R


def jaccard(sets):
    v = [len(a & b) / len(a | b) for i, a in enumerate(sets) for b in sets[i + 1:]]
    return float(np.mean(v))


out = ["# Оптимизация выбора корней (оси игнорируются)", "",
       "Цель: максимизировать среднее по словам лучшее косинусное сходство слова с корнем (пространство без частотности и формы). Корни выбираются на обучающей половине слов (кандидаты — только обучающие слова), покрытие считается на отложенной половине; 5 разбиений. «Устойчивость» — среднее Жаккара наборов корней между разбиениями.",
       "Задача A: слова-полюса градиентов (good/bad, big/small, …) исключены из кандидатов. Задача B: допускаются; у корня-полюса одна ось «бесплатна» (направление к противоположному полюсу вычитается).", ""]
for task in ("A", "B"):
    for K in KS:
        res = {name: {"tr": [], "te": [], "sets": []} for name in ("greedy-300", "greedy-all", "greedy+swap", "k-means (центры)")}
        keep0 = {}
        for seed in SEEDS:
            S, train, test, Xn = similarity(seed, task)
            allowed = np.array([i for i in train if task == "B" or words[i] not in POLES])
            gpool = np.array([i for i in general_pool if i in set(allowed)])
            r1 = greedy(S, train, gpool, K)
            r2 = greedy(S, train, allowed, K)
            r3 = swap_search(S, train, allowed, r2)
            for name, R in (("greedy-300", r1), ("greedy-all", r2), ("greedy+swap", r3)):
                res[name]["tr"].append(objective(S, train, R))
                res[name]["te"].append(objective(S, test, R))
                res[name]["sets"].append({words[i] for i in R})
                if seed == 0:
                    keep0[name] = [words[i] for i in R]
            km = KMeans(n_clusters=K, n_init=3, random_state=seed).fit(Xn[train])
            C = unit(km.cluster_centers_)
            res["k-means (центры)"]["tr"].append((Xn[train] @ C.T).max(axis=1).mean())
            res["k-means (центры)"]["te"].append((Xn[test] @ C.T).max(axis=1).mean())
            print(task, K, seed, "done", flush=True)
        out += [f"## Задача {task}, K={K}", "", "| алгоритм | покрытие (обучение) | покрытие (отложенные) | устойчивость |", "| :-- | --: | --: | --: |"]
        for name, r in res.items():
            st = f"{jaccard(r['sets']):.2f}" if r["sets"] else "—"
            out.append(f"| {name} | {np.mean(r['tr']):.3f} | {np.mean(r['te']):.3f} | {st} |")
        out += ["", "Корни (разбиение 0): greedy+swap: " + ", ".join(keep0["greedy+swap"]), "",
                "greedy-300: " + ", ".join(keep0["greedy-300"]), ""]
text = "\n".join(out)
(ROOT / "data" / "roots_optimization.md").write_text(text, encoding="utf-8")
print(text)
