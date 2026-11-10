# lexs (dec.md): выбор кода по чтениям gpt-5-mini и проверка в предложениях.
#   run.py pick              → pick.json, select.txt (выбор по чтениям 1–2, проверка на чтении 3, стоп-кран)
#   node run.mjs sent        → sent_codes.json
#   run.py readers SC        → lists.json, SC/tK (по 2 слепых Haiku на M0, MG, ML; по 60 предложений на читателя)
#   run.py judges SC         → pairs.json, SC/uK;   run.py score SC → result.txt, answers/, judge/
import json, os, re, sys, random, subprocess, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); P = f"{D}/../pipe"; R0 = f"{D}/../../../.."; cmd = sys.argv[1]; S = sys.argv[2] if len(sys.argv) > 2 else ""
J = lambda f: json.load(open(f"{D}/{f}")); V = ["G1", "G2", "S1", "S2"]
if cmd == "pick":
    L, R, Jd = J("lemmas.json"), J("reads.json"), J("judged.json"); n = len(L)
    sc = lambda v, rep, i: Jd.get(f"{i}\t{R[f'{v}/{rep}'][i].lower().strip()}")
    close = lambda v, rep, i: 1.0 if sc(v, rep, i) == 2 else 0.0
    pick = []
    for i in range(n):
        key = lambda v: (sum(close(v, r, i) for r in (1, 2)), sum((sc(v, r, i) or 0) for r in (1, 2)), -V.index(v))
        pick.append(max(V, key=key))
    json.dump(pick, open(f"{D}/pick.json", "w"))
    out = []
    for r in (1, 2, 3): out.append(f"чтение {r}: " + "  ".join(f"{v} {np.mean([close(v, r, i) for i in range(n)]):.0%}" for v in V))
    x3 = np.array([close(pick[i], 3, i) for i in range(n)]); g3 = np.array([close("G1", 3, i) for i in range(n)])
    rng = np.random.default_rng(0); B = rng.integers(0, n, (5000, n)); d = x3 - g3; bs = d[B].mean(1)
    out.append(f"выбрано: " + "  ".join(f"{v} {pick.count(v)}" for v in V) + f"; код отличается от G1 у {sum(p != 'G1' and J('cands.json')[p][i] != J('cands.json')['G1'][i] for i, p in enumerate(pick))}/{n}")
    out.append(f"чтение 3 (проверка): выбранный {x3.mean():.1%}, G1 {g3.mean():.1%}, выигрыш {d.mean() * 100:+.1f} п. п. [{np.percentile(bs, 2.5) * 100:+.1f} … {np.percentile(bs, 97.5) * 100:+.1f}]")
    out.append("стоп-кран (порог +8 п. п.): " + ("ПРОЙДЕН — дальше предложения" if d.mean() >= 0.08 else "СТОП — предложения не кодируются"))
    open(f"{D}/select.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out)); sys.exit()
SN = [x["s"] for x in J("sents.json")]; N = len(SN); SV = ["M0", "MG", "ML"]
num = lambda txt: {int(m[1]): m[2].strip() for x in txt.splitlines() if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
def put(d, files):
    os.makedirs(d, exist_ok=True)
    for k, v in files.items(): open(f"{d}/{k}", "w").write(v)
if cmd == "readers":
    C = J("sent_codes.json"); p = f"{S}/dec_sents.md"
    subprocess.run([f"{R0}/.venv/bin/python", f"{R0}/scripts/eval/prepare.py", "spec", "dec", "sents", p, "--braces"], check=True, capture_output=True)
    s = open(p).read(); db = s[:s.index("## Task")] + s[s.index("WORD BOUNDARIES"):] + "\n\n" + open(f"{P}/tasks/D0_read.md").read(); Ls = []
    for v in SV:
        for rep in range(2):
            o = list(range(N)); random.Random(5000 + len(Ls)).shuffle(o)
            for h in (o[:N // 2], o[N // 2:]): Ls.append({"enc": v, "order": h})
    random.Random(6).shuffle(Ls)
    for r, l in enumerate(Ls, 1): l["r"] = r; put(f"{S}/t{r}", {"spec.md": db, "list.md": "".join(f"{k + 1}. {C[l['enc']][i] or '(no code)'}\n" for k, i in enumerate(l["order"]))})
    json.dump(Ls, open(f"{D}/lists.json", "w")); print(len(Ls), "читателей"); sys.exit()
Ls = J("lists.json"); RD = {}
for l in Ls:
    a = num(open(f"{S}/t{l['r']}/answers.md").read())
    for k, i in enumerate(l["order"]): RD[(l["r"], i)] = a.get(k + 1, "—")
if cmd == "judges":
    keys = sorted(RD); random.Random(9).shuffle(keys); per = 120; PR = []
    for j in range(-(-len(keys) // per)):
        ch = keys[j * per:(j + 1) * per]
        put(f"{S}/u{j + 1}", {"spec.md": open(f"{P}/tasks/judge.md").read(), "pairs.md": "".join(f"{t + 1}. ORIGINAL: {SN[i]}\n   READING: {RD[(r, i)]}\n" for t, (r, i) in enumerate(ch))})
        PR += [{"j": j + 1, "t": t + 1, "r": r, "i": i} for t, (r, i) in enumerate(ch)]
    json.dump(PR, open(f"{D}/pairs.json", "w")); print(len(keys), "пар,", j + 1, "судей"); sys.exit()
PR = J("pairs.json"); sc = {}
for j in {p["j"] for p in PR}: sc[j] = {int(m[1]): int(m[2]) for x in open(f"{S}/u{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([0-3])", x))}
G = {(p["r"], p["i"]): sc[p["j"]][p["t"]] for p in PR}; assert len(G) == len(RD)
for sub in ("answers", "judge"): os.makedirs(f"{D}/{sub}", exist_ok=True)
for l in Ls: open(f"{D}/answers/t{l['r']}_{l['enc']}.md", "w").write(open(f"{S}/t{l['r']}/list.md").read() + "---\n" + open(f"{S}/t{l['r']}/answers.md").read())
for j in sc: open(f"{D}/judge/u{j}.md", "w").write(open(f"{S}/u{j}/pairs.md").read() + "---\n" + open(f"{S}/u{j}/scores.md").read())
M = {v: np.array([np.mean([G[(l["r"], i)] for l in Ls if l["enc"] == v and i in l["order"]]) for i in range(N)]) for v in SV}
rng = np.random.default_rng(0); B = rng.integers(0, N, (5000, N)); out = []
for v in SV: out.append(f"{v} среднее {M[v].mean():.2f}/3  ≥2: {np.mean(M[v] >= 2) * 100:.0f} %")
for a, b in (("ML", "M0"), ("MG", "M0"), ("ML", "MG")):
    d = M[a] - M[b]; bs = d[B].mean(1); out.append(f"{a} − {b}: {d.mean():+.2f} [{np.percentile(bs, 2.5):+.2f} … {np.percentile(bs, 97.5):+.2f}]")
C, L, CA, pick = J("sent_codes.json"), J("lemmas.json"), J("cands.json"), J("pick.json")
norm = lambda c: re.sub(r"\s+", " ", c.split("|")[0]).strip()  # корни слова словаря (без формы)
for v, src in (("MG", lambda i: CA["G1"][i]), ("ML", lambda i: CA[pick[i]][i])):
    used = [norm(src(i)) in C[v][n] for i, x in enumerate(L) for n in x["sents"]]
    out.append(f"{v}: корни слова словаря взяты дословно в {np.mean(used):.0%} вхождений")
out.append("сбоев (нет кода): " + "  ".join(f"{v} {sum(1 for c in C[v] if not c)}" for v in SV))
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
