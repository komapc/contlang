"""Word-level round trip: word -> k quantized axes -> nearest OTHER word.

We do not expect to get the same word back; we expect a word close in meaning and form.
Metrics (held-out words), per embedding source, k and axis method:
  cos      cosine between the reconstruction and the original vector (full space)
  top10/50 the decoded word is among the original's 10/50 true nearest neighbours
  wup      WordNet Wu-Palmer similarity between original and decoded word (same-POS pairs only);
           baselines: true nearest neighbour in the full space, and a random same-POS word
  pos      decoded word has the same part of speech as the original (baseline: majority class)
Axes are fitted on a train split.
"""
import sys

import numpy as np
from common import ROOT, SOURCES, word_matrix
from lib_axes import (dequantize, fit_axes, make_wup, nearest_other,
                      quantize)

LIST = sys.argv[1] if len(sys.argv) > 1 else "wordlist_en_x5.tsv"
KS = [10, 30, 100]
SEED = 0


rows = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / LIST)][1:]
words = [r[0] for r in rows]
pos = np.array([r[1] for r in rows])
n = len(words)
rng = np.random.default_rng(SEED)
perm = rng.permutation(n)
train, test = perm[: n // 2], perm[n // 2:]
test = test[:600]  # wordnet lookups dominate the runtime

_, mean_wup = make_wup(words, pos)


majority = max((pos == c).mean() for c in set(pos))
out = [f"# Round-trip: слово → k осей (11 уровней) → ближайшее другое слово\n",
       f"{n} слов ({len(train)} train, {len(test)} test), кандидаты — все {n}. "
       "Ожидание — не то же слово, а близкое по смыслу и форме.\n",
       "- **cos** — косинус реконструкции с оригиналом (полное пространство);\n"
       "- **top10 / top50** — найденное слово среди 10 / 50 истинных соседей оригинала;\n"
       "- **wup** — WordNet Wu-Palmer между оригиналом и найденным (только пары одной части речи); "
       "ориентиры: истинный ближайший сосед и случайное слово той же части речи;\n"
       f"- **pos** — часть речи найденного слова совпала (базовый уровень {majority:.0%}).\n"]
examples = []

for src in SOURCES:
    X = word_matrix(src, words)
    X = X / np.linalg.norm(X, axis=1, keepdims=True)
    Xtr = X[train]
    sims_full = X[test] @ X.T
    sims_full[np.arange(len(test)), test] = -np.inf
    true_order = np.argsort(-sims_full, axis=1)
    true10 = [set(r[:10]) for r in true_order]
    true50 = [set(r[:50]) for r in true_order]
    nn_true = true_order[:, 0]
    rand = np.array([rng.choice(np.flatnonzero(pos == pos[t])) for t in test])
    out.append(f"## {src}\n")
    out.append(f"Ориентиры wup: истинный сосед {mean_wup(zip(test, nn_true)):.3f}, "
               f"случайное слово той же части речи {mean_wup(zip(test, rand)):.3f}; "
               f"pos у истинного соседа {np.mean(pos[nn_true] == pos[test]):.0%}.\n")
    out.append("| k | метод | cos | top10 | top50 | wup | pos |")
    out.append("| --: | :-- | --: | --: | --: | --: | --: |")
    for k in KS:
        for method in ["pca", "random"]:
            mean, W = fit_axes(method, Xtr, k, np.random.default_rng(SEED + k))
            std = ((Xtr - mean) @ W).std(axis=0)
            Q = quantize((X[test] - mean) @ W, std)
            R = dequantize(Q, std) @ W.T + mean
            nn = nearest_other(R, X, test, 1)[:, 0]
            cos = np.mean(np.sum(R / np.linalg.norm(R, axis=1, keepdims=True) * X[test], axis=1))
            t10 = np.mean([d in s for d, s in zip(nn, true10)])
            t50 = np.mean([d in s for d, s in zip(nn, true50)])
            out.append(f"| {k} | {method} | {cos:.2f} | {t10:.0%} | {t50:.0%} | "
                       f"{mean_wup(zip(test, nn)):.3f} | {np.mean(pos[nn] == pos[test]):.0%} |")
            if method == "pca" and k in (10, 30):
                examples.append((src, k, [(words[t], words[d]) for t, d in zip(test[:24], nn[:24])]))
    out.append("")

out.append("## Примеры (слово → найденное слово)\n")
for src, k, ex in examples:
    out.append(f"**{src}, k={k}:** " + "; ".join(f"{a} → {b}" for a, b in ex) + "\n")

text = "\n".join(out)
(ROOT / "data" / "roundtrip_en.md").write_text(text, encoding="utf-8")
print(text)
