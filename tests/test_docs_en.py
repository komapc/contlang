"""Английские документы docs/en идут парой с русскими docs: те же файлы, заголовки, таблицы, код и числа.

Ловит расхождение кода и чисел после правки одной из сторон, но не изменения в формулировках.
"""
import re
import sys
from collections import Counter
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "site"))
import pages  # noqa: E402

RU = REPO / "docs"
EN = RU / "en"
CYRILLIC = re.compile("[а-яёА-ЯЁ]")
FENCE = re.compile(r"```.*?```", flags=re.S)
SPAN = re.compile(r"`[^`\n]+`")
ROOT = re.compile(r"[A-Z]{2,}(?:\(=[-+]?\d\))?")


def read(folder, name):
    return (folder / (name + ".md")).read_text(encoding="utf8")


def prose(md):
    """Текст без блоков кода, HTML-комментариев (маркеры generated есть только в русском)."""
    return re.sub(r"<!--.*?-->", "", FENCE.sub("", md), flags=re.S)


def numbers(md, ru):
    """Числа вне кода и адресов ссылок; 10 721 и 0,5 в русском — то же, что 10,721 и 0.5 в английском."""
    t = re.sub(r"\]\([^)]*\)", "]", SPAN.sub("", prose(md)))
    if ru:
        t = re.sub(r"(?<=[0-9])[  ](?=[0-9]{3}(?![0-9]))", "", t)
        t = re.sub(r"(?<=[0-9]),(?=[0-9])", ".", t)
    else:
        t = re.sub(r"(?<=[0-9]),(?=[0-9]{3}(?![0-9]))", "", t)
    return Counter(re.findall(r"[0-9]+(?:\.[0-9]+)?", t))


def test_same_files():
    assert {p.stem for p in EN.glob("*.md")} == set(pages.DOCS)


@pytest.mark.parametrize("name", pages.DOCS)
def test_structure(name):
    ru, en = read(RU, name), read(EN, name)
    for pattern in (r"^#+ ", r"^\|"):
        assert len(re.findall(pattern, prose(ru), flags=re.M)) == len(re.findall(pattern, prose(en), flags=re.M)), pattern


@pytest.mark.parametrize("name", pages.DOCS)
def test_code_blocks(name):
    ru, en = FENCE.findall(read(RU, name)), FENCE.findall(read(EN, name))
    assert [ROOT.findall(b) for b in ru] == [ROOT.findall(b) for b in en]


@pytest.mark.parametrize("name", pages.DOCS)
def test_inline_code(name):
    ru, en = SPAN.findall(prose(read(RU, name))), SPAN.findall(prose(read(EN, name)))
    assert len(ru) == len(en)
    # код с кириллицей переводится (СВЯЗКА → LINK), весь остальной остаётся как есть
    assert not Counter(s for s in ru if not CYRILLIC.search(s)) - Counter(en)


@pytest.mark.parametrize("name", pages.DOCS)
def test_numbers(name):
    assert numbers(read(RU, name), True) == numbers(read(EN, name), False)


@pytest.mark.parametrize("name", pages.DOCS)
def test_links_resolve(name):
    for href in re.findall(r"\]\(([^)]+)\)", read(EN, name)):
        if not re.match(r"^(https?:|mailto:|#)", href):
            assert (EN / href.partition("#")[0]).exists(), href
