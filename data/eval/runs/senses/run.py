# readers SC → SC/rK (смысл 1 у r1–r2, смысл 2 у r3–r4); pairs SC → SC/jK (судья видит «слово (толкование) — ответ»); score SC → result.txt
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); B = f"{D}/../big1000"; cmd, S = sys.argv[1], sys.argv[2]
its = json.load(open(f"{D}/items.json")); C = json.load(open(f"{D}/codes.json"))
if cmd == "readers":
    ds = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read(); L = []; random.seed(11)
    for k in (0, 1):
        ws = [o["w"] for o in its]; random.shuffle(ws)
        for h in (0, 1):
            r = len(L) + 1; ch = ws[h * 50:(h + 1) * 50]; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(ds)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][k]['code']}\n" for i, w in enumerate(ch))); L.append({"r": r, "k": k, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); sys.exit()
first = lambda f: {int(m[1]): m[2].split("|")[0].strip().lower() for x in open(f) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
A = {}  # (вариант, слово, смысл) → первый ответ
for l in json.load(open(f"{B}/lists.json")):
    if l["var"] == "math":
        a = first(f"{B}/answers/r{l['r']}_math.md")
        for i, w in enumerate(l["words"]): A[("one", w, 0)] = A[("one", w, 1)] = a.get(i + 1, "—")
for l in json.load(open(f"{D}/lists.json")):
    a = first(f"{S}/r{l['r']}/answers.md")
    for i, w in enumerate(l["words"]): A[("sense", w, l["k"])] = a.get(i + 1, "—")
g = {(o["w"], k): o["senses"][k]["gloss"] for o in its for k in (0, 1)}; tgt = lambda w, k: f"{w} ({g[(w, k)]})"
if cmd == "pairs":
    keys = sorted({(tgt(w, k), a) for (v, w, k), a in A.items() if (w, k) in g}); n = -(-len(keys) // 150); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{D}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
P = json.load(open(f"{D}/pairs.json")); os.makedirs(f"{D}/judge", exist_ok=True); os.makedirs(f"{D}/answers", exist_ok=True)
sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for x in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", x))}
for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
for l in json.load(open(f"{D}/lists.json")): open(f"{D}/answers/r{l['r']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
lab = {(p["w"], p["a"]): sc[(p["j"], p["t"])] for p in P}; s = {k: lab[(tgt(k[1], k[2]), a)] for k, a in A.items() if (k[1], k[2]) in g}
W = [o["w"] for o in its]; out = []
def cmp(ks, name):
    f = lambda v, w: np.mean([s[(v, w, k)] == 2 for k in ks]); d = np.array([f("sense", w) - f("one", w) for w in W])
    rng = np.random.default_rng(0); lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5])
    out.append(f"{name:10s} one {np.mean([f('one', w) for w in W]):4.0%}  sense {np.mean([f('sense', w) for w in W]):4.0%}  разница {d.mean():+.0%} [{lo:+.0%} … {hi:+.0%}]")
cmp((0, 1), "оба смысла"); cmp((0,), "смысл 1"); cmp((1,), "смысл 2")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
md = ["| слово | смысл | one → ответ | sense → ответ |", "|---|---|---|---|"]
site = json.load(open(f"{B}/site_codes.json"))
for o in its:
    for k in (0, 1): w = o["w"]; md.append(f"| {w} | {g[(w, k)][:50]} | `{site[w]}` → {A[('one', w, k)]} ({s[('one', w, k)]}) | `{C[w][k]['code']}` → {A[('sense', w, k)]} ({s[('sense', w, k)]}) |")
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
