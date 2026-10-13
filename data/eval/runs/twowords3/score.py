# «Два слова» 3: место с синонимами вместе с ответами ../twowords2 (A–E). F — X словом, Y кодом (выбор модели), G — X кодом, Y словом,
# H — один код, написанный моделью, I — пара кодами, написанными моделью. Ответы v/ans_K_R.md.
#   .venv/bin/python data/eval/runs/twowords3/score.py data/raw/numberbatch-en-19.08.txt.gz
# DISTILL=1 — A, B, H и N (кодер с перенесённым словарём, ответы ../distill/n/ans_K_R.md).
# DEF=1 — A, H, S и GTS (кодер-«определение», ответы ../definition/{s,gts}/ans_K_R.md).
# BOLD=1 — A, H, B3 и B5 (кодер «коротко и резко», ответы ../bold/{b3,b5}/ans_K_R.md).
# Проверка другим читателем: SONNET=1 — ответы Sonnet sonnet/v/ans_K_1.md (A, H, I, по одному на половину).
import gzip, json, os, re, sys, numpy as np
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); NB = sys.argv[1]
T = f"{D}/../twowords2"; items = json.load(open(f"{T}/items.json")); SON = os.environ.get("SONNET") == "1"; DIS = os.environ.get("DISTILL") == "1"; DEF = os.environ.get("DEF") == "1"; BOLD = os.environ.get("BOLD") == "1"; VS = "ahi" if SON else "abhn" if DIS else "ahpq" if DEF else "ahjk" if BOLD else "abcdefghi"; RS = "1" if SON else "12"; it3 = json.load(open(f"{D}/items.json")); N = len(items)
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for v in VS:
    for k in "12":
        for r in RS:
            for l in open(f"{D}/sonnet/{v}/ans_{k}_{r}.md" if SON else f"{D}/../distill/n/ans_{k}_{r}.md" if v == "n" else f"{D}/../definition/{ {'p': 's', 'q': 'gts'}[v] }/ans_{k}_{r}.md" if v in "pq" else f"{D}/../bold/{ {'j': 'b3', 'k': 'b5'}[v] }/ans_{k}_{r}.md" if v in "jk" else f"{D if v in 'fghi' else T}/{v}/ans_{k}_{r}.md"):
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
P = {v: np.array([[place(ans[(v, r, i)][0], i) if (v, r, i) in ans else len(W) for r in RS] for i in range(N)]) for v in VS}
top3 = {v: sum(any(place(p, i) == 1 for p in ans.get((v, r, i), [])[:3]) for i in range(N) for r in RS) for v in VS}
NAME = {"a": "A один код", "b": "B код, выбранный моделью", "c": "C пара кодами математики", "d": "D пара кодами, выбранными моделью", "e": "E пара словами", "f": "F X словом, Y кодом", "g": "G X кодом, Y словом", "h": "H один код модели", "i": "I пара кодами модели", "n": "N кодер с перенесённым словарём (../distill)", "p": "S толкование (../definition)", "q": "GTS род + правда + толкование (../definition)", "j": "B3 коротко: 0, ±3, ±5, δ 0,03 (../bold)", "k": "B5 резко: 0, ±5, δ 0,06 (../bold)"}
for v in VS:
    print(f"{NAME[v]}: место (геом. среднее) {gm(P[v].ravel())}, первым {int((P[v] == 1).sum())}/{len(RS) * N}, в тройке {top3[v]}/{len(RS) * N}")
json.dump({v: P[v].tolist() for v in P}, open(f"{D}/places{'_sonnet' if SON else '_distill' if DIS else '_def' if DEF else '_bold' if BOLD else ''}.json", "w"))
rng = np.random.default_rng(0)
for x, y in (("h", "a"), ("i", "a"), ("i", "h")) if SON else (("n", "a"), ("n", "b"), ("h", "n")) if DIS else (("p", "a"), ("q", "a"), ("q", "p"), ("h", "q")) if DEF else (("j", "a"), ("k", "a"), ("k", "j"), ("h", "j"), ("h", "k")) if BOLD else (("f", "d"), ("g", "d"), ("f", "g"), ("h", "a"), ("h", "b"), ("i", "d"), ("i", "h"), ("i", "a")):
    rat = (np.log(P[x]) - np.log(P[y])).mean(1); bs = [np.exp(rat[rng.integers(0, N, N)].mean()) for _ in range(5000)]
    print(f"{x.upper()} / {y.upper()} {np.exp(rat.mean()):.2f} 95 % {np.round(np.percentile(bs, [2.5, 97.5]), 2)}  (< 1 — {x.upper()} лучше)")
print()
for i, it in enumerate(items):
    print(f"{it['w']} [{it['pair']}]: " + " | ".join(f"{v.upper()} {[ans.get((v, r, i), ['—'])[0] for r in '12']}" for v in (VS if SON or DIS or DEF or BOLD else "abdfghi")) + f"\n    H `{it3[i]['H']}`  I `{it3[i]['I']}`")
