# conj (dec.md): OLD vs NEW (связки), по 2 независимых прогона кодировщика E0V на ячейку (a, b), по 2 слепых Haiku на прогон.
#   run.py stage S E0|W1|W2 OLDa|OLDb|NEWa|NEWb — каталог агента S/<stage>_<unit>; агент пишет answers.md
#   run.py check S <stage>_<unit>     run.py readers S (8 слепых Haiku, D0)     run.py judges S     run.py score S
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R0 = f"{D}/../../../.."; cmd, S = sys.argv[1], sys.argv[2]
sys.path.insert(0, f"{R0}/scripts/eval"); sys.path.insert(0, D)
from prepare import build_spec
import grammar
SN = json.load(open(f"{D}/sents.json")); N = len(SN); OUT = D; CELLS = ["OLD", "NEW"]; UNITS = [c + x for c in CELLS for x in "ab"]
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
    st, u = sys.argv[3], sys.argv[4]; c = u[:3]; n = f"{st}_{u}"
    if st == "E0": put(n, spec("enc", c), orig)
    elif st == "W1": put(n, dec_body(c) + "\n\n" + T("D1_read.md"), code(f"E0_{u}"))
    elif st == "W2":
        r = ans(f"W1_{u}"); put(n, spec("enc", c) + "\n\n" + T("V2_revise.md"),
                               [f"INTENDED: {b}\n   CODE: {x}\n   READ AS: {y}" for b, x, y in zip(orig, code(f"E0_{u}"), r)])
    print("ok", n, N); sys.exit()
def chk(n):
    c = n.split("_")[1][:3]; tmp = f"{S}/chk_{n}.json"; json.dump({str(i + 1): x for i, x in enumerate(code(n))}, open(tmp, "w"))
    return json.loads(subprocess.run(["node", f"{D}/check_sent.mjs", tmp, c], capture_output=True, text=True, check=True).stdout)
if cmd == "check":
    n = sys.argv[3]; r = chk(n); bad = {k: v["bad"] for k, v in r.items() if v["bad"]}
    print(n, "строк с ошибками:", len(bad), "слов:", sum(v["n"] for v in r.values()), "связок:", sum(v["nc"] for v in r.values()))
    for k, v in bad.items(): print(f"{k}. " + " ; ".join(v))
    sys.exit()
if cmd == "readers":
    L = []; r = 0
    for u in UNITS:
        cs = code(f"W2_{u}")
        for rep in range(2):
            r += 1; o = list(range(N)); random.Random(3000 + r).shuffle(o)
            put(f"t{r}", dec_body(u[:3]) + "\n\n" + T("D0_read.md"), [cs[i] for i in o]); L.append({"r": r, "unit": u, "cell": u[:3], "order": o})
    json.dump(L, open(f"{OUT}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{OUT}/lists.json")); RD = {}
for l in L:
    a = ans(f"t{l['r']}")
    for k, i in enumerate(l["order"]): RD[(l["r"], i)] = a[k]
if cmd == "judges":
    keys = sorted(RD); random.Random(9).shuffle(keys); per = 120; P = []
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
for u in UNITS:
    for st in ("E0", "W1", "W2"):
        n = f"{st}_{u}"; open(f"{OUT}/codes/{n}.md", "w").write(open(f"{S}/{n}/list.md").read() + "---\n" + open(f"{S}/{n}/answers.md").read())
M = {c: np.zeros(N) for c in CELLS}; MU = {u: np.zeros(N) for u in UNITS}
for l in L:
    for i in range(N): M[l["cell"]][i] += G[(l["r"], i)] / 4; MU[l["unit"]][i] += G[(l["r"], i)] / 2
json.dump({c: list(v) for c, v in {**M, **MU}.items()}, open(f"{OUT}/per_sent.json", "w"))
rng = np.random.default_rng(0); out = []
def diff(mask, lab):
    idx = np.flatnonzero(mask); d = (M["NEW"] - M["OLD"])[idx]; B = rng.integers(0, len(idx), (5000, len(idx))); bs = d[B].mean(1)
    out.append(f"NEW − OLD {lab} (n={len(idx)}): {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]   OLD {M['OLD'][idx].mean():.2f}  NEW {M['NEW'][idx].mean():.2f}")
low = [x.lower() for x in orig]
CL = {"contrast": r"\b(but|yet|however|although|though)\b", "cond": r"\b(if|unless)\b", "cause": r"\b(because|since)\b",
      "result": r"\b(so|therefore|thus)\b", "alt": r"\bor\b", "time": r"\b(when|while|as|after|before|until)\b", "rel": r"\b(who|which|whom|whose)\b"}
has = np.array([any(re.search(x, s) for x in CL.values()) for s in low])
for c in CELLS: out.append(f"{c}  среднее {M[c].mean():.2f}/3  ≥2: {np.mean(M[c] >= 2) * 100:.0f} %")
for u in UNITS: out.append(f"  прогон {u}: {MU[u].mean():.2f}")
diff(np.ones(N, bool), "все"); diff(has, "со связкой"); diff(~has, "без связки")
for c in CELLS:  # вторичная: класс связки сохранён в прочтении
    h = t = 0
    for l in L:
        if l["cell"] != c: continue
        for i in range(N):
            for k, x in CL.items():
                if re.search(x, low[i]): t += 1; h += bool(re.search(x, RD[(l["r"], i)].lower()))
    w = nc = e = 0
    for u in UNITS:
        if u[:3] == c: r = chk(f"W2_{u}"); w += sum(v["n"] for v in r.values()); nc += sum(v["nc"] for v in r.values()); e += sum(1 for v in r.values() if v["bad"])
    out.append(f"{c}: связка того же класса в прочтении {h}/{t};  слов (2 прогона) {w}, связок {nc}, строк с ошибками {e}")
open(f"{OUT}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
