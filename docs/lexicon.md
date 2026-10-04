# Словарь

Фиксированного словаря нет: слова порождаются как **корень + суффикс + признаки** ([синтаксис](syntax.md)). Ниже — рабочая схема, полученная экспериментами на английском (ConceptNet Numberbatch, 3000 слов; метрики и сравнения в [плане](plan.md)). Всё здесь **рабочая гипотеза**, а не окончательный словарь.

## Структура кода слова

Слово = корень + суффикс (2 бита) + до трёх корней-модификаторов (и `ABSTRACT` сверх лимита, если слово абстрактное), у каждого корня своя ось (−5…+5) или никакой ([модель](model.md)). Общих осей нет: оттенок задаёт ещё один корень. Всё, что ниже раздела «Корни: текущий список», — исторический материал (автоподбор корней, глобальные оси, послабления до модели «всё в корнях»), он сохранён для истории и не описывает текущий язык.

## Корни: текущий список (черновик, 46)

Правило: у каждого корня **своя** ось (одна) или никакой; составные слова из двух-трёх корней, как в эсперанто (главное первым, остальные уточняют; см. [модель](model.md)). Корни берутся из NSM; автоматически подобранные слова корнями не берутся (проверено: выигрыш по wup ≤ 0,01, корни нечитаемы, набор нестабилен, см. `data/roots_optimization.md`).

**С осью (37):**

| корень | ось (−5 … +5) | статус |
| :-- | :-- | :-- |
| GOOD | плохо … хорошо | принято |
| BIG | мало … много | принято |
| NEAR | далеко … близко (в том числе «этот / тот») | принято |
| ABOVE | ниже … выше | принято |
| LIVE | мёртвое … живое | принято |
| SAME | другое … то же | принято |
| MAYBE | нет … точно (шкала вероятности из [синтаксиса](syntax.md)) | принято |
| TIME | раньше … позже | принято |
| INSIDE | снаружи … внутри | принято (данные: полюса в одной семье) |
| PART | лестница: частица … часть … целое … группа (−5 крошка, −2 часть / член, +2 целое / «полностью», +5 группа, набор, союз); после главного слова `PART(=+5)` — собрание таких вещей, как *-aro* в эсперанто: `SOMEONE PART(=+5) \| o` общество, `THING(=0) PART(=+5) \| o` стадо / роща; `SOMEONE PART(=-2) \| o` член | принято, слепой тест 10 из 10 (`data/translation_test/roundtrip_part_ladder.md`) |
| SIDE | зад … перёд | принято |
| KNOW | не знаю … знаю | принято |
| WANT | не хочу … хочу (ненависть … любовь) | принято |
| HEAT | холодно … жарко (−5 лёд, 0 тепло/комнатная, +5 огонь) | **новое**, принято |
| BEGIN | начало … конец (−5 начать, 0 идёт / середина, +5 закончить): `BEGIN(=-5) \| i` начинать, `BEGIN(=+5) \| i` заканчивать, `BEGIN(=-4) \| a` первый, `BEGIN(=+4) \| a` последний | **новое**, принято |
| GIVE | взять … отдать (−5 взять / украсть, 0 обмен, +5 отдать / подарить): `GIVE(=-5) \| i` брать, `GIVE(=+5) \| i` давать, `GIVE(=-5) GOOD(=-4) \| i` красть, `GIVE(=-3) TIME(=+3) \| i` брать взаймы | **новое**, принято (MOVE + INSIDE не работает, `data/translation_test/roundtrip_200.md`) |
| TOUCH | мягкое … твёрдое (−5 мягкое / нежное, 0 обычное, +5 твёрдое / острое): `TOUCH(=-4) \| a` мягкий, `TOUCH(=+5) \| a` твёрдый | **новое**, принято (тест: sharp, concrete, board перепутаны без оси) |
| MATTER | твёрдое … жидкое … газ (−5 твёрдое, 0 жидкое, +5 газ): `MATTER(=0) \| o` жидкость, `MATTER(=+5) \| o` газ | **новое**, принято (анализ ниже: классы разделены в четыре σ) |
| SEX | женское … мужское | **новое**, предложено |
| HAPPEN | причина … следствие (−5 первопричина, 0 просто событие, +5 результат): `HAPPEN(=+4) \| o` следствие, `HAPPEN(=-4) \| o` причина, `HAPPEN(=+4) \| e` следовательно, `HAPPEN(=-4) \| e` потому что | **новое**, принято (слепой тест: 6 из 6) |
| THINK | сомневаться … решить (−5 сомневаться, 0 думать, +5 решить): `THINK(=+5) \| i` решить / выбрать, `THINK(=+5) \| o` решение | **предложено**, слепой тест 5 из 6; отдельного корня «выбрать» не нужно |
| CAN | не могу … могу (−5 невозможно, −3 трудно, +4 легко); из NSM, нужен для «трудно / возможно» | **новое**, принято (BECAUSE отвергнут) |
| MANY | **односторонняя** 0 … +5: ни одного … единицы … многие … все | **новое**, пробуем; «один» и точные числа — числа из послаблений |
| SOMEONE | лицо (−5 они / другой, 0 кто-то, +3 ты, +5 я): `SOMEONE(=+5) \| o` я, `SOMEONE(=+3) \| o` ты, `SOMEONE(=-3) \| o` он; множественное — `MANY` вторым корнем: `SOMEONE(=+5) MANY(=+3) \| o` мы | **новое**, принято (слепой тест: 8 из 8 местоимений) |
| THING | одушевлённость (−5 камень … 0 растение … +4 животное; человек — SOMEONE): `THING(=-5) \| o` камень, `THING(=+4) BIG(=+5) \| o` слон | **новое**, принято (тест: камень, насекомое, животное, слон верно; растения слабо) |
| MOVE | стоять … быстро (−5 стоять, 0 идти, +5 мчаться): `MOVE(=+4) \| i` бежать, `MOVE(=+4) \| e` быстро | **новое**, принято (тест: 6 из 8 слово или синоним) |
| RULE | личное … официальное (−5 личное, неформальное, частное; 0 обычное; +5 официальное, учреждение, закон): `RULE(=+4) \| o` власть, учреждение, `SOMEONE PART(=+5) RULE(=+4) \| o` комитет, ведомство | **новое**, предложено (SemAxis: комитет +0,53, комиссия, ведомство; оси почти не пересекается с другими, |cos| ≤ 0,12) |
| CHANGE | остаться … измениться (−5 остаться, не меняться, 0 меняться, +5 превратить, измениться полностью): `CHANGE \| i` менять, `CHANGE(=-4) \| i` оставаться, `CHANGE BIG(=+3) \| i` расти, `CHANGE GOOD(=+3) \| i` улучшать | **новое**, предложено (SemAxis: alter, transform, modify, shift; направление увеличить/уменьшить даётся осями `BIG` и `GOOD`) |
| PARTICULAR | общее … особое (−5 общее, универсальное, 0 обычное, +5 особое, единственное, конкретное): `PARTICULAR(=+4) \| a` особый, конкретный, `PARTICULAR(=-4) \| a` общий | **новое**, предложено, проверить слепым тестом (SemAxis: unique, peculiar, particular, specific) |
| ART | техника … творчество (−5 расчёт, техника, устройства, точные науки, 0 смешанное, +5 творчество, культура, гуманитарное): `ART(=-4) KNOW \| o` физика, `ART(=+5) SAY \| o` поэзия, `ART(=-5) SOMEONE \| o` инженер; корень без значения — умение, ремесло, дисциплина | **новое**, предложено (SemAxis: полюса «гуманитарное + искусство» против «точные науки + техника», LOO 1.00, оси покрывают 10 %); принято (слепой тест: 29 из 32, мимо только *architecture*) |
| JOIN | отделить … присоединить (−5 отделить, убрать, уйти, вычесть, 0 состав не меняется, +5 присоединить, добавить, привнести, объединить): `JOIN(=+4) \| i` присоединять, `JOIN(=-4) \| i` убирать | **новое**, предложено (SemAxis: полюса join/add/attach против separate/remove/detach, LOO 1.00; ближайшие оси GIVE +0.3, NEAR +0.2); принято с оговоркой (слепой тест: ~8 из 10; *add* не читается, внутри кластера слова сливаются) |
| VALUE | дёшево … дорого (−5 дёшево, бесполезно, ничего не стоит, 0 обычная цена, +5 дорого, ценно, драгоценно): `VALUE(=+4) \| a` дорогой, ценный, `VALUE(=-4) \| a` дешёвый; покупка и продажа — вместе с `GIVE` | **новое**, предложено (SemAxis: полюса cheap/worthless/useless против expensive/valuable/precious, LOO 0.91); принято (слепой тест: 10 из 10 на прилагательных; *buy/sell* путаются по знаку `GIVE`) |
| CARE | небрежно … тщательно (−5 небрежно, наспех, 0 обычно, +5 тщательно, осторожно, методично): `CARE(=+4) \| e` тщательно, `CARE(=-4) \| e` небрежно, наспех | **новое**, предложено (SemAxis: carefully/meticulously против carelessly/hastily, LOO 0.92); принято (слепой тест: 6 из 6, 12 из 12 с осью на `DO`) |
| TONE | грубо … вежливо (−5 грубо, холодно, враждебно, резко, 0 нейтрально, +5 вежливо, тепло, дружелюбно, искренне): `TONE(=+4) \| a` вежливый, `TONE(=-4) \| a` грубый, `TONE(=+4) \| e` вежливо | **новое**, предложено (SemAxis: polite/kind/warm против rude/harsh/cold, LOO 1.00; ближайшие оси TOUCH −0.4, GOOD +0.3); принято (слепой тест: 26 из 32, ещё 5 рядом; *kind / courteous / tactful* сливаются) |
| CONSUME | выделить … поглотить (−5 выделить, выбросить, излить, 0 обмен, +5 поглотить, принять внутрь: есть, пить, читать, слушать; −5 выделять: испражняться, писать, говорить, излучать): `CONSUME(=+4) \| i` поглощать, есть, `CONSUME(=-4) \| i` выделять; канал задаёт второй корень: `CONSUME(=+4) SEE \| i` читать, `CONSUME(=-4) SAY \| i` говорить | **новое**, предложено пользователем (приём ↔ выдача: есть / испражняться, читать / писать, слушать / говорить); принято (слепой тест: 26 из 32; еда, дыхание, речь читаются, *read / write* нет) |
| ABSTRACT | конкретное … абстрактное (−5 вещественное, физическое, осязаемое: дом, пинать, трясти, 0 смешанное, +5 отвлечённое, умственное: теория, принцип, предполагать, подразумевать): `ABSTRACT(=-4) \| o` вещь, предмет, `ABSTRACT(=+4) \| o` понятие, `ABSTRACT(=+4) THINK \| i` предполагать; конкретный / абстрактный как признак — `\| a` | **новое**, предложено остаточным PCA по частям речи (у глаголов, существительных, прилагательных, наречий; SemAxis: idea/theory/concept/principle против house/stone/hand/door/kick, косинус с ART +0,05, максимум с остальными осями 0,16); принято (слепой тест: 25 из 32, знак не перепутан ни разу, промахи — соседи: *theory / concept, kick / hit*) |
| MEASURE | величина сама по себе … относительно другой (−5 величина как есть: размер, количество, длина, число, 0 уровень, степень, +5 величина относительно другой: отношение, доля, пропорция, процент, скорость-как-отношение, среднее): `MEASURE(=-5) \| o` количество, размер, `MEASURE(=+5) \| o` отношение, `MEASURE \| i` измерять, единица — `MEASURE SAME \| o` | **новое**, введено по правилу (*ratio / proportion / measurement* дважды не читались через `PART`, `BIG`, `SAME`, `SEE`); первая версия оси (единица … количество … отношение) была смесью трёх понятий, переписана; ось независима (SemAxis, максимум косинуса с BIG −0,18); слепой тест v2 26 из 32 — см. [roundtrip_measure](../data/translation_test/roundtrip_measure.md) |
| LONG | тонкое гибкое … толстое жёсткое длинное (−5 нить, верёвка, волос, проволока, 0 палочка, прут, ветка, +5 столб, бревно, балка, шест): `LONG(=-5) \| o` нить, `LONG(=+4) \| o` шест, `LONG \| a` длинный, высокий, `LONG(=+3) PLACE \| o` башня | **новое**, по просьбе автора (аналог *palisa* / *linja* в Toki Pona: длинный предмет); ось независима (SemAxis, косинус с ABSTRACT −0,17, TOUCH 0,13, BIG ≈ 0); слепой тест — [roundtrip_long](../data/translation_test/roundtrip_long.md) |
| FEEL | спокойно … возбуждённо (−5 вялость, +5 сильное чувство; приятно или нет — GOOD): `FEEL(=+4) GOOD(=-4) \| a` злой | **новое**, принято (тест: 6 из 8; «злой» и «испуганный» путаются) |

**Правило нуля.** Ось не написана — значение не указано. `(=0)` — явное значение: у двусторонних осей середина (`TIME(=0)` — «сейчас»), у односторонних настоящий ноль (`MANY(=0)` — ни одного). Односторонние оси (степени, количества) идут 0 … +5, двусторонние (полюса) −5 … +5.

**Новые оси и корни** (слепой тест на 46 словах, `data/translation_test/roundtrip_axes_rules.md`: слово или синоним 31 из 46, 67%; слова подбирались под оси, поэтому оценка завышена по сравнению со случайными 26–34%). SOMEONE получил ось «лицо», THING — одушевлённости, MOVE — скорости, FEEL — возбуждения. Добавлены **RULE** (закон, правило, управлять) и **FIGHT** (бой, война, ссора) без осей; *peace* = `FIGHT MANY(=0) | o`. Слабые места: *tax, duty, defend, politics*; *though, instead, nevertheless* корней не получают намеренно.

**Эмоции** (слепой тест на 40 словах, `data/translation_test/roundtrip_emotions.md`): `FEEL` (возбуждение) + `GOOD` (приятность) + третий корень по смыслу, а не ось «направления» (`NEAR`/`WANT` дали 24–25 из 40 против 21; по смыслу — 28). Страх `FEEL(=+4) GOOD(=-4) TIME(=+3) | a` (плохое впереди), злость и ненависть `… FIGHT`, социальные эмоции `… SOMEONE` (+ `SEE | i`). Слабо: *shy, contempt, pity, jealous, amused*.

**Без оси (7):** BODY, SEE, SAY, DO, PLACE, CONTAINER, FIGHT.

**Правки по тесту на 200 слов** (`data/translation_test/roundtrip_200.md`): убраны HEAR, KIND, WORD (в тесте 0 удач из 7; звук читается через `SAY`, `FEEL`, тип — через `THING`, слово — `SAY | o`). Добавлены **CONSUME** (есть, пить, поглощать; *eat* = `CONSUME | i`, *food* = `THING CONSUME | o`, вместо трёх корней eat/food/drink) и **CONTAINER** (ёмкость, как *poki* в токипоне: *bag, pitcher, bottle, box*; `CONTAINER | o`). Обе без оси, пока не проверено. Правило употребления: `ABOVE`, `INSIDE`, `BIG` — только настоящее «верх / внутри / размер», не метафора и не усилитель.

**PEOPLE убран:** `SOMEONE MANY(=+4) | o` («многие кто-то») заменяет его без потерь (слепой тест на 12 словах с PEOPLE: слово или синоним 2 из 12 как до замены, «мимо» 3 вместо 5). Добавлены также HEAT, BEGIN, GIVE (см. таблицу).

Примеры составных слов: дом = `PLACE LIVE | o`; спальня = `PLACE LIVE(=-2) | o`; морг = `PLACE LIVE(=-5) | o`; мужчина = `SOMEONE SEX(=+5)`. Дыры (анатомия, родство) идут в послабления.

**Коррелятивы (идея эсперанто) без списка слов:**

| | кто | что | где | когда |
| :-- | :-- | :-- | :-- | :-- |
| вопрос | `SOMEONE?` | `THING?` | `PLACE?` | `TIME?` |
| неопределённое | `SOMEONE` | `THING` | `PLACE` | `TIME` |
| этот / здесь / сейчас | `SOMEONE NEAR(=+3)` | `THING NEAR(=+3)` | `PLACE NEAR(=+3)` | `TIME(=0)` |
| тот / там / тогда | `SOMEONE NEAR(=-3)` | `THING NEAR(=-3)` | `PLACE NEAR(=-3)` | `TIME(=-3)` или `+3` |
| всё / везде / всегда | `SOMEONE MANY(=+5)` | `THING MANY(=+5)` | `PLACE MANY(=+5)` | `TIME MANY(=+5)` |
| ничто / нигде / никогда | `SOMEONE MANY(=0)` | `THING MANY(=0)` | `PLACE MANY(=0)` | `TIME MANY(=0)` |

Открыто: у «когда» ось NEAR не подходит (там своя ось TIME); «сейчас / тогда» пока записаны через TIME.

Старые списки ниже (NSM 33, автоматические) — исторический материал и противоречат этому списку.

## Корни: NSM вместо автоматического выбора (кандидат)

Автоматический выбор нестабилен и даёт плохо читаемые корни (OBVIOUSLY, FORMIDABLE, SOFTLY). Поэтому проверен готовый список примитивов NSM (Natural Semantic Metalanguage, Вежбицкая): SOMEONE, THING, PEOPLE, BODY, KIND, PART, SAME, GOOD, BAD, BIG, SMALL, THINK, KNOW, WANT, FEEL, SEE, HEAR, WORD, TRUE, HAPPEN, MOVE, TOUCH, LIVE, DIE, TIME, PLACE, ABOVE, BELOW, FAR, NEAR, SIDE, INSIDE, MAYBE (33 из 41; служебные *say, do, can, other, because, like, much, many, all* отсутствуют в списке слов, где только знаменательные слова).

Результат на тех же 3000 записях (после послаблений), одно разбиение train/test, 27.8 бит (6 осей) / 38.2 бит (9 осей):

| набор корней | wup | pos | top50 |
| :-- | --: | --: | --: |
| NSM 33 + суффикс + 6 осей | 0.401 | 73% | 55% |
| авто 30 + суффикс + 6 осей | 0.388 | 68% | 56% |
| NSM 33 + суффикс + 9 осей | 0.411 | 74% | 59% |
| авто 30 + суффикс + 9 осей | 0.398 | 71% | 60% |

Вывод: по метрикам NSM не хуже автоматических корней (wup и pos чуть лучше, top50 на уровне), при этом набор фиксирован, читаем и не зависит от разбиения. Оговорки: корней 33, а не 30; одно разбиение, разброса нет; часть семей странная (SOMEONE-i = steal, throw; BODY-i = bury); омонимы по-прежнему грубо: *love* → WANT, *work* → HAPPEN, *play* → LIVE, *rent* → MOVE. Подробности: `data/roots_suffix_numberbatch_sense_nsm.md`.

### Градиентные корни: пара полюсов — один корень

Пары полюсов (good/bad, big/small, near/far, above/below, live/die, same/different, maybe/true (ось уверенности; нулевое значение — простое утверждение, см. [синтаксис](syntax.md))) не нужны как два корня. Корень берёт один полюс, а у корня есть **одна локальная ось** (11 уровней) от этого полюса к противоположному: GOOD+5 = good, GOOD−5 = bad. Количество (all … few), уверенность (*maybe* … *certain*), сходство (*same* … *opposite*) задаются так же. Общей оси «полярности» нет: направления good→bad, big→small, near→far в эмбеддингах почти ортогональны (средний косинус 0.07), поэтому ось у каждого корня своя; это и есть «одна локальная ось на корень».

**Ось состояния вещества (твёрдое — жидкое — газ, как kiwen/telo/kon в Toki Pona).** Проверено на 36 словах Numberbatch (12 твёрдых: stone, iron, wood…; 12 жидких: water, milk, oil…; 12 газообразных: air, smoke, steam…): проекция на направление «газ − твёрдое» даёт твёрдое −0.34, жидкое +0.06, газ +0.44 (σ ≈ 0.09), то есть жидкое лежит между и классы разделены в четыре σ; ближайший центроид с отбрасыванием слова угадывает 34 из 36. Промежуточные слова ложатся разумно: ice −0.14, sand −0.12, mud −0.01, snow +0.07, fire +0.15, dust +0.23. Оговорка: центры трёх классов лежат на прямой лишь на 62% (жидкое слегка отклоняется в сторону), так что это градиент, а не идеальная шкала. Вывод: градиентный корень MATTER (вещество) с одной локальной осью −5 (твёрдое) … 0 (жидкое) … +5 (газ); *water* как вещество всё равно может идти заимствованием (*H2O*), а ось нужна для *mud, sand, snow, dust, foam* и вообще материалов. Проверено, что среди универсальных осей такой нет: «вещественная оценка» слова (проекция на направление газ − твёрдое) по всем 3000 словам почти не выражается через оси (R² 0.07 для 9 осей, 0.21 на отложенных словах для 20 осей; корреляция с отдельной осью не выше 0.26), а назначение корня объясняет всего 6% её дисперсии. Крайние слова по оценке при этом осмысленны (fog, air, breath, smoke, cloud, gas против stone, concrete, steel, metal, rock, wood, wall). Причина: ось касается малой части словаря, поэтому оси, упорядоченные по дисперсии, её не ловят; такие редкие, но осмысленные измерения нужно задавать явно как градиентные корни.

Эксперимент (то же разбиение; 9 универсальных осей; биты не сравнивались):

| набор корней | wup | pos | top50 |
| :-- | --: | --: | --: |
| NSM, 33 отдельных корня (пары разделены) | 0.411 | 74% | 59% |
| 27 корней, у 7 локальная ось «полюс → полюс» | 0.411 | 78% | 61% |

С 6 осями: 0.401 / 73% / 55% против 0.395 / 73% / 54%. Вывод: сжатие на 6 корней без потери качества. Локальные направления заданы разностью двух слов, а не подобраны по данным. Не проверено: градиенты для времени и количества (в списке слов нет *all, many, few*), корни SAY и DO (убраны стоп-списком скрипта 01, поэтому их нет). Файлы: `data/roots_suffix_numberbatch_sense_grad.md` (с градиентом), `..._nograd.md` (контроль). Запуск: `ROOTS_WORDS`, `ROOTS_GRADIENT`, `ROOTS_TAG` для `scripts/09_roots_suffix.py`.

## Корни (автоматический выбор)

Корни выбираются жадно: среди общих слов (по числу гипонимов в WordNet) берутся те, что лучше всего покрывают остальные. Форма (часть речи) предварительно вычитается, чтобы корни не зависели от части речи.

**Нестабильность.** При смене разбиения данных набор корней меняется: в двух запусках совпало около половины (14 из 30). Поэтому корни ниже — рабочий пример, а не окончательный список.

**Устойчивое ядро** (выбрано в обоих запусках):

| Корень | `-o` | `-i` | `-a` | `-e` |
| :-- | :-- | :-- | :-- | :-- |
| THINK | idea, thing | think, suppose | sure, likely | probably, maybe |
| MOVE | movement, motion | move, shift | quick, rapid | forward, swiftly |
| PROVIDE | provision, assistance | provide, furnish | adequate, reliable | helpfully, sufficiently |
| AMOUNT | amount, quantity | expend, allot | total, minimum | roughly, approximately |
| CORRESPOND | address, letter | correspond, coincide | identical, similar | respectively, exactly |
| REGARD | respect, consideration | regard, concern | particular, careful | particularly, especially |
| OCCURRENCE | occurrence, incident | occur, happen | unusual, rare | rarely, seldom |
| NOISE | noise, sound | clamor, roar | loud, shrill | loudly, quietly |
| EXAMINE | examination, study | examine, inspect | analytic, curious | carefully, thoroughly |
| ROOM | room, bedroom | huddle, sit | comfortable, private | upstairs, inside |
| CREATE | form, environment | create, generate | creative, unique | thereby, deliberately |
| COMMITTEE | committee, board | appoint, elect | legislative, municipal | unanimously, formally |

**Остальные корни одного из запусков:** DEFEAT, DESIRE, INCREASE, ROAD, STICK, MIXTURE, EVIDENCE, RESTRAIN, RELIGION, INFORM, COMPANY, CUT, OFFICER, WRITER, WEATHER, DISEASE. В другом запуске вместо них были EMOTION, HIT, REQUEST, AREA, IMPROVE, DESCEND, TERMINATE, FAITH, SOLDIER, ACHIEVEMENT, FASTEN, COMPETE, METAL, FOOD, AUTHOR, OFFICIAL.

**Известные проблемы корней.**
- Часть семей нерегулярна: у *AREA* глагол `-i` — *sprawl, locate*; у *MONTH* глагол `-i` был *march, rent* (теперь снято: месяцы и дни недели идут числами, см. «Послабления»).
- 30 корней — грубое покрытие: *love* попадает в THINK, а не в EMOTION.
- Конверсии (*work, play, love, order*) размечены WordNet как производные формы и получают общий корень (`TOOL | o` / `TOOL | i`); настоящие омонимы (*close* «закрыть» и «близкий») получают разные корни.

## Послабления (слова вне 30 корней)

Часть лексики не имеет смысла кодировать через общие корни и оси. Она выносится за пределы бюджета в 30 корней и не расходует оси:

- **Названия стран** (и вообще имена собственные-топонимы) — заимствуются как есть, без корня и признаков.
- **Числа** — отдельная система счёта, не корни.
- **Месяцы и дни недели** — по номеру: месяц 3, день недели 2 (а не слова *March*, *Tuesday*).
- **Цвета** — непрерывные координаты (RGB или HSL), а не слова и не корень COLOR (убран из списка корней).
- **Имена собственные** (люди, места, организации, марки) — заимствуются как есть, как и названия стран.
- **Национальности и религии** (*american*, *mexican*, *christian*, *catholic*) — производные от имён собственных, заимствуются вместе с ними. В эксперименте они сами собирались в корни AMERICAN и CHRISTIAN.
- **Биологические таксоны** — латинская номенклатура как есть (*Canis lupus familiaris*, *Opuntia indica*); для обычной речи достаточно названия рода или вида (*Canis*, *Felis*, *Quercus*). Корни ANIMAL и PLANT поэтому не нужны. Анатомия и медицина (латинские термины, болезни) пока не решены, см. [roadmap](roadmap.md).
- **Химия** — названия элементов и соединений по IUPAC/латинские (*H2O*, *natrii chloridum*), формулы как есть.
- **Минералы и горные породы** — научные названия как есть (*quartz*, *granite* в латинской/минералогической форме).
- **Астрономия** — названия звёзд, созвездий, планет и других небесных тел как есть (*Sol*, *Ursa Major*).

Следствие: корень MONTH больше не нужен, а с ним уходит и ошибка с омонимами *march* (шагать) и *rent* (аренда): их отнесли в MONTH из-за «месячного» контекста. Остаётся открытым, как записывать сами числа, как отличить заимствованное имя от слова языка (метка или фонологический признак) и как склонять/присоединять суффиксы к ним ([фонология](phonology.md)).

## Суффиксы

`-o` имя, `-i` глагол, `-a` признак, `-e` обстоятельство — суффиксы эсперанто. Любой корень берёт любой суффикс (см. [синтаксис](syntax.md)). В экспериментах суффикс стоит 2 бита вместо ~10 бит у трёх непрерывных осей формы при тех же или лучших метриках. Потеряны промежуточные формы (причастия, герундий); они могут вернуться позже как операторы слоя 2 ([план](plan.md)).

## Универсальные смысловые оси

Оси найдены по отклонениям слов от центра своего корня (пулом по всем корням), поэтому значат одно и то же для любого корня. Названий у них пока нет. Ниже — слова на полюсах осей одного из запусков (знак и порядок осей между запусками не стабильны):

| № | полюс − | полюс + |
| :-: | :-- | :-- |
| M1 | fundamental, principle, term, objective, requirement, basic | grateful, shudder, dear, glad, joy, friendly |
| M2 | broad, profound, extensive, impulse, sudden, intensity | oblige, fortunate, lucky, certify, owe, insist |
| M3 | real, truly, genuine, uniquely, wholly, true | impatiently, anxiously, cautiously, nervously, hastily |
| M4 | hereafter, somewhere, forever, eternal, inevitable | tremendously, vastly, impressive, remarkably, big, large |
| M5 | ask, invoke, beckon, lend, invite, borrow | fairly, perfectly, reasonably, extremely, sufficiently |
| M6 | flatly, tax, ratio, totally, wildly, rate | linger, foresee, considerable, farther, significant, emerge |
| M7 | strive, mentally, educate, engage, collaborate | vague, shortly, sadly, nevertheless, mention, notice |
| M8 | stubbornly, exist, stare, falter, underlie | select, arrange, able, ideally, dispose, locate |
| M9 | incredible, brilliant, fantastic, magnificent, remarkable | frequent, tend, sometimes, usually, frequently, mostly |

Честная оценка: оси читаются плохо (степень, манера, оценка, но без чёткой темы), и это главная слабость текущей схемы. Рассматривается замена на оси, заданные по полюсам вручную (*small ↔ large*, *bad ↔ good*, …) с проверкой качества на данных. Одна локальная ось на корень (0/1) прибавляла бы лишь 2–3 пункта точности за +30 осей в описании языка, поэтому не используется.


## Архив: глобальные оси nano-10 (из данных)

Получена экспериментом на английском (Numberbatch, 3000 слов, частотность вычтена): 3 оси формы + 7 смысловых. Подробности и метрики: [план](plan.md), `data/form_meaning_numberbatch.md`. Названия полюсов автоматические (слова с наибольшей нагрузкой); колонка «ярлык» — ручная интерпретация, а не результат метода. Знак и порядок осей зависят от выборки и не стабильны между запусками.

### Форма (части речи как непрерывные координаты)

| № | полюс − | полюс + | ярлык |
| :-: | :-- | :-- | :-- |
| F1 | plainly, practically, subsequently, mildly, similarly, largely | give, seek, invoke, summon, assign, ask | наречие ↔ глагол |
| F2 | peculiar, vivid, practical, severe, intelligent, logical | come, move, give, bring, tell, raise | прилагательное ↔ глагол |
| F3 | significant, nice, serious, strong, big, obvious | guy, attitude, aspect, image, scene, element | прилагательное ↔ существительное |

### Смысл

| № | полюс − | полюс + | ярлык | близкая ручная ось |
| :-: | :-- | :-- | :-- | :-- |
| M1 | specify, determine, define, entail, pursuant, affirm | roar, swoop, gasp, shiver, scream, slam | формальное определение ↔ физическая экспрессия | — |
| M2 | complete, subtract, minimum, eliminate, remove, total | concern, uneasy, resent, regret, wonder, admire | удаление и полнота ↔ переживание | EMOTION POS / NEG |
| M3 | educate, help, collaborate, strengthen, foster, promote | suppose, probably, guess, presume, reckon, anyway | поддержка ↔ предположение | CERTAINTY |
| M4 | later, after, late, postpone, before, thereafter | uniquely, truly, perfectly, really, pretty, absolutely | время ↔ степень | TENSE, TEMPORALITY |
| M5 | assuredly, hope, surely, believe, finally, concede | vary, various, mainly, specific, primarily, variety | уверенность ↔ разнообразие | CERTAINTY, QUANTITY |
| M6 | greater, tremendous, enormous, considerable, huge | notify, designate, instruct, inform, report, briefly | размер и степень ↔ сообщение | SIZE, INTENSITY |
| M7 | achieve, happen, occur, attain, accomplish, realize | denounce, reject, endorse, condemn, approve, refuse | свершение ↔ оценка и отказ | GOODNESS (смутно) |

Ярлыки у M1, M5 и M7 слабые: полюса смешанные. Чёткие оси: F1–F3, M2, M3, M4, M6.

## Архив: исходная гипотеза, 30 ручных признаков

Список ниже составлен вручную до экспериментов. Он используется как гипотеза для сравнения с осями из данных, а не как окончательный набор.

Каждый признак — непрерывная шкала от **-5 до +5**.

| Признак | Спектр |
| :-- | :-- |
| SIZE | tiny ← small ← medium → large → vast |
| TENSE | far past ← recent past ← now → near future → far future |
| GOODNESS | bad ← flawed ← neutral → good → excellent |
| ENERGY | inert ← passive ← stable → active → hyper |
| SPEED | frozen ← slow ← normal → fast → instant |
| INTENSITY | faint ← weak ← average → strong → overwhelming |
| CERTAINTY | unsure ← guess ← probable → certain → obvious |
| FAMILIARITY | unknown ← distant ← neutral → familiar → intimate |
| HUMANNESS | object ← machine ← animal → human → divine |
| TEMPORALITY | ancient ← old ← modern → futuristic → timeless |
| SPATIALITY | far ← yonder ← near → here → internal |
| LIQUIDITY | solid ← gel ← liquid → vapor → formless |
| SHARPNESS | dull ← soft ← crisp → sharp → piercing |
| COLOR VALUE | dark ← muted ← normal → bright → radiant |
| COLOR HUE | red ← orange ← green → blue → purple |
| EMOTION POS | sad ← bored ← neutral → happy → euphoric |
| EMOTION NEG | calm ← uneasy ← nervous → afraid → terrified |
| TOGETHERNESS | alone ← few ← group → crowd → swarm |
| ABSTRACTION | tangible ← concrete ← idea → symbol → metaphysical |
| AGENCY | passive ← dependent ← neutral → active → autonomous |
| DEFINITENESS | vague ← ambiguous ← referenced → definite → specific |
| DEIXIS | far ← that ← here/this → immediate |
| SURENESS | doubtful ← unsure ← probable → confident → evident |
| FORMALITY | playful ← casual ← polite → formal → ceremonial |
| DISCRETENESS | individual ← few ← many → mass → undifferentiated |
| QUANTITY | none ← some ← many → all → universal existence |
| TRUTH | lie ← ironic ← true → sacred |
| IMPORTANCE | trivial ← helpful ← important → vital |
| TIME_SCALE | momentary ← brief ← long → eternal |
| SERIOUSNESS | humorous ← light ← serious → solemn → ritual |
