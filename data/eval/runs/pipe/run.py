# pipe (dec.md): многопроходный кодировщик E0/ES/E1/E1V × декодер D0/D1 на предложениях Brown.
#   run.py stage SC NAME  — готовит каталог агента SC/NAME/{spec.md,list.md}; агент пишет SC/NAME/answers.md
#     E0 P1 → ES P2 → P3 → V1 → V2      (P1 упрощает, P2 ставит {}, P3 кодирует = E1, V1 — Haiku читает E1, V2 правит = E1V)
#   run.py check SC NAME  — проверка кодов по правилам (check_sent.mjs)
#   run.py readers SC     — 16 слепых читателей Haiku: 4 кодировщика × D0/D1 × 2
#   run.py judges SC      — пары (исходное, прочтение) перемешаны, судьи Sonnet по 120;   run.py score SC
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R0 = f"{D}/../../../.."; cmd, S = sys.argv[1], sys.argv[2]
SET = os.environ.get("SET", "dev"); SN = json.load(open(f"{D}/sents.json"))[SET]; N = len(SN); OUT = f"{D}/{SET}"
T = lambda f: open(f"{D}/tasks/{f}").read()
def spec(kind):
    p = f"{S}/{kind}_sents.md"
    subprocess.run([f"{R0}/.venv/bin/python", f"{R0}/scripts/eval/prepare.py", "spec", kind, "sents", p, "--braces"], check=True, capture_output=True)
    s = open(p).read(); assert "## Roots (45)" in s; return s
def ans(name):
    a = {int(m[1]): m[2].strip() for x in open(f"{S}/{name}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    assert sorted(a) == list(range(1, N + 1)), (name, sorted(set(range(1, N + 1)) - set(a))); return [a[i + 1] for i in range(N)]
def code(name): return [re.sub(r"^`+|`+$", "", c).strip() for c in ans(name)]
def put(name, sp, lines):
    d = f"{S}/{name}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
    open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {x}\n" for i, x in enumerate(lines)))
ALLV = {"E0": "E0", "ES": "ES", "E1": "P3", "E1V": "V2", "E0V": "W2"}  # E0V (holdout, разведка): E0 → чтение W1 → правка W2
ENCV = {k: ALLV[k] for k in os.environ.get("ENCS", "E0,ES,E1,E1V").split(",")}
DECS = os.environ.get("DECS", "D0,D1").split(","); SON = [x for x in os.environ.get("SONNET", "").split(",") if x]  # кодировщики, которые читает ещё и Sonnet (1 читатель, D0)
def dec_body():
    s = spec("dec"); i = s.index("## Task"); j = s.index("WORD BOUNDARIES"); return s[:i] + s[j:]
if cmd == "stage":
    n = sys.argv[3]; enc = spec("enc"); body = enc[enc.index("# min-co: how a word is written"):]; orig = [x["s"] for x in SN]
    if n == "E0": put(n, enc, orig)
    elif n == "P1": put(n, T("P1_simplify.md") + "\n\n# Reference: the min-co spec\n\n" + body, orig)
    elif n == "ES": put(n, enc, ans("P1"))
    elif n == "P2": put(n, T("P2_bracket.md") + "\n\n# Reference: the min-co spec\n\n" + body, ans("P1"))
    elif n == "P3": put(n, enc + "\n\n" + T("P3_encode.md"), ans("P2"))
    elif n == "V1": put(n, dec_body() + "\n\n" + T("D1_read.md"), code("P3"))
    elif n == "V2":
        r = ans("V1"); put(n, enc + "\n\n" + T("V2_revise.md"), [f"INTENDED: {b}\n   CODE: {c}\n   READ AS: {x}" for b, c, x in zip(ans("P2"), code("P3"), r)])
    elif n == "W1": put(n, dec_body() + "\n\n" + T("D1_read.md"), code("E0"))
    elif n == "W2":
        r = ans("W1"); put(n, enc + "\n\n" + T("V2_revise.md"), [f"INTENDED: {b}\n   CODE: {c}\n   READ AS: {x}" for b, c, x in zip(orig, code("E0"), r)])
    print("ok", n, N); sys.exit()
if cmd == "check":
    n = sys.argv[3]; cs = code(n); tmp = f"{S}/chk_{n}.json"; json.dump({str(i + 1): c for i, c in enumerate(cs)}, open(tmp, "w"))
    r = json.loads(subprocess.run(["node", f"{D}/check_sent.mjs", tmp], capture_output=True, text=True).stdout)
    bad = {k: v["bad"] for k, v in r.items() if v["bad"]}; print(n, "строк с ошибками:", len(bad), "слов:", sum(v["n"] for v in r.values()))
    for k, v in bad.items(): print(f"{k}. " + " ; ".join(v))
    sys.exit()
if cmd == "readers":
    db = dec_body(); L = []; r = 0
    for v, src in ENCV.items():
        cs = code(src)
        for dv, rep, lab in [(dv, rep, v) for dv in DECS for rep in range(2)] + ([("D0", 0, v + "@sonnet")] if v in SON else []):
                r += 1; o = list(range(N)); random.Random(1000 + r).shuffle(o)
                put(f"t{r}", db + "\n\n" + T(f"{dv}_read.md"), [cs[i] for i in o]); L.append({"r": r, "enc": lab, "dec": dv, "order": o})
    os.makedirs(OUT, exist_ok=True); json.dump(L, open(f"{OUT}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{OUT}/lists.json")); RD = {}
for l in L:
    a = ans(f"t{l['r']}")
    for k, i in enumerate(l["order"]):
        x = a[k].split("=>")[-1].strip() if l["dec"] == "D1" else a[k]; RD[(l["r"], i)] = x
if cmd == "judges":
    keys = sorted(RD); random.Random(7).shuffle(keys); per = 120; P = []
    for j in range(-(-len(keys) // per)):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/u{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. ORIGINAL: {SN[i]['s']}\n   READING: {RD[(r, i)]}\n" for t, (r, i) in enumerate(ch)))
        open(f"{d}/spec.md", "w").write(T("judge.md")); P += [{"j": j + 1, "t": t + 1, "r": r, "i": i} for t, (r, i) in enumerate(ch)]
    json.dump(P, open(f"{OUT}/pairs.json", "w")); print(len(keys), "пар,", j + 1, "судей"); sys.exit()
# score
P = json.load(open(f"{OUT}/pairs.json")); sc = {}
for j in {p["j"] for p in P}:
    sc[j] = {int(m[1]): int(m[2]) for l in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([0-3])", l))}
G = {(p["r"], p["i"]): sc[p["j"]][p["t"]] for p in P}; assert len(G) == len(RD)
for sub in ("answers", "judge", "codes"): os.makedirs(f"{OUT}/{sub}", exist_ok=True)
for l in L: open(f"{OUT}/answers/t{l['r']}_{l['enc']}_{l['dec']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
for j in sc: open(f"{OUT}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
for n in ("E0", "P1", "ES", "P2", "P3", "V1", "V2", "W1", "W2"):
    if os.path.exists(f"{S}/{n}/answers.md"): open(f"{OUT}/codes/{n}.md", "w").write(open(f"{S}/{n}/list.md").read() + "---\n" + open(f"{S}/{n}/answers.md").read())
M = {}; NR = {}
for l in L: NR[(l["enc"], l["dec"])] = NR.get((l["enc"], l["dec"]), 0) + 1
for l in L:
    for i in range(N): M.setdefault((l["enc"], l["dec"]), np.zeros(N)); M[(l["enc"], l["dec"])][i] += G[(l["r"], i)] / NR[(l["enc"], l["dec"])]
json.dump({f"{e}/{d}": list(v) for (e, d), v in M.items()}, open(f"{OUT}/per_sent.json", "w"))
rng = np.random.default_rng(0); B = rng.integers(0, N, (5000, N)); out = []
for k, v in sorted(M.items()): out.append(f"{k[0]:4s} {k[1]}  среднее {v.mean():.2f}/3  ≥2: {np.mean(v >= 2) * 100:.0f} %  =3: {np.mean(v >= 3) * 100:.0f} %")
def diff(a, b):
    d = M[a] - M[b]; bs = d[B].mean(1); return f"{a[0]}/{a[1]} − {b[0]}/{b[1]}: {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]"
for a, b in [(("ES", "D0"), ("E0", "D0")), (("E1", "D0"), ("ES", "D0")), (("E1V", "D0"), ("E1", "D0")), (("E1", "D0"), ("E0", "D0")),
             (("E1V", "D0"), ("E0", "D0")), (("E0", "D1"), ("E0", "D0")), (("E1", "D1"), ("E1", "D0")), (("E1V", "D1"), ("E1V", "D0")),
             (("E0V", "D0"), ("E0", "D0")), (("E1V", "D0"), ("E0V", "D0")), (("E1V@sonnet", "D0"), ("E0@sonnet", "D0"))]:
    if a in M and b in M: out.append(diff(a, b))
best = max((k for k in M if "@" not in k[0]), key=lambda k: M[k].mean()); out.append(f"лучший: {best[0]}/{best[1]}"); out.append(diff(best, ("E0", "D0")) if best != ("E0", "D0") else "")
open(f"{OUT}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
