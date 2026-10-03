# Тест слов в изоляции: хватает ли имеющихся корней

18 слов из списка провалов статьи *Republic*. Каждое слово (с пометкой смысла) закодировали три независимых кодировщика только корнями, без словаря `@NN`; три слепых декодера дали слово и две альтернативы. «Попадание» — исходное слово или его близкий синоним в лучшем ответе или альтернативах (оценка моя, не слепая).

| слово | попаданий | кодировщик A | кодировщик B | кодировщик C |
| :-- | :-- | :-- | :-- | :-- |
| function | 1/3 (B) | `PART DO \| o` → component | `PART-o DO-o \| o` → role | `DO PART \| o` → task |
| member | 0/3 | `PART SOMEONE MANY \| o` → population | `PART-o SOMEONE-o MANY(=3) \| o` → group | `PART SOMEONE MANY \| o` → population |
| regime | 0/3 | `RULE SOMEONE TIME(=0) \| o` → president | `RULE-o SOMEONE-o BIG(=3) \| o` → king | `RULE SOMEONE TIME(=0) \| o` → president |
| meaning | 1/3 (B) | `SAY THINK THING \| o` → idea | `THINK-o PI SAY-o \| o` → meaning | `SAY THINK \| o` → opinion |
| refer to | 3/3 | `SAY THING \| i` → speak | `SAY-i E THING-o \| i` → state | `SAY THING \| i` → name |
| require | 1/3 (A: demand) | `SAY WANT(=+5) \| i` → request | `RULE-i WANT(=4) \| i` → reign | `WANT(=5) DO \| i` → strive |
| necessarily | 3/3 | `MAYBE(=+4) HAPPEN(=+5) \| e` → inevitably | `HAPPEN(=5) MAYBE(=4) \| e` → consequently | `MAYBE(=4) HAPPEN(=5) \| e` → inevitably |
| specific | 0/3 | `PART SAME(=+5) \| a` → identical | `PART(=-3) SAME(=5) \| a` → similar | `PART(=-3) SAME(=5) \| a` → similar |
| institution | 1/3 (B: parliament) | `RULE SOMEONE MANY \| o` → government | `PLACE-o RULE-o SOMEONE-o MANY(=3) \| o` → parliament | `RULE PLACE MANY \| o` → empire |
| class | 0/3 | `SOMEONE MANY SAME \| o` → community | `SOMEONE-o MANY(=3) SAME(=3) \| o` → community | `SOMEONE SAME(=3) PART \| o` → colleague |
| union | 0/3 | `MANY PART(=+5) \| o` → majority | `MANY-o PART(=5) SAME(=5) \| o` → entirety | `MANY PART(=5) \| o` → everything |
| influence | 0/3 | `DO HAPPEN(=+5) \| i` → cause | `DO-i HAPPEN(=5) \| i` → achieve | `DO HAPPEN(=5) \| i` → achieve |
| protect | 0/3 | `DO GOOD FIGHT(=-5) \| i` → help | `DO-i FIGHT(=-4) GOOD(=4) \| i` → make peace | `DO FIGHT(=-5) GOOD \| i` → reconcile |
| limit | 1/3 (B) | `DO CAN(=-3) PLACE \| i` → prevent | `DO-i CAN(=-3) BIG(=-3) \| i` → restrict | `DO CAN(=-3) PLACE \| i` → position |
| ideal | 1/3 (B) | `THINK GOOD(=+5) \| o` → optimism | `THINK-o GOOD(=5) PART(=5) \| o` → ideal | `GOOD(=5) THINK \| o` → idea |
| philosophy | 1/3 (B) | `THINK KNOW(=+5) \| o` → certainty | `THINK-o KNOW-o BIG(=4) \| o` → philosophy | `THINK KNOW MANY \| o` → knowledge |
| modern | 3/3 | `TIME(=0) \| a` → current | `TIME(=-1) \| a` → recent | `TIME(=0) NEAR(=5) \| a` → current |
| term | 3/3 | `SAY THING \| o` → word | `SAY-o THING-o \| o` → word | `SAY THING \| o` → word |

Итоги:
- Читаются всеми тремя: *refer to, necessarily, modern, term* (4).
- Не читаются ни одним (0/3): *member, regime, specific, class, union, influence, protect* (7).
- Читаются только при удачном кодировании (1/3), кодировщики расходятся: *function, meaning, require, institution, limit, ideal, philosophy* (7).

Выводы: провалы 0/3 — слова-отношения (член группы, режим, класс, союз) и оттенки (*specific, influence, protect*); они кодируются через `PART SOMEONE MANY`, `RULE SOMEONE`, `DO HAPPEN`, `DO FIGHT(=-5)`, и декодер читает их как «население», «президент», «достичь», «помирить». В группе 1/3 проблема в нестабильности: слово выразимо, но разные кодировщики пишут разные коды. Размер выборки маленький (18 слов, по одному декодеру на набор).
