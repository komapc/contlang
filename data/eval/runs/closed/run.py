# closed (dec.md): OLD vs NEW грамматика, кодировщик E0V (кодировать → слепое чтение → правка), пары ячеек одинаковы кроме спецификации.
#   run.py stage S E0|W1|W2 OLD|NEW — каталог агента S/<stage>_<cell>/{spec.md,list.md}; агент пишет answers.md
#   run.py check S <stage>_<cell>     run.py readers S (4 слепых Haiku: 2 на ячейку, D0)     run.py judges S     run.py score S
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R0 = f"{D}/../../../.."; cmd, S = sys.argv[1], sys.argv[2]
sys.path.insert(0, f"{R0}/scripts/eval"); sys.path.insert(0, D)
from prepare import build_spec
import grammar
SN = json.load(open(f"{D}/sents.json")); N = len(SN); OUT = D; CELLS = ["OLD", "NEW"]
T = lambda f: open(f"{D}/tasks/{f}").read()
def spec(kind, cell):
    s = build_spec(kind, "sents", braces=True); assert "## Roots (45)" in s
    return grammar.patch(s) if cell == "NEW" else s
def dec_body(cell):
    s = spec("dec", cell); i = s.index("## Task"); j = s.index("WORD BOUNDARIES"); return s[:i] + s[j:]
def ans(name):
    a = {int(m[1]): m[2].strip() for x in open(f"{S}/{name}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    assert sorted(a) == list(range(1, N + 1)), (name, sorted(set(range(1, N + 1)) - set(a))); return [a[i + 1] for i in range(N)]
def code(name): return [re.sub(r"^`+|`+$", "", c).strip() for c in ans(name)]
def put(name, sp, lines):
    d = f"{S}/{name}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
    open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {x}\n" for i, x in enumerate(lines)))
orig = [x["s"] for x in SN]
if cmd == "stage":
    st, c = sys.argv[3], sys.argv[4]; n = f"{st}_{c}"
    if st == "E0": put(n, spec("enc", c), orig)
    elif st == "W1": put(n, dec_body(c) + "\n\n" + T("D1_read.md"), code(f"E0_{c}"))
    elif st == "W2":
        r = ans(f"W1_{c}"); put(n, spec("enc", c) + "\n\n" + T("V2_revise.md"),
                               [f"INTENDED: {b}\n   CODE: {x}\n   READ AS: {y}" for b, x, y in zip(orig, code(f"E0_{c}"), r)])
    print("ok", n, N); sys.exit()
def chk(n):
    c = n.split("_")[1]; tmp = f"{S}/chk_{n}.json"; json.dump({str(i + 1): x for i, x in enumerate(code(n))}, open(tmp, "w"))
    return json.loads(subprocess.run(["node", f"{D}/check_sent.mjs", tmp, c], capture_output=True, text=True, check=True).stdout)
if cmd == "check":
    n = sys.argv[3]; r = chk(n); bad = {k: v["bad"] for k, v in r.items() if v["bad"]}
    print(n, "строк с ошибками:", len(bad), "слов:", sum(v["n"] for v in r.values()), "из них p:", sum(v["np"] for v in r.values()))
    for k, v in bad.items(): print(f"{k}. " + " ; ".join(v))
    sys.exit()
if cmd == "readers":
    L = []; r = 0
    for c in CELLS:
        cs = code(f"W2_{c}")
        for rep in range(2):
            r += 1; o = list(range(N)); random.Random(2000 + r).shuffle(o)
            put(f"t{r}", dec_body(c) + "\n\n" + T("D0_read.md"), [cs[i] for i in o]); L.append({"r": r, "cell": c, "order": o})
    json.dump(L, open(f"{OUT}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{OUT}/lists.json")); RD = {}
for l in L:
    a = ans(f"t{l['r']}")
    for k, i in enumerate(l["order"]): RD[(l["r"], i)] = a[k]
if cmd == "judges":
    keys = sorted(RD); random.Random(8).shuffle(keys); per = 120; P = []
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
for l in L: open(f"{OUT}/answers/t{l['r']}_{l['cell']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
for j in sc: open(f"{OUT}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
for c in CELLS:
    for st in ("E0", "W1", "W2"):
        n = f"{st}_{c}"; open(f"{OUT}/codes/{n}.md", "w").write(open(f"{S}/{n}/list.md").read() + "---\n" + open(f"{S}/{n}/answers.md").read())
M = {c: np.zeros(N) for c in CELLS}
for l in L:
    for i in range(N): M[l["cell"]][i] += G[(l["r"], i)] / 2
json.dump({c: list(v) for c, v in M.items()}, open(f"{OUT}/per_sent.json", "w"))
rng = np.random.default_rng(0); out = []
def diff(mask, lab):
    idx = np.flatnonzero(mask); d = (M["NEW"] - M["OLD"])[idx]; B = rng.integers(0, len(idx), (5000, len(idx))); bs = d[B].mean(1)
    out.append(f"NEW − OLD {lab} (n={len(idx)}): {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]   OLD {M['OLD'][idx].mean():.2f}  NEW {M['NEW'][idx].mean():.2f}")
low = [x.lower() for x in orig]
PRON = r"\b(he|him|his|she|her|they|them|their)\b"; PREP = r"\b(to|in|on|at|with|from|for|about|by|into|of|under|over|after|before|through|than|without|toward)\b"
pron = np.array([bool(re.search(PRON, s)) for s in low]); prep = np.array([bool(re.search(PREP, s)) for s in low])
for c in CELLS: out.append(f"{c}  среднее {M[c].mean():.2f}/3  ≥2: {np.mean(M[c] >= 2) * 100:.0f} %")
diff(np.ones(N, bool), "все"); diff(pron, "с he/she/they…"); diff(prep & ~pron, "предлоги без he/she/they"); diff(~pron & ~prep, "ни того ни другого")
for c in CELLS:  # вторичная: третье лицо сохранено в прочтении
    h = t = 0
    for l in L:
        if l["cell"] != c: continue
        for i in np.flatnonzero(pron): t += 1; h += bool(re.search(PRON, RD[(l["r"], i)].lower()))
    r = chk(f"W2_{c}"); out.append(f"{c}: he/she/they сохранено {h}/{t};  слов {sum(v['n'] for v in r.values())}, из них p {sum(v['np'] for v in r.values())}, строк с ошибками {sum(1 for v in r.values() if v['bad'])}")
open(f"{OUT}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
