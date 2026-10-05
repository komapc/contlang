# Обучение словаря корней при условии читаемости

Numberbatch, 2687 слов (без слов-полюсов), обучение 1880, **тест 807** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 19.0% | 68.9% | 94.9% | 5 | 0.425 | 0.277 |
| корни из полюсов, вес не главных 0.6 | 21.7% | 71.0% | 96.2% | 5 | 0.432 | 0.286 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 26.0% | 78.7% | 98.4% | 4 | 0.487 | 0.356 |

Сдвиг корней: cos(центр, исходный) в среднем 0.93 (минимум 0.85), cos(ось, исходная) в среднем 0.93 (минимум 0.88). итерация 1: на обучающих словах до шага top1 23.0%, cos 0.439; итерация 2: на обучающих словах до шага top1 39.2%, cos 0.514; итерация 3: на обучающих словах до шага top1 41.5%, cos 0.524.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.93 | fantastic, nice, lovely, magnificent, brilliant | fantastic, magnificent, brilliant, impressive, outstanding | worst, unspeakable, unfortunate, worse, monstrous | unspeakable, unfortunate, worse, worst, monstrous |
| BIG | 0.94 | gigantic, massive, tremendous, considerable, extensive | tremendous, massive, gigantic, considerable, extensive | smaller, few, slightly, larger, minimal | smaller, few, mere, slightly, minimal |
| NEAR | 0.90 | shut, neighborhood, closely, along, around | neighborhood, shut, downtown, park, entrance | afar, farther, distance, beyond, off | afar, farther, distance, beyond, journey |
| ABOVE | 0.92 | higher, rise, beyond, upper, climb | higher, rise, climb, raise, beyond | bottom, downstairs, drop, descend, decline | bottom, drop, descend, slide, decline |
| LIVE | 0.93 | live, vivid, vitally, life, healthy | vivid, vividly, healthy, live, vigorous | corpse, die, fatal, kill, murder | die, corpse, murder, fatal, kill |
| SAME | 0.95 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, equate, exact, correspond | differ, differently, distinctive, various, distinctly | differ, various, distinctive, differently, variety |
| TIME | 0.93 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, await, arrive | previous, previously, recently, recent, formerly | previous, recently, previously, recent, years |
| INSIDE | 0.94 | inner, deep, around, room, therein | inner, deep, basement, room, therein | outdoor, inner, porch, side, surface | outdoor, protective, inner, porch, protection |
| PART | 0.92 | pack, gather, assemble, variety, selection | pack, selection, team, organization, crowd | portion, dust, atom, part, texture | portion, dust, element, part, bite |
| SIDE | 0.93 | advance, rearward, before, side, precede | advance, southward, northward, westward, rearward | rearward, shoulder, return, reverse, forth | rearward, reverse, return, shoulder, tilt |
| KNOW | 0.91 | understand, knowledge, conscious, realize, sure | understand, knowledge, inform, learn, perceive | dumb, indifferent, stupid, helpless, silly | stupid, dumb, silly, fool, absurd |
| WANT | 0.90 | wish, need, cherish, urge, seek | wish, need, hope, cherish, seek | despise, dislike, resent, oppose, deny | despise, oppose, denounce, condemn, dislike |
| HEAT | 0.95 | burn, heat, temperature, thermal, glow | burn, heat, glow, erupt, sun | freeze, snow, winter, temperature, melt | freeze, snow, winter, weather, temperature |
| BEGIN | 0.93 | conclusion, culminate, ultimate, terminate, complete | conclusion, fourth, sixth, ninth, victory | initiate, initially, onset, launch, early | initiate, initially, onset, launch, originate |
| GIVE | 0.88 | provide, receive, lend, contribute, accept | provide, receive, accept, submit, lend | capture, catch, grasp, hold, acquire | catch, capture, grasp, pull, acquire |
| TOUCH | 0.94 | tough, severe, rugged, strong, stiffly | tough, strong, severe, rugged, fierce | gentle, sweet, porous, smooth, delicate | sweet, tender, delicate, gentle, porous |
| MATTER | 0.93 | exhaust, oxygen, breath, breathe, atmosphere | oxygen, respiratory, exhaust, breath, atmosphere | concrete, steel, wood, iron, sturdy | concrete, steel, wood, wooden, iron |
| SEX | 0.95 | papa, boy, comrade, man, guy | papa, boy, comrade, man, guy | girl, woman, parent, family, lady | girl, woman, parent, lady, family |
| HAPPEN | 0.92 | impact, conclusion, affect, inevitable, occurrence | impact, occurrence, affect, implication, occur | motive, originate, explanation, main, basis | motive, originate, main, true, explanation |
| THINK | 0.88 | select, settle, define, assess, evaluate | assess, evaluate, define, identify, establish | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, suspect, think, question |
| CAN | 0.93 | convenient, efficient, conceivably, likely, probable | efficient, convenient, effective, useful, competent | tough, difficulty, painful, desperate, awkward | difficulty, desperate, tough, desperately, struggle |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | invariably, whole, basically, practically, totally | nowhere, hardly, anymore, scarcely, barely | hardly, certainly, nowhere, scarcely, apparently |
| SOMEONE | 0.96 | personally, someone, honestly, anyway, dear | anyway, honestly, personally, anyhow, maybe | people, either, individually, own, someone | people, either, several, various, individually |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, chicken, hen, bird, farm | concrete, dirt, hill, mud, mountain | dirt, mud, concrete, sidewalk, hill |
| MOVE | 0.94 | quick, speed, hasten, rapid, accelerate | quick, speed, rapid, hasten, accelerate | sit, halt, keep, linger, continue | sit, halt, pause, keep, while |
| FEEL | 0.93 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, furious, mad, eager, crazy | relax, asleep, slow, sleep, dull | asleep, sleep, awake, relax, weary |
| RULE | 0.89 | department, federal, congress, legislative, secretary | secretary, department, administrative, legislative, congress | intimate, privately, public, individually, person | social, intimate, subjective, personality, professional |
| CHANGE | 0.92 | modify, adjust, adapt, variation, convert | modify, adjust, adapt, affect, improve | steady, persist, keep, continue, maintain | steady, persist, keep, maintain, continuous |
| PARTICULAR | 0.91 | distinctive, uniquely, unusual, special, peculiarly | distinctive, unusual, special, peculiarly, uniquely | usual, ordinary, customary, standard, conventional | usual, commonly, conventional, customary, standard |
| ART | 0.88 | artist, artistic, aesthetic, collage, literary | artist, artistic, literary, contemporary, collage | technological, machinery, electrical, technical, apparatus | technological, electrical, machinery, technical, industrial |
| JOIN | 0.89 | merge, integrate, together, mingle, link | integrate, mingle, merge, collaborate, together | split, sever, isolate, apart, secede | eliminate, sever, withdraw, dissolve, split |
| VALUE | 0.92 | worth, important, cost, cherish, value | important, worth, cherish, essential, critical | buy, price, economical, simple, deal | buy, sell, purchase, price, sale |
| CARE | 0.91 | intently, thoroughly, neatly, properly, calmly | thoroughly, comprehensively, intently, properly, neatly | awkwardly, arbitrarily, deliberately, unconsciously, lightly | awkwardly, abruptly, unconsciously, unexpectedly, arbitrarily |
| TONE | 0.89 | heartily, helpfully, happily, grateful, thank | heartily, grateful, happily, thank, glad | savagely, furiously, violently, sharply, flatly | savagely, severely, sharply, violently, furiously |
| CONSUME | 0.94 | consume, chew, sip, bite, meal | consume, chew, sip, bite, meal | breathe, hurl, smell, discharge, breath | hurl, produce, discharge, utter, breathe |
| ABSTRACT | 0.92 | assumption, conception, sense, implication, suggestion | assumption, implication, doctrine, conception, interpretation | porch, floor, window, knock, wooden | porch, floor, bedroom, upstairs, room |
| MEASURE | 0.92 | percent, proportionately, calculate, decrease, probability | percent, decrease, income, calculate, increase | extent, magnitude, diameter, tall, scale | extent, magnitude, scale, depth, diameter |
| LONG | 0.91 | wooden, column, frame, wood, vertical | wooden, column, frame, plate, box | tie, bind, chain, fasten, curl | tie, cloth, fasten, bind, dress |
| SAY | 0.94 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, clamor, loudly | silence, silently, quietly, softly, rustle | silence, silently, quietly, softly, rustle |
| GRAIN | 0.92 | concrete, steel, massive, structure, carve | carve, concrete, structure, steel, shape | aqueous, flow, drip, pour, effluent | aqueous, effluent, drip, flow, sewage |
| BODY | 0.93 | shoulder, neck, finger, chest, knee | shoulder, neck, chest, knee, finger | | |
| SEE | 0.92 | gaze, observe, glance, sight, stare | glance, gaze, sight, stare, observe | | |
| DO | 0.94 | undertake, accomplish, operate, enact, behave | operate, undertake, behave, accomplish, conduct | | |
| PLACE | 0.92 | locate, position, neighborhood, country, town | neighborhood, country, district, land, locate | | |
| FIGHT | 0.96 | struggle, contend, debate, argument, argue | struggle, contend, debate, soldier, argument | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| teacher | `ART(=+1) SEX(=0) RULE(=0) \| o` | 5 | artistic, artist, literary, academic, teacher |
| city | `PLACE RULE(=+2) MATTER(=0) \| o` | 3 | district, department, city, municipal, town |
| money | `VALUE(=0) GIVE(=+2) MEASURE(=+1) \| o` | 12 | cost, worth, price, value, expense |
| winter | `HEAT(=-2) INSIDE(=-1) BEGIN(=+1) \| o` | 1 | winter, freeze, snow, weather, temperature |
| child | `SEX(=-1) BIG(=-4) VALUE(=+2) \| o` | 1 | child, girl, baby, kid, parent |
