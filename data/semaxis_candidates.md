# Кандидаты в новые оси (SemAxis, Numberbatch)

База: 27 осей, средняя R² 0.1360. Одна случайная ось добавляет +0.0061 ± 0.0013.

| кандидат | ΔR² (все слова) | ΔR² (слова-провалы) | в разах от случайной |
| :-- | --: | --: | --: |
| CHANGE_dir | +0.0052 | +0.0032 | 0.8× |
| CHANGE_any | +0.0066 | +0.0056 | 1.1× |
| AUTHORITY | +0.0055 | +0.0316 | 0.9× |
| PARTICULAR | +0.0055 | +0.0147 | 0.9× |

Все четыре вместе: ΔR² +0.0225 (все слова), +0.0520 (слова-провалы).

## Координаты слов на новых осях (косинус)

| слово | CHANGE_dir | CHANGE_any | AUTHORITY | PARTICULAR |
| :-- | --: | --: | --: | --: |
| member | +0.04 | -0.06 | +0.09 | -0.01 |
| regime | -0.04 | +0.00 | +0.19 | -0.08 |
| function | -0.03 | +0.04 | +0.07 | +0.05 |
| union | +0.01 | -0.01 | +0.18 | -0.13 |
| party | -0.08 | +0.04 | -0.00 | -0.03 |
| committee | +0.02 | -0.00 | +0.53 | -0.05 |
| institution | +0.01 | -0.05 | +0.15 | +0.08 |
| specific | +0.03 | +0.14 | -0.18 | +0.38 |
| influence | +0.07 | +0.21 | +0.11 | +0.06 |
| protect | +0.05 | +0.00 | -0.02 | +0.03 |
| group | +0.02 | +0.02 | +0.06 | +0.00 |
| team | +0.05 | -0.04 | +0.06 | +0.04 |
| society | +0.02 | +0.01 | +0.11 | -0.09 |
| class | -0.03 | +0.06 | -0.14 | -0.03 |
| increase | +0.22 | +0.14 | +0.04 | -0.03 |
| decrease | -0.31 | +0.15 | +0.03 | -0.09 |
| committee | +0.02 | -0.00 | +0.53 | -0.05 |
| authority | +0.12 | +0.07 | +0.50 | -0.02 |
| specific | +0.03 | +0.14 | -0.18 | +0.38 |
| general | -0.04 | -0.00 | +0.04 | -0.33 |
| change | +0.06 | +0.56 | -0.04 | +0.08 |
| stay | +0.05 | -0.45 | -0.03 | +0.05 |

**CHANGE_dir** — больше всего выигрывают: expand (+0.15), improve (+0.14), fall (+0.13), develop (+0.12), grow (+0.12), broaden (+0.10), enhance (+0.10), strengthen (+0.09), drop (+0.09), augment (+0.08), build (+0.08), amend (+0.08), extend (+0.08), decline (+0.07), widen (+0.07), enlarge (+0.07), improvement (+0.07), flourish (+0.07), exploit (+0.06), shrink (+0.06), better (+0.06), decrease (+0.06), establish (+0.05), raise (+0.05), reinforce (+0.05)
  слова-провалы: member +0.00, regime +0.01, function +0.00, union +0.00, party +0.01, committee +0.00, institution +0.00, specific +0.00, influence +0.01, protect +0.00, group +0.00, team +0.00, society +0.00, class +0.01
**CHANGE_any** — больше всего выигрывают: alter (+0.36), change (+0.36), transform (+0.32), modify (+0.29), shift (+0.19), vary (+0.16), convert (+0.15), amend (+0.14), remain (+0.14), revise (+0.13), adjust (+0.12), stay (+0.12), stable (+0.12), translate (+0.11), radically (+0.11), variation (+0.10), adapt (+0.10), differ (+0.10), steady (+0.10), difference (+0.09), replace (+0.09), affect (+0.09), persistent (+0.09), different (+0.08), differently (+0.08)
  слова-провалы: member +0.00, regime +0.00, function +0.01, union +0.00, party +0.00, committee +0.00, institution +0.00, specific +0.02, influence +0.04, protect +0.00, group +0.00, team +0.00, society +0.00, class +0.00
**AUTHORITY** — больше всего выигрывают: commission (+0.34), personal (+0.27), committee (+0.27), authority (+0.23), private (+0.19), agency (+0.19), individual (+0.17), government (+0.17), intimate (+0.16), department (+0.15), congress (+0.13), secretary (+0.11), unanimously (+0.10), board (+0.10), director (+0.09), chief (+0.09), federal (+0.08), president (+0.08), approval (+0.08), recommendation (+0.08), legislative (+0.07), individually (+0.07), approve (+0.07), chair (+0.07), privately (+0.06)
  слова-провалы: member +0.01, regime +0.04, function +0.00, union +0.03, party +0.00, committee +0.27, institution +0.02, specific +0.03, influence +0.01, protect +0.00, group +0.00, team +0.00, society +0.01, class +0.02
**PARTICULAR** — больше всего выигрывают: unique (+0.25), peculiar (+0.22), particular (+0.19), uniquely (+0.18), distinct (+0.17), distinctive (+0.14), specific (+0.13), special (+0.12), unusual (+0.12), universal (+0.12), odd (+0.11), strange (+0.10), remarkable (+0.10), peculiarly (+0.09), general (+0.09), extraordinary (+0.09), specially (+0.08), meticulously (+0.08), precisely (+0.07), exact (+0.07), identical (+0.07), weird (+0.07), distinctly (+0.07), individually (+0.07), precise (+0.06)
  слова-провалы: member +0.00, regime +0.01, function +0.00, union +0.03, party +0.01, committee +0.01, institution +0.00, specific +0.13, influence +0.00, protect +0.00, group +0.00, team +0.00, society +0.02, class +0.00

## Сколько слов реально выигрывают

| кандидат | слов с ΔR² > 0,05 | слов с ΔR² > 0,10 | макс. |cos| с нашими осями |
| :-- | --: | --: | :-- |
| CHANGE_dir (уменьшить … увеличить) | 25 | 7 | 0,45 (ABOVE) |
| CHANGE_any (остаться … изменить) | 46 | 18 | 0,28 (MOVE) |
| AUTHORITY (личное … официальное) | 34 | 14 | 0,12 (MANY) |
| PARTICULAR (общее … особое) | 37 | 13 | 0,27 (SAME) |

cos между CHANGE_dir и CHANGE_any: 0,02 (это две разные оси).
