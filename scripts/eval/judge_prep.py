"""Лист для слепого судьи: перемешивает варианты (A, B, C …), чтобы судья не знал, какой где.

    python3 scripts/eval/judge_prep.py RUNDIR words --key items/key.json --variants full,abl [--seed 7]
    python3 scripts/eval/judge_prep.py RUNDIR sents --key ... --variants ...

Читает RUNDIR/dec_<вариант>_<кусок>.md и RUNDIR/codes_<вариант>_<кусок>.md, пишет
RUNDIR/judge_<вид>.md и RUNDIR/judge_map.json (id -> варианты в порядке A, B, …).
Перед этим печатает долю кодов с ошибками валидатора по вариантам.
"""
import argparse
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "mincode"))
from validator import Validator, iter_codes  # noqa: E402


def read_numbered(path):
    d = {}
    for line in open(path, encoding="utf8"):
        m = re.match(r"\s*(\d+)\.\s*(.*)", line)
        if m:
            d[int(m.group(1))] = m.group(2).strip()
    return d


def main():
    p = argparse.ArgumentParser()
    p.add_argument("run")
    p.add_argument("kind", choices=["words", "sents"])
    p.add_argument("--key", required=True)
    p.add_argument("--variants", required=True)
    p.add_argument("--seed", type=int, default=7)
    a = p.parse_args()
    run = Path(a.run)
    variants = a.variants.split(",")
    key = json.loads(Path(a.key).read_text(encoding="utf8"))
    chunks = [c for c in key if key[c] and c.startswith("w" if a.kind == "words" else "s")]
    rnd = random.Random(a.seed)
    val = Validator()
    for v in variants:
        n = bad = 0
        for c in chunks:
            for code in iter_codes(run / f"codes_{v}_{c}.md"):
                n += 1
                bad += any(i.level == "error" for i in val.check_any(code))
        print(f"{v}: кодов {n}, с ошибками валидатора {bad} ({100 * bad / max(n, 1):.0f}%)")
    mapping, rows = {}, []
    for c in chunks:
        dec = {v: read_numbered(run / f"dec_{v}_{c}.md") for v in variants}
        for i, orig in enumerate(key[c], 1):
            order = variants[:]
            rnd.shuffle(order)
            mapping[f"{c}-{i}"] = order
            rows.append(f"{c}-{i}\nORIG: {orig}\n" + "\n".join(f"{chr(65 + j)}: {dec[v].get(i, '')}" for j, v in enumerate(order)) + "\n")
    (run / f"judge_{a.kind}.md").write_text("\n".join(rows), encoding="utf8")
    old = json.loads((run / "judge_map.json").read_text()) if (run / "judge_map.json").exists() else {}
    old.update(mapping)
    (run / "judge_map.json").write_text(json.dumps(old), encoding="utf8")
    print(f"judge_{a.kind}.md: {len(mapping)} пунктов")


if __name__ == "__main__":
    main()
