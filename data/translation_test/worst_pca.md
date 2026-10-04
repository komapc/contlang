# Где хуже всего: остаточный PCA и слова, которые не угадываются

Оси (39 вместе с MEASURE, LONG) объясняют R² ≈ 0,20 дисперсии словаря (случайные оси ≈ 0,2, PCA ≈ 0,36). Слова из теста на 100 слов (8 прогонов) разделены по числу угаданных: 0–1 из 8 (39+ слов, «плохие») против 5+ из 8 («хорошие»).

**Остаточная норма слова не предсказывает провал**: 0,90 у плохих и 0,89 у хороших, то есть «непонятость» эмбеддингом не связана с тем, что код не читается. Узкое место — выбор различений, а не общее разрешение.

Направления остатка, на которых лежат плохие слова (ближайшие слова словаря вдоль них):

| направление | слова словаря | плохие слова теста | кандидат |
| :-- | :-- | :-- | :-- |
| громкий голос, шум ↔ тихий | whistle, shrill, groan, wail, roar, scream, noise, murmur, buzz | whistled, groan(ing), buzz, sound, hear | ось на `SAY` (громко … тихо) |
| предел, граница ↔ неопределённость | finite, indefinite, restrict, confine, holder, uncertain | finite, indefinite, holder | корень `LIMIT` или ось |
| смелость, дерзость ↔ робость | bold, brave, dare, alert, afraid, honest, vivid | bold, afraid, alert, courage | ось на `FEEL` или `WANT` |
| манера, способ, стиль | manner, way, style, fashion, pattern, domestic | manner, fashion, nature, way | корень `METHOD` (уже обсуждали) |
| суждение: решить, оценить | determine, decide, evaluate, weigh, certify, assess | determine, certify, admit, speculate | уже есть `THINK`, нужен рецепт |
