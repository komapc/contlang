# Как кодировать: приёмы

Приёмы подобраны слепыми тестами (кодировщик видит только спецификацию). Для каждого дана ссылка на тест; **без теста** — подсказка не проверена. Корни и оси — в [lexicon.md](lexicon.md), метки и частицы — в [syntax.md](syntax.md), модель — в [model.md](model.md). Используется скиллом `mincode` (`.claude/skills/mincode/SKILL.md`).

## Общее

- Действия без своего корня — через `DO-i E …` (делать, вызывать) или `SAY-i …` (говорить, просить) ([roundtrip_30](../data/translation_test/roundtrip_30.md)).
- «Мочь, трудно, возможно» — `CAN` (`DO CAN(=-3) | a` — *difficult*); `MAYBE` вместо `CAN` не использовать.
- **Термины в кавычках.** Названия институтов и должностей (*parliament, president, official, company*), химические вещества и минералы (*sulfur dioxide, silicate*), технические и научные термины без корня (*railway, bellows, furnace, tephra, gluten*) пишутся в кавычках как есть, а не собираются из корней. В тесте на 60 предложениях ([roundtrip_wiki_new4](../data/translation_test/roundtrip_wiki_new4.md)) предложения с такими кавычками получили 2,35 из 3, остальные 1,85; собранные из корней термины читались как *price controls* (вместо *company*), *mechanical parts* (вместо *furnace*), *the authorities* (вместо *Parliament*). Обычные слова (*water, house, food*) в кавычки не ставить.
- Количество — `MANY` (ноль — ни одного, +5 — все), точные числа цифрами в кавычках.
- `ABOVE`, `INSIDE`, `BIG` — только настоящие «верх / внутри / размер»; метафора (*roof, coffee, desk*) и усилитель (`BIG(=+5)` как «очень») почти всегда читаются неверно ([roundtrip_200](../data/translation_test/roundtrip_200.md)).
- Не злоупотреблять `ABOVE` для «важного»: *elect* через `ABOVE(=+4)` читается как *worship*.
- Еда и питьё — `CONSUME`, ёмкость — `CONTAINER`; корней HEAR, KIND, WORD, PEOPLE больше нет (PEOPLE = `SOMEONE MANY(=+4) | o`).

## Связки: и, также, поэтому

- «И, также, ещё» — частица `AND` между сочиняемым: `X AND Y`, `[ … ] AND [ … ]`, в перечислении перед последним элементом; `JOIN`, `CHANGE`, `SAME` как связки не использовать (декодеры читали их буквально: *joined, changed*; [roundtrip_wiki4](../data/translation_test/roundtrip_wiki4.md)). Проверено ([roundtrip_wiki_new4](../data/translation_test/roundtrip_wiki_new4.md)): `AND` в 39 кодах из 60, декодеры читают её как *and / also* (54 раза), буквальных «joined» 2 вместо 8.
- **`AND` с модификаторами** (слепой тест, 2 кодировщика × 2 декодера, 11 предложений; [roundtrip_and_mod](../data/translation_test/roundtrip_and_mod.md)): оси берутся у самой частицы, порядок слов исходный. `AND SAME(=-5)` — *но, а, тогда как* (4/4 верно); `AND SAME(=-2)` — *хотя* (4/4); `AND HAPPEN(=+4)` — *поэтому, так что* (2/2); `AND HAPPEN(=-4)` — *потому что* (2/2); `AND BIG(=+4)` — *тем более, не говоря уже* (*let alone* 2/2, *what is more* читается как простое *and* + усиление); `AND MAYBE(=-3)` — *или* (2/2). `LA` остаётся для *если / когда*.

## Против, причина, решение

- «Против» (*protest, refuse*) — через явного носителя: `SOMEONE MANY(=+4) SAY WANT(=-5) | o`; голое `WANT(=-5)` декодер часто игнорирует.
- Причина и следствие как предметы — ось `HAPPEN` (`HAPPEN(=-4) | o` причина, `HAPPEN(=+4) | o` следствие). «Потому что / поэтому / так как» между клаузами — `LA [ причина ] следствие` (причина стоит первой, порядок слов меняют) **без теста**.
- Решение — ось `THINK` (`THINK(=+5) | i` решить, `THINK(=-4) | i` сомневаться).

## Люди и предметы

- Местоимения — ось `SOMEONE` (я +5, ты +3, он −3), множественное через `MANY`: `SOMEONE(=+5) MANY(=+3) | o` — *we*.
- Одушевлённость — ось `THING` (камень −5, растение 0, животное +4); скорость — `MOVE`, возбуждение — `FEEL`; приятно или нет — `GOOD`.
- *grandfather, old man* = `SOMEONE SEX(=+5) TIME(=-4) LIVE(=+3) | o` («живой предок»; `TIME(=-4)` один даёт *ancestor*). **Без теста.**

## Эмоции, бой

- Закон и власть — `RULE`, бой и война — `FIGHT` (*peace* = `FIGHT MANY(=0) | o`).
- Эмоции: `FEEL` (возбуждение) + `GOOD` (приятность) + корень по смыслу: страх `TIME(+3)` (плохое впереди), злость `FIGHT | a`, социальные `SOMEONE | o` (+ `SEE | i`); оси `NEAR` и `WANT` для направления не работают.

## Время

- `TIME(=+1)` читается как *soon*; для «потом» его не использовать.
- *later, subsequent, earlier, before, after, initially* — метка `R`, не `TIME(=±n)` ([roundtrip_reltime](../data/translation_test/roundtrip_reltime.md)).

## Размер, группы, части

- *small* = только `BIG(=-3)`, без `PART` ([roundtrip_words_isolated](../data/translation_test/roundtrip_words_isolated.md)).
- Ось `PART`: крошка −5, часть / член −2, целое / «полностью» +2, группа +5 ([roundtrip_part_ladder](../data/translation_test/roundtrip_part_ladder.md), [roundtrip_part_groups](../data/translation_test/roundtrip_part_groups.md)).
- *society* = `SOMEONE PART(=+5)`, *member* = `SOMEONE PART(=-2)`, *set / union* = `PART(=+5)`, *herd* = `THING(=0) PART(=+5)`; не `MANY SAME` и не `PART SOMEONE MANY`. `PART(=+5)` ставить сразу после главного слова, не первым.

## Изменение, власть, особенное

([roundtrip_new_axes](../data/translation_test/roundtrip_new_axes.md), 38 из 54)

- Изменение — корень `CHANGE` (−5 остаться … +5 превратить); направление через `BIG` и `GOOD`: *grow* = `CHANGE BIG(=+3) | i`, *improve* = `CHANGE GOOD(=+3) | i`, *remain* = `CHANGE(=-4) | i`.
- Власть и учреждение — ось `RULE` (−5 личное … +5 официальное): *authority* = `RULE(=+4) | o`, *official* = `RULE(=+5) | a`, *private* = `RULE(=-5) | a`. Слабые значения около 0 ничего не несут.
- Организационные типы (*committee, commission, agency, union, party, institution*) корнями не различаются: код `SOMEONE PART(=+5) RULE(=+4) | o` читается как «официальная группа». Словарь `@NN` не вводим, потеря принята.
- *specific / particular / special* = `PARTICULAR(=+3…+4)`, *general* = `PARTICULAR(=-4)`, *unique* = `PARTICULAR(=+5) SAME(=-5)`. Оттенки внутри кластера не различаются.

## Залог

- Метка `V` ([roundtrip_voice](../data/translation_test/roundtrip_voice.md), 10 из 11): −4 страдательный, 0 само собой, +4 намеренно.
- Деятель при пассиве — частица `PE`: `… V-4 PE X` ([roundtrip_pe](../data/translation_test/roundtrip_pe.md), 6 из 6, предварительно).

## Степень

([roundtrip_degree](../data/translation_test/roundtrip_degree.md), 18 из 24 верно, 2 частично)

- Усилитель и ослабитель — метка `I` на главном слове: *very good* = `GOOD(=+3) | a I+4`, *extremely big* = `BIG(=+3) | a I+5`, *slightly warm* = `HEAT(=+2) | a I-2`, *hardly possible* = `CAN(=+1) | a I-5`, *completely different* = `SAME(=-5) | a I+5`.
- `I0` («довольно, умеренно») может теряться; для слабой степени писать `I+1…+2`.
- Не `BIG(=+5)` как «очень»; не `C` (сравнение).
- *Almost* («почти») метка `I` не передаёт: читается как *quite likely / fairly certain* — принято как допустимая потеря, ничего не вводим.
- Важность — `BIG` + `HAPPEN` («большие последствия»): `BIG(=+3) HAPPEN(=+3) | a` *significant*, `BIG(=+4) HAPPEN(=+4) | a` *important / major*, `BIG(=+5) HAPPEN(=+5) | a` *crucial / momentous* ([roundtrip_importance](../data/translation_test/roundtrip_importance.md), 8–9 из 10). Не `PARTICULAR` (читается как *special*) и не `GOOD + BIG` (читается как *great / wonderful*, 0 из 10); *vital* через `LIVE` не читается.

## Наука, техника, искусство

([roundtrip_art](../data/translation_test/roundtrip_art.md), 29 из 32 верно, ещё 1 запасным)

- Область знания или занятия — корень `ART` (−5 расчёт, техника … +5 творчество, культура): *poetry* = `ART(=+5) SAY | o`, *painting* = `ART(=+5) SEE MATTER(=0) | o`, *history* = `ART(=+4) KNOW TIME(=-3) | o`, *physics* = `ART(=-4) MATTER MOVE | o`, *mathematics* = `ART(=-5) MANY SEE | o`, *engineering* = `ART(=-4) DO THING | o`.
- Человек дела — `SOMEONE ART(=±n) …`: *engineer* = `SOMEONE ART(=-4) DO | o`, *scientist* = `SOMEONE ART(=-4) KNOW | o`, *artist* = `SOMEONE ART(=+5) DO | o`.
- Устройства — `THING(=-5)` и действие: *machine* = `THING(=-5) MOVE DO | o`, *computer* = `THING(=-5) THINK ART(=-5) | o`.
- Не читается: *architecture* (`ART(=0) DO PLACE` → *workshop*; `ART(=+3) PLACE LIVE` → *theater*). Принято как потеря.

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

- Ось `CONSUME`: −5 выделить, выбросить … +5 поглотить, принять. Канал задаёт второй корень: *eat* = `CONSUME(=+5) MATTER(=-5) | i`, *drink* = `CONSUME(=+5) MATTER(=0) | i`, *inhale* = `CONSUME(=+5) MATTER(=+5) | i`, *exhale* = `CONSUME(=-5) MATTER(=+5) | i`, *excrete* = `CONSUME(=-5) BODY | i`, *vomit* = `CONSUME(=-5) BODY ABOVE(=+3) | i`.
- Речь и слух: *speak* = `CONSUME(=-5) SAY | i`, *listen* = `CONSUME(=+5) SAY CARE(=+3) | i`.
- Не читается: *write* (`CONSUME(=-5) SEE` → *show*), *read* (`CONSUME(=+5) SEE` → *watch*, у одного декодера верно). Принято как потеря.

## Побуждение

([roundtrip_causative](../data/translation_test/roundtrip_causative.md), 25 из 32 верно, ещё 3 запасным)

- Метка `K` на глаголе: подлежащее воздействует на дополнение `E`, чтобы оно совершило или претерпело действие. `K-5` запретить, `K-4` помешать, `K-2` отговорить, `K0` разрешить, `K+3` сделать / убедить, `K+4` заставить, `K+5` принудить.
- Что именно вызывается, задаёт корень глагола: *make / prevent* = `DO | i K+3 / K-4`, *feed* = `CONSUME | i K+4`, *teach* = `KNOW | i K+4`, *frighten* = `FEEL(=+4) GOOD(=-4) | i K+4`, *force* = `DO WANT(=-5) | i K+5`, *persuade* = `SAY THINK(=+5) | i K+3`, *allow* = `RULE(=+3) | i K0`, *forbid* = `RULE(=+4) DO | i K-5`.
- *Induce / encourage* (`K+2…3`) путаются с *have / get / entice*.

## Конкретное и абстрактное

([roundtrip_abstract](../data/translation_test/roundtrip_abstract.md), 25 из 32 верно)

- Ось `ABSTRACT`: −5 физическое, осязаемое … +5 умственное, отвлечённое. Она не про область (это `ART`), а про осязаемость.
- Прилагательные: *concrete* = `ABSTRACT(=-5) | a`, *abstract* = `ABSTRACT(=+5) | a`, *tangible* = `TOUCH CAN ABSTRACT(=-5) | a`, *theoretical* = `KNOW ABSTRACT(=+5) | a` (путается с *speculative*).
- Мысль: *idea* = `THINK ABSTRACT(=+5) | o`, *principle* = `RULE ABSTRACT(=+5) | o`, *imply* = `SAY ABSTRACT(=+5) | i`, *assume / suppose* = `THINK(=+3) MAYBE(=-1) | i` (между собой сливаются).
- Физическое действие: *shake* = `MOVE(=+2) ABSTRACT(=-5) | i`, *tumble* = `MOVE ABOVE(=-4) CARE(=-4) | i`, *kick* = `TOUCH(=+4) MOVE(=+4) ABSTRACT(=-5) | i` (путается с *hit*).
- Не различаются: *theory / concept / philosophy*, *belief / knowledge*, *rattle / rumble*.

## Рецепты понятий (два слепных теста: [roundtrip_and_mod](../data/translation_test/roundtrip_and_mod.md), раунд 2)

- Работают: *game* — `FIGHT(=-4) ART(=+2) | o` (sport/game, оба раунда); *independent* — `SOMEONE(=+5) CAN(=+5) JOIN(=-5) | a` (2/2); *help* — `DO GOOD(=+3) | i`; *exception* — `PARTICULAR(=+4) JOIN(=-5) RULE | o`; *equality* — `SAME(=+5) ABSTRACT(=+3) | o`; *economic* — `VALUE GIVE(=0) | a` (1/2).
- Не работают (по две серии рецептов, ни один не прочитан верно): *way/method*, *role*, *measurement*, *ratio/proportion* (`PART BIG(=0) SAME | o` даёт *half/share*, близко, но не то), *a sort of X* (`I-2` на имени не читается как «вид»; *a sort of bird* → *bird*). `RULE(=-5)`/`SAME(=-5) RULE` для «независимый» читается как *illegal*.
