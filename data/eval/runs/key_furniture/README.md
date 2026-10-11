# key и furniture: слепой тест вариантов из одного и двух слов

Кандидаты: 2 кодировщика Haiku (enc_A.md, enc_B.md: по 4 кода из одного слова и 4 из двух через `PI`) + варианты автора (рецепт key, `INSIDE LONG DO`, `INSIDE BIG(=-4) DO`, «вещи дома» через рецепт house) — по 14 на слово.
Листы (make.py): на каждом один вариант key, один вариант furniture и 8 наполнителей — проверенных рецептов (book, brush, car, hammer, kitchen, knife, ladder, library, machine, mountain).
Декодеры Haiku по 2 на лист, видят только spec_task_dec.md (спецификация без рецептов) и лист. Подсчёт — score.py, результат — score.md.

Первый прогон (run1_path_leak/) испорчен: листы лежали в папке `key_furniture`, и декодер сам написал, что угадал по имени папки. Повторён из папки с нейтральным именем; ниже — только чистый прогон.

## Итог (первым из 2)

- **furniture решается**: `PART(=+5) THING(=-5) | o PI PLACE INSIDE(=+5) LIVE | o` («набор неживых вещей дома», второе слово — рецепт house) 2/2;
  `PART(=+5) THING(=-5) | o PI INSIDE(=+5) PLACE | o` 2/2; одним словом `PART(=+5) THING(=-5) MOVE(=-5) | o` («неподвижные вещи») 2/2.
  Без второго слова почти всё мимо: contents, equipment, skeleton, container, stones.
- **key не решается ни одним из 14 вариантов** (0/28, в тройке тоже 0): «орудие разъединения» читается как scissors / saw / hacksaw,
  «маленький твёрдый» — как pill / nail / chip, «внутрь + орудие» — как needle / container, `RULE` — как seal / gavel. Рецепт `INSIDE(=+4) CAN(=+4) DO(=+5)` — container / engine.
- Наполнители (контроль): 143 из 224 первым.

## По смысловой близости (sem.py → sem.md)

Не «угадано ли слово», а cos ответа декодера со словом в полном Numberbatch. Ориентиры: key — lock 0,48, door 0,35, tool 0,25, pliers 0,21, scissors 0,14, needle 0,05; furniture — chair 0,47, timber 0,38, equipment 0,33, contents 0,12.
key: лучший вариант 0,18 (pliers / staple remover), остальные 0,03–0,14 — ответы из семейства «орудие», но не рядом с ключом (ни lock, ни door не назван ни разу).
furniture: 4 варианта 1,00 (слово названо), одним словом с `DO(=+5)` — equipment 0,33, с `LONG(=+5)` — timber / lumber 0,39.
