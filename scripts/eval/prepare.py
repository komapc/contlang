"""Подготовка слепого теста: спецификации и фрагменты списка пунктов.

    # спецификация кодировщика или декодера из шаблона и roots.yaml
    python3 scripts/eval/prepare.py spec enc words OUT.md [--drop SIDE,HEAT] [--axis 'SEE=visibility: -5 hidden ... +5 bright']
    python3 scripts/eval/prepare.py spec dec sents OUT.md

    # пункты: файл со строками «слово — пояснение» (или JSON-список предложений) -> items_<имя><N>.txt и key.json
    python3 scripts/eval/prepare.py items LIST.txt OUTDIR --prefix w --chunk 46

Дальше агенты (кодировщики по `enc`-спецификации, декодеры по `dec`-спецификации) пишут
codes_<вариант>_<кусок>.md и dec_<вариант>_<кусок>.md; см. scripts/eval/README.md.
"""
import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
import spec  # noqa: E402

TEMPLATES = REPO / "data" / "eval" / "templates"


CLAUSE_RULE = {
    "enc": "CLAUSES: independent clauses of a long sentence are separated by `;` (each clause has its own words and particles); `[ ... ]` is only for a clause that is an argument or is nested inside another. EVERY word, including a head noun before PI or E, carries its own `| FORM` (at least the part of speech), so a word is at most 3 roots plus ABSTRACT; never run two words together without `|`.",
    "dec": "CLAUSES: `;` separates independent clauses of a long sentence; `[ ... ]` marks a nested or argument clause. Every word has its own `| FORM`.",
}


def build_spec(kind, task, drop=(), axes=None, clause_rule=True):
    doc = spec.load()
    roots = [r for r in doc["roots"] if r["name"] not in set(drop)]
    for name, text in (axes or {}).items():
        for r in roots:
            if r["name"] == name:
                r["en_axis"] = text
                r["axis"] = r.get("axis") or {"neg": "", "mid": "", "pos": ""}
    items = []
    for r in roots:
        items.append(f"{r['name']} ({r['en_gloss']})" if r.get("en_gloss") else r["name"])
    roots_par = f"{len(roots)} roots (NSM-like primitives): " + ", ".join(items) + "."
    axes_lines = "\n".join(f"- {r['name']}: {r['en_axis']}" for r in roots if r.get("axis") and r.get("en_axis"))
    text = (TEMPLATES / f"{kind}_{task}.md").read_text(encoding="utf8")
    text = text.replace("{{CLAUSE_RULE}}\n", CLAUSE_RULE[kind] + "\n" if clause_rule else "")
    return text.replace("{{ROOTS}}", roots_par).replace("{{AXES}}", axes_lines).replace("{{N_ROOTS}}", str(len(roots)))


def cmd_spec(a):
    axes = dict(x.split("=", 1) for x in a.axis)
    drop = [x for x in a.drop.split(",") if x]
    unknown = set(drop) - set(spec.root_names())
    if unknown:
        raise SystemExit(f"нет таких корней: {sorted(unknown)}")
    Path(a.out).write_text(build_spec(a.kind, a.task, drop, axes, not a.no_clause_rule), encoding="utf8")
    print(f"записано {a.out}")


def cmd_items(a):
    src = Path(a.list)
    if src.suffix == ".json":
        raw = json.loads(src.read_text(encoding="utf8"))
        entries = [x[1] if isinstance(x, list) else x for x in raw]
    else:
        entries = [re.sub(r"^\d+\.\s*", "", l.strip()) for l in src.read_text(encoding="utf8").splitlines() if l.strip()]
    out = Path(a.outdir)
    out.mkdir(parents=True, exist_ok=True)
    key = {}
    for n in range(0, len(entries), a.chunk):
        name = f"{a.prefix}{n // a.chunk}"
        chunk = entries[n:n + a.chunk]
        (out / f"items_{name}.txt").write_text("\n".join(f"{j + 1}. {x}" for j, x in enumerate(chunk)) + "\n", encoding="utf8")
        key[name] = chunk
    (out / "key.json").write_text(json.dumps(key, ensure_ascii=False, indent=1), encoding="utf8")
    print(f"{len(entries)} пунктов, кусков {len(key)}")


def main():
    p = argparse.ArgumentParser()
    sp = p.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("spec")
    s.add_argument("kind", choices=["enc", "dec"])
    s.add_argument("task", choices=["words", "sents"])
    s.add_argument("out")
    s.add_argument("--drop", default="")
    s.add_argument("--no-clause-rule", action="store_true", help="спецификация предложений без правила про `;` и форму у каждого слова (для сравнения)")
    s.add_argument("--axis", action="append", default=[], help="ROOT=английское описание оси")
    s.set_defaults(f=cmd_spec)
    i = sp.add_parser("items")
    i.add_argument("list")
    i.add_argument("outdir")
    i.add_argument("--prefix", default="w")
    i.add_argument("--chunk", type=int, default=46)
    i.set_defaults(f=cmd_items)
    a = p.parse_args()
    a.f(a)


if __name__ == "__main__":
    main()
