"""Общая часть математического кодирования (см. docs/math.md).

Слово x (вектор Numberbatch, единичный) кодируется не более чем m корнями с
уровнями; код декодируется линейно:
    y = sum_j w_j * (c_{r_j} + (s/5) * v_j * a_{r_j}),
где c_r — центр корня (среднее его слов-полюсов), a_r — ось (полюс+ минус
полюс−), v_j — уровень −5…+5, w_j — вес позиции (главный корень первым).

Здесь: загрузка данных с фиксированным словарём узнавания и разбиением на
обучение и тест, построение словаря из roots.yaml, точный кодер и метрики.
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
    "TEXT": "text writing written document page script",
}
LEVELS = list(range(-5, 6))
POS_FORM = {"noun": "o", "verb": "i", "adj": "a", "adv": "e"}


def unit(v):
    return v / (np.linalg.norm(v, axis=-1, keepdims=True) + 1e-9)


def wordlist():
    rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
    return [r[0] for r in rows], {r[0]: r[1] for r in rows}


def root_specs(overrides=None, extra=None, axes=None):
    """[(name, plus_words, minus_words | None, center_words | None)].

    overrides: {name: (plus, minus)} — заменить полюса; axes: {name: (plus,
    minus)} — дать ось корню без оси (центр остаётся из его слов); extra:
    кандидаты в новые корни, такие же четвёрки (minus None — без оси).
    """
    out = []
    for r in spec.axis_roots():
        p, n = (overrides or {}).get(r["name"], r["semaxis"])
        out.append((r["name"], p, n, None))
    for name, ws in NOAXIS.items():
        if name in (axes or {}):
            out.append((name, *axes[name], ws))
        else:
            out.append((name, ws, None, None))
    out += list(extra or [])
    return out


class Data:
    """Векторы, словарь узнавания (без слов-полюсов) и разбиение 70/30."""

    def __init__(self, specs_list, seed=0, center=False):
        words, self.pos = wordlist()
        need = set(words)
        for specs in specs_list:
            for _, p, n, c in specs:
                need |= set(p.split()) | set((n or "").split()) | set((c or "").split())
        self.vec = s15.load_subset(need)
        poles = set()
        for specs in specs_list:
            for _, p, n, c in specs:
                poles |= set(p.split()) | set((n or "").split()) | set((c or "").split())
        self.poles = poles
        self.vocab = [w for w in words if w in self.vec and w not in poles]
        raw = np.stack([self.vec[w] for w in self.vocab])
        self.mu = unit(raw).mean(0) if center else np.zeros(raw.shape[1])
        self.V = self.emb(self.vocab)
        rng = np.random.default_rng(seed)
        perm = rng.permutation(len(self.vocab))
        cut = int(0.7 * len(perm))
        self.train, self.test = np.sort(perm[:cut]), np.sort(perm[cut:])

    def emb(self, ws):
        return unit(unit(np.stack([self.vec[w] for w in ws])) - self.mu)

    def dictionary(self, specs):
        names, C, A = [], [], []
        for name, p, n, c in specs:
            P = self.emb([w for w in p.split() if w in self.vec])
            if n:
                N = self.emb([w for w in n.split() if w in self.vec])
                center = self.emb([w for w in c.split() if w in self.vec]).mean(0) if c else P.mean(0) + N.mean(0)
                C.append(unit(center))
                A.append(unit(P.mean(0) - N.mean(0)))
            else:
                C.append(unit(P.mean(0)))
                A.append(np.zeros(P.shape[1]))
            names.append(name)
        return names, np.stack(C), np.stack(A)


class Coder:
    """Точный перебор: опоры из topr лучших корней, все уровни и выбор главного.

    head_w — вес второго и третьего корня относительно главного (1 — порядок
    не важен). cos(x, y) считается через матрицы Грама, без векторов 300-d.
    """

    def __init__(self, C, A, s=2.0, levels=LEVELS, head_w=1.0, topr=8):
        self.C, self.A, self.s, self.levels, self.hw, self.topr = C, A, s / 5, levels, head_w, topr
        self.has = A.any(1)
        M = np.concatenate([C, A])
        self.G = M @ M.T
        self.R = len(C)
        self.grids = {}

    def grid(self, flags):
        if flags not in self.grids:
            self.grids[flags] = np.array(list(itertools.product(
                *[self.levels if f else [0] for f in flags])), dtype=float)
        return self.grids[flags]

    def __call__(self, x, m=3):
        cx, ax = self.C @ x, self.A @ x
        cand = list(np.argsort(-(np.abs(cx) + np.abs(ax)))[:self.topr])
        best = (-2, None, None)
        for k in range(1, m + 1):
            for S in itertools.combinations(cand, k):
                heads = range(k) if (k > 1 and self.hw != 1.0) else [0]
                for h in heads:
                    S2 = [S[h]] + [r for i, r in enumerate(S) if i != h]
                    w = np.array([1.0] + [self.hw] * (k - 1))
                    G = self.grid(tuple(self.has[S2]))
                    idx = S2 + [self.R + r for r in S2]
                    U = np.concatenate([np.broadcast_to(w, G.shape), w * self.s * G], 1)
                    dot = U @ np.concatenate([cx[S2], ax[S2]])
                    nrm = ((U @ self.G[np.ix_(idx, idx)]) * U).sum(1)
                    cos = dot / np.sqrt(np.maximum(nrm, 1e-9))
                    i = int(np.argmax(cos))
                    if cos[i] > best[0]:
                        best = (cos[i], S2, G[i], w)
        _, S, v, w = best
        return S, v, self.decode(S, v)

    def decode(self, S, v):
        w = np.array([1.0] + [self.hw] * (len(S) - 1))
        return (w[:, None] * (self.C[S] + (self.s * np.asarray(v))[:, None] * self.A[S])).sum(0)

    def design(self, codes):
        """Строки матрицы M: y_i = M_i @ [C; A] (для обучения словаря)."""
        Mx = np.zeros((len(codes), 2 * self.R))
        for i, (S, v, _) in enumerate(codes):
            w = np.array([1.0] + [self.hw] * (len(S) - 1))
            Mx[i, S] += w
            Mx[i, [self.R + r for r in S]] += w * self.s * np.asarray(v)
        return Mx


def encode_all(coder, X, m=3):
    return [coder(x, m) for x in X]


def metrics(data, idx, Y):
    """top1, top10, top50, медиана места, cos(x, y), близость промаха к слову."""
    V, X = data.V, data.V[idx]
    Y = unit(Y)
    sims = Y @ V.T
    tgt = sims[np.arange(len(idx)), idx]
    r = (sims > tgt[:, None]).sum(1) + 1
    guess = np.argmax(sims, 1)
    gs = (V[guess] * X).sum(1)
    miss = r > 1
    return {"top1": np.mean(r == 1), "top10": np.mean(r <= 10), "top50": np.mean(r <= 50),
            "med": int(np.median(r)), "cos": float((Y * X).sum(1).mean()),
            "miss": float(gs[miss].mean()) if miss.any() else float("nan"), "ranks": r}


HEAD = "| top1 | top10 | top50 | медиана | cos(x,y) | промах похож |"
SEP = "| --: | --: | --: | --: | --: | --: |"


def row(m):
    return (f"| {m['top1']:.1%} | {m['top10']:.1%} | {m['top50']:.1%} | {m['med']} "
            f"| {m['cos']:.3f} | {m['miss']:.3f} |")


def fmt_code(names, A, S, v, form="o"):
    parts = []
    for r, lv in zip(S, v):
        if not A[r].any():
            parts.append(names[r])
        else:
            parts.append(f"{names[r]}(={int(lv):+d})".replace("(=+0)", "(=0)"))
    return " ".join(parts) + f" | {form}"
