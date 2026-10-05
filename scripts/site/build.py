"""Сборка данных сайта из roots.yaml и спецификаций: site/data/roots.json, site/data/examples.json, worker/prompts.js.

    python3 scripts/site/build.py          # записать
    python3 scripts/site/build.py --check  # проверить, что файлы не устарели
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
sys.path.insert(0, str(REPO / "scripts" / "eval"))
import spec  # noqa: E402
from prepare import build_spec  # noqa: E402
from validator import Validator, iter_codes  # noqa: E402

RUN = REPO / "data" / "eval" / "runs" / "holdout"


def roots_json():
    doc = spec.load()
    roots = []
    for r in doc["roots"]:
        ax = r.get("axis")
        roots.append({
            "name": r["name"],
            "axis": bool(ax),
            "neg": (ax or {}).get("neg", ""),
            "mid": (ax or {}).get("mid", ""),
            "pos": (ax or {}).get("pos", ""),
            "one_sided": bool(r.get("one_sided")),
            "ru": r.get("ru_axis") or r.get("ru_gloss") or "",
        })
    labels = [{"name": l["name"], "what": l["what"], "range": l.get("range"), "scale": l.get("scale", "")} for l in doc["labels"]]
    particles = [{"name": p["name"], "role": p["role"]} for p in doc["particles"]]
    return {"roots": roots, "labels": labels, "particles": particles, "counts": dict(zip(("roots", "with_axis", "without_axis"), (len(roots), sum(x["axis"] for x in roots), sum(not x["axis"] for x in roots))))}


def examples_json():
    """Пары из слепых тестов GRAIN и чисел (data/site/examples_words.json): слово, код, что прочитал декодер; верные и ошибочные."""
    return json.loads((REPO / "data" / "site" / "examples_words.json").read_text(encoding="utf8"))


def tips():
    """Сокращённые приёмы для сайта (дешевле полного encoding.md); правятся вручную в data/site/tips_short.md."""
    return (REPO / "data" / "site" / "tips_short.md").read_text(encoding="utf8")


def prompts_js():
    enc = build_spec("enc", "words") + "\n\n# Encoding tips (verified by blind tests)\n\n" + tips()
    dec = build_spec("dec", "words")
    return "// сгенерировано scripts/site/build.py, руками не править\nexport const ENC_SPEC = " + json.dumps(enc, ensure_ascii=False) + ";\nexport const DEC_SPEC = " + json.dumps(dec, ensure_ascii=False) + ";\n"


def outputs():
    return {
        REPO / "site" / "data" / "roots.json": json.dumps(roots_json(), ensure_ascii=False, indent=1) + "\n",
        REPO / "site" / "data" / "examples.json": json.dumps(examples_json(), ensure_ascii=False, indent=1) + "\n",
        REPO / "worker" / "prompts.js": prompts_js(),
    }


def main():
    out = outputs()
    if "--check" in sys.argv:
        bad = [str(p) for p, t in out.items() if not p.exists() or p.read_text(encoding="utf8") != t]
        print("устарели: " + ", ".join(bad) if bad else "в порядке")
        sys.exit(1 if bad else 0)
    for p, t in out.items():
        p.write_text(t, encoding="utf8")
        print("записано", p.relative_to(REPO))


if __name__ == "__main__":
    main()
