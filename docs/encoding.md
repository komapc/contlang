# Как кодировать: приёмы

Приёмы подобраны слепыми тестами (кодировщик видит только спецификацию). Для каждого дана ссылка на тест; **без теста** — подсказка не проверена. Корни и оси — в [lexicon.md](lexicon.md), метки и частицы — в [syntax.md](syntax.md), модель — в [model.md](model.md). Используется скиллом `mincode` (`.claude/skills/mincode/SKILL.md`).

## Общее

- Действия без своего корня — через `DO-i E …` (делать, вызывать) или `SAY-i …` (говорить, просить) ([roundtrip_30](../data/translation_test/roundtrip_30.md)).
- «Мочь, трудно, возможно» — `CAN` (`DO CAN(=-3) | a` — *difficult*); `MAYBE` вместо `CAN` не использовать.
- Количество — `MANY` (ноль — ни одного, +5 — все), точные числа цифрами в кавычках.
- `ABOVE`, `INSIDE`, `BIG` — только настоящие «верх / внутри / размер»; метафора (*roof, coffee, desk*) и усилитель (`BIG(=+5)` как «очень») почти всегда читаются неверно ([roundtrip_200](../data/translation_test/roundtrip_200.md)).
- Не злоупотреблять `ABOVE` для «важного»: *elect* через `ABOVE(=+4)` читается как *worship*.
- Еда и питьё — `CONSUME`, ёмкость — `CONTAINER`; корней HEAR, KIND, WORD, PEOPLE больше нет (PEOPLE = `SOMEONE MANY(=+4) | o`).

## Против, причина, решение

- «Против» (*protest, refuse*) — через явного носителя: `SOMEONE MANY(=+4) SAY WANT(=-5) | o`; голое `WANT(=-5)` декодер часто игнорирует.
- Причина и следствие — ось `HAPPEN` (`HAPPEN(=-4) | o` причина, `HAPPEN(=+4) | o` следствие, `HAPPEN(=-4) | e` потому что).
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
- *Almost* («почти») метка `I` не передаёт; *important* корнем не выражается (читается как *special*).
