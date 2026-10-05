# Кандидаты в корни и оси: слепой круговой тест (36 слов, 2 кодировщика, 1 декодер на набор)

Кандидаты найдены математикой ([docs/math.md](../../docs/math.md), раздел «Лакуны»): ось здоровья у `BODY`, ось «всерьёз ли» у `FIGHT`, новый корень `TEXT`. Слова — по 12 из области каждого кандидата: *sick*, *healthy*, *disease*, *patient*, *doctor*, *hospital*, *medicine*, *fever*, *wound*, *cure*, *nurse*, *infection*, *game*, *sport*, *player*, *champion*, *toy*, *tournament*, *war*, *soldier*, *army*, *weapon*, *gun*, *enemy*, *book*, *letter*, *page*, *newspaper*, *article*, *writer*, *author*, *write*, *read*, *document*, *poem*, *library*.

Кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер — только таблицы и правила чтения, оригиналов не видит, коды перемешаны. В наборах B оба дополнительно видят описание кандидатов:

| корень | ось / смысл |
| :-- | :-- |
| BODY | тело; **новая ось — здоровье**: −5 тяжело больной, болезнь … 0 обычное состояние … +5 здоровый, крепкий. Без значения — просто тело, как раньше |
| FIGHT | бой, ссора; **новая ось — всерьёз ли**: −5 игра, спорт, соревнование по правилам … 0 драка, спор … +5 война насмерть. Без значения — бой, ссора, как раньше |
| TEXT | **новый корень без оси**: письменная речь — текст, документ, запись (в отличие от `SAY` — устной речи). `TEXT \| o` — текст, `TEXT \| i` — записывать |

Модель: sonnet (субагенты). Счёт строгий: ✓ — лучшее слово совпало с оригиналом, ~ — оригинал среди трёх ответов.

| область | без кандидатов (A1 + A2) | с кандидатами (B1 + B2) |
| :-- | :-- | :-- |
| BODY | 15 / 20 из 24 | 19 / 22 из 24 |
| FIGHT | 11 / 15 из 24 | 17 / 21 из 24 |
| TEXT | 3 / 5 из 24 | 15 / 17 из 23 |
| всего | 29 / 40 из 72 | 51 / 60 из 71 |

Решение:

- **`TEXT` добавлен** (46-й корень, без оси): 3 → 15 точных из 24. Без него письменное собирается из `SAY` и читается как устное (*letter* → *promise, message*, *write* → *compose, sing*). Корень понятен человеку, у токипоны есть `lipu` / `sitelen`.
- **Ось у `FIGHT` добавлена** (−5 игра, спорт … 0 драка, спор … +5 война): 11 → 17. Без оси *game, sport, player, tournament* читаются как бой.
- **Ось у `BODY` не добавлена**: 15 → 19, здоровье и болезнь и без неё выражаются через `LIVE` и `GOOD` (*disease* = `LIVE(=-3) GOOD(=-4) | o`). Оставлено на решение автора.

Оговорки: слова выбраны под кандидатов; по одному декодеру на набор; в B2 кодировщик пропустил *document* (35 слов). Шум порядка ±3 слов на область.

## Набор A1 (без кандидатов)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| player | `SOMEONE FIGHT ART(=+2) \| o` | warrior / soldier / fighter |  |
| doctor | `SOMEONE KNOW LIVE GOOD(=+3) \| o` | doctor / physician / healer | ✓ |
| letter | `THING(=-5) SAY GIVE(=+3) \| o` | promise / letter / message | ~ |
| toy | `THING(=-5) ART(=+2) BIG(=-3) \| o` | ornament / toy / figurine | ~ |
| weapon | `THING(=-5) FIGHT \| o` | weapon / sword / gun | ✓ |
| hospital | `PLACE LIVE GOOD(=+3) \| o` | hospital / clinic / sanatorium | ✓ |
| author | `SOMEONE ART(=+5) SAY \| o` | poet / singer / writer |  |
| medicine | `GOOD(=+3) CONSUME(=+5) LIVE \| o` | food / meal / nutrition |  |
| champion | `SOMEONE FIGHT ABOVE(=+5) \| o` | winner / champion / victor | ~ |
| poem | `ART(=+5) SAY \| o` | poetry / song / literature |  |
| disease | `LIVE(=-3) GOOD(=-4) \| o` | illness / disease / sickness | ~ |
| sport | `FIGHT ART(=+2) BODY \| o` | wrestling / boxing / martial art |  |
| book | `THING(=-5) ART(=+3) SAY \| o` | poem / song / story |  |
| gun | `THING(=-5) FIGHT MOVE(=+5) \| o` | bullet / missile / arrow |  |
| wound | `BODY TOUCH(=+4) GOOD(=-4) \| o` | injury / wound / bruise | ~ |
| war | `FIGHT BIG(=+5) \| o` | war / battle / conflict | ✓ |
| article | `SAY ART(=-2) PART(=-2) \| o` | syllable / word / term |  |
| healthy | `LIVE(=+4) GOOD(=+4) \| a` | healthy / fit / lively | ✓ |
| army | `SOMEONE PART(=+5) FIGHT RULE(=+5) \| o` | army / military / troops | ✓ |
| document | `THING(=-5) SAY RULE(=+4) \| o` | law / regulation / decree |  |
| sick | `LIVE(=-2) GOOD(=-4) \| a` | sick / ill / unwell | ✓ |
| writer | `SOMEONE ART(=+3) SAY \| o` | writer / author / speaker | ✓ |
| write | `SAY ART(=+3) \| i` | recite / sing / tell |  |
| game | `FIGHT ART(=+2) \| o` | duel / fencing / sport |  |
| page | `THING(=-5) SAY PART(=-2) \| o` | word / syllable / letter |  |
| read | `CONSUME(=+5) SAY ABSTRACT(=-3) \| i` | read / listen / learn | ✓ |
| fever | `HEAT(=+4) LIVE GOOD(=-4) \| o` | fever / inflammation / infection | ✓ |
| soldier | `SOMEONE FIGHT RULE(=+5) \| o` | soldier / policeman / officer | ✓ |
| infection | `LIVE GOOD(=-4) CHANGE \| o` | death / decay / infection | ~ |
| patient | `SOMEONE LIVE(=-2) GOOD(=-4) \| o` | patient / invalid / sufferer | ✓ |
| library | `PLACE THING(=-5) SAY PART(=+5) \| o` | library / archive / bookstore | ✓ |
| nurse | `SOMEONE DO GOOD(=+3) LIVE \| o` | nurse / healer / caregiver | ✓ |
| tournament | `FIGHT ART(=+2) PART(=+5) \| o` | tournament / competition / championship | ✓ |
| cure | `DO LIVE GOOD(=+4) \| i` | heal / cure / treat | ~ |
| newspaper | `THING(=-5) SAY TIME(=+0) \| o` | news / report / announcement |  |
| enemy | `SOMEONE FIGHT WANT(=-5) \| o` | enemy / foe / adversary | ✓ |

## Набор A2 (без кандидатов)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| poem | `THING(=-5) ART(=+5) SAY \| o` | instrument / microphone / megaphone |  |
| war | `FIGHT BIG(=+4) \| o` | war / battle / army | ✓ |
| newspaper | `THING(=-5) SEE HAPPEN \| o` | camera / mirror / screen |  |
| book | `THING(=-5) KNOW SEE \| o` | microscope / telescope / binoculars |  |
| document | `THING(=-5) SEE RULE(=+4) \| o` | sign / signal / flag |  |
| article | `THING(=-5) KNOW PART(=-2) \| o` | label / clue / handle |  |
| infection | `GOOD(=-4) LIVE(=+3) INSIDE \| o` | parasite / germ / worm |  |
| soldier | `SOMEONE FIGHT RULE(=+4) \| o` | soldier / policeman / police | ✓ |
| fever | `BODY HEAT(=+3) GOOD(=-3) \| o` | fever / burn / sunburn | ✓ |
| tournament | `FIGHT ART(=+2) PART(=+5) \| o` | sports / tournament / games | ~ |
| game | `FIGHT ART(=+2) \| o` | sport / boxing / duel |  |
| read | `CONSUME(=+5) SEE \| i` | watch / stare / look |  |
| sport | `FIGHT ART(=+2) BODY \| o` | wrestling / gymnastics / boxing |  |
| nurse | `SOMEONE CARE(=+4) BODY \| o` | nurse / doctor / caretaker | ✓ |
| toy | `THING(=-5) FIGHT ART(=+2) \| o` | racket / ball / glove |  |
| hospital | `PLACE BODY GOOD(=+4) \| o` | gym / spa / clinic |  |
| write | `CONSUME(=-5) SEE \| i` | show / display / reveal |  |
| patient | `SOMEONE BODY GOOD(=-3) \| o` | patient / invalid / sufferer | ✓ |
| wound | `BODY FIGHT HAPPEN(=+4) \| o` | wound / bruise / scar | ✓ |
| letter | `THING(=-5) SEE GIVE(=+3) \| o` | lamp / light / lantern |  |
| healthy | `BODY GOOD(=+3) \| a` | healthy / fit / strong | ✓ |
| weapon | `THING(=-5) FIGHT \| o` | weapon / sword / gun | ✓ |
| player | `SOMEONE FIGHT ART(=+2) \| o` | athlete / boxer / wrestler |  |
| cure | `DO BODY GOOD(=+4) \| i` | heal / cure / exercise | ~ |
| disease | `BODY GOOD(=-4) LIVE(=+2) \| o` | disease / illness / infection | ✓ |
| champion | `SOMEONE FIGHT GOOD(=+5) \| o` | hero / champion / winner | ~ |
| author | `SOMEONE ART(=+5) CONSUME(=-5) \| o` | poet / writer / singer |  |
| gun | `THING(=-5) FIGHT MOVE(=+5) \| o` | missile / bullet / arrow |  |
| page | `THING(=-5) PART(=-2) SEE \| o` | lens / glass / window |  |
| writer | `SOMEONE CONSUME(=-5) SEE \| o` | guide / exhibitor / showman |  |
| sick | `BODY GOOD(=-3) \| a` | sick / ill / unhealthy | ✓ |
| doctor | `SOMEONE ART(=-4) BODY \| o` | surgeon / physician / anatomist |  |
| medicine | `THING(=-5) BODY GOOD(=+4) \| o` | medicine / remedy / vitamin | ✓ |
| army | `SOMEONE FIGHT PART(=+5) \| o` | army / troops / soldiers | ✓ |
| library | `PLACE THING(=-5) KNOW \| o` | museum / laboratory / library | ~ |
| enemy | `SOMEONE FIGHT WANT(=-5) \| o` | enemy / foe / hater | ✓ |

## Набор B1 (с кандидатами)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| doctor | `SOMEONE BODY(=+4) KNOW \| o` | doctor / physician / healer | ✓ |
| sport | `FIGHT(=-5) \| o` | game / sport / match | ~ |
| poem | `ART(=+5) TEXT \| o` | literature / novel / poetry |  |
| gun | `THING(=-5) FIGHT MOVE(=+5) \| o` | bullet / missile / projectile |  |
| champion | `SOMEONE FIGHT(=-5) GOOD \| o C+5` | champion / winner / best player | ✓ |
| document | `TEXT RULE(=+4) \| o` | law / statute / constitution |  |
| write | `TEXT \| i` | write / record / note | ✓ |
| fever | `BODY(=-3) HEAT(=+3) \| o` | fever / temperature / heat | ✓ |
| medicine | `BODY(=+4) CONSUME(=+5) \| o` | food / meal / nourishment |  |
| wound | `BODY(=-3) FIGHT \| o` | wound / injury / bruise | ✓ |
| disease | `BODY(=-5) \| o` | illness / disease / sickness | ~ |
| game | `FIGHT(=-4) ART(=+2) \| o` | gymnastics / martial art / dance |  |
| cure | `BODY(=+4) CHANGE(=+5) \| i` | heal / recover / cure | ~ |
| article | `TEXT KNOW(=+3) \| o` | information / data / article | ~ |
| nurse | `SOMEONE BODY(=+3) CARE(=+4) \| o` | nurse / caregiver / medic | ✓ |
| writer | `SOMEONE TEXT \| o` | writer / scribe / secretary | ✓ |
| healthy | `BODY(=+5) \| a` | healthy / strong / fit | ✓ |
| newspaper | `TEXT TIME(=0) KNOW \| o` | news / newspaper / report | ~ |
| hospital | `PLACE BODY(=-3) CHANGE(=+3) \| o` | hospital / clinic / ward | ✓ |
| library | `PLACE TEXT PART(=+5) \| o` | library / archive / bookstore | ✓ |
| war | `FIGHT(=+5) \| o` | war / battle / combat | ✓ |
| letter | `TEXT GIVE(=+3) SOMEONE \| o` | letter / message / mail | ✓ |
| weapon | `THING(=-5) FIGHT DO \| o` | weapon / sword / gun | ✓ |
| player | `SOMEONE FIGHT(=-5) \| o` | player / athlete / competitor | ✓ |
| infection | `BODY(=-4) JOIN(=+3) \| o` | infection / contagion / contamination | ✓ |
| sick | `BODY(=-4) \| a` | sick / ill / unwell | ✓ |
| soldier | `SOMEONE FIGHT(=+5) RULE(=+4) \| o` | soldier / warrior / officer | ✓ |
| army | `SOMEONE FIGHT PART(=+5) \| o` | army / troops / gang | ✓ |
| enemy | `SOMEONE(=-3) FIGHT \| o` | enemy / opponent / foe | ✓ |
| page | `TEXT PART(=-2) \| o` | sentence / word / paragraph |  |
| tournament | `FIGHT(=-5) PART(=+5) \| o` | tournament / league / team | ✓ |
| book | `TEXT PART(=+2) \| o` | book / chapter / volume | ✓ |
| author | `SOMEONE TEXT HAPPEN(=-4) \| o` | author / creator / poet | ✓ |
| toy | `THING(=-5) FIGHT(=-5) \| o` | ball / toy / puck | ~ |
| patient | `SOMEONE BODY(=-4) \| o` | patient / invalid / sufferer | ✓ |
| read | `CONSUME(=+5) TEXT \| i` | read / study / peruse | ✓ |

## Набор B2 (с кандидатами)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| army | `SOMEONE FIGHT(=+5) PART(=+5) \| o` | army / troops / regiment | ✓ |
| page | `TEXT PART(=-2) \| o` | paragraph / sentence / word |  |
| toy | `THING(=-5) FIGHT(=-5) \| o` | toy / ball / game piece | ✓ |
| article | `TEXT PARTICULAR(=+3) \| o` | document / contract / inscription |  |
| library | `PLACE TEXT PART(=+5) \| o` | library / archive / bookshop | ✓ |
| nurse | `SOMEONE CARE(=+4) BODY(=-3) \| o` | nurse / caregiver / doctor | ✓ |
| disease | `BODY(=-5) \| o` | disease / illness / plague | ✓ |
| weapon | `THING(=-5) FIGHT(=+5) \| o` | weapon / bomb / bullet | ✓ |
| writer | `SOMEONE TEXT \| o` | writer / author / secretary | ✓ |
| poem | `TEXT ART(=+5) \| o` | literature / poetry / novel |  |
| read | `CONSUME(=+5) TEXT \| i` | read / study / peruse | ✓ |
| infection | `BODY(=-4) JOIN(=+3) MOVE \| o` | infection / epidemic / contagion | ✓ |
| write | `TEXT \| i` | write / record / type | ✓ |
| newspaper | `TEXT TIME(=0) PART(=+5) \| o` | newspaper / news / magazine | ✓ |
| sport | `FIGHT(=-5) BODY \| o` | sport / athletics / gymnastics | ✓ |
| author | `SOMEONE TEXT HAPPEN(=-4) \| o` | author / source / creator | ✓ |
| doctor | `SOMEONE KNOW BODY(=-3) \| o` | doctor / physician / medic | ✓ |
| wound | `BODY(=-3) JOIN(=-4) \| o` | surgery / amputation / operation |  |
| sick | `BODY(=-4) \| a` | sick / ill / diseased | ✓ |
| letter | `TEXT GIVE(=+3) \| o` | letter / publication / mail | ✓ |
| game | `FIGHT(=-5) \| o` | game / match / sport | ✓ |
| enemy | `SOMEONE FIGHT(=+3) \| o` | fighter / warrior / enemy | ~ |
| hospital | `PLACE BODY(=-3) CARE(=+4) \| o` | hospital / clinic / infirmary | ✓ |
| player | `SOMEONE FIGHT(=-5) \| o` | player / athlete / competitor | ✓ |
| gun | `THING(=-5) FIGHT(=+5) MOVE(=+5) \| o` | missile / bullet / rocket |  |
| soldier | `SOMEONE FIGHT(=+5) \| o` | soldier / warrior / combatant | ✓ |
| war | `FIGHT(=+5) \| o` | war / battle / combat | ✓ |
| patient | `SOMEONE BODY(=-3) \| o` | patient / invalid / sufferer | ✓ |
| fever | `BODY(=-3) HEAT(=+3) \| o` | fever / temperature / inflammation | ✓ |
| tournament | `FIGHT(=-5) PART(=+5) \| o` | team / league / tournament | ~ |
| champion | `SOMEONE FIGHT(=-5) ABOVE(=+5) \| o` | champion / winner / victor | ✓ |
| healthy | `BODY(=+5) \| a` | healthy / strong / robust | ✓ |
| medicine | `CONSUME(=+5) BODY(=-3) CHANGE(=+4) \| o` | medicine / remedy / drug | ✓ |
| book | `TEXT PART(=+2) THING(=-5) \| o` | book / manuscript / volume | ✓ |
| cure | `BODY(=-3) CHANGE(=+4) \| i` | recover / heal / cure | ~ |
