# Векторы фраз из items.json (Numberbatch, как vocab.bin сайта: int8, единичная длина) → vecs.json.
#   .venv/bin/python data/eval/runs/phrases2/vecs.py
import gzip, json, os, numpy as np
D = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(f"{D}/../../../..")
need = {i["phrase"].replace(" ", "_"): i["phrase"] for i in json.load(open(f"{D}/items.json"))}; out = {}
with gzip.open(f"{REPO}/data/raw/numberbatch-en-19.08.txt.gz", "rt") as f:
    next(f)
    for l in f:
        k = l[:l.index(" ")]
        if k in need:
            x = np.round((x := np.array(l.split()[1:], dtype=float)) / np.linalg.norm(x) * 127)
            out[need[k]] = np.round(x / np.linalg.norm(x), 6).tolist()
assert len(out) == len(need), set(need.values()) - set(out)
json.dump(out, open(f"{D}/vecs.json", "w")); print(len(out), "векторов")
