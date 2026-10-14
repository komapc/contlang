# readers SC → spec_new.md, SC/rK; pairs SC; merge SC; score SC → result.txt, table.md  (см. dec.md)
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]
C = json.load(open(f"{D}/codes.json")); p = json.load(open(f"{D}/pool.json"))
K = [w for w in p["near"] + p["big"] if "KIND" in C[w][1]]; SS = [w for w in p["big"] if C[w][0] != C[w][1] and "KIND" not in C[w][1]]; W = K + SS
LINE = "- KIND: -5 an example, a sample, an instance, evidence … 0 a model, a pattern … +5 a kind, type, category, class (the plain root means kind, sort)"
if cmd == "readers":
    s0 = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read()
    s1, n = re.subn(r"^## Roots \(45\)$", "## Roots (46)", s0, flags=re.M); assert n == 1
    s1, n = re.subn(r"^(- PLACE: .*)$", LINE + r"\n\1", s1, count=1, flags=re.M); assert n == 1
    s1 = s1.replace("Use ONLY the 45 roots", "Use ONLY the 46 roots"); open(f"{D}/spec_new.md", "w").write(s1); L = []; random.seed(3)
    for k, v, sp in ((0, "old", s0), (1, "new", s1)):
        ws = W[:]; random.shuffle(ws); n = -(-len(ws) // 50); per = -(-len(ws) // n)
        for c in range(n):
            r = len(L) + 1; ch = ws[c * per:(c + 1) * per]; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][k]}\n" for i, w in enumerate(ch))); L.append({"r": r, "var": v, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей", [len(l["words"]) for l in L]); sys.exit()
lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().lower() for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    A.update({(l["var"], w): a.get(i + 1, "—") for i, w in enumerate(l["words"])})
L = json.load(open(LP))
if cmd == "pairs":
    keys = sorted({(w, a) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]; os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] == 2 for k, a in A.items()}; out = []
def cmp(ws, name):
    d = np.array([s[("new", w)] - s[("old", w)] for w in ws], float); rng = np.random.default_rng(0); lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5])
    out.append(f"{name:26s} old {np.mean([s[('old', w)] for w in ws]):4.0%}  new {np.mean([s[('new', w)] for w in ws]):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
cmp(K, "K: код с KIND"); cmp([w for w in K if w in p["near"]], "  близкие к атому"); cmp([w for w in K if w in p["big"]], "  из big1000")
cmp([w for w in K if C[w][1].startswith("KIND")], "  KIND — голова"); cmp(SS, "S: сдвиг без KIND")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
md = ["| слово | old → ответ | new → ответ |", "|---|---|---|"] + [f"| {w} | `{C[w][0]}` → {A[('old', w)]} ({L[w + chr(9) + A[('old', w)]]}) | `{C[w][1]}` → {A[('new', w)]} ({L[w + chr(9) + A[('new', w)]]}) |" for w in W]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
