# readers SC → spec_v1.md, spec_v3.md, SC/rK; pairs SC → SC/jK; merge SC; score SC → result.txt, table.md  (см. dec.md)
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); B = f"{D}/../big1000"; LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]
its = json.load(open(f"{D}/items.json")); C = json.load(open(f"{D}/codes.json")); W = [o["w"] for o in its]; RW = [o["w"] for o in its if o["role"]]
NEW = {  # оси по ближайшим словам атомов (atoms.txt)
    "LONG": "-5 thread, cloth, textile … 0 wire, rod, fastening … +5 beam, plank, wooden furniture (long objects and what is made of them)",
    "KNOW": "-5 stupid, foolish, absurd … 0 aware … +5 know, inform, teach",
    "MEASURE": "-5 an amount (size, length, weight, quantity) … 0 a level, degree … +5 a ratio, rate, percentage, statistics",
    "TOUCH": "-5 soft, smooth, tender … +5 hard, stiff, tough, harsh",
    "NEAR": "-5 far, abroad, journey … +5 here, nearby, downtown, center",
    "GIVE": "-5 grab, seize, steal … 0 exchange, get … +5 give, donate, grant",
    "VALUE": "-5 cheap, a bargain, buying and selling … +5 precious, important, vital (price, worth)",
    "CARE": "-5 careless, a mistake, fault … +5 careful, thorough, diligent",
}
AG0 = "- `agent`: the one who does it (person or thing)."
AG1 = "- `agent`: the one who does it, or a person of that field (person or thing). `ART(=+5) | o agent` = artist."
if cmd == "readers":
    s0 = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read(); s1 = s0
    for k, t in NEW.items(): s1, n = re.subn(rf"^- {k}: .*$", f"- {k}: {t}", s1, flags=re.M); assert n == 1, k
    assert AG0 in s0 and "artist" not in W; s3 = s0.replace(AG0, AG1)
    open(f"{D}/spec_v1.md", "w").write(s1); open(f"{D}/spec_v3.md", "w").write(s3); L = []; random.seed(5)
    for v, sp, ws, key in (("V1", s1, W, "A"), ("V2", s0, W, "V2"), ("V3", s3, RW, "V3")):
        ws = ws[:]; random.shuffle(ws); n = -(-len(ws) // 50); per = -(-len(ws) // n)
        for c in range(n):
            r = len(L) + 1; ch = ws[c * per:(c + 1) * per]; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][key]}\n" for i, w in enumerate(ch))); L.append({"r": r, "var": v, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей", [len(l["words"]) for l in L]); sys.exit()
first = lambda f: {int(m[1]): m[2].split("|")[0].strip().lower() for x in open(f) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
A = {}
for l in json.load(open(f"{B}/lists.json")):
    if l["var"] == "math":
        a = first(f"{B}/answers/r{l['r']}_math.md"); A.update({("A", w): a.get(i + 1, "—") for i, w in enumerate(l["words"]) if w in C})
for l in json.load(open(f"{D}/lists.json")):
    a = first(f"{S}/r{l['r']}/answers.md"); A.update({(l["var"], w): a.get(i + 1, "—") for i, w in enumerate(l["words"])})
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
for l in json.load(open(f"{D}/lists.json")): open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] == 2 for k, a in A.items()}; out = []
def cmp(a, b, ws, name):
    d = np.array([s[(a, w)] - s[(b, w)] for w in ws], float); rng = np.random.default_rng(0); lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5])
    out.append(f"{name:24s} {a} {np.mean([s[(a, w)] for w in ws]):4.0%}  {b} {np.mean([s[(b, w)] for w in ws]):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
cmp("V1", "A", W, "оси 8 корней"); cmp("V2", "A", W, "полюса, 2 корня"); cmp("V3", "V2", RW, "роль (к V2)"); cmp("V3", "A", RW, "роль + полюса (к A)")
for ro in ("agent", "quality", "tool"):
    ws = [o["w"] for o in its if o["role"] == ro]; cmp("V3", "A", ws, f"  {ro}")
ws8 = [w for w in W if re.search(r"\b(" + "|".join(NEW) + r")\b", C[w]["A"])]; cmp("V1", "A", ws8, "  V1, коды с этими корнями")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
md = ["| слово | роль | A | V1 | V2 | V3 |", "|---|---|---|---|---|---|"]
sc = lambda v, w: f"{A.get((v, w), '')} ({L.get(w + chr(9) + A[(v, w)], '')})" if (v, w) in A else ""
for o in its: w = o["w"]; md.append(f"| {w} | {o['role'] or ''} | `{C[w]['A']}` → {sc('A', w)} | {sc('V1', w)} | `{C[w]['V2']}` → {sc('V2', w)} | " + (f"`{C[w]['V3']}` → {sc('V3', w)}" if C[w]["V3"] else "") + " |")
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
