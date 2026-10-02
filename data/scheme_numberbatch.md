# Рабочая схема: 30 корней + 3 оси формы + 6 универсальных смысловых осей

Numberbatch, 3000 слов, частотность вычтена. Оси найдены по отклонению слов от центра своего корня; полюса — слова с крайними значениями по всему списку. Знаки и порядок осей нестабильны между запусками.

## Корни (по размеру кластера)

- **think** (183): suppose, believe, imagine, guess, consider, know
- **move** (171): shift, push, movement, motion, transfer, step
- **amount** (156): quantity, sum, proportion, total, extent, proportionately
- **provide** (138): give, furnish, offer, deliver, supply, impart
- **occurrence** (125): incident, event, occur, circumstance, phenomenon, occasion
- **correspond** (124): coincide, pertain, relate, represent, identical, indicate
- **diminish** (116): lessen, reduce, decrease, dwindle, minimize, weaken
- **regard** (115): respect, consideration, concern, commend, appreciate, relation
- **emotion** (112): emotional, excitement, anger, emotionally, anxiety, sympathy
- **examine** (112): inspect, investigate, evaluate, analyze, assess, explore
- **hit** (108): strike, smash, knock, slam, beat, slap
- **area** (108): region, neighborhood, location, district, town, land
- **declare** (105): proclaim, assert, announce, affirm, profess, certify
- **metal** (93): steel, iron, silver, brass, gold, material
- **month** (93): week, year, september, february, june, november
- **color** (90): purple, yellow, blue, red, paint, pink
- **terminate** (86): cancel, cease, conclude, suspend, end, quit
- **create** (86): generate, produce, build, construct, establish, invent
- **achievement** (85): success, achieve, attain, accomplish, award, congratulate
- **room** (84): bedroom, hall, upstairs, downstairs, basement, floor
- **request** (83): ask, demand, beg, submit, proposal, recommendation
- **faith** (83): belief, confidence, trust, religion, conviction, religious
- **noise** (80): loud, sound, din, clamor, roar, murmur
- **officer** (74): lieutenant, chief, police, captain, colonel, director
- **connect** (74): connection, link, join, communicate, attach, unite
- **animal** (70): dog, creature, cat, human, cow, cattle
- **arouse** (68): excite, provoke, stimulate, elicit, evoke, awaken
- **compete** (67): competition, competitive, contend, win, qualify, participate
- **author** (56): writer, book, novel, editor, historian, reader
- **committee** (55): commission, board, congress, unanimously, legislative, chair

## Форма (3 оси)

- F1: **−** plainly, practically, largely, eventually, completely, fairly, promptly  /  **+** overlook, impression, forget, recognize, criticize, pose, perceive
- F2: **−** nice, serious, obvious, significant, important, easy, critical  /  **+** alternately, performance, image, happen, situation, dress, boost
- F3: **−** incur, give, bring, publish, pay, write, wear  /  **+** definition, concept, thing, structure, notion, model, process

## Универсальные смысловые оси (6)

- M1: **−** subjective, define, determine, frequency, characterize, adopt, establish  /  **+** beautifully, stare, shudder, excitedly, exclaim, nowhere, bloody
- M2: **−** completely, fairly, wholly, perfectly, downright, utterly, pretty  /  **+** anxiously, wait, impatiently, nervously, excitedly, further, future
- M3: **−** attain, objective, calm, satisfactory, achieve, impossible, safe  /  **+** tremendous, enormous, tremendously, huge, extensive, vastly, numerous
- M4: **−** discover, vanish, nowhere, find, anywhere, disappear, beyond  /  **+** strongly, stiffly, harshly, tightly, cautiously, vigorously, mildly
- M5: **−** usual, aside, customary, pseudo, exclude, instead, include  /  **+** tremendously, safely, vitally, capable, efficient, able, effectively
- M6: **−** widespread, continuous, extensive, long, broad, definite, majority  /  **+** pay, repay, payment, money, owe, expense, tax

## Примеры кодирования (слова из test)

Запись: `ROOT(F1,F2,F3 | M1..M6)`, значения -5..+5.

- exert (verb) = `DIMINISH(+3,+1,-2 | -3,+1,+1,+2,+3,+0)`
- twist (verb) = `MOVE(+2,+1,+2 | +1,-3,+2,+0,-3,-1)`
- build (verb) = `CREATE(+1,+1,-2 | -1,+1,+1,+0,+1,-1)`
- pretty (adv) = `THINK(-2,-3,+1 | +5,-5,+1,+1,+2,+0)`
- worst (adj) = `THINK(+2,-4,+0 | +3,+1,-1,+1,-1,+0)`
- bake (verb) = `CREATE(+0,+0,-1 | +3,+0,-1,+1,-2,+1)`
- sea (noun) = `ANIMAL(+0,+0,-1 | +2,+1,+0,-2,+0,-2)`
- affirm (verb) = `DECLARE(+1,+1,-2 | -4,+1,+1,+0,+1,+0)`
- flap (verb) = `NOISE(+1,+1,+1 | +0,-2,+0,+2,-2,-1)`
- critical (adj) = `EXAMINE(+0,-5,+1 | -2,+2,+2,+2,+3,-2)`
- true (adj) = `FAITH(-1,-3,+0 | -1,-4,-2,-5,+2,-2)`
- capacity (noun) = `AMOUNT(+1,+1,+3 | -2,+2,+1,+1,+3,+0)`
- steady (adj) = `FAITH(-1,-4,-2 | +1,+1,-5,+5,+2,-5)`
- point (noun) = `REGARD(+2,+0,+3 | +1,+0,-4,-1,-1,-4)`