# How to encode: techniques

The techniques were selected through blind tests (the coder sees only the specification). Each has a link to its test; **no test** means the hint has not been checked. Roots and axes are in [lexicon.md](lexicon.md), labels and particles in [syntax.md](syntax.md), the model in [model.md](model.md). Used by the `mincode` skill (`.claude/skills/mincode/SKILL.md`).

**v2 (2026-10).** The limit is three roots without exceptions; `DO` and `HAPPEN` have no axis, and their earlier values were replaced by form roles (`| o agent`, `tool`, `result`, `quality`); there is no root `ABSTRACT`; `TONE` was replaced by `FRIEND` (enemy … friend). The linked tests checked the earlier notation; recipes rewritten into roles were not checked in the new notation, except by the general v2 test ([data/eval/runs/toki](../../data/eval/runs/toki/README.md)).

## General

- Actions without their own root go through `DO | i E …` (to do, to cause) or `SAY | i …` (to say, to ask) ([roundtrip_30](../../data/translation_test/roundtrip_30.md)).
- “Can, difficult, possible” is `CAN` (`DO CAN(=-3) | a` is *difficult*); “possibly, maybe” is the label `M-3`; there is no root `MAYBE`.
- **Quotes have one rule:** proper names, digits and scientific names of species and substances: `"Rome"`, `"17"`, `"Canis"` dog, `"Quercus"` oak, `"iodine"` iodine. Everything else, including categories (*animal, plant, bird* are `THING(=+4)`, `THING(=0)`…), positions and institutions, is assembled from roots. Earlier, terms (*parliament, railway, furnace*) were also put in quotes: in a test on 60 sentences ([roundtrip_wiki_new4](../../data/translation_test/roundtrip_wiki_new4.md)) this gave 2.35 of 3 against 1.85; v2 gave it up for the sake of one rule, and on words there was no difference.
- Quantity is `MANY` (−5 none, −4 shortage, −3 almost none, −1 few, 0 some amount, +3 many, +5 all; the scale has been two-sided since 2026-10, [data/eval/runs/many](../../data/eval/runs/many/README.md)), exact numbers in digits in quotes.
- `ABOVE`, `INSIDE`, `BIG` only for real “top / inside / size”; a metaphor (*roof, coffee, desk*) and an intensifier (`BIG(=+5)` as “very”) are almost always misread ([roundtrip_200](../../data/translation_test/roundtrip_200.md)).
- Do not overuse `ABOVE` for “important”: *elect* through `ABOVE(=+4)` reads as *worship*.
- Food and drink are `CONSUME`, a container is `THING INSIDE | o` or `PLACE INSIDE | o` (the root `CONTAINER` was removed); the roots HEAR, KIND, WORD, PEOPLE no longer exist (PEOPLE = `SOMEONE MANY(=+4) | o`).

## Connectors: and, also, therefore

- “And, also, too” is the particle `AND` between the coordinated items: `X AND Y`, `[ … ] AND [ … ]`, in a list before the last element; do not use `JOIN`, `CHANGE`, `SAME` as connectors (decoders read them literally: *joined, changed*; [roundtrip_wiki4](../../data/translation_test/roundtrip_wiki4.md)). Checked ([roundtrip_wiki_new4](../../data/translation_test/roundtrip_wiki_new4.md)): `AND` in 39 codes of 60, decoders read it as *and / also* (54 times), literal “joined” 2 instead of 8.
- **`AND` with modifiers** (blind test, 2 coders × 2 decoders, 11 sentences; [roundtrip_and_mod](../../data/translation_test/roundtrip_and_mod.md)): the axes are taken by the particle itself, the word order is the original one. `AND SAME(=-5)` is *but, while, whereas* (4/4 correct); `AND SAME(=-2)` is *although* (4/4); `AND HAPPEN(=+4)` is *therefore, so* (2/2); `AND HAPPEN(=-4)` is *because* (2/2); `AND BIG(=+4)` is *all the more, let alone* (*let alone* 2/2, *what is more* reads as a plain *and* + emphasis); `AND MAYBE(=-3)` (now `AND | M-3`, not checked) is *or* (2/2). `LA` stays for *if / when*.

## Against, cause, decision

- “Against” (*protest, refuse*) goes through an explicit bearer: `SOMEONE SAY WANT(=-5) | o` (the test had four roots, `SOMEONE MANY(=+4) SAY WANT(=-5)`, over the limit; the three-root variant was not checked); a bare `WANT(=-5)` is often ignored by the decoder.
- Cause and consequence as objects are roles: `HAPPEN | o agent` cause, `HAPPEN | o result` consequence. “Because / therefore / since” between clauses is `LA [ cause ] consequence` (the cause comes first, the word order is changed) **no test**.
- A decision is the axis `THINK` (`THINK(=+5) | i` to decide, `THINK(=-4) | i` to doubt).

## People and objects

- Pronouns are the axis `SOMEONE` (I +5, you +3, he −3), plural through `MANY`: `SOMEONE(=+5) MANY(=+3) | o` is *we*.
- Animacy is the axis `THING` (stone −5, plant 0, animal +4); speed is `MOVE`, excitement `FEEL`; whether pleasant or not is `GOOD`.
- *grandfather, old man* = `SOMEONE SEX(=+5) TIME(=-4) | o` (“male ancestor”; `TIME(=-4)` alone gives *ancestor*; the earlier variant with `LIVE(=+3)` had four roots). **No test.**

## Emotions, battle

- Law and authority are `RULE`, battle and war are `FIGHT` (*peace* = `FIGHT MANY(=-5) | o`).
- The axis of `FIGHT` is how serious it is: −5 game, sport, competition by the rules … 0 brawl, dispute … +5 war to the death ([roundtrip_candidates](../../data/translation_test/roundtrip_candidates.md), 11 → 17 exact of 24). *game* = `FIGHT(=-5) | o`, *sport* = `FIGHT(=-5) BODY | o`, *player* = `SOMEONE FIGHT(=-5) | o`, *tournament* = `FIGHT(=-5) PART(=+5) | o`, *toy* = `THING(=-5) FIGHT(=-5) | o`, *champion* = `SOMEONE FIGHT(=-5) GOOD | o C+5`; *war* = `FIGHT(=+5) | o`, *weapon* = `FIGHT(=+5) | o tool` (a tool of battle), *soldier* = `SOMEONE FIGHT(=+5) RULE(=+4) | o`, *army* = `SOMEONE FIGHT(=+5) PART(=+5) | o`.
- Emotions: `FEEL` (excitement) + `GOOD` (pleasantness) + a root by meaning: fear `TIME(+3)` (something bad ahead), anger `FIGHT | a`, social ones `SOMEONE | o` (+ `SEE | i`); the axes `NEAR` and `WANT` do not work for direction.
- **Mood is `MOOD`**: −5 grief, despair … −3 sadness … 0 serious … +3 merry … +5 funny ([roundtrip_mood](../../data/translation_test/roundtrip_mood.md): 24 of 32 against 11 through `FEEL GOOD`, where the funny merged with the pleasant: *pleasant*, *compliment*, *praise*). *funny* = `MOOD(=+5) | a`, *joke* = `SAY MOOD(=+5) | o`, *humor* = `MOOD(=+5) | o quality`, *comedy* = `ART MOOD(=+5) | o`, *laugh* = `MOOD(=+5) | i`, *cheerful* = `MOOD(=+3) | a`, *smile* = `MOOD(=+3) BODY | i`, *party* = `MOOD(=+3) PART(=+5) | o`, *celebrate* = `DO MOOD(=+3) PART(=+5) | i`, *serious* = `MOOD(=0) | a`, *sad* = `MOOD(=-3) | a`, *cry* = `MOOD(=-3) CONSUME(=-5) GRAIN(=-3) | i` (to emit a liquid), *grief* = `MOOD(=-5) | o`, *despair* = `MOOD(=-5) CAN(=-5) | o`, *mourn* = `MOOD(=-5) LIVE(=-5) | i`, *funeral* = `MOOD(=-5) LIVE(=-5) PART(=+5) | o`, *tragedy* = `ART MOOD(=-5) | o`. Happiness is not a mood but an evaluation: *happy* = `FEEL(=+4) GOOD(=+4) | a` (`MOOD(=+3)` reads as *cheerful*). A catastrophe is an event: `HAPPEN GOOD(=-5) | o`. `DO` before `MOOD` in an event makes an actor (*funeral* with `DO` → *mourner*).

## Time

- `TIME(=+1)` reads as *soon*; do not use it for “later”.
- *later, subsequent, earlier, before, after, initially* are the label `R`, not `TIME(=±n)` ([roundtrip_reltime](../../data/translation_test/roundtrip_reltime.md)).
- A span of time is `TIME(=0) BIG(=n) | o`, the BIG scale: −5 second, −4 minute, −2 hour, 0 full day, +1 week, +2 month, +3 year, +4 decade, +5 century; a moment is `TIME(=0) BIG(=-5) MANY(=-1) | o` (checked with `MANY(=+1)`, “a little”, on the old scale) ([roundtrip_time](../../data/translation_test/roundtrip_time.md): 20 of 20, without the scale 7 of 20).
- Which day exactly: the TIME level is the shift from “now”: yesterday `TIME(=-1) BIG(=0) | e`, tomorrow `TIME(=+1) BIG(=0) | e`, today `TIME(=0) BIG(=0) NEAR(=+5) | e` (“this day”).
- A part of the day is a day with a BEGIN level: `TIME(=0) BIG(=0) BEGIN(=n) | o`: −4 morning, 0 noon, +3 evening, +5 night, midnight is `BEGIN(=+5) | o C+5`. Annual is `TIME(=0) BIG(=+3) MANY(=+5) | a` (“every year”).

## Cardinal directions

“The sides of the earth”: `PLACE BIG(=+5)` and a direction. We stand facing the sunrise: east is the front (`SIDE(=+5)`), west is the back (`SIDE(=-5)`); north is the top of the map (`ABOVE(=+5)`), south the bottom (`ABOVE(=-5)`). East = `PLACE BIG(=+5) SIDE(=+5) | o`, north = `PLACE BIG(=+5) ABOVE(=+5) | o`, northern = `PLACE BIG(=+5) ABOVE(=+5) | a`. Without “earth” `PLACE ABOVE(=+4)` reads as *top* (0 of 6), with it 10 of 10 ([roundtrip_time](../../data/translation_test/roundtrip_time.md)). Intermediate directions: the limit is three roots, no exception: northeast = `PLACE ABOVE(=+3) SIDE(=+3) | o` (no test; may read as “top-front”).

## Direction of motion

With a verb of motion (`MOVE`, `GIVE`, `DO`), the value of `INSIDE`, `NEAR` or `ABOVE` is where the motion ends. To enter = `MOVE INSIDE(=+5) | i`, to exit = `MOVE INSIDE(=-5) | i`, to arrive = `MOVE NEAR(=+5) | i`, to leave = `MOVE NEAR(=-5) | i`, to go up = `MOVE ABOVE(=+5) | i`, to go down = `MOVE ABOVE(=-5) | i`; to approach = `MOVE NEAR(=+5) | i A0` (has not arrived yet); to return = `MOVE SAME(=+5) | i`. Moving something else is the label `K+3`: to insert = `MOVE INSIDE(=+5) | i K+3`, to take out, extract = `MOVE INSIDE(=-5) | i K+3`, to bring = `MOVE NEAR(=+5) | i K+3`, to send = `MOVE NEAR(=-5) | i K+3`, to fill = `MOVE INSIDE(=+5) MANY(=+5) | i K+3`, to empty = `MOVE INSIDE(=-5) MANY(=+5) | i K+3`, to pour = `MOVE ABOVE(=-4) GRAIN(=-3) | i K+3`. A separate “from where / to where” label is not needed: with and without it 18 of 24 ([roundtrip_direction](../../data/translation_test/roundtrip_direction.md)).

## Size, groups, parts

- *small* = only `BIG(=-3)`, without `PART` ([roundtrip_words_isolated](../../data/translation_test/roundtrip_words_isolated.md)).
- The axis of `PART`: crumb −5, part / member −2, whole / “completely” +2, group +5 ([roundtrip_part_ladder](../../data/translation_test/roundtrip_part_ladder.md), [roundtrip_part_groups](../../data/translation_test/roundtrip_part_groups.md)).
- *society* = `SOMEONE PART(=+5)`, *member* = `SOMEONE PART(=-2)`, *set / union* = `PART(=+5)`, *herd* = `THING(=0) PART(=+5)`; not `MANY SAME` and not `PART SOMEONE MANY`. Put `PART(=+5)` right after the head word, not first.

## Change, authority, the special

([roundtrip_new_axes](../../data/translation_test/roundtrip_new_axes.md), 38 of 54)

- Change is the root `CHANGE` (−5 to stay … +5 to transform); the direction goes through `BIG` and `GOOD`: *grow* = `CHANGE BIG(=+3) | i`, *improve* = `CHANGE GOOD(=+3) | i`, *remain* = `CHANGE(=-4) | i`.
- Authority and institution are the axis of `RULE` (−5 personal … +5 official): *authority* = `RULE(=+4) | o`, *official* = `RULE(=+5) | a`, *private* = `RULE(=-5) | a`. Weak values around 0 carry nothing.
- Organizational types (*committee, commission, agency, union, party, institution*) are not distinguished by roots: the code `SOMEONE PART(=+5) RULE(=+4) | o` reads as “an official group”. We do not introduce an `@NN` vocabulary; the loss is accepted.
- The special and the general are the axis of `SAME` (the root `PARTICULAR` was merged into it, [roundtrip_merge](../../data/translation_test/roundtrip_merge.md)): *special / unique* = `SAME(=-4) | a`, *especially* = `SAME(=-4) | e I+4`, *individual* = `SAME(=-4) PART(=-2) | a`, *ordinary* = `SAME(=+3) | a`, *general / universal* = `SAME(=+4) MANY(=+5) | a`. Do not assemble: *specific* (`SAME(=-4) KNOW(=+5)` → *famous*), *rare* (`MANY(=+1)` → *few*; on the new scale `MANY(=-3)`, not checked).

## Voice

- The label `V` ([roundtrip_voice](../../data/translation_test/roundtrip_voice.md), 10 of 11): −4 passive, 0 by itself, +4 on purpose.
- The agent with a passive is the particle `PE`: `… V-4 PE X` ([roundtrip_pe](../../data/translation_test/roundtrip_pe.md), 6 of 6, preliminary).

## Degree

([roundtrip_degree](../../data/translation_test/roundtrip_degree.md), 18 of 24 correct, 2 partly)

- An intensifier or a weakener is the label `I` on the head word: *very good* = `GOOD(=+3) | a I+4`, *extremely big* = `BIG(=+3) | a I+5`, *slightly warm* = `HEAT(=+2) | a I-2`, *hardly possible* = `CAN(=+1) | a I-5`, *completely different* = `SAME(=-5) | a I+5`.
- `I0` (“rather, moderately”) can get lost; for a weak degree write `I+1…+2`.
- Not `BIG(=+5)` as “very”; not `C` (comparison).
- *Almost* is not conveyed by the label `I`: it reads as *quite likely / fairly certain*; this is accepted as a tolerable loss, and we introduce nothing.
- Importance is `BIG` + `HAPPEN` (“big consequences”): `BIG(=+3) HAPPEN | a` *significant*, `BIG(=+4) HAPPEN | a` *important / major*, `BIG(=+5) HAPPEN | a` *crucial / momentous* (in the test `HAPPEN` also had a value; in v2 it does not) ([roundtrip_importance](../../data/translation_test/roundtrip_importance.md), 8–9 of 10). Not `SAME(=-4)` (reads as *special*) and not `GOOD + BIG` (reads as *great / wonderful*, 0 of 10); *vital* through `LIVE` is not read.

## Substance and tools

- The axis of `GRAIN` is how a substance holds together (the root `MATTER` was merged into it, [roundtrip_merge](../../data/translation_test/roundtrip_merge.md), 17 of 24): −5 gas, steam, smoke … −3 liquid … 0 granular … +5 a solid piece. *gas* = `GRAIN(=-5) | o`, *steam* = `GRAIN(=-5) HEAT(=+3) | o`, *liquid* = `GRAIN(=-3) | o`, *water* = `GRAIN(=-3) CONSUME(=+5) LIVE | o`, *sand* = `GRAIN(=0) THING(=-5) | o`, *flour* = `GRAIN(=0) CONSUME(=+5) THING(=0) | o`, *stone* = `GRAIN(=+5) THING(=-5) | o`, *ice* = `GRAIN(=+5) HEAT(=-5) | o`, *melt* = `CHANGE(=+4) GRAIN(=-3) HEAT(=+3) | i`. Honey (`GRAIN(=-3) CONSUME(=+5) GOOD(=+4)`) reads as wine, juice.
- A tool is the role `tool` (earlier the axis of `DO`, `DO(=+5)`: 17 of 24, [roundtrip_merge](../../data/translation_test/roundtrip_merge.md)): the roots describe the action, `| o tool` makes a tool out of it. *knife* = `JOIN(=-4) TOUCH(=+4) | o tool`, *saw* = `JOIN(=-4) MOVE(=+2) | o tool`, *scissors* = `JOIN(=-4) MANY(=-1) | o tool`, *hammer* = `TOUCH(=+5) MOVE(=+4) | o tool`, *brush* = `TOUCH(=-3) MOVE | o tool`, *pen* = `TEXT | o tool`, *thermometer* = `MEASURE HEAT | o tool`, *ladder* = `MOVE ABOVE(=+4) | o tool`, *key* = `INSIDE(=+4) CAN(=+4) | o tool`. Did not assemble: spoon (→ *cup*), broom, needle. Not `THING(=-5)` for tools: it reads as stone.

## Science, technology, art

([roundtrip_art](../../data/translation_test/roundtrip_art.md), 29 of 32 correct, 1 more as a backup answer)

- A field of knowledge or occupation is the root `ART` (−5 calculation, technology … +5 creativity, culture): *poetry* = `ART(=+5) SAY | o`, *painting* = `ART(=+5) SEE GRAIN(=-3) | o`, *history* = `ART(=+4) KNOW TIME(=-3) | o`, *physics* = `ART(=-4) GRAIN MOVE | o`, *mathematics* = `ART(=-5) MANY SEE | o`, *engineering* = `ART(=-4) DO THING | o`.
- A practitioner is `SOMEONE ART(=±n) …`: *engineer* = `SOMEONE ART(=-4) DO | o`, *scientist* = `SOMEONE ART(=-4) KNOW | o`, *artist* = `SOMEONE ART(=+5) DO | o`.
- Devices are `THING(=-5)` and an action: *machine* = `THING(=-5) MOVE DO | o`, *computer* = `THING(=-5) THINK ART(=-5) | o`.
- Not read: *architecture* (`ART(=0) DO PLACE` → *workshop*; `ART(=+3) PLACE LIVE` → *theater*). Accepted as a loss.

## Age, music, water, success

Blind test [roundtrip_lacunae2](../../data/translation_test/roundtrip_lacunae2.md): 23 of 24 with recipes, 11 and 13 of 24 without them.

- **Age** is `LIVE` with `TIME`, where the TIME level means since when the being has been alive:
  - young: `LIVE TIME(=-1) | a`;
  - adult: `LIVE TIME(=-3) | a`;
  - old, elderly: `LIVE TIME(=-5) | a`;
  - youth: `SOMEONE LIVE TIME(=-1) | o N+3`, “young people”. The test had a variant with `PART(=+5)`, which was read correctly (2 of 2), but that is four roots, over the limit; the three-root variant was not checked;
  - age: `LIVE TIME MEASURE | o`.

  About things it is written without `LIVE`: ancient is `TIME(=-5) | a`.
- **Music** is sound as an art. `FEEL(=+3)` separates singing from poetry (`ART(=+5) SAY`). If a song is written through `TEXT`, it reads as verse.
  - to sing: `SAY ART(=+5) FEEL(=+3) | i`, a song is the same with `| o`;
  - singer: `SOMEONE SAY FEEL(=+3) | o`;
  - music: `ART(=+5) SAY THING | o`;
  - melody: `ART(=+5) SAY LONG | o`;
  - to dance: `ART(=+5) MOVE BODY | i`.
- **Water and relief** are `PLACE GRAIN(=-3)`, “a place of liquid”. Without `PLACE` at the start and without a recipe such a code reads as air or sky.
  - sea: `PLACE GRAIN(=-3) BIG(=+5) | o`;
  - lake: `PLACE GRAIN(=-3) BIG(=0) | o`;
  - river: `PLACE GRAIN(=-3) MOVE(=+3) | o`;
  - island: `PLACE GRAIN(=-3) INSIDE(=+5) | o`;
  - shore: `PLACE GRAIN(=-3) NEAR(=+4) | o`;
  - mountain: `PLACE ABOVE(=+5) BIG(=+4) | o`.
- **Success and victory** are `GOOD` about a result, the role `result`.
  - to win: `FIGHT GOOD(=+4) | i`, to lose: `FIGHT GOOD(=-4) | i`;
  - victory: `FIGHT GOOD(=+4) | o result`;
  - success: `DO GOOD(=+4) | o result`;
  - to fail: `DO GOOD(=-4) | i`;
  - famous: `KNOW MANY(=+5) | a`.

## Law, money, food, transport

([roundtrip_lacunae3](../../data/translation_test/roundtrip_lacunae3.md): 24 of 24 with recipes against 17 without them)

- **Law** is `RULE(=+4)` (law) with `GOOD(=-4)` (violation): crime = `DO GOOD(=-4) RULE(=+4) | o`, criminal = `SOMEONE GOOD(=-4) RULE(=+4) | o`, court = `PLACE RULE(=+4) THINK(=+5) | o`, judge = `SOMEONE RULE(=+4) THINK(=+5) | o`, prison = `PLACE MOVE(=-5) RULE(=+4) | o`, to steal = `GIVE(=-4) GOOD(=-4) | i`.
- **Money** is `VALUE` with `GIVE`; the head root decides what is given: money = `VALUE GIVE(=0) | o`, to pay = `VALUE GIVE(=+4) | i` (to sell is `GIVE(=+3) VALUE | i`), debt = `VALUE GIVE(=+4) TIME(=+3) | o`, rich = `VALUE MANY(=+5) | a`, poor = `VALUE MANY(=-4) | a` (a shortage of money), market = `PLACE GIVE(=0) VALUE | o`.
- **Food** is `CONSUME(=+5)` with the kind of thing `THING`: meat = `CONSUME(=+5) THING(=+4) | o`, vegetable = `CONSUME(=+5) THING(=0) | o`, to cook = `HEAT(=+3) CONSUME(=+5) | i`, kitchen = `PLACE HEAT(=+3) CONSUME(=+5) | o`, farm = `PLACE THING(=0) DO | o`, to harvest = `GIVE(=-4) THING(=0) PART(=+5) | i`.
- **Transport and buildings** are the role `tool` (not “stone” `THING(=-5)`) and `PLACE`: car = `MOVE(=+4) | o tool`, ship = `MOVE GRAIN(=-3) | o tool`, road = `PLACE MOVE LONG(=-3) | o`, bridge = `PLACE MOVE ABOVE(=+4) | o`, house = `PLACE INSIDE(=+5) LIVE | o`, room = `PLACE INSIDE(=+5) PART(=-2) | o`. Institutions with a recipe are written by the recipe, not in quotes.

## Society, power, learning, war

([roundtrip_lacunae4](../../data/translation_test/roundtrip_lacunae4.md): 24 of 24 with recipes against 13 and 19 without them)

- **Society**: to trust = `THINK(=+5) GOOD(=+4) | i` (“to decide that someone is good”), friend = `FRIEND | o` (the test had `SOMEONE WANT(=+3) JOIN(=+3) | o`), ally = `SOMEONE FIGHT JOIN(=+4) | o`, leader = `SOMEONE SIDE(=+5) RULE | o`, agreement = `THINK(=+5) SAME(=+5) | o`, safe = `GOOD(=-4) CAN(=-5) | a` (“harm is impossible”).
- **Power**: king = `SOMEONE RULE(=+5) SEX(=+5) | o` (queen is `SEX(=-5)`), government = `SOMEONE RULE(=+5) PART(=+5) | o`, to vote = `THINK(=+5) MANY(=+5) | i` (“everyone decides”), elections = `THINK(=+5) MANY(=+5) RULE(=+4) | o`, citizen = `SOMEONE PART(=-2) RULE(=+4) | o`, city = `PLACE SOMEONE MANY(=+5) | o`.
- **Learning and film**: school = `PLACE KNOW CONSUME(=+5) | o`, student = `SOMEONE KNOW CONSUME(=+5) | o`, teacher = `SOMEONE KNOW GIVE(=+4) | o`, university = `PLACE KNOW ABOVE(=+4) | o`, film = `ART(=+5) SEE MOVE | o`, to advertise = `SAY GIVE(=+3) VALUE | i` (“to speak in order to sell”).
- **War**: enemy = `FRIEND(=-5) | o` (in the test `SOMEONE WANT(=-4) FIGHT | o`), battle = `FIGHT(=+5) PART(=-2) | o` (“a part of a war”), rifle = `FIGHT(=+5) HEAT(=+5) | o tool` (“a fiery tool of battle”), to defend = `DO GOOD(=-4) | i K-4` (“not to let harm be done”), to attack = `FIGHT(=+4) BEGIN(=-5) | i`.

## Quotes: categories and family members; health and sleep

([roundtrip_quotes_health](../../data/translation_test/roundtrip_quotes_health.md): 40 of 40 with the rule and recipes against 37 and 28 without them; the “quotes or roots” decisions of two coders matched in 24 of 24 against 18)

- **The quotes boundary.** From roots: categories and purposes: organ = `BODY INSIDE(=+5) PART(=-2) | o`, game = `FIGHT(=-5) | o`, sport = `FIGHT(=-5) BODY | o`, star = `HEAT(=+5) ABOVE(=+5) PART(=-2) | o`, planet = `PLACE ABOVE(=+5) MOVE | o`, satellite = `ABOVE(=+5) MOVE | o tool`, company = `PART(=+5) DO VALUE | o`, official = `SOMEONE RULE(=+4) | o`, railway = `PLACE MOVE LONG(=+5) | o`, broadcasting = `SAY GIVE(=+3) MANY(=+5) | o`. In quotes: specific members of a family in the international or Latin form (`"hepar"` liver, `"ren"` kidney, `"Sol"`, `"Luna"`, `"football"`, `"chess"`, `"protein"`) and narrow terms (`"enzyme"`, `"orbit"`, `"Parliament"`). The Moon cannot be read from roots (*horizon*, *sunset*), `"Luna"` gets 2 of 2.
- **Health and sleep are the middle of `LIVE`** (“half alive”), and `GOOD` says which: to sleep = `LIVE(=0) GOOD(=+3) | i`, dream = `LIVE(=0) SEE | o`, to wake up = `LIVE(=+5) BEGIN(=-4) | i`, tired = `LIVE(=0) CAN(=-3) | a`, to rest = `MOVE(=-5) GOOD(=+3) | i`; sick = `LIVE(=0) GOOD(=-4) | a`, illness = `LIVE(=0) GOOD(=-4) | o`, patient = `SOMEONE LIVE(=0) GOOD(=-4) | o`, hospital = `PLACE LIVE(=0) GOOD(=-4) | o`, healthy = `LIVE(=+5) GOOD(=+4) | a`, to treat = `LIVE GOOD(=+4) | i K+3`, doctor = `SOMEONE LIVE GOOD(=+4) | o`, medicine = `LIVE GOOD(=+4) | o tool`, to die = `LIVE(=-5) | i`, wound = `BODY JOIN(=-3) | o`, pain = `BODY FEEL(=+4) GOOD(=-4) | o`. The root `HEALTH` is not needed.

## Price, thoroughness, attachment

([roundtrip_value_care_join](../../data/translation_test/roundtrip_value_care_join.md))

- Price is the root `VALUE` (−5 cheap … +5 expensive): *expensive* = `VALUE(=+4) | a`, *cheap* = `VALUE(=-4) | a`, *price* = `VALUE | o`; 10 of 10. Buying and selling go with `GIVE`: *buy* = `GIVE(=-3) VALUE | i`, *sell* = `GIVE(=+3) VALUE | i`, but the decoder can confuse the direction.
- Thoroughness is the root `CARE` (−5 careless … +5 thorough): *carefully* = `CARE(=+3) | e`, *carelessly* = `CARE(=-3) | e`, *thoroughly* = `CARE(=+5) PART(=+2) | e`, *hastily* = `CARE(=-5) MOVE(=+4) | e`, *meticulous* = `CARE(=+5) PART(=-4) | a I+4`; 6 of 6.
- Attachment is the root `JOIN` (−5 to separate … +5 to attach): *join* = `JOIN(=+3) | i`, *separate* = `JOIN(=-3) PART | i`, *remove* = `JOIN(=-4) | i`; *add / attach / unite* merge, *add* is not read.

## Attitude to people

- The root `FRIEND` (−5 enemy, hostile, cruel … 0 neutral … +5 friend, friendly, kind; 2026-10, replaced `TONE` “rude … polite”: the centers of TONE and CARE were close, cos 0.65, for FRIEND and CARE 0.12): *friend* = `FRIEND | o`, *enemy* = `FRIEND(=-5) | o`, *kind, friendly* = `FRIEND(=+4) | a`, *hostile* = `FRIEND(=-5) | a`, *cruel* = `FRIEND(=-5) TOUCH(=+4) | a`, *warm* = `FRIEND(=+4) HEAT(=+2) | a`, *cold* = `FRIEND(=-3) HEAT(=-3) | a`.
- Politeness is a manner of speech: *polite* = `FRIEND(=+3) SAY CARE(=+3) | a`, *rude* = `FRIEND(=-3) SAY | a`, *tactful* = `FRIEND(=+3) CARE(=+5) | a`, *blunt* = `SAY CARE(=-3) | a`.
- Not checked: the test [roundtrip_tone](../../data/translation_test/roundtrip_tone.md) (26 of 32) was on the earlier `TONE`.

## Intake and output

([roundtrip_consume](../../data/translation_test/roundtrip_consume.md), 26 of 32 correct)

- The axis of `CONSUME`: −5 to emit, throw out … +5 to absorb, take in. The channel is set by the second root: *eat* = `CONSUME(=+5) GRAIN(=+3) | i`, *drink* = `CONSUME(=+5) GRAIN(=-3) | i`, *inhale* = `CONSUME(=+5) GRAIN(=-5) | i`, *exhale* = `CONSUME(=-5) GRAIN(=-5) | i`, *excrete* = `CONSUME(=-5) BODY | i`, *vomit* = `CONSUME(=-5) BODY ABOVE(=+3) | i`.
- Speech and hearing: *speak* = `CONSUME(=-5) SAY | i`, *listen* = `CONSUME(=+5) SAY CARE(=+3) | i`.
- Written language is the root `TEXT` (no axis; `SAY` is oral), [roundtrip_candidates](../../data/translation_test/roundtrip_candidates.md), 3 → 15 exact of 24: *write* = `TEXT | i`, *read* = `CONSUME(=+5) TEXT | i`, *writer* = `SOMEONE TEXT | o`, *author* = `TEXT | o agent`, *book* = `TEXT PART(=+2) | o`, *letter* = `TEXT GIVE(=+3) SOMEONE | o`, *newspaper* = `TEXT TIME(=0) PART(=+5) | o`, *library* = `PLACE TEXT PART(=+5) | o`. The earlier `CONSUME(=-5) SEE` (→ *show*) and `CONSUME(=+5) SEE` (→ *watch*) were not read.

## Causation

([roundtrip_causative](../../data/translation_test/roundtrip_causative.md), 25 of 32 correct, 3 more as a backup answer)

- The label `K` on a verb: the subject acts on the object `E` so that it performs or undergoes the action. `K-5` to forbid, `K-4` to prevent, `K-2` to dissuade, `K0` to allow, `K+3` to make / persuade, `K+4` to force, `K+5` to compel.
- What exactly is caused is set by the verb's root: *make* = `DO | i K+3`, *prevent* = `DO | i K-4`, *feed* = `CONSUME | i K+4`, *teach* = `KNOW | i K+4`, *frighten* = `FEEL(=+4) GOOD(=-4) | i K+4`, *force* = `DO WANT(=-5) | i K+5`, *persuade* = `SAY THINK(=+5) | i K+3`, *allow* = `RULE(=+3) | i K0`, *forbid* = `RULE(=+4) DO | i K-5`.
- *Induce / encourage* (`K+2…3`) get confused with *have / get / entice*.

## Concrete and abstract

There is no root `ABSTRACT` (v2; earlier the axis −5 tangible … +5 abstract, [roundtrip_abstract](../../data/translation_test/roundtrip_abstract.md), 25 of 32). No test: *idea* = `THINK | o result`, *principle* = `RULE THINK | o`, *imply* = `SAY THINK | i`, *tangible* = `TOUCH CAN(=+4) | a`, *abstract* = `TOUCH CAN(=-5) | a`, *theoretical* = `KNOW THINK | a`, *shake* = `MOVE(=+2) BODY | i`, *kick* = `TOUCH(=+4) MOVE(=+4) BODY | i`; *assume / suppose* = `THINK(=+3) | i M-1`.

## Concept recipes (two blind tests: [roundtrip_and_mod](../../data/translation_test/roundtrip_and_mod.md), round 2)

- Work: *game*, now `FIGHT(=-5) | o` (`FIGHT` has got an axis, see “Emotions, battle”; the earlier `FIGHT ART(=+2) | o` was also read); *independent*: `SOMEONE(=+5) CAN(=+5) JOIN(=-5) | a` (2/2); *help*: `DO GOOD(=+3) | i`; *exception*: `SAME(=-4) JOIN(=-5) RULE | o` (2/2 in [roundtrip_merge](../../data/translation_test/roundtrip_merge.md)); *equality*: `SAME(=+5) | o quality`; *economic*: `VALUE GIVE(=0) | a` (1/2).
- **Measures and ratios are the root `MEASURE`** (axis: −5 a quantity in itself … +5 a quantity relative to another; introduced after two failures with `PART`/`BIG`/`SAME`; blind test v2 26 of 32, [roundtrip_measure](../../data/translation_test/roundtrip_measure.md)): *ratio* `MEASURE(=+5) | o`, *percentage* `MEASURE(=+5) PART(=-2) | o`, *rate* `MEASURE(=+5) TIME | o`, *amount* `MEASURE(=-5) | o`, *size* `MEASURE(=-5) BIG | o`, *degree, level* `MEASURE(=0) | o`, *average* `MEASURE(=+5) MANY SAME | o`, *measurement* and *to measure* `MEASURE DO | o` / `MEASURE | i`, *unit* `MEASURE SAME | o`. Weak: *meter, dimension, proportional* (read as *distance/area/fractional*).
- Do not work (two series of recipes each, none read correctly): *way/method*, *measurement* as an *act of measuring* (now `MEASURE(=-5)`, but it reads as *meter / unit*), *a sort of X* (`I-2` on a noun does not read as “a kind”; *a sort of bird* → *bird*). `RULE(=-5)`/`SAME(=-5) RULE` for “independent” reads as *illegal*.
