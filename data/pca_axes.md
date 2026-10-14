# Главные оси словаря сайта (шаги 0–1 пересмотра корней)

`scripts/23_pca_axes.py 20`. Слов 5949 (леммы словаря сайта без служебных и имён), векторы Numberbatch (vocab.bin).

## Шаг 0. Очистка

Вычтены направление частотности и 3 направления частей речи. В клетке — |r| главной оси с частотой / η² части речи.

| | PC1 | PC2 | PC3 | PC4 | PC5 | PC6 | PC7 | PC8 | PC9 | PC10 |
|---|---|---|---|---|---|---|---|---|---|---|
| до очистки | 0.16 / 0.50 | 0.05 / 0.14 | 0.11 / 0.45 | 0.07 / 0.06 | 0.07 / 0.11 | 0.09 / 0.09 | 0.16 / 0.00 | 0.05 / 0.02 | 0.00 / 0.06 | 0.03 / 0.03 |
| после очистки | 0.05 / 0.00 | 0.02 / 0.00 | 0.10 / 0.00 | 0.02 / 0.00 | 0.09 / 0.00 | 0.08 / 0.00 | 0.00 / 0.00 | 0.05 / 0.00 | 0.01 / 0.00 | 0.04 / 0.00 |

## Шаг 1. PCA

Доля дисперсии верхних компонент: 10 — 11.6%, 20 — 19.9%, 30 — 26.8% (одна случайная ось в среднем 0.3%).

## PCA, верхние 20

| ось | доля | r част. | η² ч.р. | − полюс | + полюс | ближе всего из корней |
|---|--:|--:|--:|---|---|---|
| 1 | 1.6% | 0.05 | 0.00 | mandate, requirement, consideration, provision, statement, regard, implementation, approve, commission, agreement, advisory, approval | fell, away, blast, hit, beat, slowly, burst, slide, surge, boom, blow, corner | RULE·центр -0.52, GIVE·ось -0.41 |
| 2 | 1.4% | 0.02 | 0.00 | amount, extent, range, generate, ratio, variety, increase, size, scale, enhance, density, output | deputy, resignation, secretary, resign, chairman, envoy, president, chancellor, vowed, commissioner, lieutenant, senator | MEASURE·центр -0.51, SEX·центр +0.32 |
| 3 | 1.2% | 0.10 | 0.00 | administrative, department, headquarters, administrator, personnel, municipal, office, administration, maintenance, facility, bureau, subsidiary | indeed, certainly, truly, really, significance, sense, impression, obviously, think, wonder, fact, remarkable | THINK·ось -0.42, ART·ось +0.33 |
| 4 | 1.2% | 0.02 | 0.00 | downturn, slowdown, slump, recession, momentum, inflation, surge, decline, losses, deficit, increase, reduction | unique, famous, wonderful, beautiful, belong, special, legendary, identify, dedicated, guest, feature, specifically | ABOVE·центр -0.31, MEASURE·центр -0.31 |
| 5 | 1.1% | 0.09 | 0.00 | final, date, next, last, deadline, subsequent, completion, days, year, month, season, arrival | deeply, strengthen, integrity, strongly, actively, strong, leadership, heavily, advocate, militant, culture, encourage | TIME·центр -0.45, BEGIN·центр -0.42 |
| 6 | 1.1% | 0.08 | 0.00 | plain, explanation, reasonable, notice, instructions, suspect, prosecutor, complaint, wrong, police, warrant, explain | success, successful, prestigious, achievement, debut, exciting, compete, championship, inaugural, competitive, competition, internationally | BIG·ось +0.31, PART·ось +0.31 |
| 7 | 1.0% | 0.00 | 0.00 | earn, worth, afford, pay, money, cost, cash, premium, salary, expense, cent, profit | briefing, probe, summary, incident, investigation, briefly, brief, outbreak, shortly, scene, report, introduction | VALUE·центр -0.31, TEXT·центр +0.30 |
| 8 | 1.0% | 0.05 | 0.00 | refuge, hope, journey, safe, facility, assistance, rescue, help, necessary, haven, peaceful, comfort | prominent, respectively, predominantly, conservative, republican, democrat, consecutive, notably, top, poll, represent, traditionally | TIME·ось -0.33, SAME·центр +0.33 |
| 9 | 1.0% | 0.01 | 0.00 | victory, sovereignty, constitution, establish, stronghold, supreme, constitutional, secure, defeat, defend, solid, prove | frequent, monthly, employee, sales, consultant, occasionally, concern, friend, increase, associate, weekly, frequently | RULE·ось -0.32, FEEL·центр +0.26 |
| 10 | 1.0% | 0.04 | 0.00 | quick, goal, accurate, quickly, teammate, carefully, striker, position, objective, forward, training, ready | largely, downtown, mostly, municipality, mall, community, municipal, exist, rural, metropolitan, neighbouring, town | LAND·центр +0.35, CAN·центр -0.30 |
| 11 | 0.9% | 0.00 | 0.00 | spiritual, religious, gradually, secular, slowly, faith, forever, spirit, soul, peace, citizenship, prayer | extremely, terrible, quite, pretty, devastating, impressive, absolutely, really, amazing, brutal, highly, fairly | GOOD·центр +0.43, CHANGE·центр -0.30 |
| 12 | 0.9% | 0.08 | 0.00 | petition, presentation, announcement, document, declaration, praise, review, comprehensive, paper, beautiful, sheet, publish | probably, possibly, assume, likely, former, veteran, lieutenant, infantry, guess, unlike, commander, captain | TEXT·центр -0.33, SAY·центр -0.31 |
| 13 | 0.9% | 0.04 | 0.00 | venue, downtown, comfortable, corner, way, district, sit, debate, mall, prospect, think, nice | subsequently, deadly, recover, legendary, destruction, allegedly, destroy, death, subsequent, alleged, original, release | FIGHT·ось +0.29, PLACE·центр -0.28 |
| 14 | 0.9% | 0.01 | 0.00 | alternative, merger, sell, solution, eventually, maker, replace, buy, abandon, idea, creative, producer | attendance, notable, greatly, considerable, impressive, remarkable, outstanding, importance, high, rank, turnout, honor | MEASURE·центр +0.30, VALUE·ось +0.29 |
| 15 | 0.8% | 0.00 | 0.00 | predict, forecast, economist, estimate, analyst, determine, researcher, uncertain, optimistic, confirm, examine, explore | usually, especially, riot, traditionally, normally, typically, special, event, assault, routine, regular, combination | THINK·центр -0.31, FIGHT·центр +0.27 |
| 16 | 0.8% | 0.02 | 0.00 | presence, indication, loyal, strong, apparently, confirmation, visible, signal, sign, supporter, support, reluctant | properly, carefully, disaster, tragedy, ethics, crisis, educational, badly, health, economic, economics, education | THINK·ось +0.25, MANY·ось +0.25 |
| 17 | 0.8% | 0.01 | 0.00 | compete, dispute, contest, mutual, competitive, competition, conflict, hostile, confrontation, transactions, tournament, match | deputy, chancellor, minister, governor, replace, legislature, successor, replacement, aide, presidency, chairman, mayor | FIGHT·центр -0.32, BIG·центр +0.28 |
| 18 | 0.8% | 0.03 | 0.00 | status, temporarily, holder, permanent, owner, secure, retain, control, automatically, disabled, temporary, user | research, suggest, dozen, conspiracy, experiment, study, preliminary, investigation, exploration, theory, experimental, effort | CHANGE·центр -0.26, BEGIN·центр +0.21 |
| 19 | 0.8% | 0.03 | 0.00 | require, commonly, demand, conventional, rapid, popular, speed, standard, frequent, usually, frequently, automatic | somewhat, slightly, little, remainder, relationship, partnership, strengthen, bit, portion, involvement, rest, contribution | SAY·ось -0.30, JOIN·центр +0.27 |
| 20 | 0.7% | 0.04 | 0.00 | gather, election, electoral, democratic, polls, voter, collect, constituency, parliamentary, crowd, ballot, generate | decline, refusal, abandon, strict, reverse, downturn, restructuring, tradition, contract, construction, slump, classic | WANT·ось -0.24, ABOVE·центр +0.24 |

## Varimax, 20 осей

Поворот верхних K компонент: базис ортогонален, оценки слов разреженнее (у слова меньше сильных осей).

| ось | доля | r част. | η² ч.р. | − полюс | + полюс | ближе всего из корней |
|---|--:|--:|--:|---|---|---|
| 1 | 1.1% | 0.01 | 0.00 | refusal, declaration, plea, agreement, statement, mandate, approve, approval, petition, proposal, request, reject | grow, generate, gather, locally, enhance, create, learn, discover, manage, population, humans, explore | RULE·ось -0.37, WANT·ось +0.34 |
| 2 | 1.1% | 0.01 | 0.00 | increase, downturn, growth, momentum, slowdown, surge, significantly, decline, trend, boost, rise, expansion | innocent, properly, dinner, beautiful, legally, treat, belong, collect, eat, store, shop, rooms | ABOVE·центр -0.43, CHANGE·центр -0.36 |
| 3 | 1.0% | 0.05 | 0.00 | quick, slightly, flat, throw, switch, pretty, bit, slide, nice, shift, schedule, drop | honor, integrity, respect, sovereignty, faith, pride, importance, reputation, trust, fame, confidence, credibility | VALUE·ось +0.37, WANT·центр +0.24 |
| 4 | 1.0% | 0.07 | 0.00 | amount, earnings, income, expense, revenue, percentage, profits, pay, salary, cost, percent, profit | revolutionary, breakthrough, legendary, concept, legend, scene, path, famous, style, classic, mechanism, evolution | MEASURE·центр -0.57, ART·центр +0.28 |
| 5 | 1.0% | 0.01 | 0.00 | examine, detailed, report, investigate, summary, analysis, findings, survey, assessment, investigation, review, explain | temporarily, forever, permanent, abandon, temporary, anymore, still, eventually, quit, switch, replace, become | TEXT·центр -0.45, CARE·ось -0.41 |
| 6 | 1.0% | 0.10 | 0.00 | subsequent, later, earlier, earliest, next, last, shortly, subsequently, previous, upcoming, year, early | feel, attitude, comfortable, sensitive, tough, sense, environment, honest, really, stance, extremely, understand | TIME·центр -0.65, BEGIN·центр -0.49 |
| 7 | 1.0% | 0.02 | 0.00 | sharply, carefully, regularly, repeatedly, quickly, heavily, properly, slowly, rapidly, national, alert, monitor | certainly, probably, guess, think, possibly, likely, indeed, actually, unlikely, imagine, definitely, obviously | THINK·центр +0.51, MANY·ось -0.41 |
| 8 | 1.0% | 0.05 | 0.00 | riot, crowd, violence, massacre, massive, mass, conspiracy, chaos, destruction, mixture, explosion, pure | assistant, deputy, aide, administrator, director, adviser, manager, chief, secretary, executive, consultant, officer | SEX·центр +0.43, PART·центр -0.27 |
| 9 | 1.0% | 0.06 | 0.00 | enable, location, access, available, secure, appropriate, necessary, useful, destination, immediate, ensure, able | graham, argue, say, collins, sharply, wright, indicted, fell, miller, cole, warren, believe | CAN·центр -0.30, TIME·ось -0.29 |
| 10 | 1.0% | 0.04 | 0.00 | parliamentary, legislature, legislative, democratic, senate, parliament, congressional, electoral, congress, election, democrat, judiciary | adventure, journey, pursuit, training, chase, relationship, childhood, experience, life, love, cruise, description | RULE·ось -0.38, WANT·ось +0.20 |
| 11 | 1.0% | 0.06 | 0.00 | essentially, basically, structure, largely, entirely, establish, framework, partially, completely, contain, preserve, separate | eager, urge, rush, keen, ask, hopeful, joy, urgent, reluctant, willing, invitation, desire | FEEL·центр +0.44, SAY·центр +0.42 |
| 12 | 1.0% | 0.06 | 0.00 | southeast, northeast, southeastern, northwest, roads, area, southwest, situated, south, northeastern, east, downtown | formula, ability, composition, powerful, technique, substitute, reaction, replacement, format, replace, version, words | PLACE·центр -0.55, NEAR·центр -0.50 |
| 13 | 1.0% | 0.06 | 0.00 | championship, playoff, win, tournament, winner, compete, victory, contest, competition, league, score, champion | ministry, authorities, reduction, government, creation, pollution, liquid, infrastructure, increase, substantial, larger, minister | FIGHT·центр -0.55, FIGHT·ось +0.34 |
| 14 | 1.0% | 0.07 | 0.00 | exact, accurate, correct, height, speed, mph, exactly, predict, absolute, temperature, aircraft, bullet | participation, partnership, collaboration, cooperation, involvement, community, initiative, participate, alliance, organization, encourage, join | JOIN·ось +0.34, PART·ось +0.30 |
| 15 | 1.0% | 0.01 | 0.00 | mutual, settle, neutral, relationship, decide, conflict, separately, consensus, instead, determine, sexual, respectively | impressive, spectacular, amazing, wonderful, remarkable, tremendous, great, outstanding, extraordinary, excellent, beautiful, enormous | GOOD·центр +0.59, BIG·ось +0.35 |
| 16 | 1.0% | 0.04 | 0.00 | solid, broad, wide, stick, white, arm, frame, top, strong, aim, foot, length | disaster, tragedy, devastating, aftermath, terrible, accident, turmoil, crisis, incident, worse, fatal, unrest | GOOD·ось -0.43, HAPPEN·центр +0.40 |
| 17 | 0.9% | 0.04 | 0.00 | confident, hopeful, optimistic, secure, rebuild, finally, desperate, recover, hope, safe, ultimately, confidence | typically, usually, commonly, generally, normally, usual, typical, frequent, frequently, traditionally, variety, regularly | SAME·центр +0.49, HAPPEN·центр +0.40 |
| 18 | 0.9% | 0.04 | 0.00 | company, commercial, sell, marketing, industry, sales, manufacturer, market, corporation, worldwide, retail, mart | rest, prayer, temple, little, discipline, chapel, detention, slightly, session, spiritual, bit, time | ART·ось +0.26, BIG·ось -0.25 |
| 19 | 0.9% | 0.02 | 0.00 | theme, economic, future, artistic, calendar, change, outlook, topic, economics, economy, trend, contemporary | troops, army, armed, battalion, infantry, squadron, brigade, troop, militia, artillery, military, regiment | FIGHT·ось +0.55, FIGHT·центр +0.42 |
| 20 | 0.9% | 0.03 | 0.00 | implement, practical, prepare, implementation, develop, education, efficient, plan, preparation, educational, pursue, training | unidentified, note, visible, presence, apparently, indicate, notice, prominent, comment, apparent, unknown, mention | ART·центр -0.38, DO·центр -0.33 |

## ICA, 20 осей

Независимые оси в том же подпространстве; базис не ортогонален: наибольший |cos| между осями 0.17, средний 0.03.

| ось | доля | r част. | η² ч.р. | − полюс | + полюс | ближе всего из корней |
|---|--:|--:|--:|---|---|---|
| 1 | 1.0% | 0.05 | 0.00 | increase, percentage, amount, earnings, percent, income, significantly, revenue, profits, rate, average, total | dialogue, scene, venue, simple, concept, peaceful, ready, classic, assembly, confrontation, formally, demonstration | MEASURE·центр -0.70, ABOVE·центр -0.37 |
| 2 | 1.0% | 0.06 | 0.00 | solid, pound, white, graham, wright, pure, mm, barrel, broad, stone, miller, throw | attend, attendance, personnel, affairs, appointment, circumstances, services, situation, temporarily, temporary, employment, assistance | RULE·центр +0.34, GRAIN·центр -0.32 |
| 3 | 1.0% | 0.10 | 0.00 | subsequent, next, later, earlier, earliest, shortly, last, upcoming, subsequently, year, early, prior | attitude, extremely, feel, stance, really, sensitive, tough, sense, comfortable, strong, environment, deeply | TIME·центр -0.63, BEGIN·центр -0.49 |
| 4 | 1.0% | 0.03 | 0.00 | sharply, carefully, repeatedly, regularly, slowly, heavily, rapidly, quickly, properly, alert, national, monitor | certainly, probably, possibly, guess, think, likely, actually, indeed, unlikely, imagine, definitely, obviously | THINK·центр +0.48, MANY·ось -0.39 |
| 5 | 1.0% | 0.07 | 0.00 | devastating, tragedy, disaster, terrible, aftermath, collapse, fatal, downturn, crash, crisis, turmoil, destruction | willing, provide, give, optional, sufficient, additional, membership, offer, available, request, invitation, allow | GOOD·ось +0.44, FRIEND·ось +0.34 |
| 6 | 1.0% | 0.04 | 0.00 | generate, gather, locally, enhance, create, grow, manage, discover, find, population, environment, potential | refusal, declaration, plea, agreement, statement, approve, reject, verdict, mandate, indictment, approval, petition | WANT·ось -0.36, RULE·ось +0.35 |
| 7 | 1.0% | 0.06 | 0.00 | slightly, somewhat, nice, session, schedule, pretty, briefing, bit, interesting, quite, lunch, discussion | integrity, sovereignty, honor, faith, pride, fame, respect, credibility, greatest, reputation, independence, prosperity | VALUE·ось +0.29, CHANGE·ось -0.22 |
| 8 | 1.0% | 0.05 | 0.00 | reduction, creation, increase, massive, authorities, ministry, government, pollution, infrastructure, substantial, restoration, liquid | championship, playoff, win, tournament, compete, winner, league, score, contest, competition, game, competitive | FIGHT·центр +0.54, FIGHT·ось -0.35 |
| 9 | 1.0% | 0.00 | 0.00 | impressive, amazing, spectacular, wonderful, remarkable, tremendous, great, outstanding, extraordinary, greatly, enormous, excellent | mutual, neutral, settle, determine, decide, conflict, avoid, principle, psychological, instead, relationship, gender | GOOD·центр -0.56, BIG·ось -0.35 |
| 10 | 1.0% | 0.06 | 0.00 | eager, urge, reluctant, keen, willingness, desire, angry, audience, rush, passion, hopeful, cautious | essentially, entirely, preserve, rebuild, restore, completely, structure, basically, establish, create, totally, destroy | FEEL·центр -0.43, SAY·центр -0.42 |
| 11 | 0.9% | 0.02 | 0.00 | dinner, eat, guilty, spend, treat, care, innocent, eggs, lunch, sweet, crime, chapel | momentum, expansion, position, indication, signal, rapid, dominant, visible, surge, transition, launch, stance | CHANGE·центр +0.28, SOMEONE·центр -0.24 |
| 12 | 0.9% | 0.00 | 0.00 | examine, report, detailed, investigate, summary, findings, describe, survey, explain, investigation, commentary, identify | permanent, abandon, temporarily, afford, temporary, switch, replacement, replace, forever, electric, traditional, eventually | TEXT·центр -0.46, SEE·центр -0.39 |
| 13 | 0.9% | 0.03 | 0.00 | assistant, director, deputy, chief, adviser, manager, administrator, aide, secretary, consultant, executive, chairman | crowd, riot, contest, confrontation, violence, turnout, massacre, conflict, demonstration, venue, event, action | SEX·центр -0.46, PART·центр +0.28 |
| 14 | 0.9% | 0.04 | 0.00 | adventure, pursuit, relationship, training, journey, childhood, life, chase, experience, love, lifetime, cruise | parliamentary, democratic, legislature, legislative, senate, parliament, congressional, congress, electoral, election, democrat, lawmaker | RULE·ось +0.36, WANT·ось -0.19 |
| 15 | 0.9% | 0.04 | 0.00 | southeast, northeast, roads, northwest, southwest, southeastern, south, area, north, east, highway, situated | replace, substitute, formula, replacement, format, composition, powerful, produce, copy, edition, extra, version | PLACE·центр -0.53, NEAR·центр -0.47 |
| 16 | 0.9% | 0.05 | 0.00 | temple, priest, discipline, prayer, spiritual, step, height, slight, slightly, guard, stretch, little | sell, mart, retail, sales, commercial, market, company, marketing, business, corporation, merchant, purchase | VALUE·центр +0.28, ART·ось -0.24 |
| 17 | 0.9% | 0.03 | 0.00 | hopeful, confident, secure, optimistic, finally, hope, rebuild, desperate, soon, safe, hopefully, recover | typically, commonly, usually, generally, typical, normally, traditionally, usual, frequent, frequently, predominantly, variety | SAME·центр +0.51, HAPPEN·центр +0.36 |
| 18 | 0.9% | 0.03 | 0.00 | unidentified, unknown, spot, empty, name, temporarily, location, holder, dead, detained, visible, hide | develop, development, initiative, ambitious, education, educational, implementation, implement, intensive, strategy, pursue, training | ART·центр +0.39, DO·центр +0.29 |
| 19 | 0.9% | 0.03 | 0.00 | economic, trend, economy, change, artistic, downturn, secular, recession, economics, outlook, future, theme | troops, army, armed, battalion, infantry, squadron, brigade, troop, militia, artillery, military, regiment | FIGHT·ось +0.53, FIGHT·центр +0.42 |
| 20 | 0.9% | 0.04 | 0.00 | accurate, proper, properly, necessary, appropriate, correct, exact, quickly, speed, fast, perfect, determine | partnership, involvement, alliance, collaboration, affiliated, solidarity, cooperation, participation, group, coalition, community, largely | CAN·центр -0.31, TIME·ось -0.27 |

## Нынешние корни в подпространстве верхних 20 компонент

Доля длины атома (квадрат), лежащая в подпространстве; у случайного направления 6.7%.

| корень | доля | | корень | доля |
|---|--:|---|---|--:|
| MEASURE·центр | 70% | | PART·ось | 30% |
| FIGHT·центр | 56% | | FRIEND·центр | 30% |
| TIME·центр | 54% | | DO·центр | 30% |
| GOOD·центр | 52% | | BIG·ось | 30% |
| BEGIN·центр | 52% | | SEE·центр | 30% |
| THINK·ось | 50% | | CARE·центр | 30% |
| HAPPEN·центр | 49% | | VALUE·центр | 29% |
| THINK·центр | 48% | | JOIN·ось | 28% |
| FIGHT·ось | 47% | | CARE·ось | 28% |
| TEXT·центр | 47% | | LONG·центр | 27% |
| PLACE·центр | 46% | | KNOW·центр | 27% |
| ABOVE·центр | 46% | | GIVE·центр | 26% |
| RULE·ось | 44% | | FEEL·ось | 26% |
| ART·центр | 44% | | SOMEONE·ось | 25% |
| RULE·центр | 44% | | KNOW·ось | 25% |
| NEAR·центр | 43% | | MOVE·ось | 25% |
| WANT·центр | 43% | | CHANGE·ось | 24% |
| SAME·центр | 43% | | BEGIN·ось | 24% |
| CAN·центр | 41% | | CAN·ось | 24% |
| WANT·ось | 40% | | INSIDE·центр | 22% |
| SEX·центр | 38% | | SAY·ось | 22% |
| GIVE·ось | 38% | | MEASURE·ось | 21% |
| SAY·центр | 37% | | LIVE·центр | 21% |
| FEEL·центр | 36% | | SAME·ось | 20% |
| GOOD·ось | 35% | | BODY·центр | 20% |
| LAND·центр | 35% | | TOUCH·ось | 19% |
| FRIEND·ось | 35% | | CONSUME·центр | 19% |
| MOVE·центр | 35% | | SOMEONE·центр | 18% |
| ART·ось | 34% | | SIDE·ось | 18% |
| JOIN·центр | 33% | | THING·центр | 17% |
| CHANGE·центр | 33% | | GRAIN·ось | 16% |
| PART·центр | 33% | | MOOD·ось | 16% |
| MANY·ось | 33% | | ABOVE·ось | 14% |
| MANY·центр | 33% | | NEAR·ось | 11% |
| BIG·центр | 32% | | HEAT·центр | 10% |
| MOOD·центр | 32% | | INSIDE·ось | 10% |
| VALUE·ось | 32% | | THING·ось | 8% |
| TOUCH·центр | 32% | | CONSUME·ось | 6% |
| LIVE·ось | 31% | | LONG·ось | 5% |
| SIDE·центр | 31% | | LAND·ось | 5% |
| GRAIN·центр | 31% | | SEX·ось | 3% |
| TIME·ось | 31% | | HEAT·ось | 3% |

Оси корней: в среднем 24% в подпространстве; центры: 36%.
Покрытие главных компонент осями всех 39 корней (доля длины компоненты в их линейной оболочке): PC1 37%, PC2 36%, PC3 46%, PC4 44%, PC5 37%, PC6 44%, PC7 27%, PC8 34%, PC9 46%, PC10 28%, PC11 36%, PC12 32%, PC13 39%, PC14 34%, PC15 26%, PC16 37%, PC17 32%, PC18 30%, PC19 42%, PC20 27%.

