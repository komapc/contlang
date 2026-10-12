# Обучение словаря корней при условии читаемости

Numberbatch, 2727 слов (без слов-полюсов), обучение 1908, **тест 819** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 18.2% | 70.3% | 94.0% | 5 | 0.413 | 0.275 |
| корни из полюсов, вес не главных 0.6 | 18.7% | 70.2% | 95.4% | 5 | 0.420 | 0.283 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.6) | 26.4% | 79.0% | 97.9% | 4 | 0.480 | 0.348 |

Сдвиг корней: cos(центр, исходный) в среднем 0.92 (минимум 0.85), cos(ось, исходная) в среднем 0.91 (минимум 0.85). итерация 1: на обучающих словах до шага top1 19.4%, cos 0.428; итерация 2: на обучающих словах до шага top1 37.1%, cos 0.512; итерация 3: на обучающих словах до шага top1 40.1%, cos 0.524.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.92 | fantastic, nice, lovely, magnificent, brilliant | fantastic, magnificent, lovely, impressive, outstanding | worst, unspeakable, unfortunate, worse, monstrous | worse, worst, unspeakable, terribly, unfortunate |
| BIG | 0.93 | gigantic, massive, tremendous, considerable, extensive | massive, gigantic, tremendous, extensive, considerable | smaller, few, slightly, larger, minimal | smaller, few, slightly, minimal, relatively |
| NEAR | 0.92 | shut, neighborhood, closely, along, around | shut, center, downtown, corner, around | afar, farther, distance, beyond, off | afar, farther, distance, beyond, somewhere |
| ABOVE | 0.92 | higher, rise, beyond, upper, climb | higher, rise, climb, raise, upper | bottom, downstairs, drop, descend, decline | bottom, drop, decline, descend, downstairs |
| LIVE | 0.95 | live, vivid, vitally, life, healthy | vitally, healthy, vigorous, vivid, spirit | corpse, die, fatal, kill, murder | corpse, die, murder, kill, fatal |
| SAME | 0.89 | comparable, equivalent, equally, similarly, equate | equivalent, comparable, exact, equate, correspond | differ, differently, distinctive, various, distinctly | distinctive, characteristically, peculiar, variety, distinctly |
| TIME | 0.92 | shortly, sometime, someday, hereafter, await | shortly, await, sometime, arrive, someday | previous, previously, recently, recent, formerly | previous, previously, recently, recent, years |
| INSIDE | 0.93 | inner, deep, around, room, therein | inner, room, basement, house, bedroom | outdoor, inner, porch, side, surface | outdoor, porch, protective, inner, protection |
| PART | 0.88 | pack, gather, assemble, variety, selection | organization, collective, team, association, crowd | portion, dust, atom, part, texture | dust, atom, substance, portion, element |
| SIDE | 0.92 | advance, rearward, before, side, precede | advance, southward, northward, side, rearward | rearward, shoulder, return, reverse, forth | rearward, reverse, return, shoulder, recover |
| KNOW | 0.88 | understand, knowledge, conscious, realize, sure | inform, understand, learn, knowledge, tell | dumb, indifferent, stupid, helpless, silly | dumb, stupid, silly, fool, absurd |
| WANT | 0.89 | wish, need, cherish, urge, seek | wish, need, cherish, hope, urge | despise, dislike, resent, oppose, deny | despise, oppose, dislike, denounce, resent |
| HEAT | 0.95 | burn, heat, temperature, thermal, glow | heat, burn, glow, light, sun | freeze, snow, winter, coldly, temperature | freeze, snow, winter, temperature, weather |
| BEGIN | 0.92 | conclusion, culminate, ultimate, outcome, terminate | conclusion, culminate, ultimate, fourth, outcome | initiate, initially, onset, launch, early | initiate, initially, launch, onset, originate |
| GIVE | 0.89 | provide, receive, lend, contribute, accept | provide, receive, request, lend, submit | capture, catch, grasp, hold, acquire | grasp, catch, capture, pull, hold |
| TOUCH | 0.93 | tough, severe, rugged, strong, stiffly | tough, strong, severe, rugged, sturdy | gentle, sweet, porous, smooth, delicate | porous, smooth, thick, delicate, gentle |
| SEX | 0.95 | papa, boy, comrade, man, guy | papa, boy, man, guy, comrade | girl, woman, parent, family, lady | girl, parent, woman, family, lady |
| THINK | 0.85 | select, settle, define, assess, evaluate | assess, evaluate, define, identify, examine | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, think, question, guess |
| CAN | 0.93 | convenient, efficient, conceivably, likely, probable | efficient, convenient, effective, useful, adequate | tough, difficulty, painful, desperate, awkward | difficulty, tough, struggle, task, desperate |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | invariably, practically, totally, basically, completely | nowhere, hardly, anymore, scarcely, barely | hardly, nowhere, scarcely, certainly, apparently |
| SOMEONE | 0.85 | personally, someone, honestly, anyway, dear | anyway, anyhow, honestly, personally, maybe | people, either, individually, own, someone | effectively, readily, properly, repeatedly, promptly |
| THING | 0.91 | cattle, barn, farm, gallop, creature | cattle, chicken, hen, farm, duck | rock, concrete, dirt, hill, mud | rock, dirt, concrete, mud, soil |
| MOVE | 0.92 | quick, speed, hasten, rapid, accelerate | quick, rapid, speed, hasten, quickly | sit, halt, keep, linger, continue | sit, keep, halt, while, pause |
| FEEL | 0.91 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, excitedly, furiously, madly, frantically | relax, asleep, slow, sleep, dull | sleep, asleep, awake, relax, disturb |
| RULE | 0.86 | enforce, government, court, legislative, regulate | legislative, sanction, judge, commission, government | privately, intimate, public, individually, own | intimate, privately, professional, social, vocational |
| CHANGE | 0.91 | modify, adjust, adapt, variation, convert | modify, improve, adjust, radically, enhance | steady, persist, keep, continue, maintain | steady, persist, keep, maintain, continuous |
| ART | 0.86 | artist, artistic, aesthetic, collage, literary | artistic, artist, classical, culture, contemporary | technological, machinery, electrical, technical, apparatus | technological, machinery, equipment, electrical, apparatus |
| JOIN | 0.89 | merge, integrate, together, mingle, link | integrate, merge, collaborate, together, cooperate | split, sever, isolate, apart, secede | eliminate, sever, exclude, withdraw, reduce |
| VALUE | 0.94 | worth, important, cost, cherish, value | important, worth, cherish, beloved, dear | buy, price, economical, simple, deal | buy, price, sell, sale, deal |
| CARE | 0.90 | meticulously, carefully, precise, cautiously, thoroughly | meticulously, carefully, thoroughly, methodically, thoughtfully | indifferent, stupid, neglect, inadequate, dumb | mistake, neglect, wrong, error, inadequate |
| FRIEND | 0.94 | relationship, neighbor, comrade, sympathy, fellow | relationship, sympathy, reciprocal, comrade, neighbor | hatred, fierce, violent, savage, violence | savage, violent, fierce, violence, hatred |
| MOOD | 0.96 | humorous, happy, laugh, delightful, joy | happy, laugh, humorous, delightful, glad | sad, despair, desperate, regret, weep | sad, despair, desperate, weep, regret |
| CONSUME | 0.94 | consume, chew, sip, bite, meal | consume, sip, chew, bite, meal | breathe, hurl, smell, discharge, breath | hurl, discharge, breathe, utter, smell |
| MEASURE | 0.92 | percent, proportionately, calculate, decrease, probability | percent, decrease, income, calculate, estimate | extent, magnitude, diameter, tall, scale | extent, magnitude, depth, density, diameter |
| LONG | 0.91 | wooden, column, frame, wall, wood | wooden, plate, table, frame, porch | tie, bind, chain, fasten, curl | tie, bind, fasten, cloth, chain |
| SAY | 0.90 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, loudly, clamor | silence, silently, quietly, softly, rustle | silently, quietly, softly, silence, rustle |
| GRAIN | 0.90 | concrete, massive, metal, steel, structure | concrete, structure, steel, massive, metal | exhaust, oxygen, breath, breathe, atmosphere | oxygen, chlorine, liquid, exhaust, fluid |
| FIGHT | 0.87 | war, battle, conflict, soldier, fight | war, soldier, army, military, battle | competition, game, compete, competitive, sport | competition, game, compete, win, competitive |
| HAPPEN | 0.94 | circumstance, encounter, arise, occasion, phenomenon | encounter, circumstance, arise, occasion, phenomenon | | |
| BODY | 0.94 | shoulder, neck, finger, chest, knee | shoulder, neck, chest, finger, cheek | | |
| SEE | 0.95 | gaze, observe, glance, sight, stare | gaze, glance, sight, observe, stare | | |
| DO | 0.91 | undertake, enact, accomplish, behave, conduct | undertake, enact, conduct, behave, produce | | |
| PLACE | 0.91 | locate, position, neighborhood, country, town | country, neighborhood, district, facility, town | | |
| TEXT | 0.93 | letter, article, paper, book, note | article, letter, book, publish, note | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| river | `THING(=-1) ABOVE(=0) PLACE \| o` | 13 | rock, hill, mountain, ground, soil |
| anger | `FEEL(=+1) FRIEND(=-3) MOOD(=-4) \| o` | 5 | angry, furious, rage, despair, anger |
| hope | `WANT(=+2) TIME(=+3) MOOD(=0) \| o` | 2 | wish, hope, await, someday, joy |
