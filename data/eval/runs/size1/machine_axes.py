"""size1, for curiosity: "if I learn X axes, how surely do I guess the word?" — PCA axes vs min-co roots.

Machine: X = the top X principal components of ConceptNet Numberbatch vectors of 21.5k Brown content lemmas. A word is
written as its values on the r axes where it lies furthest (r = 1, 2, 3, 6, 9) or on all X, each value rounded to 11 levels
like min-co's -5..+5. The reader decodes by the nearest word vector, with a word-frequency prior (the human/LLM reader
also prefers common words; its weight is tuned once for the machine's benefit).
"Close" for the machine is a proxy calibrated on size1's own judged answers: same word, a WordNet synonym, or vector cosine
to the target at least θ, where θ best reproduces the judges' "close" on the 1440 judged reader answers.
Result is token-weighted over Brown (like U at N = 0). min-co / Toki Pona points are the measured size1 values (N = 0).
    NLTK_DATA=data/raw/nltk .venv/bin/python data/eval/runs/size1/machine_axes.py → axes.json, axes.txt
"""
import gzip
import json
import re
import sys
from pathlib import Path

import numpy as np

D = Path(__file__).resolve().parent
sys.path.insert(0, str(D))
from run import brown_counts, parse_numbered  # noqa: E402

XS = (5, 10, 20, 30, 51, 82, 120, 200, 300)
RS = (1, 2, 3, 6, 9, "all")


def main():
    from nltk.corpus import wordnet as wn
    c = brown_counts()
    tot = {w: sum(v.values()) for w, v in c.items()}
    order = sorted(tot, key=lambda w: -tot[w])
    items = json.load(open(D / "items.json"))
    lists = json.load(open(D / "lists.json"))
    ans = {}
    for l in lists:
        a = parse_numbered(D / f"answers/read_{l['r']}.md")
        for t, (i, k) in enumerate(l["order"], 1):
            ans[(l["r"], i, k)] = a.get(t, "—").split("|")[0].strip().lower()
    judged = {}
    for j in (1, 2, 3):
        ks = json.load(open(D / f"answers/judge_j{j}_keys.json"))
        s = parse_numbered(D / f"answers/judge_j{j}.md")
        for t, key in enumerate(ks, 1):
            if t in s and s[t][:1].isdigit():
                judged.setdefault(tuple(key), []).append(int(s[t][0]))
    want = set(order) | {re.sub(r"[^a-z ]", "", a).replace(" ", "_") for a in ans.values()}
    vec = {}
    with gzip.open(D.parents[3] / "data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
        next(f)
        for line in f:
            w, rest = line.split(" ", 1)
            if w in want:
                v = np.array(rest.split(), dtype=np.float32)
                vec[w] = v / np.linalg.norm(v)
    syn = lambda w: {l.name().lower() for s in wn.synsets(w) for l in s.lemmas()} | {w}

    # --- calibrate the "close" proxy on judged human answers
    rows = []
    for (r, i, k), v in judged.items():
        tgt = items[i]["w"]
        a = re.sub(r"[^a-z ]", "", ans[(r, i, k)]).replace(" ", "_")
        a = wn.morphy(a) or a
        same = a in syn(tgt)
        cos = float(vec[tgt] @ vec[a]) if tgt in vec and a in vec else -1.0
        rows.append((same, cos, np.mean(v) >= 1.5))
    best = max(np.arange(0.2, 0.95, 0.01), key=lambda th: np.mean([(s or co >= th) == y for s, co, y in rows]))
    agree = np.mean([(s or co >= best) == y for s, co, y in rows])
    base = np.mean([y for *_, y in rows])

    words = [w for w in order if w in vec]
    X = np.stack([vec[w] for w in words])
    mu = X.mean(0)
    Xc = X - mu
    _, sv, Vt = np.linalg.svd(Xc, full_matrices=False)
    logf = np.log(np.array([tot[w] for w in words], dtype=np.float32))
    synw = [syn(w) for w in words]
    wt = np.array([tot[w] for w in words], dtype=np.float64)
    T = sum(tot.values())

    def close_rate(Zh, P, beta):
        Y = Zh @ P + mu
        Y /= np.linalg.norm(Y, axis=1, keepdims=True) + 1e-9
        hit = np.zeros(len(words), bool)
        for a in range(0, len(words), 2000):
            j = (Y[a:a + 2000] @ X.T + beta * logf).argmax(1)
            for t, jj in enumerate(j):
                n = a + t
                hit[n] = words[jj] in synw[n] or float(X[n] @ X[jj]) >= best
        return (wt * hit).sum() / T

    def code(Xn, r):
        P = Vt[:Xn]
        Z = Xc @ P.T
        sc = np.percentile(np.abs(Z), 99, axis=0)
        Zq = np.clip(np.round(Z / sc * 5), -5, 5) / 5 * sc
        if r == "all":
            return Zq, P
        Zh = np.zeros_like(Zq)
        idx = np.argsort(-np.abs(Z), axis=1)[:, :r]
        np.put_along_axis(Zh, idx, np.take_along_axis(Zq, idx, 1), 1)
        return Zh, P

    Zh, P = code(51, 3)
    sub = slice(None, None, 4)
    betas = (0.0, 0.01, 0.02, 0.04, 0.08)
    def tune_rate(beta):
        Y = Zh[sub] @ P + mu
        Y /= np.linalg.norm(Y, axis=1, keepdims=True)
        j = (Y @ X.T + beta * logf).argmax(1)
        idx = np.arange(len(words))[sub]
        return np.mean([words[jj] in synw[n] or float(X[n] @ X[jj]) >= best for n, jj in zip(idx, j)])
    beta = max(betas, key=tune_rate)

    res = []
    for Xn in XS:
        for r in RS:
            if r != "all" and r > Xn:
                continue
            Zh, P = code(Xn, r)
            res.append({"X": Xn, "r": r, "U": close_rate(Zh, P, beta)})
            print(Xn, r, f"{res[-1]['U']:.1%}", flush=True)
    json.dump({"theta": float(best), "beta": beta, "res": res}, open(D / "axes.json", "w"), indent=0)
    out = [f"vocabulary {len(words)} lemmas; close proxy: same/synonym or cosine ≥ {best:.2f} — agrees with the judges' "
           f"close on {agree:.0%} of {len(rows)} judged answers (judges' close rate {base:.0%}); frequency prior β = {beta}",
           f"variance explained by top X axes: " + ", ".join(f"{x}: {np.sum(sv[:x] ** 2) / np.sum(sv ** 2):.0%}" for x in XS), "",
           "| axes X | " + " | ".join(f"{r} value{'s' if r != 1 else ''}" if r != "all" else "all X values" for r in RS) + " |",
           "|---|" + "---|" * len(RS)]
    for Xn in XS:
        cell = {x["r"]: x["U"] for x in res if x["X"] == Xn}
        out.append(f"| {Xn} | " + " | ".join(f"{100 * cell[r]:.0f} %" if r in cell else "—" for r in RS) + " |")
    (D / "axes.txt").write_text("\n".join(out) + "\n")
    print("\n".join(out))


main()
