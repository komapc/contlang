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
    """Несколько настоящих пар из отложенного прогона `toki`: исходное предложение, код, раскодировано."""
    items = {}
    for c in ("s0", "s1"):
        for i, line in enumerate((RUN / f"items_h{c[1]}.txt" if (RUN / f"items_h{c[1]}.txt").exists() else RUN / f"items_{c}.txt").read_text(encoding="utf8").splitlines(), 1):
            m = re.match(r"\s*\d+\.\s*(.*\S)", line)
            if m:
                items[(c, i)] = m.group(1)
    v = Validator()
    out = []
    for c in ("s0", "s1"):
        codes = list(iter_codes(RUN / f"codes_toki_A_{c}.md"))
        decs = [re.sub(r"^\s*\d+\.\s*", "", l).strip() for l in (RUN / f"dec_toki_A_{c}.md").read_text(encoding="utf8").splitlines() if l.strip()]
        for i, code in enumerate(codes, 1):
            if i > len(decs) or any(x.level == "error" for x in v.check_toki(code)) or len(code) > 140 or len(items[(c, i)]) > 110 or "  " in items[(c, i)]:
                continue
            out.append({"en": items[(c, i)], "code": code, "decoded": decs[i - 1]})
    return out[:8]


def prompts_js():
    enc = build_spec("enc", "toki")
    dec = build_spec("dec", "toki")
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
