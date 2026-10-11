## Тест 2. Устойчивость кода к малым правкам

| коды | n | cos вектора кода | после правок | cos прочтения | после правок |
|---|--:|--:|--:|--:|--:|
| коды моделей | 92 | 0.22 | 0.19 | 0.19 | 0.17 |
| коды математики | 100 | 0.50 | 0.45 | 0.93 | 0.68 |

Связь с Haiku (Спирмен с cos первого ответа слепого Haiku):

- cos прочтения после правок: все -0.33, коды моделей 0.06, коды математики 0.21
- cos вектора после правок: все -0.23, коды моделей 0.11, коды математики 0.39
- падение cos вектора: все -0.06, коды моделей 0.27, коды математики 0.18

## Тест 4. Похожи ли коды близких слов

- случайные пары (19980): Спирмен сходства кодов с cos слов 0.15; коды переставлены случайно 0.00; среднее сходство кодов 0.05
- пары «слово — 3 ближайших в наборе» (3000): Спирмен сходства кодов с cos слов 0.32; коды переставлены случайно -0.02; среднее сходство кодов 0.38

Примеры: слово, ближайшее в наборе и их коды

- one `MANY(=+1) TIME(=-4) BEGIN(=+3) | o` — second `BEGIN(=+1) SIDE(=-1) PLACE | o` (cos 0.48, сходство кодов 0.28)
- clutch `GIVE(=-5) PART(=+4) ART(=-2) | o` — transmission `ART(=-4) CHANGE(=+2) LONG(=+2) | o` (cos 0.34, сходство кодов 0.28)
- briefly `CARE(=-1) TONE(=+1) TIME(=0) | o` — later `TIME(=0) | o` (cos 0.42, сходство кодов 0.52)
- wait `MOVE(=-1) TIME(=+3) WANT(=+1) | o` — impatiently `FEEL(=+1) TONE(=-1) TIME(=+3) | o` (cos 0.53, сходство кодов 0.27)
- arbitration `RULE(=+3) FIGHT(=-3) VALUE(=-2) | o` — mediation `RULE(=+1) FIGHT(=0) VALUE(=-3) | o` (cos 0.68, сходство кодов 0.80)
- chronicle `TEXT HAPPEN(=0) MOOD(=0) | o` — column `TEXT LONG(=+2) SIDE(=0) | o` (cos 0.39, сходство кодов 0.45)
- politically `CAN(=+1) TONE(=-3) HAPPEN(=+2) | o` — democratic `RULE(=+2) FIGHT(=-1) SIDE(=0) | o` (cos 0.40, сходство кодов 0.00)
- gravity `MEASURE(=-1) GRAIN(=-3) ABOVE(=-4) | o` — magnetic `ART(=-3) INSIDE(=-3) SAME(=-3) | o` (cos 0.38, сходство кодов 0.00)

## Тест 5. Чистота корня

Для каждого корня — слова из 1000 случайных, в коде которых он главный; cos центра этих слов со смыслом корня по спецификации (имя и полюса из roots.yaml, читатель по глоссам) и с вектором корня в словаре математики. Для сравнения — те же числа по кодам моделей из слепых тестов и рецептов (корень в любой позиции).

| корень | главный у слов (из 1000) | центр ↔ смысл по спецификации | центр ↔ вектор корня у математики | коды моделей: слов | центр ↔ смысл | примеры (математика) |
|---|--:|--:|--:|--:|--:|---|
| CARE | 13 | 0.01 | 0.85 | 6 | 0.12 | briefly, continually, cautiously, finely, empirically, experimentally |
| THING | 43 | 0.02 | 0.69 | 18 | 0.09 | thai, glen, sheep, carson, guinea, virus |
| SEX | 37 | 0.07 | 0.64 | 1 | — | husband, billy, earl, gibbs, bobby, edward |
| GRAIN | 15 | 0.10 | 0.76 | 48 | 0.34 | formation, carbon, air, alveolar, locomotive, statue |
| TONE | 19 | 0.11 | 0.78 | 7 | 0.12 | severely, positively, friendly, sir, behave, heavily |
| DO | 38 | 0.13 | 0.73 | 50 | 0.12 | owner, object, piano, salesman, devices, enterprise |
| ABSTRACT | 29 | 0.15 | 0.73 | 10 | 0.54 | proof, pat, mind, truth, barrier, insistence |
| LONG | 28 | 0.16 | 0.81 | 10 | 0.16 | havana, rod, belt, antenna, mount, chain |
| TOUCH | 17 | 0.17 | 0.72 | 20 | 0.21 | erect, conservative, texture, bold, sensitive, tough |
| SOMEONE | 11 | 0.22 | 0.34 | 27 | 0.17 | lah, astronauts, turks, ana, personally, advertisers |
| BODY | 9 | 0.22 | 0.66 | 6 | 0.29 | tung, cheek, kidney, gun, shin, rub |
| CONSUME | 4 | 0.22 | 0.51 | 32 | 0.27 | blood, clean, breathe, sink |
| GOOD | 9 | 0.24 | 0.64 | 23 | 0.24 | bizarre, bloody, slavery, foul, lucky, shame |
| SAY | 13 | 0.24 | 0.70 | 10 | 0.38 | gong, mike, listen, boo, radio, noise |
| MOOD | 8 | 0.26 | 0.50 | 15 | 0.26 | valentine, jew, patriotic, robin, devastated, sympathetic |
| FEEL | 13 | 0.26 | 0.64 | 5 | 0.27 | emotion, emotional, impatiently, chaos, weary, randy |
| MANY | 20 | 0.27 | 0.85 | 13 | 0.21 | one, definitely, happen, der, anyway, literally |
| PART | 25 | 0.27 | 0.62 | 33 | 0.22 | segment, convoy, nova, cherry, substance, stamp |
| LIVE | 13 | 0.31 | 0.68 | 21 | 0.18 | die, doom, alive, artificial, survivor, coral |
| HAPPEN | 21 | 0.31 | 0.71 | 4 | 0.24 | haitian, algerian, relation, achievement, implication, pose |
| JOIN | 14 | 0.32 | 0.79 | 28 | 0.20 | discourage, apart, avoid, engage, conceal, broaden |
| BEGIN | 17 | 0.35 | 0.77 | 2 | — | second, conclude, tenth, season, annual, period |
| NEAR | 31 | 0.36 | 0.54 | 6 | 0.20 | madagascar, peru, delhi, sea, bucharest, checkpoint |
| THINK | 24 | 0.36 | 0.79 | 10 | 0.31 | wonder, holmes, demonstrate, install, elect, clues |
| MOVE | 12 | 0.36 | 0.72 | 36 | 0.36 | wait, stretch, cox, proceed, instant, solo |
| KNOW | 9 | 0.36 | 0.68 | 9 | 0.12 | unidentified, innocent, unknown, notify, safety, realize |
| FIGHT | 64 | 0.39 | 0.77 | 20 | 0.53 | farc, player, arena, doha, rovers, bowling |
| RULE | 60 | 0.39 | 0.67 | 17 | 0.40 | arbitration, dean, evaluation, petitioner, referendum, clinton |
| SIDE | 10 | 0.39 | 0.65 | 3 | 0.13 | straighten, edge, southward, thrust, oriented, curve |
| ART | 35 | 0.39 | 0.81 | 17 | 0.43 | logistics, magnetic, gothic, infrastructure, medicine, classical |
| CAN | 18 | 0.41 | 0.78 | 4 | 0.13 | politically, sustainable, succeed, preferably, inability, impasse |
| PLACE | 47 | 0.41 | 0.79 | 41 | 0.33 | dell, position, arkansas, delaware, kashmir, nationwide |
| SAME | 15 | 0.41 | 0.73 | 8 | 0.42 | identical, distinctive, various, pertain, criteria, typically |
| SEE | 16 | 0.43 | 0.73 | 4 | 0.04 | showcase, show, display, focus, observation, kohl |
| VALUE | 25 | 0.43 | 0.61 | 12 | 0.45 | junk, luxury, profitable, goodwill, premium, tariff |
| HEAT | 16 | 0.44 | 0.69 | 12 | 0.53 | danish, boil, sunshine, flood, sunny, frost |
| WANT | 17 | 0.45 | 0.75 | 4 | 0.02 | favour, denounce, neglect, urge, defiance, need |
| ABOVE | 18 | 0.46 | 0.77 | 17 | 0.33 | grade, upper, arch, bottom, crawl, climb |
| MEASURE | 36 | 0.46 | 0.82 | 7 | 0.42 | gravity, expenditure, proportion, demographics, outnumbered, importance |
| TIME | 23 | 0.46 | 0.83 | 9 | 0.27 | years, incoming, ago, reappear, kuwaiti, fifteen |
| BIG | 16 | 0.49 | 0.73 | 20 | 0.25 | negro, slovak, klein, smaller, juvenile, angel |
| CHANGE | 18 | 0.51 | 0.75 | 4 | 0.33 | continue, dependent, positive, preserve, deteriorating, downgraded |
| INSIDE | 9 | 0.53 | 0.67 | 23 | 0.30 | foreign, oval, bunker, external, dome, cell |
| GIVE | 35 | 0.61 | 0.83 | 11 | 0.30 | clutch, possession, hurl, donor, donate, bring |
| TEXT | 30 | 0.70 | 0.88 | 20 | 0.45 | chronicle, clause, tag, database, blank, reply |

Среднее по 43 корням, где есть оба: математика 0.33, коды моделей 0.27.

