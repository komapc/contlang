"""POS-specific entries and sense vectors for homographs.

Each word of the list gets one entry per POS whose SemCor share is >= MIN_SHARE (the dominant POS
always). Words with several entries get vector = unit(W_WORD * word vector + (1 - W_WORD) * sense
vector of that POS); the sense vector is built from the WordNet synsets of that (word, POS):
lemmas, hypernym lemmas and content words of the gloss, looked up in Numberbatch.
Words with one entry keep their plain Numberbatch vector.
Writes data/wordlist_en_sense.tsv (word, pos, share, generality) and data/raw/sense_numberbatch.npy.
"""
import re
from collections import Counter

import numpy as np

from common import RAW, ROOT, load_vectors, load_wordnet
from lib_axes import generality, unit

MIN_SHARE = 0.2
W_WORD = 0.2
TAG = {"n": "noun", "v": "verb", "a": "adj", "r": "adv"}
STOP = set("""that which with from this have having been being were their there then than into onto
such other about over under some most more very also when where what who whom whose while without
within used using often usually something someone somebody especially esp like make made makes
having particular certain any each every between through during before after above below""".split())

wn = load_wordnet()
kv = load_vectors("numberbatch")
vocab = kv.key_to_index

base = [l.rstrip("\n").split("\t") for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
base_words = [r[0] for r in base]
base_pos = np.array([r[1] for r in base])
base_gen = generality(base_words, base_pos, RAW / "generality_x5.npy")
gen_of = {(w, p): g for w, p, g in zip(base_words, base_pos, base_gen)}


# Vectors are centered on the mean of the list words first: otherwise averaging many words
# pulls every sense towards the common centre and all senses look alike.
_base = [l.split("\t")[0] for l in open(ROOT / "data" / "wordlist_en_x5.tsv").read().splitlines()[1:]]
MU = unit(np.stack([kv[w] for w in _base])).mean(axis=0)


def cvec(w):
    return unit((kv[w] - MU)[None])[0]


def lemma_vec(name):
    name = name.lower()
    return cvec(name) if name in vocab else None


def synset_vec(s):
    acc, tot = np.zeros(kv.vector_size), 0.0
    for l in s.lemmas():
        v = lemma_vec(l.name())
        if v is not None:
            acc += v; tot += 1.0
    for h in s.hypernyms():
        for l in h.lemmas()[:2]:
            v = lemma_vec(l.name())
            if v is not None:
                acc += 0.5 * v; tot += 0.5
    for w in set(re.findall(r"[a-z]+", s.definition().lower())):
        if len(w) >= 4 and w not in STOP and w in vocab:
            acc += 0.3 * cvec(w); tot += 0.3
    return acc / tot if tot else None


def sense_vec(word, pos_letter):
    acc, tot = np.zeros(kv.vector_size), 0.0
    for s in wn.synsets(word, pos_letter):
        v = synset_vec(s)
        if v is None:
            continue
        w = 1 + sum(l.count() for l in s.lemmas() if l.name().lower() == word)
        acc += w * v; tot += w
    return unit((acc / tot)[None])[0] if tot else None


entries = []
for w, dom in zip(base_words, base_pos):
    c = Counter()
    for syn in wn.synsets(w):
        p = "a" if syn.pos() == "s" else syn.pos()
        for l in syn.lemmas():
            if l.name().lower() == w:
                c[TAG[p]] += l.count() + 1
    tot = sum(c.values())
    keep = [p for p, v in c.items() if v / tot >= MIN_SHARE or p == dom]
    for p in keep:
        entries.append((w, p, c[p] / tot, len(keep)))

inv = {v: k for k, v in TAG.items()}
vecs, rows, report = [], [], []
SV = {}
for w, p, share, nkeep in entries:
    wv = cvec(w)
    if nkeep > 1:
        sv = sense_vec(w, inv[p])
        SV[(w, p)] = (wv, sv)
        v = unit((W_WORD * wv + (1 - W_WORD) * sv)[None])[0] if sv is not None else wv
    else:
        v = wv
    vecs.append(v)
    if (w, p) in gen_of:
        g = gen_of[(w, p)]
    else:
        syns = wn.synsets(w, inv[p]) if p in ("noun", "verb") else []
        g = len(set(syns[0].closure(lambda s: s.hyponyms()))) if syns else 0
    rows.append((w, p, share, g))



def linked(w, p, q):
    """WordNet derivational link between the word as POS p and the same word as POS q."""
    for syn in wn.synsets(w, inv[p]):
        for l in syn.lemmas():
            if l.name().lower() != w:
                continue
            for rl in l.derivationally_related_forms():
                if rl.name().lower() == w and ("a" if rl.synset().pos() == "s" else rl.synset().pos()) == inv[q]:
                    return True
    return False


conv = []
for i, (w, p, _, _) in enumerate(rows):
    same = [(q, j) for j, (ww, q, _, _) in enumerate(rows) if ww == w]
    comp = sorted({q for q, _ in same if q == p or linked(w, p, q) or linked(w, q, p)})
    conv.append(w + "#" + "".join(c[0] for c in comp))   # entries linked to each other share an id

with open(ROOT / "data" / "wordlist_en_sense.tsv", "w") as f:
    f.write("word\tpos\tshare\tgenerality\tconv\n")
    for (w, p, sh, g), c in zip(rows, conv):
        f.write(f"{w}\t{p}\t{sh:.2f}\t{int(g)}\t{c}\n")
np.save(RAW / "sense_numberbatch.npy", np.stack(vecs).astype(np.float32))

print(len(base_words), "words ->", len(rows), "entries;",
      sum(1 for e in entries if e[3] > 1) , "entries belong to multi-POS words")
idx = {(w, p): i for i, (w, p, _, _) in enumerate(rows)}
print("cosine between POS entries of the same word (high = conversion, low = homonym):")
for w in ["work", "play", "run", "love", "march", "rent", "issue", "point", "order", "close",
          "left", "mean", "well", "pretty"]:
    ps = [p for (ww, p) in idx if ww == w]
    cs = [f"{a}/{b}: {float(np.dot(vecs[idx[(w, a)]], vecs[idx[(w, b)]])):.2f}"
          for i, a in enumerate(ps) for b in ps[i + 1:]]
    print(f"  {w}: {', '.join(cs) if cs else '(одна запись)'}")

print("diagnostics: cos(sense_a, sense_b) | cos(word, sense_a) | cos(word, sense_b)")
for w in ["march", "close", "work", "issue", "rent", "point", "order"]:
    ps = [p for (ww, p) in SV if ww == w]
    if len(ps) >= 2:
        a, b = ps[:2]
        (wv, sa), (_, sb) = SV[(w, a)], SV[(w, b)]
        print(f"  {w} {a}/{b}: {float(sa @ sb):.2f} | {float(wv @ sa):.2f} | {float(wv @ sb):.2f}")
from nltk.corpus import wordnet as _wn
for w, pl in [("march", "n"), ("close", "v"), ("close", "a")]:
    print(w, pl, [s.name() + ":" + s.definition()[:40] for s in _wn.synsets(w, pl)[:6]])
