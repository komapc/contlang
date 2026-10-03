# Туда-обратно: 30 случайных слов (слепой декодер)

Слова выбраны случайно из `data/wordlist_en_x5.tsv` (зерно 20261003). Кодировал ассистент по модели из `docs/model.md` (31 корень, оси в корнях, составные слова), одна попытка без правок. Декодировал субагент без оригиналов, только по спецификации. Оценку («точно» — слово среди трёх ответов; «синоним» — близкий по смыслу; «рядом» — родственное значение; «мимо») поставил я, независимого судьи не было.

| # | слово | код | декодер (лучший / запасные) | оценка |
| --: | :-- | :-- | :-- | :-- |
| 1 | world | PLACE-o BIG(=+5) MANY(=5) | world / universe, everywhere | точно |
| 2 | mighty | DO-a BIG(=+4) | active / powerful, busy | синоним |
| 3 | ask | SAY-i WANT-a(=+3) KNOW-o | ask / question, inquire | точно |
| 4 | elect | WANT-i PEOPLE-o MANY(=+4) E SOMEONE-o | admire / popular, court | мимо |
| 5 | production | DO-o E THING-o MANY(=+4) | work / industry, business | рядом |
| 6 | fulfill | DO-i E WANT-o PART(=+5) | fulfill / satisfy, achieve | точно |
| 7 | lot | THING-o MANY(=+4) | stuff / goods, things | рядом |
| 8 | assess | THINK-i E GOOD-o(=0) | consider / judge, evaluate | синоним |
| 9 | letter | WORD-o THING-o MOVE-a | verb / action, gerund | мимо |
| 10 | worst | GOOD-a(=-5) | terrible / awful, horrible | синоним |
| 11 | christ | "Christ" | christ / jesus, messiah | точно (имя, послабление) |
| 12 | delicate | TOUCH-a BIG(=-4) GOOD(=+2) | soft / gentle, smooth | синоним |
| 13 | scream | SAY-i HEAR(=+5) GOOD(=-3) | scold / shout, curse | синоним |
| 14 | city | PLACE-o PEOPLE-o MANY(=+4) | city / town, country | точно |
| 15 | serve | DO-i E SOMEONE-o WANT-o | serve / please, help | точно |
| 16 | rebuild | DO-i E PLACE-o SAME(=+5) TIME(=+2) | reserve / prepare, stay | мимо |
| 17 | restore | DO-i E THING-o SAME(=+5) TIME(=-2) | restore / repair, maintain | точно |
| 18 | protest | SAY-i WANT(=-5) E HAPPEN-o | forbid / prevent, prohibit | мимо |
| 19 | film | SEE-o MOVE-a | movie / film, show | точно |
| 20 | ponder | THINK-i BIG(=+4) TIME-o | ponder / remember, history | точно |
| 21 | difficult | DO-a BIG(=+4) GOOD(=-2) | destructive / harmful, wicked | мимо |
| 22 | variable | SAME-a(=-3) TIME-o MANY(=+3) | various / different, varied | синоним |
| 23 | decline | HAPPEN-i BIG(=-3) | occur / happen, trifle | мимо |
| 24 | whole | PART-a(=+5) | complete / whole, entire | точно |
| 25 | consequently | HAPPEN-e TIME(=+1) | soon / shortly, suddenly | мимо |
| 26 | culture | PEOPLE-o LIVE-o KIND-o | humanity / mankind, species | рядом |
| 27 | accurate | SAME-a(=+5) GOOD(=+3) | equal / fair, alike | мимо |
| 28 | nucleus | PART-o INSIDE(=+5) | core / interior, center | синоним |
| 29 | supply | MOVE-i E THING-o SOMEONE-o NEAR(=+3) | bring / give, deliver | синоним |
| 30 | glance | SEE-i TIME-o BIG(=-4) | glance / glimpse, blink | точно |

Итого: точно 11 (10 без имени «Christ»), синоним 8, рядом 3, мимо 8.

## Второй проход: 8 «мимо» закодированы иначе

Тот же слепой протокол, другой декодер (оригиналов и первых результатов не видел). Новые коды писал я, зная, как декодер ошибся в первый раз.

| слово | новый код | декодер | оценка |
| :-- | :-- | :-- | :-- |
| elect | PEOPLE-o MANY(=+4) WANT-i E SOMEONE-o ABOVE(=+4) | worship / admire, follow | мимо |
| letter (письмо) | THING-o PI WORD-o MOVE-a | letter / message, mail | точно |
| rebuild | DO-i E PLACE-o SAME(=+5) TIME(=-2) | restore / repair, **renovate** | рядом |
| protest | SAY-i HEAR(=+4) WANT(=-5) | yell / shout, curse | мимо |
| difficult | DO-a MAYBE(=-3) | possible / able, feasible | мимо (противоположное) |
| decline | HAPPEN-i BIG(=-3) TIME(=+2) | begin / start, arrive | мимо |
| consequently | HAPPEN-e NEAR(=+5) TIME(=+1) | soon / immediately, presently | мимо |
| accurate | SAME-a(=+5) KNOW-o | fact / truth, consensus | рядом |

Итого: точно 1, рядом 2, мимо 5. Провалы теперь не от двусмысленного кода, а от отсутствия понятий: нет «мочь» (*difficult / possible*), нет «потому что» (*consequently*), нет «выбирать» (*elect*), отрицание через `WANT(=-5)` декодер не читает. В NSM есть CAN, BECAUSE, IF, NOT, MORE, VERY, LIKE — в наш список они не попали, так как в тесте слов их исключал стоп-лист.

## Третий проход: CAN и ось причины у HAPPEN

Корень CAN (ось «не могу … могу») добавлен; `DO-a CAN(=-3)` → *difficult*, `DO-a CAN(=+4)` → *easy*, `CAN-a(=-5)` → *impossible* (слепой декодер, 3 из 3). Ось HAPPEN «причина … следствие» (−5 … +5): `HAPPEN-o(=+4)` → *result*, `HAPPEN-o(=-4)` → *cause*, `HAPPEN-e(=+4)` → *therefore / consequently*, `HAPPEN-e(=-4)` → *because*, `HAPPEN-i(=+4)` → *follow*, `HAPPEN-a(=+3)` → *resulting* (6 из 6). Оба теста с описанием оси в спецификации, слова подбирались под ось, не случайная выборка.

## Четвёртый проход: elect, protest, decline (с CAN и осью HAPPEN)

Слепой декодер, по несколько вариантов кода на слово.

| слово | код | декодер | оценка |
| :-- | :-- | :-- | :-- |
| elect | DO-i E SOMEONE-o ABOVE(=+4) | serve / obey, worship | мимо |
| elect | THINK-i MANY(=+4) E SOMEONE-o ABOVE(=+4) | respect / admire, worship | мимо |
| protest | SAY-i GOOD(=-4) HEAR(=+3) | curse / scold, shout | мимо |
| protest | PEOPLE-o MANY(=+4) SAY-i WANT(=-5) | **protest** / boycott, complain | точно |
| decline (уменьшаться) | MOVE-i ABOVE(=-3) BIG(=-2) | sink / drop, descend | рядом |
| decline (ухудшаться) | HAPPEN-i GOOD(=-2) TIME(=+2) | danger / threat, disaster | мимо |
| decline (отказать) | SAY-i WANT(=-5) | refuse / deny, **decline** | точно |

Итог: protest и decline решены (в разных значениях), elect нет: понятия «выбирать голосованием» в корнях не выражается.
