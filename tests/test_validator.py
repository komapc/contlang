"""Проверка валидатора кодов и кодов из документации."""
import re
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
from validator import Validator  # noqa: E402

V = Validator()


def errors(code):
    return {i.kind for i in V.check_any(code) if i.level == "error"}


GOOD = [
    "GOOD(=-5) | a",
    "THING(=+4) BIG(=+5) | o N+3",
    'SOMEONE | o M-5 SEE | i T-2 E THING | o',
    "MOVE NEAR(=+4) | i T-2 M-5",
    'LA [ RULE(=+4) PLACE | o ] SAY | i V-4 PE SOMEONE | o',
    "SOMEONE | o AND SOMEONE | o",
    "LIVE | i AND SAME(=-5) SAY | i",
    "AND | M-3",
    'SAY | i T-2 "Serpentes" ',
    "KNOW ABSTRACT(=+5) | o",
    "SOMEONE KNOW RULE ABSTRACT(=+4) | o",  # ABSTRACT сверх лимита
    "DO | i K+4 E SOMEONE | o",
    "MANY(=0) | e",
    "CONSUME | i !",
]

BAD = {
    "UNKNOWNROOT | o": "unknown_root",
    "MAYBE(=-3) | i": "unknown_root",
    "CONTAINER | o": "unknown_root",
    "SEE(=+3) | i": "axis_on_axisless",
    "PLACE(=-5) | o": "axis_on_axisless",
    "GOOD(=+7) | a": "axis_range",
    "MANY(=-3) | a": "axis_range",
    "SOMEONE MOVE THINK KNOW | o": "too_many_roots",
    "GOOD | a I0": "label_value",
    "GOOD | a I+9": "label_range",
    "GOOD | a T-2 T-3": "dup_label",
    "GOOD | a Z+1": "unknown_label",
    "T-2 GOOD | a": "label_before_bar",
    "GOOD | q": "bad_pos",
    "LA [ GOOD | a": "brackets",
    "GOOD | a ]": "brackets",
    'GOOD | a "oops': "bad_quote",
    "GOOD(=+1) goodness | o": "bare_word",
}


@pytest.mark.parametrize("code", GOOD)
def test_good(code):
    assert not errors(code), (code, [i for i in V.check(code)])


@pytest.mark.parametrize("code,kind", list(BAD.items()))
def test_bad(code, kind):
    assert kind in errors(code), (code, V.check(code))


def test_quoted_content_is_opaque():
    # кавычки не дают ложных «неизвестных корней» (CO, II в названиях)
    assert not errors('BEGIN(=-5) | i PI "Photosystem II" PI "CO2"')


def test_legacy_notation_is_warning_not_error():
    iss = V.check("SOMEONE-o LI SEE-i(TIME=-2)")
    assert iss and all(i.level == "warning" for i in iss), iss


def _doc_codes(rel):
    for ln, line in enumerate((REPO / rel).read_text(encoding="utf8").splitlines(), 1):
        for s in re.findall(r"`([^`]+)`", line):
            s = s.replace("\\|", "|")
            if "|" in s and re.search(r"[A-Z]{2,}", s) and "ROOT" not in s and "…" not in s:
                yield rel, ln, s


@pytest.mark.parametrize("rel", ["docs/encoding.md", "docs/tables.md", "docs/syntax.md", "docs/model.md", ".claude/skills/mincode/SKILL.md"])
def test_codes_in_docs_are_valid(rel):
    bad = [(ln, s, sorted(errors(s))) for _, ln, s in _doc_codes(rel) if errors(s)]
    assert not bad, bad


def test_clause_separator_and_form_rule():
    assert not errors('SOMEONE | o SAY | i T-2 ; THING | o LIVE | i')
    assert "no_form" in errors('SOMEONE PI "Aden"')  # главное слово без формы
    assert not errors('SOMEONE | o PI "Aden"')
    assert not errors('TIME MEASURE(=-5) "10" | o N+3')
    assert not errors("LIVE | i AND SAME(=-5) SAY | i")  # модификатор после AND без формы допустим


def test_braced_sentences():
    v = Validator()
    ok = [
        "{ SOMEONE | o } { SAY | i T-2 } E { THING | o }",
        "{ SOMEONE | o } AND { SAME(=-5) } { SAY | i }",
        '{ SOMEONE | o } "Europe" ; { LIVE | i }',
    ]
    bad = {
        "SOMEONE | o { SAY | i }": "outside_word",
        "{ SOMEONE SAY | o  SAY | i }": "bar",
        "{ SOMEONE | o": "braces",
        "{ GOOD BIG LIVE SAME | o }": "too_many_roots",
    }
    for c in ok:
        assert not [i for i in v.check_any(c) if i.level == "error"], c
    for c, kind in bad.items():
        assert kind in {i.kind for i in v.check_any(c)}, c
