# run.py readers S → S/rK/{spec.md,codes.md}, lists.json;  pairs S;  merge S;  score S → result.txt, table.md
import json, os, re, sys, random
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."; LP = f"{D}/../reader/labels.json"
cmd, S = sys.argv[1], sys.argv[2]; C = json.load(open(f"{D}/codes.json"))
spec = lambda k: os.popen(f"cd {R}/worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.{k}))'").read()
if cmd == "readers":
    ds = spec("DEC_SPEC"); random.seed(11); L = []
    for v in "ABFD":
        ws = [w for w in C if v != "D" or C[w]["D"] != C[w]["B"]]; random.shuffle(ws); n = -(-len(ws) // 50); per = -(-len(ws) // n)
        for c in range(0, len(ws), per):
            r = len(L) + 1; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); ch = ws[c:c + per]; open(f"{d}/spec.md", "w").write(ds)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][v]}\n" for i, w in enumerate(ch))); L.append({"r": r, "var": v, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); print([(l["r"], l["var"], len(l["words"])) for l in L]); sys.exit()
L = json.load(open(LP)); lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): [t.strip().lower() for t in m[2].split("|")] for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    for i, w in enumerate(l["words"]): A[(l["var"], w)] = a.get(i + 1) or ["—"]
for w in C:  # у слов без ребра D = B
    if ("D", w) not in A: A[("D", w)] = A[("B", w)]
if cmd == "pairs":
    keys = sorted({(w, a[0]) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]
    os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
import numpy as np
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a[0]}"] for k, a in A.items()}; W = list(C); E = [w for w in W if C[w]["D"] != C[w]["B"]]
cl = lambda v, ws: np.array([s[(v, w)] == 2 for w in ws], float)
def diff(a, b, ws):
    x = cl(a, ws) - cl(b, ws); rng = np.random.default_rng(0); bs = [x[rng.integers(0, len(x), len(x))].mean() for _ in range(10000)]
    return f"{a} − {b} (n {len(ws)}): {x.mean():+.1%} [{np.percentile(bs, 2.5):+.1%} … {np.percentile(bs, 97.5):+.1%}]"
V = [v for v in ("A", "B", "F", "D", "G", "A2") if all((v, w) in s for w in W)]
out = [f"{v:2s} близко {cl(v, W).mean():.0%}  рядом {np.mean([s[(v, w)] == 1 for w in W]):.0%}" for v in V]
out += [diff("B", "A", W), diff("F", "A", W), diff("F", "B", W), diff("D", "A", W), diff("D", "B", E), diff("F", "B", E), diff("D", "F", E)]
if "G" in V: out += [diff("G", "B", W), diff("G", "F", W), diff("A2", "A", W), diff("G", "A", W)]
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
md = ["| слово | " + " | ".join(V) + " |", "|---" * (len(V) + 1) + "|"]
for w in W: md.append(f"| **{w}** | " + " | ".join(f"`{C[w][{"G": "F", "A2": "A"}.get(v, v)]}` → {A[(v, w)][0]} ({s[(v, w)]})" for v in V) + " |")
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
