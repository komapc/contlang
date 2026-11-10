# Разбор корней min-co 1: степень или лестница

Черновик Claude (2026-11-10), классификация — на глаз по `en_axis` в `roots.yaml`; её проверяет [пилот осей](../../data/eval/runs/v2_axes/README.md).

- **степень** — одно качество сильнее или слабее, как *mal-* / *-et-* / *-eg-* в эсперанто: промежуточные значения
  выводятся из полюсов (18 корней);
- **лестница** — под числами стоят разные вещи (газ → жидкость → порошок → твёрдое): каждую ступень надо заучить (15);
- **смешанная** — степень, но с особыми опорами или вторым значением (6);
- **без оси** (6).

«Значений» — сколько раз корень встретился со значением в кодах моделей min-co 1 ([values.py](../../data/eval/runs/v2_axes/values.py));
«крайних» — доля ±5 в процентах.

| корень | тип | ось (`en_axis`) | значений | крайних, % |
|---|---|---|--:|--:|
| GOOD | степень | -5 terrible … +5 excellent | 441 | 14 |
| BIG | степень | -5 tiny … +5 huge (size only) | 237 | 20 |
| ABOVE | степень | -5 below, down … +5 above, up | 229 | 78 |
| HEAT | степень | -5 ice cold … +5 fire hot | 85 | 60 |
| WANT | степень | -5 hate, refuse … +5 love, crave | 115 | 58 |
| FRIEND | степень | -5 enemy, hostile, cruel … +5 friend, friendly, kind (attitude toward people) | 86 | 63 |
| CARE | степень | -5 careless, a mistake, fault … +5 careful, thorough, diligent | 66 | 66 |
| JOIN | степень | -5 separate, remove … +5 join, add, attach | 230 | 96 |
| TOUCH | степень | -5 soft, smooth, tender … +5 hard, stiff, tough, harsh | 140 | 69 |
| MOVE | степень | -5 stand still … 0 walk … +5 rush | 192 | 53 |
| SAY | степень | -5 whisper … 0 speak … +5 shout (also noises) | 36 | 33 |
| FEEL | степень | -5 calm … +5 excited, intense (pleasant or not is GOOD) | 114 | 48 |
| CAN | степень | -5 impossible … -3 hard … +5 easy | 106 | 56 |
| CHANGE | степень | -5 stay the same … 0 change … +5 transform (the direction comes from the next root: `CHANGE GOOD(=+3)` improve) | 93 | 75 |
| MOOD | степень | -5 tragic … -3 sad … 0 serious … +3 glad … +5 funny | 67 | 45 |
| TIME | степень | -5 long ago … 0 now … +5 far future (-1 just now, +1 soon) | 283 | 9 |
| INSIDE | степень | -5 outside … 0 on the border, at the edge, the surface … +5 inside | 237 | 84 |
| NEAR | степень | -5 far, abroad, journey … +5 here, nearby, downtown, center | 164 | 91 |
| MANY | смешанная | -5 none, never … -1 few … 0 some … +3 many … +5 all, always | 254 | 42 |
| VALUE | смешанная | -5 cheap, a bargain, buying and selling … +5 precious, important, vital (price, worth) | 74 | 76 |
| SIDE | смешанная | -5 back, behind, backward; also going back, return … +5 front, ahead, forward; also coming up, ready | 146 | 90 |
| LIVE | смешанная | -5 dead … -2 asleep … +5 alive | 101 | 66 |
| SEX | смешанная | -5 female … +5 male (only for words of explicit sex) | 164 | 97 |
| SAME | смешанная | -5 opposite, different … -4 special … +3 ordinary … +5 identical | 362 | 56 |
| GRAIN | лестница | -5 gas … -3 liquid … 0 powder, grain … +5 one solid piece | 172 | 36 |
| THING | лестница | -5 stone, inanimate … 0 plant … +4 animal | 162 | 16 |
| LONG | лестница | -5 thread, cloth, textile … 0 wire, rod, fastening … +5 beam, plank, wooden furniture (long objects and what is made of them) | 124 | 78 |
| LAND | лестница | -5 sea, water … 0 shore, coast … +5 dry land, ground (the plain root means land, country, region) | 42 | 97 |
| FIGHT | лестница | -5 game, sport … 0 quarrel … +5 war | 209 | 85 |
| MEASURE | лестница | -5 an amount (size, length, weight, quantity) … 0 a level, degree … +5 a ratio, rate, percentage, statistics | 118 | 79 |
| SOMEONE | лестница | -5 they, others … 0 someone … +3 you … +5 I | 160 | 83 |
| PART | лестница | -5 particle, crumb … -2 a part, member … +2 the whole … +5 a group of many | 517 | 43 |
| KNOW | лестница | -5 stupid, foolish, absurd … 0 aware … +5 know, inform, teach | 127 | 81 |
| GIVE | лестница | -5 grab, seize, steal … 0 exchange, get … +5 give, donate, grant | 314 | 39 |
| BEGIN | лестница | -5 start … 0 ongoing … +5 end | 158 | 80 |
| CONSUME | лестница | -5 give out (emit, speak, write) … +5 take in (eat, drink, read, listen) | 95 | 99 |
| ART | лестница | -5 technology, exact science … +5 arts, humanities (the plain root means skill, craft) | 179 | 90 |
| THINK | лестница | -5 doubt … 0 think … +5 decide | 162 | 82 |
| RULE | лестница | -5 private, informal … +4 authority, institution … +5 law, official | 272 | 33 |
| HAPPEN | без оси | — | 0 | — |
| BODY | без оси | — | 0 | — |
| SEE | без оси | — | 0 | — |
| DO | без оси | — | 0 | — |
| PLACE | без оси | — | 2 | 100 |
| TEXT | без оси | — | 0 | — |
