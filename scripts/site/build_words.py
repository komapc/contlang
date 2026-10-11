"""Сведения о словах словаря сайта для декодера: site/data/words.json (по порядку слов math.json).

pos   — строка из 4 цифр 0…9 на слово: доля смыслов имени, глагола, прилагательного, наречия по WordNet
        (счётчики употреблений лемм из SemCor, +0,2 на каждый синсет, чтобы не было нулей у редких);
        "" — слова нет в WordNet.
lemma — номер слова-леммы в словаре (tools → tool, housed → house) или -1, если слово само лемма или леммы нет в словаре.
stop  — номера служебных слов (местоимения, предлоги, союзы, модальные…, и всё, чего нет в WordNet): декодер их не предлагает.

Запуск локально (нужен WordNet в data/raw/nltk):
    .venv/bin/python scripts/site/build_words.py
"""
import json
from pathlib import Path

import nltk

REPO = Path(__file__).resolve().parents[2]
nltk.data.path.insert(0, str(REPO / "data" / "raw" / "nltk"))
from nltk.corpus import wordnet as wn  # noqa: E402

OUT = REPO / "site" / "data"
P = "nvar"  # имя, глагол, прилагательное (с сателлитами s), наречие
FUNC = set("""
i me my mine myself we us our ours ourselves you your yours yourself yourselves he him his himself she her hers herself
it its itself they them their theirs themselves what which who whom whose this that these those
am is are was were be been being have has had having do does did doing done
a an the and but if or because as until while of at by for with about against between into through during before after
above below to from up down in out on off over under again further then once here there when where why how all any both
each few more most other some such no nor not only own same so than too very can will just should now
among amongst within without upon unto onto toward towards across along around behind beneath beside besides beyond
despite except inside near outside since though although unless whether whereas via per amid throughout
would could might must shall may ought also yet ever never always often perhaps maybe else however therefore thus hence
anyone anybody anything everyone everybody everything someone somebody something nobody nothing none either neither
whoever whatever whichever wherever whenever another every many much several lot lots
""".split())


def shares(w):
    c = dict.fromkeys(P, 0.0)
    for p in P:
        base = wn.morphy(w, p)
        if not base:
            continue
        for l in wn.lemmas(base, pos=p):
            c[p] += l.count() + 0.2
    t = sum(c.values())
    return {p: c[p] / t for p in P} if t else None


def main():
    words = json.loads((OUT / "math.json").read_text(encoding="utf8"))["words"]
    index = {w: i for i, w in enumerate(words)}
    pos, lemma, stop = [], [], []
    for i, w in enumerate(words):
        sh = shares(w)
        pos.append("".join(str(min(9, round(sh[p] * 9))) for p in P) if sh else "")
        if w in FUNC or not sh:
            stop.append(i)
        base = wn.morphy(w, max(P, key=sh.get)) if sh else None
        lemma.append(index[base] if base and base != w and base in index else -1)
    (OUT / "words.json").write_text(json.dumps({"pos": pos, "lemma": lemma, "stop": stop}, separators=(",", ":")), encoding="utf8")
    print(f"слов {len(words)}, служебных {len(stop)}, со своей леммой в словаре {sum(x >= 0 for x in lemma)}, "
          f"words.json {(OUT / 'words.json').stat().st_size // 1024} КБ")


if __name__ == "__main__":
    main()
