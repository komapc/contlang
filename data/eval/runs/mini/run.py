# mini (dec.md): конвейер PR #19 на gpt-5-mini против одного прохода и против конвейера Sonnet из pipe.
#   run.py scodes          → s_codes.json (S = E0V из pipe/holdout: Sonnet кодирует, Haiku читает, Sonnet правит)
#   node run.mjs encode/decode (нужен ключ OpenRouter) → enc.json, dec_gpt.json
#   run.py readers SC      → codes.json, lists.json, SC/tK (по 2 слепых Haiku на M0, MV, S; спецификация и задача как в pipe, D0)
#   run.py judges SC       → SC/uK (судьи Sonnet, judge.md из pipe);   run.py score SC → result.txt, answers/, judge/
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); P = f"{D}/../pipe"; R0 = f"{D}/../../../.."; cmd = sys.argv[1]; S = sys.argv[2] if len(sys.argv) > 2 else ""
SN = [x["s"] for x in json.load(open(f"{P}/sents.json"))["holdout"]]; N = len(SN); V = ["M0", "MV", "S"]
num = lambda txt: {int(m[1]): m[2].strip() for x in txt.splitlines() if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
if cmd == "scodes":
    a = num(open(f"{P}/holdout/codes/W2.md").read().split("\n---\n", 1)[1])
    json.dump([re.sub(r"^`+|`+$", "", a[i + 1]).strip() for i in range(N)], open(f"{D}/s_codes.json", "w"), indent=0); sys.exit()
def dec_body():
    p = f"{S}/dec_sents.md"; subprocess.run([f"{R0}/.venv/bin/python", f"{R0}/scripts/eval/prepare.py", "spec", "dec", "sents", p, "--braces"], check=True, capture_output=True)
    s = open(p).read(); i = s.index("## Task"); j = s.index("WORD BOUNDARIES"); return s[:i] + s[j:]
def put(d, files):
    os.makedirs(d, exist_ok=True)
    for k, v in files.items(): open(f"{d}/{k}", "w").write(v)
if cmd == "readers":
    E = sorted(json.load(open(f"{D}/enc.json")), key=lambda e: e["i"]); assert [e["i"] for e in E] == list(range(N))
    C = {"M0": [e.get("first") or "" for e in E], "MV": [e.get("code") or "" for e in E], "S": json.load(open(f"{D}/s_codes.json"))}
    json.dump(C, open(f"{D}/codes.json", "w"), indent=1); db = dec_body() + "\n\n" + open(f"{P}/tasks/D0_read.md").read(); L = []
    for v in V:
        for rep in range(2): o = list(range(N)); random.Random(2000 + len(L)).shuffle(o); L.append({"enc": v, "order": o})
    random.Random(3).shuffle(L)  # номер читателя не выдаёт вариант
    for r, l in enumerate(L, 1): l["r"] = r; put(f"{S}/t{r}", {"spec.md": db, "list.md": "".join(f"{k + 1}. {C[l['enc']][i]}\n" for k, i in enumerate(l["order"]))})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{D}/lists.json")); RD = {}
for l in L:
    a = num(open(f"{S}/t{l['r']}/answers.md").read())
    for k, i in enumerate(l["order"]): RD[(f"h{l['r']}", i)] = (l["enc"], a.get(k + 1, "—"))
for g in json.load(open(f"{D}/dec_gpt.json")): RD[(f"g_{g['v']}", g["i"])] = (g["v"], g["best"] or "—")
if cmd == "judges":
    keys = sorted(RD); random.Random(7).shuffle(keys); per = 120; PR = []
    for j in range(-(-len(keys) // per)):
        ch = keys[j * per:(j + 1) * per]
        put(f"{S}/u{j + 1}", {"spec.md": open(f"{P}/tasks/judge.md").read(), "pairs.md": "".join(f"{t + 1}. ORIGINAL: {SN[i]}\n   READING: {RD[(r, i)][1]}\n" for t, (r, i) in enumerate(ch))})
        PR += [{"j": j + 1, "t": t + 1, "r": r, "i": i} for t, (r, i) in enumerate(ch)]
    json.dump(PR, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", j + 1, "судей"); sys.exit()
# score
PR = json.load(open(f"{S}/pairs.json")); sc = {}
for j in {p["j"] for p in PR}: sc[j] = {int(m[1]): int(m[2]) for x in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([0-3])", x))}
G = {(p["r"], p["i"]): sc[p["j"]][p["t"]] for p in PR}; assert len(G) == len(RD)
for sub in ("answers", "judge"): os.makedirs(f"{D}/{sub}", exist_ok=True)
for l in L: open(f"{D}/answers/t{l['r']}_{l['enc']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
for j in sc: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
def cell(v, reader):  # средняя оценка по предложениям
    ks = [r for r in {k[0] for k in G} if (r.startswith("h") if reader == "haiku" else r == f"g_{v}") and RD[(r, 0)][0] == v]
    return np.array([np.mean([G[(r, i)] for r in ks]) for i in range(N)])
rng = np.random.default_rng(0); B = rng.integers(0, N, (5000, N)); out = []
M = {(v, rd): cell(v, rd) for rd in ("haiku", "gpt") for v in V if rd == "haiku" or v != "S"}
for (v, rd), x in M.items(): out.append(f"{v:3s} читатель {rd:5s}  среднее {x.mean():.2f}/3  ≥2: {np.mean(x >= 2) * 100:.0f} %")
for a, b, rd in (("MV", "M0", "haiku"), ("MV", "S", "haiku"), ("M0", "S", "haiku"), ("MV", "M0", "gpt")):
    d = M[(a, rd)] - M[(b, rd)]; bs = d[B].mean(1); out.append(f"{a} − {b} ({rd}): {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]")
E = json.load(open(f"{D}/enc.json")); out.append(f"кодов с нарушениями правил после правки: {sum(1 for e in E if e.get('warnings'))}/{N}; сбоев: {sum(1 for e in E if e.get('error'))}")
out.append("слов на предложение: " + "  ".join(f"{v} {np.mean([len(re.findall(r'{', c)) for c in json.load(open(f'{D}/codes.json'))[v]]):.1f}" for v in V))
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
