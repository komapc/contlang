"""Sparse coding (everything in roots) vs dense global axes, at comparable bits per word.

Word = head root + POS suffix + up to kmax modifiers; a modifier is a root used with a value on its own
axis (nonzero level; zero = not written). Variants (what the modifier directions are):
  S1  the 16 axis-roots, direction = difference of two pole words (readable, fixed)
  S2  any of the roots, direction = the root word itself (a second root as a modifier, signed value)
  S3  S1 + S2
  S0  9 data-fitted varimax axes coded sparsely (separates sparsity from readability)
Dense baseline: same roots + suffix + u varimax axes always written (as in 09).
"""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import ROOT, load_vectors, word_matrix
from lib_axes import dequantize, fit_axes, make_wup, nearest_other, quantize, remove_freq, unit

ROOTS = ("someone thing people body kind part word happen move think know want feel see hear touch place inside "
         "side say do good big near above live same maybe time sex many").split()
POLES = {"good": ("good", "bad"), "big": ("big", "small"), "near": ("near", "far"), "above": ("above", "below"),
         "live": ("live", "die"), "same": ("same", "different"), "maybe": ("certain", "impossible"),
         "time": ("future", "past"), "inside": ("inside", "outside"), "part": ("whole", "part"),
         "side": ("front", "back"), "hear": ("loud", "quiet"), "know": ("know", "ignorant"),
         "want": ("love", "hate"), "sex": ("male", "female"), "many": ("many", "few")}
SUFFIX = {"noun": "-o", "verb": "-i", "adj": "-a", "adv": "-e"}
NFORM, SEED, BITS = 3, 0, np.log2(11)
rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
group = np.unique(words, return_inverse=True)[1]
rng = np.random.default_rng(SEED)
gperm = rng.permutation(group.max() + 1)
train = np.flatnonzero(np.isin(group, gperm[: len(gperm) // 2]))
test = rng.permutation(np.flatnonzero(np.isin(group, gperm[len(gperm) // 2:])))[:600]

kv, glove = load_vectors("numberbatch"), load_vectors("glove100")
extra = list(ROOTS) + [w for p in POLES.values() for w in p]
extra = list(dict.fromkeys(extra))
X0 = unit(np.vstack([word_matrix("numberbatch", words), np.stack([kv[w] for w in extra])]))
logfreq = -np.log1p(np.array([glove.key_to_index.get(w, 400000) for w in words + extra]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X = remove_freq(X0, logfreq, train)
ex = {w: n + i for i, w in enumerate(extra)}
_, mean_wup = make_wup(words, pos)
sims_raw = X0[test] @ X0[:n].T
sims_raw[group[None, :] == group[test][:, None]] = -np.inf
true50 = [set(r[:50]) for r in np.argsort(-sims_raw, axis=1)]
Xw = X[:n]


def evaluate(R):
    nn = nearest_other(R[test], Xw, test, 1, group)[:, 0]
    return (mean_wup(zip(test, nn)), float(np.mean(pos[nn] == pos[test])),
            float(np.mean([d in s for d, s in zip(nn, true50)])))


mean0 = Xw[train].mean(axis=0)
Xc = X - mean0
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(Xc[:n][train], pos[train])
F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
f = Xc @ F
Xm_all = Xc - f @ F.T
Xm = Xm_all[:n]
Xm_n = unit(Xm_all)
f_class = {p: f[:n][train][pos[train] == p].mean(axis=0) for p in SUFFIX}
form_offset = np.stack([f_class[p] for p in pos]) @ F.T
root_idx = [ex[w] for w in ROOTS]
R_ = len(ROOTS)
assign = np.argmax(Xm_n[:n] @ Xm_n[root_idx].T, axis=1)
mu = np.stack([Xm[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0)
               if np.any(assign[train] == r) else Xm_all[root_idx[r]] for r in range(R_)])
Er = Xm - mu[assign]
base = mu[assign] + form_offset + mean0
print("root sizes:", dict(zip(ROOTS, np.bincount(assign, minlength=R_))))


def sparse_code(G, kmax):
    """Greedy matching pursuit; each step adds the modifier with the largest error reduction (nonzero level)."""
    sd = (Er[train] @ G.T).std(axis=0)
    r, A = Er.copy(), np.zeros_like(Er)
    used = np.zeros((n, len(G)), bool)
    nmod = np.zeros(n)
    for _ in range(kmax):
        c = r @ G.T
        a = dequantize(quantize(c, sd), sd)
        red = a * (2 * c - a)
        red[used] = -np.inf
        red[a == 0] = -np.inf
        j = np.argmax(red, axis=1)
        ok = red[np.arange(n), j] > 0
        step = np.zeros_like(Er)
        step[ok] = a[ok, j[ok]][:, None] * G[j[ok]]
        r -= step
        A += step
        used[np.flatnonzero(ok), j[ok]] = True
        nmod += ok
    return A, nmod


def row(label, rec, bits):
    w, p, t = evaluate(rec)
    return f"| {label} | {bits:.1f} | {w:.3f} | {p:.0%} | {t:.0%} |"


G1 = np.stack([unit((Xm_all[ex[a]] - Xm_all[ex[b]])[None])[0] for a, b in POLES.values()])
G2 = unit(Xm_all[root_idx])
mean_r, W = fit_axes("varimax", Er[train], 9, np.random.default_rng(SEED))
G0 = W.T
out = ["# Разреженное кодирование (всё в корнях) против плотных общих осей", "",
       f"Слово = корень ({R_} корней, {np.log2(R_):.1f} бита) + суффикс (2 бита) + модификаторы. Модификатор — корень со значением на своей оси (ненулевой из 10 уровней, ноль = не пишется): номер {np.log2(10):.1f}+log₂(M) бит. Поле «сколько модификаторов» стоит log₂(kmax+1) бит. Режим слов, тот же протокол, что у 09 (train/test, wup, pos, top50).",
       "S1 — 16 корней со своей осью, направление = разность двух слов-полюсов; S2 — любой корень как направление (второй корень-модификатор); S3 — вместе; S0 — 9 осей varimax из данных, закодированных разреженно (отделяет разреженность от читаемости).", "",
       "| схема | биты на слово | wup | pos | top50 |", "| :-- | --: | --: | --: | --: |"]
out.append(row("корень + суффикс, без осей", base, np.log2(R_) + 2))
for u in (3, 6, 9):
    mean_r_, W_ = fit_axes("varimax", Er[train], u, np.random.default_rng(SEED))
    M = (Er - mean_r_) @ W_
    sm = M[train].std(axis=0)
    out.append(row(f"**плотно: {u} общих осей**", base + dequantize(quantize(M, sm), sm) @ W_.T + mean_r_,
                   np.log2(R_) + 2 + u * BITS))
samples = {}
for name, G in (("S1 (16 осей-корней)", G1), ("S2 (любой корень)", G2),
                ("S3 (S1 + S2)", np.vstack([G1, G2])), ("S0 (9 осей из данных)", G0)):
    for kmax in (1, 2, 3, 4, 6):
        A, nmod = sparse_code(G, kmax)
        bits = np.log2(R_) + 2 + np.log2(kmax + 1) + nmod.mean() * (np.log2(len(G)) + np.log2(10))
        out.append(row(f"{name}, ≤{kmax} модификаторов (в среднем {nmod.mean():.1f})", base + A, bits))
        if kmax == 3:
            samples[name] = (A, nmod)
out += ["", "## Примеры кодов (S1, ≤3 модификатора)", ""]
axis_names = [k.upper() for k in POLES]
A1, _ = sparse_code(G1, 3)
sd1 = (Er[train] @ G1.T).std(axis=0)
for w in ("bedroom", "house", "rent", "love", "pretty", "mother", "kitchen", "doctor", "anger", "mountain", "quickly", "hungry"):
    if w not in words:
        continue
    i = words.index(w)
    q = quantize(A1[i] @ G1.T, sd1)
    mods = [f"{axis_names[j]}({int(q[j]):+d})" for j in np.argsort(-np.abs(q)) if q[j] != 0][:3]
    out.append(f"- **{w}** → {ROOTS[assign[i]].upper()}{SUFFIX[pos[i]]} " + " ".join(mods))
text = "\n".join(out)
(ROOT / "data" / "sparse_vs_dense.md").write_text(text, encoding="utf-8")
print(text)
