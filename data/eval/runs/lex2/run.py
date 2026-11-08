# lex2: проверенный словарь на новых читателях. Варианты V2 (из lex), L (выбор по чтениям lex, pick.json), R (второй круг правки V2).
#   run.py readback SC → SC/b (Haiku читает V2);  run.py revise SC → SC/v (Sonnet правит)
#   run.py readers SC  → codes.json, lists.json, SC/rK (3 Haiku + 1 Sonnet на вариант)
#   run.py pairs SC → SC/jK;  run.py score SC → result.txt, answers/, judge/
import json, os, re, sys, random, subprocess
D = os.path.dirname(os.path.abspath(__file__)); X = f"{D}/../lex"; R = f"{D}/../../../.."
cmd, S = sys.argv[1], sys.argv[2]
spec = lambda k: subprocess.run(["node", "-e", f'import("./prompts.js").then(m=>process.stdout.write(m.{k}))'], cwd=f"{R}/worker", capture_output=True, text=True).stdout
ITS = {o["w"]: o for o in json.load(open(f"{X}/items.json"))}; W = [o["w"] for o in json.load(open(f"{X}/items.json"))]
C0 = json.load(open(f"{X}/codes.json")); pick = json.load(open(f"{D}/pick.json"))
T = lambda n: open(f"{D}/{n}").read(); line = lambda w: f"{w} ({ITS[w]['pos']}) — {ITS[w]['gloss']}"
read = lambda p: {int(m[1]): m[2].strip().strip("`").strip() for x in open(p) if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
def put(d, files):
    os.makedirs(d, exist_ok=True)
    for k, v in files.items(): open(f"{d}/{k}", "w").write(v)
def check(C):
    p = f"{S}/chk.json"; json.dump(C, open(p, "w"))
    out = json.loads(subprocess.run(["node", f"{D}/../phrases3/check.mjs", p], capture_output=True, text=True).stdout)
    return {k: v["bad"] + ([f"{v['n']} words"] if v["n"] != 1 else []) for k, v in out.items() if v["bad"] or v["n"] != 1}
V2 = C0["V2"]; L = {w: C0[pick[w]][w] for w in W}
if cmd == "readback":
    put(f"{S}/b", {"spec.md": spec("DEC_SPEC"), "task.md": T("reader_task.md"), "codes.md": "".join(f"{i + 1}. {V2[w]}\n" for i, w in enumerate(W))}); sys.exit()
if cmd == "revise":
    r = read(f"{S}/b/answers.md")
    put(f"{S}/v", {"spec.md": spec("ENC_SPEC"), "task.md": T("revise_task.md"), "blocks.md": "".join(
        f"{i + 1}. INTENDED: {line(w)}\n   CODE: {V2[w]}\n   READ AS: {r.get(i + 1, '—')}\n" for i, w in enumerate(W))}); sys.exit()
def Rc():
    a = read(f"{S}/v/answers.md"); return {w: a.get(i + 1, "") for i, w in enumerate(W)}
if cmd == "check":
    print(check(Rc())); sys.exit()
if cmd == "readers":
    SETS = {"V2": V2, "L": L, "R": Rc()}; print({k: check(v) for k, v in SETS.items()})
    json.dump(SETS, open(f"{D}/codes.json", "w"), indent=1); ds = spec("DEC_SPEC"); random.seed(13); Ls = []
    for v in SETS:
        for m in ("haiku", "haiku", "haiku", "sonnet"):
            ws = W[:]; random.shuffle(ws); Ls.append({"var": v, "model": m, "words": ws})
    random.shuffle(Ls)
    for i, l in enumerate(Ls):
        l["r"] = i + 1; put(f"{S}/r{i + 1}", {"spec.md": ds, "task.md": T("reader_task.md"), "codes.md": "".join(f"{k + 1}. {SETS[l['var']][w]}\n" for k, w in enumerate(l["words"]))})
    json.dump(Ls, open(f"{D}/lists.json", "w")); print([(l["r"], l["model"]) for l in Ls]); sys.exit()
Ls = json.load(open(f"{D}/lists.json")); A = {}
for l in Ls:
    a = read(f"{S}/r{l['r']}/answers.md")
    for i, w in enumerate(l["words"]): A[(l["var"], l["model"], l["r"], w)] = (a.get(i + 1) or "—").split("|")[0].strip().lower()
if cmd == "pairs":
    keys = sorted({(k[3], a) for k, a in A.items()}); random.seed(5); random.shuffle(keys); n = -(-len(keys) // 150); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]
        put(f"{S}/j{j + 1}", {"task.md": T("judge_task.md"), "pairs.md": "".join(f"{t + 1}. {line(w)} — {a}\n" for t, (w, a) in enumerate(ch))})
        P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
P = json.load(open(f"{S}/pairs.json")); sc = {}
for j in sorted({p["j"] for p in P}):
    s = {int(m[1]): int(m[2]) for x in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", x))}
    for p in P:
        if p["j"] == j: sc[(p["w"], p["a"])] = s[p["t"]]
os.makedirs(f"{D}/answers", exist_ok=True); os.makedirs(f"{D}/judge", exist_ok=True)
for l in Ls: open(f"{D}/answers/r{l['r']}_{l['var']}_{l['model']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
for j in sorted({p["j"] for p in P}): open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
def close(v, m, ws):
    out = []
    for w in ws:
        x = [sc[(w, a)] for k, a in A.items() if k[0] == v and k[1] == m and k[3] == w]; out.append(sum(s == 2 for s in x) / len(x))
    return out
def boot(a, b, m, ws, n=5000):
    rnd = random.Random(0); x, y = close(a, m, ws), close(b, m, ws); d = []
    for _ in range(n):
        ix = [rnd.randrange(len(ws)) for _ in ws]; d.append(sum(x[i] - y[i] for i in ix) / len(ix))
    d.sort(); return (sum(x) - sum(y)) / len(ws), d[int(.025 * n)], d[int(.975 * n)]
out = []
diff = [w for w in W if L[w] != V2[w]]; codes = json.load(open(f"{D}/codes.json")); rdiff = [w for w in W if codes["R"][w] != V2[w]]
for m in ("haiku", "sonnet"):
    out.append(f"[{m}] " + "  ".join(f"{v} {sum(close(v, m, W)) / len(W):4.0%}" for v in ("V2", "L", "R")))
    for a in ("L", "R"):
        d, lo, hi = boot(a, "V2", m, W); out.append(f"  {a} − V2  {d * 100:+.1f} п. п. [{lo * 100:+.1f} … {hi * 100:+.1f}]")
    d, lo, hi = boot("L", "V2", m, diff); out.append(f"  L − V2 на {len(diff)} словах, где коды разные: {d * 100:+.1f} [{lo * 100:+.1f} … {hi * 100:+.1f}]")
    d, lo, hi = boot("R", "V2", m, rdiff); out.append(f"  R − V2 на {len(rdiff)} словах, где коды разные: {d * 100:+.1f} [{lo * 100:+.1f} … {hi * 100:+.1f}]")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
