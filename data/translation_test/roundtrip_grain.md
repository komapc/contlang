# GRAIN: слепой круговой тест (12 слов, 2 кодировщика, 2 декодера)

Слова: sand, flour, dust, honey, gravel, rice, mud, ingot, boulder, seamless, continuous, granular. Кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер только таблицы и правила чтения, оригиналов не видит. Модель: sonnet (субагенты), по одному декодеру на набор.

| | без GRAIN (45→44 корня) | с GRAIN |
| :-- | :-- | :-- |
| точно (лучшее слово = оригинал) | 3 из 24 (mud, gravel, boulder) | 7 из 24 (sand ×2, dust ×2, boulder ×2, continuous ×1) |
| оригинал среди трёх ответов | 4 из 24 | 14 из 24 |

Что получилось. Слова, у которых суть в связности (sand, dust, continuous, boulder), собираются; `GRAIN(=0)` у sand, flour, dust, rice, gravel одинаков, различает их соседний корень (PART, THING, CONSUME). *continuous* = `GRAIN(=+5) TIME | a A0` декодирован верно в одном наборе из двух (в другом без `A0`: *permanent*). Ошибка *seamless* = `GRAIN(=+5) JOIN(=-5)`: `JOIN(=-5)` значит «отделить», декодер прочёл *separate*; для «без швов» брать `GRAIN(=+5)` без `JOIN`.

Оговорки: выборка 12 слов, 2 кодировщика, 1 декодер на набор; слова выбраны под ось; шум порядка ±3 слов.
