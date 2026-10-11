"""Раунд 2 (key через door/lock/open): cos ответов к слову в полном Numberbatch; для key ещё cos к lock и door.
Метрики на вариант: cos первого ответа и лучший cos среди трёх, среднее по декодерам."""
import gzip, json, re, glob, sys, os
import numpy as np
D = os.path.dirname(os.path.abspath(__file__)); NB = sys.argv[1]
k = json.load(open(f"{D}/key.json")); ans = {}
for f in sorted(glob.glob(f"{D}/dec_*_[ab].md")):
    s = str(int(os.path.basename(f)[4:6])); a = {}
    for l in open(f):
        m = re.match(r'\s*(\d+)\.\s*(.*)', l)
        if m: a[int(m[1])] = [x.strip() for x in re.split(r'[|,]', m[2]) if x.strip()][:3]
    ans[f] = (s, a)
REF = {"key": ["lock", "door", "keys", "doorknob", "latch", "staple", "stapler", "clamp", "nail", "fastener", "coin"],
       "door": ["entrance", "front", "gate", "room", "facade"], "lock": ["clamp", "bolt", "glue", "latch", "padlock"], "open": ["extract", "insert", "cut", "remove", "detach", "unlock"]}
toks = lambda p: [w for w in re.sub(r"[^a-z -]", "", p.lower()).replace("-", " ").split() if w not in {"the", "a", "of"}]
need = set(REF) | {w for v in REF.values() for x in v for w in toks(x)}
for s, a in ans.values():
    for x in a.values():
        for p in x: need |= set(toks(p)) | {"_".join(toks(p))}
vec = {}
with gzip.open(NB, "rt") as fh:
    next(fh)
    for l in fh:
        w = l[:l.find(" ")]
        if w in need: v = np.array(l.split()[1:], float); vec[w] = v / np.linalg.norm(v)
def pv(p):
    t = toks(p); j = "_".join(t)
    if j in vec: return vec[j]
    vs = [vec[w] for w in t if w in vec]
    return np.sum(vs, 0) / np.linalg.norm(np.sum(vs, 0)) if vs else None
def cos(a, b): return float(a @ b) if a is not None and b is not None else 0.0
res = {}
for f, (s, a) in ans.items():
    for i, (w, c, n) in enumerate(k["sheets"][s], 1):
        if not n: continue
        x = a.get(i, []); t = vec[w]; cs = [cos(t, pv(p)) for p in x] or [0]
        res.setdefault((w, n), {"c": c, "r": []})["r"].append((x[0] if x else "—", cs[0], max(cs)))
for w in ("key", "door", "lock", "open"):
    print(f"\n### {w}\n\nдля сравнения: " + ", ".join(f"{x} {cos(vec[w], pv(x)):.2f}" for x in REF[w]) + "\n")
    print("| # | код | cos первого ответа | лучший из трёх | прочитано первым |\n|--:|---|--:|--:|---|")
    rows = sorted(((np.mean([r[1] for r in v["r"]]), np.mean([r[2] for r in v["r"]]), n, v) for (ww, n), v in res.items() if ww == w), key=lambda r: -r[0])
    for m1, m3, n, v in rows:
        print(f"| {n} | `{v['c'].replace('|', chr(92) + '|')}` | {m1:.2f} | {m3:.2f} | " + ", ".join(f"{r[0]} ({r[1]:.2f})" for r in v["r"]) + " |")
print("\n### key: насколько ответы близки к lock / door (лучший из трёх)\n\n| # | key | lock | door |\n|--:|--:|--:|--:|")
for (w, n), v in sorted(res.items()):
    if w != "key": continue
    print(f"| {n} | {np.mean([r[2] for r in v['r']]):.2f} | " + " | ".join(f"{np.mean([max([cos(vec[t], pv(p)) for p in a.get(i, [])] or [0]) for f, (s, a) in ans.items() for i, (ww, c, nn) in enumerate(k['sheets'][s], 1) if ww == 'key' and nn == n]):.2f}" for t in ("lock", "door")) + " |")
