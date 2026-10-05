# Обучение словаря корней при условии читаемости

Numberbatch, 2701 слов (без слов-полюсов), обучение 1890, **тест 811** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 20.8% | 71.9% | 96.4% | 4 | 0.427 | 0.295 |
| корни из полюсов, вес не главных 0.6 | 22.8% | 73.6% | 96.9% | 4 | 0.435 | 0.300 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 28.5% | 81.5% | 98.8% | 3 | 0.491 | 0.364 |

Сдвиг корней: cos(центр, исходный) в среднем 0.92 (минимум 0.85), cos(ось, исходная) в среднем 0.92 (минимум 0.85). итерация 1: на обучающих словах до шага top1 23.0%, cos 0.440; итерация 2: на обучающих словах до шага top1 39.3%, cos 0.515; итерация 3: на обучающих словах до шага top1 41.3%, cos 0.525.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.93 | fantastic, nice, lovely, magnificent, brilliant | fantastic, magnificent, lovely, nice, brilliant | worst, unspeakable, unfortunate, worse, monstrous | worst, worse, unfortunate, unspeakable, monstrous |
| BIG | 0.94 | gigantic, massive, tremendous, considerable, extensive | tremendous, massive, gigantic, considerable, extensive | smaller, few, slightly, larger, minimal | smaller, few, minimal, mere, slightly |
| NEAR | 0.92 | shut, neighborhood, closely, along, around | neighborhood, station, downtown, along, around | afar, farther, distance, beyond, off | afar, farther, distance, beyond, journey |
| ABOVE | 0.91 | higher, rise, beyond, upper, climb | higher, rise, climb, raise, beyond | bottom, downstairs, drop, descend, decline | drop, descend, decline, bottom, fall |
| LIVE | 0.94 | live, vivid, vitally, life, healthy | vivid, vividly, vitally, live, spirit | corpse, die, fatal, kill, murder | die, corpse, murder, fatal, kill |
| SAME | 0.89 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, exact, correspond, exactly | differ, differently, distinctive, various, distinctly | distinctive, characteristically, peculiar, distinctly, differ |
| TIME | 0.93 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, await, arrive | previous, previously, recently, recent, formerly | previous, recently, previously, recent, years |
| INSIDE | 0.95 | inner, deep, around, room, therein | inner, deep, hole, basement, room | outdoor, inner, porch, side, surface | outdoor, inner, porch, protective, repel |
| PART | 0.93 | pack, gather, assemble, variety, selection | collective, team, pack, assemble, crowd | portion, dust, atom, part, texture | dust, atom, substance, portion, texture |
| SIDE | 0.93 | advance, rearward, before, side, precede | advance, rearward, side, straight, northward | rearward, shoulder, return, reverse, forth | rearward, recover, return, restore, reverse |
| KNOW | 0.92 | understand, knowledge, conscious, realize, sure | understand, learn, realize, perceive, knowledge | dumb, indifferent, stupid, helpless, silly | dumb, stupid, silly, vague, absurd |
| WANT | 0.92 | wish, need, cherish, urge, seek | wish, need, hope, seek, cherish | despise, dislike, resent, oppose, deny | despise, oppose, denounce, dislike, condemn |
| HEAT | 0.93 | burn, heat, temperature, thermal, glow | burn, heat, glow, erupt, light | freeze, snow, winter, temperature, melt | freeze, snow, winter, temperature, weather |
| BEGIN | 0.93 | conclusion, culminate, ultimate, terminate, complete | conclusion, ultimate, fourth, culminate, sixth | initiate, initially, onset, launch, early | initiate, initially, launch, onset, originate |
| GIVE | 0.89 | provide, receive, lend, contribute, accept | provide, contribute, lend, receive, accept | capture, catch, grasp, hold, acquire | capture, grasp, catch, pull, hold |
| TOUCH | 0.94 | tough, severe, rugged, strong, stiffly | tough, strong, rugged, fierce, severe | gentle, sweet, porous, smooth, delicate | sweet, gentle, tender, smooth, delicate |
| SEX | 0.95 | papa, boy, comrade, man, guy | papa, boy, comrade, man, guy | girl, woman, parent, family, lady | girl, woman, parent, lady, child |
| HAPPEN | 0.91 | impact, conclusion, affect, inevitable, occurrence | impact, affect, occurrence, occur, incident | motive, originate, explanation, main, basis | originate, primary, main, motive, native |
| THINK | 0.85 | select, settle, define, assess, evaluate | assess, evaluate, define, declare, establish | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, think, guess, suspect |
| CAN | 0.93 | convenient, efficient, conceivably, likely, probable | convenient, efficient, effective, adequate, useful | tough, difficulty, painful, desperate, awkward | difficulty, tough, desperate, task, struggle |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | whole, basically, practically, invariably, totally | nowhere, hardly, anymore, scarcely, barely | hardly, certainly, indeed, nowhere, evidently |
| SOMEONE | 0.95 | personally, someone, honestly, anyway, dear | personally, anyway, maybe, honestly, anyhow | people, either, individually, own, someone | people, either, several, individually, otherwise |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, bird, barn, chicken, duck | rock, concrete, dirt, hill, mud | rock, mud, dirt, concrete, muddy |
| MOVE | 0.94 | quick, speed, hasten, rapid, accelerate | speed, quick, hasten, accelerate, pace | sit, halt, keep, linger, continue | sit, halt, keep, pause, while |
| FEEL | 0.94 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, mad, furious, excitement, eager | relax, asleep, slow, sleep, dull | sleep, asleep, relax, awake, weary |
| RULE | 0.88 | department, federal, congress, legislative, secretary | legislative, president, congress, secretary, chief | intimate, privately, public, individually, person | intimate, social, public, professional, subjective |
| CHANGE | 0.90 | modify, adjust, adapt, variation, convert | modify, adjust, adapt, improve, affect | steady, persist, keep, continue, maintain | steady, persist, maintain, keep, continue |
| ART | 0.89 | artist, artistic, aesthetic, collage, literary | artistic, artist, collage, contemporary, classical | technological, machinery, electrical, technical, apparatus | electrical, technological, machinery, industrial, electric |
| JOIN | 0.89 | merge, integrate, together, mingle, link | integrate, mingle, merge, bring, engage | split, sever, isolate, apart, secede | eliminate, sever, withdraw, reduce, dissolve |
| VALUE | 0.94 | worth, important, cost, cherish, value | worth, important, cherish, value, cost | buy, price, economical, simple, deal | price, deal, buy, sale, purchase |
| CARE | 0.91 | intently, thoroughly, neatly, properly, calmly | thoroughly, properly, comprehensively, correctly, intently | awkwardly, arbitrarily, deliberately, unconsciously, lightly | awkwardly, abruptly, unconsciously, unexpectedly, violently |
| TONE | 0.92 | heartily, helpfully, happily, grateful, thank | grateful, heartily, thank, helpfully, welcome | savagely, furiously, violently, sharply, flatly | savagely, violently, severely, sharply, furiously |
| CONSUME | 0.92 | consume, chew, sip, bite, meal | consume, sip, chew, meal, bite | breathe, hurl, smell, discharge, breath | discharge, hurl, transmit, breathe, flow |
| ABSTRACT | 0.92 | assumption, conception, sense, implication, suggestion | assumption, implication, doctrine, interpretation, argument | porch, floor, window, knock, wooden | floor, porch, room, bedroom, upstairs |
| MEASURE | 0.92 | percent, proportionately, calculate, decrease, probability | percent, income, calculate, estimate, decrease | extent, magnitude, diameter, tall, scale | magnitude, extent, diameter, tall, scale |
| LONG | 0.89 | wooden, column, frame, wood, vertical | wooden, wagon, wheel, truck, frame | tie, bind, chain, fasten, curl | tie, cloth, bind, fasten, dress |
| SAY | 0.93 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, loudly, clamor | silence, silently, quietly, softly, rustle | silently, silence, quietly, softly, rustle |
| GRAIN | 0.93 | concrete, massive, metal, steel, structure | concrete, carve, steel, metal, structure | exhaust, oxygen, breath, breathe, atmosphere | oxygen, exhaust, breath, liquid, breathe |
| FIGHT | 0.87 | war, battle, conflict, soldier, fight | war, soldier, army, military, battle | competition, game, compete, competitive, sport | competition, compete, win, competitive, game |
| DO | 0.91 | apparatus, equipment, method, useful, object | apparatus, method, equipment, technique, system | producer, musician, artist, writer, composer | producer, director, manager, writer, musician |
| BODY | 0.94 | shoulder, neck, finger, chest, knee | neck, shoulder, chest, muscle, knee | | |
| SEE | 0.94 | gaze, observe, glance, sight, stare | gaze, glance, sight, observe, stare | | |
| PLACE | 0.93 | locate, position, neighborhood, country, town | country, neighborhood, land, district, facility | | |
| TEXT | 0.94 | letter, article, paper, book, note | article, letter, publish, note, paper | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| teacher | `DO(=-2) SEX(=0) ART(=+1) \| o` | 8 | artist, musician, producer, composer, director |
| city | `PLACE RULE(=+2) NEAR(=0) \| o` | 4 | district, town, central, city, downtown |
| doctor | `SEX(=+1) DO(=-2) RULE(=-2) \| o` | 9 | parent, employee, papa, comrade, family |
