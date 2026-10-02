# Корни по смыслу + суффикс части речи (numberbatch, режим sense, 3571 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 27 + суффикс + 6 осей** | 27.5 | 0.395 | 73% | 54% |
| корни 27 + 3 непрерывные формы + 6 осей | 35.9 | 0.394 | 76% | 55% |
| глобальные plain, 8 осей | 27.7 | 0.348 | 76% | 43% |
| глобальные split (3+5) | 27.7 | 0.361 | 81% | 40% |
| **корни 27 + суффикс + 9 осей** | 37.9 | 0.411 | 78% | 61% |
| корни 27 + 3 непрерывные формы + 9 осей | 46.3 | 0.410 | 78% | 62% |
| глобальные plain, 11 осей | 38.1 | 0.364 | 76% | 54% |
| глобальные split (3+8) | 38.1 | 0.373 | 83% | 53% |

## Омонимы и конверсии: корень и суффикс записи

- **march**: 
- **rent**: noun → MOVE-o; verb → MOVE-i
- **issue**: noun → THING-o; verb → THING-i
- **point**: noun → PLACE-o; verb → PLACE-i
- **order**: noun → WANT-o; verb → WANT-i
- **close**: verb → NEAR-i; adj → NEAR-a
- **work**: noun → HAPPEN-o; verb → HAPPEN-i
- **play**: noun → LIVE-o; verb → LIVE-i
- **love**: noun → WANT-o; verb → WANT-i
- **pretty**: adj → GOOD-a; adv → GOOD-e

## Корни (27), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **MOVE** (252): `-o` shift, movement, step; `-i` move, transfer, shift; `-a` fast, backward, swift; `-e` forward, swiftly, backward
- **TIME** (169): `-o` time, past, period; `-i` pause, spend, devote; `-a` late, past, long; `-e` before, late, thereafter
- **INSIDE** (164): `-o` interior, box, shell; `-i` surround, penetrate, tuck; `-a` interior, outside, inner; `-e` inside, outside, within
- **ABOVE** (159): `-o` top, bottom, level; `-i` rise, climb, exceed; `-a` higher, upper, upward; `-e` above, below, upward
- **PART** (158): `-o` part, portion, component; `-i` participate, comprise, split; `-a` complete, whole, entire; `-e` partly, partially, primarily
- **HAPPEN** (158): `-o` occurrence, incident, result; `-i` happen, occur, arise; `-a` inevitable, unlikely, future; `-e` inevitably, rarely, seldom
- **BIG** (156): `-o` size, magnitude, bang; `-i` bang, swell, overlook; `-a` big, huge, large; `-e` mighty, heavily, largely
- **PLACE** (153): `-o` place, spot, location; `-i` place, park, spot; `-a` appropriate, downtown, fifth; `-e` anywhere, elsewhere, centrally
- **TOUCH** (151): `-o` touch, contact, kiss; `-i` touch, concern, kiss; `-a` sensitive, subtle, delicate; `-e` directly, lightly, instantly
- **HEAR** (148): `-o` whisper, sound, murmur; `-i` hear, listen, overhear; `-a` loud, deaf, shrill; `-e` loudly, aloud, excitedly
- **BODY** (145): `-o` body, corpse, flesh; `-i` bury, stiffen, shape; `-a` skeletal, dead, muscular; `-e` stiffly, unanimously, duly
- **WANT** (139): `-o` need, desire, lack; `-i` want, desire, need; `-a` eager, able, necessary; `-e` necessarily, ideally, simply
- **GOOD** (137): `-o` benefit, wise, luck; `-i` improve, enjoy, fit; `-a` good, nice, better; `-e` better, well, fine
- **SIDE** (133): `-o` side, front, rear; `-i` tilt, rear, turn; `-a` front, opposite, rearward; `-e` rearward, across, along
- **LIVE** (132): `-o` life, hereafter, suburb; `-i` live, reside, dwell; `-a` alive, real, vivid; `-e` forever, home, happily
- **FEEL** (132): `-o` sensation, sense, ache; `-i` feel, sense, regret; `-a` comfortable, uneasy, helpless; `-e` emotionally, somewhat, terribly
- **SAME** (128): `-o` equivalent, parallel, difference; `-i` equal, differ, correspond; `-a` same, identical, similar; `-e` exactly, differently, similarly
- **THINK** (128): `-o` idea, notion, assumption; `-i` think, suppose, believe; `-a` doubtful, wrong, stupid; `-e` honestly, really, actually
- **PEOPLE** (118): `-o` people, public, men; `-i` crowd, mingle, inspire; `-a` public, civilian, human; `-e` commonly, violently, openly
- **WORD** (112): `-o` word, term, dictionary; `-i` term, utter, state; `-a` literal, verbal, biblical; `-e` literally, loosely, formally
- **KNOW** (98): `-o` knowledge, truth, secret; `-i` know, understand, realize; `-a` aware, sure, unaware; `-e` truly, anymore, assuredly
- **NEAR** (90): `-o` distance, end, mile; `-i` close, shut, approach; `-a` near, close, nearby; `-e` near, nearby, nearly
- **THING** (89): `-o` thing, matter, aspect; `-i` matter, feature, damn; `-a` damn, weird, important; `-e` basically, quite, absolutely
- **MAYBE** (84): `-o` possibility, hint, chance; `-i` hint, intimate, convince; `-a` likely, probable, possible; `-e` maybe, perhaps, possibly
- **SEE** (82): `-o` glance, view, sight; `-i` see, view, look; `-a` visible, evident, apparent; `-e` visibly, dimly
- **SOMEONE** (79): `-o` someone, person, individual; `-i` steal, throw, peer; `-a` odd, individual, strange; `-e` somewhere, personally, suddenly
- **KIND** (77): `-o` kind, sort, type; `-i` form, classify, treat; `-a` gentle, downright, friendly; `-e` downright, awfully, characteristically

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** report, influence, advise, relevant, influence, warrant, significance  /  **+** tear, damn, stumble, fall, tear, grin, dash
- M2: **−** repay, finance, grant, award, purchase, grant, award  /  **+** tendency, impulse, drift, solid, pattern, strain, flux
- M3: **−** analyze, supply, calculate, supply, synthetic, evaluate, compute  /  **+** love, respect, concern, respect, favor, embrace, gesture
- M4: **−** gain, secure, sustain, strength, secure, defeat, power  /  **+** address, interview, prominently, outline, pertain, list, beautifully
- M5: **−** enlist, creative, cooperative, boost, educate, help, employ  /  **+** half, final, estimate, definite, score, mark, percent
- M6: **−** final, later, before, off, back, after, shortly  /  **+** relatively, comparatively, remarkably, extremely, generally, ordinarily, quite
- M7: **−** abolish, warrant, cancel, suspend, certify, approve, enforce  /  **+** explore, experience, profound, journey, meaningful, path, experience
- M8: **−** cautiously, nervously, anxiously, carefully, calmly, politely, assess  /  **+** provide, produce, evoke, supply, truly, create, utterly
- M9: **−** decrease, decrease, cost, increase, subtract, interest, increase  /  **+** clear, conclusively, stoutly, decisive, complete, impossible, accurately