# mini2 (dec.md): сильный правщик (Sonnet) поверх кода и слепого прочтения gpt-5-mini из ../mini.
#   run.py revise SC   → SC/v (spec.md = ENC_SENTS + задача правки воркера, blocks.md); агент пишет SC/v/answers.md
#   run.py check SC    → нарушения правил в SC/v/answers.md (w/check.js из ../mini)
#   run.py readers SC  → codes.json, lists.json, SC/tK (по 2 слепых Haiku на M0, MV, SR, S; D0 как в pipe)
#   run.py judges SC   → pairs.json, SC/uK (судьи Sonnet, judge.md из pipe);   run.py score SC → result.txt, answers/, judge/
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); MI = f"{D}/../mini"; P = f"{D}/../pipe"; R0 = f"{D}/../../../.."; cmd, S = sys.argv[1], sys.argv[2]
SN = [x["s"] for x in json.load(open(f"{P}/sents.json"))["holdout"]]
E = [e for e in sorted(json.load(open(f"{MI}/enc.json")), key=lambda e: e["i"]) if "code" in e]  # 57 предложений без сбоя
IX = [e["i"] for e in E]; N = len(IX); V = ["M0", "MV", "SR", "S"]
num = lambda txt: {int(m[1]): m[2].strip() for x in txt.splitlines() if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
js = lambda name: subprocess.run(["node", "-e", f'import("{MI}/w/prompts.js").then(m=>process.stdout.write(m.{name}))'], capture_output=True, text=True).stdout
def put(d, files):
    os.makedirs(d, exist_ok=True)
    for k, v in files.items(): open(f"{d}/{k}", "w").write(v)
def sr():
    a = num(open(f"{S}/v/answers.md").read()); return [re.sub(r"^`+|`+$", "", a.get(k + 1, "(no code)")).strip() for k in range(N)]
if cmd == "revise":
    rev = re.search(r"const SENT_REVISE = `([\s\S]*?)`;", open(f"{MI}/w/index.js").read())[1]
    task = rev.replace('Reply with ONLY a JSON object: {"code": "<the revised code>"}',
        "The items are in blocks.md, numbered. Reply by writing answers.md: one line per item, exactly \"N. <the revised code>\", nothing else.")
    put(f"{S}/v", {"spec.md": js("ENC_SENTS") + task, "blocks.md": "".join(
        f"{k + 1}. INTENDED: {SN[e['i']]}\n   CODE: {e['first']}\n   READ AS: {' / '.join(e['readback']['words'])} => {e['readback']['sentence']}\n" for k, e in enumerate(E))})
    sys.exit()
if cmd == "check":
    p = f"{S}/chk.mjs"; open(p, "w").write(f'import {{ sentenceProblems }} from "{MI}/w/check.js"; import fs from "fs";\n'
        'const C = JSON.parse(fs.readFileSync(process.argv[2])); for (const [k, c] of Object.entries(C)) { const b = sentenceProblems(c); if (b.length) console.log(k, b.join(" ; ")); }')
    json.dump({k + 1: c for k, c in enumerate(sr())}, open(f"{S}/chk.json", "w")); print(subprocess.run(["node", p, f"{S}/chk.json"], capture_output=True, text=True).stdout or "ok"); sys.exit()
def dec_body():
    p = f"{S}/dec_sents.md"; subprocess.run([f"{R0}/.venv/bin/python", f"{R0}/scripts/eval/prepare.py", "spec", "dec", "sents", p, "--braces"], check=True, capture_output=True)
    s = open(p).read(); i = s.index("## Task"); j = s.index("WORD BOUNDARIES"); return s[:i] + s[j:]
if cmd == "readers":
    sc = json.load(open(f"{MI}/s_codes.json"))
    C = {"M0": [e["first"] for e in E], "MV": [e["code"] for e in E], "SR": sr(), "S": [sc[i] for i in IX]}
    json.dump({"sents": IX, **C}, open(f"{D}/codes.json", "w"), indent=1); db = dec_body() + "\n\n" + open(f"{P}/tasks/D0_read.md").read(); L = []
    for v in V:
        for rep in range(2): o = list(range(N)); random.Random(3000 + len(L)).shuffle(o); L.append({"enc": v, "order": o})
    random.Random(4).shuffle(L)
    for r, l in enumerate(L, 1): l["r"] = r; put(f"{S}/t{r}", {"spec.md": db, "list.md": "".join(f"{k + 1}. {C[l['enc']][i]}\n" for k, i in enumerate(l["order"]))})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{D}/lists.json")); RD = {}
for l in L:
    a = num(open(f"{S}/t{l['r']}/answers.md").read())
    for k, i in enumerate(l["order"]): RD[(l["r"], i)] = a.get(k + 1, "—")
if cmd == "judges":
    keys = sorted(RD); random.Random(8).shuffle(keys); per = 120; PR = []
    for j in range(-(-len(keys) // per)):
        ch = keys[j * per:(j + 1) * per]
        put(f"{S}/u{j + 1}", {"spec.md": open(f"{P}/tasks/judge.md").read(), "pairs.md": "".join(f"{t + 1}. ORIGINAL: {SN[IX[i]]}\n   READING: {RD[(r, i)]}\n" for t, (r, i) in enumerate(ch))})
        PR += [{"j": j + 1, "t": t + 1, "r": r, "i": i} for t, (r, i) in enumerate(ch)]
    json.dump(PR, open(f"{D}/pairs.json", "w")); print(len(keys), "пар,", j + 1, "судей"); sys.exit()
PR = json.load(open(f"{D}/pairs.json")); sc = {}
for j in {p["j"] for p in PR}: sc[j] = {int(m[1]): int(m[2]) for x in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([0-3])", x))}
G = {(p["r"], p["i"]): sc[p["j"]][p["t"]] for p in PR}; assert len(G) == len(RD)
for sub in ("answers", "judge"): os.makedirs(f"{D}/{sub}", exist_ok=True)
for l in L: open(f"{D}/answers/t{l['r']}_{l['enc']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
for j in sc: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
open(f"{D}/revise.md", "w").write(open(f"{S}/v/blocks.md").read() + "---\n" + open(f"{S}/v/answers.md").read())
M = {v: np.array([np.mean([G[(l["r"], i)] for l in L if l["enc"] == v]) for i in range(N)]) for v in V}
rng = np.random.default_rng(0); B = rng.integers(0, N, (5000, N)); out = []
for v in V: out.append(f"{v:3s} среднее {M[v].mean():.2f}/3  ≥2: {np.mean(M[v] >= 2) * 100:.0f} %")
for a, b in (("SR", "M0"), ("SR", "S"), ("MV", "M0"), ("S", "M0")):
    d = M[a] - M[b]; bs = d[B].mean(1); out.append(f"{a} − {b}: {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]")
C = json.load(open(f"{D}/codes.json")); out.append("слов на предложение: " + "  ".join(f"{v} {np.mean([c.count('{') for c in C[v]]):.1f}" for v in V))
out.append(f"SR: код не изменён у {sum(a == b for a, b in zip(C['SR'], C['M0']))}/{N}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
