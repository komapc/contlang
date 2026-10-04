"""Генерация таблиц и фрагментов из roots.yaml.

    python3 scripts/mincode/gen.py          # записать
    python3 scripts/mincode/gen.py --check  # выйти с ошибкой, если файлы разошлись с roots.yaml

Генерируются: docs/tables.md целиком, два блока в docs/lexicon.md между
<!-- BEGIN generated:NAME --> и <!-- END generated:NAME -->, строка roots=set(...)
в data/translation_test/republic_validate.py. Спецификации для кодировщика и
декодера собирает scripts/eval/prepare.py из шаблонов и тех же данных.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import spec  # noqa: E402

REPO = spec.REPO
TABLES = REPO / "docs" / "tables.md"
LEXICON = REPO / "docs" / "lexicon.md"
VALIDATE = REPO / "data" / "translation_test" / "republic_validate.py"


def esc(s):
    return s


def tables_md(doc):
    total, na, nn = spec.counts(doc)
    L = []
    L.append("# Сводные таблицы: корни, оси, метки\n")
    L.append("> Файл сгенерирован из [`roots.yaml`](../roots.yaml) (`python3 scripts/mincode/gen.py`); руками не править.\n")
    L.append("Краткий обзор текущего состояния. Источники правды: `roots.yaml` (корни и оси), [syntax.md](syntax.md) (метки и частицы), [model.md](model.md) (модель). Здесь только сводка; при расхождении верны они.\n")
    L.append(f"## Корни с осью ({na})\n")
    L.append("Ось — шкала −5 … +5; ось не написана — значение не указано, `(=0)` — явная середина.\n")
    L.append("| корень | −5 | 0 | +5 |")
    L.append("| :-- | :-- | :-- | :-- |")
    for r in spec.axis_roots(doc):
        a = r["axis"]
        L.append(f"| {r['name']} | {a['neg']} | {a['mid']} | {a['pos']} |".replace("|  |", "| |"))
    L.append("")
    L.append(f"## Корни без оси ({nn})\n")
    L.append("| корень | значение |")
    L.append("| :-- | :-- |")
    for r in spec.noaxis_roots(doc):
        L.append(f"| {r['name']} | {r['ru_gloss']} |")
    L.append("")
    L.append("## Форма слова: после `|`\n")
    L.append("Часть речи (2 бита): " + ", ".join(f"`{p['name']}` {p['what']}" for p in doc["pos"]) + ".\n")
    L.append("Метки (не корни, в лимит трёх корней не входят; метки ставятся один раз на главном слове группы):\n")
    L.append("| метка | что | шкала |")
    L.append("| :-- | :-- | :-- |")
    for m in doc["labels"]:
        L.append(f"| `{m['name']}` | {m['what']} | {m['scale']} |")
    L.append("")
    L.append("## Частицы фразы\n")
    L.append("| частица | роль |")
    L.append("| :-- | :-- |")
    for p in doc["particles"]:
        L.append(f"| `{p['name']}` | {p['role']} |")
    L.append("")
    L.append("## Счёт\n")
    lim = doc["limits"]
    L.append(f"Корней {total} ({na} с осью, {nn} без); меток формы {len(doc['labels'])}; частиц {len([p for p in doc['particles'] if p['name'] != '\"…\"'])} (+ кавычки); частей речи {len(doc['pos'])}. "
             f"Лимит: до {lim['max_roots']} смысловых корней в слове; `{lim['extra_root']}` как индикатор абстрактности (абстрактные существительные) сверх лимита, четвёртым.")
    return "\n".join(L) + "\n"


def lexicon_blocks(doc):
    total, na, nn = spec.counts(doc)
    b1 = [f"**Всего {total} корней: {na} с осью, {nn} без оси.** Блок сгенерирован из [`roots.yaml`](../roots.yaml).\n",
          f"**С осью ({na}):**\n", "| корень | ось (−5 … +5) | статус |", "| :-- | :-- | :-- |"]
    for r in spec.axis_roots(doc):
        b1.append(f"| {r['name']} | {r['ru_axis']} | {r['status']} |")
    b2 = [f"**Без оси ({nn}):** " + ", ".join(r["name"] for r in spec.noaxis_roots(doc)) + "."]
    return {"roots-with-axis": "\n".join(b1), "roots-no-axis": "\n".join(b2)}


def replace_block(text, name, body):
    pat = re.compile(rf"(<!-- BEGIN generated:{name} -->\n).*?(\n<!-- END generated:{name} -->)", re.S)
    if not pat.search(text):
        raise SystemExit(f"в lexicon.md нет блока generated:{name}")
    return pat.sub(lambda m: m.group(1) + body + m.group(2), text)


def validate_py(doc, text):
    names = " ".join(spec.root_names(doc))
    return re.sub(r'roots=set\("[^"]*"\.split\(\)\)', f'roots=set("{names}".split())', text)


def outputs():
    doc = spec.load()
    out = {TABLES: tables_md(doc)}
    lex = LEXICON.read_text(encoding="utf8")
    for k, v in lexicon_blocks(doc).items():
        lex = replace_block(lex, k, v)
    out[LEXICON] = lex
    out[VALIDATE] = validate_py(doc, VALIDATE.read_text(encoding="utf8"))
    return out


def main():
    check = "--check" in sys.argv
    doc = spec.load()
    total, na, nn = spec.counts(doc)
    print(f"корней {total}: с осью {na}, без оси {nn}")
    assert na + nn == total
    bad = []
    for path, text in outputs().items():
        old = path.read_text(encoding="utf8") if path.exists() else None
        if old != text:
            bad.append(path.relative_to(REPO))
            if not check:
                path.write_text(text, encoding="utf8")
    if check and bad:
        print("расхождение с roots.yaml:", *map(str, bad))
        sys.exit(1)
    print("записано:" if not check else "в порядке", *map(str, bad) if not check else "")


if __name__ == "__main__":
    main()
