"""Какие значения осей кодировщики-модели реально пишут (min-co 1): доля каждого значения −5…+5 по корням.

    .venv/bin/python v2/values.py

Источники — коды моделей из прогонов (не математика сайта): big1000 (Haiku), lex (Sonnet), pipe и mini (предложения),
lexs/cands.json (gpt-5-mini и Sonnet; файл лежит в ветке eval-lexs, берётся оттуда через git, если его нет в рабочем дереве).
"""
import collections
import glob
import re
import subprocess
from pathlib import Path

import yaml

R = Path(__file__).resolve().parent.parent
roots = {r["name"] for r in yaml.safe_load(open(R / "roots.yaml"))["roots"]}
runs = R / "data/eval/runs"
files = [runs / "big1000/llm_codes.json", runs / "lex/codes.json"]
files += [Path(p) for p in glob.glob(str(runs / "pipe/**/*.json"), recursive=True) + glob.glob(str(runs / "mini*/codes.json"))]
texts = [f.read_text() for f in files if f.exists()]
lexs = runs / "lexs/cands.json"
if lexs.exists():
    texts.append(lexs.read_text())
else:
    r = subprocess.run(["git", "-C", str(R), "show", "eval-lexs:data/eval/runs/lexs/cands.json"], capture_output=True, text=True)
    if r.returncode == 0:
        texts.append(r.stdout)

pat = re.compile(r"\b([A-Z]{2,})\(=([+-]?\d+)\)")
C = collections.defaultdict(collections.Counter)
for s in texts:
    for r, v in pat.findall(s):
        if r in roots:
            C[r][int(v)] += 1
allv = collections.Counter()
for r in C:
    allv.update(C[r])
n = sum(allv.values())
print(f"источников {len(texts)}, значений {n}")
print("значение  " + " ".join(f"{v:+4d}" for v in range(-5, 6)))
print("все, %    " + " ".join(f"{allv[v] * 100 / n:4.0f}" for v in range(-5, 6)))
for r in sorted(C, key=lambda r: -sum(C[r].values())):
    k = sum(C[r].values())
    print(f"{r:8s}{k:5d} " + " ".join(f"{C[r][v] * 100 // k:4d}" for v in range(-5, 6)))
