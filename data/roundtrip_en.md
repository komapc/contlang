# Round-trip: слово → k осей (11 уровней) → ближайшее другое слово

3000 слов (1500 train, 600 test), кандидаты — все 3000. Ожидание — не то же слово, а близкое по смыслу и форме.

- **cos** — косинус реконструкции с оригиналом (полное пространство);
- **top10 / top50** — найденное слово среди 10 / 50 истинных соседей оригинала;
- **wup** — WordNet Wu-Palmer между оригиналом и найденным (только пары одной части речи); ориентиры: истинный ближайший сосед и случайное слово той же части речи;
- **pos** — часть речи найденного слова совпала (базовый уровень 33%).

## glove100

Ориентиры wup: истинный сосед 0.458, случайное слово той же части речи 0.344; pos у истинного соседа 70%.

| k | метод | cos | top10 | top50 | wup | pos |
| --: | :-- | --: | --: | --: | --: | --: |
| 10 | pca | 0.69 | 44% | 82% | 0.392 | 54% |
| 10 | random | 0.55 | 6% | 28% | 0.384 | 25% |
| 30 | pca | 0.83 | 89% | 100% | 0.426 | 66% |
| 30 | random | 0.67 | 29% | 59% | 0.401 | 51% |
| 100 | pca | 0.99 | 100% | 100% | 0.450 | 71% |
| 100 | random | 0.99 | 100% | 100% | 0.454 | 71% |

## numberbatch

Ориентиры wup: истинный сосед 0.513, случайное слово той же части речи 0.336; pos у истинного соседа 72%.

| k | метод | cos | top10 | top50 | wup | pos |
| --: | :-- | --: | --: | --: | --: | --: |
| 10 | pca | 0.39 | 24% | 49% | 0.390 | 67% |
| 10 | random | 0.26 | 7% | 16% | 0.339 | 36% |
| 30 | pca | 0.54 | 68% | 88% | 0.445 | 79% |
| 30 | random | 0.36 | 38% | 52% | 0.438 | 51% |
| 100 | pca | 0.77 | 98% | 100% | 0.505 | 78% |
| 100 | random | 0.59 | 96% | 99% | 0.504 | 71% |

## Примеры (слово → найденное слово)

**glove100, k=10:** exert → diminish; twist → kind; build → help; pretty → quite; worst → fear; bake → wrap; sea → along; affirm → hesitate; flap → nose; critical → particular; true → fact; capacity → increase; steady → far; point → time; antibody → measurement; possibly → though; indefinite → decision; fall → again; load → cost; absurd → obvious; prompt → push; stomach → suddenly; clamor → diminish; follow → sure

**glove100, k=30:** exert → diminish; twist → odd; build → expand; pretty → quite; worst → worse; bake → wrap; sea → near; affirm → uphold; flap → nose; critical → response; true → indeed; capacity → increase; steady → low; point → edge; antibody → therapeutic; possibly → though; indefinite → halt; fall → rise; load → amount; absurd → silly; prompt → immediate; stomach → chest; clamor → shudder; follow → come

**numberbatch, k=10:** exert → sustain; twist → throw; build → achieve; pretty → quite; worst → incredible; bake → pull; sea → big; affirm → endorse; flap → down; critical → extensive; true → truly; capacity → greater; steady → steadily; point → amount; antibody → form; possibly → surely; indefinite → significant; fall → off; load → amount; absurd → incredible; prompt → undertake; stomach → slowly; clamor → groan; follow → initiate

**numberbatch, k=30:** exert → sustain; twist → pull; build → construct; pretty → quite; worst → terrible; bake → spend; sea → distant; affirm → assert; flap → heave; critical → important; true → absolute; capacity → ability; steady → vigorous; point → goal; antibody → initial; possibly → perhaps; indefinite → vague; fall → tumble; load → amount; absurd → incredible; prompt → necessitate; stomach → nervous; clamor → groan; follow → proceed
