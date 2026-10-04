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
