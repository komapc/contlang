# very (dec.md): степень — метка I / значение оси X / оба IX / отдельное слово W.
#   run.py writer SC → SC/w/{spec.md,list.md}  (Sonnet пишет answers.md)
#   run.py build SC  → codes.json;  run.py readers SC → SC/t{r} (8 Haiku);  run.py pairs SC → SC/u1;  run.py score SC
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); R0 = f"{D}/../../../.."; cmd, S = sys.argv[1], sys.argv[2]
ADJ = ["cold", "happy", "tired", "fast", "big", "angry", "old", "hungry", "dangerous", "expensive", "quiet", "strong"]
DEG = {"barely": 1, "slightly": 2, "very": 4, "extremely": 5}; IM = {"barely": -5, "slightly": -2, "very": 4, "extremely": 5}
VR = ["I", "X", "IX", "W"]
spec = lambda k: subprocess.run(["node", "-e", f'import("./prompts.js").then(m=>process.stdout.write(m.{k}))'], cwd=f"{R0}/worker", capture_output=True, text=True).stdout
ITEMS = [(a, None) for a in ADJ] + [(a, d) for a in ADJ for d in DEG]
key = lambda a, d: f"{d} {a}" if d else a
def put(d, sp, lines):
    os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp); open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {x}\n" for i, x in enumerate(lines)))
def ans(d, n):
    a = {int(m[1]): m[2].strip().strip("`").strip() for x in open(f"{d}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    assert sorted(a) == list(range(1, n + 1)), d; return [a[i + 1] for i in range(n)]
WL = [f"ADJ {a}" for a in ADJ] + [f"ADV {d}" for d in DEG]
if cmd == "writer":
    es = spec("ENC_SPEC"); body = es[es.index("# min-co: how a word is written"):]; assert "## Roots (45)" in body
    put(f"{S}/w", open(f"{D}/writer_task.md").read() + "\n" + body, WL); print("ok"); sys.exit()
if cmd == "build":
    w = dict(zip(WL, ans(f"{S}/w", len(WL)))); C = {v: {} for v in VR}
    for a, d in ITEMS:
        b = w[f"ADJ {a}"]; m = re.match(r"\s*([A-Z]+)\(=([+-]?\d)\)", b); assert m and abs(int(m[2])) == 3, (a, b)
        if d is None:
            for v in VR: C[v][a] = b
            continue
        x = re.sub(r"\(=[+-]?\d\)", f"(={'+' if int(m[2]) > 0 else '-'}{DEG[d]})", b, count=1)
        i = lambda c: re.sub(r"(\|\s*a)", rf"\1 I{IM[d]:+d}", c, count=1)
        C["I"][key(a, d)] = i(b); C["X"][key(a, d)] = x; C["IX"][key(a, d)] = i(x); C["W"][key(a, d)] = b + " " + w[f"ADV {d}"]
    json.dump(C, open(f"{D}/codes.json", "w"), indent=1); [print(k, "|", C["I"][k], "|", C["X"][k], "|", C["W"][k]) for k in list(C["I"])[:16]]; sys.exit()
C = json.load(open(f"{D}/codes.json")); K = [key(a, d) for a, d in ITEMS]
if cmd == "readers":
    sp = spec("DEC_SPEC"); sp = sp[:sp.index("## Task")] if "## Task" in sp else sp; L = []; r = 0
    for v in VR:
        for rep in range(2):
            r += 1; o = K[:]; random.Random(500 + r).shuffle(o); put(f"{S}/t{r}", sp + "\n\n" + open(f"{D}/reader_task.md").read(), [C[v][k] for k in o]); L.append({"r": r, "var": v, "items": o})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(f"{D}/lists.json")); A = {}
for l in L:
    for k, x in zip(l["items"], ans(f"{S}/t{l['r']}", len(K))):
        p = x.split("|"); g = re.search(r"[1-5]", p[-1]) if len(p) > 1 else None; A[(l["r"], k)] = (p[0].strip().lower(), int(g[0]) if g else 3)
adj = {key(a, d): a for a, d in ITEMS}; tgt = {key(a, d): DEG.get(d, 3) for a, d in ITEMS}
if cmd == "pairs":
    P = sorted({(adj[k], x[0]) for (r, k), x in A.items()}); os.makedirs(f"{S}/u1", exist_ok=True)
    open(f"{S}/u1/pairs.md", "w").write("".join(f"{i + 1}. {a} — {b}\n" for i, (a, b) in enumerate(P))); json.dump(P, open(f"{S}/pairs.json", "w")); print(len(P), "пар"); sys.exit()
P = json.load(open(f"{S}/pairs.json")); sc = {int(m[1]): int(m[2]) for l in open(f"{S}/u1/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
J = {(a, b): sc[i + 1] for i, (a, b) in enumerate(P)}
os.makedirs(f"{D}/answers", exist_ok=True)
for l in L: open(f"{D}/answers/t{l['r']}_{l['var']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
open(f"{D}/judge.md", "w").write(open(f"{S}/u1/pairs.md").read() + "---\n" + open(f"{S}/u1/scores.md").read())
open(f"{D}/writer.md", "w").write(open(f"{S}/w/list.md").read() + "---\n" + open(f"{S}/w/answers.md").read())
M = [k for k in K if k not in ADJ]; RV = {v: [l["r"] for l in L if l["var"] == v] for v in VR}; rng = np.random.default_rng(0); B = rng.integers(0, len(M), (5000, len(M)))
def per(v, f): return np.array([np.mean([f(A[(r, k)], k) for r in RV[v]]) for k in M])
hit = {v: per(v, lambda x, k: x[1] == tgt[k]) for v in VR}; err = {v: per(v, lambda x, k: abs(x[1] - tgt[k])) for v in VR}
mean = {v: per(v, lambda x, k: J[(adj[k], x[0])] == 2) for v in VR}
plain = {v: np.mean([A[(r, a)][1] == 3 for r in RV[v] for a in ADJ]) for v in VR}
out = [f"{v:3s} степень точно {hit[v].mean() * 100:4.0f} %  ошибка {err[v].mean():.2f}  смысл близко {mean[v].mean() * 100:4.0f} %  (простые слова: степень 3 у {plain[v] * 100:.0f} %)" for v in VR]
ci = lambda d: f"{d.mean() * 100:+.1f} п. п. [{np.percentile(d[B].mean(1), 2.5) * 100:+.1f} … {np.percentile(d[B].mean(1), 97.5) * 100:+.1f}]"
for v in ("I", "X", "IX"): out.append(f"{v} − W: степень {ci(hit[v] - hit['W'])}; смысл {ci(mean[v] - mean['W'])}")
out.append("по степеням (точно, %): " + "; ".join(f"{v}: " + " ".join(f"{d} {np.mean([hit[v][i] for i, k in enumerate(M) if k.startswith(d)]) * 100:.0f}" for d in DEG) for v in VR))
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
