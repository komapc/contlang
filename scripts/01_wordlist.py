"""Build a word list: common WordNet lemmas (ranked by SemCor sense counts) present in GloVe.

POS is only recorded for later analysis; it is not used to split the data.
"""
from collections import Counter

from common import ROOT, load_glove, load_wordnet

QUOTA = {"noun": 200, "verb": 200, "adj": 120, "adv": 80}
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

wn = load_wordnet()
kv = load_glove()
vocab = set(kv.index_to_key[:60000])

best = {}  # word -> (count, pos); keep the dominant POS
total = Counter()
for pos in "nvar":
    for name in wn.all_lemma_names(pos):
        if not name.isalpha() or len(name) < 3 or name in STOP or name not in vocab:
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

out = ROOT / "data" / "wordlist_en.tsv"
with open(out, "w") as f:
    f.write("word\tpos\tpos_share\n")
    for w, p, share in rows:
        f.write(f"{w}\t{p}\t{share:.2f}\n")
print(len(rows), "words ->", out.relative_to(ROOT), dict(taken))
