# Туда и обратно: вся статья Republic (Wikipedia, 318 предложений)

Текст: https://en.wikipedia.org/w/api.php (explaintext), без разделов «See also», ссылок и литературы; 318 предложений, около 7 100 слов.
Процедура: 10 кодировщиков (sonnet) по ~32 предложения, каждый видел только инструкцию (спецификация корней, формы и фраз, около 5 тыс. символов) и свою часть; 10 декодеров (sonnet), которые видели только спецификацию и коды (строки `MISSING:` с английскими словами убраны); 10 оценщиков (sonnet), которые сравнивали оригинал с декодированным предложением. Шкала: 3 — тот же смысл, 2 — основная мысль сохранена, деталь потеряна или искажена, 1 — связано только по теме или ключевое утверждение неверно, 0 — не связано.

## Итог

| оценка | предложений | доля |
| :-- | --: | --: |
| 3 | 47 | 15% |
| 2 | 118 | 37% |
| 1 | 141 | 44% |
| 0 | 12 | 4% |

Средняя оценка 1,63 из 3. Основная мысль сохранена (оценка 2–3) в 52% предложений. Длина предложения почти не влияет (короткие 1,55, длинные 1,46, средние 1,6–1,7).

По разделам (средняя): лучше всего *Original meaning* 2,5, *Icelandic Commonwealth* 2,25, *Decolonization* 2,25, *Classical republics* 1,94, *Liberal republics* 1,89, *United States* 1,84; хуже всего *Elections* 0,9, *Ambiguities* 1,17, *Indian subcontinent* 1,25, *Mercantile republics* 1,4 (много специальных терминов, цепочек «кто что кому сделал» и институтов).

## Что потеряно

Чаще всего в замечаниях оценщиков: «lost» (120), «garbled» (51), «vague» (44). Типичные потери: институты и их отношения (парламент избирает президента, суды, законодательная власть), различие монархия / республика / империя / феодальное государство, причины и следствия, степени («номинально», «в основном»).

Кодировщики сами перечислили, что не смогли закодировать (`MISSING:`): *republic, monarchy* (в 9 частях из 10), *constitution* (8), *sovereign / sovereignty* (6), *citizen, democracy, aristocracy, assembly, parliament, revolution, election, empire, colony* (3–4 раза каждое), далее *feudal, noble, guild, charter, ideology, legitimacy, president, referendum*.

## Качество самих кодов

Кодировщики-субагенты не всегда следовали записи: в 57 из 318 кодов (18%) есть выдуманные «корни» английскими словами (`THIS` 19, `HAVE` 14, `AND` 12, `NEW`, `GET`, `USE`, `BUT`), в 127 метка формы слита с частью речи (`| iT-2`). Одни и те же понятия кодировались по-разному в разных частях. Оценка поэтому смешивает ограничения языка и качество кодирования (кодировщики и декодеры — модель среднего размера с краткой инструкцией).

## Примеры

- 3: *The French Second Republic was created in 1848 but abolished by Napoleon III who proclaimed himself Emperor in 1852.* → «The French Second Republic began in 1848, when Napoleon III was elected president, and ended in 1852 when he became emperor».
- 2: *The Empire of Magadha included republican communities such as the community of Rajakumara.* → «The great kingdom of Magadha later absorbed these many kingdoms, which were similar to the “community of Rajakumara”».
- 1: *These states are parliamentary republics and operate similarly to constitutional monarchies…* → «Some states are “parliamentary republics” and do the same as the great ruler’s known rule…».
- 0: *In states with a parliamentary system, the president is usually elected by the parliament.* → «Republics of many rulers were called “most” by the head of state…».
