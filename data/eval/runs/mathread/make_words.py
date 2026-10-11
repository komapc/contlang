"""Набор слов для проверки математики: 200 общих слов словаря сайта, половина dev (подбор), половина test (не трогается до конца).
Берутся леммы (не словоформы), не служебные, из 3+ букв, есть в WordNet не только как имя собственное (instance), ни один смысл не пишется с заглавной (имена, сокращения), слово — начальная форма своей части речи (WordNet morphy).
Части речи по главной (в words.json — доля смыслов WordNet): 90 существительных, 50 глаголов, 40 прилагательных, 20 наречий.
Частотность — место в словаре (math.json идёт от частых к редким); берутся слова из первых 9000. Seed 5.
    .venv/bin/python data/eval/runs/mathread/make_words.py   → words.json: {"dev": [[слово, часть речи]], "test": [...]}"""
import json, random
from pathlib import Path
from nltk.corpus import wordnet as wn
REPO = Path(__file__).resolve().parents[4]
m = json.loads((REPO / "site/data/math.json").read_text()); meta = json.loads((REPO / "site/data/words.json").read_text())
stop = set(meta["stop"]); NEED = {"o": 90, "i": 50, "a": 40, "e": 20}
def ok(i, w):
    if i in stop or meta["lemma"][i] >= 0 or not w.isalpha() or len(w) < 3 or not meta["pos"][i]: return False
    ss = wn.synsets(w)
    if not ss or all(s.instance_hypernyms() for s in ss if s.pos() == "n") and all(s.pos() == "n" for s in ss): return False
    if any(l.name()[0].isupper() and l.name().lower() == w for s in ss for l in s.lemmas()): return False   # имена, сокращения (RBI)
    p = [int(c) for c in meta["pos"][i]]; f = "nvar"["oiae".index("oiae"[p.index(max(p))])]
    return wn.morphy(w, f) == w   # начальная форма (miners, rescuers — нет)
pool = {f: [] for f in NEED}
for i, w in enumerate(m["words"][:9000]):
    if ok(i, w):
        p = [int(c) for c in meta["pos"][i]]; pool["oiae"[p.index(max(p))]].append(w)
rnd = random.Random(5); out = {"dev": [], "test": []}
for f, n in NEED.items():
    ws = rnd.sample(pool[f], n)
    out["dev"] += [[w, f] for w in ws[: n // 2]]; out["test"] += [[w, f] for w in ws[n // 2:]]
for k in out: rnd.shuffle(out[k])
(Path(__file__).parent / "words.json").write_text(json.dumps(out, indent=0))
print({f: len(v) for f, v in pool.items()}); print("dev:", " ".join(w for w, _ in out["dev"]))
