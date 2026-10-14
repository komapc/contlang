"""Пересмотр корней, шаги 0–1: главные оси словаря сайта и их повороты (data/pca_axes.md).

Шаг 0 — пространство. Слова: словарь сайта (site/data/math.json, vocab.bin — Numberbatch int8), без служебных, имён
собственных и словоформ (только леммы). Очистка: центрирование; вычитается направление частотности (гребневая регрессия
−log ранга по вектору) и направления частей речи (разности средних имени, глагола, прилагательного, наречия — часть речи
задаёт форма `| o i a e`, корням она не нужна). Проверка — корреляция каждой главной оси с частотой и доля
дисперсии, объяснённая частью речи (η²), до и после очистки.

Шаг 1 — сырые оси. PCA на 30 компонент: доля дисперсии, полюса (по 12 частых слов, ранг < 6000). Повороты верхних K:
varimax (оценки слов разреженнее, базис остаётся ортогональным) и FastICA (независимые оси, базис не ортогонален —
приводится наибольший |cos| между осями). Покрытие нынешних корней: какая доля каждого атома (центр C и ось A
из site/data/math.json, после той же очистки) лежит в подпространстве верхних K компонент, и какой корень ближе всего
к каждой оси.

    .venv/bin/python scripts/23_pca_axes.py [K=20]
"""
import json
import sys
from pathlib import Path

import numpy as np
from sklearn.decomposition import FastICA

REPO = Path(__file__).resolve().parents[1]
K = int(sys.argv[1]) if len(sys.argv) > 1 else 20
NPC, POLE, RANK = 30, 12, 6000
SITE = REPO / "site" / "data"

m = json.loads((SITE / "math.json").read_text(encoding="utf8"))
meta = json.loads((SITE / "words.json").read_text(encoding="utf8"))
W = m["words"]
X = np.frombuffer((SITE / "vocab.bin").read_bytes(), dtype=np.int8).reshape(len(W), m["dim"]).astype(float)
X /= np.linalg.norm(X, axis=1, keepdims=True)

bad = set(meta["stop"]) | set(meta["proper"]) | set(meta["plural"])
keep = [i for i, w in enumerate(W) if i not in bad and meta["lemma"][i] == -1 and meta["pos"][i] and w.isalpha()]
words = [W[i] for i in keep]
Y = X[keep]
rank = np.array(keep, float)                      # math.json — по частоте
logf = -np.log1p(rank)
logf = (logf - logf.mean()) / logf.std()
pos = np.array([int(np.argmax([int(c) for c in meta["pos"][i]])) for i in keep])  # 0 имя, 1 глагол, 2 прил., 3 нар.
PN = ["имя", "глагол", "прил.", "нар."]
n = len(words)


def unit(v):
    return v / np.linalg.norm(v)


def eta2(s):
    """доля дисперсии оценок s, объяснённая частью речи"""
    tot = ((s - s.mean()) ** 2).sum()
    return sum(((s[pos == p].mean() - s.mean()) ** 2) * (pos == p).sum() for p in range(4) if (pos == p).any()) / tot


def pca(Z, k):
    U, S, Vt = np.linalg.svd(Z - Z.mean(0), full_matrices=False)
    return Vt[:k], S ** 2 / (S ** 2).sum()


def check(Z, name, k=10):
    V, ev = pca(Z, k)
    sc = (Z - Z.mean(0)) @ V.T
    r = [abs(np.corrcoef(sc[:, j], logf)[0, 1]) for j in range(k)]
    e = [eta2(sc[:, j]) for j in range(k)]
    return f"| {name} | " + " | ".join(f"{a:.2f} / {b:.2f}" for a, b in zip(r, e)) + " |"


# шаг 0: очистка
Z0 = Y - Y.mean(0)
lam = 1.0
wf = np.linalg.solve(Z0.T @ Z0 + lam * np.eye(Z0.shape[1]), Z0.T @ logf)
dirs = [unit(wf)]
mu = [Z0[pos == p].mean(0) for p in range(4)]
dirs += [mu[p] - mu[0] for p in (1, 2, 3)]
Q, _ = np.linalg.qr(np.stack(dirs).T)             # ортонормированный базис 4 вычитаемых направлений
P = lambda Z: Z - (Z @ Q) @ Q.T
Z = P(Z0)
Z /= np.linalg.norm(Z, axis=1, keepdims=True)
Z -= Z.mean(0)

L = [f"# Главные оси словаря сайта (шаги 0–1 пересмотра корней)", "",
     f"`scripts/23_pca_axes.py {K}`. Слов {n} (леммы словаря сайта без служебных и имён), векторы Numberbatch (vocab.bin).", "",
     "## Шаг 0. Очистка", "",
     "Вычтены направление частотности и 3 направления частей речи. В клетке — |r| главной оси с частотой / η² части речи.", "",
     "| | " + " | ".join(f"PC{j + 1}" for j in range(10)) + " |", "|---|" + "---|" * 10,
     check(Y, "до очистки"), check(Z, "после очистки"), ""]

# шаг 1: PCA
V, ev = pca(Z, NPC)
S = Z @ V.T
freq = np.array([r < RANK for r in rank])


def poles(s, k=POLE):
    o = np.argsort(s)
    lo = [words[i] for i in o if freq[i]][:k]
    hi = [words[i] for i in o[::-1] if freq[i]][:k]
    return ", ".join(lo), ", ".join(hi)


# корни: центры и оси, очищенные тем же проектором
names = m["names"]
C = P(np.array(m["dict"]["C"]) - Y.mean(0))  # центр — точка: берётся её направление от среднего слова
A = P(np.array(m["dict"]["A"]))
has = m["has_axis"]
R = [(f"{nm}·ось", unit(A[r])) for r, nm in enumerate(names) if has[r] and np.linalg.norm(A[r]) > 0] + \
    [(f"{nm}·центр", unit(C[r])) for r, nm in enumerate(names)]


def nearest_root(v):
    c = [(abs(float(unit(v) @ d)), nm, float(unit(v) @ d)) for nm, d in R]
    c.sort(reverse=True)
    return ", ".join(f"{nm} {s:+.2f}" for _, nm, s in c[:2])


def table(B, title, note=""):
    out = [f"## {title}", ""] + ([note, ""] if note else [])
    out += ["| ось | доля | r част. | η² ч.р. | − полюс | + полюс | ближе всего из корней |", "|---|--:|--:|--:|---|---|---|"]
    for j, b in enumerate(B):
        s = Z @ unit(b)
        lo, hi = poles(s)
        share = float(((Z @ unit(b)) ** 2).sum() / (Z ** 2).sum())
        out.append(f"| {j + 1} | {share:.1%} | {abs(np.corrcoef(s, logf)[0, 1]):.2f} | {eta2(s):.2f} | {lo} | {hi} | {nearest_root(b)} |")
    return out + [""]


L += [f"## Шаг 1. PCA", "", f"Доля дисперсии верхних компонент: 10 — {ev[:10].sum():.1%}, 20 — {ev[:20].sum():.1%}, 30 — {ev[:30].sum():.1%} "
      f"(одна случайная ось в среднем {1 / Z.shape[1]:.1%}).", ""]
L += table(V[:K], f"PCA, верхние {K}")

# varimax на оценках слов верхних K компонент
def varimax(Phi, gamma=1.0, it=100, tol=1e-6):
    p, k = Phi.shape
    Rm = np.eye(k)
    d = 0
    for _ in range(it):
        Lm = Phi @ Rm
        u, s, vh = np.linalg.svd(Phi.T @ (Lm ** 3 - (gamma / p) * Lm @ np.diag((Lm ** 2).sum(0))))
        Rm = u @ vh
        dn = s.sum()
        if d and dn / d < 1 + tol:
            break
        d = dn
    return Rm


Sk = S[:, :K] / S[:, :K].std(0)
Rv = varimax(Sk)
Bv = (Rv.T @ V[:K])
order = np.argsort(-((Z @ Bv.T) ** 2).sum(0))
L += table(Bv[order], f"Varimax, {K} осей", "Поворот верхних K компонент: базис ортогонален, оценки слов разреженнее (у слова меньше сильных осей).")

ica = FastICA(n_components=K, random_state=0, max_iter=2000, whiten="unit-variance").fit(S[:, :K])
Bi = np.array([unit(v) for v in ica.components_ @ V[:K]])
order = np.argsort(-((Z @ Bi.T) ** 2).sum(0))
Bi = Bi[order]
G = np.abs(Bi @ Bi.T) - np.eye(K)
L += table(Bi, f"ICA, {K} осей", f"Независимые оси в том же подпространстве; базис не ортогонален: наибольший |cos| между осями {G.max():.2f}, средний {G.sum() / (K * K - K):.2f}.")

# покрытие нынешних корней подпространством верхних K
VK = V[:K]
cov = [(nm, float(np.linalg.norm(VK @ d) ** 2)) for nm, d in R]
cov.sort(key=lambda t: -t[1])
rnd = np.random.default_rng(0).normal(size=(200, Z.shape[1]))
base = np.mean([np.linalg.norm(VK @ unit(P(r[None])[0])) ** 2 for r in rnd])
L += [f"## Нынешние корни в подпространстве верхних {K} компонент", "",
      f"Доля длины атома (квадрат), лежащая в подпространстве; у случайного направления {base:.1%}.", "",
      "| корень | доля | | корень | доля |", "|---|--:|---|---|--:|"]
half = -(-len(cov) // 2)
for a, b in zip(cov[:half], cov[half:] + [("", None)] * (2 * half - len(cov))):
    L.append(f"| {a[0]} | {a[1]:.0%} | | {b[0]} | {'' if b[1] is None else f'{b[1]:.0%}'} |")
axes_only = [c for nm, c in cov if nm.endswith("ось")]
L += ["", f"Оси корней: в среднем {np.mean(axes_only):.0%} в подпространстве; центры: {np.mean([c for nm, c in cov if nm.endswith('центр')]):.0%}."]
# какая доля подпространства верхних K покрыта осями корней (span), и наоборот
Ax = np.stack([d for nm, d in R if nm.endswith("ось")])
Qa, _ = np.linalg.qr(Ax.T)
cap = [float(np.linalg.norm(Qa.T @ v) ** 2) for v in VK]
L += [f"Покрытие главных компонент осями всех {Ax.shape[0]} корней (доля длины компоненты в их линейной оболочке): "
      + ", ".join(f"PC{j + 1} {c:.0%}" for j, c in enumerate(cap)) + ".", ""]

out = REPO / "data" / "pca_axes.md"
out.write_text("\n".join(L) + "\n", encoding="utf8")
print("записано", out, "слов", n)
