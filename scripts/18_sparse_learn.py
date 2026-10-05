"""Обучение словаря корней на словах при условии читаемости (docs/math.md).

Чередование: при фиксированных кодах направления корней (центр c_r и ось
a_r) подбираются гребневой регрессией с притяжением к исходным (из полюсов
roots.yaml, вес lam); затем атомы нормируются, и если атом ушёл от исходного
дальше, чем cos < TAU, он возвращается по дуге до cos = TAU; затем слова
кодируются заново. Учимся на 70% слов, всё оценивается на отложенных 30%.

Пишет data/sparse_learn.md и data/sparse_dict_learned.npz (словарь только
для анализа: в roots.yaml остаются человеческие списки полюсов).
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from lib_code import (HEAD, SEP, Coder, Data, encode_all, fmt_code, metrics,  # noqa: E402
                      root_specs, row, unit)

LAM, TAU, ITERS, HW = 30.0, 0.85, 3, 0.6
OUT = ROOT / "data" / "sparse_learn.md"
NPZ = ROOT / "data" / "sparse_dict_learned.npz"
SHOW = ("river knife bank teacher city money anger hope winter child friend "
        "doctor computer kitchen").split()


def clamp(new, old, tau):
    """Вернуть единичный атом new к old по дуге, пока cos(new, old) < tau."""
    c = new @ old
    if c >= tau:
        return new
    perp = unit(new - c * old)
    return tau * old + np.sqrt(1 - tau ** 2) * perp


def learn(d, C0, A0, lam=LAM, tau=TAU, iters=ITERS, hw=HW, log=None):
    R, has = len(C0), A0.any(1)
    Th0 = np.concatenate([C0, A0])
    C, A = C0.copy(), A0.copy()
    Xtr = d.V[d.train]
    for it in range(iters):
        co = Coder(C, A, head_w=hw)
        codes = encode_all(co, Xtr)
        M = co.design(codes)
        Y = M @ np.concatenate([C, A])
        T = np.linalg.norm(Y, axis=1)[:, None] * Xtr
        Th = unit(np.linalg.solve(M.T @ M + lam * np.eye(2 * R), M.T @ T + lam * Th0))
        for i in range(2 * R):
            if i >= R and not has[i - R]:
                Th[i] = 0
            else:
                Th[i] = clamp(Th[i], Th0[i], tau)
        C, A = Th[:R], Th[R:]
        if log is not None:
            m = metrics(d, d.train, np.stack([e[2] for e in codes]))
            log.append(f"итерация {it + 1}: на обучающих словах до шага top1 {m['top1']:.1%}, cos {m['cos']:.3f}")
    return C, A


def main():
    specs = root_specs()
    d = Data([specs])
    names, C0, A0 = d.dictionary(specs)
    has = A0.any(1)
    Xte = d.V[d.test]

    L = ["# Обучение словаря корней при условии читаемости", "",
         f"Numberbatch, {len(d.vocab)} слов (без слов-полюсов), обучение {len(d.train)}, "
         f"**тест {len(d.test)}** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. "
         "Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).", "",
         "| словарь | " + HEAD[2:], "| :-- " + SEP]
    rows = {}
    for label, hw in (("корни из полюсов, порядок не важен", 1.0), (f"корни из полюсов, вес не главных {HW}", HW)):
        Y = np.stack([e[2] for e in encode_all(Coder(C0, A0, head_w=hw), Xte)])
        rows[label] = metrics(d, d.test, Y)
        L.append(f"| {label} " + row(rows[label]))
        print(L[-1], flush=True)
    log = []
    C, A = learn(d, C0, A0, log=log)
    co = Coder(C, A, head_w=HW)
    enc = encode_all(co, Xte)
    ml = metrics(d, d.test, np.stack([e[2] for e in enc]))
    L.append(f"| обученные (λ = {LAM:g}, cos с исходным ≥ {TAU}, вес {HW}) " + row(ml))
    print(L[-1], flush=True)
    sc, sa = (C * C0).sum(1), (A[has] * A0[has]).sum(1)
    L += ["", f"Сдвиг корней: cos(центр, исходный) в среднем {sc.mean():.2f} (минимум {sc.min():.2f}), "
          f"cos(ось, исходная) в среднем {sa.mean():.2f} (минимум {sa.min():.2f}). " + "; ".join(log) + ".", ""]

    nb = lambda v, k=5: ", ".join(d.vocab[i] for i in np.argsort(-(d.V @ unit(v)))[:k])  # noqa: E731
    L += ["## Читаемость: ближайшие слова к полюсам до и после обучения", "",
          "| корень | cos | + до | + после | − до | − после |", "| :-- | --: | :-- | :-- | :-- | :-- |"]
    for r, n in enumerate(names):
        if has[r]:
            L.append(f"| {n} | {min(C[r] @ C0[r], A[r] @ A0[r]):.2f} | {nb(C0[r] + A0[r])} | {nb(C[r] + A[r])} "
                     f"| {nb(C0[r] - A0[r])} | {nb(C[r] - A[r])} |")
        else:
            L.append(f"| {n} | {C[r] @ C0[r]:.2f} | {nb(C0[r])} | {nb(C[r])} | | |")

    pos = {d.vocab[i]: j for j, i in enumerate(d.test)}
    L += ["", "## Примеры (тестовые слова, обученный словарь)", "",
          "| слово | код | место | ближайшие к декодированному |", "| :-- | :-- | --: | :-- |"]
    for w in SHOW:
        if w in pos:
            S, v, y = enc[pos[w]]
            L.append(f"| {w} | `{fmt_code(names, A, S, v, 'o').replace('|', chr(92) + '|')}` "
                     f"| {ml['ranks'][pos[w]]} | {nb(y)} |")
    OUT.write_text("\n".join(L) + "\n", encoding="utf8")
    np.savez(NPZ, names=np.array(names), C=C, A=A, C0=C0, A0=A0)
    print("\n".join(L[-len(SHOW) - 2:]))


if __name__ == "__main__":
    main()
