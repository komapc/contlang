# Лакуны: перевод без ограничения числа корней

Скрипт `scripts/20_lacunae.py`. 9647 частых слов (без слов-полюсов), словарь — корни из полюсов (44 корней). Попадание — среди 10 ближайших к коду есть слово с той же основой.

| кодер | в top10 | cos(x,y) | корней в коде (медиана / макс.) |
| :-- | --: | --: | --: |
| жадный, без предела корней, целые уровни | 63.0% | 0.403 | 8 / 24 |
| то же, только обычные слова (2016) | 86.5% | 0.472 | 8 / 22 |
| потолок: проекция на все центры и оси | 99.9% | 0.585 | все |

Потолок — хеш-эффект (docs/math.md, раздел 3): 84 свободных коэффициента различают почти любое слово, смысла это не добавляет; для лакун он не годится.

Промахи среди всех слов — большей частью имена, страны, города, названия (идут в кавычках). Ниже — только обычные слова: 273 промахов из 2016.

## Кластеры промахов

Слова, ближайшие к среднему остатку (чего не хватает коду), и промахи кластера (первые по частоте).

### 19 слов: psychiatric, clinical, health, medical

- остаток ближе всего к: psychiatric, clinical, health, medical, illness, diseases, illnesses, disease
- промахи: health, hospital, medical, care, drug, disease, cancer, marriage, gay, mental, prevention, clinical, psychological, cigarette, chronic, anxiety, cure, infectious, psychologist

### 17 слов: naval, captain, navy, sailors

- остаток ближе всего к: naval, captain, navy, sailors, admiral, lieutenant, commander, ships
- промахи: british, nuclear, station, coast, ship, captain, crew, fish, naval, lieutenant, regiment, colonel, brigade, humor, slave, sail, brass

### 17 слов: loans, finance, financial, lending

- остаток ближе всего к: loans, finance, financial, lending, loan, finances, fund, financing
- промахи: bank, financial, agency, tax, aid, fund, net, credit, finance, trust, loan, earthquake, cent, rob, tsunami, rebuild, borrow

### 16 слов: christ, christianity, theological, evangelical

- остаток ближе всего к: christ, christianity, theological, evangelical, theology, christian, church, christians
- промахи: church, cross, jewish, god, faith, religion, moral, spiritual, christ, devil, congregation, sin, theology, biblical, theological, dictionary

### 16 слов: security, guarantee, guarantees, safeguard

- остаток ближе всего к: security, guarantee, guarantees, safeguard, safety, protection, ensuring, protect
- промахи: security, defense, safety, risk, cover, guard, confidence, guarantee, payment, customer, proof, provision, bet, battery, threaten, violate

### 14 слов: promote, reinforce, promoting, promoted

- остаток ближе всего к: promote, reinforce, promoting, promoted, promotes, exclusively, emphasize, advertising
- промахи: newspaper, serve, promote, guide, pursue, print, muscle, exclusively, stamp, solely, recruit, buzz, reinforce, emphasize

### 14 слов: democratic, election, democrat, elections

- остаток ближе всего к: democratic, election, democrat, elections, electoral, voters, voter, electorate
- промахи: election, campaign, vote, democratic, presidential, leadership, communist, editor, liberal, electoral, citizen, elect, sympathy, communism

### 14 слов: summer, year, summers, spring

- остаток ближе всего к: summer, year, summers, spring, month, winter, months, autumn
- промахи: year, month, young, period, summer, camp, spring, decade, garden, resort, compound, hire, tent, bee

### 13 слов: nation, national, culture, cultural

- остаток ближе всего к: nation, national, culture, cultural, society, nations, country, societies
- промахи: state, international, men, nation, king, society, culture, cultural, irish, truth, proud, lie, conscience

### 11 слов: trial, trials, jury, verdict

- остаток ближе всего к: trial, trials, jury, verdict, defendants, prosecution, defendant, judge
- промахи: research, test, trial, justice, guilty, jury, suit, dry, laboratory, judgment, sue

### 11 слов: arrests, arrest, arrested, crime

- остаток ближе всего к: arrests, arrest, arrested, crime, crimes, warrants, warrant, police
- промахи: police, news, violence, threat, crime, arrest, article, cell, resign, conviction, warrant

### 11 слов: growth, commercial, business, development

- остаток ближе всего к: growth, commercial, business, development, market, businesses, industry, markets
- промахи: market, business, growth, success, commercial, industrial, baby, improvement, protein, mature, ear

### 10 слов: flight, flights, flying, fly

- остаток ближе всего к: flight, flights, flying, fly, airplane, wings, plane, bird
- промахи: book, hotel, flight, plane, wing, fly, transfer, bird, duck, accompany

### 10 слов: school, college, students, student

- остаток ближе всего к: school, college, students, student, schools, ucla, university, colleges
- промахи: school, university, college, class, hall, professor, teacher, grade, institution, parent

### 9 слов: congress, congressional, subcommittee, senate

- остаток ближе всего к: congress, congressional, subcommittee, senate, legislature, committee, legislative, caucus
- промахи: federal, committee, conference, congress, commission, session, legislative, passage, stomach

### 9 слов: sixth, fifth, seventh, eighth

- остаток ближе всего к: sixth, fifth, seventh, eighth, ninth, fourth, third, tenth
- промахи: century, fourth, mark, fifth, sixth, eighth, ninth, substitute, intermediate

### 8 слов: township, district, town, county

- остаток ближе всего к: township, district, town, county, village, districts, municipality, valley
- промахи: town, district, county, river, village, valley, forest, municipal

### 8 слов: hitter, baseman, pitchers, pitcher

- остаток ближе всего к: hitter, baseman, pitchers, pitcher, baseball, fielder, catcher, inning
- промахи: player, baseball, older, defensive, inning, pat, pitcher, ace

### 8 слов: evening, afternoon, morning, tonight

- остаток ближе всего к: evening, afternoon, morning, tonight, night, midday, noon, saturday
- промахи: night, today, radio, morning, afternoon, rain, tonight, sing

### 8 слов: chicago, metropolitan, suburbs, suburban

- остаток ближе всего к: chicago, metropolitan, suburbs, suburban, suburb, downtown, city, paris
- промахи: europe, paris, chicago, downtown, metropolitan, suburb, suburban, shoe

### 7 слов: moon, planet, lunar, mars

- остаток ближе всего к: moon, planet, lunar, mars, venus, orbit, suns, earth
- промахи: species, sun, moon, planet, spectrum, lunar, civilization

### 6 слов: moreover, furthermore, besides, additionally

- остаток ближе всего к: moreover, furthermore, besides, additionally, meanwhile, likewise, nevertheless, whereas
- промахи: meanwhile, rich, obviously, besides, moreover, furthermore

### 6 слов: movie, film, films, movies

- остаток ближе всего к: movie, film, films, movies, filmed, comedy, filming, cinema
- промахи: film, song, movie, comedy, kiss, naked

### 6 слов: south, west, eastern, east

- остаток ближе всего к: south, west, eastern, east, north, western, southern, southeast
- промахи: south, north, west, southern, western, eastern

### 5 слов: pistol, rifle, rifles, gun

- остаток ближе всего к: pistol, rifle, rifles, gun, firearms, barrel, guns, ammunition
- промахи: magazine, barrel, rifle, pistol, snake

## Примеры кодов промахов

| слово | код | ближайшие к коду |
| :-- | :-- | :-- |
| year | `TIME(=-1) MEASURE(=0) BEGIN(=+1)` | previous, lasted, before, after, prior |
| state | `RULE(=+1) PLACE` | jurisdiction, governing, rules, laws, regulations |
| south | `PLACE SIDE(=+1) HEAT(=0) NEAR(=-1) ABOVE(=+2) INSIDE(=-2)` | areas, beyond, across, places, locations |
| police | `RULE(=+2) SOMEONE(=-2) THING(=+2) FIGHT(=+3) INSIDE(=-1) TIME(=-2) DO(=-2) GIVE(=-2) SEX(=-2) TONE(=0)` | her, before, officers, she, officials |
| international | `FIGHT(=-5) BIG(=+5) RULE(=+1) JOIN(=+5) SAY(=+5) TIME(=-1) DO(=-3) BODY PART(=+3) MOVE(=+2) INSIDE(=-1) VALUE(=-1)` | competitions, compete, competition, contests, competing |
| school | `ART(=0) ABOVE(=+4) RULE(=-1) FIGHT(=-2) SEX(=-1) PART(=+4) SIDE(=-4) MANY(=-1) TIME(=0)` | her, his, other, with, and |
| news | `TIME(=+1) TEXT SEE GOOD(=-2) PART(=-2) RULE(=+1) LIVE(=0) LONG(=0) GIVE(=+3) MOVE(=+3) KNOW(=-1)` | announcement, next, before, tells, shortly |
| north | `NEAR(=0) HEAT(=-2) PLACE SIDE(=+2) ABOVE(=+2)` | farther, across, at, closer, off |
| security | `RULE(=0) ART(=-3) INSIDE(=+1) GIVE(=-1)` | electronic, computer, computers, own, technical |
| market | `VALUE(=-2) PLACE THING(=+2) TIME(=+2) ABOVE(=-2) GRAIN(=+1) PART(=+3) NEAR(=+5) MEASURE(=+2) DO(=0) WANT(=+2) FIGHT(=0)` | at, locations, items, in, prices |
| university | `ART(=-1) RULE(=+1) NEAR(=+2)` | electronic, science, technical, computers, sciences |
| month | `TIME(=-1) BEGIN(=0) MEASURE(=0)` | previous, before, lasted, after, prior |
| bank | `SIDE(=+2) RULE(=+1) PLACE LONG(=0) TOUCH(=0) SAME(=-2)` | side, sides, on, areas, across |
| business | `RULE(=0) ART(=-1) INSIDE(=+1) DO(=-1) VALUE(=-2) BEGIN(=-3) PLACE` | begins, starts, starting, began, begun |
| west | `PLACE ABOVE(=+3) SIDE(=0) NEAR(=-1) INSIDE(=-2)` | beyond, across, farther, around, places |
| british | `RULE(=+1) MEASURE(=-2) GRAIN(=-1) DO(=-2) FIGHT(=+3) TIME(=0) GIVE(=-2) THING(=-1) SEX(=0) INSIDE(=+2) WANT(=-3) LONG(=-1) MANY(=+5) HAPPEN(=0)` | each, the, in, during, whole |
| men | `SOMEONE(=-2) SEX(=+2) PART(=+3) FIGHT(=0) BEGIN(=-1) MEASURE(=-1)` | ones, those, these, groups, his |
| film | `DO(=-3) ART(=+2) TEXT LONG(=-3) TIME(=+3) GOOD(=-2) SEE` | artist, actors, actress, writer, artists |
| town | `PLACE BIG(=-2) NEAR(=+2)` | located, locations, places, situated, proximity |
| federal | `RULE(=+2)` | laws, governing, rules, regulations, jurisdiction |
| health | `LIVE(=+2) RULE(=-1) THING(=+1) INSIDE(=+3) CONSUME(=+1) MEASURE(=-2)` | contains, inner, lives, in, live |
| night | `TIME(=0) FEEL(=-2) BEGIN(=+3) MANY(=+2) HEAT(=0) SAY(=0) PLACE` | next, until, during, before, after |
| election | `HAPPEN(=+3) FIGHT(=-1) THINK(=+3) RULE(=+3) MANY(=+2) ABSTRACT(=-4) ART(=-1) TIME(=+1)` | results, consequences, decides, ensuing, decisions |
| today | `TIME(=0)` | before, next, sometime, previous, after |
| district | `PLACE RULE(=+1)` | locations, venue, areas, places, sites |
| county | `PLACE RULE(=+2) THING(=+1) FIGHT(=-1)` | venue, locations, places, competitions, venues |
| financial | `RULE(=0) ART(=-2) ABOVE(=-3) THINK(=-1) INSIDE(=-2) GIVE(=+3) HAPPEN(=+2) BIG(=+1)` | substantial, significant, given, limited, accept |
| campaign | `FIGHT(=0)` | battle, battles, fighting, war, wars |
| agency | `RULE(=+1) DO(=-2)` | governing, rules, laws, administrative, administrator |
| committee | `RULE(=+2) PART(=+4) TIME(=+1) THINK(=+1) TEXT TOUCH(=0)` | decides, governing, rules, ruling, guidelines |
| conference | `FIGHT(=-2) TIME(=+2) PLACE RULE(=0) SAY(=-1) PART(=+3) GOOD(=-2) ART(=-2) TEXT` | tournaments, competitions, event, events, venue |
| young | `BIG(=-2) SEX(=0) TIME(=-1) THINK(=-2) PART(=+3) LIVE(=0) FIGHT(=-2)` | few, youngest, smallest, handful, some |
| defense | `FIGHT(=+2) RULE(=+4) SIDE(=+2) ABSTRACT(=+1) TIME(=-5) MOVE(=0) ART(=-2) CAN(=-3) GIVE(=+1)` | before, battles, fighting, force, battle |
| southern | `PLACE HEAT(=0) NEAR(=-1) SIDE(=+2) BIG(=0) INSIDE(=-1) TIME(=-3) FIGHT(=+1) GRAIN(=-1) RULE(=+3)` | areas, in, before, the, regions |
| nuclear | `ART(=-5) GRAIN(=-2) PART(=-3) FIGHT(=+2) THING(=0) BEGIN(=0) NEAR(=+2) MEASURE(=+4) BIG(=+4) TEXT` | quantum, massive, machines, particles, computer |
| college | `ART(=0) MEASURE(=+3) FIGHT(=-2) TIME(=0) RULE(=0) ABOVE(=+4)` | higher, highest, overs, averaged, averaging |
| church | `ABSTRACT(=-1) INSIDE(=0) SEX(=-1)` | walls, doors, grandmother, home, mom |
| nation | `PLACE MANY(=+4) RULE(=+2) LONG(=-2) MEASURE(=+3) SOMEONE(=-3) FIGHT(=+1) SEX(=+1) PART(=0)` | each, ones, everybody, places, those |
| station | `NEAR(=+2) GRAIN(=-1) PLACE LONG(=+3) WANT(=-1) DO(=-1)` | located, proximity, nearest, beside, locations |
| research | `ART(=-2) CARE(=+2) GIVE(=+3) TEXT FIGHT(=+2) PART(=+2) NEAR(=+1) HAPPEN(=-2) VALUE(=+2) BODY HEAT(=-3) RULE(=-1)` | computer, computers, equipment, technical, parts |
