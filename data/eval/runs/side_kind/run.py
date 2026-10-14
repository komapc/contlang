# Тест KIND только головой (H) и SIDE (O / R / D), пороги — dec.md.  Коды: codes.js на пулах pool.js → codes.json.
#   run.py readers SC → spec_*.md, items.json, lists.json, SC/rK/{spec,codes}.md;  pairs SC;  merge SC;  score SC → result.txt, table.md
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]
KLINE = "- KIND: -5 an example, a sample, an instance, evidence … 0 a model, a pattern … +5 a kind, type, category, class (the plain root means kind, sort)"
DLINE = "- SIDE: -5 back, behind, backward; also going back, return … +5 front, ahead, forward; also coming up, ready"
sub = lambda s, a, b: (lambda r: r[0] if r[1] == 1 else sys.exit(f"нет: {a}"))(re.subn(a, b, s, count=1, flags=re.M))
if cmd == "readers":
    C = json.load(open(f"{D}/codes.json")); p = json.load(open(f"{D}/pool.json")); oldk = json.load(open(f"{D}/../kind/codes.json"))
    H = [w for w in p["kind"] if C[w].get("kind") and C[w]["kind"].startswith("KIND")]
    sw = [w for w in p["side"] if C[w]["cur"] and re.search(r"\bSIDE\b", C[w]["cur"])]
    random.seed(20261014); SW = sorted(random.sample(sw, min(180, len(sw)))) if len(sw) > 180 else sw
    its = [{"w": w, "set": "H", "old": C[w]["cur"], "new": C[w]["kind"], "rep": bool(oldk.get(w) and (oldk[w][1] or "").startswith("KIND"))} for w in H]
    its += [{"w": w, "set": "S", "O": C[w]["cur"], "R": C[w]["noside"], "D": C[w]["cur"]} for w in SW]
    json.dump(its, open(f"{D}/items.json", "w"), indent=0); print("H", len(H), "SIDE", len(sw), "→", len(SW))
    s0 = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read()
    sk = sub(sub(s0, r"^## Roots \(45\)$", "## Roots (46)"), r"^(- PLACE: .*)$", KLINE + r"\n\1").replace("Use ONLY the 45 roots", "Use ONLY the 46 roots")
    sd = sub(s0, r"^- SIDE: .*$", DLINE)
    sr = sub(sub(s0, r"^- SIDE: .*\n", ""), r"^## Roots \(45\)$", "## Roots (44)").replace("Use ONLY the 45 roots", "Use ONLY the 44 roots")
    sr = sub(sr, r"east `PLACE SIDE\(=\+5\) \| o` \(front\), west `SIDE\(=-5\)`, north", "north")
    sr = sub(sr, r"; northeast `PLACE ABOVE\(=\+3\) SIDE\(=\+3\) \| o`\.", ".")
    sr = sub(sr, r" leader `SOMEONE SIDE\(=\+5\) RULE \| o`,", "")
    assert "SIDE" not in sr.replace("INSIDE", ""), [l for l in sr.splitlines() if "SIDE" in l.replace("INSIDE", "")]
    for n, t in (("spec_kind.md", sk), ("spec_side_def.md", sd), ("spec_noside.md", sr)): open(f"{D}/{n}", "w").write(t)
    L = []
    for st, var, key, sp in (("H", "old", "old", s0), ("H", "new", "new", sk), ("S", "O", "O", s0), ("S", "R", "R", sr), ("S", "D", "D", sd)):
        ws = [o for o in its if o["set"] == st]; random.shuffle(ws); n = -(-len(ws) // 50); per = -(-len(ws) // n)
        for c in range(n):
            r = len(L) + 1; ch = ws[c * per:(c + 1) * per]; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[key]}\n" for i, o in enumerate(ch))); L.append({"r": r, "set": st, "var": var, "words": [o["w"] for o in ch]})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей", [len(l["words"]) for l in L]); sys.exit()
its = json.load(open(f"{D}/items.json")); lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
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
s = {k: L[f"{k[1]}\t{a}"] for k, a in A.items()}; out = []
def cmp(ws, a, b, name):
    d = np.array([(s[(b, w)] == 2) - (s[(a, w)] == 2) for w in ws], float); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5]); f = lambda v: np.mean([s[(v, w)] == 2 for w in ws])
    out.append(f"{name:28s} {a} {f(a):4.0%}  {b} {f(b):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
H = [o["w"] for o in its if o["set"] == "H"]; SW = [o["w"] for o in its if o["set"] == "S"]; rep = {o["w"] for o in its if o.get("rep")}
cmp(H, "old", "new", "H: KIND головой"); cmp([w for w in H if w in rep], "old", "new", "  повтор (голова в ../kind)"); cmp([w for w in H if w not in rep], "old", "new", "  новые слова")
cmp(SW, "O", "R", "SIDE: убрать (R − O)"); cmp(SW, "O", "D", "SIDE: переопределить (D − O)"); cmp(SW, "R", "D", "SIDE: D − R")
for v in ("O", "R", "D"): out.append(f"  {v}: рядом {np.mean([s[(v, w)] == 1 for w in SW]):4.0%}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
g = lambda v, w: f"{A[(v, w)]} ({s[(v, w)]})"
md = ["## KIND головой", "", "| слово | old → ответ | new → ответ |", "|---|---|---|"] + [f"| {o['w']} | `{o['old']}` → {g('old', o['w'])} | `{o['new']}` → {g('new', o['w'])} |" for o in its if o["set"] == "H"]
md += ["", "## SIDE", "", "| слово | O / D: код | O → | D → | R: код без SIDE | R → |", "|---|---|---|---|---|---|"] + [f"| {o['w']} | `{o['O']}` | {g('O', o['w'])} | {g('D', o['w'])} | `{o['R']}` | {g('R', o['w'])} |" for o in its if o["set"] == "S"]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
