# «Два слова» 2: место с синонимами (как ../twowords). A — один код, B — код, выбранный моделью, C — пара кодами математики,
# D — пара кодами, выбранными моделью, E — пара словами. 100 существительных × 2 читателя Haiku на вариант; ответы v/ans_K_R.md.
#   .venv/bin/python data/eval/runs/twowords2/score.py data/raw/numberbatch-en-19.08.txt.gz
import gzip, json, os, re, sys, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); NB = sys.argv[1]
items = json.load(open(f"{D}/items.json")); N = len(items)
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for v in "abcde":
    for k in "12":
        for r in "12":
            for l in open(f"{D}/{v}/ans_{k}_{r}.md"):
                m = re.match(r"\s*(\d+)\.\s*(.*)", l)
                if m and 1 <= int(m[1]) <= 50: ans[(v, r, (int(k) - 1) * 50 + int(m[1]) - 1)] = [x.strip() for x in re.split(r"[|,]", m[2]) if x.strip()]
def syn(w):
    out = {w}
    for p in "nvar":
        b = wn.morphy(w, p) or w
        out |= {b} | {l.name().lower() for s in wn.synsets(b, p) for l in s.lemmas()}
    return out
words = json.load(open(f"{D}/../../../../site/data/math.json"))["words"]
S = [syn(it["w"]) for it in items]
vec = {}
with gzip.open(NB, "rt") as fh:
    next(fh); want = set(words) | set().union(*S) | {w for ps in ans.values() for p in ps for w in toks(p) + ["_".join(toks(p))]}
    for l in fh:
        w = l[:l.find(" ")]
        if w in want: x = np.array(l.split()[1:], float); vec[w] = x / np.linalg.norm(x)
W = [w for w in words if w in vec]; W += [w for s in S for w in s if w in vec and w not in set(W)]
WI = {w: i for i, w in enumerate(W)}; M = np.stack([vec[w] for w in W])
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
def place(p, i):
    if "_".join(toks(p)) in S[i] or any(wn.morphy(t) in S[i] for t in toks(p)): return 1
    v = pv(p); ix = [WI[x] for x in S[i] if x in WI]
    if v is None or not ix: return len(W)
    s = M @ v; return int((s > s[ix].max()).sum()) + 1
gm = lambda xs: round(float(np.exp(np.mean(np.log(xs)))), 1)
P = {v: np.array([[place(ans[(v, r, i)][0], i) if (v, r, i) in ans else len(W) for r in "12"] for i in range(N)]) for v in "abcde"}
top3 = {v: sum(any(place(p, i) == 1 for p in ans.get((v, r, i), [])[:3]) for i in range(N) for r in "12") for v in "abcde"}
NAME = {"a": "A один код", "b": "B код, выбранный моделью", "c": "C пара кодами математики", "d": "D пара кодами, выбранными моделью", "e": "E пара словами"}
for v in "abcde":
    print(f"{NAME[v]}: место (геом. среднее) {gm(P[v].ravel())}, первым {int((P[v] == 1).sum())}/{2 * N}, в тройке {top3[v]}/{2 * N}")
json.dump({v: P[v].tolist() for v in P}, open(f"{D}/places.json", "w"))
rng = np.random.default_rng(0)
for x, y in (("b", "a"), ("c", "a"), ("d", "a"), ("d", "c"), ("d", "b"), ("e", "d")):
    rat = (np.log(P[x]) - np.log(P[y])).mean(1); bs = [np.exp(rat[rng.integers(0, N, N)].mean()) for _ in range(5000)]
    print(f"{x.upper()} / {y.upper()} {np.exp(rat.mean()):.2f} 95 % {np.round(np.percentile(bs, [2.5, 97.5]), 2)}  (< 1 — {x.upper()} лучше)")
print()
for i, it in enumerate(items):
    print(f"{it['w']} [{it['pair']}]: " + " | ".join(f"{v.upper()} {[ans.get((v, r, i), ['—'])[0] for r in '12']}" for v in "abcde") + f"\n    B `{it['B']}`  D `{it['D']}`")
