# Обучение словаря корней при условии читаемости

Numberbatch, 2727 слов (без слов-полюсов), обучение 1908, **тест 819** (все числа ниже — на тесте). m = 3, уровни −5…+5, масштаб оси s = 2. Скрипт `scripts/18_sparse_learn.py`, постановка и метрики — [docs/math.md](../docs/math.md).

| словарь | top1 | top10 | top50 | медиана | cos(x,y) | промах похож |
| :-- | --: | --: | --: | --: | --: | --: |
| корни из полюсов, порядок не важен | 18.2% | 70.3% | 94.0% | 5 | 0.413 | 0.275 |
| корни из полюсов, вес не главных 0.4 | 16.7% | 69.6% | 94.9% | 5 | 0.419 | 0.275 |
| обученные (λ = 30, cos с исходным ≥ 0.85, вес 0.4) | 20.3% | 74.4% | 96.9% | 5 | 0.474 | 0.330 |

Сдвиг корней: cos(центр, исходный) в среднем 0.94 (минимум 0.85), cos(ось, исходная) в среднем 0.94 (минимум 0.85). итерация 1: на обучающих словах до шага top1 17.9%, cos 0.427; итерация 2: на обучающих словах до шага top1 28.8%, cos 0.503; итерация 3: на обучающих словах до шага top1 31.0%, cos 0.513.

## Читаемость: ближайшие слова к полюсам до и после обучения

| корень | cos | + до | + после | − до | − после |
| :-- | --: | :-- | :-- | :-- | :-- |
| GOOD | 0.95 | fantastic, nice, lovely, magnificent, brilliant | fantastic, magnificent, lovely, nice, impressive | worst, unspeakable, unfortunate, worse, monstrous | worst, worse, unspeakable, terribly, unfortunate |
| BIG | 0.96 | gigantic, massive, tremendous, considerable, extensive | massive, gigantic, tremendous, considerable, extensive | smaller, few, slightly, larger, minimal | smaller, few, slightly, minimal, relatively |
| NEAR | 0.96 | shut, neighborhood, closely, along, around | shut, around, neighborhood, center, corner | afar, farther, distance, beyond, off | afar, farther, distance, beyond, somewhere |
| ABOVE | 0.94 | higher, rise, beyond, upper, climb | higher, rise, climb, raise, upper | bottom, downstairs, drop, descend, decline | bottom, drop, downstairs, descend, decline |
| LIVE | 0.96 | live, vivid, vitally, life, healthy | healthy, vitally, vivid, live, vigorous | corpse, die, fatal, kill, murder | corpse, die, murder, kill, fatal |
| SAME | 0.91 | comparable, equivalent, equally, similarly, equate | comparable, equivalent, equate, exact, correspond | differ, differently, distinctive, various, distinctly | distinctive, peculiar, differ, distinctly, characteristically |
| TIME | 0.95 | shortly, sometime, someday, hereafter, await | shortly, sometime, someday, await, arrive | previous, previously, recently, recent, formerly | previous, previously, recently, years, recent |
| INSIDE | 0.94 | inner, deep, around, room, therein | inner, room, basement, house, bedroom | outdoor, inner, porch, side, surface | outdoor, porch, inner, protective, wall |
| PART | 0.93 | pack, gather, assemble, variety, selection | organization, collective, pack, team, selection | portion, dust, atom, part, texture | dust, atom, portion, substance, element |
| SIDE | 0.95 | advance, rearward, before, side, precede | advance, rearward, southward, northward, side | rearward, shoulder, return, reverse, forth | rearward, reverse, shoulder, corner, return |
| KNOW | 0.94 | understand, knowledge, conscious, realize, sure | inform, understand, learn, knowledge, tell | dumb, indifferent, stupid, helpless, silly | dumb, stupid, silly, fool, indifferent |
| WANT | 0.92 | wish, need, cherish, urge, seek | wish, need, cherish, hope, urge | despise, dislike, resent, oppose, deny | despise, oppose, dislike, resent, denounce |
| HEAT | 0.97 | burn, heat, temperature, thermal, glow | burn, heat, glow, sun, light | freeze, snow, winter, coldly, temperature | freeze, snow, winter, temperature, weather |
| BEGIN | 0.94 | conclusion, culminate, ultimate, outcome, terminate | conclusion, culminate, ultimate, fourth, outcome | initiate, initially, onset, launch, early | initiate, initially, launch, onset, originate |
| GIVE | 0.91 | provide, receive, lend, contribute, accept | provide, receive, contribute, lend, accept | capture, catch, grasp, hold, acquire | grasp, catch, capture, pull, swoop |
| TOUCH | 0.95 | tough, severe, rugged, strong, stiffly | tough, strong, severe, rugged, sturdy | gentle, sweet, porous, smooth, delicate | porous, thick, gentle, delicate, smooth |
| SEX | 0.96 | papa, boy, comrade, man, guy | papa, boy, man, guy, comrade | girl, woman, parent, family, lady | girl, parent, woman, family, lady |
| THINK | 0.88 | select, settle, define, assess, evaluate | assess, evaluate, define, identify, examine | doubtful, speculate, contemplate, think, doubtless | doubtful, speculate, think, question, doubtless |
| CAN | 0.94 | convenient, efficient, conceivably, likely, probable | convenient, efficient, effective, useful, conceivably | tough, difficulty, painful, desperate, awkward | difficulty, tough, desperate, task, struggle |
| MANY | 0.85 | whole, entire, invariably, everywhere, continually | invariably, generally, practically, consistently, usually | nowhere, hardly, anymore, scarcely, barely | hardly, nowhere, scarcely, certainly, apparently |
| SOMEONE | 0.85 | personally, someone, honestly, anyway, dear | honestly, personally, anyway, anyhow, maybe | people, either, individually, own, someone | effectively, repeatedly, properly, promptly, readily |
| THING | 0.93 | cattle, barn, farm, gallop, creature | cattle, chicken, farm, hen, bird | rock, concrete, dirt, hill, mud | rock, dirt, concrete, mud, soil |
| MOVE | 0.95 | quick, speed, hasten, rapid, accelerate | quick, rapid, speed, hasten, quickly | sit, halt, keep, linger, continue | sit, halt, keep, linger, pause |
| FEEL | 0.94 | enthusiastic, eager, excitement, excitedly, furious | enthusiastic, excitedly, madly, furiously, furious | relax, asleep, slow, sleep, dull | sleep, asleep, awake, relax, disturb |
| RULE | 0.90 | enforce, government, court, legislative, regulate | enforce, sanction, legislative, commission, government | privately, intimate, public, individually, own | intimate, privately, professional, social, public |
| CHANGE | 0.93 | modify, adjust, adapt, variation, convert | modify, adjust, improve, radically, adapt | steady, persist, keep, continue, maintain | steady, persist, keep, maintain, continuous |
| ART | 0.90 | artist, artistic, aesthetic, collage, literary | artistic, artist, classical, contemporary, culture | technological, machinery, electrical, technical, apparatus | technological, machinery, electrical, equipment, apparatus |
| JOIN | 0.91 | merge, integrate, together, mingle, link | integrate, merge, collaborate, together, mingle | split, sever, isolate, apart, secede | eliminate, sever, withdraw, split, exclude |
| VALUE | 0.96 | worth, important, cost, cherish, value | important, worth, cherish, value, cost | buy, price, economical, simple, deal | price, buy, sell, sale, purchase |
| CARE | 0.93 | meticulously, carefully, precise, cautiously, thoroughly | meticulously, carefully, thoroughly, precise, methodically | indifferent, stupid, neglect, inadequate, dumb | mistake, neglect, blame, wrong, inadequate |
| FRIEND | 0.96 | relationship, neighbor, comrade, sympathy, fellow | relationship, sympathy, comrade, neighbor, fellow | hatred, fierce, violent, savage, violence | savage, violent, fierce, hatred, violence |
| MOOD | 0.97 | humorous, happy, laugh, delightful, joy | happy, laugh, humorous, delightful, glad | sad, despair, desperate, regret, weep | sad, despair, desperate, regret, weep |
| CONSUME | 0.96 | consume, chew, sip, bite, meal | consume, sip, chew, bite, meal | breathe, hurl, smell, discharge, breath | hurl, breathe, discharge, utter, smell |
| MEASURE | 0.94 | percent, proportionately, calculate, decrease, probability | percent, decrease, calculate, estimate, probability | extent, magnitude, diameter, tall, scale | extent, magnitude, depth, diameter, scale |
| LONG | 0.94 | wooden, column, frame, wall, wood | wooden, plate, frame, table, wood | tie, bind, chain, fasten, curl | tie, bind, fasten, chain, cloth |
| SAY | 0.94 | wail, exclaim, cry, loudly, clamor | exclaim, wail, cry, clamor, loudly | silence, silently, quietly, softly, rustle | silently, quietly, silence, softly, rustle |
| GRAIN | 0.93 | concrete, massive, metal, steel, structure | concrete, structure, steel, massive, metal | exhaust, oxygen, breath, breathe, atmosphere | oxygen, chlorine, liquid, exhaust, water |
| FIGHT | 0.91 | war, battle, conflict, soldier, fight | war, soldier, military, battle, army | competition, game, compete, competitive, sport | competition, game, compete, win, competitive |
| HAPPEN | 0.96 | circumstance, encounter, arise, occasion, phenomenon | circumstance, encounter, arise, occasion, phenomenon | | |
| BODY | 0.96 | shoulder, neck, finger, chest, knee | shoulder, neck, chest, finger, cheek | | |
| SEE | 0.97 | gaze, observe, glance, sight, stare | gaze, glance, sight, observe, stare | | |
| DO | 0.93 | undertake, enact, accomplish, behave, conduct | undertake, enact, accomplish, produce, conduct | | |
| PLACE | 0.94 | locate, position, neighborhood, country, town | country, neighborhood, town, district, suburb | | |
| TEXT | 0.94 | letter, article, paper, book, note | article, letter, book, publish, note | | |

## Примеры (тестовые слова, обученный словарь)

| слово | код | место | ближайшие к декодированному |
| :-- | :-- | --: | :-- |
| river | `THING(=-1) ABOVE(=0) PLACE \| o` | 19 | rock, hill, mountain, dirt, soil |
| anger | `FEEL(=+1) FRIEND(=-4) MOOD(=-5) \| o` | 6 | furious, angry, rage, desperate, despair |
| hope | `WANT(=+2) TIME(=+3) MOOD(=0) \| o` | 2 | wish, hope, need, urge, someday |
