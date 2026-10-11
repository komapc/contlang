"""Варианты словаря корней с центрами, привязанными к смыслу корня по спецификации (идея 4, README).
Ось a_r везде — из полюсов (A0) или обученная; меняется центр c_r:
  learned — как на сайте (обучение, уход от полюсов до cos 0,85);   poles — без обучения (C0, A0);
  name — c = unit(C0 + β·имя корня как слово);   spec — c = unit(C0 + β·центр слов спецификации: имя, «0 …» середина оси, «Bare root: …»);
  spec_only — c = центр слов спецификации;   learned_spec — обученный центр + β·слова спецификации, ось обученная.
Пишет dict_<вариант>.json: {C, A, hub} (hub — хабовость слов словаря сайта для этого словаря, как в build_math.py) и spec_words.json.
    .venv/bin/python data/eval/runs/anchor/dicts.py [β=1]"""
import json, re, sys
from pathlib import Path
import numpy as np
REPO = Path(__file__).resolve().parents[4]; OUT = Path(__file__).parent
sys.path.insert(0, str(REPO / "scripts")); sys.path.insert(0, str(REPO / "scripts" / "site"))
from lib_code import s15, unit  # noqa: E402
from build_math import hubness  # noqa: E402
import yaml
B = float(sys.argv[1]) if len(sys.argv) > 1 else 1.0
m = json.loads((REPO / "site/data/math.json").read_text()); names = m["names"]
D = np.load(REPO / "data/sparse_dict_learned.npz"); assert list(D["names"]) == names
roots = {r["name"]: r for r in yaml.safe_load(open(REPO / "roots.yaml"))["roots"]}
STOP = set("the a an of and or as in on to by is it its also e g eg etc thing one two plain ordinary mixed neutral itself means bare root".split())
def spec_words(n):
    r = roots.get(n, {}); ax = r.get("en_axis") or ""; out = [n.lower()]
    for pat in (r"(?:^|\.\.\.\s*)0\s+([^.]+?)\s*(?=\.\.\.|$)", r"[Bb]are root(?:\s+means)?:?\s*([^.]+)"):
        for t in re.findall(pat, ax): out += re.findall(r"[a-z]+", t.lower())
    if not ax and r.get("en_gloss"): out += re.findall(r"[a-z]+", r["en_gloss"].lower())
    return [w for w in dict.fromkeys(out) if w not in STOP and len(w) > 2 or w == n.lower()]
SW = {n: spec_words(n) for n in names}
vec = s15.load_subset({w for ws in SW.values() for w in ws})
SW = {n: [w for w in ws if w in vec] for n, ws in SW.items()}
json.dump(SW, open(OUT / "spec_words.json", "w"), indent=0)
sv = {n: unit(np.mean([unit(vec[w]) for w in ws], 0)) for n, ws in SW.items()}
nv = {n: unit(vec[n.lower()]) if n.lower() in vec else sv[n] for n in names}
S = np.stack([sv[n] for n in names]); Nm = np.stack([nv[n] for n in names])
V = {"learned": (D["C"], D["A"]), "poles": (D["C0"], D["A0"]),
     "name": (unit(D["C0"] + B * Nm), D["A0"]), "spec": (unit(D["C0"] + B * S), D["A0"]),
     "spec_only": (S, D["A0"]), "learned_spec": (unit(D["C"] + B * S), D["A"])}
X = np.frombuffer((REPO / "site/data/vocab.bin").read_bytes(), np.int8).reshape(-1, m["dim"]).astype(float); X = unit(X)
has = np.array(m["has_axis"])
for k, (C, A) in V.items():
    hub = np.round(hubness(X, C, A, has), 4).tolist()
    json.dump({"C": np.round(C, 5).tolist(), "A": np.round(A, 5).tolist(), "hub": hub}, open(OUT / f"dict_{k}.json", "w"))
    print(k, "cos центра с исходным:", f"{np.mean(np.sum(unit(C) * D['C0'], 1)):.2f}")
for n in names: print(n, SW[n])
