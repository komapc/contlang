# phrases3 (dec.md): коды пишет модель (M1 — одно слово, M2 — пословно, MC — сама выбирает) против математики пословно (A).
#   run.py writers SC  → SC/w{V}{k}/{spec.md,list.md}   (кодировщики Sonnet пишут answers.md: "N. CODE")
#   run.py collect SC  → codes.json[V] + проверка правилами (check.mjs); печатает неверные коды по кодировщикам
#   run.py readers SC  → SC/t{r}/{spec.md,codes.md}, lists.json (16 слепых читателей Haiku)
#   run.py pairs SC    → SC/u{j}/pairs.md (новые пары; оценки ../phrases и ../phrases2 берутся готовыми)
#   run.py merge SC    → labels.json, judge/;   run.py score SC → result.txt, table.md, answers/, codes_by_writer/
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); cmd, S = sys.argv[1], sys.argv[2]; LP = f"{D}/labels.json"; R0 = f"{D}/../../../.."
IT = {i["phrase"]: i for i in json.load(open(f"{D}/items.json"))}; W = sorted(IT); C = json.load(open(f"{D}/codes.json"))
VW = ["M1", "M2", "MC"]; VR = ["A", "M1", "M2", "MC"]
spec = lambda k: subprocess.run(["node", "-e", f'import("./prompts.js").then(m=>process.stdout.write(m.{k}))'], cwd=f"{R0}/worker", capture_output=True, text=True).stdout
def halves(seed):
    ws = W[:]; random.Random(seed).shuffle(ws); return ws[:60], ws[60:]
if cmd == "writers":
    es = spec("ENC_SPEC"); body = es[es.index("# min-co: how a word is written"):]; assert "## Roots (45)" in body
    for vi, v in enumerate(VW):
        for k, ws in enumerate(halves(100 + vi)):
            d = f"{S}/w{v}{k + 1}"; os.makedirs(d, exist_ok=True)
            open(f"{d}/spec.md", "w").write(open(f"{D}/writer_task_{v}.md").read() + "\n" + body)
            open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {w}\n" for i, w in enumerate(ws)))
    print("6 кодировщиков по 60 фраз"); sys.exit()
if cmd == "collect":
    bad = {}
    for vi, v in enumerate(VW):
        C[v] = {}
        for k, ws in enumerate(halves(100 + vi)):
            a = {int(m[1]): m[2].strip().strip("`").strip() for x in open(f"{S}/w{v}{k + 1}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
            miss = [i + 1 for i in range(len(ws)) if i + 1 not in a]; assert not miss, (v, k, miss)
            for i, w in enumerate(ws): C[v][w] = re.sub(r"\s*;\s*", " ", a[i + 1].strip("`").strip())  # «;» между словами (M2) — только разделитель, как пробел у A и MC
    json.dump(C, open(f"{D}/codes.json", "w"), indent=0, ensure_ascii=False)
    tmp = f"{S}/chk.json"; json.dump({f"{v}\t{w}": C[v][w] for v in VW for w in W}, open(tmp, "w"))
    chk = json.loads(subprocess.run(["node", f"{D}/check.mjs", tmp], capture_output=True, text=True).stdout); json.dump(chk, open(f"{S}/chk_out.json", "w"))
    for vi, v in enumerate(VW):
        for k, ws in enumerate(halves(100 + vi)):
            b = [(i + 1, C[v][w], chk[f"{v}\t{w}"]["bad"]) for i, w in enumerate(ws) if chk[f"{v}\t{w}"]["bad"]]
            if b: print(f"w{v}{k + 1}:", len(b)); [print("  ", i, c, "→", "; ".join(p)) for i, c, p in b]
    for v in VW:
        n = [chk[f"{v}\t{w}"]["n"] for w in W]; print(v, "слов в коде:", {x: n.count(x) for x in sorted(set(n))})
    sys.exit()
if cmd == "readers":
    sp = spec("DEC_SPEC"); assert "## Roots (45)" in sp
    sp = sp.replace("## Task\n\nEach line is one code standing for ONE common English word in some sense. Give your best English word and 2 alternatives.\n", ""); assert "ONE common English word" not in sp
    task = open(f"{D}/reader_task.md").read(); L = []; r = 0
    for vi, v in enumerate(VR):
        for h, ws in enumerate(halves(200 + vi)):
            for rep in range(2):
                r += 1; o = ws[:]; random.Random(1000 + r).shuffle(o); d = f"{S}/t{r}"; os.makedirs(d, exist_ok=True)
                open(f"{d}/spec.md", "w").write(sp + "\n\n" + task); open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[v][w]}\n" for i, w in enumerate(o)))
                L.append({"r": r, "var": v, "words": o})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей по 60 кодов"); sys.exit()
lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`\"").lower() for x in open(f"{S}/t{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    assert len(a) == len(l["words"]), (l["r"], len(a)); A.update({(l["r"], w): a[i + 1] for i, w in enumerate(l["words"])})
if os.path.exists(LP): L = json.load(open(LP))
else:
    L = {}
    for p in ("phrases", "phrases2"): L.update(json.load(open(f"{D}/../{p}/labels.json")))
    json.dump(L, open(LP, "w"), ensure_ascii=False, indent=0)
if cmd == "pairs":
    keys = sorted({(w, a) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 110)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/u{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "новых пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]; os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w"), ensure_ascii=False, indent=0); print("добавлено", len(P)); sys.exit()
# score
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/t{l['r']}_{l['var']}.md", "w").write(open(f"{S}/t{l['r']}/answers.md").read())
os.makedirs(f"{D}/codes_by_writer", exist_ok=True)
for v in VW:
    for k in (1, 2): open(f"{D}/codes_by_writer/w{v}{k}.md", "w").write(open(f"{S}/w{v}{k}/list.md").read() + "---\n" + open(f"{S}/w{v}{k}/answers.md").read())
s = {k: L[f"{k[1]}\t{a}"] for k, a in A.items()}; RD = {v: [l["r"] for l in lists if l["var"] == v] for v in VR}
f = lambda v, w, x=(2,): np.mean([s[(r, w)] in x for r in RD[v] if (r, w) in s])
chk = json.load(open(f"{S}/chk_out.json")); one = {w: chk[f"MC\t{w}"]["n"] == 1 for w in W}
out = []; rng = np.random.default_rng(0)
def cmp(a, b, ws, name, x=(2,)):
    da = np.array([f(a, w, x) for w in ws]); db = np.array([f(b, w, x) for w in ws]); d = db - da
    bs = [d[rng.integers(0, len(d), len(d))].mean() for _ in range(5000)]; lo, hi = np.percentile(bs, [2.5, 97.5])
    out.append(f"{name:24s} {a:2s} {da.mean():4.0%}  {b:2s} {db.mean():4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
G = ["fixed_n", "fixed_v", "free_n", "free_v", "deg", "light", "axis", "indep"]
cmp("A", "MC", W, "MC − A (главный)")
for g in G: cmp("A", "MC", [w for w in W if IT[w]["grp"] == g], f"  MC − A {g}")
for a, b in (("M1", "MC"), ("M2", "MC"), ("A", "M2"), ("A", "M1"), ("M2", "M1")): cmp(a, b, W, f"{b} − {a}")
for g in G: cmp("M2", "M1", [w for w in W if IT[w]["grp"] == g], f"  M1 − M2 {g}")
out.append("")
for v in VR: out.append(f"  {v:2s}: близко {np.mean([f(v, w) for w in W]):4.0%}, близко или рядом {np.mean([f(v, w, (1, 2)) for w in W]):4.0%}")
orc = np.mean([max(f('M1', w), f('M2', w)) for w in W]); out.append(f"  оракул max(M1, M2) по фразе: близко {orc:4.0%}")
out.append(f"\nMC свернул в одно слово: {sum(one.values())} из 120; по группам: " + ", ".join(f"{g} {sum(one[w] for w in W if IT[w]['grp'] == g)}/15" for g in G))
dis = [w for w in W if f("M1", w) != f("M2", w)]; good = [w for w in dis if (f("M1", w) > f("M2", w)) == one[w]]
out.append(f"выбор MC на спорных фразах (M1 ≠ M2 по «близко»): верный {len(good)} из {len(dis)} ({len(good) / max(1, len(dis)):.0%})")
for name, ws in (("MC свернул", [w for w in W if one[w]]), ("MC пословно", [w for w in W if not one[w]])):
    if ws: out.append(f"  {name:12s} n {len(ws):3d}: M1 {np.mean([f('M1', w) for w in ws]):4.0%}  M2 {np.mean([f('M2', w) for w in ws]):4.0%}  MC {np.mean([f('MC', w) for w in ws]):4.0%}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
esc = lambda c: c.replace("|", "\\|"); md = ["| фраза | группа | " + " | ".join(f"{v} | →" for v in VR) + " |", "|---|---|" + "---|---|" * len(VR)]
for w in sorted(W, key=lambda w: (G.index(IT[w]["grp"]), w)):
    cells = []
    for v in VR: cells += [f"`{esc(C[v][w])}`", ", ".join(f"{A[(r, w)]} ({s[(r, w)]})" for r in RD[v] if (r, w) in A)]
    md.append(f"| {w} | {IT[w]['grp']} | " + " | ".join(cells) + " |")
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
