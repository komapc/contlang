# 64 слова, прочитанные мимо во всех трёх вариантах (A, S, HS)

Разбор по каждому слову (2026-10-14). «Лучше» — мой код нынешними корнями; это гипотеза, слепо не проверена.

## 1. Код можно исправить нынешними корнями (математика выбрала не то)

**Голова THINK вместо нужной** (THINK притягивает глаголы ума и речи):

| слово | смысл | код A → ответ | беда | лучше |
|---|---|---|---|---|
| alleged | заявленный без доказательства | `THINK(=+2) TIME(=-5) MANY(=-5) \| i` → forget | голова должна быть SAY; TIME(-5) MANY(-5) — «давно, никогда» | `SAY THINK(=-3) \| a` |
| alleging | утверждать (обвиняя) | `THINK(=+1) TIME(=-5) RULE(=+3) \| i` → remember | то же | `SAY RULE(=+3) THINK(=-3) \| i` |
| discussed | обсуждали | `THINK(=0) KNOW(=+2) TIME(=-1) \| i` → remember | голова SAY | `SAY THINK \| i N+3 T-2` |
| searching | искать | `THINK(=0) CARE(=+4) LIVE(=-1) \| i` → meditate | голова SEE | `SEE WANT(=+4) \| i` |
| maintain | сохранять | `CHANGE(=-3) THINK(=+4) GIVE(=-1) \| i` → choose | THINK(+4) = «решить» | `CHANGE(=-5) \| i K+5` |
| stabilize | сделать устойчивым | `CHANGE(=0) THINK(=+3) ABOVE(=-2) \| i` → revise | CHANGE(=0) = «менять»; THINK лишний | `MOVE(=-5) \| i K+5` |
| test | проверять | `THINK(=+2) ART(=-3) FIGHT(=-1) \| i` → plan | ART, FIGHT случайны | `MEASURE KNOW \| i` |

**Есть готовая запись, но математика не ставит метки (K, роли):**

| слово | код A → ответ | лучше |
|---|---|---|
| prevent | `JOIN(=-1) MOVE(=-2) HAPPEN \| i` → collapse | `HAPPEN \| i K-5`: в спецификации прямо «K-5 prevent» |
| hide | `INSIDE(=0) JOIN(=-2) SAY(=-3) \| i` → murmur | `SEE \| i K-5` — не дать увидеть |
| exposed | `KNOW(=0) INSIDE(=-1) ABOVE(=-1) \| i` → suspect | `INSIDE(=-5) SEE \| i V-4` |
| source | `TEXT CHANGE(=-2) CAN(=+3) \| o` → manual | `BEGIN(=-5) PLACE \| o` (или `HAPPEN \| o agent` = cause) |

**Ключевой корень с неверным значением, часто 0:**

| слово | код A → ответ | беда | лучше |
|---|---|---|---|
| grown | `BIG(=0) ABOVE(=+4) TOUCH(=-1) \| i` → lift | BIG(=0) — «средний», рост потерян | `CHANGE BIG(=+4) \| i T-2` |
| specifically | `SAME(=-1) SOMEONE(=-1) CARE(=+2) \| e` → similarly | на оси SAME «особый» = −4 | `SAME(=-4) \| e` |
| cigarette | `GRAIN(=-2) HEAT(=+5) CONSUME(=+4) \| o` → soup | −2 ≈ жидкость; читатель прав | `CONSUME(=+5) GRAIN(=-5) HEAT(=+5) \| o tool` (дым) |
| preceded | `BEGIN(=0) SAME(=0) HAPPEN \| i` → continue | два нуля — шум | `SIDE(=+5) MOVE \| i T-2` |
| steps | `ABOVE(=0) SIDE(=0) DO \| i` → turn | два нуля; скорее имя | `MOVE PART(=-2) \| o N+3` |
| tired | `FEEL(=-1) \| a` → calm | FEEL −5 = «спокойный» | `LIVE(=-2) \| a` (−2 = asleep) |
| session | `PART(=+2) BEGIN(=+1) TIME(=0) \| o` → ending | BEGIN(+1) тянет к «концу» | `TIME PART(=-2) JOIN(=+5) \| o` |
| remainder | `BEGIN(=+2) JOIN(=-4) MOVE(=-5) \| o` → pause | MOVE(-5) = «стоять» | `PART(=-2) CHANGE(=-5) \| o` (часть, что осталась) |

**Остальные корни случайны, нужна другая сборка:**

| слово | код A → ответ | лучше |
|---|---|---|
| evident | `SAME(=-2) MANY(=-4) CARE(=+2) \| a` → rare | `SEE CAN(=+5) \| a` — легко увидеть |
| explicitly | `TEXT SOMEONE(=-4) MANY(=-2) \| e` → anonymously | `SAY SEE CAN(=+5) \| e` |
| notorious | `TIME(=-2) BIG(=+4) FRIEND(=-4) \| a` → bitter | `KNOW MANY(=+5) GOOD(=-4) \| a` — все знают, дурное |
| voting | `FIGHT(=-2) RULE(=+5) PART(=+3) \| i` → compete | `THINK(=+5) PART(=+5) \| i` — решать группой |
| warnings | `KNOW(=+1) SAY(=+2) TEXT \| o N+3` → lessons | `SAY GOOD(=-4) TIME(=+1) \| o N+3` — сказ о скорой беде |
| parliamentary | `RULE(=+3) INSIDE(=+1) FIGHT(=-1) \| a` → internal | `RULE(=+4) SAY PART(=+5) \| a` |
| attracting | `FEEL(=+1) INSIDE(=-3) SAME(=-3) \| i` → surprise | `WANT(=+4) NEAR(=+4) \| i K+5` |
| negative | `CHANGE(=0) MEASURE(=+3) GOOD(=-2) \| a` → variable | `GOOD(=-3) THINK \| a` (или «ниже нуля» `MEASURE ABOVE(=-5)`) |
| junk | `VALUE(=-1) PART(=0) LONG(=+2) \| o` → wood | `GOOD(=-5) THING(=-5) \| o N+3`; VALUE −5 смешивает «дешёвый» и «торговля» |
| surprising | `GOOD(=+1) THINK(=-3) HAPPEN \| i` → gamble | признак, а не глагол: `SAME(=-5) THINK \| a` — не как думали |
| related | `SAME(=0) JOIN(=+3) HAPPEN \| i` → coincide | признак: `JOIN(=+3) \| a`; HAPPEN лишний |

**В код протёк вид или другой смысл английского слова** (Numberbatch держит и части слова, и другие смыслы):

| слово | код A → ответ | откуда корень | лучше |
|---|---|---|---|
| billboard | `TEXT LONG(=+3) ART(=+2) \| o` → novel | board = доска → LONG | `TEXT VALUE(=-5) BIG(=+5) \| o` — большая надпись-торговля |
| chief | `RULE(=+3) TIME(=-1) BODY \| a` → medical | chief ≈ head → BODY | `VALUE(=+5) \| a C+5` (главный) |
| chair | `LONG(=+2) MOVE(=-3) RULE(=+2) \| o` → path | chairman → RULE; LONG +2 = прут, не мебель | `LONG(=+5) \| o FOR BODY ABOVE(=-2) \| o` (сидеть нечем сказать) |
| setting | `PLACE HEAT(=+3) PART(=+4) \| i` → ignite | sun setting, set fire → HEAT | имя: `PLACE NEAR(=+5) \| o` — окружение |

**Многозначные слова, взят не тот смысл или не та часть речи:**

| слово | код A → ответ | лучше |
|---|---|---|
| certain | `SAME(=-1) MANY(=0) THINK(=+1) \| a` → various | «уверенный» `KNOW(=+5) \| a`; «некий» — другой код |
| tears | `MOOD(=-2) SAY(=+1) CONSUME(=-2) \| i` → complain | слёзы: `GRAIN(=-3) MOOD(=-3) \| o PI SEE \| o tool` (жидкость глаза) |
| shares | `GIVE(=+1) MEASURE(=+2) VALUE(=-2) \| i` → discount | делиться: `GIVE PART(=-2) \| i`; акции: `PART(=-2) VALUE \| o N+3` |
| projects | `ART(=0) GIVE(=+3) SOMEONE(=0) \| i` → teach | скорее имя: `DO TIME(=+2) \| o result N+3` |
| hatch | `INSIDE(=0) LONG(=+3) BEGIN(=-1) \| i` → stretch | вылупиться: `LIVE BEGIN(=-5) INSIDE(=-5) \| i`; люк — другой код |

## 2. Нет корня или значения на оси

| чего нет | слова | что видно |
|---|---|---|
| **истина, реальность** (токипонское *lon*) | truth, proved, alleged, justified, evident, certain | `KNOW(=0) MANY(=-3) WANT(=+3)` → curiosity: «правда» не собрать |
| **нужно, обязан** (токипонское *wile* = хотеть/нужно/должен) | requires, mandatory, sufficient, qualify, deserved | `DO WANT(=+1) CAN(=+1)` → try (во всех трёх). Дёшево: дописать к WANT +5 «need, must» |
| **закон, преступление** (LAW из ../swap) | forensic, plaintiffs, justified, mandatory | всё сводится к RULE = «порядок, формальность» → precise, owners, formal |
| **публичное и тайное** (PUBLIC из ../swap) | disclosure, exposed, hide, explicitly | `RULE(=+1) KNOW(=+2) TEXT` → manual |
| **священное, вера** | blessed, saint, sect (ранее monks, chapel) | saint → actor, sect → capital, blessed → enjoy |
| **цвет, свет** | pink | `LONG(=-1) TOUCH(=-4) BIG(=-2)` → delicate; цветов нет вовсе |
| **одежда, нога** | shoe | `THING(=-1) LONG(=-4) MEASURE(=-3)` → thread (LONG −4 = ткань) |
| **опасность, защита** | protected, warnings | protected → notice |
| **значение, слово** (метаязык, как в ../manifesto) | defining | → imagine |
| **причина** («почему») | justify | `THINK(=+1) WANT(=-1) DO` → plan |

## 3. Мусор в списке целей
dos, gilbert, jay, semi (и rick ранее) — имена, обрывки, не обычные слова. Убрать из будущих тестов. entity — слишком общее, угадать почти нельзя.

## Итог
- Около 40 из 64 — ошибки кодера сайта, которые нынешние корни могли бы исправить. Типовые ошибки:
  - голова THINK там, где нужен SAY или SEE;
  - ключевой корень со значением 0 или с неверным значением;
  - не ставятся метки K и роли;
  - в код протекает вид английского слова (board, head, chairman);
  - взята не та часть речи.
- Около 20 — нет понятия. Чаще всего не хватает «истины» (6 слов) и «нужно» (5). Оба есть в Токипоне (*lon*, *wile*).
  «Нужно» можно дописать к оси WANT без нового корня. Дальше идут LAW и PUBLIC: они уже кандидаты из ../swap.
