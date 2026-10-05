# Обучение словаря корней при условии читаемости

Numberbatch, 2689 слов (без слов-полюсов), обучение 1882, **тест 807** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 21.8% | 71.7% | 96.3% | 4 | 0.432 | 0.288 |
| корни из полюсов, вес не главных 0.6 | 24.0% | 73.0% | 96.5% | 4 | 0.440 | 0.297 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 28.7% | 82.3% | 98.8% | 3 | 0.495 | 0.362 |

Сдвиг корней: cos(центр, исходный) в среднем 0.93 (минимум 0.85), cos(ось, исходная) в среднем 0.93 (минимум 0.86). итерация 1: на обучающих словах до шага top1 23.3%, cos 0.442; итерация 2: на обучающих словах до шага top1 38.5%, cos 0.517; итерация 3: на обучающих словах до шага top1 40.8%, cos 0.527.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.93 | fantastic, nice, lovely, magnificent, brilliant | fantastic, lovely, magnificent, nice, brilliant | worst, unspeakable, unfortunate, worse, monstrous | unspeakable, unfortunate, worst, monstrous, worse |
| BIG | 0.94 | gigantic, massive, tremendous, considerable, extensive | tremendous, massive, gigantic, extensive, considerable | smaller, few, slightly, larger, minimal | smaller, few, slightly, minimal, somewhat |
| NEAR | 0.91 | shut, neighborhood, closely, along, around | shut, entrance, along, neighborhood, station | afar, farther, distance, beyond, off | afar, farther, distance, beyond, abroad |
| ABOVE | 0.92 | higher, rise, beyond, upper, climb | higher, rise, climb, raise, upper | bottom, downstairs, drop, descend, decline | drop, bottom, decline, fall, slide |
| LIVE | 0.94 | live, vivid, vitally, life, healthy | vivid, vividly, healthy, vigorous, life | corpse, die, fatal, kill, murder | die, corpse, murder, fatal, kill |
| SAME | 0.96 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, equate, correspond, exact | differ, differently, distinctive, various, distinctly | differ, various, distinctive, differently, variety |
| TIME | 0.93 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, await, arrive | previous, previously, recently, recent, formerly | recently, previously, previous, formerly, recent |
| INSIDE | 0.94 | inner, deep, around, room, therein | inner, basement, deep, room, therein | outdoor, inner, porch, side, surface | outdoor, porch, protective, inner, protection |
| PART | 0.93 | pack, gather, assemble, variety, selection | pack, selection, crowd, collective, organization | portion, dust, atom, part, texture | element, portion, dust, atom, component |
| SIDE | 0.93 | advance, rearward, before, side, precede | advance, rearward, northward, southward, along | rearward, shoulder, return, reverse, forth | rearward, return, reverse, shoulder, tilt |
| KNOW | 0.92 | understand, knowledge, conscious, realize, sure | understand, inform, knowledge, learn, realize | dumb, indifferent, stupid, helpless, silly | dumb, stupid, silly, fool, indifferent |
| WANT | 0.88 | wish, need, cherish, urge, seek | wish, need, hope, cherish, seek | despise, dislike, resent, oppose, deny | denounce, despise, condemn, oppose, criticize |
| HEAT | 0.95 | burn, heat, temperature, thermal, glow | heat, burn, erupt, boil, glow | freeze, snow, winter, temperature, melt | freeze, snow, winter, temperature, weather |
| BEGIN | 0.93 | conclusion, culminate, ultimate, terminate, complete | conclusion, fourth, sixth, ultimate, ninth | initiate, initially, onset, launch, early | initiate, launch, onset, initially, phase |
| GIVE | 0.89 | provide, receive, lend, contribute, accept | provide, receive, request, submit, lend | capture, catch, grasp, hold, acquire | capture, grasp, catch, pull, hold |
| TOUCH | 0.93 | tough, severe, rugged, strong, stiffly | tough, strong, severe, rugged, sturdy | gentle, sweet, porous, smooth, delicate | sweet, tender, delicate, gentle, smooth |
| MATTER | 0.92 | exhaust, oxygen, breath, breathe, atmosphere | oxygen, aircraft, atmosphere, breath, flight | concrete, steel, wood, iron, sturdy | concrete, steel, wood, iron, wooden |
| SEX | 0.94 | papa, boy, comrade, man, guy | papa, boy, comrade, beloved, guy | girl, woman, parent, family, lady | woman, girl, lady, parent, family |
| HAPPEN | 0.92 | impact, conclusion, affect, inevitable, occurrence | impact, occurrence, incident, circumstance, implication | motive, originate, explanation, main, basis | motive, main, originate, primary, problem |
| THINK | 0.86 | select, settle, define, assess, evaluate | assess, evaluate, define, identify, establish | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, worry, think, guess |
| CAN | 0.93 | convenient, efficient, conceivably, likely, probable | efficient, effective, convenient, useful, likely | tough, difficulty, painful, desperate, awkward | difficulty, tough, desperate, struggle, desperately |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | whole, invariably, totally, entire, practically | nowhere, hardly, anymore, scarcely, barely | hardly, certainly, apparently, evidently, indeed |
| SOMEONE | 0.97 | personally, someone, honestly, anyway, dear | personally, honestly, someone, maybe, anyway | people, either, individually, own, someone | people, either, several, men, various |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, chicken, hen, farm, barn | concrete, dirt, hill, mud, mountain | dirt, mud, sidewalk, concrete, soil |
| MOVE | 0.94 | quick, speed, hasten, rapid, accelerate | quick, speed, rapid, accelerate, hasten | sit, halt, keep, linger, continue | sit, halt, pause, while, keep |
| FEEL | 0.94 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, mad, furious, crazy, eager | relax, asleep, slow, sleep, dull | asleep, sleep, relax, awake, weary |
| RULE | 0.89 | department, federal, congress, legislative, secretary | department, secretary, administrative, legislative, congress | intimate, privately, public, individually, person | social, intimate, subjective, personality, professional |
| CHANGE | 0.91 | modify, adjust, adapt, variation, convert | modify, adjust, adapt, improve, revise | steady, persist, keep, continue, maintain | steady, keep, maintain, persist, forever |
| PARTICULAR | 0.89 | distinctive, uniquely, unusual, special, peculiarly | distinctive, unusual, special, peculiarly, uniquely | usual, ordinary, customary, standard, conventional | usual, conventional, standard, customary, widespread |
| ART | 0.89 | artist, artistic, aesthetic, collage, literary | artist, artistic, contemporary, collage, classical | technological, machinery, electrical, technical, apparatus | machinery, technological, electrical, apparatus, equipment |
| JOIN | 0.90 | merge, integrate, together, mingle, link | integrate, mingle, merge, bring, together | split, sever, isolate, apart, secede | eliminate, sever, withdraw, split, dissolve |
| VALUE | 0.94 | worth, important, cost, cherish, value | important, worth, cherish, cost, essential | buy, price, economical, simple, deal | buy, sell, sale, price, purchase |
| CARE | 0.93 | intently, thoroughly, neatly, properly, calmly | thoroughly, intently, comprehensively, properly, neatly | awkwardly, arbitrarily, deliberately, unconsciously, lightly | awkwardly, abruptly, unconsciously, arbitrarily, unexpectedly |
| TONE | 0.90 | heartily, helpfully, happily, grateful, thank | heartily, grateful, thank, happily, helpfully | savagely, furiously, violently, sharply, flatly | savagely, sharply, severely, violently, furiously |
| CONSUME | 0.94 | consume, chew, sip, bite, meal | consume, sip, chew, meal, bite | breathe, hurl, smell, discharge, breath | hurl, breathe, discharge, produce, utter |
| ABSTRACT | 0.92 | assumption, conception, sense, implication, suggestion | assumption, doctrine, implication, conception, argument | porch, floor, window, knock, wooden | porch, floor, upstairs, bedroom, room |
| MEASURE | 0.93 | percent, proportionately, calculate, decrease, probability | percent, calculate, decrease, increase, income | extent, magnitude, diameter, tall, scale | magnitude, extent, diameter, tall, scale |
| LONG | 0.90 | wooden, column, frame, wood, vertical | wooden, plate, frame, box, wagon | tie, bind, chain, fasten, curl | tie, cloth, fasten, bind, dress |
| SAY | 0.93 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, clamor, loudly | silence, silently, quietly, softly, rustle | silence, silently, quietly, secret, rustle |
| GRAIN | 0.91 | concrete, steel, massive, structure, carve | carve, concrete, structure, gouge, massive | aqueous, flow, drip, pour, effluent | aqueous, effluent, flow, drip, sewage |
| FIGHT | 0.91 | war, battle, conflict, soldier, fight | war, soldier, battle, army, military | competition, game, compete, competitive, sport | competition, game, compete, competitive, win |
| BODY | 0.94 | shoulder, neck, finger, chest, knee | neck, shoulder, chest, finger, knee | | |
| SEE | 0.94 | gaze, observe, glance, sight, stare | gaze, glance, observe, sight, stare | | |
| DO | 0.95 | undertake, accomplish, operate, enact, behave | undertake, operate, accomplish, behave, enact | | |
| PLACE | 0.92 | locate, position, neighborhood, country, town | neighborhood, district, land, country, town | | |
| TEXT | 0.94 | letter, article, paper, book, note | article, letter, book, publish, note | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| money | `VALUE(=0) GIVE(=+2) MEASURE(=+1) \| o` | 12 | cost, worth, price, value, expense |
| winter | `HEAT(=-2) INSIDE(=-1) BEGIN(=+1) \| o` | 2 | freeze, winter, snow, weather, temperature |
| child | `SEX(=-1) BIG(=-4) VALUE(=+2) \| o` | 1 | child, girl, dear, baby, beloved |
