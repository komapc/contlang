# Корни по смыслу + суффикс части речи (numberbatch, режим sense, 3581 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 10 + суффикс + 3 осей** | 15.7 | 0.394 | 77% | 34% |
| корни 10 + 3 непрерывные формы + 3 осей | 24.1 | 0.385 | 76% | 38% |
| глобальные plain, 5 осей | 17.3 | 0.337 | 72% | 27% |
| глобальные split (3+2) | 17.3 | 0.338 | 83% | 22% |
| **корни 10 + суффикс + 6 осей** | 26.1 | 0.399 | 77% | 44% |
| корни 10 + 3 непрерывные формы + 6 осей | 34.5 | 0.410 | 76% | 50% |
| глобальные plain, 8 осей | 27.7 | 0.364 | 75% | 43% |
| глобальные split (3+5) | 27.7 | 0.371 | 81% | 38% |
| **корни 30 + суффикс + 3 осей** | 17.3 | 0.398 | 74% | 55% |
| корни 30 + 3 непрерывные формы + 3 осей | 25.7 | 0.403 | 70% | 60% |
| глобальные plain, 5 осей | 17.3 | 0.337 | 72% | 27% |
| глобальные split (3+2) | 17.3 | 0.338 | 83% | 22% |
| **корни 30 + суффикс + 6 осей** | 27.7 | 0.396 | 75% | 60% |
| корни 30 + 3 непрерывные формы + 6 осей | 36.0 | 0.413 | 73% | 62% |
| глобальные plain, 8 осей | 27.7 | 0.364 | 75% | 43% |
| глобальные split (3+5) | 27.7 | 0.371 | 81% | 38% |
| **корни 30 + суффикс + 9 осей** | 38.0 | 0.407 | 77% | 65% |
| корни 30 + 3 непрерывные формы + 9 осей | 46.4 | 0.423 | 75% | 68% |
| глобальные plain, 11 осей | 38.1 | 0.390 | 71% | 55% |
| глобальные split (3+8) | 38.1 | 0.376 | 79% | 54% |

## Омонимы и конверсии: корень и суффикс записи

- **march**: noun → MONTH-o; verb → MONTH-i
- **rent**: noun → MONTH-o; verb → MONTH-i
- **issue**: noun → REQUEST-o; verb → REQUEST-i
- **point**: noun → PLACE-o; verb → PLACE-i
- **order**: noun → REQUEST-o; verb → REQUEST-i
- **close**: verb → MOVE-i; adj → PLACE-a
- **work**: noun → TOOL-o; verb → TOOL-i
- **play**: noun → MOVE-o; verb → MOVE-i
- **love**: noun → THINK-o; verb → THINK-i
- **pretty**: adj → THINK-a; adv → THINK-e

## Корни (30), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **THINK** (228): `-o` idea, thing, notion; `-i` think, suppose, believe; `-a` sure, likely, afraid; `-e` probably, maybe, perhaps
- **HURT** (188): `-o` hurt, injury, pain; `-i` hurt, injure, ache; `-a` sore, painful, severe; `-e` badly, severely, emotionally
- **CURVE** (150): `-o` curve, line, circle; `-i` curve, bend, tilt; `-a` upward, straight, parallel; `-e` upward, backward, straight
- **AMOUNT** (148): `-o` amount, quantity, total; `-i` total, expend, average; `-a` least, less, equal; `-e` proportionately, roughly, enough
- **REQUEST** (139): `-o` request, demand, appeal; `-i` request, demand, ask; `-a` prompt, immediate, necessary; `-e` politely, hereby, apologetically
- **CORRESPOND** (138): `-o` match, address, relative; `-i` correspond, coincide, match; `-a` identical, similar, comparable; `-e` respectively, exactly, precisely
- **MIXTURE** (137): `-o` mixture, blend, combination; `-i` mix, blend, mingle; `-a` liquid, aqueous, pure; `-e` finely, mostly, together
- **MOVE** (137): `-o` movement, motion, step; `-i` move, transfer, dance; `-a` fast, slow, swift; `-e` forward, swiftly, quickly
- **PROVIDE** (133): `-o` supply, support, provision; `-i` provide, supply, feed; `-a` adequate, ample, reliable; `-e` helpfully, uniquely, sufficiently
- **COLOR** (127): `-o` color, purple, blue; `-i` stain, paint, shade; `-a` purple, blue, pink; `-e` vividly, beautifully
- **DECREASE** (124): `-o` decrease, decline, increase; `-i` decrease, diminish, lessen; `-a` smaller, greater, fewer; `-e` significantly, dramatically, considerably
- **MONTH** (124): `-o` month, week, year; `-i` march, rent, spring; `-a` lunar, fifth, twentieth; `-e` annually, sometime, twice
- **WIND** (116): `-o` wind, weather, rain; `-i` wind, rain, blow; `-a` cold, cool, warm; `-e` north, northward, southward
- **NOISE** (116): `-o` noise, clamor, roar; `-i` roar, sound, grunt; `-a` loud, shrill, quiet; `-e` loudly, aloud, quietly
- **CHIEF** (115): `-o` chief, leader, head; `-i` appoint, supervise, guide; `-a` chief, principal, former; `-e` formerly, headlong, angrily
- **HONOR** (114): `-o` honor, award, recognition; `-i` honor, respect, award; `-a` worthy, proud, heroic; `-e` proudly, solemnly, rightly
- **PLACE** (113): `-o` place, spot, location; `-i` place, park, spot; `-a` near, appropriate, downtown; `-e` somewhere, near, anywhere
- **CLUTCH** (112): `-o` clutch, grip, snatch; `-i` clutch, seize, grip; `-a` loose, secure, precious; `-e` firmly, tightly, momentarily
- **FIGHT** (111): `-o` fight, struggle, battle; `-i` fight, struggle, contend; `-a` fierce, competitive, tough; `-e` stoutly, doggedly, vigorously
- **STUDY** (110): `-o` study, survey, research; `-i` study, survey, examine; `-a` analytic, preliminary, experimental; `-e` carefully, intently, thoughtfully
- **EVIDENCE** (104): `-o` evidence, proof, witness; `-i` prove, testify, rebut; `-a` evident, scientific, apparent; `-e` conclusively, empirically, clearly
- **DEFEAT** (100): `-o` defeat, victory, loss; `-i` defeat, overcome, win; `-a` decisive, formidable, final; `-e` triumphantly, successfully, easily
- **AMERICAN** (99): `-o` american, native, mexican; `-i` invade, live, eat; `-a` american, native, mexican; `-e` abroad
- **TOOL** (95): `-o` tool, implement, instrument; `-i` tool, implement, utilize; `-a` useful, effective, practical; `-e` effectively, universally, automatically
- **PLAN** (94): `-o` plan, design, program; `-i` plan, design, schedule; `-a` ambitious, underway, utopian; `-e` methodically, initially, deliberately
- **INFORM** (88): `-o` information, notice, report; `-i` inform, notify, advise; `-a` aware, alert, present; `-e` promptly, shortly, briefly
- **CHANGE** (88): `-o` change, shift, switch; `-i` change, alter, modify; `-a` variable, different, radical; `-e` radically, differently, permanently
- **COMPANY** (86): `-o` company, corporation, firm; `-i` invest, sell, venture; `-a` firm, commercial, industrial; `-e` commercially, wholly, privately
- **ROOM** (80): `-o` room, bedroom, hall; `-i` huddle, bathe, shed; `-a` upstairs, interior, comfortable; `-e` upstairs, downstairs, inside
- **CHRISTIAN** (67): `-o` christian, catholic, protestant; `-i` baptize, preach, pray; `-a` christian, religious, protestant

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** define, attribute, attribute, consequence, implication, designate, imply  /  **+** stare, nicely, tumble, glance, fall, gouge, suddenly
- M2: **−** achieve, farther, attain, able, reach, accomplish, experience  /  **+** abolish, rule, rule, dismiss, reject, denounce, split
- M3: **−** trim, verify, adjust, repair, arrange, check, filter  /  **+** seldom, universally, rarely, peculiarly, surprisingly, remarkably, characteristically
- M4: **−** adopt, alternative, alternative, repay, owe, choose, spend  /  **+** feature, burst, intensity, intense, burst, surge, characteristic
- M5: **−** forever, eternal, cease, persist, hereafter, inevitable, lag  /  **+** tremendously, wonderful, fantastic, excellent, incredibly, vastly, greatly
- M6: **−** headlong, headlong, instant, chance, opportunity, race, venture  /  **+** stick, remain, stiffly, stay, maintain, keep, rigid
- M7: **−** further, southward, westward, northward, broaden, elsewhere, extend  /  **+** perfectly, utterly, absolutely, completely, downright, thoroughly, perfect
- M8: **−** cautiously, steady, calmly, steady, strongly, firmly, nervously  /  **+** unique, instance, individual, uniquely, create, individual, encounter
- M9: **−** encourage, spring, inspire, force, flourish, capacity, urge  /  **+** comment, remark, trace, note, vague, trace, notice