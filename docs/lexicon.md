# Словарь

Фиксированного словаря нет: слова порождаются как **корень + суффикс + признаки** ([синтаксис](syntax.md)). Ниже — рабочая схема, полученная экспериментами на английском (ConceptNet Numberbatch, 3000 слов; метрики и сравнения в [плане](plan.md)). Всё здесь **рабочая гипотеза**, а не окончательный словарь.

## Структура кода слова

| Часть | Что это | Размер |
| :-- | :-- | :-- |
| корень | одно из ~30 общих понятий, не привязанных к части речи | log2(30) ≈ 5 бит |
| суффикс | `-o`, `-i`, `-a`, `-e` | 2 бита |
| признаки | универсальные оси, значения -5..+5 (11 уровней); порядка 6–9 осей, корень может использовать часть из них | ≈ 3.5 бита на ось |

При такой схеме (30 корней + суффикс + 6 осей, 27.7 бит на слово) ближайшее по смыслу и форме слово находится заметно лучше, чем при глобальных осях той же длины (8 осей): top50 66% против 39%.

## Корни: текущий список (черновик, 32)

Правило: у каждого корня **своя** ось (одна) или никакой; составные слова из двух-трёх корней, как в эсперанто (главное первым, остальные уточняют; см. [модель](model.md)). Корни берутся из NSM; автоматически подобранные слова корнями не берутся (проверено: выигрыш по wup ≤ 0,01, корни нечитаемы, набор нестабилен, см. `data/roots_optimization.md`).

**С осью (19):**

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
| PART | часть … целое | принято |
| SIDE | зад … перёд | принято |
| HEAR | тихо … громко | принято |
| KNOW | не знаю … знаю | принято |
| WANT | не хочу … хочу (ненависть … любовь) | принято |
| SEX | женское … мужское | **новое**, предложено |
| HAPPEN | причина … следствие (−5 первопричина, 0 просто событие, +5 результат): `HAPPEN-o(=+4)` следствие, `HAPPEN-o(=-4)` причина, `HAPPEN-e(=+4)` следовательно, `HAPPEN-e(=-4)` потому что | **новое**, принято (слепой тест: 6 из 6) |
| THINK | сомневаться … решить (−5 сомневаться, 0 думать, +5 решить): `THINK-i(=+5)` решить / выбрать, `THINK-o(=+5)` решение | **предложено**, слепой тест 5 из 6; отдельного корня «выбрать» не нужно |
| CAN | не могу … могу (−5 невозможно, −3 трудно, +4 легко); из NSM, нужен для «трудно / возможно» | **новое**, принято (BECAUSE отвергнут) |
| MANY | **односторонняя** 0 … +5: ни одного … единицы … многие … все | **новое**, пробуем; «один» и точные числа — числа из послаблений |

**Правило нуля.** Ось не написана — значение не указано. `(=0)` — явное значение: у двусторонних осей середина (`TIME(=0)` — «сейчас»), у односторонних настоящий ноль (`MANY(=0)` — ни одного). Односторонние оси (степени, количества) идут 0 … +5, двусторонние (полюса) −5 … +5.

**Предложено, не подтверждено** (ось у корня есть, но решение за пользователем): SOMEONE и PEOPLE — ось «лицо» (я +5, ты +3, кто-то 0, он −3; PEOPLE — мы, вы, они); THING — ось одушевлённости (камень −5 … растение 0 … животное +4; человек — SOMEONE).

**Без оси (13):** SOMEONE, PEOPLE (оси «лицо» выше), THING, KIND, WORD, BODY, MOVE, FEEL, SEE, TOUCH, SAY, DO, PLACE. Оси MOVE (стоять … быстро) и FEEL (неприятно … приятно) средние, их проверяем.

Примеры составных слов: дом = `PLACE-o LIVE-i`; спальня = `PLACE-o LIVE-i(=-2)`; морг = `PLACE-o LIVE-i(=-5)`; мужчина = `SOMEONE SEX(=+5)`. Дыры (анатомия, родство) идут в послабления.

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
- Конверсии (*work, play, love, order*) размечены WordNet как производные формы и получают общий корень (`TOOL-o` / `TOOL-i`); настоящие омонимы (*close* «закрыть» и «близкий») получают разные корни.

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
