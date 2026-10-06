# Лакуны: перевод без ограничения числа корней

Скрипт `scripts/20_lacunae.py`. 9647 частых слов (без слов-полюсов), словарь — корни из полюсов (44 корней). Попадание — среди 10 ближайших к коду есть слово с той же основой.

| кодер | в top10 | cos(x,y) | корней в коде (медиана / макс.) |
| :-- | --: | --: | --: |
| жадный, без предела корней, целые уровни | 63.0% | 0.403 | 8 / 24 |
| то же, только обычные слова (7128) | 77.5% | 0.442 | 8 / 22 |
| потолок: проекция на все центры и оси | 99.9% | 0.585 | все |

Потолок — хеш-эффект (docs/math.md, раздел 3): 84 свободных коэффициента различают почти любое слово, смысла это не добавляет; для лакун он не годится.

Промахи среди всех слов — большей частью имена, страны, города, названия (идут в кавычках). Ниже — только обычные слова (список 3000 частых и нарицательные по корпусу Brown): 1605 промахов из 7128.

## Кластеры промахов

Слова, ближайшие к среднему остатку (чего не хватает коду), и промахи кластера (первые по частоте).

### 96 слов: accountability, solidarity, leadership, confidence

- остаток ближе всего к: accountability, solidarity, leadership, confidence, integrity, cooperation, morale, loyalty
- промахи: security, administration, aid, safety, coalition, leadership, communist, confidence, alliance, treaty, trust, allies, minority, stability, humanitarian, truth, partnership, stressed, welfare, resignation, guide, socialist, aides, parent, chancellor

### 79 слов: monarch, sovereign, colonies, monarchy

- остаток ближе всего к: monarch, sovereign, colonies, monarchy, empire, colony, ambassador, tribes
- промахи: united, nations, nation, king, republic, society, rebels, species, culture, citizens, prince, ambassador, embassy, diplomatic, federation, fighters, empire, falls, bird, diplomats, birds, duke, emperor, survivors, commonwealth

### 72 слов: church, episcopal, clergy, catholic

- остаток ближе всего к: church, episcopal, clergy, catholic, churches, anglican, religious, priests
- промахи: church, islamic, muslim, religious, christian, ministers, god, catholic, roman, pope, temple, faith, saint, religion, bishop, parish, churches, mosque, orthodox, spiritual, priest, cathedral, christ, grace, virgin

### 64 слов: crimes, convicted, criminal, prosecuted

- остаток ближе всего к: crimes, convicted, criminal, prosecuted, indicted, crime, indictment, violation
- промахи: violence, charges, threat, crime, illegal, criminal, alleged, arrest, crimes, sanctions, corruption, threatened, convicted, guilty, allegations, abuse, sentenced, scandal, fraud, threats, offense, threatening, arrests, violations, evil

### 60 слов: brought, escorted, pursued, summoned

- остаток ближе всего к: brought, escorted, pursued, summoned, chased, tracked, accompanied, followed
- промахи: led, released, rose, arrived, warned, completed, directed, drew, revealed, discussed, delivered, acquired, hired, transferred, emerged, promoted, heading, tested, pursue, climbed, cleared, triggered, resumed, addressed, dressed

### 58 слов: european, hungarian, romanian, bulgarian

- остаток ближе всего к: european, hungarian, romanian, bulgarian, turkish, ukrainian, czech, europeans
- промахи: american, international, countries, european, british, chinese, french, israeli, russian, german, europe, japanese, african, english, indian, nato, asian, italian, korean, spanish, canadian, jewish, soviet, ethnic, greek

### 53 слов: investments, investment, investing, equities

- остаток ближе всего к: investments, investment, investing, equities, financial, funds, finance, investors
- промахи: billion, bank, financial, investors, investment, fund, stocks, yen, banks, net, cents, funds, finance, profit, earnings, cash, currency, inflation, revenue, securities, institutions, deficit, profits, fiscal, investments

### 52 слов: baseball, football, basketball, baseman

- остаток ближе всего к: baseball, football, basketball, baseman, soccer, athletics, fielder, volleyball
- промахи: defense, football, player, meanwhile, olympic, stadium, baseball, soccer, draft, basketball, offensive, golf, tennis, cricket, defensive, obviously, cap, besides, athletic, quarterback, coaches, matt, athletics, ski, pat

### 52 слов: election, democrat, democratic, elections

- остаток ближе всего к: election, democrat, democratic, elections, voters, senate, republican, republicans
- промахи: bush, election, campaign, vote, democratic, congress, elections, parliament, senate, presidential, governor, elected, voters, reform, candidates, democracy, votes, lawmakers, polls, voted, parliamentary, voting, liberal, congressional, senator

### 52 слов: sauce, tomatoes, garlic, pepper

- остаток ближе всего к: sauce, tomatoes, garlic, pepper, salad, olive, lemon, potatoes
- промахи: oil, black, red, serve, rich, wine, salt, sugar, orange, palm, apple, barrel, barrels, pan, fruit, beef, blacks, cooking, eggs, pepper, oak, sauce, gallon, olive, juice

### 51 слов: sea, seas, boats, ocean

- остаток ближе всего к: sea, seas, boats, ocean, maritime, sailing, coastal, boat
- промахи: island, coast, pacific, bay, ship, gulf, islands, fish, marine, ships, atlantic, boat, mainland, ocean, hurricane, naval, fleet, fishing, tropical, coastal, peninsula, cape, boats, vessel, shipping

### 51 слов: successes, fame, achievements, acclaimed

- остаток ближе всего к: successes, fame, achievements, acclaimed, celebrated, success, achievement, victories
- промахи: won, mark, success, records, debut, medal, champions, steps, promote, marks, recognized, winners, emerging, reputation, priority, praised, streak, improvement, popularity, medals, renamed, proud, titled, quotes, introduction

### 50 слов: passengers, buses, airports, airport

- остаток ближе всего к: passengers, buses, airports, airport, flights, passenger, bus, airlines
- промахи: tour, airport, paris, flight, plane, traffic, bus, transport, driving, transportation, flights, fly, transfer, tourists, arrival, tourist, landing, carrier, traveling, departure, charter, routes, riding, arriving, transit

### 49 слов: firearms, rifles, rifle, pistol

- остаток ближе всего к: firearms, rifles, rifle, pistol, gun, hunting, ammunition, licenses
- промахи: test, bomb, ban, shooting, bombing, testing, guns, references, hunt, proof, hunting, bomber, buffalo, inspection, checks, hunter, completion, admission, confirmation, rifle, registration, completing, bullets, licensed, identification

### 44 слов: disease, diseases, infection, illness

- остаток ближе всего к: disease, diseases, infection, illness, infections, illnesses, hiv, malaria
- промахи: problems, drug, risk, disease, suicide, drugs, cancer, aids, flu, virus, tobacco, abortion, alcohol, diseases, infected, prevention, symptoms, infection, troubles, epidemic, disorder, marijuana, cigarette, chronic, bacteria

### 44 слов: commissioners, commissioner, subcommittee, committee

- остаток ближе всего к: commissioners, commissioner, subcommittee, committee, investigators, investigator, investigations, investigation
- промахи: minister, police, federal, council, agency, committee, conference, research, ministry, commission, vice, joint, affairs, session, bureau, commissioner, investigators, delegation, fbi, forum, investigating, interim, inquiry, investigations, appointment

### 40 слов: payments, payment, loans, mortgages

- остаток ближе всего к: payments, payment, loans, mortgages, mortgage, debt, debts, loan
- промахи: tax, credit, debt, insurance, card, loans, taxes, notes, loan, cards, payments, compensation, mortgage, guarantee, payment, salary, pension, credited, provision, credits, subsidies, bail, debts, hire, guaranteed

### 38 слов: highway, crossing, bridge, bridges

- остаток ближе всего к: highway, crossing, bridge, bridges, lanes, road, roads, canal
- промахи: river, cross, lake, valley, railway, forest, avenue, creek, crossing, railroad, cemetery, reconstruction, passage, lane, canal, crossed, tunnel, dam, forests, bridges, rebuild, junction, interstate, arroyo, basin

### 38 слов: newspaper, editorial, newspapers, publications

- остаток ближе всего к: newspaper, editorial, newspapers, publications, magazine, publication, editors, headlines
- промахи: news, media, published, newspaper, magazine, cover, journal, newspapers, editor, article, coverage, publication, publishing, editorial, editors, headlines, commentary, publisher, print, publications, journalism, quarterly, herald, chronicle, circulation

### 37 слов: immigration, immigrant, citizenship, immigrants

- остаток ближе всего к: immigration, immigrant, citizenship, immigrants, marriages, marriage, visas, passports
- промахи: index, married, census, cultural, refugees, marriage, baby, immigration, gay, immigrants, labour, earthquake, couples, refugee, citizen, foreigners, geography, wedding, dating, visa, pregnant, citizenship, immigrant, surname, translation

### 36 слов: hotel, inn, rooms, mansion

- остаток ближе всего к: hotel, inn, rooms, mansion, hotels, lodge, palace, suite
- промахи: book, hall, camp, hotel, wing, offices, palace, resort, castle, camps, compound, laboratory, mall, novels, lab, zoo, refuge, spell, lobby, cave, apartments, inn, victorian, bath, reservations

### 36 слов: college, students, colleges, undergraduate

- остаток ближе всего к: college, students, colleges, undergraduate, school, student, schools, graduate
- промахи: school, university, college, schools, class, professor, studies, teacher, campus, teachers, grade, classes, taught, institution, graduated, masters, universities, faculty, colleges, scholarship, freshman, grades, graduating, graduation, enrolled

### 34 слов: psychiatric, hospitals, medical, hospital

- остаток ближе всего к: psychiatric, hospitals, medical, hospital, clinic, clinics, doctors, patients
- промахи: health, hospital, medical, care, prison, patients, doctors, prisoners, jail, medicine, surgery, hospitals, mental, prisoner, clinical, inmates, therapy, clinic, psychological, nursing, rehabilitation, psychology, prisons, physicians, prescription

### 32 слов: broadcasting, commercials, advertising, cbs

- остаток ближе всего к: broadcasting, commercials, advertising, cbs, broadcasts, broadcast, broadcasters, advertisers
- промахи: station, radio, commercial, channel, stations, communications, fox, marketing, brand, advertising, ad, nbc, medium, broadcasting, guerrillas, ads, channels, transmission, guerrilla, subscribers, lucrative, broadcasts, propaganda, anchor, soap

### 31 слов: battalion, regiment, brigade, corps

- остаток ближе всего к: battalion, regiment, brigade, corps, squadron, army, lieutenant, commanders
- промахи: guard, captain, navy, commander, crew, fort, pentagon, corps, guards, patrol, militia, lieutenant, regiment, elite, colonel, brigade, squadron, marines, commanders, battalion, policemen, convoy, recruiting, cavalry, wartime

### 31 слов: exports, markets, sales, exporting

- остаток ближе всего к: exports, markets, sales, exporting, export, market, trading, retail
- промахи: market, business, sales, growth, trading, industrial, exports, goods, expansion, export, clients, traded, manufacturing, retail, delivery, imports, traders, economies, acquisition, customer, franchise, buyers, transactions, internationally, trader

### 30 слов: le, se, en, es

- остаток ближе всего к: le, se, en, es, mi, la, de, du
- промахи: de, un, la, non, re, le, ah, en, ma, uh, et, des, il, les, grams, se, tan, cm, sin, pa, mi, amp, ab, est, con

### 29 слов: crops, farmers, agriculture, farming

- остаток ближе всего к: crops, farmers, agriculture, farming, crop, agricultural, farmer, farms
- промахи: farmers, agriculture, rain, garden, agricultural, dry, acres, corn, wheat, gardens, crops, crop, seeds, grain, drought, ranch, farming, rains, harvest, poultry, ear, dairy, swine, rainfall, planting

### 28 слов: ninth, seventh, eighth, sixth

- остаток ближе всего к: ninth, seventh, eighth, sixth, fifth, third, fourth, inning
- промахи: third, fourth, latest, fifth, sixth, innings, ranked, seventh, eighth, ninth, oldest, inning, triple, doubles, homer, batting, doubled, substitute, successive, birdie, ace, putt, tenth, bogey, richest

### 26 слов: elderly, aged, seniors, youths

- остаток ближе всего к: elderly, aged, seniors, youths, older, young, youth, teens
- промахи: women, men, young, older, guys, males, racial, aged, ages, somebody, elderly, disabled, generations, elder, aging, youths, teenage, mature, grandchildren, teens, juvenile, intermediate, newer, glasses, disability

### 25 слов: filming, film, filmed, movie

- остаток ближе всего к: filming, film, filmed, movie, films, footage, camera, photography
- промахи: film, movie, films, episode, comedy, photo, episodes, hostages, comic, cameras, cinema, portrait, filmed, photographer, edited, premiere, screening, photography, naked, trailer, lens, portraits, editing, photographers, saga

### 24 слов: satellites, moon, orbit, planet

- остаток ближе всего к: satellites, moon, orbit, planet, spacecraft, lunar, suns, venus
- промахи: nuclear, sun, missile, satellite, moon, rockets, planet, uranium, solar, universe, rays, twins, mercury, orbit, spectrum, rotation, satellites, galaxy, spacecraft, hemisphere, observatory, lunar, sunshine, radioactive

### 24 слов: singers, orchestra, singing, songs

- остаток ближе всего к: singers, orchestra, singing, songs, choir, chorus, sung, sing
- промахи: played, album, song, performed, opera, jazz, orchestra, singing, blues, bass, lyrics, dancing, recordings, vocal, sing, sang, symphony, sung, ballet, quartet, chorus, choir, pianist, brass

### 22 слов: municipalities, township, city, municipality

- остаток ближе всего к: municipalities, township, city, municipality, municipal, district, districts, town
- промахи: town, district, county, province, village, chicago, mayor, urban, provincial, downtown, districts, township, municipal, metropolitan, counties, suburb, suburban, borough, suburbs, commune, municipalities, outskirts

### 22 слов: year, month, holidays, holiday

- остаток ближе всего к: year, month, holidays, holiday, summer, december, months, christmas
- промахи: year, month, months, weeks, period, century, summer, spring, era, decade, holiday, anniversary, centuries, birthday, eve, calendar, holidays, dated, millennium, autumn, thanksgiving, summers

### 22 слов: proteins, protein, enzyme, liver

- остаток ближе всего к: proteins, protein, enzyme, liver, cholesterol, molecular, cells, cell
- промахи: cell, hip, protein, regulatory, breast, genetic, muscle, acid, chemistry, proliferation, stomach, cellular, biology, liver, kidney, cholesterol, proteins, molecular, sodium, enzyme, dose, complexity

### 21 слов: defendants, defendant, lawsuit, plaintiffs

- остаток ближе всего к: defendants, defendant, lawsuit, plaintiffs, prosecution, litigation, lawsuits, sued
- промахи: trial, justice, jury, suit, prosecutor, tribunal, prosecution, counsel, defendants, judgment, filing, suits, patent, sued, sue, defendant, litigation, plaintiffs, herein, alleging, patents

### 20 слов: twenty, fifteen, thirty, forty

- остаток ближе всего к: twenty, fifteen, thirty, forty, fourteen, twelve, thirteen, ten
- промахи: million, five, seven, nine, ten, millions, dozen, hundred, thousand, twenty, twelve, cardinal, eleven, thirty, fifteen, fifty, forty, thirteen, sixteen, fourteen

### 17 слов: friday, thursday, wednesday, monday

- остаток ближе всего к: friday, thursday, wednesday, monday, saturday, tuesday, sunday, noon
- промахи: tuesday, wednesday, monday, thursday, friday, sunday, saturday, night, today, morning, afternoon, pm, tonight, midnight, nights, noon, midday

### 15 слов: southeast, southeastern, northwest, southwest

- остаток ближе всего к: southeast, southeastern, northwest, southwest, eastern, south, northeast, west
- промахи: state, states, south, north, west, east, southern, western, eastern, southeast, northwest, northeast, southwest, northwestern, southeastern

## Примеры кодов промахов

| слово | код | ближайшие к коду |
| :-- | :-- | :-- |
| year | `TIME(=-1) MEASURE(=0) BEGIN(=+1)` | previous, lasted, before, after, prior |
| state | `RULE(=+1) PLACE` | jurisdiction, governing, rules, laws, regulations |
| million | `MEASURE(=0) TIME(=-2) GIVE(=+2) CARE(=-4) GRAIN(=+3) ABOVE(=+3) VALUE(=0)` | amounted, amounts, nearly, approximately, per |
| united | `JOIN(=+2) RULE(=+2) GRAIN(=+1) SIDE(=+1)` | joins, merge, connects, joining, joined |
| states | `RULE(=+3) PLACE SAME(=-1) SOMEONE(=-1) MEASURE(=+2) DO(=-1)` | laws, rules, jurisdiction, governing, regulations |
| south | `PLACE SIDE(=+1) HEAT(=0) NEAR(=-1) ABOVE(=+2) INSIDE(=-2)` | areas, beyond, across, places, locations |
| american | `DO(=-3) GRAIN(=-1) MANY(=+5) HAPPEN(=-4) MEASURE(=+1) CHANGE(=+5) CONSUME(=+5) TIME(=-2) ART(=+1) KNOW(=-5) WANT(=+5) LONG(=+1) THING(=-2) RULE(=-1) SAY(=+5)` | each, varies, wants, the, whatever |
| minister | `RULE(=+3) SEX(=+2) INSIDE(=+2) DO(=-3) TIME(=-1) TONE(=0)` | governing, officials, deputy, authorities, laws |
| police | `RULE(=+2) SOMEONE(=-2) THING(=+2) FIGHT(=+3) INSIDE(=-1) TIME(=-2) DO(=-2) GIVE(=-2) SEX(=-2) TONE(=0)` | her, before, officers, she, officials |
| international | `FIGHT(=-5) BIG(=+5) RULE(=+1) JOIN(=+5) SAY(=+5) TIME(=-1) DO(=-3) BODY PART(=+3) MOVE(=+2) INSIDE(=-1) VALUE(=-1)` | competitions, compete, competition, contests, competing |
| billion | `MEASURE(=+1) CARE(=-4) TIME(=-2) GRAIN(=+3) VALUE(=0) CONSUME(=+1) ABOVE(=+2)` | averaged, nearly, amounted, approximately, per |
| school | `ART(=0) ABOVE(=+4) RULE(=-1) FIGHT(=-2) SEX(=-1) PART(=+4) SIDE(=-4) MANY(=-1) TIME(=0)` | her, his, other, with, and |
| tuesday | `TIME(=0)` | before, next, sometime, previous, after |
| news | `TIME(=+1) TEXT SEE GOOD(=-2) PART(=-2) RULE(=+1) LIVE(=0) LONG(=0) GIVE(=+3) MOVE(=+3) KNOW(=-1)` | announcement, next, before, tells, shortly |
| five | `TIME(=-2) PART(=+4) BIG(=-2) SOMEONE(=-3) MEASURE(=+1) SAME(=-3) INSIDE(=+4) BEGIN(=+2) JOIN(=-3) FIGHT(=-4) MANY(=-2) ABOVE(=+2)` | two, three, several, few, ones |
| wednesday | `TIME(=0)` | before, next, sometime, previous, after |
| monday | `TIME(=+1) BEGIN(=0) FEEL(=-2) RULE(=0)` | next, before, shortly, early, after |
| thursday | `TIME(=0)` | before, next, sometime, previous, after |
| friday | `TIME(=+1) BEGIN(=+1)` | next, before, shortly, sometime, after |
| north | `NEAR(=0) HEAT(=-2) PLACE SIDE(=+2) ABOVE(=+2)` | farther, across, at, closer, off |
| security | `RULE(=0) ART(=-3) INSIDE(=+1) GIVE(=-1)` | electronic, computer, computers, own, technical |
| market | `VALUE(=-2) PLACE THING(=+2) TIME(=+2) ABOVE(=-2) GRAIN(=+1) PART(=+3) NEAR(=+5) MEASURE(=+2) DO(=0) WANT(=+2) FIGHT(=0)` | at, locations, items, in, prices |
| university | `ART(=-1) RULE(=+1) NEAR(=+2)` | electronic, science, technical, computers, sciences |
| won | `FIGHT(=-1) BEGIN(=+2) GIVE(=0)` | win, finals, wins, competitions, tournaments |
| month | `TIME(=-1) BEGIN(=0) MEASURE(=0)` | previous, before, lasted, after, prior |
| bank | `SIDE(=+2) RULE(=+1) PLACE LONG(=0) TOUCH(=0) SAME(=-2)` | side, sides, on, areas, across |
| sunday | `TIME(=+1) FIGHT(=-2) BEGIN(=+2) HEAT(=+1)` | next, finals, finale, before, after |
| third | `BEGIN(=+1) SIDE(=0) PLACE MEASURE(=+2) RULE(=0)` | ends, ending, ended, second, conclusion |
| countries | `SOMEONE(=-3) PLACE SAME(=-3) MEASURE(=+1) FIGHT(=-1) MANY(=+4) NEAR(=-4) RULE(=+5) INSIDE(=-2) DO(=+2)` | other, those, ones, places, ways |
| business | `RULE(=0) ART(=-1) INSIDE(=+1) DO(=-1) VALUE(=-2) BEGIN(=-3) PLACE` | begins, starts, starting, began, begun |
| west | `PLACE ABOVE(=+3) SIDE(=0) NEAR(=-1) INSIDE(=-2)` | beyond, across, farther, around, places |
| months | `TIME(=-1) MEASURE(=0)` | previous, previously, before, recent, lasted |
| women | `SOMEONE(=-2) SEX(=-3) FIGHT(=-1) MEASURE(=-2) BEGIN(=-2) MANY(=+2)` | each, her, those, ones, everybody |
| bush | `ABSTRACT(=-2) TOUCH(=-2) FIGHT(=+5) LONG(=0) SOMEONE(=-4) TIME(=-5) MOVE(=+4) SAY(=-4) HEAT(=+5) BIG(=+4) WANT(=-3) SIDE(=-4) CARE(=+1) RULE(=+3)` | backs, massive, quietly, rushing, fires |
| saturday | `TIME(=+1) FIGHT(=-2)` | next, sometime, shortly, sooner, before |
| european | `MANY(=+5) FIGHT(=-5) BIG(=+2) RULE(=+4) TIME(=+1) GRAIN(=+1) DO(=+4) SAME(=+4) BEGIN(=+3) HAPPEN(=-4) PART(=+3) SAY(=-5) SIDE(=+5) THING(=+3) LONG(=+3) ART(=+3)` | each, whole, entire, next, the |
| british | `RULE(=+1) MEASURE(=-2) GRAIN(=-1) DO(=-2) FIGHT(=+3) TIME(=0) GIVE(=-2) THING(=-1) SEX(=0) INSIDE(=+2) WANT(=-3) LONG(=-1) MANY(=+5) HAPPEN(=0)` | each, the, in, during, whole |
| men | `SOMEONE(=-2) SEX(=+2) PART(=+3) FIGHT(=0) BEGIN(=-1) MEASURE(=-1)` | ones, those, these, groups, his |
| oil | `GRAIN(=-2) ART(=+1) BODY VALUE(=+1)` | gases, breath, fuel, pipes, fuels |
| film | `DO(=-3) ART(=+2) TEXT LONG(=-3) TIME(=+3) GOOD(=-2) SEE` | artist, actors, actress, writer, artists |
