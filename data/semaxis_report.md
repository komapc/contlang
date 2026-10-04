# SemAxis на наших осях (Numberbatch, 3000 слов)

Оси: 35; слов: 3001; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: нет.

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
| TONE | 1.00 |
| ART | 1.00 |

## Оси, похожие друг на друга (|cos| ≥ 0,35)

| ось 1 | ось 2 | cos |
| :-- | :-- | --: |
| KNOW | MAYBE | +0.39 |
| TONE | TOUCH | -0.39 |

## Какую долю вектора слова объясняют оси (R², средняя по словам)

- наши 35 осей: **0.177**
- случайные 35 осей (20 прогонов): 0.199 ± 0.004
- лучшие 35 направлений PCA (верхний предел для 35 измерений): 0.356

## Хуже всего объяснённые слова (R², 40 слов)

leaf (0.04), university (0.04), barrel (0.04), player (0.04), professor (0.04), tree (0.04), wagon (0.05), door (0.05), theological (0.05), fish (0.05), convict (0.05), cancer (0.05), drug (0.05), film (0.05), forest (0.05), tumor (0.06), synthetic (0.06), wing (0.06), conjugate (0.06), series (0.06), stain (0.06), whisky (0.06), movie (0.06), word (0.06), store (0.06), chapter (0.06), hair (0.06), oath (0.06), text (0.06), truck (0.06), legal (0.06), interview (0.06), kitchen (0.06), strain (0.06), political (0.06), star (0.06), avocado (0.06), ear (0.06), dinner (0.06), grin (0.06)

## Слова из списка провалов (R²)

member (0.15), regime (0.15), function (0.16), union (0.20), party (0.10), committee (0.36), institution (0.09), specific (0.31), influence (0.20), protect (0.15), group (0.12), team (0.17), society (0.16), class (0.09)

## Главные направления остатка (кандидаты на недостающие оси)

**1** (доля остатка 2.7%): + fairly, actually, quite, plainly, hardly, remarkably, reasonably, similarly, practically, evidently, rather, indeed, surprisingly, simply
  − leave, safety, financial, give, check, send, leadership, tax, boost, register, share, cultural, top, control

**2** (доля остатка 2.2%): + area, field, region, community, whole, style, way, mid, middle, center, development, group, color, atmosphere
  − deem, insist, assume, presume, suggest, concede, propose, affirm, necessitate, consider, assert, deny, ask, imply

**3** (доля остатка 1.8%): + implication, significance, principle, attribute, assumption, fundamental, interpretation, relation, reason, context, concept, particular, subjective, theory
  − softly, quietly, gently, silently, briskly, loudly, slowly, nervously, angrily, sharply, furiously, excitedly, down, calmly

**4** (доля остатка 1.6%): + decrease, increase, diminish, lessen, reduce, vary, dwindle, minimal, smaller, dilute, greater, swell, exceed, intensity
  − privately, politely, angrily, request, solemnly, decision, openly, publicly, calmly, interview, hastily, comrade, triumphantly, thoughtfully

**5** (доля остатка 1.4%): + further, steadily, expand, increase, cautiously, actively, restrict, indirectly, augment, broaden, strengthen, growth, decrease, vigorously
  − beautiful, nice, lovely, wonderful, delightful, pretty, awful, fantastic, pleasant, funny, terrible, loud, brilliant, weird

**6** (доля остатка 1.3%): + competent, efficient, financially, capable, protect, severely, healthy, economical, sturdy, skilled, effective, injure, comfortable, secure
  − earlier, precede, reappear, latter, before, after, previous, indicate, later, occur, sometime, emerge, appear, thereafter

