# score.py pairs SCRATCH → SCRATCH/jN/pairs.md для неоценённых пар; score.py merge SCRATCH → ../reader/labels.json; score.py SCRATCH → итог
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; L = json.load(open(LP))
S = sys.argv[-1]; lists = json.load(open(f"{D}/lists.json")); its = {o["w"]: o for o in json.load(open(f"{D}/items.json"))}
R = []  # (var, word, first answer)
for l in lists:
    a = {int(m[1]): m[2] for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*([^|\n]*)", x))}
    R += [(l["var"], w, (a.get(i + 1) or "—").strip().lower()) for i, w in enumerate(l["words"])]
if sys.argv[1] == "pairs":
    keys = sorted({(w, a) for _, w, a in R} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if sys.argv[1] == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]
    os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
cl = {}
for v, w, a in R: cl.setdefault((v, w), []).append(L[f"{w}\t{a}"] == 2)
f = lambda v, w: np.mean(cl[(v, w)])
def cmp(a, b, ws, name):
    d = np.array([f(a, w) - f(b, w) for w in ws]); rng = np.random.default_rng(0); bs = [rng.choice(d, len(d)).mean() for _ in range(5000)]
    lo, hi = np.percentile(bs, [2.5, 97.5]); print(f"{name:28s} {a} {np.mean([f(a, w) for w in ws]):4.0%}  {b} {np.mean([f(b, w) for w in ws]):4.0%}  разница {d.mean():+.0%} [{lo:+.0%} … {hi:+.0%}]  (n {len(ws)})")
NR = [w for w, o in its.items() if o["root"] != "-"]
cmp("new", "old", NR, "новые корни, все 120")
for r in ("LAND", "SACRED", "CONTAINER"): cmp("new", "old", [w for w in NR if its[w]["root"] == r], r)
cmp("new", "old", [w for w, o in its.items() if o["root"] == "-"], "побочный сдвиг (без новых)")
hd = lambda w: its[w]["sz2"].split()[0].split("(")[0] in ("LAND", "SACRED", "CONTAINER")
print("после ответов (не заявлено):")
for r in ("LAND", "SACRED", "CONTAINER"):
    for h in (True, False): cmp("new", "old", [w for w in NR if its[w]["root"] == r and hd(w) == h], f"{r} {'род' if h else 'уточн.'}")
