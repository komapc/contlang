# Rethinking the language: where we are and what to change (2026-10)

## Update (2026-10-14): the “close” measure

The main measure is now different: the share of a blind reader's first answers that a blind judge (Haiku) considers “close”, the same semantic field (2 close, 1 near, 0 miss). The rank among 10,721 words below is the earlier measure, kept for the record.

- 1000 words ([big1000](../../data/eval/runs/big1000/result.txt)): the site encoder 24%, Haiku with ENC_SPEC 52%.
- Accepted (user's decision of 2026-10-14, without a blind test): the site encoder always encodes the base form and appends labels (`discussed` → the code of discuss + `T-2`, `-ing` → `A0`, an attributive participle → `| a V-4`, plural → `N+3`, degrees → `C+3`/`C+5`); bases outside the dictionary are taken from Numberbatch; for a homonym, one sense is encoded (WordNet; at almost equal frequency, the one nearest the word's vector). `scripts/site/build_words.py` → infl, extra, sense. Corrections of 2026-10-14: the part of speech of a word form follows Brown if the form occurs there ≥ 5 times and Brown sees a noun or an attribute (attacks, plans, projects, tears → noun, surprising → attribute; 157 forms); sense anchors without hypernyms (reverse reading: word first 29.9 → 32.1%).
- Accepted: the axes of 8 roots (LONG, KNOW, MEASURE, TOUCH, NEAR, GIVE, VALUE, CARE) from the words around the learned atoms, and the role `agent` for people ([fix1](../../data/eval/runs/fix1/README.md)).
- Blind tests of the encoder (not accepted): choosing the code by the reader model ([reader2](../../data/eval/runs/reader2/README.md), +4.7% [−4.0 … +13.3]), an economical encoder with fewer roots and no zeros ([occam](../../data/eval/runs/occam/README.md), −1.3% [−8.0 … +5.3]).
- Not accepted: separate codes for the senses of polysemous words ([senses](../../data/eval/runs/senses/README.md), −2%), the root KIND ([kind](../../data/eval/runs/kind/README.md), +5.6% at the threshold; as a head only +6.7% [−2.7 … +16], [side_kind](../../data/eval/runs/side_kind/README.md); user's decision of 2026-10-14), the roles `tool` and `quality` by WordNet.
- Postponed: removing the PI pair from the site encoder.

## The measure and the benchmark (earlier)

Reading accuracy is measured by the rank of the target word among the 10,721 words of the site dictionary: the words are ordered by cos with a blind reader's answer, and 1 means the answer is closest to the target.
The geometric mean of ranks is taken over 200 readings: 100 dev words, two Haiku readers each.
Details: [data/eval/runs/toki](../../data/eval/runs/toki/README.md).

**A measure for “10 times more accurate”.** Rank with synonyms: any word from the WordNet synsets of the target word in its part of speech counts as a hit (*car* instead of *automobile* is rank 1). The geometric mean of this rank is how many equally likely candidates the reader has left; log2 of the rank is the remaining uncertainty in bits.
“10 times more accurate” = 10 times fewer candidates = 3.3 bits less.

| who encodes | rank | rank with synonyms | bits | 1 − cos | outside the top 10 (of 200, with synonyms) |
|---|--:|--:|--:|--:|--:|
| Toki Pona | 120 | 62 | 5.9 | 0.68 | 142 |
| min-co | 51 | 25 | 4.7 | 0.58 | 121 |
| min-co v2 | 61 | 28 | 4.8 | 0.59 | 119 |
| site math | 137 | 82 | 6.4 | 0.71 | 156 |

- For now min-co is 2.5 times more accurate than Toki Pona (by 1.2 bits). The 10× goal is a rank with synonyms of about 6.
- Why not other measures:
  - 1 − cos is compressed from above and below: a 10 times smaller error is cos 0.93, almost exact words only; the difference between Toki Pona and min-co on it is 0.68 against 0.58.
  - the share of misses (outside the top 10 with synonyms): 142 against 121 of 200 hardly distinguishes the languages, and 10× (14 misses of 200) would mean almost error-free reading.
  - rank without synonyms penalizes *car* instead of *automobile*: synonyms share one rank, and the reader is not at fault.

| who encodes | rank of the first answer (95%) | best of three | exactly first of 200 |
|---|--:|--:|--:|
| Toki Pona, Haiku | 120 (76–188) | 51 | 21 |
| min-co, Haiku | 51 (30–84) | 21 | 44 |
| min-co v2, Haiku | 61 | 22 | 39 |
| min-co, site math* | 137 (88–214) | 61 | 14 |

- For now min-co is 2.4 times more accurate than Toki Pona.
  - The gap differs by part of speech: adjectives 27 against 209, adverbs 52 against 210, verbs 173 against 373, nouns 34 against 44.
- The main losses:
  - verbs;
  - verbal and institutional nouns: *installation, nomination, fee, municipality*.
- The site math's codes are no better than Toki Pona.
- A caveat: Haiku knows Toki Pona from training, and min-co only from the specification.
- \* The math codes were made before the two-sided MANY and the level limits. ① hardly changed from these edits.

## Proposals

| # | proposal | basis | what it removes | status |
|---|---|---|---|---|
| 1 | A short specification v2 ([spec_v2.md](../../data/eval/runs/toki/spec_v2.md), 4.8 KB instead of 11 KB) | Blind test on the same 100 words: v2 / v1 = 1.19 (95%: 0.76–1.87), no difference | The fourth root ABSTRACT, the exception for cardinal directions, BIG as “degree”, the old `-o` notation, three different descriptions of labels. One rule for axes: −5 the opposite pole, 0 the middle, +5 the full pole | accepted (2026-10) |
| 2 | Roles in the form instead of the DO and HAPPEN axes: `agent`, `tool`, `result`, `quality` after `\| o` (like *-ist, -il, -aĵ, -ec* in Esperanto) | Part of v2. The coder used them in 10 words of 100: telegraph 18 → 2, but beef 1 → 114 (`result` out of place) | Two axes that are not scales (actor … action … tool; cause … consequence) | accepted with v2; since 2026-10 the site encoder gives `agent` to people (noun.person in WordNet): +19% “close” [+10 … +30], [fix1](../../data/eval/runs/fix1/README.md) |
| 3 | A list of frequent words with fixed codes (about 1000, from verified recipes). Composition for the rest | The best of three answers is already at rank 21: the needed word is usually among the options but does not come first. A fixed word is read exactly (the site's recipes) | — | the only lever toward 10× that I see; it changes the principle “there is no fixed vocabulary”; not checked on these 100 words (how many of them would make the list was not counted) |
| 4 | Measure on sentences, not words | [toki_sents](../../data/eval/runs/toki_sents/README.md): the same 100 words in sentences. Toki Pona 62 → 26, min-co 28 → 40. Toki Pona / min-co = 0.65 (0.36–1.17), no difference. Context helps polysemous Toki Pona. min-co in a sentence encodes the word more coarsely, and the reader does not complete the code from the meaning | — | done: min-co's advantage on words disappeared in text |
| 5 | Site encoder: choose the roots that models use (a prior over the corpus of model codes, kNN), not only y ≈ x | Math 137 against 51 for the model; fitting the dictionary did not move ② ([anchor](../../data/eval/runs/anchor/README.md)) | — | checked: moving model codes into the dictionary ([distill](../../data/eval/runs/distill/README.md)) reads almost as before, not accepted |
| 6 | CARE is the attitude to work, TONE replaced by FRIEND (enemy … friend) | For math the roots moved apart: cos of the centers 0.65 → 0.12 (learned dictionary 0.07). Blind test on 20 words ([friend](../../data/eval/runs/friend/README.md)): FRIEND / TONE 1.45 (0.71–3.01), no difference; *friend* better, *polite* worse | Two roots with close centers | accepted (2026-10) |
| 7 | Do not remove rare roots: NEAR, WANT, BEGIN, SEX, FEEL, CHANGE, MEASURE (4–8 times in 458 codes) | Each carries its own words (king, improve, unit…) | — | keep |
| 8 | The labels I, C, N hardly occur on words (2, 1, 1 times) | They cannot be tested on words | — | decide after the test on sentences |
| 9 | One quotes rule: proper names, digits, scientific names of species and substances | Part of v2 | The category lists in encoding.md | accepted with v2 |
| 10 | A verb with a head root with a value = transition into that state (`BIG(=+3) \| i` grow, `LIVE(=-5) \| i K+3` kill), without `CHANGE` | [verbs](../../data/eval/runs/verbs/README.md): 40 verbs, B / A = 0.89 (0.67–1.19), no difference. Better *learn, forget*, worse *weaken, accelerate* | `CHANGE` in verbs of change of state | not accepted: no difference |
| 11 | New roots from the worst words: light (dark … bright), strength (weak … strong), humidity (dry … wet), openness, fullness; clothing, help, electricity, word/name | The verbs *darken, brighten, weaken, strengthen, dry, open, close, fill, empty* are bad in both variants (rank 50–1800): the meaning has no axis. Words from the Toki Pona test *suit, assistant, current, note, sentence* | — | candidates: need clusters and a blind test |

[encoding.md](encoding.md) was rewritten in the v2 notation: roles instead of `DO(=+5)` and `HAPPEN(=±n)`, without ABSTRACT and four-root cardinal directions. Recipes converted to roles were not checked separately.

## Open questions

- ~~Is the particle `LI` needed if the verb is already marked `| i`.~~ Removed (2026-10-14): the predicate is the word with `| i`.
- Anatomy and medicine: Latin in quotes or roots.
- Pronouns and kinship.
- The sounds of roots and the notation of values ([phonology](phonology.md)).
- A check in Russian.

Earlier plans and questions (in Russian): [history/plan.md](../history/plan.md), [history/roadmap.md](../history/roadmap.md).
