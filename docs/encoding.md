# Как кодировать: приёмы

Приёмы подобраны слепыми тестами (кодировщик видит только спецификацию). Для каждого дана ссылка на тест; **без теста** — подсказка не проверена. Корни и оси — в [lexicon.md](lexicon.md), метки и частицы — в [syntax.md](syntax.md), модель — в [model.md](model.md). Используется скиллом `mincode` (`.claude/skills/mincode/SKILL.md`).

## Общее

- Действия без своего корня — через `DO-i E …` (делать, вызывать) или `SAY-i …` (говорить, просить) ([roundtrip_30](../data/translation_test/roundtrip_30.md)).
- «Мочь, трудно, возможно» — `CAN` (`DO CAN(=-3) | a` — *difficult*); «возможно, может быть» — метка `M-3`; корня `MAYBE` нет.
- **Животные, растения, элементы — латинскими и химическими названиями, всегда в кавычках** (решение автора): `"Serpentes"` змея, `"Canis"` собака, `"Quercus"` дуб, `"iodine"` йод; родовые категории (*animal, plant, tree, bird, fish*) — корнями (`THING(=+4)`, `THING(=0)`…). Причина: в тесте на 100 словах *snake* и *iodine* из корней читались как *animal*, *rock*.
- **Термины в кавычках.** Названия институтов и должностей (*parliament, president, official, company*), химические вещества и минералы (*sulfur dioxide, silicate*), технические и научные термины без корня (*railway, bellows, furnace, tephra, gluten*) пишутся в кавычках как есть, а не собираются из корней. В тесте на 60 предложениях ([roundtrip_wiki_new4](../data/translation_test/roundtrip_wiki_new4.md)) предложения с такими кавычками получили 2,35 из 3, остальные 1,85; собранные из корней термины читались как *price controls* (вместо *company*), *mechanical parts* (вместо *furnace*), *the authorities* (вместо *Parliament*). Обычные слова (*water, house, food*) в кавычки не ставить.
- Количество — `MANY` (ноль — ни одного, +5 — все), точные числа цифрами в кавычках.
- `ABOVE`, `INSIDE`, `BIG` — только настоящие «верх / внутри / размер»; метафора (*roof, coffee, desk*) и усилитель (`BIG(=+5)` как «очень») почти всегда читаются неверно ([roundtrip_200](../data/translation_test/roundtrip_200.md)).
- Не злоупотреблять `ABOVE` для «важного»: *elect* через `ABOVE(=+4)` читается как *worship*.
- Еда и питьё — `CONSUME`, ёмкость — `THING INSIDE | o` или `PLACE INSIDE | o` (корень `CONTAINER` убран); корней HEAR, KIND, WORD, PEOPLE больше нет (PEOPLE = `SOMEONE MANY(=+4) | o`).

## Связки: и, также, поэтому

- «И, также, ещё» — частица `AND` между сочиняемым: `X AND Y`, `[ … ] AND [ … ]`, в перечислении перед последним элементом; `JOIN`, `CHANGE`, `SAME` как связки не использовать (декодеры читали их буквально: *joined, changed*; [roundtrip_wiki4](../data/translation_test/roundtrip_wiki4.md)). Проверено ([roundtrip_wiki_new4](../data/translation_test/roundtrip_wiki_new4.md)): `AND` в 39 кодах из 60, декодеры читают её как *and / also* (54 раза), буквальных «joined» 2 вместо 8.
- **`AND` с модификаторами** (слепой тест, 2 кодировщика × 2 декодера, 11 предложений; [roundtrip_and_mod](../data/translation_test/roundtrip_and_mod.md)): оси берутся у самой частицы, порядок слов исходный. `AND SAME(=-5)` — *но, а, тогда как* (4/4 верно); `AND SAME(=-2)` — *хотя* (4/4); `AND HAPPEN(=+4)` — *поэтому, так что* (2/2); `AND HAPPEN(=-4)` — *потому что* (2/2); `AND BIG(=+4)` — *тем более, не говоря уже* (*let alone* 2/2, *what is more* читается как простое *and* + усиление); `AND MAYBE(=-3)` (теперь `AND | M-3`, не проверено) — *или* (2/2). `LA` остаётся для *если / когда*.

## Против, причина, решение

- «Против» (*protest, refuse*) — через явного носителя: `SOMEONE SAY WANT(=-5) | o` (в тесте было четыре корня, `SOMEONE MANY(=+4) SAY WANT(=-5)`, сверх лимита; трёхкорневой вариант не проверен); голое `WANT(=-5)` декодер часто игнорирует.
- Причина и следствие как предметы — ось `HAPPEN` (`HAPPEN(=-4) | o` причина, `HAPPEN(=+4) | o` следствие). «Потому что / поэтому / так как» между клаузами — `LA [ причина ] следствие` (причина стоит первой, порядок слов меняют) **без теста**.
- Решение — ось `THINK` (`THINK(=+5) | i` решить, `THINK(=-4) | i` сомневаться).

## Люди и предметы

- Местоимения — ось `SOMEONE` (я +5, ты +3, он −3), множественное через `MANY`: `SOMEONE(=+5) MANY(=+3) | o` — *we*.
- Одушевлённость — ось `THING` (камень −5, растение 0, животное +4); скорость — `MOVE`, возбуждение — `FEEL`; приятно или нет — `GOOD`.
- *grandfather, old man* = `SOMEONE SEX(=+5) TIME(=-4) | o` («предок-мужчина»; `TIME(=-4)` один даёт *ancestor*; прежний вариант с `LIVE(=+3)` был четырёхкорневым). **Без теста.**

## Эмоции, бой

- Закон и власть — `RULE`, бой и война — `FIGHT` (*peace* = `FIGHT MANY(=0) | o`).
- Ось `FIGHT` — всерьёз ли: −5 игра, спорт, соревнование по правилам … 0 драка, спор … +5 война насмерть ([roundtrip_candidates](../data/translation_test/roundtrip_candidates.md), 11 → 17 точных из 24). *game* = `FIGHT(=-5) | o`, *sport* = `FIGHT(=-5) BODY | o`, *player* = `SOMEONE FIGHT(=-5) | o`, *tournament* = `FIGHT(=-5) PART(=+5) | o`, *toy* = `THING(=-5) FIGHT(=-5) | o`, *champion* = `SOMEONE FIGHT(=-5) GOOD | o C+5`; *war* = `FIGHT(=+5) | o`, *weapon* = `DO(=+5) FIGHT(=+5) | o` (орудие боя), *soldier* = `SOMEONE FIGHT(=+5) RULE(=+4) | o`, *army* = `SOMEONE FIGHT(=+5) PART(=+5) | o`.
- Эмоции: `FEEL` (возбуждение) + `GOOD` (приятность) + корень по смыслу: страх `TIME(+3)` (плохое впереди), злость `FIGHT | a`, социальные `SOMEONE | o` (+ `SEE | i`); оси `NEAR` и `WANT` для направления не работают.
- **Настроение — `MOOD`**: −5 горе, отчаяние … −3 грусть … 0 всерьёз … +3 весело … +5 смешно ([roundtrip_mood](../data/translation_test/roundtrip_mood.md): 24 из 32 против 11 через `FEEL GOOD`, где смешное сливалось с приятным — *pleasant*, *compliment*, *praise*). *funny* = `MOOD(=+5) | a`, *joke* = `SAY MOOD(=+5) | o`, *humor* = `MOOD(=+5) ABSTRACT(=+5) | o`, *comedy* = `ART MOOD(=+5) | o`, *laugh* = `MOOD(=+5) | i`, *cheerful* = `MOOD(=+3) | a`, *smile* = `MOOD(=+3) BODY | i`, *party* = `MOOD(=+3) PART(=+5) | o`, *celebrate* = `DO MOOD(=+3) PART(=+5) | i`, *serious* = `MOOD(=0) | a`, *sad* = `MOOD(=-3) | a`, *cry* = `MOOD(=-3) CONSUME(=-5) GRAIN(=-3) | i` (выделять жидкость), *grief* = `MOOD(=-5) | o`, *despair* = `MOOD(=-5) CAN(=-5) | o`, *mourn* = `MOOD(=-5) LIVE(=-5) | i`, *funeral* = `MOOD(=-5) LIVE(=-5) PART(=+5) | o`, *tragedy* = `ART MOOD(=-5) | o`. Счастье — не настроение, а оценка: *happy* = `FEEL(=+4) GOOD(=+4) | a` (`MOOD(=+3)` читается как *cheerful*). Катастрофа — событие: `HAPPEN GOOD(=-5) | o`. `DO` перед `MOOD` в событии делает деятеля (*funeral* с `DO` → *mourner*).

## Время

- `TIME(=+1)` читается как *soon*; для «потом» его не использовать.
- *later, subsequent, earlier, before, after, initially* — метка `R`, не `TIME(=±n)` ([roundtrip_reltime](../data/translation_test/roundtrip_reltime.md)).
- Отрезок времени — `TIME(=0) BIG(=n) | o`, шкала BIG: −5 секунда, −4 минута, −2 час, 0 день (сутки), +1 неделя, +2 месяц, +3 год, +4 десятилетие, +5 век; миг — `TIME(=0) BIG(=-5) MANY(=+1) | o` ([roundtrip_time](../data/translation_test/roundtrip_time.md): 20 из 20, без шкалы 7 из 20).
- Какой именно день: уровень TIME — сдвиг от «сейчас»: вчера `TIME(=-1) BIG(=0) | e`, завтра `TIME(=+1) BIG(=0) | e`, сегодня `TIME(=0) BIG(=0) NEAR(=+5) | e` («этот день»).
- Часть суток — день с уровнем BEGIN: `TIME(=0) BIG(=0) BEGIN(=n) | o`: −4 утро, 0 полдень, +3 вечер, +5 ночь, полночь — `BEGIN(=+5) | o C+5`. Ежегодный — `TIME(=0) BIG(=+3) MANY(=+5) | a` («каждый год»).

## Стороны света

«Стороны земли»: `PLACE BIG(=+5)` и направление. Стоим лицом к восходу: восток — перёд (`SIDE(=+5)`), запад — зад (`SIDE(=-5)`); север — верх карты (`ABOVE(=+5)`), юг — низ (`ABOVE(=-5)`). Восток = `PLACE BIG(=+5) SIDE(=+5) | o`, север = `PLACE BIG(=+5) ABOVE(=+5) | o`, северный = `… | a`. Промежуточные — оба направления, единственное исключение из лимита трёх корней: северо-восток = `PLACE BIG(=+5) ABOVE(=+3) SIDE(=+3) | o`, юго-запад = `PLACE BIG(=+5) ABOVE(=-3) SIDE(=-3) | o` (без теста). Без «земли» `PLACE ABOVE(=+4)` читается как *top* (0 из 6), с ней — 10 из 10 ([roundtrip_time](../data/translation_test/roundtrip_time.md)).

## Направление движения

У глагола движения (`MOVE`, `GIVE`, `DO`) значение `INSIDE`, `NEAR` или `ABOVE` — где движение кончается. Войти = `MOVE INSIDE(=+5) | i`, выйти = `MOVE INSIDE(=-5) | i`, прибыть = `MOVE NEAR(=+5) | i`, уйти = `MOVE NEAR(=-5) | i`, подняться = `MOVE ABOVE(=+5) | i`, спуститься = `MOVE ABOVE(=-5) | i`; приближаться = `MOVE NEAR(=+5) | i A0` (ещё не пришёл); вернуться = `MOVE SAME(=+5) | i`. Двигать другое — метка `K+3`: вставить = `MOVE INSIDE(=+5) | i K+3`, вынуть, извлечь = `MOVE INSIDE(=-5) | i K+3`, принести = `MOVE NEAR(=+5) | i K+3`, отправить = `MOVE NEAR(=-5) | i K+3`, наполнить = `MOVE INSIDE(=+5) MANY(=+5) | i K+3`, опустошить = `MOVE INSIDE(=-5) MANY(=+5) | i K+3`, лить = `MOVE ABOVE(=-4) GRAIN(=-3) | i K+3`. Отдельная метка «откуда / куда» не нужна: с ней и без неё 18 из 24 ([roundtrip_direction](../data/translation_test/roundtrip_direction.md)).

## Размер, группы, части

- *small* = только `BIG(=-3)`, без `PART` ([roundtrip_words_isolated](../data/translation_test/roundtrip_words_isolated.md)).
- Ось `PART`: крошка −5, часть / член −2, целое / «полностью» +2, группа +5 ([roundtrip_part_ladder](../data/translation_test/roundtrip_part_ladder.md), [roundtrip_part_groups](../data/translation_test/roundtrip_part_groups.md)).
- *society* = `SOMEONE PART(=+5)`, *member* = `SOMEONE PART(=-2)`, *set / union* = `PART(=+5)`, *herd* = `THING(=0) PART(=+5)`; не `MANY SAME` и не `PART SOMEONE MANY`. `PART(=+5)` ставить сразу после главного слова, не первым.

## Изменение, власть, особенное

([roundtrip_new_axes](../data/translation_test/roundtrip_new_axes.md), 38 из 54)

- Изменение — корень `CHANGE` (−5 остаться … +5 превратить); направление через `BIG` и `GOOD`: *grow* = `CHANGE BIG(=+3) | i`, *improve* = `CHANGE GOOD(=+3) | i`, *remain* = `CHANGE(=-4) | i`.
- Власть и учреждение — ось `RULE` (−5 личное … +5 официальное): *authority* = `RULE(=+4) | o`, *official* = `RULE(=+5) | a`, *private* = `RULE(=-5) | a`. Слабые значения около 0 ничего не несут.
- Организационные типы (*committee, commission, agency, union, party, institution*) корнями не различаются: код `SOMEONE PART(=+5) RULE(=+4) | o` читается как «официальная группа». Словарь `@NN` не вводим, потеря принята.
- Особое и общее — ось `SAME` (корень `PARTICULAR` в неё влит, [roundtrip_merge](../data/translation_test/roundtrip_merge.md)): *special / unique* = `SAME(=-4) | a`, *especially* = `SAME(=-4) | e I+4`, *individual* = `SAME(=-4) PART(=-2) | a`, *ordinary* = `SAME(=+3) | a`, *general / universal* = `SAME(=+4) MANY(=+5) | a`. Не собираются: *specific* (`SAME(=-4) KNOW(=+5)` → *famous*), *rare* (`MANY(=+1)` → *few*).

## Залог

- Метка `V` ([roundtrip_voice](../data/translation_test/roundtrip_voice.md), 10 из 11): −4 страдательный, 0 само собой, +4 намеренно.
- Деятель при пассиве — частица `PE`: `… V-4 PE X` ([roundtrip_pe](../data/translation_test/roundtrip_pe.md), 6 из 6, предварительно).

## Степень

([roundtrip_degree](../data/translation_test/roundtrip_degree.md), 18 из 24 верно, 2 частично)

- Усилитель и ослабитель — метка `I` на главном слове: *very good* = `GOOD(=+3) | a I+4`, *extremely big* = `BIG(=+3) | a I+5`, *slightly warm* = `HEAT(=+2) | a I-2`, *hardly possible* = `CAN(=+1) | a I-5`, *completely different* = `SAME(=-5) | a I+5`.
- `I0` («довольно, умеренно») может теряться; для слабой степени писать `I+1…+2`.
- Не `BIG(=+5)` как «очень»; не `C` (сравнение).
- *Almost* («почти») метка `I` не передаёт: читается как *quite likely / fairly certain* — принято как допустимая потеря, ничего не вводим.
- Важность — `BIG` + `HAPPEN` («большие последствия»): `BIG(=+3) HAPPEN(=+3) | a` *significant*, `BIG(=+4) HAPPEN(=+4) | a` *important / major*, `BIG(=+5) HAPPEN(=+5) | a` *crucial / momentous* ([roundtrip_importance](../data/translation_test/roundtrip_importance.md), 8–9 из 10). Не `SAME(=-4)` (читается как *special*) и не `GOOD + BIG` (читается как *great / wonderful*, 0 из 10); *vital* через `LIVE` не читается.

## Вещество и орудия

- Ось `GRAIN` — как вещество держится вместе (корень `MATTER` в неё влит, [roundtrip_merge](../data/translation_test/roundtrip_merge.md), 17 из 24): −5 газ, пар, дым … −3 жидкость … 0 сыпучее … +5 цельный кусок. *gas* = `GRAIN(=-5) | o`, *steam* = `GRAIN(=-5) HEAT(=+3) | o`, *liquid* = `GRAIN(=-3) | o`, *water* = `GRAIN(=-3) CONSUME(=+5) LIVE | o`, *sand* = `GRAIN(=0) THING(=-5) | o`, *flour* = `GRAIN(=0) CONSUME(=+5) THING(=0) | o`, *stone* = `GRAIN(=+5) THING(=-5) | o`, *ice* = `GRAIN(=+5) HEAT(=-5) | o`, *melt* = `CHANGE(=+4) GRAIN(=-3) HEAT(=+3) | i`. Мёд (`GRAIN(=-3) CONSUME(=+5) GOOD(=+4)`) читается как вино, сок.
- Орудие — ось `DO` (роль в действии: −5 деятель … 0 действие … +5 орудие), 17 из 24, [roundtrip_merge](../data/translation_test/roundtrip_merge.md): корни описывают действие, `DO(=+5)` делает из него орудие. *knife* = `JOIN(=-4) TOUCH(=+4) DO(=+5) | o`, *saw* = `JOIN(=-4) MOVE(=+2) DO(=+5) | o`, *scissors* = `JOIN(=-4) MANY(=+1) DO(=+5) | o`, *hammer* = `TOUCH(=+5) MOVE(=+4) DO(=+5) | o`, *brush* = `TOUCH(=-3) MOVE DO(=+5) | o`, *pen* = `TEXT DO(=+5) | o`, *thermometer* = `MEASURE HEAT DO(=+5) | o`, *ladder* = `MOVE ABOVE(=+4) DO(=+5) | o`, *key* = `INSIDE(=+4) CAN(=+4) DO(=+5) | o` (1 из 2). Не собираются: ложка (→ *cup*), метла, иголка. Не `THING(=-5)` для орудий: читается как камень. Порядок свободный: `DO(=+5)` первым или последним читается одинаково (20 из 28 в обоих вариантах, [roundtrip_tool_order](../data/translation_test/roundtrip_tool_order.md)).

## Наука, техника, искусство

([roundtrip_art](../data/translation_test/roundtrip_art.md), 29 из 32 верно, ещё 1 запасным)

- Область знания или занятия — корень `ART` (−5 расчёт, техника … +5 творчество, культура): *poetry* = `ART(=+5) SAY | o`, *painting* = `ART(=+5) SEE GRAIN(=-3) | o`, *history* = `ART(=+4) KNOW TIME(=-3) | o`, *physics* = `ART(=-4) GRAIN MOVE | o`, *mathematics* = `ART(=-5) MANY SEE | o`, *engineering* = `ART(=-4) DO THING | o`.
- Человек дела — `SOMEONE ART(=±n) …`: *engineer* = `SOMEONE ART(=-4) DO | o`, *scientist* = `SOMEONE ART(=-4) KNOW | o`, *artist* = `SOMEONE ART(=+5) DO | o`.
- Устройства — `THING(=-5)` и действие: *machine* = `THING(=-5) MOVE DO | o`, *computer* = `THING(=-5) THINK ART(=-5) | o`.
- Не читается: *architecture* (`ART(=0) DO PLACE` → *workshop*; `ART(=+3) PLACE LIVE` → *theater*). Принято как потеря.

## Возраст, музыка, вода, успех

Слепой тест [roundtrip_lacunae2](../data/translation_test/roundtrip_lacunae2.md): 23 из 24 с рецептами, 11 и 13 из 24 без них.

- **Возраст** — `LIVE` с `TIME`, где уровень TIME означает, с какого времени существо живёт:
  - молодой — `LIVE TIME(=-1) | a`;
  - взрослый — `LIVE TIME(=-3) | a`;
  - старый, пожилой — `LIVE TIME(=-5) | a`;
  - молодёжь — `SOMEONE LIVE TIME(=-1) | o N+3`, «молодые люди». В тесте был вариант с `PART(=+5)`, он прочитан верно (2 из 2), но это четыре корня, сверх лимита; трёхкорневой вариант не проверен;
  - возраст — `LIVE TIME MEASURE | o`.

  О вещах пишется без `LIVE`: древний — `TIME(=-5) | a`.
- **Музыка** — звук как искусство. `FEEL(=+3)` отделяет пение от поэзии (`ART(=+5) SAY`). Если писать песню через `TEXT`, она читается как стихи.
  - петь — `SAY ART(=+5) FEEL(=+3) | i`, песня — то же с `| o`;
  - певец — `SOMEONE SAY FEEL(=+3) | o`;
  - музыка — `ART(=+5) SAY THING | o`;
  - мелодия — `ART(=+5) SAY LONG | o`;
  - танцевать — `ART(=+5) MOVE BODY | i`.
- **Вода и рельеф** — `PLACE GRAIN(=-3)`, «место жидкости». Без `PLACE` в начале и без рецепта такой код читается как воздух или небо.
  - море — `PLACE GRAIN(=-3) BIG(=+5) | o`;
  - озеро — `PLACE GRAIN(=-3) BIG(=0) | o`;
  - река — `PLACE GRAIN(=-3) MOVE(=+3) | o`;
  - остров — `PLACE GRAIN(=-3) INSIDE(=+5) | o`;
  - берег — `PLACE GRAIN(=-3) NEAR(=+4) | o`;
  - гора — `PLACE ABOVE(=+5) BIG(=+4) | o`.
- **Успех и победа** — `GOOD` о результате, `HAPPEN(=+5)` означает результат.
  - победить — `FIGHT GOOD(=+4) | i`, проиграть — `FIGHT GOOD(=-4) | i`;
  - победа — `FIGHT GOOD(=+4) HAPPEN(=+5) | o`;
  - успех — `DO GOOD(=+4) HAPPEN(=+5) | o`;
  - потерпеть неудачу — `DO GOOD(=-4) HAPPEN(=+5) | i`;
  - знаменитый — `KNOW MANY(=+5) | a`.

## Право, деньги, еда, транспорт

([roundtrip_lacunae3](../data/translation_test/roundtrip_lacunae3.md): 24 из 24 с рецептами против 17 без них)

- **Право** — `RULE(=+4)` (закон) с `GOOD(=-4)` (нарушение): преступление = `DO GOOD(=-4) RULE(=+4) | o`, преступник = `SOMEONE GOOD(=-4) RULE(=+4) | o`, суд = `PLACE RULE(=+4) THINK(=+5) | o`, судья = `SOMEONE RULE(=+4) THINK(=+5) | o`, тюрьма = `PLACE MOVE(=-5) RULE(=+4) | o`, украсть = `GIVE(=-4) GOOD(=-4) | i`.
- **Деньги** — `VALUE` с `GIVE`, главный корень решает, что отдают: деньги = `VALUE GIVE(=0) | o`, платить = `VALUE GIVE(=+4) | i` (продать — `GIVE(=+3) VALUE | i`), долг = `VALUE GIVE(=+4) TIME(=+3) | o`, богатый = `VALUE MANY(=+5) | a`, бедный = `VALUE MANY(=0) | a`, рынок = `PLACE GIVE(=0) VALUE | o`.
- **Еда** — `CONSUME(=+5)` с родом вещи `THING`: мясо = `CONSUME(=+5) THING(=+4) | o`, овощ = `CONSUME(=+5) THING(=0) | o`, готовить = `HEAT(=+3) CONSUME(=+5) | i`, кухня = `PLACE HEAT(=+3) CONSUME(=+5) | o`, ферма = `PLACE THING(=0) DO | o`, собирать урожай = `GIVE(=-4) THING(=0) PART(=+5) | i`.
- **Транспорт и постройки** — орудие `DO(=+5)` (не «камень» `THING(=-5)`) и `PLACE`: машина = `DO(=+5) MOVE(=+4) | o`, корабль = `DO(=+5) MOVE GRAIN(=-3) | o`, дорога = `PLACE MOVE LONG(=-3) | o`, мост = `PLACE MOVE ABOVE(=+4) | o`, дом = `PLACE INSIDE(=+5) LIVE | o`, комната = `PLACE INSIDE(=+5) PART(=-2) | o`. Учреждения с рецептом пишутся рецептом, не в кавычках.

## Общество, власть, учёба, война

([roundtrip_lacunae4](../data/translation_test/roundtrip_lacunae4.md): 24 из 24 с рецептами против 13 и 19 без них)

- **Общество**: доверять = `THINK(=+5) GOOD(=+4) | i` («решить, что хороший»), друг = `SOMEONE WANT(=+3) JOIN(=+3) | o`, союзник = `SOMEONE FIGHT JOIN(=+4) | o`, лидер = `SOMEONE SIDE(=+5) RULE | o`, соглашение = `THINK(=+5) SAME(=+5) | o`, безопасный = `GOOD(=-4) CAN(=-5) | a` («вред невозможен»).
- **Власть**: король = `SOMEONE RULE(=+5) SEX(=+5) | o` (королева — `SEX(=-5)`), правительство = `SOMEONE RULE(=+5) PART(=+5) | o`, голосовать = `THINK(=+5) MANY(=+5) | i` («решают все»), выборы = `THINK(=+5) MANY(=+5) RULE(=+4) | o`, гражданин = `SOMEONE PART(=-2) RULE(=+4) | o`, город = `PLACE SOMEONE MANY(=+5) | o`.
- **Учёба и кино**: школа = `PLACE KNOW CONSUME(=+5) | o`, ученик = `SOMEONE KNOW CONSUME(=+5) | o`, учитель = `SOMEONE KNOW GIVE(=+4) | o`, университет = `PLACE KNOW ABOVE(=+4) | o`, фильм = `ART(=+5) SEE MOVE | o`, рекламировать = `SAY GIVE(=+3) VALUE | i` («говорить, чтобы продать»).
- **Война**: враг = `SOMEONE WANT(=-4) FIGHT | o`, битва = `FIGHT(=+5) PART(=-2) | o` («часть войны»), ружьё = `DO(=+5) FIGHT(=+5) HEAT(=+5) | o` («огненное орудие боя»), защищать = `DO GOOD(=-4) | i K-4` («не дать навредить»), нападать = `FIGHT(=+4) BEGIN(=-5) | i`.

## Кавычки: категории и члены семейства; здоровье и сон

([roundtrip_quotes_health](../data/translation_test/roundtrip_quotes_health.md): 40 из 40 с правилом и рецептами против 37 и 28 без них; решения «кавычки или корни» у двух кодировщиков совпали в 24 из 24 против 18)

- **Граница кавычек.** Из корней — категории и назначения: орган = `BODY INSIDE(=+5) PART(=-2) | o`, игра = `FIGHT(=-5) | o`, спорт = `FIGHT(=-5) BODY | o`, звезда = `HEAT(=+5) ABOVE(=+5) PART(=-2) | o`, планета = `PLACE ABOVE(=+5) MOVE | o`, спутник = `DO(=+5) ABOVE(=+5) MOVE | o`, компания = `PART(=+5) DO VALUE | o`, чиновник = `SOMEONE RULE(=+4) | o`, железная дорога = `PLACE MOVE LONG(=+5) | o`, вещание = `SAY GIVE(=+3) MANY(=+5) | o`. В кавычках — конкретные члены семейства в международной или латинской форме (`"hepar"` печень, `"ren"` почка, `"Sol"`, `"Luna"`, `"football"`, `"chess"`, `"protein"`) и узкие термины (`"enzyme"`, `"orbit"`, `"Parliament"`). Луна из корней не читается (*horizon*, *sunset*), `"Luna"` — 2 из 2.
- **Здоровье и сон — середина `LIVE`** («жив наполовину»), `GOOD` — какая: спать = `LIVE(=0) GOOD(=+3) | i`, сновидение = `LIVE(=0) SEE ABSTRACT(=+5) | o`, проснуться = `LIVE(=+5) BEGIN(=-4) | i`, усталый = `LIVE(=0) CAN(=-3) | a`, отдыхать = `MOVE(=-5) GOOD(=+3) | i`; больной = `LIVE(=0) GOOD(=-4) | a`, болезнь = `… | o`, пациент = `SOMEONE LIVE(=0) GOOD(=-4) | o`, больница = `PLACE LIVE(=0) GOOD(=-4) | o`, здоровый = `LIVE(=+5) GOOD(=+4) | a`, лечить = `LIVE GOOD(=+4) | i K+3`, врач = `SOMEONE LIVE GOOD(=+4) | o`, лекарство = `DO(=+5) LIVE GOOD(=+4) | o`, умереть = `LIVE(=-5) | i`, рана = `BODY JOIN(=-3) | o`, боль = `BODY FEEL(=+4) GOOD(=-4) | o`. Корень `HEALTH` не нужен.

## Цена, тщательность, присоединение

([roundtrip_value_care_join](../data/translation_test/roundtrip_value_care_join.md))

- Цена — корень `VALUE` (−5 дёшево … +5 дорого): *expensive* = `VALUE(=+4) | a`, *cheap* = `VALUE(=-4) | a`, *price* = `VALUE | o`; 10 из 10. Купить и продать — с `GIVE`: *buy* = `GIVE(=-3) VALUE | i`, *sell* = `GIVE(=+3) VALUE | i`, но декодер может перепутать направление.
- Тщательность — корень `CARE` (−5 небрежно … +5 тщательно): *carefully* = `CARE(=+3) | e`, *carelessly* = `CARE(=-3) | e`, *thoroughly* = `CARE(=+5) PART(=+2) | e`, *hastily* = `CARE(=-5) MOVE(=+4) | e`, *meticulous* = `CARE(=+5) PART(=-4) | a I+4`; 6 из 6.
- Присоединение — корень `JOIN` (−5 отделить … +5 присоединить): *join* = `JOIN(=+3) | i`, *separate* = `JOIN(=-3) PART | i`, *remove* = `JOIN(=-4) | i`; *add / attach / unite* сливаются, *add* не читается.

## Тон

([roundtrip_tone](../data/translation_test/roundtrip_tone.md), 26 из 32 верно, 5 рядом)

- Манера обращения с людьми — корень `TONE` (−5 грубо, холодно, враждебно … +5 вежливо, тепло, искренне): *polite* = `TONE(=+4) | a`, *rude* = `TONE(=-4) | a`, *politely* = `TONE(=+4) | e`, *rudely* = `TONE(=-4) | e`.
- Сочетания: *harsh* = `TONE(=-4) TOUCH(=+4) | a`, *warm* = `TONE(=+4) HEAT(=+2) | a`, *cold* = `TONE(=-4) HEAT(=-3) | a`, *hostile* = `TONE(=-5) FIGHT | a`, *friendly* = `TONE(=+4) WANT(=+3) | a`, *tactful* = `TONE(=+3) CARE(=+5) | a`, *blunt* = `TONE(=-2) CARE(=-3) | a`.
- *Kind, courteous, tactful, considerate* путаются между собой, *sincere* читается не всегда.

## Приём и выдача

([roundtrip_consume](../data/translation_test/roundtrip_consume.md), 26 из 32 верно)

- Ось `CONSUME`: −5 выделить, выбросить … +5 поглотить, принять. Канал задаёт второй корень: *eat* = `CONSUME(=+5) GRAIN(=+3) | i`, *drink* = `CONSUME(=+5) GRAIN(=-3) | i`, *inhale* = `CONSUME(=+5) GRAIN(=-5) | i`, *exhale* = `CONSUME(=-5) GRAIN(=-5) | i`, *excrete* = `CONSUME(=-5) BODY | i`, *vomit* = `CONSUME(=-5) BODY ABOVE(=+3) | i`.
- Речь и слух: *speak* = `CONSUME(=-5) SAY | i`, *listen* = `CONSUME(=+5) SAY CARE(=+3) | i`.
- Письменная речь — корень `TEXT` (без оси; `SAY` — устная), [roundtrip_candidates](../data/translation_test/roundtrip_candidates.md), 3 → 15 точных из 24: *write* = `TEXT | i`, *read* = `CONSUME(=+5) TEXT | i`, *writer* = `SOMEONE TEXT | o`, *author* = `SOMEONE TEXT HAPPEN(=-4) | o`, *book* = `TEXT PART(=+2) | o`, *letter* = `TEXT GIVE(=+3) SOMEONE | o`, *newspaper* = `TEXT TIME(=0) PART(=+5) | o`, *library* = `PLACE TEXT PART(=+5) | o`. Прежние `CONSUME(=-5) SEE` (→ *show*) и `CONSUME(=+5) SEE` (→ *watch*) не читались.

## Побуждение

([roundtrip_causative](../data/translation_test/roundtrip_causative.md), 25 из 32 верно, ещё 3 запасным)

- Метка `K` на глаголе: подлежащее воздействует на дополнение `E`, чтобы оно совершило или претерпело действие. `K-5` запретить, `K-4` помешать, `K-2` отговорить, `K0` разрешить, `K+3` сделать / убедить, `K+4` заставить, `K+5` принудить.
- Что именно вызывается, задаёт корень глагола: *make* = `DO | i K+3`, *prevent* = `DO | i K-4`, *feed* = `CONSUME | i K+4`, *teach* = `KNOW | i K+4`, *frighten* = `FEEL(=+4) GOOD(=-4) | i K+4`, *force* = `DO WANT(=-5) | i K+5`, *persuade* = `SAY THINK(=+5) | i K+3`, *allow* = `RULE(=+3) | i K0`, *forbid* = `RULE(=+4) DO | i K-5`.
- *Induce / encourage* (`K+2…3`) путаются с *have / get / entice*.

## Конкретное и абстрактное

([roundtrip_abstract](../data/translation_test/roundtrip_abstract.md), 25 из 32 верно)

- Ось `ABSTRACT`: −5 физическое, осязаемое … +5 умственное, отвлечённое. Она не про область (это `ART`), а про осязаемость.
- Прилагательные: *concrete* = `ABSTRACT(=-5) | a`, *abstract* = `ABSTRACT(=+5) | a`, *tangible* = `TOUCH CAN ABSTRACT(=-5) | a`, *theoretical* = `KNOW ABSTRACT(=+5) | a` (путается с *speculative*).
- Мысль: *idea* = `THINK ABSTRACT(=+5) | o`, *principle* = `RULE ABSTRACT(=+5) | o`, *imply* = `SAY ABSTRACT(=+5) | i`, *assume / suppose* = `THINK(=+3) | i M-1` (между собой сливаются).
- Физическое действие: *shake* = `MOVE(=+2) ABSTRACT(=-5) | i`, *tumble* = `MOVE ABOVE(=-4) CARE(=-4) | i`, *kick* = `TOUCH(=+4) MOVE(=+4) ABSTRACT(=-5) | i` (путается с *hit*).
- Не различаются: *theory / concept / philosophy*, *belief / knowledge*, *rattle / rumble*.

## Рецепты понятий (два слепных теста: [roundtrip_and_mod](../data/translation_test/roundtrip_and_mod.md), раунд 2)

- Работают: *game* — теперь `FIGHT(=-5) | o` (ось у `FIGHT` появилась, см. «Эмоции, бой»; прежний `FIGHT ART(=+2) | o` тоже читался); *independent* — `SOMEONE(=+5) CAN(=+5) JOIN(=-5) | a` (2/2); *help* — `DO GOOD(=+3) | i`; *exception* — `SAME(=-4) JOIN(=-5) RULE | o` (2/2 в [roundtrip_merge](../data/translation_test/roundtrip_merge.md)); *equality* — `SAME(=+5) ABSTRACT(=+3) | o`; *economic* — `VALUE GIVE(=0) | a` (1/2).
- **Меры и отношения — корень `MEASURE`** (ось: −5 величина сама по себе … +5 величина относительно другой; введён после двух провалов с `PART`/`BIG`/`SAME`; слепой тест v2 26 из 32, [roundtrip_measure](../data/translation_test/roundtrip_measure.md)): *ratio* `MEASURE(=+5) | o`, *percentage* `MEASURE(=+5) PART(=-2) | o`, *rate* `MEASURE(=+5) TIME | o`, *amount* `MEASURE(=-5) | o`, *size* `MEASURE(=-5) BIG | o`, *degree, level* `MEASURE(=0) | o`, *average* `MEASURE(=+5) MANY SAME | o`, *measurement* и *to measure* `MEASURE DO | o` / `MEASURE | i`, *unit* `MEASURE SAME | o`. Слабо: *meter, dimension, proportional* (читаются *distance/area/fractional*).
- Не работают (по две серии рецептов, ни один не прочитан верно): *way/method*, *measurement* как *act of measuring* (теперь `MEASURE(=-5)`, но читается *meter / unit*), *a sort of X* (`I-2` на имени не читается как «вид»; *a sort of bird* → *bird*). `RULE(=-5)`/`SAME(=-5) RULE` для «независимый» читается как *illegal*.
