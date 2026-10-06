# Возраст, музыка, вода, успех: слепой тест

Вопрос: закрыть лакуны второго прохода [lacunae.md](../lacunae.md) рецептами на существующих корнях. Слова: *young, old, elderly, youth, age, ancient, music, song, sing, dance, singer, melody, sea, lake, river, island, shore, mountain, win, lose, victory, success, fail, famous*.

Протокол как в [roundtrip_time](roundtrip_time.md): A — нынешняя спецификация, B — с рецептами ниже (их видят кодировщик и декодер); sonnet, 2 кодировщика, по 1 декодеру на набор; ✓ лучшее слово = оригинал, ~ среди трёх.

**Рецепты набора B**

**Возраст** — `LIVE` с `TIME`: уровень TIME — с какого времени живёт. Молодой = `LIVE TIME(=-1) | a` («живёт недавно»), взрослый = `LIVE TIME(=-3) | a`, старый, пожилой = `LIVE TIME(=-5) | a`; молодёжь = `SOMEONE LIVE TIME(=-1) PART(=+5) | o`; возраст = `LIVE TIME MEASURE | o`. О вещах — без LIVE: древний, давний = `TIME(=-5) | a`.

**Музыка** — звук как искусство: `SAY ART(=+5)` и `FEEL(=+3)` (звук, несущий чувство; отличает от поэзии `ART(=+5) SAY`, где главное — слова). Петь = `SAY ART(=+5) FEEL(=+3) | i`, песня = то же `| o`, певец = `SOMEONE SAY FEEL(=+3) | o`, музыка = `ART(=+5) SAY THING | o` (искусство звуков; `SAY THING` — звук, шум), мелодия = `ART(=+5) SAY LONG | o` («протяжённый звук»). Танцевать = `ART(=+5) MOVE BODY | i`.

**Вода и рельеф** — `PLACE` с веществом: вода — `GRAIN(=-3)` (жидкость). Море, океан = `PLACE GRAIN(=-3) BIG(=+5) | o`, озеро = `PLACE GRAIN(=-3) BIG(=0) | o`, река = `PLACE GRAIN(=-3) MOVE(=+3) | o` (текущая вода), остров = `PLACE GRAIN(=-3) INSIDE(=+5) | o` («место внутри воды»), берег = `PLACE GRAIN(=-3) NEAR(=+4) | o` («место у воды»); гора = `PLACE ABOVE(=+5) BIG(=+4) | o`.

**Успех и победа** — `GOOD` о результате: `HAPPEN(=+5)` — результат. Победить = `FIGHT GOOD(=+4) | i`, проиграть = `FIGHT GOOD(=-4) | i`, победа = `FIGHT GOOD(=+4) HAPPEN(=+5) | o`; успех = `DO GOOD(=+4) HAPPEN(=+5) | o`, потерпеть неудачу = `DO GOOD(=-4) HAPPEN(=+5) | i`; знаменитый = `KNOW MANY(=+5) | a` («все знают»).

| область (6 слов) | A1 | A2 | B1 | B2 |
| :-- | --: | --: | --: | --: |
| возраст | 4 / 4 | 5 / 5 | 5 / 6 | 5 / 6 |
| музыка | 2 / 4 | 3 / 4 | 6 / 6 | 6 / 6 |
| вода и рельеф | 1 / 1 | 1 / 1 | 6 / 6 | 6 / 6 |
| успех и победа | 4 / 4 | 4 / 4 | 6 / 6 | 6 / 6 |
| всего (24) | 11 / 13 | 13 / 14 | 23 / 24 | 23 / 24 |

Что видно:

- **Вода — настоящая лакуна**: без рецепта `PLACE GRAIN(=-3) …` читается как воздух, небо, атмосфера (море, озеро, река — 0 из 6 в обоих наборах A); декодер не связывает −3 с водой без явного «вода — жидкость, место с жидкостью». С рецептом — 12 из 12.
- **Песня через `TEXT`** читается как стихи, литература; `FEEL(=+3)` отделяет пение от поэзии (песня, певец 4 из 4 против 1 из 4). Музыка — `ART(=+5) SAY THING`, мелодия — `ART(=+5) SAY LONG`.
- **Возраст и успех почти работают и без рецептов** — кодировщики сами берут `LIVE TIME`, `LIVE BEGIN`, `FIGHT GOOD`, `DO GOOD HAPPEN`; рецепт снимает разнобой (*youth* читалось как *children*, *fail* как *harm*). *elderly* = *old* (один код на оба — потеря принята). Рецепт молодёжи в тесте — четыре корня (`SOMEONE LIVE TIME(=-1) PART(=+5)`), сверх лимита; в спецификацию взят `SOMEONE LIVE TIME(=-1) | o N+3` (без теста).

Оговорки: рецепты были у декодера B в явном виде; по одному декодеру на набор; шум ±3 из 24.

## Набор A1

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| melody | `ART(=+5) SAY PART(=-2) \| o` | verse / poem / song |  |
| shore | `PLACE NEAR(=+5) GRAIN(=-3) \| o` | air / atmosphere / here |  |
| lose | `FIGHT(=-5) HAPPEN(=+4) GOOD(=-4) \| i` | lose / fail / defeat | ✓ |
| music | `ART(=+5) SAY FEEL \| o` | song / music / poem | ~ |
| fail | `DO HAPPEN(=+4) GOOD(=-4) \| i` | ruin / harm / spoil |  |
| island | `PLACE GRAIN(=+5) PART(=-2) \| o` | ground / floor / stone |  |
| young | `LIVE(=+5) BEGIN(=-4) \| a` | young / new / born | ✓ |
| youth | `SOMEONE LIVE(=+5) BEGIN(=-4) \| o N+3` | children / babies / young |  |
| success | `DO HAPPEN(=+4) GOOD(=+4) ABSTRACT \| o` | success / achievement / benefit | ✓ |
| elderly | `LIVE(=+1) BEGIN(=+4) \| a` | old / dying / ancient |  |
| song | `ART(=+5) SAY TEXT \| o` | poem / literature / story |  |
| dance | `ART(=+5) MOVE BODY \| i` | dance / perform / act | ✓ |
| ancient | `TIME(=-5) \| a` | ancient / old / past | ✓ |
| famous | `KNOW(=+5) MANY(=+5) \| a` | wise / educated / learned |  |
| river | `GRAIN(=-3) MOVE LONG(=-5) \| o` | smoke / steam / breeze |  |
| lake | `PLACE GRAIN(=-3) INSIDE(=+4) \| o` | lung / room / hole |  |
| sing | `CONSUME(=-5) SAY ART(=+5) \| i` | sing / recite / compose | ✓ |
| mountain | `PLACE GRAIN(=+5) ABOVE(=+5) \| o` | mountain / hill / peak | ✓ |
| sea | `PLACE GRAIN(=-3) BIG(=+5) \| o` | sky / atmosphere / space |  |
| old | `LIVE(=+3) TIME(=-4) \| a` | old / elderly / aged | ✓ |
| win | `FIGHT(=-5) HAPPEN(=+4) GOOD(=+4) \| i` | win / succeed / score | ✓ |
| victory | `FIGHT HAPPEN(=+4) GOOD(=+4) \| o` | victory / triumph / win | ✓ |
| singer | `SOMEONE SAY ART(=+5) \| o` | poet / author / singer | ~ |
| age | `LIVE TIME MEASURE(=-5) \| o` | age / life / year | ✓ |

## Набор A2

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| sing | `CONSUME(=-5) SAY ART(=+5) \| i` | sing / recite / compose | ✓ |
| island | `PLACE THING(=-5) GRAIN(=-3) \| o` | beach / desert / sand |  |
| river | `GRAIN(=-3) MOVE LONG \| o` | smoke / steam / wind |  |
| ancient | `TIME(=-5) \| a I+4` | ancient / old / primitive | ✓ |
| mountain | `THING(=-5) ABOVE(=+5) BIG(=+5) \| o` | mountain / hill / cliff | ✓ |
| famous | `SOMEONE MANY(=+4) KNOW \| a` | famous / popular / public | ✓ |
| success | `DO GOOD HAPPEN(=+4) ABSTRACT \| o` | success / achievement / benefit | ✓ |
| music | `ART(=+5) SAY FEEL(=+3) \| o` | poem / song / poetry |  |
| youth | `SOMEONE LIVE BEGIN(=-3) PART(=+5) \| o` | children / family / generation |  |
| young | `LIVE(=+4) BEGIN(=-3) \| a` | young / new / fresh | ✓ |
| dance | `ART(=+5) MOVE BODY \| i` | dance / perform / act | ✓ |
| age | `LIVE TIME MEASURE \| o` | age / life / lifetime | ✓ |
| lake | `GRAIN(=-3) PLACE INSIDE(=+4) \| o` | air / atmosphere / cloud |  |
| shore | `PLACE GRAIN(=-3) NEAR(=+5) \| o` | atmosphere / air / surface |  |
| elderly | `LIVE(=+2) TIME(=-5) BEGIN(=+4) \| a` | elderly / aged / dying | ✓ |
| victory | `FIGHT(=-5) GOOD(=+5) ABSTRACT(=+3) \| o` | entertainment / game / fun |  |
| lose | `FIGHT(=-5) GOOD(=-4) \| i` | lose / fail / cheat | ✓ |
| win | `FIGHT(=-5) GOOD(=+4) \| i` | win / succeed / play | ✓ |
| singer | `SOMEONE SAY ART(=+5) \| o` | singer / poet / speaker | ✓ |
| song | `ART(=+5) SAY TEXT \| o` | literature / novel / story |  |
| fail | `DO GOOD(=-4) HAPPEN(=+4) \| i` | harm / damage / hurt |  |
| sea | `GRAIN(=-3) BIG(=+5) PLACE \| o` | sky / atmosphere / air |  |
| old | `LIVE TIME(=-4) \| a` | old / ancient / aged | ✓ |
| melody | `ART(=+5) SAY TIME \| o` | music / song / melody | ~ |

## Набор B1

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| success | `DO GOOD(=+4) HAPPEN(=+5) \| o` | success / achievement / triumph | ✓ |
| win | `FIGHT GOOD(=+4) \| i` | win / defeat / beat | ✓ |
| age | `LIVE TIME MEASURE \| o` | age / lifespan / generation | ✓ |
| melody | `ART(=+5) SAY LONG \| o` | melody / tune / rhythm | ✓ |
| victory | `FIGHT GOOD(=+4) HAPPEN(=+5) \| o` | victory / triumph / win | ✓ |
| island | `PLACE GRAIN(=-3) INSIDE(=+5) \| o` | island / peninsula / isle | ✓ |
| singer | `SOMEONE SAY FEEL(=+3) \| o` | singer / vocalist / musician | ✓ |
| lose | `FIGHT GOOD(=-4) \| i` | lose / fail / be defeated | ✓ |
| ancient | `TIME(=-5) \| a I+4` | ancient / very old / antique | ✓ |
| youth | `SOMEONE LIVE TIME(=-1) PART(=+5) \| o` | youth / young people / teenagers | ✓ |
| shore | `PLACE GRAIN(=-3) NEAR(=+4) \| o` | shore / coast / beach | ✓ |
| dance | `ART(=+5) MOVE BODY \| i` | dance / ballet / perform | ✓ |
| old | `LIVE TIME(=-5) \| a` | old / elderly / aged | ✓ |
| song | `SAY ART(=+5) FEEL(=+3) \| o` | song / tune / ballad | ✓ |
| sea | `PLACE GRAIN(=-3) BIG(=+5) \| o` | sea / ocean / gulf | ✓ |
| young | `LIVE TIME(=-1) \| a` | young / youthful / new | ✓ |
| mountain | `PLACE ABOVE(=+5) BIG(=+4) \| o` | mountain / hill / peak | ✓ |
| river | `PLACE GRAIN(=-3) MOVE(=+3) \| o` | river / stream / creek | ✓ |
| lake | `PLACE GRAIN(=-3) BIG(=0) \| o` | lake / pond / lagoon | ✓ |
| sing | `SAY ART(=+5) FEEL(=+3) \| i` | sing / chant / croon | ✓ |
| music | `ART(=+5) SAY THING \| o` | music / sound / noise | ✓ |
| fail | `DO GOOD(=-4) HAPPEN(=+5) \| i` | fail / flop / fall short | ✓ |
| elderly | `LIVE TIME(=-5) \| a I+4` | very old / ancient / elderly | ~ |
| famous | `KNOW MANY(=+5) \| a` | famous / well-known / celebrated | ✓ |

## Набор B2

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| melody | `ART(=+5) SAY LONG \| o` | melody / tune / song | ✓ |
| age | `LIVE TIME MEASURE \| o` | age / lifespan / era | ✓ |
| music | `ART(=+5) SAY THING \| o` | music / sound / noise | ✓ |
| song | `SAY ART(=+5) FEEL(=+3) \| o` | song / singing / chant | ✓ |
| sea | `PLACE GRAIN(=-3) BIG(=+5) \| o` | sea / ocean / bay | ✓ |
| young | `LIVE TIME(=-1) \| a` | young / youthful / new | ✓ |
| success | `DO GOOD(=+4) HAPPEN(=+5) \| o` | success / achievement / triumph | ✓ |
| famous | `KNOW MANY(=+5) \| a` | famous / well-known / celebrated | ✓ |
| fail | `DO GOOD(=-4) HAPPEN(=+5) \| i` | fail / failure / lose | ✓ |
| elderly | `LIVE TIME(=-5) \| a I+3` | very old / ancient / elderly | ~ |
| lose | `FIGHT GOOD(=-4) \| i` | lose / be defeated / fail | ✓ |
| win | `FIGHT GOOD(=+4) \| i` | win / defeat / beat | ✓ |
| ancient | `TIME(=-5) \| a` | ancient / old / archaic | ✓ |
| river | `PLACE GRAIN(=-3) MOVE(=+3) \| o` | river / stream / creek | ✓ |
| island | `PLACE GRAIN(=-3) INSIDE(=+5) \| o` | island / isle / peninsula | ✓ |
| mountain | `PLACE ABOVE(=+5) BIG(=+4) \| o` | mountain / hill / peak | ✓ |
| sing | `SAY ART(=+5) FEEL(=+3) \| i` | sing / chant / croon | ✓ |
| lake | `PLACE GRAIN(=-3) BIG(=0) \| o` | lake / pond / pool | ✓ |
| victory | `FIGHT GOOD(=+4) HAPPEN(=+5) \| o` | victory / win / triumph | ✓ |
| dance | `ART(=+5) MOVE BODY \| i` | dance / ballet / perform | ✓ |
| shore | `PLACE GRAIN(=-3) NEAR(=+4) \| o` | shore / coast / beach | ✓ |
| old | `LIVE TIME(=-5) \| a` | old / elderly / aged | ✓ |
| singer | `SOMEONE SAY FEEL(=+3) \| o` | singer / vocalist / musician | ✓ |
| youth | `SOMEONE LIVE TIME(=-1) PART(=+5) \| o` | youth / young people / teenager | ✓ |
