# lex: потолок 45 корней на частых словах. 120 самых частых слов из ../big1000 (с частью речи и толкованием оттуда).
# Варианты: H — коды Haiku из big1000 (один проход); S1, S2 — два кодировщика Sonnet, один проход;
# V1, V2 — S1, S2 после слепого чтения (Haiku) и правки (новый Sonnet). Читают 10 слепых Haiku (по 2 на набор), судья Haiku.
#   run.py writers SC   → SC/s1, s2 (spec.md = ENC_SPEC, list.md, task.md)
#   run.py readback SC  → codes S1/S2 из SC/s*/answers.md, проверка; SC/b1, b2 — читатели для правки
#   run.py revise SC    → SC/v1, v2 (spec.md, blocks.md, task.md)
#   run.py readers SC   → codes.json; SC/rK (spec.md = DEC_SPEC, codes.md, task.md), lists.json
#   run.py pairs SC → SC/jK/pairs.md;  run.py score SC → result.txt, answers/, judge/, worst.md
import json, os, re, sys, random, subprocess
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."; B = f"{D}/../big1000"
cmd, S = sys.argv[1], sys.argv[2]
spec = lambda k: subprocess.run(["node", "-e", f'import("./prompts.js").then(m=>process.stdout.write(m.{k}))'], cwd=f"{R}/worker", capture_output=True, text=True).stdout
rank = {w: i for i, w in enumerate(json.load(open(f"{R}/site/data/math.json"))["words"])}
ITS = {o["w"]: o for o in json.load(open(f"{B}/items.json"))}
W = sorted(json.load(open(f"{B}/words.json")), key=lambda w: rank.get(w, 1e9))[:120]
T = lambda n: open(f"{D}/{n}").read()
line = lambda w: f"{w} ({ITS[w]['pos']}) — {ITS[w]['gloss']}"
def read(p):
    return {int(m[1]): m[2].strip().strip("`").strip() for x in open(p) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
def put(d, files):
    os.makedirs(d, exist_ok=True)
    for k, v in files.items(): open(f"{d}/{k}", "w").write(v)
def check(C):
    p = f"{S}/chk.json"; json.dump(C, open(p, "w"))
    out = json.loads(subprocess.run(["node", f"{D}/../phrases3/check.mjs", p], capture_output=True, text=True).stdout)
    return {k: v["bad"] + ([f"{v['n']} words"] if v["n"] != 1 else []) for k, v in out.items() if v["bad"] or v["n"] != 1}
def codes(sub):
    a = read(f"{S}/{sub}/answers.md"); return {w: a.get(i + 1, "") for i, w in enumerate(W)}
if cmd == "writers":
    json.dump([ITS[w] for w in W], open(f"{D}/items.json", "w"), indent=0); es = spec("ENC_SPEC")
    for k in (1, 2): put(f"{S}/s{k}", {"spec.md": es, "task.md": T("writer_task.md"), "list.md": "".join(f"{i + 1}. {line(w)}\n" for i, w in enumerate(W))})
    sys.exit()
if cmd in ("readback", "check"):
    for sub in sys.argv[3:] or ["s1", "s2"]:
        bad = check(codes(sub)); print(sub, len(bad), "неверных"); [print("  ", W.index(w) + 1, w, codes(sub)[w], b) for w, b in bad.items()]
    if cmd == "check": sys.exit()
    ds = spec("DEC_SPEC")
    for k in (1, 2): C = codes(f"s{k}"); put(f"{S}/b{k}", {"spec.md": ds, "task.md": T("reader_task.md"), "codes.md": "".join(f"{i + 1}. {C[w]}\n" for i, w in enumerate(W))})
    sys.exit()
if cmd == "revise":
    es = spec("ENC_SPEC")
    for k in (1, 2):
        C = codes(f"s{k}"); r = read(f"{S}/b{k}/answers.md")
        put(f"{S}/v{k}", {"spec.md": es, "task.md": T("revise_task.md"), "blocks.md": "".join(
            f"{i + 1}. INTENDED: {line(w)}\n   CODE: {C[w]}\n   READ AS: {r.get(i + 1, '—')}\n" for i, w in enumerate(W))})
    sys.exit()
if cmd == "readers":
    H = json.load(open(f"{B}/llm_codes.json")); SETS = {"H": {w: H[w] for w in W}, "S1": codes("s1"), "S2": codes("s2"), "V1": codes("v1"), "V2": codes("v2")}
    for v in ("V1", "V2"):
        bad = check(SETS[v]); print(v, len(bad), "неверных", bad)
    json.dump(SETS, open(f"{D}/codes.json", "w"), indent=1); ds = spec("DEC_SPEC"); random.seed(11); L = []
    for v, C in SETS.items():
        for rep in (1, 2):
            ws = W[:]; random.shuffle(ws); r = len(L) + 1
            put(f"{S}/r{r}", {"spec.md": ds, "task.md": T("reader_task.md"), "codes.md": "".join(f"{i + 1}. {C[w]}\n" for i, w in enumerate(ws))}); L.append({"r": r, "var": v, "words": ws})
    random.shuffle(L); [l.update(r=i + 1) for i, l in enumerate(L)]  # номера читателей не выдают вариант
    for l in L:
        C = SETS[l["var"]]; put(f"{S}/r{l['r']}", {"codes.md": "".join(f"{i + 1}. {C[w]}\n" for i, w in enumerate(l["words"]))})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{D}/lists.json")); A = {}  # (var, rep-reader, word) → first answer
for l in L:
    a = read(f"{S}/r{l['r']}/answers.md")
    for i, w in enumerate(l["words"]): A[(l["var"], l["r"], w)] = (a.get(i + 1) or "—").split("|")[0].strip().lower()
if cmd == "pairs":
    keys = sorted({(w, a) for (_, _, w), a in A.items()}); random.seed(3); random.shuffle(keys); n = -(-len(keys) // 150); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]
        put(f"{S}/j{j + 1}", {"task.md": T("judge_task.md"), "pairs.md": "".join(f"{t + 1}. {line(w)} — {a}\n" for t, (w, a) in enumerate(ch))})
        P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
# score
P = json.load(open(f"{S}/pairs.json")); sc = {}
for j in sorted({p["j"] for p in P}):
    s = {int(m[1]): int(m[2]) for x in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", x))}
    for p in P:
        if p["j"] == j: sc[(p["w"], p["a"])] = s[p["t"]]
os.makedirs(f"{D}/answers", exist_ok=True); os.makedirs(f"{D}/judge", exist_ok=True)
for l in L: open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
for j in sorted({p["j"] for p in P}): open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
V = ["H", "S1", "S2", "V1", "V2"]
per = {v: {w: [sc[(w, a)] for (vv, _, ww), a in A.items() if vv == v and ww == w] for w in W} for v in V}  # 2 чтения
cell = {"H": ["H"], "S": ["S1", "S2"], "V": ["V1", "V2"]}
def close(c, ws): return [sum(x == 2 for v in cell[c] for x in per[v][w]) / sum(len(per[v][w]) for v in cell[c]) for w in ws]
def rel(c, ws): return [sum(x >= 1 for v in cell[c] for x in per[v][w]) / sum(len(per[v][w]) for v in cell[c]) for w in ws]
def boot(a, b, ws, n=5000):
    rnd = random.Random(0); x, y = close(a, ws), close(b, ws); d = []
    for _ in range(n):
        ix = [rnd.randrange(len(ws)) for _ in ws]; d.append(sum(x[i] - y[i] for i in ix) / len(ix))
    d.sort(); return sum(x) / len(x) - sum(y) / len(y), d[int(.025 * n)], d[int(.975 * n)]
out = []
for c in cell: out.append(f"{c}  близко {sum(close(c, W)) / len(W):4.0%}  близко или рядом {sum(rel(c, W)) / len(W):4.0%}")
for v in V: out.append(f"  {v:3s} близко {sum(x == 2 for w in W for x in per[v][w]) / sum(len(per[v][w]) for w in W):4.0%}")
for a, b in (("V", "S"), ("S", "H"), ("V", "H")):
    m, lo, hi = boot(a, b, W); out.append(f"{a} − {b}  {m * 100:+.1f} п. п. [{lo * 100:+.1f} … {hi * 100:+.1f}]")
for p in ("noun", "verb", "adjective", "adverb"):
    ws = [w for w in W if ITS[w]["pos"] == p]
    if ws: out.append(f"  {p:9s} n {len(ws):3d}  " + "  ".join(f"{c} {sum(close(c, ws)) / len(ws):4.0%}" for c in cell))
best = max(cell, key=lambda c: sum(close(c, W)))
anyc = [w for w in W if any(x == 2 for v in V for x in per[v][w])]
never = [w for w in W if all(x == 0 for v in V for x in per[v][w])]
out.append(f"лучший вариант: {best}; хоть одно чтение «близко» в любом наборе: {len(anyc)}/{len(W)}; везде «мимо»: {len(never)} {never}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
C = json.load(open(f"{D}/codes.json"))
worst = sorted(W, key=lambda w: (sum(x for v in V for x in per[v][w]), rank.get(w, 1e9)))
md = ["| слово | " + " | ".join(V) + " |", "|---|" + "---|" * len(V)]
ans = lambda v, w: " / ".join(a for (vv, _, ww), a in sorted(A.items()) if vv == v and ww == w)
for w in worst[:40]: md.append(f"| **{w}** ({ITS[w]['pos']}) | " + " | ".join(f"`{C[v][w]}` → {ans(v, w)} ({'+'.join(map(str, per[v][w]))})" for v in V) + " |")
open(f"{D}/worst.md", "w").write("\n".join(md) + "\n")
