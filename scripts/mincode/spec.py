"""Загрузка roots.yaml: единый источник правды о корнях, осях, метках и частицах.

Версии языка (lang/README.md): v1 — файлы на прежних местах (roots.yaml в корне, шаблоны в data/eval/templates/),
остальные — lang/<id>/ с тем же набором файлов. Без аргумента везде v1.
"""
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parents[2]
ROOTS_YAML = REPO / "roots.yaml"
LANG = REPO / "lang"
DEFAULT = "v1"


def paths(version=DEFAULT):
    """Файлы версии: roots (roots.yaml), templates (шаблоны спецификаций), tips (приёмы для модели сайта), phonetics (может не быть)."""
    if version == "v1":
        return {"roots": ROOTS_YAML, "templates": REPO / "data" / "eval" / "templates",
                "tips": REPO / "data" / "site" / "tips_short.md", "phonetics": REPO / "phonetics.yaml"}
    base = LANG / version
    if not (base / "roots.yaml").exists():
        raise ValueError(f"нет версии языка {version!r}: нет {base / 'roots.yaml'} (есть: {', '.join(versions())})")
    return {"roots": base / "roots.yaml", "templates": base / "templates", "tips": base / "tips_short.md", "phonetics": base / "phonetics.yaml"}


def versions():
    """Все версии: v1 и каждая папка lang/<id>/ с roots.yaml."""
    return ["v1"] + sorted(p.name for p in LANG.glob("*") if (p / "roots.yaml").exists() and p.name != "v1")


def load(path=ROOTS_YAML, version=None):
    if version is not None:
        path = paths(version)["roots"]
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
