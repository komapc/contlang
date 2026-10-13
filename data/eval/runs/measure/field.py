# Близость первого ответа: cos (Numberbatch) первого ответа читателя с ближайшим синонимом слова (WordNet), по всем вариантам одного кода.
#   .venv/bin/python data/eval/runs/measure/field.py data/raw/numberbatch-en-19.08.txt.gz
import gzip, json, os, re, sys, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); E = f"{D}/.."
items = json.load(open(f"{E}/twowords2/items.json")); N = len(items)
V = {"A нынешний": "twowords2/a", "B выбор модели из 8": "twowords2/b", "T род по таксономии": "taxonomy/t", "M корни модели + значения математики": "taxonomy/mr",
     "N перенесённый словарь": "distill/n", "S толкование": "definition/s", "B5 резко": "bold/b5", "TZ": "measure/tz", "SZ": "measure/sz", "MZ": "measure/mz",
     "H код модели (идеал)": "twowords3/h", "E пара словами": "twowords2/e"}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for name, d in V.items():
    for k in "12":
        for r in "12":
            for l in open(f"{E}/{d}/ans_{k}_{r}.md"):
                m = re.match(r"\s*(\d+)\.\s*(.*)", l)
                if m and 1 <= int(m[1]) <= 50: ans[(name, r, (int(k) - 1) * 50 + int(m[1]) - 1)] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()][:1]
def syn(w):
    out = {w}
    for p in "nvar": b = wn.morphy(w, p) or w; out |= {b} | {l.name().lower() for s in wn.synsets(b, p) for l in s.lemmas()}
    return out
S = [syn(it["w"]) for it in items]
want = set().union(*S) | {w for ps in ans.values() for p in ps for w in toks(p) + ["_".join(toks(p))]}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in want: x = np.array(l.split()[1:], float); vec[w] = x / np.linalg.norm(x)
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
def cos(p, i):
    if "_".join(toks(p)) in S[i] or any(wn.morphy(t) in S[i] for t in toks(p)): return 1.0
    v = pv(p); s = [float(vec[x] @ v) for x in S[i] if x in vec]
    return max(s) if v is not None and s else 0.0
C = {n: np.array([[cos(ans[(n, r, i)][0], i) if (n, r, i) in ans else 0 for r in "12"] for i in range(N)]) for n in V}
rng = np.random.default_rng(0)
print("вариант | среднее cos | ≥ 0,3 | ≥ 0,5 | точно")
for n in V:
    c = C[n].ravel(); bs = [c[rng.integers(0, len(c), len(c))].mean() for _ in range(2000)]
    print(f"{n} | {c.mean():.2f} [{np.percentile(bs, 2.5):.2f}–{np.percentile(bs, 97.5):.2f}] | {(c >= .3).mean():.0%} | {(c >= .5).mean():.0%} | {(c >= .999).mean():.0%}")
print("\nкалибровка (первый ответ → слово, cos):")
for n in ["A нынешний", "H код модели (идеал)"]:
    for i in range(0, N, 9): print(f"  {n[:1]} {items[i]['w']} ← {ans.get((n, '1', i), ['—'])[0]}: {C[n][i, 0]:.2f}")
