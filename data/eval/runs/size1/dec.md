# Pre-registration (2026-11-12, before any code is written): size1 — lexicon size vs accuracy, by phrase limit

**Question.** The user asked for three lines on the size chart: a concept written in 1 word, in up to 2 words, in up to 3
words — for min-co and Toki Pona. [size0](../size0/README.md) mixed runs and judges and had no Toki Pona breakdown.

**Words.** 120 content lemmas from Brown (dominant tag noun / verb / adjective, WordNet sense whose lemma is the word,
no plural doubles, not in func1), 30 at random (seed 20261112) from each frequency band: ranks 1–300, 301–1000,
1001–3000, 3001–10000 ([items.json](items.json)). The encoder gets the word, its part of speech and the WordNet gloss.

**Languages.**
- **mc** — min-co v2b (51 roots, 82 units), the "Two words" section replaced by [Phrases](tasks/phrases.md): one word or
  up to 3 words joined by FROM / FOR / AGAINST / LIKE / PI; **no quotes at all** (func1 confound).
- **tp** — Toki Pona (pu, 120 words), written by the encoder in Toki Pona and **read in cipher** (tpx1 cipher): the reader
  sees only the ciphered dictionary. Every word counts, `pi` included.

**Variants** (both languages): k1 — exactly 1 word; k2 — at most 2 words; k3 — at most 3 words. The same encoder writes all
three for a word ([write_mc](tasks/write_mc.md), [write_tp](tasks/write_tp.md)); 2 Sonnet encoders per language, 60 words each.

**Reading.** Per language 3 Latin-square lists: list s has word i in variant (i + s) mod 3 + 1, so no reader sees two
variants of one word; 2 Haiku readers per list (12 readers). First answer of each reader is judged.
**Judging.** 3 Sonnet judges, each gets 2/3 of the 720 answers (every answer judged twice), word scale 0 off / 1 related /
2 close ([judge.md](tasks/judge.md)). Agents: 4 + 12 + 3 = 19. Script: [run.py](run.py).

**Measures** (paired bootstrap over words, 5000, seed 0):
- main: close rate per language and k; k2 − k1, k3 − k1, k3 − k2 per language; tp − mc per k;
- descriptive: close by frequency band; words per code; judge agreement;
- curve: U(N) = share of Brown content-word tokens read close with a lexicon of the N most frequent lemmas (entries read
  right with a_lex = 0.9, ceiling 1.0; other words at the measured band accuracy; ranks above 10 000 use the last band);
  L = 82 + N for mc, 120 + N for tp. Six lines on one chart: the three limits × two languages.

**Decision (in advance):**
- mc k3 − k1 ≥ +10 pp, interval above 0 → allow phrases of up to 3 words in 2.0;
- mc k3 − k2 interval includes 0 while k2 − k1 is above 0 → keep the current limit of 2 words;
- all mc intervals include 0 → the phrase limit does not matter for reading; choose it by learnability (shorter).
The curve is a model; lexicon decisions stay with the user.

**Claude's forecast:** mc k1 ≈ 50 %, k2 ≈ 56 %, k3 ≈ 58 %; tp k1 ≈ 25 %, k2 ≈ 38 %, k3 ≈ 43 %; Toki Pona gains more
from extra words than min-co (its single words are broad); mc beats tp at every k, gap shrinking with k.
