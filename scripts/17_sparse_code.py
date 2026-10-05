"""Математическое кодирование туда-сюда без языковой модели.

Слово x (вектор Numberbatch) кодируется не более чем m корнями с уровнями
-5..+5; код декодируется обратно в вектор и узнаётся среди всех слов.

Словарь (матрица D) строится из roots.yaml без обучения:
  корень r = центр c_r (среднее всех слов-полюсов, «о чём ось»)
             + ось a_r (полюс+ минус полюс−, SemAxis).
  Корни без оси (BODY SEE DO PLACE FIGHT) задаются списками слов ниже.
Декодер: y = sum_r (c_r + s * v_r/5 * a_r), v_r — уровень, s — общий масштаб.
Кодер: перебор опор из лучших по корреляции корней + покоординатный подбор
уровней, цель — max cos(x, y).

Сравнения: непрерывные коэффициенты (без уровней), 11 / 5 / 3 уровня,
случайный словарь той же формы, словарь из главных компонент (нечитаемый).
Слова-полюса исключены и из теста, и из кандидатов.
Пишет data/sparse_code.md.
"""
import importlib.util
import itertools
import sys
from pathlib import Path

import numpy as np

from common import ROOT

sys.path.insert(0, str(Path(__file__).resolve().parent))
from mincode import spec  # noqa: E402

_s15 = importlib.util.spec_from_file_location("s15", Path(__file__).with_name("15_semaxis.py"))
s15 = importlib.util.module_from_spec(_s15)
_s15.loader.exec_module(s15)

NOAXIS = {
    "BODY": "body arm leg head hand skin",
    "SEE": "see look watch eye view notice",
    "DO": "do make act perform action work",
    "PLACE": "place location area site region spot",
    "FIGHT": "fight war battle quarrel combat conflict",
}
SHOW = ("dog honey sand hope bank mathematics teacher anger river money "
        "child city music winter knife friend sleep idea").split()
OUT = ROOT / "data" / "sparse_code.md"
TOPR = 8          # из скольких лучших корней перебирать опоры
SCALES = (0.5, 1.0, 1.5, 2.0, 3.0)


def unit(v):
    return v / (np.linalg.norm(v, axis=-1, keepdims=True) + 1e-9)


def build_dictionary(vec):
    names, C, A, poles = [], [], [], set()
    for r in spec.axis_roots():
        p, n = r["semaxis"]
        P = [w for w in p.split() if w in vec]
        N = [w for w in n.split() if w in vec]
        poles |= set(P) | set(N)
        mp = np.mean([unit(vec[w]) for w in P], 0)
        mn = np.mean([unit(vec[w]) for w in N], 0)
        names.append(r["name"])
        C.append(unit(mp + mn))
        A.append(unit(mp - mn))
    for name, ws in NOAXIS.items():
        W = [w for w in ws.split() if w in vec]
        poles |= set(W)
        names.append(name)
        C.append(unit(np.mean([unit(vec[w]) for w in W], 0)))
        A.append(np.zeros_like(C[-1]))
    return names, np.stack(C), np.stack(A), poles


def encode_continuous(x, C, A, m):
    """Групповой OMP: опора из m корней, свободные коэффициенты при c_r и a_r."""
    S, res = [], x.copy()
    for _ in range(m):
        score = (C @ res) ** 2 + (A @ res) ** 2
        score[S] = -1
        S.append(int(np.argmax(score)))
        B = np.concatenate([C[S], A[S]]).T
        coef, *_ = np.linalg.lstsq(B, x, rcond=None)
        res = x - B @ coef
    return S, B @ coef


class LevelCoder:
    """Точный перебор: опоры из TOPR лучших корней, все сочетания уровней сразу.

    cos(x, y) считается через скалярные произведения с корнями и матрицы Грама,
    поэтому векторы размерности 300 внутри перебора не строятся.
    """

    def __init__(self, C, A, levels, s):
        self.C, self.A, self.s = C, A, s / 5
        self.has = A.any(1)
        self.CC, self.CA, self.AA = C @ C.T, C @ A.T, A @ A.T
        self.levels, self.grids = levels, {}

    def grid(self, flags):
        if flags not in self.grids:
            self.grids[flags] = np.array(list(itertools.product(
                *[self.levels if f else [0] for f in flags])), dtype=float)
        return self.grids[flags]

    def __call__(self, x, m):
        cx, ax, s = self.C @ x, self.A @ x, self.s
        cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:TOPR])
        best = (-2, None, None)
        for k in range(1, m + 1):
            for S in itertools.combinations(cand, k):
                S = list(S)
                G = self.grid(tuple(self.has[S]))
                dot = cx[S].sum() + s * G @ ax[S]
                ac = self.CA[np.ix_(S, S)].sum(0)
                nrm = (self.CC[np.ix_(S, S)].sum() + 2 * s * G @ ac
                       + s * s * ((G @ self.AA[np.ix_(S, S)]) * G).sum(1))
                cos = dot / np.sqrt(np.maximum(nrm, 1e-9))
                i = int(np.argmax(cos))
                if cos[i] > best[0]:
                    best = (cos[i], S, G[i])
        _, S, v = best
        return S, v, (self.C[S] + (s * v)[:, None] * self.A[S]).sum(0)


def ranks(Y, idx, V):
    """Место настоящего слова среди всех слов словаря по cos(y, слово)."""
    sims = unit(Y) @ V.T
    tgt = sims[np.arange(len(idx)), idx]
    return (sims > tgt[:, None]).sum(1) + 1


def summary(r):
    return f"{np.mean(r == 1):.1%} | {np.mean(r <= 10):.1%} | {np.mean(r <= 50):.1%} | {int(np.median(r))}"


def main():
    words, poles_all = s15.words_needed()
    extra = {w for ws in NOAXIS.values() for w in ws.split()}
    vec = s15.load_subset(set(words) | set(poles_all) | extra | set(SHOW))
    names, C, A, poles = build_dictionary(vec)
    # слова-полюса убраны и из теста, и из кандидатов: иначе код, попавший
    # в середину полюса, «узнаёт» само слово-полюс (top1 падал с 21% до 3%)
    vocab = [w for w in dict.fromkeys(words + SHOW) if w in vec and w not in poles]
    V = unit(np.stack([vec[w] for w in vocab]))
    test = list(range(len(vocab)))
    X = V[test]
    rng = np.random.default_rng(0)

    # случайный словарь той же формы и словарь из главных компонент
    Cr, Ar = unit(rng.normal(size=C.shape)), unit(rng.normal(size=A.shape))
    Ar[-len(NOAXIS):] = 0
    _, _, Vt = np.linalg.svd(V - V.mean(0), full_matrices=False)
    k = len(names)
    Cp, Ap = Vt[:k].copy(), Vt[k:2 * k].copy()

    L = ["# Математическое кодирование туда-сюда (без языковой модели)", "",
         f"Numberbatch: {len(vocab)} слов, каждое кодируется и узнаётся среди всех "
         f"(слова-полюса исключены и из теста, и из кандидатов). Корней: {k} "
         f"({k - len(NOAXIS)} с осью). Скрипт: `scripts/17_sparse_code.py`.", "",
         "Метрика: место настоящего слова среди всех слов по близости к декодированному вектору. "
         f"Случайное угадывание: top1 ≈ {1 / len(vocab):.2%}, top50 ≈ {50 / len(vocab):.1%}.", ""]

    # 1. непрерывные коэффициенты, зависимость от m
    L += ["## 1. Непрерывные коэффициенты (без уровней)", "",
          "| словарь | m | top1 | top10 | top50 | медиана места |", "| :-- | --: | --: | --: | --: | --: |"]
    for label, (CC, AA) in (("корни", (C, A)), ("случайный", (Cr, Ar)), ("главные компоненты", (Cp, Ap))):
        for m in (1, 2, 3, 5):
            Y = np.stack([encode_continuous(x, CC, AA, m)[1] for x in X])
            L.append(f"| {label} | {m} | {summary(ranks(Y, test, V))} |")
    print("\n".join(L[-13:]), flush=True)

    # 2. уровни: выбор масштаба на 300 словах, потом весь тест
    sub = rng.choice(len(X), 300, replace=False)
    lv11 = list(range(-5, 6))
    def top50(s):
        coder = LevelCoder(C, A, lv11, s)
        return np.mean(ranks(np.stack([coder(X[i], 3)[2] for i in sub]), [test[i] for i in sub], V) <= 50)
    best_s = max(SCALES, key=top50)
    L += ["", "## 2. Целые уровни (кодер max cos, перебор опор)", "",
          f"Масштаб оси s = {best_s} (выбран на 300 словах из {SCALES}).", "",
          "| уровни | m | top1 | top10 | top50 | медиана места |", "| :-- | --: | --: | --: | --: | --: |"]
    codes = {}
    for lvname, lv in (("11 (−5…+5)", lv11), ("5 (−5,−2,0,+2,+5)", [-5, -2, 0, 2, 5]), ("3 (−5,0,+5)", [-5, 0, 5])):
        coder = LevelCoder(C, A, lv, best_s)
        for m in (1, 2, 3):
            enc = [coder(x, m) for x in X]
            L.append(f"| {lvname} | {m} | {summary(ranks(np.stack([e[2] for e in enc]), test, V))} |")
            print(L[-1], flush=True)
            if lv is lv11 and m == 3:
                codes = enc

    # 2б. чужие словари той же формы + смысловые метрики и устойчивость
    def metrics(Y):
        Y = unit(Y)
        r = ranks(Y, test, V)
        guess = np.argmax(Y @ V.T, 1)
        gs = (V[guess] * X).sum(1)
        miss = r > 1
        return r, (Y * X).sum(1).mean(), gs[miss].mean() if miss.any() else float("nan")

    def perturb(CC, AA, enc, s):
        """Один случайный уровень корня с осью сдвинут на ±2 (ошибка кодировщика)."""
        out = []
        for S, v, _ in enc:
            v = v.copy()
            ax = [j for j, r in enumerate(S) if AA[r].any()]
            if ax:
                j = rng.choice(ax)
                v[j] = np.clip(v[j] + rng.choice([-2, 2]), -5, 5)
            out.append((CC[S] + (s / 5 * v)[:, None] * AA[S]).sum(0))
        return np.stack(out)

    L += ["", "## 2б. Корни против словарей без смысла (11 уровней, m = 3)", "",
          "cos(x, y) — насколько декодированный вектор похож на смысл слова. "
          "«Промах похож» — средняя близость неверной догадки к настоящему слову "
          "(близкий промах лучше далёкого). «После ±2» — один уровень в коде сдвинут на ±2.", "",
          "| словарь | top1 | top50 | cos(x, y) | промах похож | top1 после ±2 | промах похож после ±2 |",
          "| :-- | --: | --: | --: | --: | --: | --: |"]
    dicts = [("корни", C, A, best_s, codes)]
    for label, CC, AA in (("случайный", Cr, Ar), ("главные компоненты", Cp, Ap)):
        def top50_other(s):
            coder = LevelCoder(CC, AA, lv11, s)
            return np.mean(ranks(np.stack([coder(X[i], 3)[2] for i in sub]), [test[i] for i in sub], V) <= 50)
        s_ = max(SCALES, key=top50_other)
        coder = LevelCoder(CC, AA, lv11, s_)
        dicts.append((f"{label} (s = {s_})", CC, AA, s_, [coder(x, 3) for x in X]))
    for label, CC, AA, s_, enc in dicts:
        r, cxy, gm = metrics(np.stack([e[2] for e in enc]))
        rp, _, gmp = metrics(perturb(CC, AA, enc, s_))
        L.append(f"| {label} | {np.mean(r == 1):.1%} | {np.mean(r <= 50):.1%} | {cxy:.3f} | {gm:.3f} "
                 f"| {np.mean(rp == 1):.1%} | {gmp:.3f} |")
        print(L[-1], flush=True)
    nb = V[test] @ V.T
    nb[np.arange(len(test)), test] = -1
    L += ["", f"Для сравнения: близость слова к его настоящему ближайшему соседу в среднем "
          f"{nb.max(1).mean():.3f}, к случайному слову {(V[test] @ V[rng.choice(len(V), len(test))].T).diagonal().mean():.3f}."]

    # 3. примеры
    pos = {vocab[i]: j for j, i in enumerate(test)}
    L += ["", "## 3. Примеры (11 уровней, m = 3)", "",
          "| слово | код | место | ближайшие к декодированному |", "| :-- | :-- | --: | :-- |"]
    for w in SHOW:
        if w not in pos:
            continue
        S, v, y = codes[pos[w]]
        code = " ".join(names[r] if not A[r].any() else f"{names[r]}(={int(lv):+d})".replace("+0", "0")
                        for r, lv in zip(S, v))
        sims = V @ unit(y)
        near = ", ".join(vocab[i] for i in np.argsort(-sims)[:5])
        rk = int((sims > sims[test[pos[w]]]).sum() + 1)
        L.append(f"| {w} | `{code}` | {rk} | {near} |")
    OUT.write_text("\n".join(L) + "\n", encoding="utf8")
    print("\n".join(L[-len(SHOW) - 4:]))


if __name__ == "__main__":
    main()
