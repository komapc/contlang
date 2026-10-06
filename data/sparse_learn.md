# Обучение словаря корней при условии читаемости

Numberbatch, 2700 слов (без слов-полюсов), обучение 1889, **тест 811** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 21.3% | 73.5% | 97.0% | 5 | 0.431 | 0.290 |
| корни из полюсов, вес не главных 0.6 | 23.8% | 74.5% | 96.9% | 4 | 0.439 | 0.291 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 25.6% | 80.6% | 98.8% | 3 | 0.494 | 0.367 |

Сдвиг корней: cos(центр, исходный) в среднем 0.92 (минимум 0.85), cos(ось, исходная) в среднем 0.92 (минимум 0.86). итерация 1: на обучающих словах до шага top1 22.3%, cos 0.437; итерация 2: на обучающих словах до шага top1 39.3%, cos 0.514; итерация 3: на обучающих словах до шага top1 42.8%, cos 0.525.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.93 | fantastic, nice, lovely, magnificent, brilliant | fantastic, nice, magnificent, lovely, outstanding | worst, unspeakable, unfortunate, worse, monstrous | unspeakable, worst, unfortunate, worse, monstrous |
| BIG | 0.94 | gigantic, massive, tremendous, considerable, extensive | massive, gigantic, tremendous, extensive, considerable | smaller, few, slightly, larger, minimal | smaller, few, minimal, mere, slender |
| NEAR | 0.92 | shut, neighborhood, closely, along, around | neighborhood, downtown, park, shut, corner | afar, farther, distance, beyond, off | afar, farther, distance, beyond, journey |
| ABOVE | 0.92 | higher, rise, beyond, upper, climb | higher, rise, climb, upper, raise | bottom, downstairs, drop, descend, decline | bottom, drop, descend, slide, decline |
| LIVE | 0.94 | live, vivid, vitally, life, healthy | vivid, vividly, healthy, life, live | corpse, die, fatal, kill, murder | die, corpse, fatal, murder, kill |
| SAME | 0.90 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, correspond, equate, resemble | differ, differently, distinctive, various, distinctly | distinctive, peculiar, characteristically, unusual, variety |
| TIME | 0.93 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, hereafter, thereafter | previous, previously, recently, recent, formerly | previously, recently, previous, formerly, years |
| INSIDE | 0.95 | inner, deep, around, room, therein | inner, deep, basement, penetrate, hole | outdoor, inner, porch, side, surface | outdoor, porch, inner, protective, fence |
| PART | 0.88 | pack, gather, assemble, variety, selection | organization, collective, association, team, congregation | portion, dust, atom, part, texture | dust, atom, portion, element, substance |
| SIDE | 0.92 | advance, rearward, before, side, precede | advance, southward, northward, rearward, side | rearward, shoulder, return, reverse, forth | rearward, reverse, shoulder, return, bottom |
| KNOW | 0.92 | understand, knowledge, conscious, realize, sure | understand, inform, learn, realize, knowledge | dumb, indifferent, stupid, helpless, silly | dumb, stupid, fool, silly, absurd |
| WANT | 0.90 | wish, need, cherish, urge, seek | wish, need, hope, strive, seek | despise, dislike, resent, oppose, deny | oppose, despise, denounce, dislike, condemn |
| HEAT | 0.94 | burn, heat, temperature, thermal, glow | burn, heat, glow, erupt, sun | freeze, snow, winter, temperature, melt | freeze, snow, winter, temperature, weather |
| BEGIN | 0.93 | conclusion, culminate, ultimate, terminate, complete | conclusion, fourth, ultimate, ninth, sixth | initiate, initially, onset, launch, early | initiate, originate, initially, onset, launch |
| GIVE | 0.89 | provide, receive, lend, contribute, accept | provide, contribute, lend, receive, accept | capture, catch, grasp, hold, acquire | catch, grasp, capture, pull, hold |
| TOUCH | 0.94 | tough, severe, rugged, strong, stiffly | tough, severe, strong, rugged, fierce | gentle, sweet, porous, smooth, delicate | sweet, porous, tender, delicate, texture |
| SEX | 0.96 | papa, boy, comrade, man, guy | papa, boy, man, comrade, guy | girl, woman, parent, family, lady | girl, woman, parent, child, lady |
| HAPPEN | 0.90 | impact, conclusion, affect, inevitable, occurrence | impact, occur, affect, happen, occurrence | motive, originate, explanation, main, basis | main, originate, primary, motive, primarily |
| THINK | 0.88 | select, settle, define, assess, evaluate | assess, evaluate, identify, define, examine | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, think, worry, suspect |
| CAN | 0.93 | convenient, efficient, conceivably, likely, probable | convenient, efficient, effective, adequate, competent | tough, difficulty, painful, desperate, awkward | difficulty, tough, desperate, task, struggle |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | invariably, basically, whole, practically, usually | nowhere, hardly, anymore, scarcely, barely | hardly, certainly, nowhere, evidently, apparently |
| SOMEONE | 0.95 | personally, someone, honestly, anyway, dear | anyway, honestly, personally, maybe, anyhow | people, either, individually, own, someone | people, either, men, several, someone |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, chicken, farm, barn, hen | rock, concrete, dirt, hill, mud | rock, dirt, mud, concrete, soil |
| MOVE | 0.93 | quick, speed, hasten, rapid, accelerate | quick, speed, rapid, gallop, pace | sit, halt, keep, linger, continue | sit, halt, pause, keep, linger |
| FEEL | 0.94 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, eager, furious, excitement, excitedly | relax, asleep, slow, sleep, dull | sleep, asleep, awake, relax, disturb |
| RULE | 0.86 | enforce, government, court, legislative, regulate | commission, legislative, sanction, judge, court | privately, intimate, public, individually, own | intimate, privately, social, sexual, public |
| CHANGE | 0.90 | modify, adjust, adapt, variation, convert | modify, adjust, adapt, improve, revise | steady, persist, keep, continue, maintain | steady, maintain, persist, keep, continuous |
| ART | 0.89 | artist, artistic, aesthetic, collage, literary | artistic, artist, classical, contemporary, culture | technological, machinery, electrical, technical, apparatus | technological, electrical, machinery, technical, industrial |
| JOIN | 0.86 | merge, integrate, together, mingle, link | integrate, mingle, involve, bring, introduce | split, sever, isolate, apart, secede | eliminate, sever, dissolve, split, withdraw |
| VALUE | 0.94 | worth, important, cost, cherish, value | important, worth, value, cherish, cost | buy, price, economical, simple, deal | price, buy, purchase, sale, deal |
| CARE | 0.92 | intently, thoroughly, neatly, properly, calmly | thoroughly, properly, comprehensively, neatly, intently | awkwardly, arbitrarily, deliberately, unconsciously, lightly | abruptly, awkwardly, unexpectedly, unconsciously, suddenly |
| TONE | 0.90 | heartily, helpfully, happily, grateful, thank | heartily, thank, helpfully, grateful, happily | savagely, furiously, violently, sharply, flatly | savagely, severely, violently, furiously, sharply |
| CONSUME | 0.91 | consume, chew, sip, bite, meal | consume, meal, sip, chew, food | breathe, hurl, smell, discharge, breath | hurl, discharge, transmit, produce, dispose |
| ABSTRACT | 0.91 | assumption, conception, sense, implication, suggestion | assumption, implication, argument, conception, explanation | porch, floor, window, knock, wooden | floor, porch, upstairs, room, knock |
| MEASURE | 0.92 | percent, proportionately, calculate, decrease, probability | percent, calculate, estimate, decrease, income | extent, magnitude, diameter, tall, scale | extent, magnitude, diameter, tall, depth |
| LONG | 0.90 | wooden, column, frame, wood, vertical | wagon, wooden, truck, wheel, ship | tie, bind, chain, fasten, curl | tie, cloth, bind, fasten, curl |
| SAY | 0.93 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, loudly, clamor | silence, silently, quietly, softly, rustle | silently, silence, quietly, softly, rustle |
| GRAIN | 0.93 | concrete, massive, metal, steel, structure | concrete, carve, steel, metal, structure | exhaust, oxygen, breath, breathe, atmosphere | oxygen, chlorine, liquid, fluid, breath |
| FIGHT | 0.90 | war, battle, conflict, soldier, fight | war, soldier, battle, army, military | competition, game, compete, competitive, sport | competition, compete, win, game, competitive |
| DO | 0.88 | apparatus, equipment, method, useful, object | apparatus, method, technique, equipment, use | producer, musician, artist, writer, composer | producer, director, manager, writer, employee |
| BODY | 0.94 | shoulder, neck, finger, chest, knee | shoulder, neck, chest, finger, cheek | | |
| SEE | 0.94 | gaze, observe, glance, sight, stare | glance, gaze, observe, sight, stare | | |
| PLACE | 0.90 | locate, position, neighborhood, country, town | country, land, neighborhood, district, town | | |
| TEXT | 0.95 | letter, article, paper, book, note | article, letter, book, publish, note | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| city | `PLACE NEAR(=+1) RULE(=+3) \| o` | 8 | district, town, neighborhood, downtown, park |
| winter | `HEAT(=-2) BEGIN(=+1) TIME(=0) \| o` | 1 | winter, freeze, snow, summer, weather |
| doctor | `SEX(=0) DO(=-2) RULE(=0) \| o` | 22 | parent, papa, officer, family, employee |
