# Время и стороны света: слепой тест

Вопрос: как выразить единицы времени, части суток, «вчера / сегодня / завтра» и стороны света — лакуны из [lacunae.md](../lacunae.md) (*year, month, night, north…*: код раскрывался в *before, after, across*). Слова: *second, minute, hour, day, week, month, year, decade, century, moment, morning, noon, evening, night, midnight, today, tomorrow, yesterday, annual, north, south, east, west, northern*.

Кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер — только таблицы и правила чтения, оригиналов не видит, коды перемешаны. Наборы A — нынешняя спецификация, наборы B — с рецептами ниже (их видят и кодировщик, и декодер). Модель sonnet, 2 кодировщика и по 1 декодеру на набор. Счёт строгий: ✓ лучшее слово = оригинал, ~ оригинал среди трёх.

**Рецепты набора B**

**Время: единицы, дни, части суток.**

- Отрезок времени — `TIME(=0) BIG(=n) | o`, величина задаётся уровнем BIG: −5 секунда, −4 минута, −2 час, 0 день (сутки), +1 неделя, +2 месяц, +3 год, +4 десятилетие, +5 век. Миг — `TIME(=0) BIG(=-5) MANY(=+1)`.
- Какой именно день или год: уровень TIME — сдвиг от «сейчас»: вчера = `TIME(=-1) BIG(=0) | e`, завтра = `TIME(=+1) BIG(=0) | e`, сегодня = `TIME(=0) BIG(=0) NEAR(=+5) | e` («этот день»); так же для года, месяца.
- Часть суток — день с уровнем BEGIN: `TIME(=0) BIG(=0) BEGIN(=n) | o`: −4 утро, 0 полдень, +3 вечер, +5 ночь; полночь — `BEGIN(=+5)` с усилением `| o C+5`.
- Ежегодный, ежедневный — отрезок как признак с MANY(=+5) («каждый»): `TIME(=0) BIG(=+3) MANY(=+5) | a`.

**Стороны света** — «стороны земли»: `PLACE BIG(=+5)` и направление. Восток — перёд, там встаёт солнце: `PLACE BIG(=+5) SIDE(=+5) | o`; запад — зад, `SIDE(=-5)`; север — верх карты, `PLACE BIG(=+5) ABOVE(=+5) | o`; юг — низ, `ABOVE(=-5)`. Признак (северный) — та же запись с `| a`.

| группа | A1 | A2 | B1 | B2 |
| :-- | --: | --: | --: | --: |
| единицы (10) | 5 / 7 | 2 / 6 | 10 / 10 | 10 / 10 |
| части суток, вчера / сегодня / завтра, ежегодный (9) | 6 / 7 | 8 / 9 | 9 / 9 | 9 / 9 |
| стороны света (5) | 2 / 2 | 2 / 2 | 5 / 5 | 5 / 5 |
| всего (24) | 13 / 16 | 12 / 17 | 24 / 24 | 24 / 24 |

Что видно:

- **Шкала единиц нужна**: без неё кодировщики пишут `TIME MEASURE BIG(=n)` с разными уровнями, и декодер путает неделю, месяц, час и год. С фиксированной шкалой `TIME(=0) BIG(=n)` — 20 из 20.
- **Части суток и «вчера / завтра» почти работают и сейчас** (14 из 18): утро, вечер, полдень, вчера, завтра собираются любыми разумными кодами.
- **Стороны света**: без рецепта кодировщики сами пришли к солнцу — восток `PLACE SEE BEGIN(=-3)` («где начинается свет»), запад `BEGIN(=+3)` — и это читается (4 из 4); север и юг как `PLACE ABOVE(=±4)` читаются как *верх, низ* (0 из 6). Рецепт с «землёй» `PLACE BIG(=+5)` — 10 из 10.

Оговорки: шкала и рецепты были у декодера B в явном виде, так что B проверяет, что запись однозначна и не путается, а не что её угадают без правил; по одному декодеру на набор; шум порядка ±3 из 24.

## Набор A1

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| second | `TIME(=0) MEASURE BIG(=-5) \| o` | second / moment / minute | ✓ |
| evening | `TIME(=0) SEE BEGIN(=+3) \| o` | evening / sunset / dusk | ✓ |
| noon | `TIME(=0) SEE ABOVE(=+5) \| o` | noon / midday / afternoon | ✓ |
| night | `TIME(=0) SEE CAN(=-3) \| o` | dusk / twilight / evening |  |
| day | `TIME(=0) SEE HEAT(=+3) \| o` | day / today / daytime | ✓ |
| minute | `TIME(=0) MEASURE BIG(=-3) \| o` | minute / second / moment | ✓ |
| yesterday | `TIME(=0) SEE HEAT(=+3) \| e T-2` | yesterday / before / earlier | ✓ |
| month | `TIME(=0) MEASURE BIG(=+4) \| o` | week / day / hour |  |
| hour | `TIME(=0) MEASURE(=0) \| o` | time / hour / period | ~ |
| week | `TIME(=0) MEASURE BIG(=+3) \| o` | hour / day / week | ~ |
| north | `PLACE ABOVE(=+4) \| o` | top / up / sky |  |
| year | `TIME(=0) MEASURE BIG(=+5) \| o` | year / month / century | ✓ |
| south | `PLACE ABOVE(=-4) \| o` | bottom / floor / below |  |
| century | `TIME(=0) BIG(=+5) MANY(=+5) \| o` | always / forever / eternity |  |
| moment | `TIME(=0) PART(=-5) \| o` | moment / instant / second | ✓ |
| decade | `TIME(=0) BIG(=+5) MANY(=+3) \| o` | often / frequently / sometimes |  |
| northern | `PLACE ABOVE(=+4) \| a` | high / upper / top |  |
| annual | `TIME(=0) MEASURE BIG(=+5) \| a` | long / lasting / lengthy |  |
| today | `TIME(=0) SEE HEAT(=+3) \| e` | today / now / daily | ✓ |
| morning | `TIME(=0) SEE BEGIN(=-3) \| o` | morning / dawn / sunrise | ✓ |
| east | `PLACE SEE BEGIN(=-3) \| o` | east / sunrise / dawn | ✓ |
| midnight | `TIME(=0) SEE CAN(=-5) \| o` | night / dark / midnight | ~ |
| west | `PLACE SEE BEGIN(=+3) \| o` | west / sunset / evening | ✓ |
| tomorrow | `TIME(=0) SEE HEAT(=+3) \| e T+2` | tomorrow / later / soon | ✓ |

## Набор A2

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| hour | `TIME MEASURE BIG(=-2) \| o` | minute / moment / second |  |
| month | `TIME MEASURE BIG(=+2) \| o` | week / hour / day |  |
| yesterday | `TIME MEASURE BIG(=0) \| e T-1` | yesterday / ago / before | ✓ |
| north | `PLACE ABOVE(=+5) \| o` | sky / top / heaven |  |
| day | `TIME MEASURE BIG(=0) \| o` | hour / day / time | ~ |
| minute | `TIME MEASURE BIG(=-4) \| o` | second / instant / moment |  |
| northern | `PLACE ABOVE(=+5) \| a` | upper / high / top |  |
| moment | `TIME(=0) BIG(=-5) \| o` | moment / instant / now | ✓ |
| west | `PLACE BEGIN(=+4) SEE \| o` | west / horizon / end | ✓ |
| year | `TIME MEASURE BIG(=+3) \| o` | month / season / week |  |
| annual | `TIME MEASURE BIG(=+3) \| a` | monthly / long / annual | ~ |
| evening | `TIME BEGIN(=+4) SEE \| o` | evening / sunset / dusk | ✓ |
| second | `TIME MEASURE BIG(=-5) \| o` | moment / instant / second | ~ |
| south | `PLACE ABOVE(=-5) \| o` | bottom / floor / ground |  |
| tomorrow | `TIME MEASURE BIG(=0) \| e T+1` | tomorrow / soon / later | ✓ |
| east | `PLACE BEGIN(=-4) SEE \| o` | east / sunrise / start | ✓ |
| today | `TIME MEASURE BIG(=0) \| e T0` | today / now / present | ✓ |
| midnight | `TIME SEE ABOVE(=-5) \| o` | midnight / night / dark | ✓ |
| night | `TIME SEE \| o M-5` | night / darkness / dark | ✓ |
| morning | `TIME BEGIN(=-4) SEE \| o` | morning / dawn / sunrise | ✓ |
| week | `TIME MEASURE BIG(=+1) \| o` | day / week / hour | ~ |
| decade | `TIME MEASURE BIG(=+4) \| o` | year / decade / season | ~ |
| century | `TIME MEASURE BIG(=+5) \| o` | century / decade / era | ✓ |
| noon | `TIME SEE ABOVE(=+5) \| o` | noon / day / midday | ✓ |

## Набор B1

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| midnight | `TIME(=0) BIG(=0) BEGIN(=+5) \| o C+5` | midnight / night / late | ✓ |
| month | `TIME(=0) BIG(=+2) \| o` | month / monthly / moon | ✓ |
| day | `TIME(=0) BIG(=0) \| o` | day / daily / date | ✓ |
| noon | `TIME(=0) BIG(=0) BEGIN(=0) \| o` | noon / midday / afternoon | ✓ |
| hour | `TIME(=0) BIG(=-2) \| o` | hour / time / hourly | ✓ |
| south | `PLACE BIG(=+5) ABOVE(=-5) \| o` | south / down / southern | ✓ |
| yesterday | `TIME(=-1) BIG(=0) \| e` | yesterday / past / before | ✓ |
| morning | `TIME(=0) BIG(=0) BEGIN(=-4) \| o` | morning / dawn / sunrise | ✓ |
| north | `PLACE BIG(=+5) ABOVE(=+5) \| o` | north / up / northern | ✓ |
| moment | `TIME(=0) BIG(=-5) MANY(=+1) \| o` | moment / instant / flash | ✓ |
| today | `TIME(=0) BIG(=0) NEAR(=+5) \| e` | today / now / this day | ✓ |
| evening | `TIME(=0) BIG(=0) BEGIN(=+3) \| o` | evening / dusk / sunset | ✓ |
| night | `TIME(=0) BIG(=0) BEGIN(=+5) \| o` | night / tonight / dark | ✓ |
| northern | `PLACE BIG(=+5) ABOVE(=+5) \| a` | northern / north / upper | ✓ |
| west | `PLACE BIG(=+5) SIDE(=-5) \| o` | west / western / sunset | ✓ |
| week | `TIME(=0) BIG(=+1) \| o` | week / weekly / weekend | ✓ |
| century | `TIME(=0) BIG(=+5) \| o` | century / centuries / era | ✓ |
| second | `TIME(=0) BIG(=-5) \| o` | second / sec / instant | ✓ |
| annual | `TIME(=0) BIG(=+3) MANY(=+5) \| a` | annual / yearly / everyyear | ✓ |
| minute | `TIME(=0) BIG(=-4) \| o` | minute / min / moment | ✓ |
| tomorrow | `TIME(=+1) BIG(=0) \| e` | tomorrow / next day / future | ✓ |
| year | `TIME(=0) BIG(=+3) \| o` | year / yearly / annual | ✓ |
| east | `PLACE BIG(=+5) SIDE(=+5) \| o` | east / eastern / sunrise | ✓ |
| decade | `TIME(=0) BIG(=+4) \| o` | decade / decades / ten years | ✓ |

## Набор B2

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| year | `TIME(=0) BIG(=+3) \| o` | year / annual / yearly | ✓ |
| tomorrow | `TIME(=+1) BIG(=0) \| e` | tomorrow / later / future | ✓ |
| today | `TIME(=0) BIG(=0) NEAR(=+5) \| e` | today / now / this day | ✓ |
| noon | `TIME(=0) BIG(=0) BEGIN(=0) \| o` | noon / midday / afternoon | ✓ |
| morning | `TIME(=0) BIG(=0) BEGIN(=-4) \| o` | morning / dawn / early | ✓ |
| west | `PLACE BIG(=+5) SIDE(=-5) \| o` | west / western / sunset | ✓ |
| yesterday | `TIME(=-1) BIG(=0) \| e` | yesterday / past / before | ✓ |
| decade | `TIME(=0) BIG(=+4) \| o` | decade / ten years / era | ✓ |
| east | `PLACE BIG(=+5) SIDE(=+5) \| o` | east / eastern / sunrise | ✓ |
| annual | `TIME(=0) BIG(=+3) MANY(=+5) \| a` | annual / yearly / every year | ✓ |
| century | `TIME(=0) BIG(=+5) \| o` | century / age / era | ✓ |
| minute | `TIME(=0) BIG(=-4) \| o` | minute / moment / second | ✓ |
| second | `TIME(=0) BIG(=-5) \| o` | second / instant / moment | ✓ |
| day | `TIME(=0) BIG(=0) \| o` | day / daytime / date | ✓ |
| night | `TIME(=0) BIG(=0) BEGIN(=+5) \| o` | night / midnight / dark | ✓ |
| evening | `TIME(=0) BIG(=0) BEGIN(=+3) \| o` | evening / dusk / afternoon | ✓ |
| north | `PLACE BIG(=+5) ABOVE(=+5) \| o` | north / northern / up | ✓ |
| south | `PLACE BIG(=+5) ABOVE(=-5) \| o` | south / southern / down | ✓ |
| week | `TIME(=0) BIG(=+1) \| o` | week / weekly / weekend | ✓ |
| hour | `TIME(=0) BIG(=-2) \| o` | hour / time / clock | ✓ |
| month | `TIME(=0) BIG(=+2) \| o` | month / monthly / moon | ✓ |
| midnight | `TIME(=0) BIG(=0) BEGIN(=+5) \| o C+5` | midnight / night / dead of night | ✓ |
| moment | `TIME(=0) BIG(=-5) MANY(=+1) \| o` | moment / instant / flash | ✓ |
| northern | `PLACE BIG(=+5) ABOVE(=+5) \| a` | northern / north / arctic | ✓ |
