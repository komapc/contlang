# SemAxis на наших осях (Numberbatch, 3000 слов)

Оси: 34; слов: 3001; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: нет.

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
| VALUE | 0.91 |
| CARE | 0.92 |
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
| JOIN | 1.00 |
| ART | 1.00 |

## Оси, похожие друг на друга (|cos| ≥ 0,35)

| ось 1 | ось 2 | cos |
| :-- | :-- | --: |
| KNOW | MAYBE | +0.39 |

## Какую долю вектора слова объясняют оси (R², средняя по словам)

- наши 34 осей: **0.172**
- случайные 34 осей (20 прогонов): 0.195 ± 0.005
- лучшие 34 направлений PCA (верхний предел для 34 измерений): 0.350

## Хуже всего объяснённые слова (R², 40 слов)

leaf (0.04), university (0.04), wagon (0.04), professor (0.04), barrel (0.04), player (0.04), tree (0.04), synthetic (0.05), fish (0.05), theological (0.05), door (0.05), cancer (0.05), convict (0.05), film (0.05), drug (0.05), conjugate (0.05), whisky (0.05), forest (0.05), credit (0.05), tumor (0.06), movie (0.06), truck (0.06), stain (0.06), political (0.06), wing (0.06), store (0.06), star (0.06), chapter (0.06), series (0.06), text (0.06), word (0.06), oath (0.06), commercial (0.06), hair (0.06), loan (0.06), ear (0.06), interview (0.06), organic (0.06), avocado (0.06), strain (0.06)

## Слова из списка провалов (R²)

member (0.15), regime (0.15), function (0.16), union (0.19), party (0.10), committee (0.35), institution (0.09), specific (0.30), influence (0.20), protect (0.15), group (0.12), team (0.15), society (0.15), class (0.09)

## Главные направления остатка (кандидаты на недостающие оси)

**1** (доля остатка 2.7%): + fairly, actually, quite, plainly, remarkably, hardly, reasonably, practically, similarly, evidently, rather, indeed, surprisingly, simply
  − leave, give, safety, financial, check, send, leadership, boost, register, tax, share, bring, bury, cultural

**2** (доля остатка 2.2%): + area, field, region, whole, color, style, community, system, intensity, center, ground, development, commercial, industrial
  − deem, assume, presume, insist, suggest, concede, propose, affirm, necessitate, acknowledge, ask, intend, oblige, allow

**3** (доля остатка 1.8%): + implication, significance, principle, fundamental, attribute, assumption, interpretation, reason, relation, subjective, context, essential, concept, regard
  − softly, gently, quietly, briskly, silently, slowly, loudly, nervously, excitedly, sharply, down, furiously, angrily, heave

**4** (доля остатка 1.6%): + decrease, increase, diminish, lessen, reduce, vary, dwindle, minimal, dilute, smaller, swell, exceed, intensity, greater
  − privately, politely, request, decision, comrade, interview, solemnly, sincerely, publicly, openly, angrily, promptly, heartily, congratulate

**5** (доля остатка 1.4%): + further, steadily, increase, expand, augment, actively, restrict, broaden, growth, decrease, cautiously, indirectly, strengthen, significantly
  − beautiful, nice, lovely, wonderful, pretty, delightful, loud, awful, funny, fantastic, pleasant, terrible, brilliant, scream

**6** (доля остатка 1.3%): + harshly, vigorously, thoughtfully, savagely, stiffly, severely, tightly, violently, efficient, solemnly, coldly, strengthen, rigid, enforce
  − sometime, now, probably, maybe, latter, though, happen, anyway, perhaps, come, after, expect, day, wait

