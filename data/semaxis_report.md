# SemAxis на наших осях (Numberbatch, 3000 слов)

Оси: 40; слов: 3001; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: нет.

## Качество полюсов (leave-one-out: слово-полюс на своей стороне оси, построенной без него)

| ось | LOO |
| :-- | --: |
| ABOVE | 0.70 |
| SIDE | 0.70 |
| CONSUME | 0.73 |
| LIVE | 0.80 |
| INSIDE | 0.80 |
| SEX | 0.80 |
| CAN | 0.80 |
| VALUE | 0.80 |
| MEASURE | 0.88 |
| NEAR | 0.90 |
| SAME | 0.90 |
| TIME | 0.90 |
| WANT | 0.90 |
| HEAT | 0.90 |
| FEEL | 0.90 |
| RULE | 0.90 |
| PARTICULAR | 0.90 |
| CARE | 0.92 |
| GRAIN | 0.93 |
| SAY | 0.94 |
| LONG | 0.94 |
| GOOD | 1.00 |
| BIG | 1.00 |
| PART | 1.00 |
| KNOW | 1.00 |
| BEGIN | 1.00 |
| GIVE | 1.00 |
| TOUCH | 1.00 |
| MATTER | 1.00 |
| HAPPEN | 1.00 |
| THINK | 1.00 |
| MANY | 1.00 |
| SOMEONE | 1.00 |
| THING | 1.00 |
| MOVE | 1.00 |
| CHANGE | 1.00 |
| ART | 1.00 |
| JOIN | 1.00 |
| TONE | 1.00 |
| ABSTRACT | 1.00 |

## Оси, похожие друг на друга (|cos| ≥ 0,35)

| ось 1 | ось 2 | cos |
| :-- | :-- | --: |
| GRAIN | MATTER | -0.44 |
| SAY | FEEL | +0.41 |

## Какую долю вектора слова объясняют оси (R², средняя по словам)

- наши 40 осей: **0.201**
- случайные 40 осей (20 прогонов): 0.224 ± 0.004
- лучшие 40 направлений PCA (верхний предел для 40 измерений): 0.387

## Хуже всего объяснённые слова (R², 40 слов)

player (0.05), professor (0.05), chapter (0.06), convict (0.06), university (0.06), interview (0.06), communist (0.06), game (0.07), movie (0.07), commercial (0.07), forest (0.07), political (0.07), lunar (0.07), queen (0.07), baseball (0.07), radio (0.07), crime (0.07), threat (0.07), marriage (0.07), slave (0.07), land (0.07), tumor (0.07), cancer (0.07), dictionary (0.08), film (0.08), king (0.08), news (0.08), nineteenth (0.08), military (0.08), politics (0.08), irish (0.08), ace (0.08), arrow (0.08), valley (0.08), war (0.08), naked (0.08), rifle (0.08), city (0.08), dollar (0.08), shell (0.08)

## Слова из списка провалов (R²)

member (0.16), regime (0.17), function (0.21), union (0.22), party (0.14), committee (0.41), institution (0.13), specific (0.33), influence (0.22), protect (0.16), group (0.30), team (0.23), society (0.18), class (0.11)

## Главные направления остатка (кандидаты на недостающие оси)

**1** (доля остатка 2.8%): + leave, financial, arrest, give, withhold, relinquish, earn, seek, mental, leadership, uphold, share, explore, hire
  − fairly, quite, actually, plainly, remarkably, evidently, nicely, indeed, similarly, obviously, hardly, certainly, apparently, rather

**2** (доля остатка 2.2%): + insist, deem, concede, declare, presume, assume, assure, suggest, necessitate, affirm, denounce, remind, assert, plead
  − area, region, community, field, aspect, development, whole, atmosphere, style, process, group, density, local, history

**3** (доля остатка 1.6%): + calmly, angrily, quietly, silently, hastily, excitedly, politely, coolly, heartily, softly, eagerly, gently, furiously, nervously
  − typical, significant, contain, typically, minimal, vary, equate, denote, include, certain, comprise, comparable, entail, occur

**4** (доля остатка 1.5%): + increase, upward, decrease, dwindle, steadily, expand, widen, reduce, stretch, grow, push, down, rise, boost
  − wonderful, representative, delightful, competent, proper, lovely, homely, peculiar, strange, responsible, authentic, honest, unfortunate, genuine

**5** (доля остатка 1.4%): + indirectly, specifically, pursuant, pertain, further, relation, accordingly, reference, refer, consult, information, specific, inquire, directly
  − beautiful, nice, pretty, lovely, wonderful, pleasant, awful, delightful, fantastic, terrible, incredible, brilliant, tough, handsome

**6** (доля остатка 1.4%): + efficient, competent, financially, severely, injure, protect, healthy, sturdy, strengthen, secure, enhance, self, capable, economical
  − sometime, earlier, reappear, after, before, later, latter, emerge, previous, await, occur, wait, happen, precede

