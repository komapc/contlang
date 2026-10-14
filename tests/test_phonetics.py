"""Фонетика (phonetics.yaml): полнота, уникальность слогов, актуальность site/data/phonetics.json."""
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "site"))
sys.path.insert(0, str(REPO / "scripts" / "mincode"))
import build  # noqa: E402


def test_phonetics_json_is_current():
    p = REPO / "site" / "data" / "phonetics.json"
    assert p.read_text(encoding="utf8") == json.dumps(build.phonetics_json(), ensure_ascii=False, indent=0) + "\n"


def test_every_root_has_a_sound():
    roots = [r["name"] for r in yaml.safe_load((REPO / "roots.yaml").read_text(encoding="utf8"))["roots"]]
    ph = yaml.safe_load((REPO / "phonetics.yaml").read_text(encoding="utf8"))
    assert sorted(roots) == sorted(ph["roots"])
    ph_labels = {l["name"] for l in yaml.safe_load((REPO / "roots.yaml").read_text(encoding="utf8"))["labels"]}
    assert ph_labels == set(ph["labels"])


def test_no_two_meanings_sound_alike():
    d = build.phonetics_json()
    forms = []
    for r in d["roots"].values():
        forms += [r["z"]] + ([r["p"], r["n"]] if r["axis"] else [])
    for l in d["labels"].values():
        forms += [l["p"], l["n"], l["z"]]
    forms += list(d["roles"].values()) + list(d["particles"].values())
    dup = [f for f, c in Counter(forms).items() if c > 1]
    assert not dup, dup
