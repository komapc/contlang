# Mathematical encoding: setup, metrics, results

The goal: to check whether a word can be translated into a min-co code **without a language model**, with one matrix and simple brute force, and to use the same math to check axes and to look for missing roots. This is a report on the logic and results; the scripts are `scripts/17_sparse_code.py`, `18_sparse_learn.py`, `19_math_codes.py`, the shared part `scripts/lib_code.py`.

## 1. Setup

A word is a unit vector x in the space S₁ (Numberbatch, 300 dimensions). A code is at most m roots (for us m = 3), each root with an integer level v ∈ {−5 … +5}, roots without an axis have no level. The value `=0` is the middle of the axis, not the absence of the root.

The decoder is linear:

```
y = Σⱼ wⱼ · ( c_{rⱼ} + (s/5) · vⱼ · a_{rⱼ} )
```

- c_r is the **center** of the root (the mean of its pole words: “what the axis is about”), a_r is the **axis** (the mean of the + pole minus the mean of the − pole, as in SemAxis);
- s is the common axis scale (fitted: s = 2);
- wⱼ is the position weight: the head root 1, the others w (for us 0.6; this accounts for the rule “the head first” from [model.md](model.md)).

The encoder is an exact search: from the 8 roots with the best correlation with x, it tries all supports of up to three roots, all combinations of levels, and the choice of head root; the objective is the maximum of cos(x, y). This is the **best m-term approximation over a dictionary with integer coefficients** (sparse approximation; with “center + axis” groups, group sparsity). The discrete variant is close to sparse superposition codes (Barron, Joseph); dictionary learning is close to K-SVD and the k-sparse autoencoder. What differs from all of these is that **the atoms are named and must stay recognizable**: that is the price of readability.

Dictionary learning (the λ term of the setup): with the codes fixed, the root directions are fitted by ridge regression with attraction to the original ones (from the poles) with weight λ, the atoms are normalized, and if they have moved further than cos < 0.85 from the original, they are brought back along the arc to 0.85; then the words are encoded again (3 iterations). We train on 70% of the words, and all numbers are on the held-out 30%.

## 2. Data

- Space: Numberbatch 19.08 (ConceptNet), English.
- Words: `data/wordlist_en_x5.tsv`, 3000 frequent words (1000 nouns, 1000 verbs, 600 adjectives, 400 adverbs). After excluding pole words, about 2700.
- Axis poles: `roots.yaml`, the `semaxis` field (5–9 words per pole); roots without an axis have short lists in `lib_code.NOAXIS`.

What else would fit (not used): fastText with language alignment (Russian-English lacunae), LMMS / SensEmbed sense vectors (polysemy), human ratings on scales: Glasgow Norms (size, valence, concreteness…), Warriner VAD, Brysbaert concreteness, Lancaster sensorimotor, for external validation of the axes.

## 3. Metrics, and why four

Recognition: the rank of the real word among all dictionary words by cos(y, word). Always together:

| metric | what it means |
| :-- | :-- |
| top1 / top10 / top50 | exact recognition in a closed dictionary |
| cos(x, y) | how similar the decoded vector is to the word's meaning |
| “miss similarity” | the average closeness of a wrong guess to the real word: a near miss is better than a far one |

top1 alone is not enough: **a random matrix of the same shape gives top1 63% at cos(x, y) 0.22**, while the roots give 21% at 0.43. A random code works like a hash: the decoded point goes off into an empty place in the space, where the nearest word happens to be the right one, and the code carries no meaning. A rise in top1 with a fall in cos is hashing, not progress.

The final check is not math but a **blind round-trip test** with a language model (the coder sees the specification, the decoder only the tables and reading rules), as in all `data/translation_test/roundtrip_*.md`.

## 4. Traps found

1. **Pole leakage.** Pole words must be left neither in the test nor among the candidates: a code that lands in the middle of a pole “recognizes” the pole word itself (*river* decoded to *milk* because *milk* was in the liquid pole). With the exclusion, top1 grew from 3% to 21% with the same roots.
2. **The hash effect** (above): cos(x, y) is needed next to top1.
3. **An axis with a middle and two poles.** For axes of the form −5 … 0 … +5, SemAxis takes only the extreme poles; if words of the middle are written into the −5 pole, the axis shifts. This was the case with GRAIN (the −5 pole was “sand, flour”, which is 0) and PART (+5 was “whole”, which is +2). Fixed; the check is the nearest words to each pole.
4. **Topical poles.** A pole drags a topic along with it if its words come from one area: a liquid pole of drinks pulled toward *liquor, bottle*, soft toward *sweet, lovely*, cheap toward *stupid*. Poles should be chosen from words that share only the property of the axis.

## 5. Results (held-out words, m = 3)

A dictionary of 44 roots (`TEXT`, axes on `FIGHT` and `DO`, `MATTER` merged into `GRAIN`, `PARTICULAR` into `SAME`, the poles of `RULE` are law and authority instead of agencies, see section 6). Before the change of the `RULE` poles, the top1 of the three rows was 20.8 / 22.8 / 28.5%. For comparison, the top1 of the three rows and cos: 45 roots 19.0 / 21.7 / 26.0% and 0.425 / 0.432 / 0.487; 46 roots 21.8 / 24.0 / 28.7% and 0.432 / 0.440 / 0.495. Minus two roots costs about a percent; the set of words is slightly different each time (poles are excluded), so the comparison is approximate.

| dictionary | top1 | top10 | top50 | cos(x,y) | miss similarity |
| :-- | --: | --: | --: | --: | --: |
| roots from poles, order does not matter | 21.3% | 73.5% | 97.0% | 0.431 | 0.290 |
| the same, head root first (weight of the others 0.6) | 23.8% | 74.5% | 96.9% | 0.439 | 0.291 |
| learned roots (λ = 30, cos with the original ≥ 0.85) | 25.6% | 80.6% | 98.8% | 0.494 | 0.367 |
| for comparison: a random matrix | 63% | 96% | 99.9% | 0.22 | 0.22 |

The closeness of a word to its real nearest neighbor is 0.62 on average, to a random word 0.03.

Conclusions:

- **Discreteness is almost free**: 11 and 5 levels give the same result, 3 levels lose about a percent. The main limit is the number of roots m: m = 1 → 2 → 3 → 5 gives top50 64 → 87 → 96 → 99.8%.
- **A sum of roots gives a region of meaning, not a word**: 95–98% of words are in the top50, but discrimination within a region is weak.
- **Dictionary learning helps** (top1 +2…7 in different runs, top10 +6, cos +0.06, misses noticeably closer), and the roots stay recognizable by their nearest words (`data/sparse_learn.md`, the “before / after” table). Without the constraint cos ≥ 0.85 the roots drift and begin to serve as “slots” for frequent groups of words: MANY → *generally, really*, SOMEONE → *anyway, maybe*, BEGIN+ → the ordinals *fourth, ninth*, SIDE+ → cardinal directions, SEX+ → professions. This is both harm and a hint at what is missing.
- Centering the space (subtracting the mean vector) gives top50 98% against 95%, but lower cos; it was not taken into the main scheme.

## 6. Lacunae

The calculation is on the 45-root dictionary (before the candidates). Words with the worst reconstruction (the bottom 35% by cos), with the residuals x − proj(x onto y) clustered (k-means, 25 clusters). The clusters are topical areas: texts and publications, politics, courts, sport, finance, plots and film, business, school, army, weapons, medicine, religion, transport, work. Most of them are institutions and terms that by the rules of the language go in quotes. Candidates understandable to a human (the rule: first an axis on a root without an axis):

| candidate | cluster | cluster's top10 without → with |
| :-- | :-- | :-- |
| an axis on BODY: −5 illness … +5 health | medicine (disease, patient, hospital, doctor…) | 7% → 43% |
| an axis on FIGHT: −5 game, sport … +5 war | sport; army and weapons | 18% → 64%; 55% → 73% |
| a new root TEXT (written language) | texts (article, newspaper, page, book…) | 21% → 71% |

**Without a limit on the number of roots** ([lacunae.md](../../data/lacunae.md), `scripts/20_lacunae.py`). The encoder greedily adds roots (median 8). A hit counts if among the 10 nearest of the 10,000 frequent words there is a word with the same stem. The result: 87% of ordinary words from the list of 3000 frequent words and 63% of all words. The second pass takes ordinary words more broadly: all common nouns of the 10,000, with proper names filtered out by the Brown corpus tagging. That is 7128 words, of which 77.5% are in the top10, 1605 misses in 40 clusters ([lacunae.md](../../data/lacunae.md)).

The first finding is the poles of `RULE`. The earlier poles were words for agencies (*authority, committee, agency, commission, government*), and any code with `RULE` unfolded into *commissions, agencies*. Because of this, state, court, bank, school and elections merged: these institutions reached the top10 in 6% of cases. The new poles are law and authority (*law, official, authority, formal, legal, govern, rule* against *personal, private, informal, individual, unofficial*): now 32%, with the overall result unchanged. The meaning of the axis is the same; only the words for SemAxis changed.

The second finding is units of time and parts of the day. Recipes appeared for them, checked by a blind test ([roundtrip_time](../../data/translation_test/roundtrip_time.md)): 24 of 24 with recipes against 13 and 12 of 24 without them. The recipes are in [encoding.md](encoding.md), section “Time”. The misses among all words are mostly names, countries and titles, which go in quotes. Among ordinary words there are 270 misses, which gather into areas:

- morality and society;
- illness and medicine;
- religion;
- elections and politics;
- trade;
- school;
- security;
- courts;
- cardinal directions;
- flight;
- time of day and calendar;
- celestial bodies;
- the press;
- credit;
- police;
- connectors (*moreover*);
- the city;
- ordinal numbers;
- weapons.

On all test words the gain is small (top10 72.5% → 74.8%): the candidates cover their areas and do not interfere with the rest. The same roots arose by themselves in early automatic runs (DISEASE, WRITER, AUTHOR, COMPETE in [lexicon.md](lexicon.md)). The blind test is in section 7.

## 7. Blind tests

Math only proposes; the blind round-trip test decides (the coder and decoder are models, and the decoder does not see the originals).

**Candidates** ([roundtrip_candidates.md](../../data/translation_test/roundtrip_candidates.md), 36 words, 12 from each candidate's area; exact / among three):

| area | without candidates | with candidates | decision |
| :-- | :-- | :-- | :-- |
| BODY, health axis | 15 / 20 of 24 | 19 / 22 of 24 | not added: health is already expressed through `LIVE`, `GOOD` |
| FIGHT, axis game … war | 11 / 15 of 24 | 17 / 21 of 24 | **added** |
| TEXT, new root | 3 / 5 of 24 | 15 / 17 of 23 | **added** |

Then the surplus was removed ([roundtrip_merge.md](../../data/translation_test/roundtrip_merge.md), the similarity of axes and centers is a hint from the math): `MATTER` merged into `GRAIN` (11 → 17 of 24), `PARTICULAR` into `SAME` (13 → 12), tools as an axis on `DO` (17 of 24 against 13 with the label `U`). The total is 44 roots.

**Codes of the math encoder** ([roundtrip_math.md](../../data/translation_test/roundtrip_math.md), 24 words): roots from poles 1 of 24 exactly, learned dictionary 3 of 24 (4 among three). For comparison, the model coder on the same tools: 1 of 24 without the label `U` and 13 of 24 with it. A math code lands in the region of meaning but takes roots a human would not use to describe the word (*saw* → `SEE TIME(=-4)`: the vector is mixed with the past tense of *see*; `ABSTRACT`, `PARTICULAR` as filler).

The conclusion: math is a **tool for analyzing the language** (finding lacunae, checking poles, comparing axis variants in seconds, without a model), not a translator. A high top50 in the space does not mean readability by a human.

## 8. The “blend” decoder

The “nearest words to the sum of roots” decoder hardly ever returns the word: the winners are hub words close to any code (*things, someone, matters*). The “blend” decoder scores each word as follows:

```
mix = ½ · z(2·cos(word, y) − hub(word)) + ½ · Conj,   Conj = −log Σⱼ exp(−2·zⱼ) / 2
```

- the first term is CSLS: the word's hubness is subtracted from its closeness to the code (the mean cos with the 10 nearest of 3000 random codes);
- Conj is a soft minimum of the z-scores of the word's closeness to each root separately: the word must fit all the roots, not their sum;
- z is normalization over the whole dictionary.

On the math's own codes (2000 random words of the site dictionary, without poles and proper names, `scripts/experiments/decoder/site_eval.py`):

| dictionary | decoder | top1 | top3 | top10 | cos of the first guess with the word (median) |
| :-- | :-- | --: | --: | --: | --: |
| from poles | sum | 1.4% | 5.2% | 24.3% | 0.26 |
| from poles | blend | 45.5% | 70.0% | 90.8% | 0.83 |
| learned | sum | 6.8% | 19.1% | 44.3% | 0.30 |
| learned | blend | **50.7%** | 75.1% | 93.0% | 1.00 |

This is not the hash effect from section 3: with hashing top1 grows while the misses are far. Here the first guess is close to the word (median cos 0.83–1.00 against 0.26–0.30 for the sum), and guesses with cos < 0.3 are three times fewer. The other experiments (4 roots, an encoder checked by the decoder, a word pair, root order, the root SPIRIT) are in [decoder_experiments.md](../../data/decoder_experiments.md).

## 9. On the site

On the “Try it” page ([minco.lipu.dev](https://minco.lipu.dev/)), next to the language model, the same encoder runs, ported to JavaScript (`site/math.js`, the codes and word ranks match Python on the check words), with the learned dictionary: the word's code, the words the “blend” decoder puts first, the rank of the source word among 10,721 words (the 10,000 frequent ones and the whole list of 3000) and the 10 roots that best describe the word individually. It also reads a code produced by the model. The data is `scripts/site/build_math.py`.

**New roots are trained further, old atoms are frozen** (since 2026-10, LAND). `scripts/18_sparse_learn.py` by default takes atoms from `data/sparse_dict_learned.npz` as they are and trains only the roots of roots.yaml that are not there (the same setup, but only their rows are solved), so the codes of words without new roots do not change. Full retraining is `--full`: on 47 roots it shifted the old atoms and spoiled codes without new roots (−8% “close”, [adopt2](../../data/eval/runs/adopt2/README.md)). If a root's center is not the middle of the poles, the center's words are written in roots.yaml in the field `center` (for LAND: *land, country, region, territory, landscape, shore*). The further training reproduces the verified LAND atom ([adopt3](../../data/eval/runs/adopt3/README.md)) to an accuracy of 0.001.

**Decoder corrections on the site** (only in `site/math.js`, not in Python, so word ranks no longer match Python). The data is `site/data/words.json` (`scripts/site/build_words.py`, WordNet).

1. **Function words** (pronouns, prepositions, conjunctions, modals and everything not in WordNet, including proper names) are not offered.
2. **Word forms of one lemma** (tool / tools, house / housed) count as one word: the lemma is shown, and the rank is computed over lemmas.
3. **The code's part of speech** (`o/i/a/e`): a word loses 1.5·(1 − the share of its senses of this part of speech by WordNet counts). The coefficient was chosen on recipes from a grid 0…5.
4. **A pair through PI**: z(the score of the merged roots of both words) + 0.5·z(link), where the link is the highest cos of the word with one of the 10 first readings of the refining word (or with a word in quotes). So “furniture · house” looks for words similar to “non-living things” and related to apartment, home, residence. Numberbatch carries ConceptNet relations, so cos here is both “where it is located” and “what it is for”.

On 214 single-word recipes:

| | top1 | top10 | top50 | median rank | rank > 1000 | cos of the first reading with the word (median) |
|---|--:|--:|--:|--:|--:|--:|
| before | 6% | 27% | 49% | 54 | 30 | 0.20 |
| items 1–3 | 12% | 41% | 63% | 17 | 8 | 0.26 |

On 27 pairs from the blind tests key and furniture (geometric mean of rank): before 367 (key 206, furniture 1912), now 143 (key 147, furniture 132). There are few pairs, and λ and K were chosen on them, so this is an estimate, not a check.

The bottleneck of pairs is the refining word itself: “door” `PART(=-2) PLACE SIDE(=+5)` is read by the vectors as edges, aspect, frontier. So the math does not find key through the door that Haiku reads.

The reading code is gathered into the class `Reader` (`site/math.js`): the site and the check `scripts/site/eval_math.js` call the same thing. The link words of the refining word are `FROM`, `FOR`, `LIKE`, `PI`.

**The ConceptNet graph for pairs** (`scripts/site/build_graph.py`, the edges UsedFor, AtLocation, PartOf, HasA, MadeOf, CapableOf, IsA, ReceivesAction, RelatedTo between dictionary words; 7.6 MB). The pair's score gets graphW·(the weight of the edge from the word to the readings of the refining word), and each link word has its own relation weights (PI: part, place, material; FOR: purpose). On 51 pairs (the 27 earlier ones and 24 from the PI/FOR test) the mean rank falls from 197 to 161 at graphW = 4, for pairs with PI from 186 to 145, and for pairs with FOR it hardly changes (235 → 225). If the same codes are read through someone else's link word, the ranks are almost the same. So relation types give the math little: the bottleneck remains the reading of the refining word itself. The graph does not go on the site, graphW = 0.

**The roots of the refining word are not merged with the head.** Earlier the roots of both words were added into one vector. On 107 pairs from the blind tests (all `pairs.json`, key, furniture) this is worse than not reading the second word at all:

| roots of the second word in the common vector (modW) | link weight λ | mean rank | top10 |
|--:|--:|--:|--:|
| 1 (before) | 0.5 | 203 | 3 |
| 0.5 | 0.5 | 182 | 3 |
| 0 | 0 (the second word is not read) | 120 | 6 |
| 0 | 0.25 (site) | 112 | 7 |

Now the second word only nudges toward words related to its readings. For the vectors it gives little (120 → 112); the benefit of pairs is first of all for the LLM decoder (the blind test of link words, `data/eval/runs/links`).

**An encoder with a pair** (`Reader.encode`, until 2026-10-14): if the vectors did not put the word first, the encoder tried the word's 40 nearest neighbors, encoded each with at most two roots without the head's roots, and took the pair “code PI neighbor” with the best rank. The blind test [pi](../../data/eval/runs/pi/README.md) found no benefit, and the pair was removed: the encoder writes only the head word. Reading hand-typed pairs stayed.

The math's loop (word → code → reading) on 400 random dictionary words:

| neighbors | first | top10 | time per word (maximum) |
|--:|--:|--:|--:|
| no pair | 155 | 318 | — |
| 15 | 205 | 352 | 0.4 s (2.8 s) |
| 40 (site) | 248 | 367 | 1.0 s (5.5 s) |

Examples: ship + sailors, star + galaxy, vegetable + garden, harvest + corn (111 → 12).

**Encoder self-check and a penalty for an unmentioned root** (`READ.selfCheck`, `absLam 0,5`; data/eval/runs/selfcheck, data/eval/runs/absence). The encoder tries the best codes of 1, 2 and 3 roots and their neighbors (value ±1, minus one root), reads each with its own reading and takes the one where the word ranks higher; on a tie, the shorter. The code's head root does not change. The reading takes 0.5·max(0, z − 1) away from a word, where z is the word's highest affinity (a z-score of cos) with a root that is not in the code: if the word were strongly similar to this root, the encoder would have named it.

| | dev (100) | 1000 | another 1000 | roots in the code | model codes, cos of the first reading | pairs, mean rank |
|---|--:|--:|--:|--:|--:|--:|
| before | 69 | 406 | 382 | 2.91 | 0.172 | 183 |
| penalty only (site) | 71 | 466 | 449 | 2.91 | 0.227 | 142 |
| self-check + penalty | 84 | 558 | 555 | 2.53 | 0.227 | 142 |

The gain in firsts on 2000 words is +325 (95% +288…+363), of which the penalty is +127. The self-check is off on the site: it throws out meaningful roots for the sake of the vectors: teacher `ART(=+1) SEX(=-3) KNOW(=+3)` → `ART(=+1) SEX(=-3)`, that is, it subtracts corpus bias, not meaning. A check of readability by people or an LLM is needed. Weights of 0.6 for non-head roots are optimal: 1 and 0.8 are worse, 0.4 is almost the same, and a dictionary retrained at 0.4 is no better (data/eval/runs/weights, data/eval/runs/relearn).

**Names, number, part of speech, sex** (data/eval/runs/forms, data/eval/runs/sex). A proper name (all senses in WordNet capitalized) the encoder writes in quotes, a plural form as the lemma's code with `N+3`, and it takes the part of speech from WordNet (earlier `| o` for any word). SEX is given only to words for which sex is part of the meaning (81 words: mother, king, actress…; not teacher, president). The part of speech gives on the math's loop +158 firsts on 854 random words without names (399 → 557).

**The role for people** (data/eval/runs/fix1). If the first sense of a noun in WordNet is a person (noun.person, 952 words), the encoder uses the role `| o agent`: “the one who does it, or a person of this field” (Esperanto *-ist-*), lawyer `RULE(=+3) KNOW(=+2) SIDE(=+2) | o agent`. Blind readers: +19% “close” on 88 such words [+10 … +30]. The roles `tool` and `quality` by WordNet gave no benefit.

**What was tried for reading pairs and did not get in.** The link with the second word can be computed not as the highest cos with one of 10 readings but as the cos with the center of 20 readings. Besides, PRF can be added: shifting the scores toward the center of the 20 best readings of the code itself (`Vocab.toward`, `Reader.prf`, on the site prfMu = 0). On pairs from the blind tests written by models this is better: mean rank 112 → 86, with PRF 72; on recipes with PRF top10 41% → 44%. But on the math's loop it is worse. With a center of readings out of 150 non-first words, 23 become first against 32 with max. PRF on 1000 words with one code gives 336 firsts instead of 381. Combinations of max and center are worse than either separately. The main measure is the math's loop, so the site uses max and no PRF.

## 10. Blind check of the site's codes

The main measure now is the share of a blind reader's first answers that a blind judge considers “close” (2 close, 1 near, 0 miss): the semantic field matters, not the exact word.

- **1000 words** ([big1000](../../data/eval/runs/big1000)): the site encoder 24% “close”, Haiku with ENC_SPEC 52%. By part of speech for the site encoder: nouns 21%, verbs 25%, adjectives 28%, adverbs 32%. Worst are people (15% against 62% for the model; this is before the role agent), things and places. The 40 worst words are in `worst.md`.
- **The axes of 8 roots from atoms and the role agent for people** ([fix1](../../data/eval/runs/fix1)) were accepted (§ 9, “The role for people”).
- **Separate codes for the senses** of polysemous words (a sense vector by WordNet, [senses](../../data/eval/runs/senses)): −2% [−10 … +5], not accepted.
- **The root KIND** (“kind, variety”, [kind](../../data/eval/runs/kind)): +5.6% [−1 … +12], the threshold was not passed, not accepted. As the head of a code KIND helped (+15%), in the middle of a code it read as “evidence”.
- **A pair through PI for the site encoder** ([pi](../../data/eval/runs/pi/README.md), 137 pair codes): without the second word it is no worse (+3.6% [−3.6 … +11.7]); a second word that is the nearest anchor word from a recipe (+5% over the current pair) or a link word by ConceptNet edge type (worse) did not pass the thresholds. The broad definition of PI (“a part, place or variety of Y”) is also within noise. The bottleneck is the code of the head word; PI stays in the language. The pair was removed from the site encoder (2026-10-14).
- **KIND as a head only, and SIDE** ([side_kind](../../data/eval/runs/side_kind/README.md)): KIND as head +6.7% [−2.7 … +16] on 75 words; the earlier +15% did not repeat; KIND not accepted (user's decision, 2026-10-14). Without SIDE −2.1% [−8.5 … +3.5] on 141 words (it may be removed by the adopt rule); SIDE with a definition from the atom (“backward, to return … forward, upcoming”) +4.3% [−0.7 … +9.2], the threshold was not passed; the user chose to redefine it (2026-10-14), roots.yaml.
- **Moving model codes into the dictionary** (distillation, [distill](../../data/eval/runs/distill)): the codes look more meaningful but read almost like the earlier ones; the site dictionary did not change.

## 11. What's next

- A word pair “head + refinement” for words the code does not put first (the head being a hypernym from WordNet).
- External validation of the axes by human scales (Glasgow, Warriner, Brysbaert).
- Russian and aligning the spaces: lacunae between languages (codes near which there is a Russian word but no English one).
- A penalty for the encoder for choosing a root by a side sense of the vector: a step toward readable codes.
