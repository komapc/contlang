# Корень TRUE (dec.md): слова, где код с TRUE (T) отличается от кода сайта (M); каждый вариант читают 2 слепых Haiku (весь список),
# у читателей T в спецификации строка TRUE.   run.py readers|pairs|merge|score SCRATCH
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]
CA = json.load(open(f"{D}/codes_all.json")); WS = json.load(open(f"{D}/words.json"))
W = sorted(w for w in WS["worst"] + WS["field"] if w in CA and CA[w]["M"] != CA[w]["T"] and w != "alleged"); C = {w: CA[w] for w in W}  # alleged — пример в строке TRUE
grp = {w: "worst" if w in WS["worst"] else "field" for w in W}; LS = [("M", 1), ("M", 2), ("T", 1), ("T", 2)]
if cmd == "readers":
    sp = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read(); assert "## Roots (45)" in sp
    r = json.load(open(f"{D}/root.json")); spT = sp.replace("## Roots (45)", "## Roots (46)"); i = spT.index("\n", spT.index("- THINK:")); spT = spT[:i + 1] + r["spec"] + "\n" + spT[i + 1:]
    open(f"{D}/spec_M.md", "w").write(sp); open(f"{D}/spec_T.md", "w").write(spT); random.seed(20261018); L = []
    for k, (v, c) in enumerate(LS):
        ws = W[:]; random.shuffle(ws); d = f"{S}/t{k + 1}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(spT if v == "T" else sp)
        open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][v]}\n" for i, w in enumerate(ws))); L.append({"r": k + 1, "var": v, "words": ws})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей по", len(W), "кодов"); sys.exit()
lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f"{S}/t{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    A.update({(l["r"], w): a.get(i + 1, "—") for i, w in enumerate(l["words"])})
L = json.load(open(LP))
if cmd == "pairs":
    keys = sorted({(w, a) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
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
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/t{l['r']}_{l['var']}.md", "w").write(open(f"{S}/t{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] for k, a in A.items()}; R = {v: [l["r"] for l in lists if l["var"] == v] for v in "MT"}
f = lambda v, w, x=2: np.mean([s[(r, w)] == x for r in R[v]]); out = []
def cmp(ws, name):
    d = np.array([f("T", w) - f("M", w) for w in ws]); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5])
    out.append(f"{name:18s} M {np.mean([f('M', w) for w in ws]):4.0%}  T {np.mean([f('T', w) for w in ws]):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
cmp(W, "T − M"); cmp([w for w in W if grp[w] == "worst"], "  худшие"); cmp([w for w in W if grp[w] == "field"], "  поле TRUE")
for v in "MT": out.append(f"  {v}: рядом {np.mean([f(v, w, 1) for w in W]):4.0%}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
g = lambda v, w: ", ".join(f"{A[(r, w)]} ({s[(r, w)]})" for r in R[v])
md = ["| слово | группа | M | → | T | → |", "|---|---|---|---|---|---|"] + [f"| {w} | {grp[w]} | `{C[w]['M']}` | {g('M', w)} | `{C[w]['T']}` | {g('T', w)} |" for w in W]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
