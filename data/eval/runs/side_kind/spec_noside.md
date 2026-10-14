# min-co: how a word is written

A word is `ROOTS | FORM`.

- ROOTS: 1 to 3 roots. The first is the head: what kind of thing, action or quality it is. Each next root narrows everything before it.
- FORM: the part of speech, then optional marks.
  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb.
  - Example: `PLACE LIVE | o` = a place where one lives = house.

A root may carry a value on its axis, `ROOT(=v)`, with v from -5 to +5.
Every axis works the same way: -5 is the opposite pole, 0 the middle, +5 the full pole.
With no value, the root is meant plainly (`GOOD` = good, of unspecified degree).
Roots marked "no axis" never take a value.

## Roots (44)

- GOOD: -5 terrible … +5 excellent
- BIG: -5 tiny … +5 huge (size only)
- NEAR: -5 far, abroad, journey … +5 here, nearby, downtown, center
- ABOVE: -5 below, down … +5 above, up
- LIVE: -5 dead … -2 asleep … +5 alive
- SAME: -5 opposite, different … -4 special … +3 ordinary … +5 identical
- TIME: -5 long ago … 0 now … +5 far future (-1 just now, +1 soon)
- INSIDE: -5 outside … 0 on the border, at the edge, the surface … +5 inside
- PART: -5 particle, crumb … -2 a part, member … +2 the whole … +5 a group of many
- KNOW: -5 stupid, foolish, absurd … 0 aware … +5 know, inform, teach
- WANT: -5 hate, refuse … +5 love, crave
- HEAT: -5 ice cold … +5 fire hot
- BEGIN: -5 start … 0 ongoing … +5 end
- GIVE: -5 grab, seize, steal … 0 exchange, get … +5 give, donate, grant
- TOUCH: -5 soft, smooth, tender … +5 hard, stiff, tough, harsh
- SEX: -5 female … +5 male (only for words of explicit sex)
- HAPPEN: event, happen (no axis)
- THINK: -5 doubt … 0 think … +5 decide
- CAN: -5 impossible … -3 hard … +5 easy
- MANY: -5 none, never … -1 few … 0 some … +3 many … +5 all, always
- SOMEONE: -5 they, others … 0 someone … +3 you … +5 I
- THING: -5 stone, inanimate … 0 plant … +4 animal
- MOVE: -5 stand still … 0 walk … +5 rush
- FEEL: -5 calm … +5 excited, intense (pleasant or not is GOOD)
- RULE: -5 private, informal … +4 authority, institution … +5 law, official
- CHANGE: -5 stay the same … 0 change … +5 transform (the direction comes from the next root: `CHANGE GOOD(=+3)` improve)
- ART: -5 technology, exact science … +5 arts, humanities (the plain root means skill, craft)
- JOIN: -5 separate, remove … +5 join, add, attach
- VALUE: -5 cheap, a bargain, buying and selling … +5 precious, important, vital (price, worth)
- CARE: -5 careless, a mistake, fault … +5 careful, thorough, diligent
- FRIEND: -5 enemy, hostile, cruel … +5 friend, friendly, kind (attitude toward people)
- MOOD: -5 tragic … -3 sad … 0 serious … +3 glad … +5 funny
- CONSUME: -5 give out (emit, speak, write) … +5 take in (eat, drink, read, listen)
- MEASURE: -5 an amount (size, length, weight, quantity) … 0 a level, degree … +5 a ratio, rate, percentage, statistics
- LONG: -5 thread, cloth, textile … 0 wire, rod, fastening … +5 beam, plank, wooden furniture (long objects and what is made of them)
- SAY: -5 whisper … 0 speak … +5 shout (also noises)
- GRAIN: -5 gas … -3 liquid … 0 powder, grain … +5 one solid piece
- FIGHT: -5 game, sport … 0 quarrel … +5 war
- LAND: -5 sea, water … 0 shore, coast … +5 dry land, ground (the plain root means land, country, region)
- BODY: body (no axis)
- SEE: see, look (no axis)
- DO: do, make, act (no axis)
- PLACE: place (no axis)
- TEXT: written language, document (no axis)

## Form marks

Marks go after the part of speech. They are not roots and do not count toward the limit of 3.

Noun roles turn the meaning into a related noun:
- `agent`: the one who does it, or a person of that field (person or thing). `ART(=+5) | o agent` = artist. `TEXT | o agent` = writer, `HAPPEN | o agent` = cause.
- `tool`: the means or instrument. `TEXT | o tool` = pen, `JOIN(=-4) TOUCH(=+4) | o tool` = knife.
- `result`: what comes out of it. `HAPPEN | o result` = consequence, `TEXT | o result` = a text.
- `quality`: the quality or state itself. `GOOD | o quality` = goodness, `CAN | o quality` = ability.

Grammar marks, each with a value from -5 to +5; not written means unspecified:
- T: tense (-2 past, +2 future).
- R: event before (-3) or after (+3) the reference time.
- A: aspect (-5 beginning … +5 completed).
- N: number (+1 few, +3 plural, +5 all).
- M: negation and probability (-5 not, -3 maybe, +4 certainly).
- C: comparison (-3 less, +3 more, +5 most).
- I: intensity (-5 barely … +4 very, +5 utterly).
- D: definiteness (-3 a, +3 the).
- V: voice (-4 passive, +4 deliberate).
- K: make someone do it (-5 prevent … 0 let … +5 force).
- `!`: command.
- `?`: question.

Write the letter and the value together, without `(=`: `MOVE | i T-2` = moved, `SOMEONE | o N+3 D+3` = the people.

## Two words

A noun can be narrowed by a second noun: `X | o LINK Y | o`.
X is the kind, and Y narrows it. Each word has its own limit of 3 roots. LINK is the first of these that fits:
- `FROM`: X is made of Y.
- `FOR`: X is made for Y.
- `LIKE`: X looks like Y.
- `PI`: X is part of Y, or is found in Y.

## Quotes

Only proper names, digits and scientific names of particular species or substances are written in quotes: `"Rome"`, `"17"`, `"Canis"`, `"iodine"`.
Everything else is built from roots.

## Task

Each line is one code standing for ONE common English word in some sense. Give your best English word and 2 alternatives.


# Known recipes (codes verified by blind tests; read them as these words)

- Quotes: proper names, exact numbers (`"3"`), and specific members of a family that roots cannot tell apart, in international/Latin form: species (`"Canis"`), substances (`"iodine"`, `"protein"`), organs (`"hepar"` liver, `"ren"` kidney), celestial bodies (`"Sol"`, `"Luna"`), games (`"football"`), named institutions and narrow terms (`"Parliament"`, `"enzyme"`, `"orbit"`). Categories and functions are built from roots (organ `BODY INSIDE(=+5) PART(=-2) | o`, star `HEAT(=+5) ABOVE(=+5) PART(=-2) | o`, planet `PLACE ABOVE(=+5) MOVE | o`, company `PART(=+5) DO VALUE | o`, official `SOMEONE RULE(=+4) | o`, railway `PLACE MOVE LONG(=+5) | o`, broadcasting `SAY GIVE(=+3) MANY(=+5) | o`). Never quote what has a recipe.
- Health and sleep = middle of `LIVE` ("half alive") with `GOOD`: sleep `LIVE(=0) GOOD(=+3) | i`, sick `LIVE(=0) GOOD(=-4) | a`, disease `| o`, patient `SOMEONE LIVE(=0) GOOD(=-4) | o`, hospital `PLACE LIVE(=0) GOOD(=-4) | o`, tired `LIVE(=0) CAN(=-3) | a`, dream `LIVE(=0) SEE THINK | o`, wake `LIVE(=+5) BEGIN(=-4) | i`, healthy `LIVE(=+5) GOOD(=+4) | a`, heal `LIVE GOOD(=+4) | i K+3`, doctor `SOMEONE LIVE GOOD(=+4) | o`, medicine `LIVE GOOD(=+4) | o tool`, die `LIVE(=-5) | i`, wound `BODY JOIN(=-3) | o`, pain `BODY FEEL(=+4) GOOD(=-4) | o`.
- Actions without a root: `DO | i` (do, cause) or `SAY | i`. Difficult = `DO CAN(=-3) | a`. "Maybe" is the form label `M-3`, not a root. "And" is the particle `AND`, never JOIN/SAME/CHANGE.
- Amount: `MANY` (-5 none ... -4 lacking ... -3 hardly any ... -1 few ... 0 some ... +3 many ... +5 all). Food/drink: `CONSUME` (eat = `CONSUME(=+5) GRAIN(=+3) | i`, drink = `GRAIN(=-3)`).
- Degree is the form label I on the head word (very good = `GOOD(=+3) | a I+4`), never `BIG(=+5)` as "very". Small = `BIG(=-3)`. Earlier/later/before/after = label R, not TIME. `TIME(=+1)` reads as "soon".
- Time units: `TIME(=0) BIG(=n) | o` with BIG -5 second, -4 minute, -2 hour, 0 day, +1 week, +2 month, +3 year, +4 decade, +5 century. Yesterday `TIME(=-1) BIG(=0) | e`, tomorrow `TIME(=+1) BIG(=0) | e`, today `TIME(=0) BIG(=0) NEAR(=+5) | e`. Part of day: `TIME(=0) BIG(=0) BEGIN(=n) | o` (-4 morning, 0 noon, +3 evening, +5 night). Annual `TIME(=0) BIG(=+3) MANY(=+5) | a`.
- Compass: `PLACE` + direction, facing sunrise: north `PLACE ABOVE(=+5) | o` (top of the map), south `ABOVE(=-5)`.
- Direction of motion: with `MOVE`/`GIVE`/`DO`, the value of `INSIDE`/`NEAR`/`ABOVE` is where the motion ends: enter `MOVE INSIDE(=+5) | i`, exit `MOVE INSIDE(=-5) | i`, arrive `MOVE NEAR(=+5) | i`, leave `MOVE NEAR(=-5) | i`, rise `MOVE ABOVE(=+5) | i`, return `MOVE SAME(=+5) | i`. Moving something else adds `K+3`: insert `MOVE INSIDE(=+5) | i K+3`, extract/take out `MOVE INSIDE(=-5) | i K+3`, bring `MOVE NEAR(=+5) | i K+3`, send `MOVE NEAR(=-5) | i K+3`.
- Law: crime `DO GOOD(=-4) RULE(=+4) | o`, criminal `SOMEONE GOOD(=-4) RULE(=+4) | o`, court `PLACE RULE(=+4) THINK(=+5) | o`, judge `SOMEONE RULE(=+4) THINK(=+5) | o`, prison `PLACE MOVE(=-5) RULE(=+4) | o`, steal `GIVE(=-4) GOOD(=-4) | i`.
- Money: money `VALUE GIVE(=0) | o`, pay `VALUE GIVE(=+4) | i` (sell `GIVE(=+3) VALUE | i`), debt `VALUE GIVE(=+4) TIME(=+3) | o`, rich `VALUE MANY(=+5) | a`, poor `VALUE MANY(=-4) | a`, market `PLACE GIVE(=0) VALUE | o`.
- Food: meat `CONSUME(=+5) THING(=+4) | o`, vegetable `CONSUME(=+5) THING(=0) | o`, cook `HEAT(=+3) CONSUME(=+5) | i`, kitchen `PLACE HEAT(=+3) CONSUME(=+5) | o`, farm `PLACE THING(=0) DO | o`, harvest `GIVE(=-4) THING(=0) PART(=+5) | i`.
- Vehicles are tools, not stones: car `MOVE(=+4) | o tool`, ship `MOVE GRAIN(=-3) | o tool`; road `PLACE MOVE LONG(=-3) | o`, bridge `PLACE MOVE ABOVE(=+4) | o`, house `PLACE INSIDE(=+5) LIVE | o`, room `PLACE INSIDE(=+5) PART(=-2) | o`. Don't quote what has a recipe.
- Society: trust `THINK(=+5) GOOD(=+4) | i`, friend `FRIEND | o`, kind `FRIEND(=+4) | a`, ally `FRIEND FIGHT | o`, agreement `THINK(=+5) SAME(=+5) | o`, safe `GOOD(=-4) CAN(=-5) | a`.
- Power: king `SOMEONE RULE(=+5) SEX(=+5) | o`, government `SOMEONE RULE(=+5) PART(=+5) | o`, vote `THINK(=+5) MANY(=+5) | i`, election `THINK(=+5) MANY(=+5) RULE(=+4) | o`, citizen `SOMEONE PART(=-2) RULE(=+4) | o`, city `PLACE SOMEONE MANY(=+5) | o`.
- School: school `PLACE KNOW CONSUME(=+5) | o`, student `SOMEONE KNOW CONSUME(=+5) | o`, teacher `SOMEONE KNOW GIVE(=+4) | o`, university `PLACE KNOW ABOVE(=+4) | o`; film `ART(=+5) SEE MOVE | o`, advertise `SAY GIVE(=+3) VALUE | i`.
- War: enemy `FRIEND(=-5) | o`, battle `FIGHT(=+5) PART(=-2) | o`, weapon `FIGHT(=+5) | o tool`, gun `FIGHT(=+5) HEAT(=+5) | o tool`, defend `DO GOOD(=-4) | i K-4`, attack `FIGHT(=+4) BEGIN(=-5) | i`.
- Mood = `MOOD` (−5 grief, despair … −3 sad … 0 serious … +3 cheerful … +5 funny), not `FEEL GOOD`: funny `MOOD(=+5) | a`, joke `SAY MOOD(=+5) | o`, humor `MOOD(=+5) | o quality`, comedy `ART MOOD(=+5) | o`, laugh `MOOD(=+5) | i`, cheerful `MOOD(=+3) | a`, smile `MOOD(=+3) BODY | i`, party `MOOD(=+3) PART(=+5) | o`, celebrate `DO MOOD(=+3) PART(=+5) | i`, serious `MOOD(=0) | a`, sad `MOOD(=-3) | a`, cry `MOOD(=-3) CONSUME(=-5) GRAIN(=-3) | i`, grief `MOOD(=-5) | o`, despair `MOOD(=-5) CAN(=-5) | o`, mourn `MOOD(=-5) LIVE(=-5) | i`, funeral `MOOD(=-5) LIVE(=-5) PART(=+5) | o`, tragedy `ART MOOD(=-5) | o`. Happy is evaluation: `FEEL(=+4) GOOD(=+4) | a`.
- Age = `LIVE TIME(=n)` (since when it lives): young `LIVE TIME(=-1) | a`, old `LIVE TIME(=-5) | a`, youth `SOMEONE LIVE TIME(=-1) | o N+3`, age `LIVE TIME MEASURE | o`; ancient (things) `TIME(=-5) | a`.
- Music: sing `SAY ART(=+5) FEEL(=+3) | i`, song `| o`, singer `SOMEONE SAY FEEL(=+3) | o`, music `ART(=+5) SAY THING | o`, dance `ART(=+5) MOVE BODY | i`. Not TEXT (reads as poem).
- Water places are `PLACE GRAIN(=-3)`: sea `PLACE GRAIN(=-3) BIG(=+5) | o`, lake `BIG(=0)`, river `PLACE GRAIN(=-3) MOVE(=+3) | o`, island `PLACE GRAIN(=-3) INSIDE(=+5) | o`, shore `PLACE GRAIN(=-3) NEAR(=+4) | o`; mountain `PLACE ABOVE(=+5) BIG(=+4) | o`.
- Success: win `FIGHT GOOD(=+4) | i`, lose `FIGHT GOOD(=-4) | i`, victory `FIGHT GOOD(=+4) | o result`, success `DO GOOD(=+4) | o result`, fail `DO GOOD(=-4) | i`, famous `KNOW MANY(=+5) | a`.
- PART ladder: -5 crumb, -2 part/member, +2 whole/entire, +5 group. Society = `SOMEONE PART(=+5)`, member = `SOMEONE PART(=-2)`, herd = `THING(=0) PART(=+5)`.
- GRAIN (how stuff holds together, also solid/liquid/gas): -5 gas, steam, smoke, -3 liquid, flowing (water, honey), 0 loose/granular (sand, flour, dust, rice, gravel: add THING/PART/CONSUME to tell them apart), +5 one solid piece. Solid/whole/seamless = `GRAIN(=+5) | a`. Do not write "seamless" with `JOIN(=-5)` (reads as "separate"). Continuous in time: `GRAIN(=+5) TIME | a A0` or `BEGIN(=0) PART(=+2) | a` (BEGIN(=0) = going on).
- Numbers and maths: number `MEASURE(=-5) MANY | o`; zero `MANY(=-5) MEASURE(=-5) | o`; count (verb) `MEASURE MANY DO | i`; sum `MANY JOIN(=+4) MEASURE(=-5) | o`; equal `SAME(=+5) MEASURE | a`; calculate `ART(=-5) THINK MEASURE | i`; fraction `PART(=-2) MEASURE(=+5) | o`; percentage/ratio `MEASURE(=+5) ...`; mathematics `ART(=-5) MANY SEE | o`.
- ART axis: -5 calculation/technique ... +5 creative/humanities (poetry `ART(=+5) SAY | o`, physics `ART(=-4) GRAIN MOVE | o`). Person of a craft: `SOMEONE ART(=-4) DO | o` (engineer).
- Emotions: `FEEL` + `GOOD` + root: fear = `FEEL(=+4) GOOD(=-4) TIME(=+3) | i`; hope = `WANT(=+4) GOOD(=+4) TIME(=+3) | a`.
- Other axes: `VALUE` (-5 cheap ... +5 expensive), `FRIEND` (-5 enemy, hostile ... +5 friend, kind; toward people), `CARE` (-5 careless, lazy ... +5 careful, diligent; toward a task; carefully = `CARE(=+3) | e`), idea = `THINK | o result`, `RULE` (-5 private ... +5 official; authority = `RULE(=+4) | o`), `CHANGE` (remain = `CHANGE(=-4) | i`, grow = `CHANGE BIG(=+3) | i`).
- Metaphors fail: use ABOVE/INSIDE/BIG only for real up/inside/size. Write values as `(=+3)`, `(=-2)`, `(=0)`, never `+0`.
- Written language is the root `TEXT` (`SAY` is spoken): write `TEXT | i`, read `CONSUME(=+5) TEXT | i`, writer `TEXT | o agent`, book `TEXT PART(=+2) | o`, letter `TEXT GIVE(=+3) SOMEONE | o`, library `PLACE TEXT PART(=+5) | o`.
- FIGHT axis: -5 game/sport ... 0 brawl/quarrel ... +5 war. game `FIGHT(=-5) | o`, player `SOMEONE FIGHT(=-5) | o`, sport `FIGHT(=-5) BODY | o`, war `FIGHT(=+5) | o`, soldier `SOMEONE FIGHT(=+5) RULE(=+4) | o`.
- Roles after `| o`: the roots describe the action, the role names the noun: `tool` knife `JOIN(=-4) TOUCH(=+4) | o tool`, hammer `TOUCH(=+5) MOVE(=+4) | o tool`, pen `TEXT | o tool`, thermometer `MEASURE HEAT | o tool`; `agent` writer `TEXT | o agent`, cause `HAPPEN | o agent`; `result` consequence `HAPPEN | o result`; `quality` ability `CAN | o quality`. Never `THING(=-5)` for tools (reads as stone).
- Special / general is the SAME axis: special, unique `SAME(=-4) | a`, especially `SAME(=-4) | e I+4`, ordinary `SAME(=+3) | a`, general `SAME(=+4) MANY(=+5) | a`.
