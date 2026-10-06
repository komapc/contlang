# Общество, власть, учёба, война: слепой тест

Вопрос: закрыть следующие кластеры лакун ([lacunae.md](../lacunae.md)) рецептами на существующих корнях. Слова (24): *trust, friend, ally, leader, agreement, safe, king, government, vote, election, citizen, city, school, student, teacher, university, film, advertise, enemy, battle, gun, defend, attack, soldier*.

Протокол как в [roundtrip_lacunae3](roundtrip_lacunae3.md): A — нынешняя спецификация, B — с рецептами (их видят кодировщик и декодер); sonnet, 2 кодировщика, по 1 декодеру на набор; ✓ лучшее слово = оригинал (синонимы: *protect* = *defend*, *movie* = *film*, *town* = *city*), ~ среди трёх. Кавычки для обычных слов запрещены.

**Рецепты набора B**

- **Общество**: доверять = `THINK(=+5) GOOD(=+4) | i`, друг = `SOMEONE WANT(=+3) JOIN(=+3) | o`, союзник = `SOMEONE FIGHT JOIN(=+4) | o`, лидер = `SOMEONE SIDE(=+5) RULE | o`, соглашение = `THINK(=+5) SAME(=+5) | o`, безопасный = `GOOD(=-4) CAN(=-5) | a` («вред невозможен»).
- **Власть**: король = `SOMEONE RULE(=+5) SEX(=+5) | o`, правительство = `SOMEONE RULE(=+5) PART(=+5) | o`, голосовать = `THINK(=+5) MANY(=+5) | i`, выборы = `THINK(=+5) MANY(=+5) RULE(=+4) | o`, гражданин = `SOMEONE PART(=-2) RULE(=+4) | o`, город = `PLACE SOMEONE MANY(=+5) | o`.
- **Учёба и кино**: школа = `PLACE KNOW CONSUME(=+5) | o`, ученик = `SOMEONE KNOW CONSUME(=+5) | o`, учитель = `SOMEONE KNOW GIVE(=+4) | o`, университет = `PLACE KNOW ABOVE(=+4) | o`, фильм = `ART(=+5) SEE MOVE | o`, рекламировать = `SAY GIVE(=+3) VALUE | i`.
- **Война**: враг = `SOMEONE WANT(=-4) FIGHT | o`, битва = `FIGHT(=+5) PART(=-2) | o`, ружьё = `DO(=+5) FIGHT(=+5) HEAT(=+5) | o`, защищать = `DO GOOD(=-4) | i K-4` («не дать навредить»), нападать = `FIGHT(=+4) BEGIN(=-5) | i`, солдат = `SOMEONE FIGHT(=+5) RULE(=+4) | o`.

| набор | A1 | A2 | B1 | B2 |
| :-- | --: | --: | --: | --: |
| ✓ / ✓+~ из 24 | 13 / 17 | 19 / 20 | 24 / 24 | 24 / 24 |

Что видно:

- **Многое работает без рецептов**: друг, союзник, лидер, соглашение, король, правительство, город, ученик, учитель, фильм, битва, защищать, нападать — кодировщики A пишут почти те же коды.
- **Настоящие лакуны** (0–1 из 2 в A): *safe* (`GOOD(=-4) HAPPEN …` → *hopeless, futile*; с `CAN(=-5)` — «вред невозможен» — 2 из 2), *gun* (`FIGHT MOVE(=+5) DO(=+5)` → *missile*; нужен огонь `HEAT(=+5)`), *advertise* (*praise*, *bid*; нужно `GIVE(=+3)` — «чтобы продать»), *trust* (`KNOW …` → *understand, respect*; нужно `THINK(=+5)` — «решить»), *vote / election* (без `MANY(=+5)` — *decide*, *committee*), *citizen* (*member*, *officer*).
- *soldier* у A1 закодирован ровно по рецепту, а декодер прочёл *police* — разброс декодера: `RULE(=+4)` тянет к полиции.
- Оружие теперь — орудие `DO(=+5) FIGHT(=+5)`, как машины (`DO(=+5) MOVE(=+4)`), а не «камень» `THING(=-5)`.
- Оговорка: декодер B видел рецепты.

## По словам

| слово | A1 | A2 | B1 | B2 | код A1 | код A2 |
| :-- | :-: | :-: | :-: | :-: | :-- | :-- |
| trust | ✗ understand | ~ respect | ✓ | ✓ | `KNOW(=+5) WANT(=+3) \| i` | `KNOW(=+3) GOOD(=+4) SOMEONE \| i` |
| friend | ✓ | ✓ | ✓ | ✓ | `SOMEONE TONE(=+4) WANT(=+3) \| o` | `SOMEONE WANT(=+3) TONE(=+4) \| o` |
| ally | ✓ | ✓ | ✓ | ✓ | `SOMEONE FIGHT(=+5) JOIN(=+4) \| o` | `SOMEONE JOIN(=+4) FIGHT \| o` |
| leader | ✓ | ✓ | ✓ | ✓ | `SOMEONE RULE(=+3) SIDE(=+5) \| o` | `SOMEONE SIDE(=+5) MOVE \| o` |
| agreement | ✓ | ✓ | ✓ | ✓ | `SAY SAME(=+5) THINK(=+5) \| o` | `SAME(=+5) SAY THINK(=+5) \| o` |
| safe | ✗ unsuccessful | ✗ hopeless | ✓ | ✓ | `HAPPEN(=+5) GOOD(=-4) MANY(=0) \| a` | `GOOD(=-4) HAPPEN(=+5) CAN(=-5) \| a` |
| king | ✓ | ✓ | ✓ | ✓ | `SOMEONE SEX(=+5) RULE(=+5) \| o` | `SOMEONE RULE(=+5) SEX(=+5) \| o` |
| government | ✓ | ✓ | ✓ | ✓ | `SOMEONE PART(=+5) RULE(=+5) \| o` | `SOMEONE RULE(=+5) PART(=+5) \| o` |
| vote | ✗ decide | ✓ | ✓ | ✓ | `THINK(=+5) RULE(=+4) \| i` | `THINK(=+5) RULE(=+4) MANY \| i` |
| election | ✗ committee | ✓ | ✓ | ✓ | `THINK(=+5) RULE(=+4) PART(=+5) \| o` | `THINK(=+5) RULE(=+4) MANY \| o` |
| citizen | ~ member | ✗ officer | ✓ | ✓ | `SOMEONE PART(=-2) RULE(=+4) \| o` | `SOMEONE RULE(=+4) PART(=-2) \| o` |
| city | ✓ | ✓ | ✓ | ✓ | `PLACE SOMEONE BIG(=+5) \| o` | `PLACE SOMEONE MANY(=+5) \| o` |
| school | ~ college | ✓ | ✓ | ✓ | `PLACE KNOW SOMEONE \| o` | `PLACE KNOW RULE(=+4) \| o` |
| student | ✓ | ✓ | ✓ | ✓ | `SOMEONE CONSUME(=+5) KNOW \| o` | `SOMEONE KNOW CONSUME(=+5) \| o` |
| teacher | ✓ | ✓ | ✓ | ✓ | `SOMEONE KNOW CONSUME(=-5) \| o` | `SOMEONE KNOW GIVE(=+4) \| o` |
| university | ~ school | ✓ | ✓ | ✓ | `PLACE KNOW ABSTRACT(=+5) \| o` | `PLACE KNOW ABSTRACT(=+5) \| o` |
| film | ✓ | ✓ | ✓ | ✓ | `SEE ART(=+5) MOVE \| o` | `SEE MOVE ART(=+5) \| o` |
| advertise | ✗ praise | ✗ bid | ✓ | ✓ | `SAY(=+4) VALUE \| i` | `SAY VALUE MANY(=+5) \| i` |
| enemy | ~ soldier | ✓ | ✓ | ✓ | `SOMEONE FIGHT(=+5) \| o` | `SOMEONE FIGHT(=+4) WANT(=-5) \| o` |
| battle | ✓ | ✓ | ✓ | ✓ | `FIGHT(=+4) BIG(=-2) \| o` | `FIGHT(=+3) TIME(=0) \| o` |
| gun | ✗ missile | ✗ missile | ✓ | ✓ | `FIGHT(=+5) MOVE(=+5) DO(=+5) \| o` | `FIGHT(=+5) MOVE(=+5) DO(=+5) \| o` |
| defend | ✓ | ✓ | ✓ | ✓ | `FIGHT(=+3) CARE(=+4) \| i` | `FIGHT INSIDE(=+5) CARE(=+4) \| i` |
| attack | ✓ | ✓ | ✓ | ✓ | `FIGHT(=+4) MOVE(=+4) \| i` | `FIGHT MOVE(=+4) NEAR(=+5) \| i` |
| soldier | ✗ police | ✓ | ✓ | ✓ | `SOMEONE FIGHT(=+5) RULE(=+4) \| o` | `SOMEONE FIGHT(=+5) RULE(=+4) \| o` |
