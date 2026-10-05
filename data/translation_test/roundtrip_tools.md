# Орудия: слепой круговой тест с меткой `U` и без неё (12 слов, 2 кодировщика, 2 декодера на набор)

Слова: knife, hammer, saw, needle, key, spoon, brush, scissors, pen, broom, ladder, thermometer. Кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер — только таблицы и правила чтения (раздел «Как читается код» из SKILL.md), оригиналов не видит, коды перемешаны. В наборах B кодировщик и декодер дополнительно видят описание экспериментальной метки `U` (орудие, как эсперантское *-il-*: «корни описывают действие, `U` делает из него орудие», пример `SEE | o U` — очки, бинокль). Модель: sonnet (субагенты).

| | без `U` | с `U` |
| :-- | :-- | :-- |
| точно (лучшее слово = оригинал) | 1 из 24 | 13 из 24 |
| оригинал среди трёх ответов | 3 из 24 | 17 из 24 |

Что получилось. Без метки оба кодировщика независимо тратят корень на `THING(=-5)` («неживая вещь»), а декодер читает его буквально как камень: *knife* → *pebble*, *saw* → *landslide*, *ladder* → *meteor* (набор A1 — 0 из 12). С меткой корни описывают действие (`JOIN(=-4) TOUCH(=+4) | o U` — то, чем режут), и орудие узнаётся: hammer, thermometer, knife — в обоих наборах, spoon, brush, broom, saw, scissors, needle, ladder — в одном из двух.

Не собираются и с меткой: *key* (`CAN(=+5) PLACE INSIDE(=+5) | o U` читается как *box, container*: «открыть» нечем выразить) и *pen* (`CONSUME(=-5) SEE | o U` — «выделять + видеть» читается как свет, *lamp*, в обоих наборах).

Оговорки: выборка 12 слов, 2 кодировщика, 1 декодер на набор; слова выбраны под метку; в наборах без `U` проигрыш во многом от одного неудачного приёма (`THING(=-5)`), а не только от отсутствия метки. Шум порядка ±3 слов.


## Набор A1 (без U)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| knife | `THING(=-5) JOIN(=-4) TOUCH(=+5) \| o` | pebble / shard / flint |  |
| thermometer | `THING(=-5) HEAT MEASURE(=0) \| o` | coal / ember / lava |  |
| saw | `THING(=-5) JOIN(=-4) MOVE \| o` | landslide / avalanche / rockfall |  |
| brush | `THING(=-5) TOUCH(=-3) DO \| o` | chalk / clay / plaster |  |
| hammer | `THING(=-5) TOUCH(=+5) MOVE(=+4) \| o` | bullet / hailstone / projectile |  |
| key | `THING(=-5) CAN(=+5) INSIDE(=+5) \| o` | cave / tunnel / cavern |  |
| needle | `THING(=-5) LONG(=0) JOIN(=+3) \| o` | bridge / chain / pipe |  |
| broom | `THING(=-5) GRAIN(=0) JOIN(=-4) \| o` | sand / gravel / dust |  |
| spoon | `THING(=-5) CONSUME(=+5) MATTER(=0) \| o` | salt / mineral / sponge |  |
| ladder | `THING(=-5) ABOVE(=+4) MOVE \| o` | meteor / meteorite / rocket |  |
| scissors | `THING(=-5) JOIN(=-4) MANY(=+2) \| o` | rubble / gravel / pebbles |  |
| pen | `THING(=-5) CONSUME(=-5) SEE \| o` | glass / crystal / mirror |  |

## Набор A2 (без U)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| thermometer | `THING(=-5) HEAT MEASURE \| o` | thermometer / thermostat / heater | = |
| broom | `THING(=-5) LONG(=0) JOIN(=-4) \| o` | knife / scissors / saw |  |
| spoon | `THING(=-5) CONSUME(=+5) MATTER(=0) \| o` | sponge / cup / bowl |  |
| brush | `THING(=-5) TOUCH(=-3) MOVE(=+1) \| o` | sail / flag / curtain |  |
| needle | `THING(=-5) LONG(=0) JOIN(=+3) \| o` | nail / screw / pin |  |
| saw | `THING(=-5) JOIN(=-4) MOVE \| o` | plow / saw / razor | ~ |
| ladder | `THING(=-5) MOVE ABOVE(=+5) \| o` | rocket / elevator / balloon |  |
| knife | `THING(=-5) JOIN(=-4) TOUCH(=+5) \| o` | wall / fence / door |  |
| scissors | `THING(=-5) JOIN(=-4) LONG(=-5) \| o` | fence / net / curtain |  |
| key | `THING(=-5) CAN(=+5) INSIDE(=+4) \| o` | box / bag / bottle |  |
| hammer | `THING(=-5) TOUCH(=+5) MOVE(=+4) \| o` | bullet / bomb / hammer | ~ |
| pen | `THING(=-5) CONSUME(=-5) SEE \| o` | lamp / screen / mirror |  |

## Набор B1 (с U)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| spoon | `CONSUME(=+5) MATTER(=0) \| o U` | spoon / cup / straw | = |
| brush | `TOUCH(=-3) MOVE CARE(=+3) \| o U` | brush / sponge / feather | = |
| broom | `JOIN(=-4) PART(=-5) MOVE \| o U` | broom / brush / dustpan | = |
| hammer | `TOUCH(=+4) MOVE(=+4) JOIN(=+3) \| o U` | hammer / mallet / nail gun | = |
| saw | `JOIN(=-4) TOUCH(=+4) MOVE \| o U` | saw / axe / chisel | = |
| scissors | `JOIN(=-4) LONG(=-5) MANY(=+2) \| o U` | comb / rake / brush |  |
| key | `PLACE INSIDE(=+5) CAN(=+5) \| o U` | box / bag / basket |  |
| knife | `JOIN(=-4) TOUCH(=+4) \| o U` | knife / scissors / axe | = |
| pen | `CONSUME(=-5) SEE \| o U` | lamp / flashlight / torch |  |
| thermometer | `MEASURE HEAT \| o U` | thermometer / thermostat / gauge | = |
| ladder | `MOVE ABOVE(=+4) CAN(=+4) \| o U` | elevator / ladder / crane | ~ |
| needle | `JOIN(=+3) LONG(=0) TOUCH(=+4) \| o U` | nail / screw / bolt |  |

## Набор B2 (с U)

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| spoon | `CONSUME(=+5) GRAIN(=-5) \| o U` | straw / cup / spoon | ~ |
| key | `CAN(=+5) PLACE INSIDE(=+5) \| o U` | container / box / bag |  |
| broom | `JOIN(=-4) GRAIN(=0) \| o U` | sieve / strainer / sifter |  |
| brush | `TOUCH(=-3) MOVE(=+2) JOIN(=-2) \| o U` | eraser / sponge / brush | ~ |
| saw | `JOIN(=-5) LONG(=+5) \| o U` | axe / saw / cleaver | ~ |
| needle | `JOIN(=+4) LONG(=-5) TOUCH(=+5) \| o U` | needle / pin / awl | = |
| pen | `CONSUME(=-5) SEE \| o U` | lamp / flashlight / candle |  |
| thermometer | `MEASURE HEAT \| o U` | thermometer / thermostat / heater | = |
| scissors | `JOIN(=-5) LONG(=-5) \| o U` | scissors / shears / knife | = |
| ladder | `MOVE ABOVE(=+4) LONG(=0) \| o U` | ladder / lever / crutch | = |
| hammer | `TOUCH(=+4) MOVE(=+4) JOIN(=+3) \| o U` | hammer / mallet / nail gun | = |
| knife | `JOIN(=-5) CONSUME(=+5) MATTER(=-5) \| o U` | knife / fork / cleaver | = |
