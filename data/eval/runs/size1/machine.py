"""size1, for curiosity: the same curve for a machine code with no human-learnability limit.

Vocabulary: Brown content lemmas (same counts as run.py) that have a ConceptNet Numberbatch vector. Base units: K = 82
directions (top principal components of the vocabulary vectors, i.e. the best 82 axes a machine could pick; same count as
min-co's 82 units). A word is coded by its coordinates on these axes with CONTINUOUS values:
  sparse r = 1, 2, 3 — keep only the r largest coordinates (like 1–3 roots with a value each);
  dense — all 82 coordinates (a vector of 82 numbers per word);
  dense ±5 — all 82, each rounded to 11 levels like min-co's -5..+5.
Decoding: nearest vocabulary vector (cosine). Read "close" if the decoded lemma is the word itself or shares a WordNet
synset with it. Lexicon: the N most frequent lemmas are remembered exactly (a_lex = 1).
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size1/machine.py → machine.json, machine.txt
"""
import gzip
import json
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
from run import brown_counts  # noqa: E402

K = 82
NS = (0, 10, 20, 50, 100, 200, 300, 500, 1000, 2000, 3000, 5000, 10000)


def main():
    from nltk.corpus import wordnet as wn
    c = brown_counts()
    tot = {w: sum(v.values()) for w, v in c.items()}
    order = sorted(tot, key=lambda w: -tot[w])
    want = set(order)
    vec = {}
    with gzip.open(D.parents[3] / "data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
        next(f)
        for line in f:
            w, rest = line.split(" ", 1)
            if w in want:
                vec[w] = np.array(rest.split(), dtype=np.float32)
    words = [w for w in order if w in vec]
    X = np.stack([vec[w] for w in words])
    X /= np.linalg.norm(X, axis=1, keepdims=True)
    mu = X.mean(0)
    Xc = X - mu
    _, _, Vt = np.linalg.svd(Xc, full_matrices=False)
    P = Vt[:K]                                   # K axes
    Z = Xc @ P.T                                 # coordinates
    syn = {w: {l.name().lower() for s in wn.synsets(w) for l in s.lemmas()} | {w} for w in words}
    scale = np.abs(Z).max(0)

    def decode(Zh):
        Y = Zh @ P + mu
        Y /= np.linalg.norm(Y, axis=1, keepdims=True) + 1e-9
        hit = np.zeros(len(words), bool)
        for a in range(0, len(words), 2000):
            j = (Y[a:a + 2000] @ X.T).argmax(1)
            hit[a:a + 2000] = [words[jj] in syn[words[a + t]] for t, jj in enumerate(j)]
        return hit

    codes = {}
    for r in (1, 2, 3):
        Zh = np.zeros_like(Z)
        idx = np.argsort(-np.abs(Z), axis=1)[:, :r]
        np.put_along_axis(Zh, idx, np.take_along_axis(Z, idx, 1), 1)
        codes[f"sparse {r}"] = Zh
    codes["dense"] = Z
    codes["dense ±5"] = np.round(Z / scale * 5) / 5 * scale
    T = sum(tot.values())
    Tv = sum(tot[w] for w in words)
    out = [f"vocabulary with vectors: {len(words)} of {len(order)} lemmas, {Tv / T:.0%} of tokens; K = {K} axes "
           f"(explain {np.sum(np.linalg.svd(Xc, compute_uv=False)[:K] ** 2) / np.sum(Xc ** 2):.0%} of variance)", ""]
    res = []
    rank = {w: i for i, w in enumerate(order, 1)}
    for name, Zh in codes.items():
        hit = decode(Zh)
        hw = dict(zip(words, hit))
        out.append(f"{name}: words decoded close {hit.mean():.0%} (type), "
                   f"{sum(tot[w] for w in words if hw[w]) / Tv:.0%} (token, among words with vectors)")
        for N in NS:
            u = sum(tot[w] for w in order if rank[w] <= N or hw.get(w, False)) / T
            res.append({"code": name, "N": N, "L": K + N, "U": u})
        out.append("  U by N: " + ", ".join(f"{x['N']}: {x['U']:.0%}" for x in res if x["code"] == name))
    json.dump(res, open(D / "machine.json", "w"), indent=0)
    (D / "machine.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


main()
