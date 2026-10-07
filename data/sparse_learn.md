# Обучение словаря корней при условии читаемости

Numberbatch, 2698 слов (без слов-полюсов), обучение 1888, **тест 810** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 23.7% | 74.8% | 96.2% | 4 | 0.432 | 0.287 |
| корни из полюсов, вес не главных 0.6 | 25.3% | 75.7% | 96.2% | 4 | 0.440 | 0.291 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 28.8% | 80.6% | 98.4% | 3 | 0.495 | 0.360 |

Сдвиг корней: cos(центр, исходный) в среднем 0.93 (минимум 0.85), cos(ось, исходная) в среднем 0.92 (минимум 0.86). итерация 1: на обучающих словах до шага top1 21.9%, cos 0.440; итерация 2: на обучающих словах до шага top1 38.0%, cos 0.517; итерация 3: на обучающих словах до шага top1 41.4%, cos 0.528.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.95 | fantastic, nice, lovely, magnificent, brilliant | fantastic, nice, magnificent, lovely, beautiful | worst, unspeakable, unfortunate, worse, monstrous | unspeakable, worst, monstrous, worse, unfortunate |
| BIG | 0.94 | gigantic, massive, tremendous, considerable, extensive | massive, gigantic, tremendous, extensive, considerable | smaller, few, slightly, larger, minimal | smaller, few, mere, minimal, slightly |
| NEAR | 0.93 | shut, neighborhood, closely, along, around | neighborhood, downtown, park, station, corner | afar, farther, distance, beyond, off | afar, farther, distance, beyond, journey |
| ABOVE | 0.93 | higher, rise, beyond, upper, climb | higher, rise, climb, upper, raise | bottom, downstairs, drop, descend, decline | drop, descend, bottom, decline, fall |
| LIVE | 0.94 | live, vivid, vitally, life, healthy | live, life, healthy, vivid, vitally | corpse, die, fatal, kill, murder | die, corpse, murder, fatal, kill |
| SAME | 0.89 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, equate, correspond, exact | differ, differently, distinctive, various, distinctly | distinctive, peculiar, characteristically, variety, unusual |
| TIME | 0.93 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, await, hereafter | previous, previously, recently, recent, formerly | previously, previous, recently, years, formerly |
| INSIDE | 0.96 | inner, deep, around, room, therein | inner, deep, basement, penetrate, hole | outdoor, inner, porch, side, surface | outdoor, inner, porch, foreign, protective |
| PART | 0.88 | pack, gather, assemble, variety, selection | organization, collective, association, team, congregation | portion, dust, atom, part, texture | dust, portion, atom, texture, element |
| SIDE | 0.93 | advance, rearward, before, side, precede | advance, rearward, side, northward, southward | rearward, shoulder, return, reverse, forth | rearward, return, reverse, shoulder, corner |
| KNOW | 0.92 | understand, knowledge, conscious, realize, sure | understand, learn, inform, knowledge, realize | dumb, indifferent, stupid, helpless, silly | dumb, stupid, silly, fool, vague |
| WANT | 0.90 | wish, need, cherish, urge, seek | wish, need, hope, cherish, strive | despise, dislike, resent, oppose, deny | oppose, despise, denounce, dislike, condemn |
| HEAT | 0.94 | burn, heat, temperature, thermal, glow | burn, heat, glow, erupt, explode | freeze, snow, winter, temperature, melt | freeze, snow, winter, temperature, weather |
| BEGIN | 0.93 | conclusion, culminate, ultimate, terminate, complete | conclusion, fourth, ultimate, sixth, ninth | initiate, initially, onset, launch, early | initiate, initially, originate, launch, onset |
| GIVE | 0.89 | provide, receive, lend, contribute, accept | provide, lend, contribute, receive, accept | capture, catch, grasp, hold, acquire | capture, catch, grasp, pull, hold |
| TOUCH | 0.95 | tough, severe, rugged, strong, stiffly | tough, strong, severe, rugged, sturdy | gentle, sweet, porous, smooth, delicate | sweet, porous, thick, smooth, texture |
| SEX | 0.95 | papa, boy, comrade, man, guy | papa, boy, comrade, man, guy | girl, woman, parent, family, lady | girl, woman, parent, lady, child |
| HAPPEN | 0.91 | impact, conclusion, affect, inevitable, occurrence | impact, occur, affect, occurrence, happen | motive, originate, explanation, main, basis | main, originate, primary, motive, explanation |
| THINK | 0.88 | select, settle, define, assess, evaluate | assess, evaluate, examine, define, identify | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, think, contemplate, question |
| CAN | 0.92 | convenient, efficient, conceivably, likely, probable | efficient, convenient, effective, adequate, useful | tough, difficulty, painful, desperate, awkward | difficulty, tough, task, struggle, desperate |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | invariably, practically, basically, whole, usually | nowhere, hardly, anymore, scarcely, barely | hardly, nowhere, certainly, apparently, evidently |
| SOMEONE | 0.96 | personally, someone, honestly, anyway, dear | anyway, anyhow, maybe, honestly, guess | people, either, individually, own, someone | people, either, individually, several, respectively |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, farm, barn, chicken, milk | rock, concrete, dirt, hill, mud | rock, dirt, mud, concrete, soil |
| MOVE | 0.92 | quick, speed, hasten, rapid, accelerate | speed, quick, rapid, hasten, accelerate | sit, halt, keep, linger, continue | sit, pause, linger, occupy, hold |
| FEEL | 0.94 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, eager, excitement, furious, excitedly | relax, asleep, slow, sleep, dull | sleep, asleep, relax, awake, weary |
| RULE | 0.86 | enforce, government, court, legislative, regulate | sanction, legislative, commission, enforce, court | privately, intimate, public, individually, own | intimate, social, psychological, privately, subjective |
| CHANGE | 0.91 | modify, adjust, adapt, variation, convert | modify, adjust, adapt, improve, revise | steady, persist, keep, continue, maintain | steady, maintain, keep, persist, continue |
| ART | 0.88 | artist, artistic, aesthetic, collage, literary | artistic, artist, classical, contemporary, cultural | technological, machinery, electrical, technical, apparatus | technological, machinery, electrical, technical, industrial |
| JOIN | 0.87 | merge, integrate, together, mingle, link | integrate, mingle, merge, involve, collaborate | split, sever, isolate, apart, secede | eliminate, sever, withdraw, dissolve, reduce |
| VALUE | 0.95 | worth, important, cost, cherish, value | worth, important, cherish, value, beloved | buy, price, economical, simple, deal | price, buy, purchase, sale, deal |
| CARE | 0.89 | intently, thoroughly, neatly, properly, calmly | comprehensively, thoroughly, properly, neatly, intently | awkwardly, arbitrarily, deliberately, unconsciously, lightly | awkwardly, abruptly, unconsciously, unexpectedly, occasionally |
| TONE | 0.91 | heartily, helpfully, happily, grateful, thank | grateful, heartily, thank, helpfully, happily | savagely, furiously, violently, sharply, flatly | savagely, severely, violently, sharply, flatly |
| MOOD | 0.96 | humorous, happy, laugh, delightful, joy | humorous, happy, laugh, delightful, chuckle | sad, despair, desperate, regret, weep | sad, despair, regret, weep, desperate |
| CONSUME | 0.92 | consume, chew, sip, bite, meal | consume, meal, chew, sip, food | breathe, hurl, smell, discharge, breath | hurl, breathe, discharge, smell, throw |
| ABSTRACT | 0.89 | assumption, conception, sense, implication, suggestion | assumption, doctrine, philosophical, argument, theoretical | porch, floor, window, knock, wooden | floor, porch, room, bedroom, upstairs |
| MEASURE | 0.91 | percent, proportionately, calculate, decrease, probability | percent, calculate, estimate, income, probability | extent, magnitude, diameter, tall, scale | magnitude, extent, depth, tall, diameter |
| LONG | 0.92 | wooden, column, frame, wood, vertical | wooden, wagon, wheel, frame, truck | tie, bind, chain, fasten, curl | tie, bind, fasten, chain, cloth |
| SAY | 0.93 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, loudly, clamor | silence, silently, quietly, softly, rustle | silently, silence, quietly, softly, rustle |
| GRAIN | 0.94 | concrete, massive, metal, steel, structure | concrete, steel, metal, carve, structure | exhaust, oxygen, breath, breathe, atmosphere | oxygen, chlorine, fluid, breath, liquid |
| FIGHT | 0.89 | war, battle, conflict, soldier, fight | war, soldier, battle, military, army | competition, game, compete, competitive, sport | competition, compete, win, game, competitive |
| DO | 0.90 | apparatus, equipment, method, useful, object | apparatus, method, technique, equipment, useful | producer, musician, artist, writer, composer | producer, manager, director, writer, employee |
| BODY | 0.96 | shoulder, neck, finger, chest, knee | shoulder, neck, chest, finger, knee | | |
| SEE | 0.95 | gaze, observe, glance, sight, stare | gaze, glance, sight, observe, stare | | |
| PLACE | 0.89 | locate, position, neighborhood, country, town | country, land, neighborhood, district, suburb | | |
| TEXT | 0.94 | letter, article, paper, book, note | article, letter, book, note, publish | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| city | `PLACE NEAR(=+1) RULE(=+3) \| o` | 5 | district, town, neighborhood, downtown, city |
| doctor | `DO(=-2) SEX(=+1) RULE(=-1) \| o` | 12 | employee, manager, director, officer, professional |
