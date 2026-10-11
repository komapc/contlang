"""Идея 5, шаг 1: значение, род и отличие по WordNet для слов dev/test (../mathread/words.json) → senses.json.
Значение — первый синсет своей части речи (WordNet упорядочен по частоте в SemCor; выбор по близости к вектору слова давал vehicle → fomite, suit → lawsuit).
Род — леммы гиперонима (у прилагательных и наречий гиперонимов нет: род пустой, код как раньше).
Отличие — слово толкования: после «used for / made of / resembling …» (связка FOR / FROM / LIKE), иначе любое (PI); само слово выбирает кодер (senses.js).
    .venv/bin/python data/eval/runs/genus/senses.py"""
import json, re
from pathlib import Path
import numpy as np
from nltk.corpus import wordnet as wn
REPO = Path(__file__).resolve().parents[4]; OUT = Path(__file__).parent
m = json.loads((REPO / "site/data/math.json").read_text()); idx = {w: i for i, w in enumerate(m["words"])}
X = np.frombuffer((REPO / "site/data/vocab.bin").read_bytes(), np.int8).reshape(-1, m["dim"]).astype(float); X /= np.linalg.norm(X, axis=1, keepdims=True) + 1e-9
STOP = set("a an the of to in on and or for with by from as at is are be that which who whose this its it their his her one some any etc usually especially often something someone used make made being having".split())
W = json.loads((REPO / "data/eval/runs/mathread/words.json").read_text())
words = lambda txt: [t for t in re.findall(r"[a-z]+", txt.lower().replace("_", " "))]
def vec(ws):
    v = [X[idx[w]] for w in ws if w in idx]; return np.mean(v, 0) if v else None
LINKS = [("FROM", r"\b(?:made (?:of|from|with)|consisting (?:of|mostly of)|derived from|composed of|from the|of the flesh of)\s+"),
         ("FOR", r"\b(?:used (?:for|to|in|as)|designed (?:for|to)|intended (?:for|to)|reared for|for (?=\w+ing\b))\s*"),
         ("LIKE", r"\b(?:resembling|like (?:a|an|the)?|similar to|shaped like)\s*")]
out = {}
for part in ("dev", "test"):
    for w, f in W[part]:
        pos = {"o": "n", "i": "v", "a": "a", "e": "r"}[f]
        ss = [s for s in wn.synsets(w, pos) if s.pos() == pos or (pos == "a" and s.pos() == "s")][:4] or wn.synsets(w)[:1]
        x = X[idx[w]] if w in idx else None; best = None
        for s in ss:
            lem = [t for l in s.lemma_names() for t in words(l) if t != w]; gl = [t for t in words(s.definition()) if t not in STOP and t != w]
            v = vec(lem + gl); c = float(v @ x / np.linalg.norm(v)) if v is not None and x is not None else -1
            if best is None: best = (c, s, lem, gl)   # первое значение; cos — для справки
        c, s, lem, gl = best; hyp = s.hypernyms()[:1]
        genus = [t for h in hyp for l in h.lemma_names()[:3] for t in words(l)]
        link, after = "PI", []
        d = s.definition().lower()
        for L, pat in LINKS:
            mm = re.search(pat, d)
            if mm: link, after = L, [t for t in words(d[mm.end():]) if t not in STOP and t != w][:3]; break
        out[w] = {"form": f, "set": part, "synset": s.name(), "def": s.definition(), "cos": round(c, 3), "lemmas": lem, "gloss": gl,
                  "genus_synset": hyp[0].name() if hyp else None, "genus": genus, "link": link, "after": after}
json.dump(out, open(OUT / "senses.json", "w"), indent=1, ensure_ascii=False)
dv = [v for v in out.values() if v["set"] == "dev"]
print(f"слов {len(out)}; dev {len(dv)}: с родом {sum(1 for v in dv if v['genus'])}, связки", {L: sum(v['link'] == L for v in dv) for L in ('FROM', 'FOR', 'LIKE', 'PI')})
for w in ["suit", "beef", "vehicle", "supermarket", "breakfast", "tank", "city", "repair", "pump", "sentence", "current", "vice"]:
    v = out[w]; print(f"{w}: {v['synset']} — {v['def'][:70]} | род {v['genus_synset']} {v['genus']} | {v['link']} {v['after']}")
