# Право, деньги, еда, транспорт и постройки: слепой тест

Вопрос: закрыть четыре кластера лакун ([lacunae.md](../lacunae.md)) рецептами на существующих корнях. Слова (24): *crime, criminal, court, judge, prison, steal, money, pay, debt, rich, poor, market, cook, meat, vegetable, farm, harvest, kitchen, car, ship, road, bridge, house, room*.

Протокол как в [roundtrip_lacunae2](roundtrip_lacunae2.md): A — нынешняя спецификация, B — с рецептами ниже (их видят кодировщик и декодер); sonnet, 2 кодировщика, по 1 декодеру на набор; ✓ лучшее слово = оригинал (синонимы: *home* = *house*, *boat* = *ship*), ~ среди трёх.

**Рецепты набора B**

**Право** — `RULE(=+4)` (закон) с `GOOD(=-4)` (нарушение): преступление = `DO GOOD(=-4) RULE(=+4) | o`, преступник = `SOMEONE GOOD(=-4) RULE(=+4) | o`, суд = `PLACE RULE(=+4) THINK(=+5) | o` («место, где закон решает»), судья = `SOMEONE RULE(=+4) THINK(=+5) | o`, тюрьма = `PLACE MOVE(=-5) RULE(=+4) | o`, украсть = `GIVE(=-4) GOOD(=-4) | i`.

**Деньги** — `VALUE` с `GIVE`, главный корень решает, что отдают: деньги = `VALUE GIVE(=0) | o` («ценность для обмена»), платить = `VALUE GIVE(=+4) | i` (продать — `GIVE(=+3) VALUE | i`), долг = `VALUE GIVE(=+4) TIME(=+3) | o` («отдать потом»), богатый = `VALUE MANY(=+5) | a`, бедный = `VALUE MANY(=0) | a`, рынок = `PLACE GIVE(=0) VALUE | o`.

**Еда** — `CONSUME(=+5)` с родом вещи `THING`: мясо = `CONSUME(=+5) THING(=+4) | o`, овощ = `CONSUME(=+5) THING(=0) | o`, готовить = `HEAT(=+3) CONSUME(=+5) | i`, кухня = `PLACE HEAT(=+3) CONSUME(=+5) | o`, ферма = `PLACE THING(=0) DO | o`, собирать урожай = `GIVE(=-4) THING(=0) PART(=+5) | i`.

**Транспорт и постройки** — орудие `DO(=+5)` и `PLACE`: машина = `DO(=+5) MOVE(=+4) | o`, корабль = `DO(=+5) MOVE GRAIN(=-3) | o`, дорога = `PLACE MOVE LONG(=-3) | o`, мост = `PLACE MOVE ABOVE(=+4) | o`, дом = `PLACE INSIDE(=+5) LIVE | o`, комната = `PLACE INSIDE(=+5) PART(=-2) | o`.

| набор | A1 | A2 | B1 | B2 |
| :-- | --: | --: | --: | --: |
| ✓ / ✓+~ из 24 | 17 / 19 | 17 / 18 | 24 / 24 | 24 / 24 |

Что видно:

- **Право, еда, дом почти работают без рецептов**: кодировщики A сами пишут `DO GOOD(=-4) RULE`, `CONSUME(=+5) THING(=0)`, `PLACE CONSUME HEAT`, `PLACE LIVE INSIDE` — те же коды, что в рецептах. Рецепт снимает разнобой. A2 взял в кавычки *court, judge, prison* (правило кавычек разрешает учреждения без корня) — так угадывается, но это обход языка; с рецептом кавычки не нужны.
- **Настоящие лакуны** (0–1 из 4 в A): *money* (`VALUE GIVE(=0)` без рецепта — *price*), *debt* (*loan*, *wage*), *harvest* (`JOIN THING(=0)` — *plant*), *ship* (`THING(=-5) MOVE GRAIN(=-3)` — *train*, *wind*), *bridge* (`PLACE MOVE JOIN` — *intersection*, *station*), *farm* (*garden*). Орудие `DO(=+5)` вместо «камня» `THING(=-5)` для машин — 4 из 4 против 1 из 2.
- Оговорка: декодер B видел рецепты, как и в прошлых тестах.

## По словам

| слово | A1 | A2 | B1 | B2 | код A1 | код A2 |
| :-- | :-: | :-: | :-: | :-: | :-- | :-- |
| crime | ✓ | ✓ | ✓ | ✓ | `DO GOOD(=-4) RULE(=+5) \| o` | `DO GOOD(=-4) RULE(=+4) \| o` |
| criminal | ✓ | ✓ | ✓ | ✓ | `SOMEONE GOOD(=-4) RULE(=+5) \| o` | `SOMEONE GOOD(=-4) RULE(=+4) \| o` |
| court | ✓ | ✓ | ✓ | ✓ | `PLACE RULE(=+5) THINK(=+5) \| o` | `"court"` |
| judge | ✓ | ✓ | ✓ | ✓ | `SOMEONE RULE(=+5) THINK(=+5) \| o` | `"judge"` |
| prison | ✓ | ✓ | ✓ | ✓ | `PLACE RULE(=+5) CAN(=-4) \| o` | `"prison"` |
| steal | ✓ | ✓ | ✓ | ✓ | `GIVE(=-5) VALUE GOOD(=-4) \| i` | `GIVE(=-5) GOOD(=-4) \| i` |
| money | ✗ price | ✗ price | ✓ | ✓ | `VALUE GIVE(=0) \| o` | `VALUE GIVE(=0) \| o` |
| pay | ✓ | ✓ | ✓ | ✓ | `GIVE(=+3) VALUE \| i` | `GIVE(=+5) VALUE \| i` |
| debt | ~ loan | ✗ wage | ✓ | ✓ | `VALUE GIVE(=+3) TIME(=+3) \| o` | `GIVE VALUE TIME(=+3) \| o` |
| rich | ✓ | ✓ | ✓ | ✓ | `SOMEONE VALUE(=+5) MANY(=+4) \| a` | `SOMEONE VALUE(=+4) MANY(=+5) \| a` |
| poor | ✗ wealthy | ✓ | ✓ | ✓ | `SOMEONE VALUE MANY(=+1) \| a` | `SOMEONE VALUE(=-4) MANY(=0) \| a` |
| market | ✓ | ✓ | ✓ | ✓ | `PLACE GIVE(=0) VALUE \| o` | `PLACE GIVE(=0) VALUE \| o` |
| cook | ✓ | ✓ | ✓ | ✓ | `CHANGE(=+4) HEAT(=+4) CONSUME(=+5) \| i` | `DO CONSUME(=+5) HEAT(=+4) \| i` |
| meat | ✓ | ✓ | ✓ | ✓ | `CONSUME(=+5) THING(=+4) BODY \| o` | `CONSUME(=+5) THING(=+4) BODY \| o` |
| vegetable | ✓ | ✓ | ✓ | ✓ | `CONSUME(=+5) THING(=0) \| o` | `CONSUME(=+5) THING(=0) \| o` |
| farm | ~ garden | ~ garden | ✓ | ✓ | `PLACE THING(=0) DO \| o` | `PLACE THING(=0) DO \| o` |
| harvest | ✗ plant | ✗ plant | ✓ | ✓ | `JOIN(=+3) THING(=0) HAPPEN(=+5) \| i` | `THING(=0) JOIN(=+3) \| i` |
| kitchen | ✓ | ✓ | ✓ | ✓ | `PLACE CONSUME(=+5) HEAT(=+4) \| o` | `PLACE CONSUME(=+5) HEAT(=+4) \| o` |
| car | ✓ | ✗ bullet | ✓ | ✓ | `THING(=-5) MOVE(=+4) SOMEONE \| o` | `THING(=-5) MOVE(=+4) INSIDE(=+4) \| o` |
| ship | ✗ train | ✗ wind | ✓ | ✓ | `THING(=-5) MOVE GRAIN(=-3) \| o` | `THING(=-5) MOVE GRAIN(=-3) \| o` |
| road | ✓ | ✓ | ✓ | ✓ | `PLACE MOVE(=+3) LONG \| o` | `PLACE MOVE LONG(=-1) \| o` |
| bridge | ✗ intersection | ✗ station | ✓ | ✓ | `PLACE MOVE JOIN(=+4) \| o` | `PLACE MOVE JOIN(=+3) \| o` |
| house | ✓ | ✓ | ✓ | ✓ | `PLACE LIVE INSIDE(=+4) \| o` | `PLACE LIVE INSIDE(=+5) \| o` |
| room | ✓ | ✓ | ✓ | ✓ | `PLACE INSIDE(=+5) BIG(=-2) \| o` | `PLACE INSIDE PART(=-2) \| o` |
