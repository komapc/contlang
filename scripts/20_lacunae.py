"""Лакуны: перевод без ограничения числа корней (см. docs/math.md, раздел 6).

Каждое из 10 000 частых слов (как на сайте, без слов-полюсов) кодируется
жадно: на каждом шаге добавляется корень с лучшим уровнем, пока растёт
cos(x, y); вес главного корня 1, остальных 0,6, уровни −5…+5 — та же модель
языка, только без предела m. Для сравнения — «потолок»: проекция слова на все
центры и оси с любыми вещественными коэффициентами.

Попадание: среди 10 ближайших к коду слов есть слово с той же основой (Porter;
часть речи и форма не важны). Промахи — лакуны: остатки x − y кластеризуются
(k-means), для кластера печатаются слова, ближайшие к среднему остатку
(«чего не хватает»), и сами слова-промахи.

    .venv/bin/python scripts/20_lacunae.py   → data/lacunae.md
"""
import importlib.util
import sys
from pathlib import Path

import numpy as np
from nltk.stem import PorterStemmer
from sklearn.cluster import KMeans

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from lib_code import LEVELS, Data, root_specs, s15, unit, wordlist  # noqa: E402

_b = importlib.util.spec_from_file_location("bm", Path(__file__).with_name("site") / "build_math.py")
bm = importlib.util.module_from_spec(_b)
_b.loader.exec_module(bm)

S, HW, K, TOP = 0.4, 0.6, 25, 10


def greedy(X, C, A):
    """Жадный код без предела числа корней; X — N×d. Возвращает Y, коды, число корней."""
    R = len(C)
    has = A.any(1)
    cand = [(r, v) for r in range(R) for v in (LEVELS if has[r] else [0])]
    D = np.stack([C[r] + S * v * A[r] for r, v in cand])          # P×d
    rid = np.array([r for r, _ in cand])
    N = len(X)
    Y = np.zeros_like(X)
    used = np.zeros((N, R), bool)
    best = np.full(N, -2.0)
    codes = [[] for _ in range(N)]
    active = np.ones(N, bool)
    DD = (D * D).sum(1)
    while active.any():
        idx = np.where(active)[0]
        w = np.where(used[idx].any(1), HW, 1.0)[:, None]          # первый корень — главный
        Ya = Y[idx]
        num = (X[idx] * Ya).sum(1)[:, None] + w * (X[idx] @ D.T)
        nrm = (Ya * Ya).sum(1)[:, None] + 2 * w * (Ya @ D.T) + w * w * DD[None]
        cos = num / np.sqrt(np.maximum(nrm, 1e-9))
        cos[used[idx][:, rid]] = -2
        j = cos.argmax(1)
        c = cos[np.arange(len(idx)), j]
        up = c > best[idx] + 1e-4
        for i, jj, ok, ww in zip(idx, j, up, w[:, 0]):
            if ok:
                Y[i] += ww * D[jj]
                used[i, rid[jj]] = True
                codes[i].append(cand[jj])
            else:
                active[i] = False
        best[idx[up]] = c[up]
    return Y, codes


def main():
    specs = root_specs()
    d = Data([specs])
    names, C, A = d.dictionary(specs)
    cand = bm.frequent_words(int(bm.N * 1.6))
    vec = s15.load_subset(set(cand))
    words = [w for w in cand if w in vec][:bm.N]
    words = [w for w in words if w not in d.poles]
    X = unit(np.stack([vec[w] for w in words]))
    st = PorterStemmer()
    stem = np.array([st.stem(w) for w in words])

    def hits(Y):
        sims = unit(Y) @ X.T
        top = np.argsort(-sims, 1)[:, :TOP]
        return (stem[top] == stem[:, None]).any(1), top

    Y, codes = greedy(X, C, A)
    hit, top = hits(Y)
    M = np.concatenate([C, A[A.any(1)]])
    P = X @ np.linalg.pinv(M) @ M                               # потолок: любые коэффициенты
    hit_ls, _ = hits(P)
    m = np.array([len(c) for c in codes])
    cos = (unit(Y) * X).sum(1)

    # лакуны ищем среди обычных слов (список 3000 частых с частью речи): имена,
    # страны и города по правилам языка идут в кавычках
    common = np.isin(words, wordlist()[0])
    miss = np.where(~hit & common)[0]
    Rz = unit(X[miss] - unit(Y[miss]) * cos[miss, None])
    km = KMeans(K, n_init=4, random_state=0).fit(Rz)
    out = ["# Лакуны: перевод без ограничения числа корней", "",
           f"Скрипт `scripts/20_lacunae.py`. {len(words)} частых слов (без слов-полюсов), словарь — корни из полюсов "
           f"({len(names)} корней). Попадание — среди {TOP} ближайших к коду есть слово с той же основой.", "",
           "| кодер | в top10 | cos(x,y) | корней в коде (медиана / макс.) |", "| :-- | --: | --: | --: |",
           f"| жадный, без предела корней, целые уровни | {hit.mean():.1%} | {cos.mean():.3f} | {int(np.median(m))} / {m.max()} |",
           f"| то же, только обычные слова ({common.sum()}) | {hit[common].mean():.1%} | {cos[common].mean():.3f} | {int(np.median(m[common]))} / {m[common].max()} |",
           f"| потолок: проекция на все центры и оси | {hit_ls.mean():.1%} | {(unit(P) * X).sum(1).mean():.3f} | все |", "",
           "Потолок — хеш-эффект (docs/math.md, раздел 3): 84 свободных коэффициента различают почти любое слово, "
           "смысла это не добавляет; для лакун он не годится.", "",
           f"Промахи среди всех слов — большей частью имена, страны, города, названия (идут в кавычках). "
           f"Ниже — только обычные слова: {len(miss)} промахов из {common.sum()}.", "",
           "## Кластеры промахов", "",
           "Слова, ближайшие к среднему остатку (чего не хватает коду), и промахи кластера (первые по частоте).", ""]
    order = np.argsort(-np.bincount(km.labels_, minlength=K))
    for k in order:
        mem = miss[km.labels_ == k]
        cen = unit(km.cluster_centers_[k])
        near = [words[i] for i in np.argsort(-(X @ cen))[:8]]
        out += [f"### {len(mem)} слов: {', '.join(near[:4])}", "",
                f"- остаток ближе всего к: {', '.join(near)}",
                f"- промахи: {', '.join(words[i] for i in sorted(mem)[:25])}", ""]
    out += ["## Примеры кодов промахов", "", "| слово | код | ближайшие к коду |", "| :-- | :-- | :-- |"]
    for i in sorted(miss)[:40]:
        code = " ".join(names[r] if not A[r].any() else f"{names[r]}(={v:+d})".replace("(=+0)", "(=0)") for r, v in codes[i])
        out.append(f"| {words[i]} | `{code}` | {', '.join(words[j] for j in top[i][:5])} |")
    (ROOT / "data" / "lacunae.md").write_text("\n".join(out) + "\n")
    print("\n".join(out[:12]))


if __name__ == "__main__":
    main()
