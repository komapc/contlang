# Словосочетания (dec.md): 6 слепых читателей (A, B, C × 2) читают все 60 кодов своего варианта; судья оценивает пары «фраза — первый ответ».
#   run.py readers SCRATCH  → SCRATCH/tK/{spec.md,codes.md}, lists.json
#   run.py pairs SCRATCH    → SCRATCH/uJ/pairs.md (новые пары без оценки)
#   run.py merge SCRATCH    → labels.json (из SCRATCH/uJ/scores.md), judge/
#   run.py score SCRATCH    → result.txt, table.md, answers/
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); cmd, S = sys.argv[1], sys.argv[2]; LP = f"{D}/labels.json"
C = json.load(open(f"{D}/codes.json")); IT = {i["phrase"]: i for i in json.load(open(f"{D}/items.json"))}; W = sorted(C)
LS = [("A", 1), ("A", 2), ("B", 1), ("B", 2), ("C", 1), ("C", 2)]
if cmd == "readers":
    sp = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read(); assert "## Roots (45)" in sp
    sp = sp.replace("## Task\n\nEach line is one code standing for ONE common English word in some sense. Give your best English word and 2 alternatives.\n", ""); assert "ONE common English word" not in sp  # своё задание — reader_task.md
    task = open(f"{D}/reader_task.md").read(); random.seed(20261107); L = []
    for k, (v, _) in enumerate(LS):
        ws = W[:]; random.shuffle(ws); d = f"{S}/t{k + 1}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp + "\n\n" + task)
        open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][v]}\n" for i, w in enumerate(ws))); L.append({"r": k + 1, "var": v, "words": ws})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей по", len(W), "кодов"); sys.exit()
lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`\"").lower() for x in open(f"{S}/t{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    assert len(a) == len(l["words"]), (l["r"], len(a)); A.update({(l["r"], w): a[i + 1] for i, w in enumerate(l["words"])})
L = json.load(open(LP)) if os.path.exists(LP) else {}
if cmd == "pairs":
    keys = sorted({(w, a) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 120)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/u{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]; os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w"), ensure_ascii=False, indent=0); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/t{l['r']}_{l['var']}.md", "w").write(open(f"{S}/t{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] for k, a in A.items()}; R = {v: [l["r"] for l in lists if l["var"] == v] for v in "ABC"}
f = lambda v, w, x=2: np.mean([s[(r, w)] == x for r in R[v]]); out = []
def cmp(a, b, ws, name):
    d = np.array([f(b, w) - f(a, w) for w in ws]); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5])
    out.append(f"{name:22s} {a} {np.mean([f(a, w) for w in ws]):4.0%}  {b} {np.mean([f(b, w) for w in ws]):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
grp = lambda g=None, p=None: [w for w in W if (g is None or IT[w]["group"] == g) and (p is None or IT[w]["pos"] == p)]
cmp("A", "B", W, "B − A (главный)")
for g in ("fixed", "free"): cmp("A", "B", grp(g), f"  B − A {g}")
for p in "nv": cmp("A", "B", grp(p=p), f"  B − A {'имена' if p == 'n' else 'глаголы'}")
cmp("A", "C", W, "C − A")
for g in ("fixed", "free"): cmp("A", "C", grp(g), f"  C − A {g}")
cmp("C", "B", W, "B − C")
for g in ("fixed", "free"): cmp("C", "B", grp(g), f"  B − C {g}")
for v in "ABC": out.append(f"  {v}: рядом {np.mean([f(v, w, 1) for w in W]):4.0%}, близко или рядом {np.mean([f(v, w, 1) + f(v, w) for w in W]):4.0%}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
g = lambda v, w: ", ".join(f"{A[(r, w)]} ({s[(r, w)]})" for r in R[v])
md = ["| фраза | группа | A | → | B | → | C | → |", "|---|---|---|---|---|---|---|---|"] + [
    f"| {w} | {IT[w]['group']} {IT[w]['pos']} | `{C[w]['A']}` | {g('A', w)} | `{C[w]['B']}` | {g('B', w)} | `{C[w]['C']}` | {g('C', w)} |" for w in W]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
