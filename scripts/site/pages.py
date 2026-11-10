"""Страницы сайта: из одного двуязычного источника data/site/index.html — site/index.html (английский) и site/ru/index.html (русский),
из data/site/vs-toki-pona.{en,ru}.md — сравнение с Toki Pona site/vs-toki-pona/ и site/ru/vs-toki-pona/,
из docs/*.md — site/docs/<имя>/index.html и оглавление site/docs/index.html, из их переводов docs/en/*.md —
site/docs/en/<имя>/index.html и оглавление site/docs/en/index.html, и site/sitemap.xml.

У каждого языка свой адрес (поисковики видят одну страницу на один язык): элемент с data-l="en" или data-l="ru"
остаётся только на странице своего языка, data-l="mc" (запись на самом min-co) — на английской.
Вызывается из scripts/site/build.py (там же --check); отдельно:

    python3 scripts/site/pages.py          # записать
    python3 scripts/site/pages.py --check  # проверить, что файлы не устарели
"""
import datetime
import html
import re
import sys
from pathlib import Path

import markdown

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
SITE = REPO / "site"
SRC = REPO / "data" / "site" / "index.html"
BASE = "https://minco.lipu.dev"
GH = "https://github.com/komapc/contlang"

# публикуемые документы, в порядке оглавления (docs/history/ — архив, остаётся на GitHub)
DOCS = ["reading", "model", "philosophy", "syntax", "tables", "encoding", "lexicon", "phonology", "math", "rethink"]

# сравнение с Toki Pona: адрес на каждом языке (x-default — английский, как у главной)
COMPARE = {"en": "/vs-toki-pona/", "ru": "/ru/vs-toki-pona/"}
COMPARE_DESC = {
    "en": "Toki Pona has about 120–140 words; min-co has 45 meaning roots with value axes, encoded and decoded by vector math. "
          "How the two minimal conlangs differ in goals and grammar.",
    "ru": "В Toki Pona около 120–140 слов, в min-co — 45 смысловых корней с осями значений, которые кодирует и раскодирует "
          "векторная математика. Чем различаются два минималистичных искусственных языка.",
}

VOID = {"meta", "link", "br", "img", "input", "hr", "source"}
GENERATED = "<!-- сгенерировано scripts/site/pages.py из data/site/index.html, руками не править -->"


# ---------- главная страница: один язык из двуязычного источника

def only_lang(src, lang):
    """Убрать элементы с data-l чужого языка (вместе с содержимым)."""
    keep = {"en": {"en", "mc"}, "ru": {"ru"}}[lang]
    out, pos = [], 0
    start = re.compile(r'<([a-zA-Z][a-zA-Z0-9]*)\b[^>]*?\sdata-l="([a-z]+)"[^>]*>')
    while True:
        m = start.search(src, pos)
        if not m:
            out.append(src[pos:])
            break
        tag, l = m.group(1).lower(), m.group(2)
        end = m.end() if tag in VOID else close_of(src, tag, m.end())
        if l in keep:
            out.append(src[pos:m.end()])
            pos = m.end()
            continue
        a, b = m.start(), end
        # элемент на своей строке — убрать и строку
        ls = src.rfind("\n", 0, a) + 1
        if not src[ls:a].strip() and src[b:b + 1] == "\n":
            a, b = ls, b + 1
        out.append(src[pos:a])
        pos = b
    return "".join(out)


# Маяк Cloudflare Web Analytics и Google Analytics (грузится только после согласия, site/consent.js)
# берём из исходника главной, чтобы они были в одном месте.
BEACON = "\n".join(l for l in SRC.read_text(encoding="utf8").splitlines() if "cf-beacon" in l or "/consent.js" in l)


def close_of(src, tag, i):
    """Конец элемента tag, открытого перед позицией i (с учётом вложенных одноимённых)."""
    if tag == "script":
        return src.index("</script>", i) + len("</script>")
    depth = 1
    for m in re.finditer(r"<(/?)" + tag + r"\b[^>]*>", src[i:], flags=re.I):
        depth += -1 if m.group(1) else 1
        if depth == 0:
            return i + m.end()
    raise ValueError("не закрыт <%s> на позиции %d" % (tag, i))


def main_page(lang):
    src = SRC.read_text(encoding="utf8")
    src = src[src.index("<!doctype html>"):]  # служебный комментарий источника не публикуем
    page = only_lang(src, lang)
    page = page.replace('<html lang="en">', '<html lang="%s">' % lang, 1)
    h = page.index("</head>")  # в <head> метка языка больше не нужна
    page = re.sub(r' data-l="[a-z]+"', "", page[:h]) + page[h:]
    page = page.replace("<!doctype html>\n", "<!doctype html>\n" + GENERATED + "\n", 1)
    other = {"en": ['data-l="ru"'], "ru": ['data-l="en"', 'data-l="mc"']}[lang]
    assert not any(o in page for o in other), lang
    return page


# ---------- документы: docs/*.md → HTML

def slug(text):
    """Якорь заголовка как на GitHub: строчные, без знаков препинания, пробелы → дефисы."""
    t = re.sub(r"<[^>]+>", "", text).strip().lower()
    t = re.sub(r"[^\w\- ]", "", t)
    return t.replace(" ", "-")


def doc_title(md):
    m = re.search(r"^# (.+)$", md, flags=re.M)
    return plain(m.group(1)) if m else ""


def plain(md):
    t = re.sub(r"!?\[([^\]]*)\]\([^)]*\)", r"\1", md)
    t = re.sub(r"[`*_]", "", t)
    return re.sub(r"\s+", " ", t).strip()


def doc_description(md, limit=160, least=70):
    """Первые абзацы текста (не заголовки, не таблицы, не код), пока не наберётся least символов; не длиннее limit."""
    t = ""
    for para in re.split(r"\n\s*\n", re.sub(r"```.*?```", "", md, flags=re.S)):
        p = para.strip()
        if not p or p[0] in "#|>-*<" or re.match(r"\d+\.", p):
            continue
        t = (t + " " + plain(p)).strip()
        if len(t) >= least:
            break
    if len(t) <= limit:
        return t
    return t[:limit - 1].rsplit(" ", 1)[0].rstrip(",.;:—–- ") + "…"


def fix_links(body, rel_dir):
    """Ссылки на опубликованные документы — на страницы сайта, остальные относительные — на GitHub."""
    def sub(m):
        href = html.unescape(m.group(1))
        if re.match(r"^(https?:|mailto:|#|/)", href):
            return m.group(0)
        path, _, frag = href.partition("#")
        target = (REPO / rel_dir / path).resolve()
        rel = target.relative_to(REPO).as_posix() if target.is_relative_to(REPO) else path
        m_doc = re.fullmatch(r"docs/(en/)?([^/]+)\.md", rel)
        if m_doc and m_doc.group(2) in DOCS:
            url = "/docs/%s%s/" % (m_doc.group(1) or "", m_doc.group(2))
        else:
            url = "%s/%s/main/%s" % (GH, "tree" if target.is_dir() else "blob", rel)
        if frag:
            url += "#" + frag
        return 'href="%s"' % html.escape(url, quote=True)
    return re.sub(r'href="([^"]*)"', sub, body)


def md_html(md, rel_dir="docs"):
    body = markdown.markdown(md, extensions=["tables", "fenced_code", "sane_lists", "toc"],
                             extension_configs={"toc": {"slugify": lambda v, sep: slug(v), "permalink": False}})
    # в таблицах GitHub читает `\|` внутри кода как «|»; Python-Markdown оставляет обратную косую
    body = re.sub(r"<t([dh])([^>]*)>(.*?)</t\1>", lambda m: "<t%s%s>%s</t%s>" % (m.group(1), m.group(2), m.group(3).replace("\\|", "|"), m.group(1)), body, flags=re.S)
    return fix_links(body, rel_dir)


CSS = """:root{--bg:#fbfaf7;--fg:#1d1d1b;--mut:#6b6a63;--line:#dcd9cf;--card:#fff;--acc:#2f5d50;--acc2:#e8f0ec;--mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#161715;--fg:#ecebe4;--mut:#9b9a91;--line:#34342f;--card:#1f201d;--acc:#8fc4b0;--acc2:#23312c}}
:root[data-theme=dark]{--bg:#161715;--fg:#ecebe4;--mut:#9b9a91;--line:#34342f;--card:#1f201d;--acc:#8fc4b0;--acc2:#23312c}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}
.wrap{max-width:860px;margin:0 auto;padding:0 16px 64px}
header{padding:24px 0 8px;display:flex;gap:6px 16px;flex-wrap:wrap;align-items:baseline;border-bottom:1px solid var(--line)}
header .home{font-size:22px;font-weight:700;color:var(--fg);text-decoration:none}
header a{color:var(--acc)}
h1{font-size:28px;line-height:1.25;margin:24px 0 10px;letter-spacing:-.01em}h2{font-size:21px;margin:30px 0 8px}h3{font-size:17px;margin:22px 0 6px}
a{color:var(--acc)}
code{font-family:var(--mono);font-size:14px;background:var(--acc2);border-radius:4px;padding:0 3px;overflow-wrap:anywhere}
pre{background:var(--acc2);border-radius:8px;padding:10px 12px;overflow-x:auto}pre code{background:none;padding:0;overflow-wrap:normal}
table{border-collapse:collapse;font-size:14px;display:block;overflow-x:auto;max-width:100%}
th,td{border-bottom:1px solid var(--line);padding:6px 8px;text-align:left;vertical-align:top}th{color:var(--mut);font-weight:600}
blockquote{margin:12px 0;padding:2px 14px;border-left:3px solid var(--line);color:var(--mut)}
.mut{color:var(--mut);font-size:14px}
nav.docs{margin:36px 0 0;padding-top:12px;border-top:1px solid var(--line)}nav.docs ul{padding-left:20px}
footer{margin-top:28px;color:var(--mut);font-size:14px}"""


# подписи страниц документов по языкам
TEXT = {
    "ru": {"locale": "ru_RU", "home": "/ru/", "docs": "Документация", "nav": "Документы", "code": "код"},
    "en": {"locale": "en_US", "home": "/", "docs": "Documentation", "nav": "Documents", "code": "code"},
}


def docs_path(lang, n=None):
    """Адрес документа n (или оглавления) на языке lang."""
    return ("/docs/" if lang == "ru" else "/docs/en/") + (n + "/" if n else "")


def page_html(title, desc, n, body, lang="ru", paths=None, nav=True):
    """Страница документа n (n=None — оглавление): у каждого языка свой canonical, перекрёстные hreflang, x-default — английский, как у главной.
    paths — {"en": адрес, "ru": адрес} для страницы вне документов (тогда без оглавления документов, если nav=False)."""
    tx = TEXT[lang]
    paths = paths or {"en": docs_path("en", n), "ru": docs_path("ru", n)}
    path, ru_path, en_path = paths[lang], paths["ru"], paths["en"]
    url = BASE + path
    t, d = html.escape(title, quote=True), html.escape(desc, quote=True)
    ld = ('{"@context":"https://schema.org","@type":"TechArticle","headline":%s,"description":%s,"url":"%s","inLanguage":"%s",'
          '"isPartOf":{"@type":"WebSite","name":"min-co","url":"%s/"},"author":{"@type":"Person","name":"komapc","url":"https://github.com/komapc"}}'
          % (json_str(title), json_str(desc), url, lang, BASE))
    switch = ('<a href="%s" hreflang="en" lang="en">English</a>' % en_path if lang == "ru"
              else '<a href="%s" hreflang="ru" lang="ru">Русский</a>' % ru_path)
    return f"""<!doctype html>
<!-- сгенерировано scripts/site/pages.py, руками не править -->
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="ru" href="{BASE}{ru_path}">
<link rel="alternate" hreflang="en" href="{BASE}{en_path}">
<link rel="alternate" hreflang="x-default" href="{BASE}{en_path}">
<meta property="og:type" content="article">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="{tx['locale']}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:image" content="{BASE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<script type="application/ld+json">{ld}</script>
<style>
{CSS}
</style>
{BEACON}
</head>
<body>
<div class="wrap">
<header><a class="home" href="{tx['home']}">min-co</a><a href="{docs_path(lang)}">{tx['docs']}</a>{switch}</header>
<main>
{body}
</main>
{docs_nav(lang) if nav else ""}
<footer><a href="https://lipu.dev/">lipu.dev</a> · <a href="{GH}">{tx['code']}</a></footer>
</div>
</body>
</html>
"""


def json_str(s):
    import json
    return json.dumps(s, ensure_ascii=False)


def docs_meta(lang="ru"):
    out = []
    folder = REPO / "docs" if lang == "ru" else REPO / "docs" / "en"
    for n in DOCS:
        md = (folder / (n + ".md")).read_text(encoding="utf8")
        out.append((n, doc_title(md), doc_description(md), md))
    return out


def docs_nav(lang="ru"):
    items = "\n".join('<li><a href="%s">%s</a></li>' % (docs_path(lang, n), html.escape(t)) for n, t, _, _ in docs_meta(lang))
    label = TEXT[lang]["nav"]
    return '<nav class="docs" aria-label="%s"><b>%s</b>\n<ul>\n%s\n</ul>\n</nav>' % (label, label, items)


def doc_page(n, title, desc, md, lang="ru"):
    if lang == "ru":
        src = '<p class="mut">Исходник: <a href="%s/blob/main/docs/%s.md">docs/%s.md</a> на GitHub. Документ описывает предыдущую запись (с <code>|</code> и суффиксами); запись в стиле токи пона ещё не перенесена.</p>' % (GH, n, n)
    else:
        src = ('<p class="mut">Source: <a href="%s/blob/main/docs/en/%s.md">docs/en/%s.md</a> on GitHub, translated from the <a href="%s" hreflang="ru" lang="ru">Russian original</a>. '
               "This document describes the previous notation (with <code>|</code> and suffixes); the notation in the style of Toki Pona has not been moved over yet.</p>" % (GH, n, n, docs_path("ru", n)))
    return page_html(title if "min-co" in title else title + " — min-co", desc, n, md_html(md, "docs" if lang == "ru" else "docs/en") + "\n" + src, lang)


def docs_index(lang="ru"):
    items = "\n".join('<li><a href="%s">%s</a> — %s</li>' % (docs_path(lang, n), html.escape(t), html.escape(d)) for n, t, d, _ in docs_meta(lang))
    if lang == "ru":
        body = ("<h1>Документация min-co</h1>\n<p>min-co — минимальный непрерывный искусственный язык: слово — до трёх смысловых корней с осями значений "
                "и часть речи с метками после черты. Здесь собраны документы о языке; источник правды о корнях — "
                '<a href="%s/blob/main/roots.yaml">roots.yaml</a>. Попробовать язык — на <a href="/ru/">главной странице</a>.</p>\n<ul>\n%s\n</ul>' % (GH, items))
        return page_html("Документация min-co — искусственный язык из 45 корней",
                         "Документы о min-co, минимальном искусственном языке из 45 смысловых корней: модель, синтаксис, словарь, фонология, рецепты кодирования, математика.",
                         None, body)
    body = ("<h1>min-co documentation</h1>\n<p>min-co is a minimal continuous constructed language: a word is up to three meaning roots with value axes, "
            "and a part of speech with labels after the bar. These are the documents about the language, translated from the "
            '<a href="/docs/" hreflang="ru" lang="ru">Russian originals</a>; the source of truth about the roots is '
            '<a href="%s/blob/main/roots.yaml">roots.yaml</a>. Try the language on the <a href="/">home page</a>.</p>\n<ul>\n%s\n</ul>' % (GH, items))
    return page_html("min-co documentation: a constructed language of 45 roots",
                     "Documents about min-co, a minimal constructed language of 45 meaning roots: model, syntax, lexicon, phonology, encoding recipes, math.",
                     None, body, "en")


# ---------- сравнение с Toki Pona

def compare_page(lang):
    md = (REPO / "data" / "site" / ("vs-toki-pona.%s.md" % lang)).read_text(encoding="utf8")
    return page_html(doc_title(md), COMPARE_DESC[lang], None, md_html(md, "data/site"), lang, paths=COMPARE, nav=False)


# ---------- сборка и карта сайта

def page_outputs():
    out = {SITE / "index.html": main_page("en"), SITE / "ru" / "index.html": main_page("ru"), SITE / "docs" / "index.html": docs_index(),
           SITE / "docs" / "en" / "index.html": docs_index("en"),
           SITE / "vs-toki-pona" / "index.html": compare_page("en"), SITE / "ru" / "vs-toki-pona" / "index.html": compare_page("ru")}
    for n, t, d, md in docs_meta():
        out[SITE / "docs" / n / "index.html"] = doc_page(n, t, d, md)
    for n, t, d, md in docs_meta("en"):
        out[SITE / "docs" / "en" / n / "index.html"] = doc_page(n, t, d, md, "en")
    return out


def url_of(p):
    rel = p.relative_to(SITE).as_posix()
    return BASE + "/" + rel[:-len("index.html")]


def sitemap(pages):
    """lastmod: прежняя дата из site/sitemap.xml, если страница не изменилась, иначе сегодня (так --check не зависит от истории git)."""
    old = {}
    sm = SITE / "sitemap.xml"
    if sm.exists():
        old = dict(re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", sm.read_text(encoding="utf8")))
    today = datetime.date.today().isoformat()

    def alt(en, ru):
        return ('\n    <xhtml:link rel="alternate" hreflang="en" href="%s"/>\n    <xhtml:link rel="alternate" hreflang="ru" href="%s"/>'
                '\n    <xhtml:link rel="alternate" hreflang="x-default" href="%s"/>\n  ' % (en, ru, en))
    pairs = [(BASE + "/", BASE + "/ru/"), (BASE + COMPARE["en"], BASE + COMPARE["ru"])] + [(BASE + docs_path("en", n), BASE + docs_path("ru", n)) for n in [None] + DOCS]
    alts = {u: alt(en, ru) for en, ru in pairs for u in (en, ru)}
    rows = []
    for p, text in pages.items():
        u = url_of(p)
        same = p.exists() and p.read_text(encoding="utf8") == text
        lm = old[u] if same and u in old else today
        rows.append("  <url><loc>%s</loc><lastmod>%s</lastmod>%s</url>" % (u, lm, alts.get(u, "")))
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + "\n".join(rows) + "\n</urlset>\n")


def outputs():
    pages = page_outputs()
    pages[SITE / "sitemap.xml"] = sitemap(pages)
    return pages


def main():
    out = outputs()
    if "--check" in sys.argv:
        bad = [str(p) for p, t in out.items() if not p.exists() or p.read_text(encoding="utf8") != t]
        print("устарели: " + ", ".join(bad) if bad else "в порядке")
        sys.exit(1 if bad else 0)
    for p, t in out.items():
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(t, encoding="utf8")
        print("записано", p.relative_to(REPO))


if __name__ == "__main__":
    main()
