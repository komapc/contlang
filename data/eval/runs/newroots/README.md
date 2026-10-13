# Три новых корня из Toki Pona: LAND (ma), SACRED (sewi), CONTAINER (poki)

Кандидаты — из промахов идеала (коды модели H, где оба читателя мимо) и покрытия WordNet. spec.md — спецификация читателя с 47 корнями:

- LAND: −5 sea, water … 0 shore, coast … +5 dry land, ground (голый — land, country, region)
- SACRED: −5 cursed, demonic … 0 magic, spirit … +5 holy, divine (голый — religion, faith)
- CONTAINER: −5 open (tray, saucer, platter) … +5 closed (box, jar, bottle) (голый — container, vessel)

Полюс CONTAINER −5 сначала был «tray, bowl, basket»: basket и bowl тянули ось к спорту (athletics, playoff получали CONTAINER) —
заменено; пишущие видели старый вариант, читатели — новый.

- **H2** — модель (Haiku, write/task.md) переписала только коды, которым новые корни помогают: 10 из 100.
- **SZ2** — SZ (`sz.py`, перенос ../measure/make.js на Python, сверка 99/100) с новыми корнями: центр — среднее слов подписи,
  ось — разность полюсов; выраженность нового корня — только по центру (ось из трёх слов шумная); якоря WordNet (NEW_ANCH). 22 кода из 100.

8 слепых читателей Haiku со spec.md, судья — ../reader. Пороги — dec.md.

| | близко | против старого |
|---|--:|--:|
| H2 | **46 %** | H 38 %: +8 % (+2 … +14); на 10 изменённых +55 % (+25 … +85) |
| SZ2 | 24 % | SZ 20 %: +4 % (−2 … +10); на 22 изменённых +7 % (−11 … +27) |
| вместе на 32 изменённых | | **+22 % (+5 … +39)** |

SACRED работает лучше всех (religion, chapel, bishop, spell: из «мимо» в «близко»); LAND и CONTAINER — смешанно
(acre, fleet, bubble лучше; campus, door, cake у математики хуже).
