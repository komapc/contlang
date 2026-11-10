"""Версии языка (lang/README.md): каждая грузится, валидатор создаётся, спецификации собираются."""
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
sys.path.insert(0, str(REPO / "scripts" / "eval"))
import spec  # noqa: E402
from prepare import build_spec  # noqa: E402
from validator import Validator  # noqa: E402

VERSIONS = spec.versions()


def test_v1_and_v2_present():
    assert VERSIONS[0] == "v1" and "v2" in VERSIONS


def test_default_is_v1():
    assert spec.load() == spec.load(version="v1")
    assert spec.paths()["roots"] == spec.ROOTS_YAML


def test_unknown_version():
    with pytest.raises(ValueError):
        spec.paths("no-such-version")


@pytest.mark.parametrize("version", VERSIONS)
def test_version_loads(version):
    doc = spec.load(version=version)
    names = spec.root_names(doc)
    assert names and len(names) == len(set(names))
    for key in ("limits", "labels", "particles", "pos"):
        assert key in doc, f"{version}: нет раздела {key}"


@pytest.mark.parametrize("version", VERSIONS)
def test_version_has_description(version):
    if version == "v1":
        return
    base = spec.LANG / version
    assert (base / "README.md").exists() or (base / "charter.md").exists(), f"{version}: нет README.md или charter.md"


@pytest.mark.parametrize("version", VERSIONS)
def test_validator_builds(version):
    doc = spec.load(version=version)
    v = Validator(doc)
    root = spec.root_names(doc)[0]
    assert not [i for i in v.check(f"{root} | o") if i.level == "error"]
    assert [i for i in v.check("NOSUCHROOT | o") if i.level == "error"]


@pytest.mark.parametrize("version", VERSIONS)
@pytest.mark.parametrize("kind", ["enc", "dec"])
@pytest.mark.parametrize("task", ["words", "sents"])
def test_spec_builds(version, kind, task):
    text = build_spec(kind, task, version=version)
    doc = spec.load(version=version)
    assert "{{" not in text
    assert all(name in text for name in spec.root_names(doc))
