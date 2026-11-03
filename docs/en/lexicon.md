# Lexicon

Roots, axes, labels and particles are in [`roots.yaml`](../../roots.yaml); the blocks between the `generated` markers of the Russian lexicon and [tables.md](tables.md) are generated from it; here they are translated by hand. Encoding techniques are in [encoding.md](encoding.md). Earlier schemes (automatic root selection, universal axes, the suffixes `-o/-i`) are in [history/lexicon_archive.md](../history/lexicon_archive.md) (in Russian).

There is no fixed vocabulary: a word is up to three roots, head first, each root with its own −5…+5 axis or none ([model](model.md)). There are no shared axes: a shade is given by one more root.

## Roots: the current list (draft)

The rule: each root has **its own** axis (one) or none; compound words of two or three roots, as in Esperanto (the head first, the others refine it; see [model](model.md)). Roots are taken from NSM; automatically selected words are not taken as roots (checked: the gain in wup is ≤ 0.01, the roots are unreadable, the set is unstable, see `data/roots_optimization.md`).

**45 roots in all: 39 with an axis, 6 without.** The Russian version of this block is generated from [`roots.yaml`](../../roots.yaml).

**With an axis (39):**

| root | axis (−5 … +5) | status |
| :-- | :-- | :-- |
| GOOD | bad … good | accepted |
| BIG | little … much | accepted |
| NEAR | far … close (−5 far, abroad, a journey, +5 here, nearby, in the center; including “this / that”) | accepted |
| ABOVE | lower … higher | accepted |
| LIVE | dead … alive | accepted |
| SAME | different … the same (−5 different, opposite, −4 special, unlike others, +3 ordinary, +5 the same, identical): `SAME(=-4) \| a` special, unique, `SAME(=-4) \| e` especially, `SAME(=+3) \| a` ordinary, `SAME(=+4) MANY(=+5) \| a` common, universal, `SAME(=-4) JOIN(=-5) RULE \| o` exception | accepted; **since 2026-10 it absorbs the root PARTICULAR** (general … special): blind test 12 words × 2 coders: with PARTICULAR 13 exact of 24, through SAME 12 of 24 — [roundtrip_merge](../../data/translation_test/roundtrip_merge.md) |
| TIME | earlier … later | accepted |
| INSIDE | outside … on the boundary, on the edge, surface … inside | accepted (data: the poles are in one family); the middle `INSIDE(=0)` is boundary, edge, surface (blind test of 22 codes: 32 → 53% “close”, [inside0](../../data/eval/runs/inside0/README.md)) |
| PART | a ladder: particle … part … whole … group (−5 crumb, −2 part / member, +2 whole / “completely”, +5 group, set, union); after the head word `PART(=+5)` is a collection of such things, like *-aro* in Esperanto: `SOMEONE PART(=+5) \| o` society, `THING(=0) PART(=+5) \| o` herd / grove; `SOMEONE PART(=-2) \| o` member | accepted, blind test 10 of 10 (`data/translation_test/roundtrip_part_ladder.md`) |
| SIDE | rear, backward, to return … front, forward, upcoming | accepted; definition from the atom (2026-10-14): “backward, to return … forward, upcoming, ready”: +4.3% [−0.7 … +9.2] against “rear … front”, +6.4% against removal ([side_kind](../../data/eval/runs/side_kind/README.md)) |
| KNOW | foolish, I don't know … I know (−5 foolish, absurd, 0 informed, +5 to know, to inform, to teach) | accepted |
| WANT | I don't want … I want (hatred … love) | accepted |
| HEAT | cold … hot (−5 ice, 0 warm/room temperature, +5 fire) | **new**, accepted |
| BEGIN | beginning … end (−5 to begin, 0 in progress / middle, +5 to finish): `BEGIN(=-5) \| i` to begin, `BEGIN(=+5) \| i` to finish, `BEGIN(=-4) \| a` first, `BEGIN(=+4) \| a` last | **new**, accepted |
| GIVE | to take … to give away (−5 to seize / take away / steal, 0 exchange / to receive, +5 to give away / present / donate): `GIVE(=-5) \| i` to take, `GIVE(=+5) \| i` to give, `GIVE(=-5) GOOD(=-4) \| i` to steal, `GIVE(=-3) TIME(=+3) \| i` to borrow | **new**, accepted (MOVE + INSIDE does not work, `data/translation_test/roundtrip_200.md`) |
| TOUCH | soft … hard (−5 soft / tender / smooth, 0 ordinary, +5 hard / stiff / harsh): `TOUCH(=-4) \| a` soft, `TOUCH(=+5) \| a` hard | **new**, accepted (test: sharp, concrete, board are confused without the axis) |
| SEX | female … male (only for words with explicit sex: −5 woman, +5 man; the weak ±1, ±2 are not used) | **new**, proposed |
| THINK | idea, thing | think, suppose |
| CAN | I can't … I can (−5 impossible, −3 difficult, +4 easy); from NSM, needed for “difficult / possible” | **new**, accepted (BECAUSE rejected) |
| MANY | how many (−5 none, not at all, −4 none of what is needed: shortage, absence, −3 almost none, barely, −1 few, not many, 0 some amount, +3 many, +4 most, +5 all, always): `THING MANY(=-5) \| o` nothing, `MANY(=-4) \| o` shortage, absence, `MANY(=-3) \| e` barely, hardly, `SOMEONE MANY(=+5) \| o` everyone | accepted; **two-sided since 2026-10** (before 2026-10 the scale was 0 … +5, “none” was 0): for the math the pole none / zero / absence is at −5, and 0 reads as *certainly, absolutely*; the encoder used negative levels in 46% of the codes with MANY (*lack, absence, insufficient, hardly, barely*) — [data/eval/runs/many](../../data/eval/runs/many/README.md); “one” and exact numbers are numbers from the exemptions |
| SOMEONE | person (−5 they / another, 0 someone, +3 you, +5 I): `SOMEONE(=+5) \| o` I, `SOMEONE(=+3) \| o` you, `SOMEONE(=-3) \| o` he; plural with `MANY` as the second root: `SOMEONE(=+5) MANY(=+3) \| o` we | **new**, accepted (blind test: 8 of 8 pronouns) |
| THING | animacy (−5 stone … 0 plant … +4 animal; a human is SOMEONE): `THING(=-5) \| o` stone, `THING(=+4) BIG(=+5) \| o` elephant | **new**, accepted (test: stone, insect, animal, elephant correct; plants weak) |
| MOVE | movement, motion | move, shift |
| FEEL | calm … excited (−5 lethargy, +5 strong feeling; whether pleasant or not is GOOD): `FEEL(=+4) GOOD(=-4) \| a` angry | **new**, accepted (test: 6 of 8; “angry” and “frightened” are confused) |
| RULE | personal … official (−5 personal, informal, private; 0 ordinary; +5 official, institution, law): `RULE(=+4) \| o` authority, institution, `SOMEONE PART(=+5) RULE(=+4) \| o` committee, agency | **new**, accepted; the SemAxis poles were changed from agencies (authority committee agency commission government) to law and authority: the old ones pulled any code with RULE toward *commissions, agencies*, institutions (court, bank, school, elections…) reached the top10 in 6% of cases, now in 32% (data/lacunae.md) |
| CHANGE | to stay … to change (−5 to stay, not to change, 0 to change, +5 to transform, to change completely): `CHANGE \| i` to change, `CHANGE(=-4) \| i` to remain, `CHANGE BIG(=+3) \| i` to grow, `CHANGE GOOD(=+3) \| i` to improve | **new**, proposed (SemAxis: alter, transform, modify, shift; the direction increase/decrease is given by the axes `BIG` and `GOOD`) |
| ART | technology … creativity (−5 calculation, technology, devices, exact sciences, 0 mixed, +5 creativity, culture, humanities): `ART(=-4) KNOW \| o` physics, `ART(=+5) SAY \| o` poetry, `ART(=-5) SOMEONE \| o` engineer; the root without a value is skill, craft, discipline | **new**, proposed (SemAxis: poles “humanities + art” against “exact sciences + technology”, LOO 1.00, the axes cover 10%); accepted (blind test: 29 of 32, only *architecture* missed) |
| JOIN | to separate … to attach (−5 to separate, remove, leave, subtract, 0 composition unchanged, +5 to attach, add, bring in, unite): `JOIN(=+4) \| i` to attach, `JOIN(=-4) \| i` to remove | **new**, proposed (SemAxis: poles join/add/attach against separate/remove/detach, LOO 1.00; nearest axes GIVE +0.3, NEAR +0.2); accepted with a reservation (blind test: ~8 of 10; *add* is not read, words inside the cluster merge) |
| VALUE | cheap … expensive (−5 cheap, discount, buying and selling, 0 ordinary price, +5 expensive, valuable, important, vitally needed): `VALUE(=+4) \| a` expensive, valuable, `VALUE(=-4) \| a` cheap; buying and selling go together with `GIVE` | **new**, proposed (SemAxis: poles cheap/worthless/useless against expensive/valuable/precious, LOO 0.91); accepted (blind test: 10 of 10 on adjectives; *buy/sell* are confused by the sign of `GIVE`) |
| CARE | attitude to work: careless … diligent (−5 careless, hasty, mistake, fault, 0 ordinary, +5 diligent, thorough, attentive): `CARE(=+4) \| e` thoroughly, `CARE(=-4) \| a` careless, lazy | accepted; in 2026-10 the poles became adjectives about work (careful, diligent … careless, lazy) instead of adverbs of manner: the center was close to TONE (cos 0.65), with FRIEND it is 0.12 |
| FRIEND | attitude to people: enemy … friend (−5 enemy, hostile, cruel, 0 neutral, +5 friend, friendly, kind): `FRIEND \| o` friend, `FRIEND(=-5) \| o` enemy, `FRIEND(=+4) \| a` kind, friendly, `FRIEND(=-3) \| a` rude | accepted in 2026-10 instead of TONE (rude … polite): the poles of TONE and CARE were adverbs of manner, their centers close (cos 0.65); FRIEND is the attitude to people, CARE to work |
| MOOD | grief … funny (−5 grief, despair, tragic, −3 sadness, 0 serious, calm, no joking, +3 merry, joyful, +5 funny, laughter, comic): `MOOD(=+5) \| a` funny, `MOOD(=-3) \| a` sad, `MOOD(=0) \| a` serious, `ART MOOD(=+5) \| o` comedy | **new** (the author's proposal: the axis “comedy … tragedy”; SemAxis: nearest axes LIVE +0.40, GOOD +0.31); accepted (blind test without recipes for the test words: 24 of 32 against 11 without the root; *happy / cheerful* merge) |
| CONSUME | to emit … to absorb (−5 to emit, throw out, pour out, 0 exchange, +5 to absorb, take in: eat, drink, read, listen; −5 to emit: excrete, write, speak, radiate): `CONSUME(=+4) \| i` to absorb, eat, `CONSUME(=-4) \| i` to emit; the channel is set by the second root: `CONSUME(=+4) SEE \| i` to read, `CONSUME(=-4) SAY \| i` to speak | **new**, proposed by the user (intake ↔ output: eat / excrete, read / write, listen / speak); accepted (blind test: 26 of 32; food, breathing, speech are read, *read / write* are not) |
| MEASURE | a quantity in itself … relative to another (−5 a quantity as such: size, amount, length, number, 0 level, degree, +5 a quantity relative to another: ratio, share, proportion, percent, statistics, speed as a ratio, average): `MEASURE(=-5) \| o` amount, size, `MEASURE(=+5) \| o` ratio, `MEASURE \| i` to measure, a unit is `MEASURE SAME \| o` | **new**, introduced by the rule (*ratio / proportion / measurement* failed to read twice through `PART`, `BIG`, `SAME`, `SEE`); the first version of the axis (unit … amount … ratio) was a mixture of three concepts and was rewritten; the axis is independent (SemAxis, maximum cosine with BIG −0.18); blind test v2 26 of 32, see [roundtrip_measure](../../data/translation_test/roundtrip_measure.md) |
| LONG | thin flexible … thick stiff long (−5 thread, cloth, rope, hair, 0 wire, rod, fastener, +5 beam, board, log, wooden furniture; long objects and what is made of them): `LONG(=-5) \| o` thread, `LONG(=+4) \| o` pole, `LONG \| a` long, tall, `LONG(=+3) PLACE \| o` tower | **new**, at the author's request (analogous to *palisa* / *linja* in Toki Pona: a long object); the axis is independent (SemAxis, cosine with ABSTRACT −0.17, TOUCH 0.13, BIG ≈ 0); blind test: [roundtrip_long](../../data/translation_test/roundtrip_long.md) |
| SAY | quiet … loud (−5 whisper, mumbling, 0 ordinary speech, +5 shout, roar, screech): `SAY(=-4) \| i` to whisper, `SAY(=+5) \| i` to shout, `SAY(=+4) \| o` a shout, `SAY(=-3) \| o` a whisper, noise is `SAY(=+3) THING \| o` | **a new axis on an existing root** (accepted by the author; residual PCA of weak words: *whistle, groan, wail, roar, murmur, buzz*; SemAxis cosine with FEEL 0.41, MOVE 0.26, the rest ≤ 0.15); blind test: [roundtrip_say](../../data/translation_test/roundtrip_say.md) |
| GRAIN | how a substance holds together (−5 gas, steam, smoke, −3 liquid, flows: water, honey, 0 granular: sand, flour, groats, +5 solid, whole: stone, ingot, monolith): `GRAIN(=-5) \| o` gas, `GRAIN(=-3) \| o` liquid, `GRAIN(=0) THING(=-5) \| o` sand, `GRAIN(=+5) \| a` whole, continuous, solid; to eat `CONSUME(=+5) GRAIN(=+3) \| i`, to drink `CONSUME(=+5) GRAIN(=-3) \| i`, to inhale `CONSUME(=+5) GRAIN(=-5) \| i`. Analogous to *ko* in Toki Pona (formless substance), but broader; the step between values in numbers: reals are fluid (−3), integers about −1 | **a new root, proposed by the author**; the condition of the rule was met: on existing roots a blind test of 12 words × 2 coders gave 3 exact of 24 (sand, dust, granular, seamless, continuous, ingot do not assemble); blind test with the root: 7 exact of 24 and 14 of 24 among three answers against 3 and 4 without the root — [roundtrip_grain](../../data/translation_test/roundtrip_grain.md). **Since 2026-10 it absorbs the root MATTER** (solid … liquid … gas): one scale instead of two opposing ones, blind test of 12 words: 11 → 17 exact of 24 — [roundtrip_merge](../../data/translation_test/roundtrip_merge.md) |
| FIGHT | how serious the struggle is (−5 game, sport, competition by the rules … 0 brawl, dispute … +5 war to the death); without a value, battle, quarrel: `FIGHT(=-5) \| o` game, sport, `SOMEONE FIGHT(=-5) \| o` player, `FIGHT(=-5) PART(=+5) \| o` tournament, `FIGHT(=+5) \| o` war, `SOMEONE FIGHT(=+5) \| o` soldier | **axis added** (a lacuna from mathematical encoding, [math.md](math.md)): blind test 12 words × 2 coders: without the axis 11 exact of 24 (game and sport read as *duel, boxing*), with the axis 17 of 24 and 21 of 24 among three answers — [roundtrip_candidates](../../data/translation_test/roundtrip_candidates.md) |
| LAND | water … land (−5 sea, lake, water as a place, 0 shore, coast, +5 land, soil, solid ground); without a value, land, country, region: `LAND \| o` country, region, `LAND RULE \| o` state, province, `LAND(=+5) ABOVE(=+5) \| o` mountain, `LAND(=-5) BIG(=+5) \| o` ocean, `LAND(=0) GRAIN(=0) \| o` beach, `LAND RULE LONG(=-5) \| o` state border. Analogous to *ma* in Toki Pona | **a new root** (Toki Pona *ma*); blind tests on fresh words: encoder SZ +20% and +12% “close”, model codes +19%, site encoder +2% (does no harm) — [adopt3](../../data/eval/runs/adopt3/README.md), [adopt4](../../data/eval/runs/adopt4/README.md); the border `LAND RULE LONG(=-5)`: 4 of 4 “border” ([border](../../data/eval/runs/border/README.md)) |

**The zero rule.** An axis that is not written has an unspecified value. `(=0)` is an explicit value: on two-sided axes the middle (`TIME(=0)` is “now”); there are no one-sided axes: `MANY` has been two-sided since 2026-10, “none” is `MANY(=-5)`, 0 is “some amount”.

**New axes and roots** (blind test on 46 words, `data/translation_test/roundtrip_axes_rules.md`: the word or a synonym 31 of 46, 67%; the words were chosen to suit the axes, so the estimate is inflated compared with the random 26–34%). SOMEONE got the axis “person”, THING animacy, MOVE speed, FEEL excitement. **RULE** (law, rule, to govern) and **FIGHT** (battle, war, quarrel) were added without axes; *peace* = `FIGHT MANY(=-5) | o`. Weak spots: *tax, duty, defend, politics*; *though, instead, nevertheless* deliberately get no roots.

**Emotions** (blind test on 40 words, `data/translation_test/roundtrip_emotions.md`): `FEEL` (excitement) + `GOOD` (pleasantness) + a third root by meaning, not a “direction” axis (`NEAR`/`WANT` gave 24–25 of 40 against 21; by meaning 28). Fear `FEEL(=+4) GOOD(=-4) TIME(=+3) | a` (something bad ahead), anger and hatred `… FIGHT`, social emotions `… SOMEONE` (+ `SEE | i`). Weak: *shy, contempt, pity, jealous, amused*.

**Without an axis (6):** HAPPEN, BODY, SEE, DO, PLACE, TEXT.

CONTAINER and MAYBE were removed (blind test on 224 items without them: within noise, `data/translation_test/roundtrip_ablation3.md`; a container is `THING INSIDE`, probability is the label `M`).

**Edits from the 200-word test** (`data/translation_test/roundtrip_200.md`): HEAR, KIND, WORD were removed (0 successes of 7 in the test; sound reads through `SAY`, `FEEL`, type through `THING`, a word is `SAY | o`). Added: **CONSUME** (to eat, drink, absorb; *eat* = `CONSUME | i`, *food* = `THING CONSUME | o`, instead of three roots eat/food/drink) and **CONTAINER** (a vessel, like *poki* in Toki Pona: *bag, pitcher, bottle, box*; `CONTAINER | o`). Both without an axis, not yet checked. A rule of use: `ABOVE`, `INSIDE`, `BIG` only for real “top / inside / size”, not as a metaphor or an intensifier.

**PEOPLE was removed:** `SOMEONE MANY(=+4) | o` (“many someones”) replaces it without loss (blind test on 12 words with PEOPLE: the word or a synonym 2 of 12 as before the replacement, “miss” 3 instead of 5). HEAT, BEGIN, GIVE were also added (see the table).

Examples of compound words: house = `PLACE LIVE | o`; bedroom = `PLACE LIVE(=-2) | o`; morgue = `PLACE LIVE(=-5) | o`; man = `SOMEONE SEX(=+5) | o`. Gaps (anatomy, kinship) go to the exemptions.

**Correlatives (Esperanto's idea) without a word list** (the table has only roots; a word also has a form, for example `SOMEONE NEAR(=+3) | o`):

| | who | what | where | when |
| :-- | :-- | :-- | :-- | :-- |
| question | `SOMEONE \| o ?` | `THING \| o ?` | `PLACE \| o ?` | `TIME \| o ?` |
| indefinite | `SOMEONE` | `THING` | `PLACE` | `TIME` |
| this / here / now | `SOMEONE NEAR(=+3)` | `THING NEAR(=+3)` | `PLACE NEAR(=+3)` | `TIME(=0)` |
| that / there / then | `SOMEONE NEAR(=-3)` | `THING NEAR(=-3)` | `PLACE NEAR(=-3)` | `TIME(=-3)` or `+3` |
| all / everywhere / always | `SOMEONE MANY(=+5)` | `THING MANY(=+5)` | `PLACE MANY(=+5)` | `TIME MANY(=+5)` |
| nothing / nowhere / never | `SOMEONE MANY(=-5)` | `THING MANY(=-5)` | `PLACE MANY(=-5)` | `TIME MANY(=-5)` |

Open: for “when” the NEAR axis does not fit (it has its own axis TIME); “now / then” are written through TIME for now.


## Exemptions (words outside the roots)

Part of the vocabulary makes no sense to encode through general roots and axes. It is taken outside the roots and does not use up axes:

- **Country names** (and proper-name toponyms in general) are borrowed as they are, without a root or features.
- **Numbers** are a separate counting system, not roots.
- **Months and days of the week** go by number: month 3, weekday 2 (not the words *March*, *Tuesday*).
- **Colors** are continuous coordinates (RGB or HSL), not words and not a root COLOR (removed from the list of roots).
- **Proper names** (people, places, organizations, brands) are borrowed as they are, like country names.
- **Nationalities and religions** (*american*, *mexican*, *christian*, *catholic*) are derived from proper names and are borrowed along with them. In the experiment they assembled themselves into the roots AMERICAN and CHRISTIAN.
- **Biological taxa** use Latin nomenclature as it is (*Canis lupus familiaris*, *Opuntia indica*); for ordinary speech the name of the genus or species is enough (*Canis*, *Felis*, *Quercus*). So the roots ANIMAL and PLANT are not needed. Anatomy and medicine (Latin terms, diseases) are not yet decided, see [open questions](rethink.md).
- **Chemistry** uses IUPAC/Latin names of elements and compounds (*H2O*, *natrii chloridum*), formulas as they are.
- **Minerals and rocks** use scientific names as they are (*quartz*, *granite* in the Latin/mineralogical form).
- **Astronomy** uses the names of stars, constellations, planets and other celestial bodies as they are (*Sol*, *Ursa Major*).

A consequence: the root MONTH is no longer needed, and with it goes the error with the homonyms *march* (to walk) and *rent* (lease): they were assigned to MONTH because of a “monthly” context. It remains open how to write the numbers themselves, how to tell a borrowed name from a word of the language (a label or a phonological feature) and how to inflect or attach suffixes to them ([phonology](phonology.md)).
