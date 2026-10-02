"""Print the working scheme: 30 roots, 3 form axes, 6 universal meaning axes, coding examples."""
import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from common import RAW, ROOT, load_vectors, word_matrix
from lib_axes import (dequantize, fit_axes, generality, greedy_roots, quantize, remove_freq,
                      unit)

R_, U, NFORM, NCAND, SEED = 30, 6, 3, 300, 0
rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
rng = np.random.default_rng(SEED)
perm = rng.permutation(n)
train, test = perm[: n // 2], perm[n // 2:][:600]

glove = load_vectors("glove100")
logfreq = -np.log1p(np.array([glove.key_to_index[w] for w in words]))
logfreq = (logfreq - logfreq.mean()) / logfreq.std()
X = remove_freq(unit(word_matrix("numberbatch", words)), logfreq, train)
S = X @ X.T
cand = np.argsort(-generality(words, pos, RAW / "generality_x5.npy"))[:NCAND]
roots = greedy_roots(S, train, cand, R_)
assign = np.argmax(S[:, roots], axis=1)
mu = np.stack([X[np.intersect1d(np.flatnonzero(assign == r), train)].mean(axis=0)
               for r in range(R_)])
E = X - mu[assign]
lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(E[train], pos[train])
F, _ = np.linalg.qr(lda.scalings_[:, :NFORM])
f = E @ F
Er = E - f @ F.T
mean_r, W = fit_axes("varimax", Er[train], U, np.random.default_rng(SEED))
M = (Er - mean_r) @ W
order = np.argsort(-M[train].std(axis=0))
M, W = M[:, order], W[:, order]
sf, sm = f[train].std(axis=0), M[train].std(axis=0)
qf, qm = quantize(f, sf).astype(int), quantize(M, sm).astype(int)


def poles(sc, j, top=7):
    idx = np.argsort(sc[:, j])
    return ", ".join(words[i] for i in idx[:top]), ", ".join(words[i] for i in idx[::-1][:top])


out = ["# Рабочая схема: 30 корней + 3 оси формы + 6 универсальных смысловых осей\n",
       "Numberbatch, 3000 слов, частотность вычтена. Оси найдены по отклонению слов от центра своего корня; "
       "полюса — слова с крайними значениями по всему списку. Знаки и порядок осей нестабильны между запусками.\n",
       "## Корни (по размеру кластера)\n"]
for r in np.argsort(-np.bincount(assign, minlength=R_)):
    mem = np.flatnonzero(assign == r)
    near = mem[np.argsort(-S[mem, roots[r]])][1:7]
    out.append(f"- **{words[roots[r]]}** ({len(mem)}): " + ", ".join(words[i] for i in near))
out.append("\n## Форма (3 оси)\n")
for j in range(NFORM):
    a, b = poles(f, j)
    out.append(f"- F{j + 1}: **−** {a}  /  **+** {b}")
out.append("\n## Универсальные смысловые оси (6)\n")
for j in range(U):
    a, b = poles(M, j)
    out.append(f"- M{j + 1}: **−** {a}  /  **+** {b}")
out.append("\n## Примеры кодирования (слова из test)\n")
out.append("Запись: `ROOT(F1,F2,F3 | M1..M6)`, значения -5..+5.\n")
for i in test[:14]:
    code = ",".join(f"{v:+d}" for v in qf[i]) + " | " + ",".join(f"{v:+d}" for v in qm[i])
    out.append(f"- {words[i]} ({pos[i]}) = `{words[roots[assign[i]]].upper()}({code})`")
text = "\n".join(out)
(ROOT / "data" / "scheme_numberbatch.md").write_text(text, encoding="utf-8")
print(text)
