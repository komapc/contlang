"""Страница сравнения с Toki Pona: по адресу на язык, перекрёстные hreflang, в карте сайта; числа корней совпадают с roots.yaml."""
import re
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "scripts" / "site"))
import pages  # noqa: E402

OUT = pages.outputs()


def page(lang):
    return OUT[pages.SITE / pages.COMPARE[lang].strip("/") / "index.html"]


@pytest.mark.parametrize("lang", ["en", "ru"])
def test_lang_and_alternates(lang):
    html = page(lang)
    assert '<html lang="%s">' % lang in html
    assert '<link rel="canonical" href="%s%s">' % (pages.BASE, pages.COMPARE[lang]) in html
    for other in ("en", "ru"):
        assert '<link rel="alternate" hreflang="%s" href="%s%s">' % (other, pages.BASE, pages.COMPARE[other]) in html
    assert '<link rel="alternate" hreflang="x-default" href="%s%s">' % (pages.BASE, pages.COMPARE["en"]) in html
    assert re.search(r"<title>[^<]*Toki Pona[^<]*</title>", html)
    assert '<meta name="description" content="%s">' % pages.COMPARE_DESC[lang] in html


def test_in_sitemap():
    sitemap = OUT[pages.SITE / "sitemap.xml"]
    for lang in ("en", "ru"):
        assert "<loc>%s%s</loc>" % (pages.BASE, pages.COMPARE[lang]) in sitemap


def test_linked_from_home():
    assert 'href="/vs-toki-pona/"' in OUT[pages.SITE / "index.html"]
    assert 'href="/ru/vs-toki-pona/"' in OUT[pages.SITE / "ru" / "index.html"]


@pytest.mark.parametrize("lang", ["en", "ru"])
def test_root_counts_match_roots_yaml(lang):
    roots = yaml.safe_load((REPO / "roots.yaml").read_text(encoding="utf8"))["roots"]
    md = (REPO / "data" / "site" / ("vs-toki-pona.%s.md" % lang)).read_text(encoding="utf8")
    with_axis = sum(1 for r in roots if r.get("axis"))
    assert re.search(r"\b%d\b" % len(roots), md)
    assert re.search(r"\b%d\b" % with_axis, md)
    assert "%d" % len(roots) in pages.COMPARE_DESC[lang]


@pytest.mark.parametrize("lang", ["en", "ru"])
def test_internal_links_resolve(lang):
    for href in re.findall(r'<a href="(/[^"]*)"', page(lang)):
        target = pages.SITE / href.strip("/") / "index.html" if href != "/" else pages.SITE / "index.html"
        assert target in OUT or target.exists(), href
