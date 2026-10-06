"""Данные для математического кодера на сайте: site/data/math.json и site/data/vocab.bin.

Нужны numpy и сырые векторы (data/raw), поэтому запускается локально, не в CI:
    .venv/bin/python scripts/site/build_math.py

math.json: корни (порядок roots.yaml), признак оси, два словаря — «полюса» (из
semaxis в roots.yaml) и «обученный» (data/sparse_dict_learned.npz, только
анализ, см. docs/math.md) — как матрицы C (центры) и A (оси), параметры кодера
(s, вес не главных, topr), 10 главных компонент исходного пространства (направления,
разброс, по пять слов на полюсах) и хеш полюсов, чтобы build.py --check заметил устаревание.
vocab.bin: N слов × 300 int8 (единичный вектор × 127), слова — в math.json,
по частоте (порядок словаря GloVe wiki-gigaword), только те, что есть в Numberbatch.
"""
import gzip
import json
import sys
from pathlib import Path

import numpy as np

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "scripts"))
from lib_code import Data, root_specs, s15, unit  # noqa: E402
from mincode import spec  # noqa: E402

N = 10000
OUT = REPO / "site" / "data"


def frequent_words(n):
    out = []
    with gzip.open(REPO / "data" / "raw" / "gensim" / "glove-wiki-gigaword-100" / "glove-wiki-gigaword-100.gz", "rt", encoding="utf8") as f:
        for line in f:
            w = line.split(" ", 1)[0]
            if w.isalpha() and w.isascii() and len(w) > 1:
                out.append(w)
                if len(out) >= n:
                    break
    return out


def main():
    specs = root_specs()
    d = Data([specs])
    names, C0, A0 = d.dictionary(specs)
    D = np.load(REPO / "data" / "sparse_dict_learned.npz")
    assert list(D["names"]) == names, "обученный словарь устарел: перезапустите scripts/18_sparse_learn.py"
    assert names == [r["name"] for r in spec.axis_roots() + spec.noaxis_roots()], "порядок корней в lib_code.NOAXIS не совпадает с roots.yaml"
    cand = frequent_words(int(N * 1.6))
    vec = s15.load_subset(set(cand) | set(d.vec))
    words = [w for w in cand if w in vec][:N]
    X = unit(np.stack([vec[w] for w in words]))
    (OUT / "vocab.bin").write_bytes(np.round(X * 127).astype(np.int8).tobytes())
    # 10 главных компонент исходного пространства (по этим же словам): направление, разброс, слова на полюсах
    mean = X.mean(0)
    U, sv, Vt = np.linalg.svd(X - mean, full_matrices=False)
    pcs, sd = Vt[:10], sv[:10] / np.sqrt(len(X))
    Z = (X - mean) @ pcs.T
    poles = [{"neg": [words[i] for i in np.argsort(Z[:, k])[:5]], "pos": [words[i] for i in np.argsort(-Z[:, k])[:5]],
              "var": float(sv[k] ** 2 / (sv ** 2).sum())} for k in range(10)]
    r4 = lambda M: np.round(M, 5).tolist()  # noqa: E731
    js = {"names": names, "has_axis": [bool(a.any()) for a in A0], "dim": X.shape[1], "s": 0.4, "head_w": 0.6, "topr": 8,
          "poles_hash": spec.poles_hash(), "words": words,
          "pca": {"mean": np.round(mean, 5).tolist(), "pcs": np.round(pcs, 5).tolist(), "sd": np.round(sd, 5).tolist(), "poles": poles},
          "dicts": {"poles": {"C": r4(C0), "A": r4(A0)}, "learned": {"C": r4(D["C"]), "A": r4(D["A"])}}}
    (OUT / "math.json").write_text(json.dumps(js, separators=(",", ":")), encoding="utf8")
    print(f"слов {len(words)}, vocab.bin {(OUT / 'vocab.bin').stat().st_size // 1024} КБ, math.json {(OUT / 'math.json').stat().st_size // 1024} КБ")


if __name__ == "__main__":
    main()
