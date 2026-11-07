# Кандидаты (dec.md): двусловные записи Numberbatch, оба слова — среди 5000 частых слов сайта, фразы нет среди лемм WordNet
# (свободное сочетание, не устойчивое; устойчивые — ../phrases). Для имён — есть ли в WordNet родственный глагол (decision → decide).
#   .venv/bin/python data/eval/runs/phrases2/cand.py   → cand.json
import gzip, json, os, nltk
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../..")
nltk.data.path.insert(0, f"{REPO}/data/raw/nltk")
from nltk.corpus import wordnet as wn
top = set(json.load(open(f"{REPO}/site/data/math.json"))["words"][:5000])
out = []
with gzip.open(f"{REPO}/data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
    next(f)
    for l in f:
        k = l[:l.index(" ")]
        if k.count("_") != 1: continue
        a, b = k.split("_")
        if a in top and b in top and a != b and not wn.synsets(k): out.append(k)
# имя действия (первый смысл — действие, событие, сообщение, мысль, чувство, состояние, процесс) и его глагол: decision → decide;
# computer → compute не годится (первый смысл — артефакт)
ACT = {"noun.act", "noun.event", "noun.communication", "noun.cognition", "noun.feeling", "noun.state", "noun.process"}
def verb_of(n):
    ss = wn.synsets(n, "n")
    if not ss or ss[0].lexname() not in ACT: return []
    return sorted({d.name() for s in ss for le in s.lemmas() if le.name() == n for d in le.derivationally_related_forms() if d.synset().pos() == "v" and "_" not in d.name()})
# относительное прилагательное (political ← politics: есть pertainym) — не качество и не степень
def relational(w):
    return any(le.pertainyms() for s in wn.synsets(w) if s.pos() in "as" for le in s.lemmas() if le.name() == w)
words = {w for k in out for w in k.split("_")}
json.dump({"phrases": out, "verb_of": {w: v for w in words if (v := verb_of(w))}, "relational": sorted(w for w in words if relational(w))}, open(f"{D}/cand.json", "w"))
print(len(out), "фраз")
