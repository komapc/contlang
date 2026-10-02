# Корни по смыслу + суффикс части речи (numberbatch, режим sense, 3571 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 33 + суффикс + 6 осей** | 27.8 | 0.401 | 73% | 55% |
| корни 33 + 3 непрерывные формы + 6 осей | 36.2 | 0.399 | 76% | 56% |
| глобальные plain, 8 осей | 27.7 | 0.348 | 76% | 43% |
| глобальные split (3+5) | 27.7 | 0.361 | 81% | 40% |
| **корни 33 + суффикс + 9 осей** | 38.2 | 0.411 | 74% | 59% |
| корни 33 + 3 непрерывные формы + 9 осей | 46.6 | 0.409 | 76% | 61% |
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

## Корни (33), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **MOVE** (224): `-o` shift, movement, step; `-i` move, transfer, shift; `-a` fast, backward, swift; `-e` forward, swiftly, backward
- **TIME** (146): `-o` time, past, period; `-i` pause, spend, devote; `-a` late, past, slow; `-e` before, late, thereafter
- **PLACE** (142): `-o` place, spot, location; `-i` place, park, spot; `-a` appropriate, downtown, fifth; `-e` anywhere, elsewhere, centrally
- **HEAR** (141): `-o` whisper, sound, murmur; `-i` hear, listen, overhear; `-a` loud, deaf, shrill; `-e` loudly, aloud, excitedly
- **PART** (136): `-o` part, portion, component; `-i` participate, comprise, split; `-a` complete, whole, entire; `-e` partly, partially, primarily
- **INSIDE** (133): `-o` interior, box, shell; `-i` surround, penetrate, tuck; `-a` interior, outside, inner; `-e` inside, outside, within
- **TOUCH** (131): `-o` touch, contact, kiss; `-i` touch, concern, kiss; `-a` sensitive, subtle, delicate; `-e` directly, instantly
- **BAD** (126): `-o` worst, hurt, sin; `-i` damn, hurt, blame; `-a` bad, worst, worse; `-e` badly, awful, poorly
- **TRUE** (124): `-o` truth, reality, fact; `-i` prove, profess, fake; `-a` true, real, genuine; `-e` truly, indeed, sincerely
- **WANT** (122): `-o` need, desire, lack; `-i` want, desire, need; `-a` eager, able, necessary; `-e` necessarily, ideally, simply
- **BODY** (121): `-o` body, corpse, flesh; `-i` bury, stiffen, shape; `-a` skeletal, muscular, anatomical; `-e` stiffly, unanimously, duly
- **HAPPEN** (120): `-o` occurrence, incident, result; `-i` happen, occur, arise; `-a` inevitable, unlikely, future; `-e` inevitably, rarely, seldom
- **SIDE** (119): `-o` side, front, rear; `-i` tilt, rear, turn; `-a` front, opposite, rearward; `-e` rearward, across, along
- **SMALL** (117): `-o` size, fraction, sip; `-i` scale, narrow, compress; `-a` small, tiny, smaller; `-e` relatively, comparatively, slightly
- **SAME** (110): `-o` equivalent, parallel, difference; `-i` equal, differ, correspond; `-a` same, identical, similar; `-e` exactly, differently, similarly
- **FEEL** (108): `-o` sensation, sense, ache; `-i` feel, sense, regret; `-a` comfortable, uneasy, helpless; `-e` emotionally, somewhat, totally
- **DIE** (107): `-o` death, murder, collapse; `-i` die, starve, kill; `-a` dead, fatal, tragic; `-e` asleep, gravely, abruptly
- **GOOD** (106): `-o` benefit, wise, pleasure; `-i` improve, enjoy, fit; `-a` good, nice, better; `-e` better, well, fine
- **THINK** (103): `-o` idea, notion, assumption; `-i` think, suppose, believe; `-a` doubtful, capable, intelligent; `-e` honestly, really, actually
- **BIG** (102): `-o` magnitude, bang, blow; `-i` bang, swell, overlook; `-a` big, huge, large; `-e` mighty, heavily, largely
- **BELOW** (99): `-o` bottom, decline, surface; `-i` descend, drop, lurk; `-a` low, underground, flat; `-e` below, down, downstairs
- **LIVE** (99): `-o` life, hereafter, suburb; `-i` live, reside, dwell; `-a` alive, vivid, present; `-e` forever, home, happily
- **PEOPLE** (97): `-o` people, public, men; `-i` crowd, mingle, inspire; `-a` public, civilian, human; `-e` commonly, violently, openly
- **WORD** (93): `-o` word, term, dictionary; `-i` term, utter, state; `-a` literal, verbal, biblical; `-e` literally, loosely, formally
- **ABOVE** (88): `-o` top, level, minimum; `-i` rise, climb, exceed; `-a` higher, upper, upward; `-e` above, upward, over
- **FAR** (80): `-o` distance, stretch, range; `-i` reach, stretch, range; `-a` farther, distant, remote; `-e` far, farther, afar
- **KNOW** (77): `-o` knowledge, secret, information; `-i` know, understand, realize; `-a` aware, sure, unaware; `-e` anymore, assuredly, already
- **SEE** (73): `-o` glance, view, sight; `-i` see, view, look; `-a` visible, evident, apparent; `-e` visibly
- **THING** (72): `-o` thing, matter, aspect; `-i` matter, feature, fix; `-a` damn, weird, important; `-e` basically, quite, absolutely
- **MAYBE** (69): `-o` possibility, hint, chance; `-i` hint, intimate, convince; `-a` likely, probable, possible; `-e` maybe, perhaps, possibly
- **SOMEONE** (66): `-o` someone, person, individual; `-i` steal, throw, peer; `-a` odd, individual, strange; `-e` somewhere, personally, suddenly
- **KIND** (63): `-o` kind, sort, type; `-i` form, classify, treat; `-a` gentle, downright, friendly; `-e` downright, characteristically, naturally
- **NEAR** (57): `-o` end, mile, neighbor; `-i` close, shut, approach; `-a` near, close, nearby; `-e` near, nearby, nearly

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** influence, report, relevant, influence, advise, analyze, importance  /  **+** damn, stumble, dash, grin, curse, snap, everywhere
- M2: **−** repay, purchase, grant, grant, finance, assistance, grateful  /  **+** tendency, solid, strain, flux, drift, impulse, strong
- M3: **−** respect, concern, love, respect, favor, evident, gesture  /  **+** calculate, analyze, estimate, determine, compute, evaluate, supply
- M4: **−** half, mark, point, final, least, indicate, sum  /  **+** creative, enlist, cooperative, boost, educate, promote, train
- M5: **−** sustain, secure, secure, gain, sufficient, cure, steady  /  **+** interview, prefer, closely, pertain, historically, dance, criticize
- M6: **−** off, final, back, later, question, initial, book  /  **+** remarkably, extremely, vastly, substantially, comparatively, quite, considerably
- M7: **−** nervously, cautiously, anxiously, stoutly, calmly, final, impatiently  /  **+** evoke, provide, produce, supply, transform, imply, depict
- M8: **−** value, worth, increase, cost, benefit, decrease, benefit  /  **+** clear, clear, prompt, meticulously, simple, probe, brief
- M9: **−** experience, profound, grow, meaningful, path, develop, progress  /  **+** warrant, suspend, compel, forbid, approve, warrant, bar