# Шаг 2б: отбор осей

Кандидатов от Haiku 80 (после отбрасывания осей с < 5 словами в Numberbatch; отброшено 1), после слияния дублей |cos| > 0,7 — 55. Дубли с осями корней (|cos| > 0,7): cold - hot ≈ HEAT, hard - soft ≈ TOUCH, loud - quiet ≈ SAY, large - small ≈ BIG, near - far ≈ NEAR, alive - dead ≈ LIVE, happy - sad ≈ MOOD, give - take ≈ GIVE, join - separate ≈ JOIN, outer - inner ≈ INSIDE.

Покрытие — доля дисперсии очищенных векторов в линейной оболочке набора, в скобках — доля потолка (PCA того же k). Набор — жадный отбор при |cos| ≤ 0,3.

| пул | k | покрытие, 5949 лемм | покрытие, big1000 | наиб. / сред. abs(cos) |
|---|--:|---|---|---|
| новые | 10 | 5.5% (48%) | 5.4% (38%) | 0.25 / 0.10 |
| новые | 15 | 7.9% (49%) | 7.8% (39%) | 0.28 / 0.10 |
| новые | 20 | 10.1% (51%) | 9.9% (40%) | 0.28 / 0.10 |
| оси корней (semaxis) | 10 | 5.7% (49%) | 5.5% (39%) | 0.19 / 0.06 |
| оси корней (semaxis) | 15 | 8.1% (51%) | 7.9% (40%) | 0.28 / 0.06 |
| оси корней (semaxis) | 20 | 10.3% (52%) | 10.0% (41%) | 0.28 / 0.07 |
| оба | 10 | 5.8% (50%) | 5.6% (40%) | 0.25 / 0.07 |
| оба | 15 | 8.3% (52%) | 8.1% (41%) | 0.29 / 0.07 |
| оба | 20 | 10.6% (53%) | 10.5% (43%) | 0.29 / 0.08 |
| атомы корней (обученные) | 10 | 6.7% (58%) | 6.6% (46%) | 0.17 / 0.05 |
| атомы корней (обученные) | 15 | 9.5% (59%) | 9.2% (46%) | 0.28 / 0.07 |
| атомы корней (обученные) | 20 | 12.1% (61%) | 11.8% (48%) | 0.28 / 0.07 |
| Осгуд, 3 оси | 3 | 1.5% (37%) | 1.4% | 0.26 / 0.10 |
| все 39 осей корней | 38 | 17.0% (54%) | 16.5% | 0.48 / 0.07 |
| все новые | 55 | 23.8% (58%) | 23.4% | 0.56 / 0.12 |
| PCA (потолок) | 20 | 19.9% | 24.6% | 0 |

## Набор «новые», 20 осей (по порядку отбора)

| # | ось | источник | прирост покрытия | ближайшая ось корня | − полюс (по проекции) | + полюс (по проекции) |
|---|---|---|--:|---|---|---|
| 1 | build - destroy | haiku-1 | 0.62% | JOIN -0.27 | develop, generate, produce, provide, implement, maintain, creation, installed | devastating, destruction, damage, tear, hurt, kill, threaten, harm |
| 2 | peaceful - violent | haiku-1 | 0.58% | FRIEND -0.54 | peace, quiet, comfortable, calm, happy, settle, reconciliation, nice | intense, harsh, extreme, tough, severe, attack, crazy, mad |
| 3 | trivial - important | haiku-2 | 0.57% | VALUE +0.43 | slight, little, slightly, relatively, somewhat, less, modest, small | influential, fundamental, necessary, primary, enable, prominent, ensure, importance |
| 4 | give - take | haiku-1 | 0.57% | GIVE -0.95 | contribute, contribution, gift, sponsor, charity, assistance, volunteer, receive | catch, possession, arrest, kidnapping, kidnapped, hostage, rob, destroy |
| 5 | permanent - temporary | haiku-1 | 0.56% | BIG -0.27 | forever, constant, commitment, constantly, consistently, lifetime, maintain, sustainable | briefly, shortly, summary, preliminary, temporarily, little, slight, briefing |
| 6 | public - private | haiku-1 | 0.55% | RULE -0.33 | municipal, community, folk, municipality, nationalist, widespread, local, council | privately, hide, privacy, spy, reveal, mystery, anonymity, exclusive |
| 7 | bright - dark | haiku-2 | 0.54% | MOOD -0.34 | spectacular, excellent, remarkable, wonderful, outstanding, impressive, amazing, beautiful | uncertain, unclear, unknown, somewhat, narrow, unidentified, cemetery, slightly |
| 8 | alive - dead | haiku-1 | 0.52% | LIVE -0.73 | lifestyle, awareness, life, aware, fundamental, environment, healthy, sustainable | cemetery, old, former, empty, late, funeral, death, successor |
| 9 | irregular - regular | haiku-2 | 0.51% | CARE +0.33 | uncertain, unexpected, unusual, strange, unclear, sudden, excessive, unknown | standard, proper, comfortable, ensure, healthy, requirement, basic, efficient |
| 10 | simple - complex | haiku-1 | 0.48% | VALUE +0.28 | simply, pure, merely, honest, reasonable, absolute, ordinary, clear | heavily, involvement, closely, deeply, involve, turmoil, surrounding, diverse |
| 11 | closed - open | haiku-2 | 0.48% | CAN +0.25 | lock, stalled, closure, detained, tight, block, tie, halt | discover, obvious, reveal, explore, learn, apparent, demonstrate, clearly |
| 12 | sick - healthy | haiku-2 | 0.47% | GOOD +0.42 | illness, badly, fever, infected, wounded, hospital, flu, disease | consistent, reasonable, strong, honest, reliable, substantial, solid, fairly |
| 13 | fast - slow | haiku-1 | 0.47% | FEEL -0.39 | quickly, immediate, rapidly, immediately, powerful, accurate, lightning, soon | slowly, disappointing, rest, slowdown, slightly, gradually, slump, decline |
| 14 | light - heavy | haiku-1 | 0.47% | BIG +0.36 | bright, optimism, flash, temporary, innocent, unchanged, pure, sky | heavily, burden, difficult, complicated, painful, tough, hard, massive |
| 15 | high - low | haiku-1 | 0.47% | ABOVE -0.51 | climb, higher, raise, rise, heights, mountain, tower, lift | weak, basically, little, poor, brief, disappointing, relatively, small |
| 16 | near - far | haiku-1 | 0.45% | NEAR -0.86 | immediately, shortly, upcoming, alongside, neighbouring, subsequent, neighborhood, junction | away, continent, mainland, journey, little, abroad, exile, bit |
| 17 | legal - illegal | haiku-1 | 0.45% | CAN -0.23 | reasonable, sufficient, claim, able, eligible, proper, jurisdiction, legally | smuggling, illegally, dangerous, dirty, ban, crime, violent, corruption |
| 18 | join - separate | haiku-1 | 0.44% | JOIN -0.89 | affiliated, add, alliance, associate, together, allied, bring, association | apart, break, portion, remove, isolated, tear, cut, partially |
| 19 | full - empty | haiku-1 | 0.44% | MANY -0.29 | plenty, tons, laden, bring, crowd, comprehensive, load, enormous | flat, land, gap, silent, quit, property, silence, retire |
| 20 | young - old | haiku-1 | 0.43% | BIG +0.22 | youth, teen, kid, child, childhood, hopeful, junior, boy | traditional, grandfather, gray, tradition, historic, classic, medieval, predecessor |

## Набор «оба», 20 осей (по порядку отбора)

| # | ось | источник | прирост покрытия | ближайшая ось корня | − полюс (по проекции) | + полюс (по проекции) |
|---|---|---|--:|---|---|---|
| 1 | THINK | roots | 0.67% | THINK +1.00 | worry, afraid, uncertainty, fear, suspicion, nervous, think, concern | select, settle, conclusion, properly, conduct, selection, effectively, resolution |
| 2 | GIVE | roots | 0.62% | GIVE +1.00 | capture, catch, rob, pull, possession, kidnapping, kidnapped, hold | gift, contribution, contribute, provide, sponsor, charity, request, submit |
| 3 | RULE | roots | 0.60% | RULE +1.00 | privately, personally, share, conversation, self, guest, personality, person | jurisdiction, regulation, legislation, judiciary, judicial, constitution, enforcement, constitutional |
| 4 | peaceful - violent | haiku-1 | 0.57% | FRIEND -0.54 | peace, quiet, comfortable, calm, happy, settle, reconciliation, nice | intense, harsh, extreme, tough, severe, attack, crazy, mad |
| 5 | permanent - temporary | haiku-1 | 0.57% | BIG -0.27 | forever, constant, commitment, constantly, consistently, lifetime, maintain, sustainable | briefly, shortly, summary, preliminary, temporarily, little, slight, briefing |
| 6 | build - destroy | haiku-1 | 0.57% | JOIN -0.27 | develop, generate, produce, provide, implement, maintain, creation, installed | devastating, destruction, damage, tear, hurt, kill, threaten, harm |
| 7 | CHANGE | roots | 0.56% | CHANGE +1.00 | keep, steady, still, continue, maintain, alive, silent, forever | different, conversion, transition, dramatically, difference, switch, dramatic, turn |
| 8 | trivial - important | haiku-2 | 0.55% | VALUE +0.43 | slight, little, slightly, relatively, somewhat, less, modest, small | influential, fundamental, necessary, primary, enable, prominent, ensure, importance |
| 9 | ART | roots | 0.54% | ART +1.00 | engineer, tech, electrical, devices, hardware, electronic, technical, computer | artist, artistic, painter, arts, poet, portrait, gallery, contemporary |
| 10 | bright - dark | haiku-2 | 0.53% | MOOD -0.34 | spectacular, excellent, remarkable, wonderful, outstanding, impressive, amazing, beautiful | uncertain, unclear, unknown, somewhat, narrow, unidentified, cemetery, slightly |
| 11 | TIME | roots | 0.52% | TIME +1.00 | previously, previous, recently, formerly, last, years, times, old | ready, hopefully, arrive, shortly, possible, begin, next, decide |
| 12 | LIVE | roots | 0.51% | LIVE +1.00 | die, funeral, suicide, grave, fatal, deadly, murder, cemetery | animated, healthy, energy, sustainable, essential, exciting, fun, live |
| 13 | simple - complex | haiku-1 | 0.50% | VALUE +0.28 | simply, pure, merely, honest, reasonable, absolute, ordinary, clear | heavily, involvement, closely, deeply, involve, turmoil, surrounding, diverse |
| 14 | CAN | roots | 0.49% | CAN +1.00 | tough, severely, harsh, desperate, badly, failure, struggle, painful | efficient, practical, possibility, possibly, effective, potential, available, smart |
| 15 | PART | roots | 0.48% | PART +1.00 | slight, little, chip, tiny, substance, portion, dust, slightly | various, diverse, variety, selection, list, gang, organization, crowd |
| 16 | BEGIN | roots | 0.48% | BEGIN +1.00 | initially, launch, gradually, starter, newly, new, initiative, immediately | conclusion, outcome, victory, overtime, score, ultimate, win, ultimately |
| 17 | MEASURE | roots | 0.47% | MEASURE +1.00 | tall, large, bulk, enormous, vast, big, thick, numerous | percent, median, lowest, benchmark, worst, equity, higher, income |
| 18 | irregular - regular | haiku-2 | 0.47% | CARE +0.33 | uncertain, unexpected, unusual, strange, unclear, sudden, excessive, unknown | standard, proper, comfortable, ensure, healthy, requirement, basic, efficient |
| 19 | MOVE | roots | 0.46% | MOVE +1.00 | remain, sit, cease, remainder, keep, unchanged, alone, stay | quick, speed, quickly, rapid, rapidly, runner, race, urgent |
| 20 | high - low | haiku-1 | 0.46% | ABOVE -0.51 | climb, higher, raise, rise, heights, mountain, tower, lift | weak, basically, little, poor, brief, disappointing, relatively, small |
