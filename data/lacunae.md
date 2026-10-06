# Лакуны: перевод без ограничения числа корней

Скрипт `scripts/20_lacunae.py`. 9649 частых слов (без слов-полюсов), словарь — корни из полюсов (44 корней). Попадание — среди 10 ближайших к коду есть слово с той же основой.

| кодер | в top10 | cos(x,y) | корней в коде (медиана / макс.) |
| :-- | --: | --: | --: |
| жадный, без предела корней, целые уровни | 63.3% | 0.405 | 8 / 24 |
| то же, только обычные слова (2017) | 86.6% | 0.474 | 8 / 22 |
| потолок: проекция на все центры и оси | 99.9% | 0.586 | все |

Потолок — хеш-эффект (docs/math.md, раздел 3): 84 свободных коэффициента различают почти любое слово, смысла это не добавляет; для лакун он не годится.

Промахи среди всех слов — большей частью имена, страны, города, названия (идут в кавычках). Ниже — только обычные слова: 270 промахов из 2017.

## Кластеры промахов

Слова, ближайшие к среднему остатку (чего не хватает коду), и промахи кластера (первые по частоте).

### 19 слов: dignity, moral, conscience, integrity

- остаток ближе всего к: dignity, moral, conscience, integrity, morale, pride, ethical, loyalty
- промахи: king, society, culture, leadership, confidence, irish, queen, truth, tradition, moral, proud, resign, humor, slave, sympathy, dignity, naked, violate, conscience

### 18 слов: disease, diseases, cure, chronic

- остаток ближе всего к: disease, diseases, cure, chronic, symptoms, illness, cancer, illnesses
- промахи: book, disease, cancer, garden, resort, advice, dry, guide, improvement, compound, muscle, rebuild, chronic, stomach, anxiety, cure, weaken, infectious

### 16 слов: christ, christianity, christian, evangelical

- остаток ближе всего к: christ, christianity, christian, evangelical, theology, church, jesus, christians
- промахи: church, cross, jewish, god, marriage, gay, faith, religion, spiritual, christ, sing, devil, sin, theology, biblical, theological

### 16 слов: medical, psychiatric, clinical, psychological

- остаток ближе всего к: medical, psychiatric, clinical, psychological, hospitals, physician, mental, doctors
- промахи: british, health, hospital, medical, drug, legal, cultural, doctor, naval, mental, provision, clinical, psychological, shoe, dictionary, psychologist

### 15 слов: election, democratic, electoral, presidential

- остаток ближе всего к: election, democratic, electoral, presidential, elections, democrat, republican, voter
- промахи: president, national, election, campaign, vote, democratic, congress, presidential, candidate, liberal, legislative, electoral, enemy, lie, oath

### 15 слов: commercial, marketing, sales, business

- остаток ближе всего к: commercial, marketing, sales, business, marketed, corporate, corporation, company
- промахи: international, growth, song, management, success, commercial, promote, distribution, corporation, pursue, customer, residential, hire, exclusively, solely

### 13 слов: school, college, schools, ucla

- остаток ближе всего к: school, college, schools, ucla, colleges, student, professors, university
- промахи: school, university, village, summer, hall, camp, professor, spring, forest, teacher, institution, instruction, recruit

### 13 слов: security, safety, safeguard, protection

- остаток ближе всего к: security, safety, safeguard, protection, protect, protecting, prevention, ensuring
- промахи: security, defense, safety, risk, threat, guard, responsibility, guarantee, passage, prevention, threaten, reinforce, emphasize

### 12 слов: decade, century, year, years

- остаток ближе всего к: decade, century, year, years, decades, period, centuries, era
- промахи: year, month, period, century, mark, net, communist, older, decade, medieval, mature, communism

### 11 слов: sentencing, conviction, verdict, prosecution

- остаток ближе всего к: sentencing, conviction, verdict, prosecution, defendants, judge, defendant, jury
- промахи: court, trial, justice, guilty, jury, sentence, proof, conviction, judgment, warrant, battery

### 11 слов: west, eastern, western, south

- остаток ближе всего к: west, eastern, western, south, east, southern, north, northern
- промахи: state, south, north, west, union, southern, europe, western, river, eastern, valley

### 11 слов: fly, flight, flying, flies

- остаток ближе всего к: fly, flight, flying, flies, flown, flights, airplane, wings
- промахи: flight, plane, wing, fish, fly, suit, bird, bee, sail, buzz, accompany

### 10 слов: afternoon, evening, morning, tonight

- остаток ближе всего к: afternoon, evening, morning, tonight, night, midday, noon, saturday
- промахи: night, today, conference, morning, session, afternoon, rain, tonight, rob, tent

### 10 слов: planet, moon, lunar, earth

- остаток ближе всего к: planet, moon, lunar, earth, venus, spacecraft, orbit, galaxy
- промахи: species, ship, sun, earthquake, moon, planet, tsunami, spectrum, lunar, civilization

### 10 слов: newspaper, magazine, newspapers, editorial

- остаток ближе всего к: newspaper, magazine, newspapers, editorial, reporter, headlines, reporters, news
- промахи: news, local, radio, newspaper, interview, magazine, cover, editor, article, print

### 10 слов: loans, loan, lending, credit

- остаток ближе всего к: loans, loan, lending, credit, payments, debt, borrowing, mortgage
- промахи: bank, bill, tax, credit, finance, hotel, loan, transfer, payment, borrow

### 10 слов: police, detectives, detective, lieutenant

- остаток ближе всего к: police, detectives, detective, lieutenant, sergeant, arrests, policeman, policemen
- промахи: police, men, violence, investigation, crime, arrest, lieutenant, regiment, colonel, detective

### 10 слов: furthermore, moreover, additionally, meanwhile

- остаток ближе всего к: furthermore, moreover, additionally, meanwhile, besides, nevertheless, likewise, nonetheless
- промахи: meanwhile, obviously, preliminary, besides, pat, substitute, bet, moreover, sue, furthermore

### 9 слов: metropolitan, city, suburban, suburbs

- остаток ближе всего к: metropolitan, city, suburban, suburbs, chicago, suburb, minneapolis, metro
- промахи: city, federal, county, paris, chicago, municipal, metropolitan, suburb, suburban

### 7 слов: baseball, pitcher, baseman, pitchers

- остаток ближе всего к: baseball, pitcher, baseman, pitchers, hitter, fielder, catcher, inning
- промахи: player, baseball, defensive, inning, pitcher, hat, ace

### 7 слов: egg, eggs, duck, protein

- остаток ближе всего к: egg, eggs, duck, protein, cell, cells, young, baby
- промахи: young, cell, baby, protein, egg, ear, duck

### 5 слов: sixth, seventh, fifth, eighth

- остаток ближе всего к: sixth, seventh, fifth, eighth, ninth, fourth, tenth, third
- промахи: fourth, fifth, sixth, eighth, ninth

### 5 слов: pistol, rifle, rifles, gun

- остаток ближе всего к: pistol, rifle, rifles, gun, firearms, barrel, guns, barrels
- промахи: barrel, rifle, cigarette, pistol, snake

### 4 слов: grade, grades, intermediate, test

- остаток ближе всего к: grade, grades, intermediate, test, tests, exam, class, classes
- промахи: test, rich, grade, intermediate

### 3 слов: movie, film, films, movies

- остаток ближе всего к: movie, film, films, movies, cinema, comedy, filmed, filming
- промахи: film, movie, comedy

## Примеры кодов промахов

| слово | код | ближайшие к коду |
| :-- | :-- | :-- |
| year | `TIME(=-1) MEASURE(=0) BEGIN(=+1)` | previous, lasted, before, after, prior |
| president | `RULE(=+4) TIME(=-2) SEX(=+2) DO(=-3) GIVE(=+2) SIDE(=+3) ART(=-3) TONE(=-1)` | commissions, commissioners, commissioner, chairman, secretary |
| state | `RULE(=+1) PLACE FIGHT(=-2) MOVE(=-1)` | commissions, agencies, officials, commissioners, council |
| city | `PLACE RULE(=+2) LIVE(=+2)` | areas, places, locations, district, council |
| national | `RULE(=+1) FIGHT(=-2)` | commissions, commissioners, agencies, governmental, officials |
| south | `PLACE SIDE(=+1) HEAT(=0) NEAR(=-1) ABOVE(=+2) INSIDE(=-2)` | areas, beyond, across, places, locations |
| police | `RULE(=+2) SOMEONE(=-1) THING(=+2) FIGHT(=+2) INSIDE(=-1) SEX(=-2)` | agencies, authorities, commissions, officials, governments |
| international | `FIGHT(=-5) BIG(=+5) RULE(=+2) JOIN(=+5) SAY(=+5) TIME(=-1) DO(=-3) BODY MOVE(=+2) PART(=+3) INSIDE(=-1) VALUE(=-1)` | competitions, compete, competition, competing, crowd |
| school | `ART(=0) ABOVE(=+4) RULE(=0) FIGHT(=-2) TIME(=0) PART(=+4) SIDE(=-4) SEX(=-1) MANY(=-1)` | her, his, and, with, after |
| news | `TIME(=+1) TEXT SEE RULE(=0) GOOD(=-2) PART(=-3) LIVE(=0) MOVE(=+3) KNOW(=0) LONG(=0) GIVE(=+3)` | tells, announcement, next, before, quick |
| north | `NEAR(=0) HEAT(=-2) PLACE SIDE(=+2) ABOVE(=+2)` | farther, across, at, closer, off |
| security | `RULE(=0) ART(=-3) INSIDE(=+1) GIVE(=-1) CHANGE(=-3)` | keep, hold, keeps, holds, maintain |
| court | `RULE(=+1) FIGHT(=-1) SIDE(=+2) THINK(=+2)` | commissions, decides, commissioners, council, committees |
| university | `ART(=-1) RULE(=+1) NEAR(=+1) HEAT(=0) BEGIN(=+1)` | science, computers, computer, electrical, ends |
| month | `TIME(=-1) BEGIN(=0) MEASURE(=0)` | previous, before, lasted, after, prior |
| bank | `RULE(=+1) SIDE(=+2) LONG(=+1) NEAR(=+2) HEAT(=-1)` | committees, commissions, officials, council, on |
| local | `PLACE RULE(=0) INSIDE(=-1) HAPPEN(=-2) BIG(=-1) NEAR(=+3) LONG(=0) TIME(=0)` | locations, areas, located, places, surrounding |
| west | `PLACE ABOVE(=+3) SIDE(=0) NEAR(=-1) INSIDE(=-2)` | beyond, across, farther, around, places |
| british | `RULE(=0) MEASURE(=-1) TIME(=0) GRAIN(=-1) FIGHT(=+2) DO(=-2) GIVE(=-2) SEX(=0) THING(=-1) WANT(=-2) INSIDE(=+2) HAPPEN(=-1)` | force, into, in, after, out |
| men | `SOMEONE(=-2) SEX(=+2) RULE(=0) PART(=+3) FIGHT(=0) BEGIN(=-1) MEASURE(=-1)` | ones, those, individuals, groups, people |
| film | `DO(=-3) ART(=+2) TEXT LONG(=-3) TIME(=+3) GOOD(=-2) SEE` | artist, actors, actress, writer, artists |
| federal | `RULE(=+2)` | commissions, agencies, commissioners, council, councils |
| union | `JOIN(=+2) RULE(=+3) GRAIN(=+1)` | joins, merge, merged, unified, combines |
| health | `RULE(=-1) LIVE(=+2) THING(=+1) INSIDE(=+2) CONSUME(=+1)` | inner, individuals, own, lives, person |
| night | `TIME(=0) FEEL(=-2) BEGIN(=+3) MANY(=+2) HEAT(=0) SAY(=0) PLACE` | next, until, during, before, after |
| election | `HAPPEN(=+3) RULE(=+4) FIGHT(=-1) THINK(=+2) MANY(=+2) THING(=-1) TIME(=+1)` | decisions, results, conclusion, consequences, decision |
| today | `TIME(=0)` | before, next, sometime, previous, after |
| county | `RULE(=+2) PLACE FIGHT(=-1) THING(=+1) NEAR(=+2)` | commissions, agencies, officials, commissioners, authorities |
| campaign | `FIGHT(=0) RULE(=+1) SIDE(=-1)` | battles, battle, fighting, war, wars |
| conference | `RULE(=+1) FIGHT(=-3) TIME(=+2) PLACE SAY(=-1)` | commissions, commissioners, officials, council, tournaments |
| young | `BIG(=-2) SEX(=0) TIME(=-1) THINK(=-2) PART(=+3) LIVE(=0) FIGHT(=-2)` | few, youngest, smallest, handful, some |
| defense | `FIGHT(=+2) RULE(=+3) SIDE(=+2) ABSTRACT(=+2) MOVE(=0) TIME(=-5) ART(=-2) CAN(=-3) GIVE(=+1)` | force, has, before, fighting, battles |
| bill | `RULE(=+2) TEXT ABSTRACT(=0) SAME(=+2) SIDE(=0) VALUE(=-1) CONSUME(=-1)` | commissions, committees, council, councils, governments |
| southern | `PLACE HEAT(=0) NEAR(=-1) SIDE(=+2) BIG(=0) INSIDE(=-1) TIME(=-3) FIGHT(=+1) RULE(=+3) GRAIN(=-1) SAME(=-4) WANT(=+3) ABOVE(=+2)` | areas, across, regions, from, places |
| church | `ABSTRACT(=-1) INSIDE(=0) RULE(=+2) SEX(=-1)` | walls, bureau, cabinet, authorities, doors |
| europe | `MANY(=+3) NEAR(=-5) PLACE GRAIN(=0) TIME(=+3) BIG(=+3) JOIN(=+4) HEAT(=-4) FIGHT(=-1) HAPPEN(=-4) DO(=+3) SIDE(=+2)` | whole, for, throughout, to, entire |
| vote | `THINK(=+1) RULE(=+2) MEASURE(=+1) LONG(=+1) FIGHT(=0) WANT(=-2) SAY(=0) TIME(=+3)` | decides, deciding, commissions, chose, declare |
| book | `TEXT` | pages, wrote, manuscript, writings, texts |
| growth | `MEASURE(=+1) CHANGE(=0) SIDE(=0) HAPPEN(=-1) LIVE(=+2) BIG(=0) RULE(=+2)` | increases, amounts, increase, greater, factor |
| western | `PLACE INSIDE(=-2) ABOVE(=+3) THING(=+2) SAME(=-4) BEGIN(=+2) BIG(=+3) FIGHT(=+2) ART(=+3) FEEL(=-5) DO(=+1) TIME(=-3) NEAR(=-2) WANT(=0)` | off, across, places, areas, beyond |
