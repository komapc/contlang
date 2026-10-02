"""Build a word list: common WordNet lemmas (ranked by SemCor sense counts) present in GloVe.

POS is only recorded for later analysis; it is not used to split the data.
"""
import sys
from collections import Counter

from common import ROOT, load_vectors, load_wordnet

# usage: python 01_wordlist.py [scale]   scale=1 -> 600 words, 5 -> 3000 words
SCALE = int(sys.argv[1]) if len(sys.argv) > 1 else 1
QUOTA = {"noun": 200 * SCALE, "verb": 200 * SCALE, "adj": 120 * SCALE, "adv": 80 * SCALE}
POS_TAGS = {"n": "noun", "v": "verb", "a": "adj", "r": "adv"}
# closed-class and auxiliary words that WordNet happens to list
STOP = set("""
the and but not who whom whose which what when where why how this that these those
will would can could shall should may might must have has had been being was were are
also more most much many some any all each every other another such only just very
too than then there here still even ever never ago yet once thus however per via
one two three four five six seven eight nine ten first second third last next
said say says like make get got let put take took
""".split())

# relaxations (docs/lexicon.md): colors, months, weekdays, numbers, countries are outside the 30 roots
EXCL_HYPER = {"chromatic_color.n.01", "achromatic_color.n.01", "color.n.01", "calendar_month.n.01",
              "day_of_the_week.n.01", "country.n.02", "state.n.04", "integer.n.01", "large_integer.n.01",
              "digit.n.01", "cardinal.n.01", "ordinal.n.01"}
EXCL_WORDS = set("""zero eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty
thirty forty fifty sixty seventy eighty ninety hundred thousand million billion dozen
black white red blue green yellow orange purple pink brown gray grey""".split())


EXCL_RELIGION = {"religion.n.01", "religious_person.n.01", "religionist.n.01", "christian.n.01", "adherent.n.01"}


def _is_place(s):
    return any(h.name() in ("country.n.02", "city.n.01", "state.n.01", "continent.n.01") or "country" in h.name()
               for h in s.instance_hypernyms())


def relaxed(wn, name):
    if name in EXCL_WORDS:
        return True
    # nationality / place-derived words (american, mexican, european)
    for s in wn.synsets(name):
        for l in s.lemmas():
            if l.name().lower() != name:
                continue
            for r in l.pertainyms() + l.derivationally_related_forms():
                if _is_place(r.synset()):
                    return True
    for s in wn.synsets(name):
        if s.name().startswith(name + ".") and (EXCL_HYPER | EXCL_RELIGION) & ({h.name() for h in s.closure(lambda x: x.hypernyms())}):
            return True
    return False


wn = load_wordnet()
# words must exist in both embedding spaces so the sources can be compared
vocab = set(load_vectors("glove100").index_to_key[:100000])
vocab &= set(load_vectors("numberbatch").index_to_key)

best = {}  # word -> (count, pos); keep the dominant POS
total = Counter()
for pos in "nvar":
    for name in wn.all_lemma_names(pos):
        if not name.isalpha() or len(name) < 3 or name in STOP or name not in vocab or relaxed(wn, name):
            continue
        if any(wn.morphy(name, p) not in (None, name) for p in "nvar"):
            continue  # inflected form
        syns = wn.synsets(name, pos)
        if all(s.instance_hypernyms() for s in syns):
            continue  # proper noun
        count = sum(l.count() for s in syns for l in s.lemmas() if l.name().lower() == name)
        total[name] += count
        if name not in best or count > best[name][0]:
            best[name] = (count, POS_TAGS[pos])

rows, taken = [], Counter()
for name, (count, pos) in sorted(best.items(), key=lambda kv_: -kv_[1][0]):
    if taken[pos] < QUOTA[pos]:
        taken[pos] += 1
        rows.append((name, pos, count / max(total[name], 1)))

out = ROOT / "data" / ("wordlist_en.tsv" if SCALE == 1 else f"wordlist_en_x{SCALE}.tsv")
with open(out, "w") as f:
    f.write("word\tpos\tpos_share\n")
    for w, p, share in rows:
        f.write(f"{w}\t{p}\t{share:.2f}\n")
print(len(rows), "words ->", out.relative_to(ROOT), dict(taken))
