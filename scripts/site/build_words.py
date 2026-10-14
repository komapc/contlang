"""Сведения о словах словаря сайта для декодера: site/data/words.json (по порядку слов math.json).

pos   — строка из 4 цифр 0…9 на слово: доля смыслов имени, глагола, прилагательного, наречия по WordNet
        (счётчики употреблений лемм из SemCor, +0,2 на каждый синсет, чтобы не было нулей у редких);
        "" — слова нет в WordNet.
lemma — номер слова-леммы в словаре (tools → tool, housed → house) или -1, если слово само лемма или леммы нет в словаре.
stop  — номера служебных слов (местоимения, предлоги, союзы, модальные…, и всё, чего нет в WordNet): декодер их не предлагает.
sexed — номера слов, у которых пол — часть смысла: male, female… или первый нарицательный синсет WordNet начинается
        с «a woman / a male / a young man…» либо лежит под man, woman, male, female. Только им кодер даёт корень SEX:
        teacher, president, chief — без пола (data/eval/runs/sex).
proper — номера имён собственных: все значения слова в WordNet — с заглавной (jakarta, monroe); кодер пишет их в кавычках.
plural — номера форм множественного числа имени (cities → city): кодер пишет код леммы (если её нет в словаре — самого слова) с меткой N+3.
person — номера слов, у которых первое значение имени в WordNet — человек (noun.person): кодер ставит роль `| o agent`
        (lawyer `RULE(=+3) KNOW(=+2) SIDE(=+2) | o agent`; +19 % «близко» на 88 словах, data/eval/runs/fix1).
infl  — словоформа → [база, часть речи кода, метки]: кодер всегда кодирует базовую форму и дописывает метки (решение пользователя 2026-10-14):
        множественное имени → `| o N+3`; глагол в прошедшем (-ed, got, grew, grown) → `| i T-2`, на -ing → `| i A0`, на -s → `| i`;
        причастие-признак (tired, alleged, related) → код глагола с `| a`, страдательное (-ed, -en) ещё `V-4`; отглагольное имя на -ing
        (setting, wedding) → код глагола с `| o`; сравнительная степень → `| a C+3`, превосходная → `C+5`.
        База — WordNet morphy в части речи, которая у формы главная (так discuss не становится discus), и правила для -er/-est.
extra — базы, которых нет в словаре сайта (allege, imprison, plaintiff): векторы Numberbatch (int8 × 127, base64), только для кодера.
sense — один смысл омонима (решение пользователя): у слова в этой части речи есть далёкий смысл (другой lexname, wup < 0.3,
        или другая часть речи без словообразовательной связи) → кодер кодирует вектор первого смысла:
        норм(слово) + норм(среднее опорных слов: леммы синсета, гиперонимов и слова толкования), как в data/eval/runs/senses.
        Ключ «база|часть речи кода», значение — номера опорных слов (в словаре сайта или в extra: номер ≥ N).

Запуск локально (нужен WordNet в data/raw/nltk):
    .venv/bin/python scripts/site/build_words.py
"""
import base64
import gzip
import json
from pathlib import Path

import numpy as np

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


import re  # noqa: E402

SEXW = r"(male|female|woman|man|girl|boy|mother|father|wife|husband|son|daughter|sister|brother|lady|queen|king|bride)"
HEAD = re.compile(r"^(a |an |the |any )?(adult |young |youthful |old |elderly |married |unmarried |fertile |only fertile |"
                  r"informal term for a |term of address for a )?" + SEXW + r"\b")
BOTH = re.compile(r"^\S* ?" + SEXW + " or " + SEXW + r"\b")  # «a father or mother» — пол не важен
SEXROOT = {"male.n.02", "female.n.02", "man.n.01", "woman.n.01", "male_child.n.01", "female_child.n.01"}
SEXADJ = {"male", "female", "masculine", "feminine"}


def sexed(w):
    """Пол — часть смысла: male, female… или первый нарицательный синсет имени — «a woman who…», «a male sovereign» или под man / woman."""
    if w in SEXADJ or wn.morphy(w, "a") in SEXADJ:
        return True
    b = wn.morphy(w, "n")
    ss = [s for s in wn.synsets(b, "n") if not any(l.name()[0].isupper() for l in s.lemmas() if l.name().lower() == b)][:1] if b else []
    return any((HEAD.search(s.definition()) and not BOTH.search(s.definition())) or s.name() in SEXROOT or SEXROOT & {h.name() for h in s.closure(lambda x: x.hypernyms())} for s in ss)


def proper(w):
    ls = {l.name() for p in P for b in {wn.morphy(w, p), w} - {None} for l in wn.lemmas(b, pos=p)}
    return bool(ls) and all(n[0].isupper() for n in ls)


def person(w):
    ss = wn.synsets(w, "n")
    return bool(ss) and ss[0].lexname() == "noun.person"


def bases(w, p):
    """все леммы формы w в части речи p (morphy даёт одну: stations → «Stations», а не station)"""
    return [b for b in dict.fromkeys(wn._morphy(w, p) + ([w] if wn.lemmas(w, pos=p) else [])) if wn.lemmas(b, pos=p)]


def lcount(b, p):
    return sum(l.count() + 0.2 for l in wn.lemmas(b, pos=p))


def shares(w):
    c = {p: sum(lcount(b, p) for b in bases(w, p)) for p in P}
    t = sum(c.values())
    return {p: c[p] / t for p in P} if t else None


def base(w, p):
    """базовая форма w в части речи p: самая частая лемма, отличная от w, если она частотнее самой w"""
    bs = [b for b in bases(w, p) if b != w]
    if not bs:
        return None
    b = max(bs, key=lambda b: lcount(b, p))
    return b if w not in bases(w, p) or lcount(b, p) >= lcount(w, p) else None


IRR = {"better": ("good", "C+3"), "best": ("good", "C+5"), "worse": ("bad", "C+3"), "worst": ("bad", "C+5")}
WNP = {"o": "n", "i": "v", "a": "a", "e": "r"}


def comparative(w):
    """bigger → big C+3, happiest → happy C+5 (morphy не снимает удвоение)"""
    if w in IRR:
        return IRR[w]
    for suf, mk in (("est", "C+5"), ("er", "C+3")):
        if not w.endswith(suf) or len(w) < len(suf) + 3:
            continue
        st = w[: -len(suf)]
        for b in (st[:-1] + "y" if st.endswith("i") else None, st[:-1] if len(st) > 2 and st[-1] == st[-2] else None, st, st + "e"):
            if b and wn.synsets(b, "a"):
                return b, mk
    return None


def derived(w, vb):
    """форма w (имя или признак) связана с глаголом vb словообразованием или как причастие (WordNet)"""
    return any(r.name() == vb and r.synset().pos() == "v" for p in "nas" for l in wn.lemmas(w, pos=p)
               for r in l.derivationally_related_forms() + l._related("<"))


def infl(w, sh):
    """словоформа → (база, часть речи кода, метки) или None, если w — сама базовая форма"""
    d = max(P, key=sh.get)
    vb = base(w, "v")
    if d == "v" and vb:
        if w.endswith("ing"):
            return vb, "i", "A0"
        if w.endswith("s") and w[:-1].rstrip("e") in (vb, vb.rstrip("e"), vb[:-1] + "i"):
            return vb, "i", ""
        return vb, "i", "T-2"
    if d == "a":
        if vb and (w.endswith(("ed", "en", "ing")) or wn.synsets(vb, "v")) and not base(w, "n"):
            return vb, "a", "" if w.endswith("ing") else "V-4"
        c = comparative(w)
        return (c[0], "a", c[1]) if c else None
    if d == "n":
        nb = base(w, "n")
        if nb and w.endswith("s"):
            return nb, "o", "N+3"
        if vb and w.endswith("ing") and derived(w, vb):
            return vb, "o", ""
    return None


cnt = lambda s, w: sum(l.count() for l in s.lemmas() if l.name().lower() == w)  # noqa: E731


def homonym(w, p, vec):
    """один смысл слова w в части речи p, если у w есть далёкий смысл, иначе None.
    Смысл — самый частый в WordNet; при почти равной частоте (≥ половины) — ближайший к вектору слова (bank — банк, а не берег)."""
    ps = {"a": "as"}.get(p, p)
    ss = [s for q in ps for s in wn.synsets(w, q)]
    if not ss:
        return None
    top = max(cnt(s, w) for s in ss)
    tie = [s for s in ss if cnt(s, w) * 2 >= top]
    def cos(s):
        A = [vec(a) for a in anchors(w, s)]
        A = [a for a in A if a is not None]
        if not A or vec(w) is None:
            return -1
        m = np.mean(A, 0)
        return float(m @ vec(w) / np.linalg.norm(m))
    s0 = max(tie, key=cos) if len(tie) > 1 else tie[0]
    near0 = {r.name() for l in s0.lemmas() if l.name().lower() == w for r in l.derivationally_related_forms()}
    for s in wn.synsets(w):
        if s == s0:
            continue
        if s.pos() in ps:
            far = (s0.wup_similarity(s) or 0) < 0.3 and s.lexname() != s0.lexname()
        else:  # другая часть речи: далёкий, если нет словообразовательной связи с выбранным смыслом
            far = not ({r.name() for l in s.lemmas() if l.name().lower() == w for r in l.derivationally_related_forms()} & ({w} | near0)) \
                and not any(r.synset() == s0 for l in s.lemmas() for r in l.derivationally_related_forms())
        if far:
            return s0
    return None


def anchors(w, s):
    a = [l.name() for l in s.lemmas()] + [l.name() for h in s.hypernyms() for l in h.lemmas()] + re.findall(r"[a-z]+", s.definition().lower())
    return [x.lower() for x in a if "_" not in x and x.lower() != w and len(x) > 2 and x.lower() not in FUNC]


def numberbatch(need):
    """векторы Numberbatch для слов вне словаря сайта (без кэша: кэш build_math не трогаем)"""
    got = {}
    with gzip.open(REPO / "data" / "raw" / "numberbatch-en-19.08.txt.gz", "rt", encoding="utf8") as f:
        next(f)
        for line in f:
            w, rest = line.split(" ", 1)
            if w in need:
                got[w] = np.array(rest.split(), dtype=np.float32)
                if len(got) == len(need):
                    break
    return got


def main():
    words = json.loads((OUT / "math.json").read_text(encoding="utf8"))["words"]
    index = {w: i for i, w in enumerate(words)}
    pos, lemma, stop, sx, pr, pl, pe = [], [], [], [], [], [], []
    for i, w in enumerate(words):
        sh = shares(w)
        pos.append("".join(str(min(9, round(sh[p] * 9))) for p in P) if sh else "")
        if w in FUNC or not sh:
            stop.append(i)
        elif sexed(w):
            sx.append(i)
        b = base(w, max(P, key=sh.get)) if sh else None
        lemma.append(index[b] if b and b in index else -1)
        if sh and i not in stop[-1:] and proper(w):
            pr.append(i)
        elif sh and max(P, key=sh.get) == "n" and base(w, "n") and w.endswith("s"):
            pl.append(i)
        if sh and i not in stop[-1:] and i not in pr[-1:] and person(w):
            pe.append(i)
    # базовая форма и метки; базы вне словаря — в extra
    IN = {}
    for i, w in enumerate(words):
        sh = shares(w)
        if sh and i not in stop and i not in pr and w.isalpha() and (f := infl(w, sh)):
            IN[i] = list(f)
    need = {b for b, _, _ in IN.values() if b not in index}
    nb = numberbatch(need)
    IN = {i: f for i, f in IN.items() if f[0] in index or f[0] in nb}
    ex = sorted(nb.keys() & {f[0] for f in IN.values()})
    exi = {w: len(words) + k for k, w in enumerate(ex)}
    E = np.stack([nb[w] / np.linalg.norm(nb[w]) for w in ex]) if ex else np.zeros((0, 300))
    # один смысл: базы и самостоятельные слова в своей части речи кода
    keys = {(f[0], f[1]) for f in IN.values()} | {(w, "oiae"[max(range(4), key=lambda j: int(pos[i][j]))]) for i, w in enumerate(words)
                                                  if pos[i] and i not in stop and i not in pr and i not in IN}
    XV = np.frombuffer((OUT / "vocab.bin").read_bytes(), dtype=np.int8).reshape(len(words), -1).astype(np.float32)
    XV /= np.linalg.norm(XV, axis=1, keepdims=True)
    vec = lambda a: XV[index[a]] if a in index else (E[exi[a] - len(words)] if a in exi else None)  # noqa: E731
    SE = {}
    for b, f in keys:
        s0 = homonym(b, "v" if (f == "a" and wn.synsets(b, "v") and not wn.synsets(b, "a")) else WNP[f], vec)
        if s0:
            A = sorted({index[a] if a in index else exi[a] for a in anchors(b, s0) if (a in index and index[a] not in stop and index[a] >= 300) or a in exi})  # без 300 самых частых (one, makes)
            if A:
                SE[f"{b}|{f}"] = A
    extra = {"words": ex, "vec": base64.b64encode(np.round(E * 127).astype(np.int8).tobytes()).decode(), "person": [exi[w] for w in ex if person(w)]}
    (OUT / "words.json").write_text(json.dumps({"pos": pos, "lemma": lemma, "stop": stop, "sexed": sx, "proper": pr, "plural": pl, "person": pe,
                                                "infl": {str(i): f for i, f in IN.items()}, "extra": extra, "sense": SE}, separators=(",", ":")), encoding="utf8")
    print(f"форм с базой {len(IN)} (баз вне словаря {len(ex)}), омонимов с одним смыслом {len(SE)}")
    print(f"слов {len(words)}, служебных {len(stop)}, со своей леммой в словаре {sum(x >= 0 for x in lemma)}, "
          f"с полом {len(sx)}, имён {len(pr)}, множественных {len(pl)}, людей {len(pe)}, words.json {(OUT / 'words.json').stat().st_size // 1024} КБ")


if __name__ == "__main__":
    main()
