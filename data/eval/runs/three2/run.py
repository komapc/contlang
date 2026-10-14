# Умный выбор слов (select.py → codes.json: A, S, HS) на 188 неудачных словах ../three, пороги — dec.md. Устройство — как ../three/run.py.
#   run.py readers SC → spec.md, lists.json, SC/tK/{spec,codes}.md;  pairs SC;  merge SC;  score SC → result.txt, table.md
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]; V3 = ("A", "S", "HS")
MULTI = ("- Several words: a word can be followed by up to two more words, each after its own link: `X | o LINK Y | o LINK Z | o`; "
         "every following word narrows the first one (X). `LIKE` also works for verbs, adjectives and adverbs: "
         "`X | i LIKE Y | i` = to X, close in meaning to Y. Brackets group words: `X | o LINK ( Y | o LINK Z | o )` — Z narrows Y, and the pair narrows X.")
C = json.load(open(f"{D}/codes.json")); W = sorted(C)
if cmd == "readers":
    s0 = os.popen(f"cd {D}/../../../.. /worker 2>/dev/null; cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read()
    k = s0.index("- `PI`: X is part of Y"); e = s0.index("\n", k) + 1; sp = s0[:e] + MULTI + "\n" + s0[e:]
    open(f"{D}/spec.md", "w").write(sp); random.seed(20261014); L = []
    # слово в трёх вариантах — на трёх разных листах: варианты по очереди, у листа один вариант
    for v in V3:
        ws = W[:]; random.shuffle(ws); n = 4; per = -(-len(ws) // n)
        for c in range(n):
            r = len(L) + 1; ch = ws[c * per:(c + 1) * per]; d = f"{S}/t{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w][v]}\n" for i, w in enumerate(ch))); L.append({"r": r, "var": v, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей", [len(l["words"]) for l in L]); sys.exit()
lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f"{S}/t{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    A.update({(l["var"], w): a.get(i + 1, "—") for i, w in enumerate(l["words"])})
L = json.load(open(LP))
if cmd == "pairs":
    keys = sorted({(w, a) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/u{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs4.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs4.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]; os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/t{l['r']}_{l['var']}.md", "w").write(open(f"{S}/t{l['r']}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] for k, a in A.items()}; out = []
pos = lambda c: re.search(r"\|\s*([oiae])\b", c)[1]
def cmp(ws, a, b, name):
    d = np.array([(s[(b, w)] == 2) - (s[(a, w)] == 2) for w in ws], float); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5]); f = lambda v: np.mean([s[(v, w)] == 2 for w in ws])
    out.append(f"{name:26s} {a} {f(a):4.0%}  {b} {f(b):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
cmp(W, "A", "S", "S − A"); cmp(W, "A", "HS", "HS − A"); cmp(W, "S", "HS", "HS − S")
ad = [w for w in W if C[w]["wS"]]; cmp(ad, "A", "S", "  S добавил слова: S − A")
for p, nm in (("o", "имена"), ("i", "глаголы"), ("a", "признаки")):
    ws = [w for w in W if pos(C[w]["A"]) == p]; cmp(ws, "A", "S", f"  {nm}: S − A"); cmp(ws, "A", "HS", f"  {nm}: HS − A")
for v in V3: out.append(f"  {v}: рядом {np.mean([s[(v, w)] == 1 for w in W]):4.0%}")
# для сведения: W3 из ../three (другие читатели)
T = json.load(open(f"{D}/../three/lists.json")); w3 = {}
for l in T:
    if l["var"] != "W3": continue
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f"{D}/../three/answers/t{l['r']}_W3.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    w3.update({w: L[f"{w}\t{a.get(i + 1, '—')}"] for i, w in enumerate(l["words"])})
for v in ("S", "HS"):
    d = np.array([(s[(v, w)] == 2) - (w3[w] == 2) for w in W], float); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5]); out.append(f"{v} − W3 (../three) {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]")
an = sum(A[("S", w)] in C[w]["wS"] for w in W); out.append(f"ответ S = добавленное слово: {an} из {len(W)}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
g = lambda v, w: f"{A[(v, w)]} ({s[(v, w)]})"
md = ["| слово | A → | S: слова | S → | HS: слова | HS → |", "|---|---|---|---|---|---|"] + [f"| {w} | {g('A', w)} | {', '.join(C[w]['wS'])} | {g('S', w)} | {', '.join(C[w]['wHS'])} | {g('HS', w)} |" for w in W]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
