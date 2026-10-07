"""Согласованность roots.yaml, сгенерированных файлов и документации."""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
import gen  # noqa: E402
import spec  # noqa: E402


def test_generated_files_are_current():
    for path, text in gen.outputs().items():
        assert path.read_text(encoding="utf8") == text, f"{path} расходится с roots.yaml: python3 scripts/mincode/gen.py"


def test_counts():
    total, with_axis, no_axis = spec.counts()
    assert (total, with_axis, no_axis) == (45, 41, 4)


def test_roots_unique_and_complete():
    doc = spec.load()
    names = [r["name"] for r in doc["roots"]]
    assert len(names) == len(set(names))
    for r in doc["roots"]:
        if r["axis"]:
            assert r["en_axis"] and r["ru_axis"] and r["status"], r["name"]
            a, b = r["semaxis"]
            assert a.split() and b.split(), r["name"]
            assert set(r["axis"]) == {"neg", "mid", "pos"}
        else:
            assert r["ru_gloss"], r["name"]


def test_validator_script_roots_match_yaml():
    text = (REPO / "data" / "translation_test" / "republic_validate.py").read_text(encoding="utf8")
    got = set(re.search(r'roots=set\("([^"]+)"', text).group(1).split())
    assert got == set(spec.root_names())


def test_docs_mention_current_count():
    total, a, n = spec.counts()
    assert f"Около {total}" in (REPO / "docs" / "model.md").read_text(encoding="utf8")
    assert f"Корней {total} ({a} с осью, {n} без)" in (REPO / "docs" / "tables.md").read_text(encoding="utf8")


def test_removed_roots_not_in_roots():
    names = set(spec.root_names())
    assert not names & {"MAYBE", "CONTAINER", "HEAR", "KIND", "WORD"}


def test_no_stale_counts_in_current_docs():
    stale = ["44 корня", "46 корней", "40 с осью", "Около 44", "Около 46", "Около 30"]
    for rel in ["README.md", "docs/model.md", "docs/tables.md", "docs/philosophy.md", "docs/syntax.md", "docs/encoding.md", ".claude/skills/mincode/SKILL.md"]:
        text = (REPO / rel).read_text(encoding="utf8")
        for s in stale:
            assert s not in text, (rel, s)
