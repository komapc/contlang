# 1000 слов, два кодера: math = кодер сайта (site.js → site_codes.json), llm = Haiku с ENC_SPEC сайта (worker/prompts.js).
# Слепые читатели Haiku с DEC_SPEC, первый ответ оценивает слепой судья Haiku (2 близко / 1 рядом / 0 мимо).
#   run.py writers SC   → SC/wK (часть речи — по форме кода сайта, толкование — первое значение WordNet)
#   run.py readers SC   → llm_codes.json; SC/rK/{spec.md,codes.md}, lists.json
#   run.py pairs SC     → SC/jK/pairs.md;  run.py merge SC → ../reader/labels.json;  run.py score SC → result.txt, worst.md
import json, os, re, sys, random
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__)); R = f"{D}/../../../.."; LP = f"{D}/../reader/labels.json"
cmd, S = sys.argv[1], sys.argv[2]; W = json.load(open(f"{D}/words.json")); site = json.load(open(f"{D}/site_codes.json"))
spec = lambda k: os.popen(f"cd {R}/worker && node -e 'import(\"./prompts.js\").then(m=>process.stdout.write(m.{k}))'").read()
POS = {"o": ("n", "noun"), "i": ("v", "verb"), "a": ("a", "adjective"), "e": ("r", "adverb")}
def pos(w):
    m = re.search(r"\|\s*([oiae])\b", site[w] or ""); return POS[m[1] if m else "o"]
def gloss(w):
    p, _ = pos(w); ss = wn.synsets(w, p) or (wn.synsets(w, "s") if p == "a" else []) or wn.synsets(w); return ss[0].definition()
T = """# Task: write min-co codes

spec.md explains how min-co words are written. list.md gives numbered English words with their part of speech and intended sense.
For each word write the code that lets a reader who knows only spec.md guess the word (or a word of the same meaning) most surely.

Write answers.md in ONE single write with exactly one line per word, same numbering:
N. code
Check that answers.md has as many lines as list.md, then reply "done".
"""
if cmd == "writers":
    es = spec("ENC_SPEC"); its = [{"w": w, "pos": pos(w)[1], "gloss": gloss(w)} for w in W]; json.dump(its, open(f"{D}/items.json", "w"), indent=0)
    for k in range(20):
        d = f"{S}/w{k + 1}"; os.makedirs(d, exist_ok=True); open(f"{d}/spec.md", "w").write(es); open(f"{d}/task.md", "w").write(T)
        open(f"{d}/list.md", "w").write("".join(f"{i + 1}. {o['w']} ({o['pos']}) — {o['gloss']}\n" for i, o in enumerate(its[k * 50:(k + 1) * 50])))
    sys.exit()
if cmd == "readers":
    llm = {}
    for k in range(20):
        a = {int(m[1]): m[2].strip().strip("`") for x in open(f"{S}/w{k + 1}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
        for i, w in enumerate(W[k * 50:(k + 1) * 50]): llm[w] = a.get(i + 1)
    print("нет кода llm:", [w for w in W if not llm[w]], "нет кода math:", [w for w in W if not site[w]])
    json.dump(llm, open(f"{D}/llm_codes.json", "w"), indent=0); ds = spec("DEC_SPEC"); random.seed(7); L = []
    for v, C in (("math", site), ("llm", llm)):
        ws = [w for w in W if C[w]]; random.shuffle(ws)
        for c in range(0, len(ws), 50):
            r = len(L) + 1; d = f"{S}/r{r}"; os.makedirs(d, exist_ok=True); ch = ws[c:c + 50]; open(f"{d}/spec.md", "w").write(ds)
            open(f"{d}/codes.md", "w").write("".join(f"{i + 1}. {C[w]}\n" for i, w in enumerate(ch))); L.append({"r": r, "var": v, "words": ch})
    json.dump(L, open(f"{D}/lists.json", "w")); print(len(L), "читателей"); sys.exit()
L = json.load(open(LP)); lists = json.load(open(f"{D}/lists.json")); A = {}  # (var, word) → [best, alt...]
for l in lists:
    a = {int(m[1]): [t.strip().lower() for t in m[2].split("|")] for x in open(f"{S}/r{l['r']}/answers.md") if (m := re.match(r"\s*(\d+)\.\s*(.+)", x))}
    for i, w in enumerate(l["words"]): A[(l["var"], w)] = a.get(i + 1) or ["—"]
if cmd == "pairs":
    keys = sorted({(w, a[0]) for (_, w), a in A.items()} - {tuple(k.split("\t")) for k in L}); n = max(1, -(-len(keys) // 160)); per = -(-len(keys) // n); P = []
    for j in range(n):
        ch = keys[j * per:(j + 1) * per]; d = f"{S}/j{j + 1}"; os.makedirs(d, exist_ok=True)
        open(f"{d}/pairs.md", "w").write("".join(f"{t + 1}. {w} — {a}\n" for t, (w, a) in enumerate(ch))); P += [{"j": j + 1, "t": t + 1, "w": w, "a": a} for t, (w, a) in enumerate(ch)]
    json.dump(P, open(f"{S}/pairs.json", "w")); print(len(keys), "пар,", n, "судей"); sys.exit()
if cmd == "merge":
    P = json.load(open(f"{S}/pairs.json"))
    sc = {(j, int(m[1])): int(m[2]) for j in {p["j"] for p in P} for l in open(f"{S}/j{j}/scores.md") if (m := re.match(r"\s*(\d+)\.\s*([012])", l))}
    miss = [p for p in P if (p["j"], p["t"]) not in sc]; assert not miss, miss[:3]
    os.makedirs(f"{D}/judge", exist_ok=True)
    for j in {p["j"] for p in P}: open(f"{D}/judge/j{j}.md", "w").write(open(f"{S}/j{j}/pairs.md").read() + "---\n" + open(f"{S}/j{j}/scores.md").read())
    for p in P: L[f"{p['w']}\t{p['a']}"] = sc[(p["j"], p["t"])]
    json.dump(L, open(LP, "w")); print("добавлено", len(P)); sys.exit()
# score
os.makedirs(f"{D}/answers", exist_ok=True)
for l in lists: open(f"{D}/answers/r{l['r']}_{l['var']}.md", "w").write(open(f"{S}/r{l['r']}/answers.md").read())
llm = json.load(open(f"{D}/llm_codes.json")); its = {o["w"]: o for o in json.load(open(f"{D}/items.json"))}
s = {k: L[f"{k[1]}\t{a[0]}"] for k, a in A.items()}; out = []
for v in ("math", "llm"):
    x = [s[(v, w)] for w in W if (v, w) in s]
    out.append(f"{v:5s} n {len(x)}  близко {x.count(2) / len(x):4.0%}  рядом {x.count(1) / len(x):4.0%}  мимо {x.count(0) / len(x):4.0%}")
both = [w for w in W if ("math", w) in s and ("llm", w) in s]
for a, b in ((2, 2), (0, 0)): out.append(f"оба {'близко' if a == 2 else 'мимо'}: {sum(s[('math', w)] == a and s[('llm', w)] == b for w in both)}")
out.append(f"math лучше llm: {sum(s[('math', w)] > s[('llm', w)] for w in both)}, хуже: {sum(s[('math', w)] < s[('llm', w)] for w in both)}")
for p in ("noun", "verb", "adjective", "adverb"):
    ws = [w for w in both if its[w]["pos"] == p]
    if ws: out.append(f"  {p:9s} n {len(ws):3d}  math {sum(s[('math', w)] == 2 for w in ws) / len(ws):4.0%}  llm {sum(s[('llm', w)] == 2 for w in ws) / len(ws):4.0%}")
open(f"{D}/result.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
# худшие: сумма оценок обоих кодеров, затем частота (выше в словаре — обиднее)
rank = {w: i for i, w in enumerate(json.load(open(f"{R}/site/data/math.json"))["words"])}
worst = sorted(both, key=lambda w: (s[("math", w)] + s[("llm", w)], rank.get(w, 1e9)))
md = ["| # | слово | math: код → ответ | llm: код → ответ |", "|---|---|---|---|"]
for i, w in enumerate(worst[:40]):
    md.append(f"| {i + 1} | **{w}** ({its[w]['pos']}) | `{site[w]}` → {A[('math', w)][0]} ({s[('math', w)]}) | `{llm[w]}` → {A[('llm', w)][0]} ({s[('llm', w)]}) |")
open(f"{D}/worst.md", "w").write("\n".join(md) + "\n")
