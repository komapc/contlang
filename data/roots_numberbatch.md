# Корни + локальные признаки (numberbatch, 3000 слов, частотность вычтена)

Корни выбираются жадно (покрытие всех слов по косинусу) среди 300 самых общих существительных и глаголов (по числу гипонимов в WordNet). У каждого корня свои локальные оси (PCA кластера). Сравнение при одинаковой длине кода в битах: корень = log2(R) бит, координата = 3.46 бит (11 уровней).

| схема | биты | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| корни 10 + 3 локальных | 13.7 | 0.374 | 61% | 45% |
| глобальные plain, 4 осей | 13.8 | 0.368 | 53% | 23% |
| глобальные split (3+1) | 13.8 | 0.384 | 73% | 18% |
| корни 10 + 6 локальных | 24.1 | 0.384 | 64% | 60% |
| глобальные plain, 7 осей | 24.2 | 0.383 | 60% | 39% |
| глобальные split (3+4) | 24.2 | 0.372 | 69% | 33% |
| корни 30 + 3 локальных | 15.3 | 0.392 | 65% | 70% |
| глобальные plain, 4 осей | 13.8 | 0.368 | 53% | 23% |
| глобальные split (3+1) | 13.8 | 0.384 | 73% | 18% |
| корни 30 + 6 локальных | 25.7 | 0.403 | 69% | 78% |
| глобальные plain, 7 осей | 24.2 | 0.383 | 60% | 39% |
| глобальные split (3+4) | 24.2 | 0.372 | 69% | 33% |
| корни 30 + 9 локальных | 36.0 | 0.419 | 71% | 83% |
| глобальные plain, 10 осей | 34.6 | 0.379 | 64% | 48% |
| глобальные split (3+7) | 34.6 | 0.389 | 68% | 46% |

## Корни R=10 (кластеры)

- **declare** (348 слов; noun 21%, verb 54%, adj 14%, adv 10%): proclaim, assert, announce, affirm, profess, certify
- **amount** (353 слов; noun 47%, verb 14%, adj 27%, adv 12%): quantity, sum, proportion, total, extent, proportionately
- **move** (403 слов; noun 26%, verb 48%, adj 10%, adv 16%): shift, push, movement, motion, transfer, step
- **regard** (265 слов; noun 33%, verb 29%, adj 15%, adv 22%): respect, consideration, concern, commend, appreciate, relation
- **create** (345 слов; noun 24%, verb 52%, adj 20%, adv 3%): generate, produce, build, construct, establish, invent
- **think** (252 слов; noun 14%, verb 36%, adj 15%, adv 35%): suppose, believe, imagine, guess, consider, know
- **occurrence** (305 слов; noun 52%, verb 7%, adj 30%, adv 10%): incident, event, occur, circumstance, phenomenon, occasion
- **officer** (197 слов; noun 66%, verb 12%, adj 16%, adv 6%): lieutenant, chief, police, captain, colonel, director
- **emotion** (290 слов; noun 46%, verb 15%, adj 32%, adv 8%): emotional, excitement, anger, emotionally, anxiety, sympathy
- **diminish** (242 слов; noun 13%, verb 54%, adj 21%, adv 12%): lessen, reduce, decrease, dwindle, minimize, weaken

## Корни R=30 (кластеры)

- **declare** (105 слов; noun 11%, verb 63%, adj 10%, adv 15%): proclaim, assert, announce, affirm, profess, certify
- **amount** (156 слов; noun 49%, verb 15%, adj 25%, adv 11%): quantity, sum, proportion, total, extent, proportionately
- **move** (171 слов; noun 17%, verb 58%, adj 8%, adv 17%): shift, push, movement, motion, transfer, step
- **regard** (115 слов; noun 37%, verb 21%, adj 10%, adv 32%): respect, consideration, concern, commend, appreciate, relation
- **create** (86 слов; noun 15%, verb 64%, adj 19%, adv 2%): generate, produce, build, construct, establish, invent
- **think** (183 слов; noun 12%, verb 32%, adj 14%, adv 42%): suppose, believe, imagine, guess, consider, know
- **occurrence** (125 слов; noun 47%, verb 4%, adj 34%, adv 15%): incident, event, occur, circumstance, phenomenon, occasion
- **officer** (74 слов; noun 74%, verb 4%, adj 16%, adv 5%): lieutenant, chief, police, captain, colonel, director
- **emotion** (112 слов; noun 41%, verb 16%, adj 34%, adv 9%): emotional, excitement, anger, emotionally, anxiety, sympathy
- **diminish** (116 слов; noun 7%, verb 59%, adj 17%, adv 17%): lessen, reduce, decrease, dwindle, minimize, weaken
- **area** (108 слов; noun 59%, verb 6%, adj 24%, adv 10%): region, neighborhood, location, district, town, land
- **hit** (108 слов; noun 19%, verb 66%, adj 8%, adv 7%): strike, smash, knock, slam, beat, slap
- **request** (83 слов; noun 28%, verb 48%, adj 10%, adv 14%): ask, demand, beg, submit, proposal, recommendation
- **color** (90 слов; noun 48%, verb 21%, adj 31%, adv 0%): purple, yellow, blue, red, paint, pink
- **month** (93 слов; noun 41%, verb 5%, adj 28%, adv 26%): week, year, september, february, june, november
- **connect** (74 слов; noun 28%, verb 51%, adj 8%, adv 12%): connection, link, join, communicate, attach, unite
- **examine** (112 слов; noun 16%, verb 59%, adj 11%, adv 14%): inspect, investigate, evaluate, analyze, assess, explore
- **provide** (138 слов; noun 14%, verb 52%, adj 25%, adv 9%): give, furnish, offer, deliver, supply, impart
- **noise** (80 слов; noun 32%, verb 44%, adj 16%, adv 8%): loud, sound, din, clamor, roar, murmur
- **achievement** (85 слов; noun 47%, verb 16%, adj 29%, adv 7%): success, achieve, attain, accomplish, award, congratulate
- **correspond** (124 слов; noun 9%, verb 36%, adj 30%, adv 25%): coincide, pertain, relate, represent, identical, indicate
- **metal** (93 слов; noun 53%, verb 8%, adj 40%, adv 0%): steel, iron, silver, brass, gold, material
- **terminate** (86 слов; noun 21%, verb 63%, adj 8%, adv 8%): cancel, cease, conclude, suspend, end, quit
- **faith** (83 слов; noun 55%, verb 10%, adj 29%, adv 6%): belief, confidence, trust, religion, conviction, religious
- **room** (84 слов; noun 71%, verb 7%, adj 8%, adv 13%): bedroom, hall, upstairs, downstairs, basement, floor
- **animal** (70 слов; noun 63%, verb 4%, adj 30%, adv 3%): dog, creature, cat, human, cow, cattle
- **compete** (67 слов; noun 24%, verb 48%, adj 21%, adv 7%): competition, competitive, contend, win, qualify, participate
- **committee** (55 слов; noun 73%, verb 7%, adj 16%, adv 4%): commission, board, congress, unanimously, legislative, chair
- **author** (56 слов; noun 68%, verb 9%, adj 23%, adv 0%): writer, book, novel, editor, historian, reader
- **arouse** (68 слов; noun 4%, verb 69%, adj 24%, adv 3%): excite, provoke, stimulate, elicit, evoke, awaken

## Покрытие: NSM против жадных корней

Примитивов NSM в списке слов: 39 (someone, thing, people, body, kind, part, same, little, few, good, bad, big, small, think, know, want, feel, see, hear, word, true, happen, move, touch, live, die, time, now, before, after, moment, place, above, below, far, near, side, inside, maybe).

Среднее максимальное косинусное сходство слова с ближайшим корнем: NSM **0.253**, жадные 39 корней **0.296**, случайные 39 слов 0.272.