"""Automatic coding of sentence words: word -> root + suffix + gradient + 9 universal axes -> nearest vocabulary word.

Uses the NSM-gradient roots (docs/lexicon.md) on the 3000-word list plus the sentence words
(held out of training). Writes data/translation_test/auto_words.md.
"""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import ROOT, load_vectors, word_matrix
from lib_axes import dequantize, fit_axes, quantize, remove_freq, unit

ROOTS = "someone,thing,people,body,kind,part,word,happen,move,think,know,want,feel,see,hear,touch,place,inside,side,good,big,near,above,live,same,maybe,time".split(",")
GRADIENT = [g.split(":") for g in "good:bad,big:small,near:far,above:below,live:die,same:different,maybe:true".split(",")]
import os
U, NFORM, SEED = int(os.environ.get("AXES", 9)), 3, 0
TAG = os.environ.get("TAG", "")
SUFFIX = {"noun": "-o", "verb": "-i", "adj": "-a", "adv": "-e"}
SENT = """dog:noun sleep:verb house:noun want:verb see:verb friend:noun hear:verb noise:noun die:verb war:noun rain:noun
stay:verb big:adj car:noun move:verb quickly:adv king:noun say:verb dead:adj think:verb water:noun cold:adj child:noun
learn:verb language:noun listen:verb meeting:noun love:verb book:noun good:adj come:verb happy:adj know:verb answer:noun""".split()

rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = [r[1] for r in rows]
n_list = len(words)
extra = []
for sp in SENT:
    w, p = sp.split(":")
    if w not in words:
        words.append(w); pos.append(p); extra.append(len(words) - 1)
pos = np.array(pos); n = len(words)
first = {}
for i, w in enumerate(words):
    first.setdefault(w, i)
group = np.unique(words, return_inverse=True)[1]
rng = np.random.default_rng(SEED)
gperm = rng.permutation(group.max() + 1)
held = {sp.split(':')[0] for sp in SENT}
is_extra = np.array([w in held for w in words])
train = np.flatnonzero(np.isin(group, gperm[: len(gperm) // 2]) & ~is_extra)

glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index.get(w, 100000) for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X0 = unit(word_matrix("numberbatch", words))
X = remove_freq(X0, logfreq, train)

mean0 = X[train].mean(axis=0)
Xc = X - mean0
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(Xc[train], pos[train])
F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
f = Xc @ F
Xm = Xc - f @ F.T
Xm_n = unit(Xm)
f_class = {p: f[train][pos[train] == p].mean(axis=0) for p in SUFFIX}
form_offset = np.stack([f_class[p] for p in pos]) @ F.T

roots = [first[w] for w in ROOTS]
S_m = Xm_n @ Xm_n.T
assign = np.argmax(S_m[:, roots], axis=1)
mu = np.stack([Xm[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0) for r in range(len(roots))])
Er = Xm - mu[assign]
local = np.zeros_like(Er)
lval = {}
for w1, w2 in GRADIENT:
    r = ROOTS.index(w1)
    g = Xm[first[w1]] - Xm[first[w2]]
    g /= np.linalg.norm(g)
    mem = np.flatnonzero(assign == r)
    c = Er[mem] @ g
    sd = c[np.isin(mem, train)].std()
    q = quantize(c[:, None], np.array([sd]))[:, 0]
    for i, qi in zip(mem, q):
        lval[i] = int(qi)
    Er[mem] -= np.outer(c, g)
    local[mem] += np.outer(dequantize(q[:, None], np.array([sd]))[:, 0], g)
mean_r, W = fit_axes("varimax", Er[train], U, np.random.default_rng(SEED))
M = (Er - mean_r) @ W
sm = M[train].std(axis=0)
Q = quantize(M, sm)
R = mu[assign] + local + dequantize(Q, sm) @ W.T + mean_r + form_offset + mean0
Rn = unit(R)

Xn = unit(X)
out = ["# Автоматическое кодирование слов предложений: слово → корень + суффикс + градиент + 9 осей → ближайшее слово",
       "", f"Словарь для декодирования: {n_list} слов списка + {len(extra)} слов предложений ({n} записей). Все слова предложений исключены из обучения осей и корней (корни из списка NSM заданы заранее). Декодирование — ближайшая запись по косинусу в пространстве X (без частотности); «сам» — слово вернулось само.", "",
       "| слово | код | вернулось (топ-5) | сам |", "| :-- | :-- | :-- | :-- |"]
hits = 0
for sp in SENT:
    w, p = sp.split(":")
    i = first[w]
    sims = Xn @ Rn[i]
    top = np.argsort(-sims)[:5]
    me = "да" if top[0] == i else ("в топ-5" if i in top else "нет")
    hits += top[0] == i
    code = f"{ROOTS[assign[i]].upper()}{SUFFIX[p]}"
    if i in lval:
        code += f"(={lval[i]})"
    code += " [" + ",".join(str(v) for v in Q[i]) + "]"
    out.append(f"| {w} ({p}) | {code} | {', '.join(words[j] for j in top)} | {me} |")
out.append(f"\nСлово вернулось само первым: {hits} из {len(SENT)}.")
text = "\n".join(out)
(ROOT / "data" / "translation_test" / f"auto_words{TAG}.md").write_text(text, encoding="utf-8")
print(text)
