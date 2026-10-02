# Корни по смыслу + суффикс части речи (numberbatch, 3000 слов)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 10 + суффикс + 3 осей** | 15.7 | 0.374 | 65% | 40% |
| корни 10 + 3 непрерывные формы + 3 осей | 24.1 | 0.376 | 70% | 40% |
| глобальные plain, 5 осей | 17.3 | 0.377 | 54% | 28% |
| глобальные split (3+2) | 17.3 | 0.382 | 71% | 22% |
| **корни 10 + суффикс + 6 осей** | 26.1 | 0.380 | 68% | 48% |
| корни 10 + 3 непрерывные формы + 6 осей | 34.5 | 0.382 | 71% | 46% |
| глобальные plain, 8 осей | 27.7 | 0.384 | 60% | 41% |
| глобальные split (3+5) | 27.7 | 0.380 | 70% | 38% |
| **корни 30 + суффикс + 3 осей** | 17.3 | 0.383 | 66% | 66% |
| корни 30 + 3 непрерывные формы + 3 осей | 25.7 | 0.380 | 68% | 66% |
| глобальные plain, 5 осей | 17.3 | 0.377 | 54% | 28% |
| глобальные split (3+2) | 17.3 | 0.382 | 71% | 22% |
| **корни 30 + суффикс + 6 осей** | 27.7 | 0.388 | 70% | 70% |
| корни 30 + 3 непрерывные формы + 6 осей | 36.0 | 0.387 | 69% | 69% |
| глобальные plain, 8 осей | 27.7 | 0.384 | 60% | 41% |
| глобальные split (3+5) | 27.7 | 0.380 | 70% | 38% |
| **корни 30 + суффикс + 9 осей** | 38.0 | 0.405 | 73% | 73% |
| корни 30 + 3 непрерывные формы + 9 осей | 46.4 | 0.397 | 70% | 71% |
| глобальные plain, 11 осей | 38.1 | 0.390 | 64% | 51% |
| глобальные split (3+8) | 38.1 | 0.397 | 68% | 51% |

## Корни (30), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **THINK** (174): `-o` idea, thing, doubt; `-i` think, suppose, believe; `-a` sure, aware, likely; `-e` probably, maybe, perhaps
- **AMOUNT** (148): `-o` amount, quantity, sum; `-i` expend, allot, pay; `-a` total, considerable, minimum; `-e` proportionately, roughly, approximately
- **PROVIDE** (130): `-o` provision, assistance, information; `-i` provide, furnish, give; `-a` adequate, ample, reliable; `-e` helpfully, uniquely, sufficiently
- **EMOTION** (122): `-o` emotion, anger, excitement; `-i` regret, love, ache; `-a` emotional, sad, intense; `-e` emotionally, deeply, vividly
- **OCCURRENCE** (120): `-o` occurrence, incident, event; `-i` occur, happen, encounter; `-a` unusual, occasional, unfortunate; `-e` ordinarily, rarely, seldom
- **CORRESPOND** (111): `-o` address, description, standard; `-i` correspond, coincide, pertain; `-a` identical, similar, equal; `-e` respectively, exactly, precisely
- **MOVE** (107): `-o` movement, motion, step; `-i` move, shift, push; `-a` rapid, quick, swift; `-e` forward, swiftly, backward
- **HIT** (106): `-o` target, impact, blow; `-i` hit, strike, smash; `-a` single, straight, hard; `-e` squarely, repeatedly, violently
- **REQUEST** (105): `-o` proposal, recommendation, suggestion; `-i` request, ask, demand; `-a` immediate, eager, unable; `-e` politely, hereby, immediately
- **AREA** (105): `-o` area, region, neighborhood; `-i` sprawl, locate, surround; `-a` downtown, residential, near; `-e` within, centrally, around
- **IMPROVE** (105): `-o` improvement, efficiency, quality; `-i` improve, enhance, strengthen; `-a` better, worse, best; `-e` dramatically, significantly, radically
- **DESCEND** (104): `-o` flight, level, plane; `-i` descend, climb, clamber; `-a` higher, low, high; `-e` down, upward, below
- **TERMINATE** (103): `-o` end, contract, conclusion; `-i` terminate, cancel, cease; `-a` indefinite, finite, short; `-e` abruptly, off, permanently
- **MONTH** (102): `-o` month, week, year; `-i` march, rent, issue; `-a` lunar, twentieth, fourth; `-e` annually, sometime, twice
- **EXAMINE** (101): `-o` examination, investigation, study; `-i` examine, inspect, investigate; `-a` curious, analytic, experimental; `-e` carefully, thoroughly, comprehensively
- **NOISE** (99): `-o` noise, sound, din; `-i` clamor, roar, murmur; `-a` loud, shrill, quiet; `-e` loudly, aloud, quietly
- **FAITH** (99): `-o` faith, belief, confidence; `-i` trust, profess, affirm; `-a` religious, christian, protestant; `-e` blindly, solemnly, stubbornly
- **SOLDIER** (98): `-o` soldier, army, regiment; `-i` enlist, recruit, volunteer; `-a` military, civilian, brave; `-e` gravely, stoutly, wearily
- **REGARD** (96): `-o` respect, consideration, relation; `-i` regard, concern, commend; `-a` particular, careful, respectable; `-e` particularly, especially, regardless
- **ACHIEVEMENT** (95): `-o` achievement, success, award; `-i` achieve, attain, accomplish; `-a` successful, heroic, academic; `-e` academically, triumphantly, successfully
- **CREATE** (90): `-o` form, creature, environment; `-i` create, generate, produce; `-a` creative, unique, artistic; `-e` thereby, deliberately, instead
- **COLOR** (88): `-o` color, shade, texture; `-i` paint, blush, stain; `-a` purple, yellow, blue; `-e` beautifully
- **FASTEN** (87): `-o` wire, chain, safety; `-i` fasten, attach, tighten; `-a` tight, loose, bound; `-e` tightly, firmly, loosely
- **COMPETE** (80): `-o` competition, race, battle; `-i` compete, contend, win; `-a` competitive, regional, fierce; `-e` physically, independently, commercially
- **METAL** (79): `-o` metal, steel, iron; `-i` grind, polish, melt; `-a` silver, solid, heavy; `-e` heavily, mainly, finely
- **ROOM** (77): `-o` room, bedroom, hall; `-i` huddle, sit, bathe; `-a` comfortable, private, homely; `-e` upstairs, downstairs, inside
- **FOOD** (72): `-o` food, meal, dinner; `-i` eat, feed, cook; `-a` hungry, organic, raw
- **COMMITTEE** (71): `-o` committee, commission, board; `-i` elect, appoint, vote; `-a` legislative, democratic, municipal; `-e` unanimously, jointly, tonight
- **AUTHOR** (69): `-o` author, writer, book; `-i` write, publish, read; `-a` literary, fictional, famous; `-e` wildly, happily
- **OFFICIAL** (57): `-o` official, agency, authority; `-i` announce, release, certify; `-a` formal, chief, preliminary; `-e` formally, publicly, newly