"""Слепое чтение 20 кодов математики с MANY по старой (односторонней) и новой (двусторонней) спецификации: cos первого ответа со словом (полный Numberbatch), близко — cos ≥ 0,5.
    .venv/bin/python data/eval/runs/many/score.py data/raw/numberbatch-en-19.08.txt.gz"""
import gzip, json, os, re, sys
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); key = json.load(open(f"{D}/key.json")); codes = {c["w"]: c["code"] for c in json.load(open(f"{D}/codes.json"))}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "an", "of", "to"}]
ans = {}
for v in ("old", "new"):
    for x in "ab":
        for l in open(f"{D}/dec_{v}_{x}.md"):
            m = re.match(r"\s*(\d+)\.\s*(.*)", l)
            if m: ans.setdefault(v, {}).setdefault(key[int(m[1]) - 1], []).append(re.split(r"[|,]", m[2])[0].strip())
need = set(key) | {t for v in ans.values() for a in v.values() for p in a for t in toks(p) + ["_".join(toks(p))]}
vec = {}
with gzip.open(sys.argv[1], "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]; return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
cos = lambda w, p: float(vec[w] @ pv(p)) if w in vec and pv(p) is not None else 0.0
print("| слово | код | старая спецификация | новая |\n|---|---|---|---|")
tot = {v: [] for v in ans}
for w in key:
    row = []
    for v in ("old", "new"):
        cs = [cos(w, p) for p in ans[v][w]]; tot[v] += cs; row.append(" / ".join(f"{p} ({c:.2f})" for p, c in zip(ans[v][w], cs)))
    print(f"| {w} | `{codes[w]}` | {row[0]} | {row[1]} |")
neg = [w for w in key if re.search(r"MANY\(=-", codes[w])]
print()
for v in ("old", "new"):
    a = tot[v]; sub = [c for w in key for c, ww in zip([cos(w, p) for p in ans[v][w]], [w] * 2) if w in neg]
    print(f"- {v}: cos первого {np.mean(a):.2f}, близко {sum(c >= .5 for c in a)}/{len(a)}, точно {sum(1 for w in key for p in ans[v][w] if toks(p) == [w])}; коды с MANY < 0 ({len(neg)} слов): cos {np.mean(sub):.2f}, близко {sum(c >= .5 for c in sub)}/{len(sub)}")
