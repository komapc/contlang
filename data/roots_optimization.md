# Оптимизация выбора корней: MILP, жадный, обмены (оси игнорируются)

Цель: максимизировать среднее по 3000 словам лучшее косинусное сходство слова с корнем (пространство без частотности и формы). Выбор по всем словам. MILP — p-median (HiGHS, 30 ближайших кандидатов на слово, лимит 240 с); «верхняя граница» — оптимум модели (не меньше настоящего оптимума), «MILP (настоящее)» — найденный набор, пересчитанный по полной матрице.
A: слова-полюса градиентов (good/bad, big/small, …) не кандидаты. B: допускаются, у корня-полюса одна ось «бесплатна»; `a` — бюджет полюсов-корней.

| задача | K | бюджет a | greedy | greedy+swap | MILP (настоящее) | верхняя граница | полюсов в наборе |
| :-- | --: | --: | --: | --: | --: | --: | --: |
| A | 30 | ∞ | 0.2665 | 0.2700 | 0.2161 | 10.6109 | 0 |
| A | 36 | ∞ | 0.2838 | 0.2870 | 0.2320 | 10.6109 | 0 |
| B | 30 | 0 | 0.2676 | 0.2711 | 0.2153 | 10.4977 | 0 |
| B | 30 | 2 | 0.2676 | 0.2711 | 0.2143 | 10.6751 | 0 |
| B | 30 | 4 | 0.2676 | 0.2711 | 0.2143 | 10.6751 | 0 |
| B | 30 | 8 | 0.2676 | 0.2711 | 0.2143 | 10.6751 | 0 |
| B | 30 | ∞ | 0.2676 | 0.2711 | 0.2143 | 10.6751 | 0 |
| B | 36 | ∞ | 0.2847 | 0.2891 | 0.2314 | 10.6751 | 0 |

## Наборы корней (MILP)

- **A, K=30, a=∞:** possible, tree, company, property, select, mile, depth, goal, progress, guide, commit, please, wound, softly, float, normally, height, liquor, proportion, characterize, descend, lend, found, ease, guilty, stern, certify, humorous, profess, lurid
- **A, K=36, a=∞:** possible, tree, company, property, select, mile, author, depth, goal, progress, distant, guide, hero, commit, primarily, please, wound, softly, float, normally, height, liquor, proportion, characterize, cling, descend, lend, automobile, found, ease, guilty, stern, certify, humorous, profess, lurid
- **B, K=30, a=0:** face, money, fire, religion, basis, latter, define, grass, explanation, shift, west, authority, vague, visual, gradually, recognition, loan, overall, biological, recount, sprawl, utter, grateful, spiritual, honestly, sometime, forth, academically, jointly, momentarily
- **B, K=30, a=2:** develop, world, fight, development, ride, bear, support, technique, text, detail, lung, essentially, western, fat, weather, cultural, entry, shell, sum, veteran, dig, sober, risk, perpetuate, verify, reappear, anatomical, afar, conceivably, conspicuously
- **B, K=30, a=4:** develop, world, fight, development, ride, bear, support, technique, text, detail, lung, essentially, western, fat, weather, cultural, entry, shell, sum, veteran, dig, sober, risk, perpetuate, verify, reappear, anatomical, afar, conceivably, conspicuously
- **B, K=30, a=8:** develop, world, fight, development, ride, bear, support, technique, text, detail, lung, essentially, western, fat, weather, cultural, entry, shell, sum, veteran, dig, sober, risk, perpetuate, verify, reappear, anatomical, afar, conceivably, conspicuously
- **B, K=30, a=∞:** develop, world, fight, development, ride, bear, support, technique, text, detail, lung, essentially, western, fat, weather, cultural, entry, shell, sum, veteran, dig, sober, risk, perpetuate, verify, reappear, anatomical, afar, conceivably, conspicuously
- **B, K=36, a=∞:** develop, world, fight, development, ride, bear, support, technique, text, detail, remind, lung, essentially, detergent, western, fat, leader, weather, cultural, entry, shell, sum, veteran, dig, wonderful, sober, chew, risk, perpetuate, verify, reappear, anatomical, bathe, afar, conceivably, conspicuously

Для сравнения: набор NSM из 27 корней даёт сходство 0.1970 (B-сходство) и 0.1939 (A-сходство).

## Устойчивость (бутстрап, 20 выборок по 80% слов, задача A, K=30, greedy+swap)

Среднее Жаккара между наборами: 0.17; покрытие отложенных слов: 0.2459 ± 0.0042.

Корни по частоте выбора: water (17), usually (17), amount (13), gleam (13), officer (13), depict (12), shortly (12), southward (11), request (10), certainly (10), victory (10), wonderful (9), anxiously (9), murmur (9), furiously (8), affirm (8), examine (8), reduce (8), bedroom (8), remarkably (8), earlier (7), enhance (7), perfectly (7), throw (7), suppose (7), provide (7), analyze (6), loudly (6), particular (6), think (6), hurt (6), fasten (5), quickly (5), achieve (5), strange (5), tightly (5), join (5), uphold (5), year (5), tumble (5)

## Примечание: MILP не сошёлся

Все восемь запусков MILP упёрлись в лимит 240 с. «Верхняя граница» (~10,6) бессмысленна (сходство не больше 1), а найденные MILP наборы (0,21–0,23) хуже жадного (0,27–0,28). Поэтому из таблицы надёжны только столбцы greedy и greedy+swap. Наборы корней, перечисленные выше, — это плохие решения MILP, брать их не нужно. Наборы greedy+swap в файл не записаны.
