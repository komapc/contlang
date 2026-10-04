# SemAxis на наших осях (Numberbatch, 3000 слов)

Оси: 31; слов: 3001; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: нет.

## Качество полюсов (leave-one-out: слово-полюс на своей стороне оси, построенной без него)

| ось | LOO |
| :-- | --: |
| ABOVE | 0.70 |
| SIDE | 0.70 |
| LIVE | 0.80 |
| INSIDE | 0.80 |
| SEX | 0.80 |
| CAN | 0.80 |
| NEAR | 0.90 |
| SAME | 0.90 |
| MAYBE | 0.90 |
| TIME | 0.90 |
| WANT | 0.90 |
| HEAT | 0.90 |
| TOUCH | 0.90 |
| FEEL | 0.90 |
| RULE | 0.90 |
| PARTICULAR | 0.90 |
| GOOD | 1.00 |
| BIG | 1.00 |
| PART | 1.00 |
| KNOW | 1.00 |
| BEGIN | 1.00 |
| GIVE | 1.00 |
| MATTER | 1.00 |
| HAPPEN | 1.00 |
| THINK | 1.00 |
| MANY | 1.00 |
| SOMEONE | 1.00 |
| THING | 1.00 |
| MOVE | 1.00 |
| CHANGE | 1.00 |
| ART | 1.00 |

## Оси, похожие друг на друга (|cos| ≥ 0,35)

| ось 1 | ось 2 | cos |
| :-- | :-- | --: |
| KNOW | MAYBE | +0.39 |

## Какую долю вектора слова объясняют оси (R², средняя по словам)

- наши 31 осей: **0.158**
- случайные 31 осей (20 прогонов): 0.178 ± 0.006
- лучшие 31 направлений PCA (верхний предел для 31 измерений): 0.330

## Хуже всего объяснённые слова (R², 40 слов)

leaf (0.03), university (0.03), wagon (0.04), professor (0.04), player (0.04), tree (0.04), dinner (0.04), barrel (0.04), door (0.04), theological (0.04), convict (0.04), organic (0.04), communist (0.05), synthetic (0.05), fish (0.05), survey (0.05), drug (0.05), star (0.05), political (0.05), jewish (0.05), cancer (0.05), conjugate (0.05), word (0.05), film (0.05), tumor (0.05), psychologist (0.05), hair (0.05), truck (0.05), bellow (0.05), club (0.05), biblical (0.05), forest (0.05), whisky (0.05), credit (0.05), kitchen (0.05), bar (0.05), loan (0.05), series (0.05), radio (0.05), doctrine (0.05)

## Слова из списка провалов (R²)

member (0.12), regime (0.14), function (0.16), union (0.14), party (0.08), committee (0.35), institution (0.09), specific (0.30), influence (0.19), protect (0.14), group (0.10), team (0.14), society (0.13), class (0.09)

## Главные направления остатка (кандидаты на недостающие оси)

**1** (доля остатка 2.6%): + leave, join, give, send, bring, add, boost, check, register, safety, share, bury, contact, impart
  − fairly, actually, quite, plainly, reasonably, remarkably, hardly, practically, rather, evidently, nicely, apparently, indeed, surprisingly

**2** (доля остатка 2.2%): + deem, presume, assume, suggest, insist, propose, concede, oblige, affirm, necessitate, acknowledge, intend, imply, accept
  − area, region, field, color, whole, intensity, unit, style, commercial, center, height, development, process, middle

**3** (доля остатка 1.8%): + softly, briskly, quietly, gently, down, silently, slowly, heave, off, lurch, loudly, back, roar, rearward
  − significance, implication, fundamental, principle, interpretation, importance, attribute, subjective, essential, regard, assumption, context, relation, concept

**4** (доля остатка 1.5%): + decrease, increase, diminish, lessen, reduce, dwindle, vary, minimal, smaller, dilute, exceed, minimum, greater, swell
  − politely, privately, solemnly, sincerely, angrily, thoughtfully, calmly, triumphantly, heartily, comrade, openly, request, interview, congratulate

**5** (доля остатка 1.4%): + probably, maybe, perhaps, happen, someday, anyway, anymore, unfortunately, sometime, thing, though, now, possibly, anyhow
  − thoughtfully, carefully, vigorously, cautiously, intently, methodically, stiffly, meticulously, sharply, softly, gently, accurately, coldly, tightly

**6** (доля остатка 1.4%): + beautiful, loud, nice, lovely, pretty, funny, wonderful, delightful, awful, brilliant, pleasant, scream, vivid, fantastic
  − further, increase, steadily, expenditure, subsequently, decrease, thereafter, expand, restrict, advance, while, farther, meanwhile, augment

