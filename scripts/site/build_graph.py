"""Связи ConceptNet между словами словаря сайта: data/raw/conceptnet/graph.json (для чтения пар PI / FOR векторами).

На сайт не идёт: 7,6 МБ, а пары улучшает слабо (scripts/site/eval_math.js --graph, docs/math.md).

Источник — conceptnet-assertions-5.7.0.csv.gz в data/raw/conceptnet (s3.amazonaws.com/conceptnet/downloads/2019/edges/).
Берутся английские рёбра с отношениями из REL. Понятие-фраза (open_lock) раскладывается на слова словаря
(open, lock), служебные слова отбрасываются; словоформы сводятся к лемме, как в words.json.

graph.json — {"rel": [имена отношений], "edges": [[a, b, r, w], ...]} — a, b — номера слов math.json, r — номер отношения,
w — вес ConceptNet, округлённый до 0,1, для пары слов и отношения берётся наибольший. Ребро направленное: a —r→ b
(key —UsedFor→ lock, nest —AtLocation→ tree). RelatedTo и прочие симметричные хранятся один раз.

Запуск локально:
    .venv/bin/python scripts/site/build_graph.py
"""
import csv
import gzip
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
SRC = REPO / "data" / "raw" / "conceptnet" / "conceptnet-assertions-5.7.0.csv.gz"
OUT = REPO / "site" / "data"
REL = ["UsedFor", "AtLocation", "PartOf", "HasA", "MadeOf", "CapableOf", "IsA", "ReceivesAction", "RelatedTo"]
SYM = {"RelatedTo"}
MAXW = 2  # фраза длиннее двух слов словаря — не связь слов, а описание; не берём


def main():
    m = json.loads((OUT / "math.json").read_text(encoding="utf8"))
    meta = json.loads((OUT / "words.json").read_text(encoding="utf8"))
    words, stop = m["words"], set(meta["stop"])
    index = {w: i for i, w in enumerate(words)}
    lemma = lambda i: meta["lemma"][i] if meta["lemma"][i] >= 0 else i  # noqa: E731
    rid = {r: k for k, r in enumerate(REL)}

    def terms(uri):
        # /c/en/open_lock/n/... → номера лемм слов словаря
        p = uri.split("/")
        if len(p) < 4 or p[2] != "en":
            return []
        ws = [index.get(t) for t in p[3].split("_")]
        ws = [lemma(i) for i in ws if i is not None and i not in stop]
        return ws if 0 < len(ws) <= MAXW else []

    best = {}
    csv.field_size_limit(sys.maxsize)
    with gzip.open(SRC, "rt", encoding="utf8") as f:
        for row in csv.reader(f, delimiter="\t"):
            r = row[1][3:]
            if r not in rid or not row[2].startswith("/c/en/") or not row[3].startswith("/c/en/"):
                continue
            A, B = terms(row[2]), terms(row[3])
            if not A or not B:
                continue
            w = json.loads(row[4]).get("weight", 1.0)
            for a in A:
                for b in B:
                    if a == b:
                        continue
                    if r in SYM and a > b:
                        a, b = b, a
                    k = (a, b, rid[r])
                    if w > best.get(k, 0):
                        best[k] = w
    edges = [[a, b, r, round(w, 1)] for (a, b, r), w in sorted(best.items())]
    (SRC.parent / "graph.json").write_text(json.dumps({"rel": REL, "edges": edges}, separators=(",", ":")), encoding="utf8")
    from collections import Counter
    c = Counter(REL[e[2]] for e in edges)
    print(f"рёбер {len(edges)}, graph.json {(SRC.parent / 'graph.json').stat().st_size // 1024} КБ; " + ", ".join(f"{r} {c[r]}" for r in REL))


if __name__ == "__main__":
    main()
