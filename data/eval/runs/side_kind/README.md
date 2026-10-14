# side_kind: KIND только головой; SIDE — убрать или переопределить

Пороги — dec.md (записаны до кодов и ответов). Кодер сайта — текущий site/math.js (без пары через PI).
`pool.js` → pool.json; `codes.js side|kind` → codes.json; `run.py readers|pairs|merge|score SCRATCH` → items.json, lists.json,
spec_kind.md, spec_noside.md, spec_side_def.md, answers/, judge/, result.txt, table.md. Атом SIDE в векторах — atoms.js → atoms.txt.
Один слепой читатель Haiku на код, судья Haiku 2/1/0 (../reader/labels.json), мера — первые ответы «близко».

| | было | стало | разница (95 %) | n | порог |
|---|--:|--:|---|--:|---|
| KIND головой (new − old) | 13 % | 20 % | +6,7 % [−2,7 … +16,0] | 75 | не пройден |
| — повтор 65 слов из ../kind | 15 % | 22 % | +6,2 % [−4,6 … +16,9] | 65 | |
| — новые слова | 0 % | 10 % | +10 % [0 … +30] | 10 | |
| SIDE убрать (R − O) | 14 % | 12 % | −2,1 % [−8,5 … +3,5] | 141 | пройден (≥ −5 %, > −15 %) |
| SIDE переопределить (D − O) | 14 % | 18 % | +4,3 % [−0,7 … +9,2] | 141 | не пройден |
| D − R | 12 % | 18 % | +6,4 % [−0,7 … +13,5] | 141 | |

**KIND.** Прежние +15 % у KIND-головы (отбор после чтения) не повторились: +6 %, ноль внутри интервала. Новых слов, где KIND встаёт
головой, почти нет (10 из 389 добавленных), значит корень покрывает узкий круг: sample, instance, type, style, lesson, norm.
Выигрыши: demonstration, instance, lesson, style, type, norm; потери: photograph → sketch, image → view, procedure → ruling.

**SIDE.** По правилу ../adopt SIDE можно убрать: без него −2 % (в шуме). Новое определение по атому
(`-5 back, behind, backward; also going back, return … +5 front, ahead, forward; also coming up, ready`) даёт +4 % [−0,7 … +9,2],
чуть ниже порога; против удаления +6 % [−0,7 … +13,5]. Выигрыши D: obstacle, returned → revert, opposes → refuse, recovering, evolution →
progress, bend, collision; потери: head → skin, drafting, ball. Без SIDE теряются rear, backward, reverse, restored, restoring, past,
rebuilding (слова «назад, вернуть»): это и есть то, что атом несёт.

У слов без SIDE запрет корня код не меняет (проверено на 100 словах ../big1000: 0 изменений).
SIDE стоит примерно в 6 % кодов (141 из 2426), поэтому на мере по словарю любой из вариантов — меньше 1 %.
Удаление касается и рецептов модели (стороны света, leader); этот тест — только кодер сайта.
