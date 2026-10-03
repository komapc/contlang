"""Choose K root words to maximize mean best cosine of words to their root (axes ignored).

Task A: gradient pole words (good/bad, big/small, ...) are not candidates.
Task B: poles are candidates; a pole root gets one free axis (its pole direction is projected out of the
        similarity), with a budget `a` on how many pole roots may be used.
Engine: p-median MILP (HiGHS) on a sparse neighbour graph (m nearest candidates per word); words with no
selected neighbour are bounded by their m-th neighbour similarity, so the model optimum is an upper bound.
The chosen set is re-scored on the full similarity matrix (lower bound). Also greedy and greedy+swap, and a
bootstrap of greedy+swap for stability. Selection uses all words (no split).
"""
import sys
import time

import numpy as np
import scipy.sparse as sp
from scipy.optimize import Bounds, LinearConstraint, milp
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import ROOT, load_vectors, word_matrix
from lib_axes import remove_freq, unit

NFORM, M_NEIGH, TIME_LIMIT, NBOOT = 3, 30, 240, 20
PAIRS = [p.split(":") for p in ("good:bad big:small near:far above:below live:die same:different maybe:true "
         "hot:cold fast:slow strong:weak rich:poor happy:sad love:hate win:lose increase:decrease open:close "
         "many:few always:never early:late high:low easy:difficult").split()]
POLES = {w for p in PAIRS for w in p}
NSM = "someone thing people body kind part word happen move think know want feel see hear touch place inside side good big near above live same maybe time".split()

rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
idx = {w: i for i, w in enumerate(words)}
pairs = [(idx[a], idx[b]) for a, b in PAIRS if a in idx and b in idx]
pole_idx = np.array(sorted({i for p in pairs for i in p}))
glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X0 = unit(word_matrix("numberbatch", words))
allw = np.arange(n)
X = remove_freq(X0, logfreq, allw)
Xc = X - X.mean(axis=0)
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(Xc, pos)
F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
Xm = Xc - (Xc @ F) @ F.T
Xn = unit(Xm)
S_A = Xn @ Xn.T
S_B = S_A.copy()
for a, b in pairs:                       # a pole word as root: its axis is free (direction projected out)
    d = Xm[a] - Xm[b]
    d /= np.linalg.norm(d)
    P = unit(Xm - np.outer(Xm @ d, d))
    line = P @ P[a]
    S_B[:, a] = line
    S_B[:, b] = line


def score(S, R, rows_=None):
    rows_ = allw if rows_ is None else rows_
    return float(S[np.ix_(rows_, R)].max(axis=1).mean())


def greedy(S, rows_, pool, K):
    best = np.full(len(rows_), -1.0)
    St = S[rows_]
    chosen = []
    for _ in range(K):
        gains = np.maximum(best[:, None], St[:, pool]).sum(axis=0)
        c = pool[int(np.argmax(gains))]
        chosen.append(c)
        best = np.maximum(best, St[:, c])
    return chosen


def swap(S, rows_, pool, R, max_pass=30):
    R = list(R)
    St = S[rows_]
    cur = St[:, R].max(axis=1).mean()
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


def solve_milp(S, cand, K, budget=None):
    """p-median on the m-nearest-candidate graph. Returns (set, model upper bound, status)."""
    nc = len(cand)
    Sc = S[:, cand]
    m = min(M_NEIGH, nc)
    top = np.argsort(-Sc, axis=1)[:, :m]
    sims = np.take_along_axis(Sc, top, axis=1)
    slack = sims[:, -1]
    nx = n * m
    ci = np.concatenate([np.zeros(nc), sims.ravel(), slack]) / n
    # equality rows: sum_c x_wc + z_w = 1
    r = np.repeat(np.arange(n), m)
    A_eq = sp.vstack([sp.hstack([sp.csr_matrix((n, nc)), sp.csr_matrix((np.ones(nx), (r, np.arange(nx)))), sp.identity(n)]),
                      sp.hstack([sp.csr_matrix(np.ones((1, nc))), sp.csr_matrix((1, nx + n))])]).tocsr()
    b_eq = np.concatenate([np.ones(n), [K]])
    # linking: x_wc - y_c <= 0
    A_link = sp.hstack([sp.csr_matrix((-np.ones(nx), (np.arange(nx), top.ravel()))), sp.identity(nx), sp.csr_matrix((nx, n))]).tocsr()
    cons = [LinearConstraint(A_eq, b_eq, b_eq), LinearConstraint(A_link, -np.inf, 0)]
    if budget is not None:
        pole_mask = np.isin(cand, pole_idx).astype(float)
        row = sp.csr_matrix(np.concatenate([pole_mask, np.zeros(nx + n)])[None, :])
        cons.append(LinearConstraint(row, 0, budget))
    integrality = np.concatenate([np.ones(nc), np.zeros(nx + n)])
    res = milp(-ci, constraints=cons, integrality=integrality, bounds=Bounds(0, 1),
               options={"time_limit": TIME_LIMIT, "disp": False})
    if res.x is None:
        return None, None, res.message
    R = cand[np.flatnonzero(res.x[:nc] > 0.5)]
    ub = -res.mip_dual_bound if res.mip_dual_bound is not None else None
    return [int(i) for i in R], ub, res.message


def jaccard(sets):
    v = [len(a & b) / len(a | b) for i, a in enumerate(sets) for b in sets[i + 1:]]
    return float(np.mean(v))


cand_A = np.array([i for i in range(n) if words[i] not in POLES])
cand_B = allw
out = ["# Оптимизация выбора корней: MILP, жадный, обмены (оси игнорируются)", "",
       f"Цель: максимизировать среднее по {n} словам лучшее косинусное сходство слова с корнем (пространство без частотности и формы). Выбор по всем словам. MILP — p-median (HiGHS, {M_NEIGH} ближайших кандидатов на слово, лимит {TIME_LIMIT} с); «верхняя граница» — оптимум модели (не меньше настоящего оптимума), «MILP (настоящее)» — найденный набор, пересчитанный по полной матрице.",
       "A: слова-полюса градиентов (good/bad, big/small, …) не кандидаты. B: допускаются, у корня-полюса одна ось «бесплатна»; `a` — бюджет полюсов-корней.", ""]
runs = [("A", S_A, cand_A, 30, None), ("A", S_A, cand_A, 36, None),
        ("B", S_B, cand_B, 30, 0), ("B", S_B, cand_B, 30, 2), ("B", S_B, cand_B, 30, 4), ("B", S_B, cand_B, 30, 8),
        ("B", S_B, cand_B, 30, None), ("B", S_B, cand_B, 36, None)]
sets_out = {}
out += ["| задача | K | бюджет a | greedy | greedy+swap | MILP (настоящее) | верхняя граница | полюсов в наборе |", "| :-- | --: | --: | --: | --: | --: | --: | --: |"]
for task, S, cand, K, a in runs:
    t0 = time.time()
    g = greedy(S, allw, cand, K)
    if a is not None:                       # budget: greedy/swap restricted to non-poles when a == 0, else unrestricted reference
        pass
    sw = swap(S, allw, cand, g)
    R, ub, msg = solve_milp(S, cand, K, a)
    tru = score(S, R) if R else float("nan")
    npole = sum(i in set(pole_idx) for i in (R or []))
    out.append(f"| {task} | {K} | {'∞' if a is None else a} | {score(S, g):.4f} | {score(S, sw):.4f} | {tru:.4f} | {ub if ub is None else round(float(ub), 4)} | {npole} |")
    sets_out[(task, K, a)] = (R, sw)
    print(task, K, a, f"{time.time() - t0:.0f}s", msg[:60], flush=True)

out += ["", "## Наборы корней (MILP)", ""]
for (task, K, a), (R, sw) in sets_out.items():
    if R:
        out.append(f"- **{task}, K={K}, a={'∞' if a is None else a}:** " + ", ".join(words[i] for i in R))
ref = [idx[w] for w in NSM if w in idx]
out += ["", f"Для сравнения: набор NSM из {len(ref)} корней даёт сходство {score(S_B, ref):.4f} (B-сходство) и {score(S_A, ref):.4f} (A-сходство).", ""]

# bootstrap stability of greedy+swap, task A, K=30
rng = np.random.default_rng(0)
freq = np.zeros(n)
sets, oob = [], []
for _ in range(NBOOT):
    keep = np.sort(rng.choice(n, int(0.8 * n), replace=False))
    pool = np.array([i for i in cand_A if i in set(keep)])
    R = swap(S_A, keep, pool, greedy(S_A, keep, pool, 30))
    freq[R] += 1
    sets.append({words[i] for i in R})
    held = np.setdiff1d(allw, keep)
    oob.append(score(S_A, R, held))
top = np.argsort(-freq)[:40]
out += [f"## Устойчивость (бутстрап, {NBOOT} выборок по 80% слов, задача A, K=30, greedy+swap)", "",
        f"Среднее Жаккара между наборами: {jaccard(sets):.2f}; покрытие отложенных слов: {np.mean(oob):.4f} ± {np.std(oob):.4f}.", "",
        "Корни по частоте выбора: " + ", ".join(f"{words[i]} ({int(freq[i])})" for i in top if freq[i] > 0), ""]
text = "\n".join(out)
(ROOT / "data" / "roots_optimization.md").write_text(text, encoding="utf-8")
print(text)
