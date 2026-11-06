"""Загрузка roots.yaml: единый источник правды о корнях, осях, метках и частицах."""
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
ROOTS_YAML = REPO / "roots.yaml"


def load(path=ROOTS_YAML):
    return yaml.safe_load(open(path, encoding="utf8"))


def root_names(doc=None):
    doc = doc or load()
    return [r["name"] for r in doc["roots"]]


def axis_roots(doc=None):
    doc = doc or load()
    return [r for r in doc["roots"] if r.get("axis")]


def noaxis_roots(doc=None):
    doc = doc or load()
    return [r for r in doc["roots"] if not r.get("axis")]


def counts(doc=None):
    doc = doc or load()
    a, n = len(axis_roots(doc)), len(noaxis_roots(doc))
    return a + n, a, n


def levels(doc=None):
    """Допустимые значения оси у отдельных корней {корень: [значения]}; у остальных корней с осью −5 … +5."""
    doc = doc or load()
    return {k: list(v) for k, v in (doc["limits"].get("levels") or {}).items()}


def poles_hash(doc=None):
    """Хеш имён корней и полюсов SemAxis: по нему build.py --check видит, что site/data/math.json устарел."""
    import hashlib
    import json
    doc = doc or load()
    key = [[r["name"], r.get("semaxis")] + ([r["center"]] if r.get("center") else []) for r in doc["roots"]]
    return hashlib.sha1(json.dumps(key, ensure_ascii=False).encode()).hexdigest()[:12]
