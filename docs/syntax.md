# Синтаксис

## Частицы

Грамматика основана на Toki Pona и состоит из четырёх частиц. Конструкции вкладываются друг в друга.

| Частица | Роль |
| :-- | :-- |
| `LI` | маркер сказуемого |
| `E` | прямое дополнение |
| `PI` | группировка модификаторов |
| `LA` | условие / контекстная клауза |

## Слово как вызов функции

`ROOT(FEATURE=value, ...)` — корень с признаками. Признаки необязательны: пропущенный признак **не важен** (не «нейтральный 0»). Нейтральное значение нужно писать явно. См. [словарь](lexicon.md).

## Примеры

Ошибки оригинала исправлены: в таблице нет признака `VALUE` (есть `COLOR VALUE` и `GOODNESS`), а `QUANTITY=0` — это «many», а не «some».

**All humans are born free and equal.**

```
HUM(QUANTITY=5) LI BE-BORN(TENSE=-2) LA HUM PI AGENCY=5 PI IMPORTANCE=0
```

**Some people fear authority.**

```
HUM(QUANTITY=-3) LI FEAR(INTENSITY=4) E RULE(AGENCY=5)
```

**If someone acts freely, society benefits.**

```
HUM(QUANTITY=-3) LI DO(AGENCY=5, CERTAINTY=4) LA SOCIAL-LIFE LI GROW(GOODNESS=4)
```

> Конкретные числа (`QUANTITY=-3`, `IMPORTANCE=0` для «equal») — моя интерпретация, шкалы пока не откалиброваны.
