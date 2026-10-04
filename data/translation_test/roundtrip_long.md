# LONG (длинный предмет) и индикатор абстрактности: слепые тесты

## LONG: 20 слов × 2 кодировщика, 2 декодера

Ось: −5 нить, верёвка, волос … 0 палочка, прут … +5 столб, бревно, балка. Слово названо лучшим или среди двух альтернатив: **32 из 40 (80%)**; A 18 из 20, B 14 из 20.

Хорошо: *stick, pole, rope, thread, hair, branch, tail, pipe, beam, long, tall, pillar* (оба). Знак оси не перепутан ни разу (нить −3…−5, шест +4, столб +5, палка 0…+1).
Промахи: *wire → needle*, *rod → spear*, *string → chain*, *tube → bone / bottle*, *tower → road* (B); *needle → nail*, *pencil → pen* (рядом).

## Индикатор абстрактности `ABSTRACT(=+3…+5)` у абстрактных существительных

20 слов (*freedom, justice, violence, need, identity, equality, situation, struggle, guarantee, knowledge, belief, danger, peace, honor, fear, memory, growth, power, reason, courage*) × 2 условия × 2 кодировщика.

| условие | A | B | всего |
| :-- | :-- | :-- | :-- |
| без правила | 12 | 14 | 26 из 40 |
| с правилом «обязательно ABSTRACT» | 10 | 11 | 21 из 40 |

Без правила кодировщики **и так** ставили `ABSTRACT` в 39 из 40 абстрактных слов (спецификация уже описывает корень), так что сравнение не чистое: правило ничего нового не добавило, а разница 26 против 21 в пределах шума. Минус индикатора: он занимает один из трёх корней (*justice* = `RULE SAME ABSTRACT` читается как *equality*, место для «справедливый / должный» не осталось).
Типичные промахи не связаны с абстрактностью: *fear → sadness / suffering* (нет оси «опасность / угроза»), *need → hope / ambition*, *courage → sensitivity / comfort*, *guarantee → education* (`GIVE KNOW`), *justice → equality*.
