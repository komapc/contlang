# SemAxis на наших осях (Numberbatch, 3000 слов)

Оси: 27; слов: 3001; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: нет.

## Качество полюсов (leave-one-out: слово-полюс на своей стороне оси, построенной без него)

| ось | LOO |
| :-- | --: |
| SEX | 0.30 |
| ABOVE | 0.70 |
| SIDE | 0.70 |
| LIVE | 0.80 |
| INSIDE | 0.80 |
| CAN | 0.80 |
| NEAR | 0.90 |
| SAME | 0.90 |
| MAYBE | 0.90 |
| TIME | 0.90 |
| WANT | 0.90 |
| HEAT | 0.90 |
| TOUCH | 0.90 |
| FEEL | 0.90 |
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

## Оси, похожие друг на друга (|cos| ≥ 0,35)

| ось 1 | ось 2 | cos |
| :-- | :-- | --: |
| KNOW | MAYBE | +0.39 |

## Какую долю вектора слова объясняют оси (R², средняя по словам)

- наши 27 осей: **0.136**
- случайные 27 осей (20 прогонов): 0.160 ± 0.004
- лучшие 27 направлений PCA (верхний предел для 27 измерений): 0.302

## Хуже всего объяснённые слова (R², 40 слов)

leaf (0.02), university (0.02), communist (0.03), drug (0.03), professor (0.03), doctrine (0.03), door (0.03), player (0.03), city (0.03), wagon (0.03), dinner (0.03), army (0.03), factory (0.03), film (0.03), movie (0.03), industrial (0.03), synthetic (0.03), biblical (0.03), military (0.03), tree (0.03), nuclear (0.03), wheel (0.03), convict (0.03), star (0.03), democratic (0.04), text (0.04), description (0.04), organic (0.04), politics (0.04), laboratory (0.04), barrel (0.04), naval (0.04), fish (0.04), strain (0.04), stain (0.04), crime (0.04), political (0.04), theological (0.04), survey (0.04), office (0.04)

## Слова из списка провалов (R²)

member (0.11), regime (0.10), function (0.11), union (0.08), party (0.07), committee (0.07), institution (0.06), specific (0.14), influence (0.13), protect (0.14), group (0.09), team (0.12), society (0.10), class (0.07)

## Главные направления остатка (кандидаты на недостающие оси)

**1** (доля остатка 2.6%): + fairly, remarkably, quite, reasonably, actually, plainly, practically, hardly, nicely, surprisingly, evidently, rather, similarly, sufficiently
  − give, join, bring, boost, leave, add, send, reinforce, strengthen, leadership, sway, impart, share, enhance

**2** (доля остатка 2.2%): + area, field, region, ground, center, residential, unit, middle, commercial, high, side, road, community, intense
  − deem, presume, suggest, assume, propose, imply, concede, necessitate, affirm, acknowledge, consider, suppose, insist, intend

**3** (доля остатка 1.8%): + significance, particular, subjective, attribute, fundamental, interpretation, context, implication, importance, specific, characterize, relation, unique, peculiar
  − quietly, briskly, silently, softly, gently, happily, loudly, furiously, excitedly, heave, slowly, back, angrily, down

**4** (доля остатка 1.5%): + decrease, vary, diminish, lessen, smaller, increase, reduce, dwindle, swell, minimal, larger, exceed, intense, fade
  − decision, committee, recommendation, agency, proposal, authority, officer, request, unanimously, commission, advice, mission, secretary, solemnly

**5** (доля остатка 1.4%): + beautiful, lovely, delightful, wonderful, nice, funny, brilliant, awful, fantastic, pleasant, loud, vivid, strange, magnificent
  − increase, decrease, reduce, further, growth, expand, augment, steadily, expenditure, significantly, restrict, reduction, strengthen, limit

**6** (доля остатка 1.4%): + thoughtfully, carefully, meticulously, methodically, intently, accurately, cautiously, vigorously, stiffly, coldly, softly, sharply, tightly, precise
  − probably, maybe, perhaps, anyway, anymore, someday, sometime, unfortunately, though, possibly, happen, now, anyhow, day

