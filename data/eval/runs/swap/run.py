# Слепой тест замены +MAKE, PUBLIC, LAW −CARE, HAPPEN, пороги — dec.md.  Коды: remove.json (O), v2/CARE_HAPPEN.json (N).
#   run.py readers SC → spec_new.md, items.json, lists.json, SC/rK/{spec,codes}.md;  pairs SC;  merge SC;  score SC → result.txt, table.md
import json, os, re, sys, random, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); LP = f"{D}/../reader/labels.json"; cmd, S = sys.argv[1], sys.argv[2]
NEW = ["- MAKE: -5 destroy, wreck, ruin … +5 make, build, create, produce",
       "- PUBLIC: -5 private, secret, personal … +5 public, common, civic, national",
       "- LAW: -5 illegal, criminal, forbidden … +5 legal, legitimate, valid, permitted"]
sub = lambda s, a, b: (lambda r: r[0] if r[1] == 1 else sys.exit(f"нет: {a}"))(re.subn(a, b, s, count=1, flags=re.M))
if cmd == "readers":
    O = json.load(open(f"{D}/remove.json")); N = json.load(open(f"{D}/v2/CARE_HAPPEN.json"))
    ws = sorted(w for w in O if w in N and O[w]["code"]); ch = [w for w in ws if N[w]["code"] != O[w]["code"]]; un = [w for w in ws if N[w]["code"] == O[w]["code"]]
    random.seed(20261014); C = sorted(random.sample(ch, 180)); U = sorted(random.sample(un, 100))
    its = [{"w": w, "set": "C", "O": O[w]["code"], "N": N[w]["code"]} for w in C] + [{"w": w, "set": "U", "O": O[w]["code"], "N": O[w]["code"]} for w in U]
    json.dump(its, open(f"{D}/items.json", "w"), indent=0); print("C", len(ch), "→", len(C), "U", len(un), "→", len(U))
    s0 = os.popen(f"cd {D}/../../../../worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.DEC_SPEC))'").read()
    sn = sub(s0, r"^- HAPPEN: .*\n", ""); sn = sub(sn, r"^- CARE: .*$", "\n".join(NEW)); sn = sub(sn, r"^## Roots \(45\)$", "## Roots (46)")
    sn = sn.replace("Use ONLY the 45 roots", "Use ONLY the 46 roots")
    sn = sub(sn, r", `HAPPEN \| o agent` = cause\.", ".")
    sn = sub(sn, r"`HAPPEN \| o result` = consequence, ", "")
    sn = sub(sn, r" `CARE` \(-5 careless, lazy \.\.\. \+5 careful, diligent; toward a task; carefully = `CARE\(=\+3\) \| e`\),", "")
    sn = sub(sn, r", cause `HAPPEN \| o agent`; `result` consequence `HAPPEN \| o result`;", "; `result` idea `THINK | o result`;")
    bad = [l for l in sn.splitlines() if re.search(r"\b(CARE|HAPPEN)\b", l)]; assert not bad, bad
    open(f"{D}/spec_new.md", "w").write(sn); L = []
    for st, var, key, sp in (("C", "O", "O", s0), ("C", "N", "N", sn), ("U", "O", "O", s0), ("U", "N", "N", sn)):
        xs = [o for o in its if o["set"] == st]; random.shuffle(xs); n = -(-len(xs) // 50); per = -(-len(xs) // n)
        for c in range(n):
            r = len(L) + 1; chn = xs[c * per:(c + 1) * per]; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(sp)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {o[key]}\n" for i, o in enumerate(chn))); L.append({"r": r, "set": st, "var": var, "words": [o["w"] for o in chn]})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей", [len(l["words"]) for l in L]); sys.exit()
its = json.load(open(f"{D}/items.json")); lists = json.load(open(f"{D}/lists.json")); A = {}
for l in lists:
    a = {int(m[1]): m[2].split("|")[0].strip().strip("*`").lower() for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    A.update({(l["set"], l["var"], w): a.get(i + 1, "—") for i, w in enumerate(l["words"])})
L = json.load(open(LP))
if cmd == "pairs":
    keys = sorted({(w, a) for (_, _, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]; os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/r{l['r']}_{l['set']}{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
s = {k: L[f"{k[2]}\t{a}"] for k, a in A.items()}; out = []
def cmp(st, ws, name):
    d = np.array([(s[(st, "N", w)] == 2) - (s[(st, "O", w)] == 2) for w in ws], float); rng = np.random.default_rng(0)
    lo, hi = np.percentile([rng.choice(d, len(d)).mean() for _ in range(5000)], [2.5, 97.5]); f = lambda v: np.mean([s[(st, v, w)] == 2 for w in ws])
    out.append(f"{name:34s} O {f('O'):4.0%}  N {f('N'):4.0%}  разница {d.mean():+.1%} [{lo:+.1%} … {hi:+.1%}]  (n {len(ws)})")
I = {o["w"]: o for o in its}; C = [o["w"] for o in its if o["set"] == "C"]; U = [o["w"] for o in its if o["set"] == "U"]
has = lambda c, rs: re.search(r"\b(" + "|".join(rs) + r")\b", c)
cmp("C", C, "C: изменённые коды (N − O)"); cmp("U", U, "U: тот же код, спецификация new − old")
cmp("C", [w for w in C if has(I[w]["O"], ["CARE", "HAPPEN"])], "  C: в O был CARE или HAPPEN")
cmp("C", [w for w in C if has(I[w]["N"], ["MAKE", "PUBLIC", "LAW"])], "  C: в N есть новый корень")
cmp("C", [w for w in C if not has(I[w]["O"], ["CARE", "HAPPEN"]) and not has(I[w]["N"], ["MAKE", "PUBLIC", "LAW"])], "  C: ни то, ни другое")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
g = lambda st, v, w: f"{A[(st, v, w)]} ({s[(st, v, w)]})"
md = ["## C: изменённые коды", "", "| слово | O: код | → | N: код | → |", "|---|---|---|---|---|"] + [f"| {w} | `{I[w]['O']}` | {g('C', 'O', w)} | `{I[w]['N']}` | {g('C', 'N', w)} |" for w in C]
md += ["", "## U: тот же код", "", "| слово | код | old → | new → |", "|---|---|---|---|"] + [f"| {w} | `{I[w]['O']}` | {g('U', 'O', w)} | {g('U', 'N', w)} |" for w in U]
open(f"{D}/table.md", "w").write("\n".join(md) + "\n")
