# Корни по смыслу + суффикс части речи (numberbatch, режим sense, 3571 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 10 + суффикс + 3 осей** | 15.7 | 0.371 | 74% | 38% |
| корни 10 + 3 непрерывные формы + 3 осей | 24.1 | 0.356 | 75% | 31% |
| глобальные plain, 5 осей | 17.3 | 0.333 | 72% | 28% |
| глобальные split (3+2) | 17.3 | 0.364 | 80% | 22% |
| **корни 10 + суффикс + 6 осей** | 26.1 | 0.384 | 79% | 48% |
| корни 10 + 3 непрерывные формы + 6 осей | 34.5 | 0.379 | 77% | 42% |
| глобальные plain, 8 осей | 27.7 | 0.348 | 76% | 43% |
| глобальные split (3+5) | 27.7 | 0.361 | 81% | 40% |
| **корни 30 + суффикс + 3 осей** | 17.3 | 0.383 | 67% | 53% |
| корни 30 + 3 непрерывные формы + 3 осей | 25.7 | 0.365 | 65% | 53% |
| глобальные plain, 5 осей | 17.3 | 0.333 | 72% | 28% |
| глобальные split (3+2) | 17.3 | 0.364 | 80% | 22% |
| **корни 30 + суффикс + 6 осей** | 27.7 | 0.388 | 68% | 56% |
| корни 30 + 3 непрерывные формы + 6 осей | 36.0 | 0.379 | 69% | 56% |
| глобальные plain, 8 осей | 27.7 | 0.348 | 76% | 43% |
| глобальные split (3+5) | 27.7 | 0.361 | 81% | 40% |
| **корни 30 + суффикс + 9 осей** | 38.0 | 0.398 | 71% | 60% |
| корни 30 + 3 непрерывные формы + 9 осей | 46.4 | 0.385 | 69% | 60% |
| глобальные plain, 11 осей | 38.1 | 0.364 | 76% | 54% |
| глобальные split (3+8) | 38.1 | 0.373 | 83% | 53% |

## Омонимы и конверсии: корень и суффикс записи

- **march**: 
- **rent**: noun → LAND-o; verb → LAND-i
- **issue**: noun → ADDRESS-o; verb → ADDRESS-i
- **point**: noun → DENOTE-o; verb → DENOTE-i
- **order**: noun → ADDRESS-o; verb → ADDRESS-i
- **close**: verb → NEAR-i; adj → NEAR-a
- **work**: noun → WORK-o; verb → WORK-i
- **play**: noun → WORK-o; verb → WORK-i
- **love**: noun → LOVE-o; verb → LOVE-i
- **pretty**: adj → EASY-a; adv → EASY-e

## Корни (30), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **HURT** (159): `-o` hurt, injury, pain; `-i` hurt, injure, ache; `-a` sore, painful, severe; `-e` badly, severely, emotionally
- **LIQUID** (157): `-o` liquid, fluid, flow; `-i` flow, drip, pour; `-a` liquid, aqueous, dry
- **STEP** (148): `-o` step, tread, pace; `-i` step, pace, tread; `-a` backward, slow, farther; `-e` forward, backward, slowly
- **PROVIDE** (146): `-o` supply, support, provision; `-i` provide, supply, feed; `-a` adequate, ample, sufficient; `-e` helpfully, plenty, enough
- **UPHOLD** (146): `-o` oath, dignity, honor; `-i` uphold, maintain, defend; `-a` moral, firm, supreme; `-e` solemnly, firmly, stoutly
- **TWIST** (146): `-o` twist, whirl, roll; `-i` twist, curve, whirl; `-a` round, upward, loose; `-e` upward, loosely, awkwardly
- **STUDY** (143): `-o` study, survey, research; `-i` study, survey, examine; `-a` analytic, preliminary, experimental; `-e` carefully, intently, thoughtfully
- **AVERAGE** (142): `-o` percentage, rate, ratio; `-i` average, mean, equate; `-a` average, ordinary, normal; `-e` typically, normally, ordinarily
- **OBVIOUSLY** (130): `-o` fact, implication, thing; `-i` suppose, guess, think; `-a` obvious, sure, evident; `-e` obviously, evidently, apparently
- **LAND** (129): `-o` land, property, desert; `-i` land, sprawl, inherit; `-a` residential, rural, muddy; `-e` home, abroad, privately
- **CHIEF** (128): `-o` chief, leader, head; `-i` appoint, supervise, master; `-a` chief, principal, official; `-e` grimly
- **ADDRESS** (124): `-o` address, message, reference; `-i` address, name, list; `-a` specific, relevant, particular; `-e` specifically, directly, correctly
- **PAST** (124): `-o` past, years, time; `-i` span, remember, lag; `-a` past, previous, late; `-e` earlier, previously, before
- **LOVE** (124): `-o` love, dear, dislike; `-i` love, cherish, hate; `-a` dear, beloved, romantic; `-e` madly, sincerely, forever
- **DENOTE** (113): `-o` symbol, mark, sign; `-i` denote, indicate, symbolize; `-a` literal, distinct, ambiguous; `-e` commonly, conspicuously, characteristically
- **EAGER** (112): `-o` desire, hope, attempt; `-i` desire, urge, hope; `-a` eager, enthusiastic, ready; `-e` eagerly, anxiously, excitedly
- **PLACE** (108): `-o` place, spot, location; `-i` place, park, spot; `-a` appropriate, downtown, fifth; `-e` somewhere, anywhere, elsewhere
- **EASY** (108): `-o` ease, difficulty, fool; `-i` ease, smooth, relax; `-a` easy, simple, convenient; `-e` easily, readily, conveniently
- **ARREST** (108): `-o` arrest, capture, snatch; `-i` arrest, seize, clutch; `-a` guilty, anti, sober; `-e` aboard
- **CHANGE** (106): `-o` change, shift, variation; `-i` change, alter, modify; `-a` variable, different, radical; `-e` radically, differently, accordingly
- **ARGUMENT** (106): `-o` argument, debate, quarrel; `-i` argue, debate, quarrel; `-a` logical, philosophical, theoretical; `-e` empirically, conclusively, briefly
- **LIGHT** (103): `-o` light, glow, gleam; `-i` illuminate, glow, gleam; `-a` light, bright, dim; `-e` dimly, brilliantly, tonight
- **COMPLAIN** (103): `-o` wail, groan, cry; `-i` complain, grumble, groan; `-a` angry, loud, indifferent; `-e` angrily, loudly, bitterly
- **WORK** (102): `-o` work, project, job; `-i` work, exercise, act; `-a` productive, busy, active; `-e` actively, satisfactorily, independently
- **SUDDEN** (101): `-o` surprise, surge, collapse; `-i` precipitate, surprise, burst; `-a` sudden, rapid, spontaneous; `-e` suddenly, abruptly, unexpectedly
- **STRANGE** (100): `-o` unknown, phenomenon, mystery; `-i` wonder, notice, resemble; `-a` strange, weird, odd; `-e` curiously, peculiarly, vaguely
- **SIGNIFICANT** (95): `-o` significance, importance, consequence; `-i` diminish, minimize, reduce; `-a` significant, substantial, considerable; `-e` significantly, appreciably, substantially
- **NEAR** (92): `-o` distance, end, mile; `-i` close, shut, reach; `-a` near, close, nearby; `-e` near, nearby, nearly
- **ENTIRELY** (87): `-o` nothing, manner, content; `-i` complete, abandon, exclude; `-a` entire, whole, total; `-e` entirely, wholly, completely
- **INFLUENCE** (81): `-o` influence, force, effect; `-i` influence, exert, affect; `-a` powerful, dominant, mighty; `-e` indirectly, mighty, inversely

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** result, warrant, method, aim, initiate, formulate, implement  /  **+** gasp, mighty, glance, mighty, barely, pant, slug
- M2: **−** attend, worthy, request, venture, volunteer, refuse, visit  /  **+** steady, rigid, continuous, offset, contrast, erect, flat
- M3: **−** concern, snarl, expect, worry, suspect, worry, seem  /  **+** charge, assign, affix, total, load, pay, trim
- M4: **−** distinctly, greet, slap, famous, introduce, present, contemporary  /  **+** finite, persist, indefinite, possible, entail, potential, unlikely
- M5: **−** abolish, originally, skip, omit, impulse, reject, mainly  /  **+** competent, closely, grasp, identify, respect, respect, locate
- M6: **−** discover, ideal, find, ideal, achieve, capture, derive  /  **+** delay, postpone, moderate, lag, delay, sharply, slow
- M7: **−** tend, prefer, often, generally, usually, typically, ordinarily  /  **+** prove, victory, improvement, confirm, advance, achieve, triumphantly
- M8: **−** remark, outcome, comment, impression, note, sentence, unlikely  /  **+** educate, train, develop, promote, strengthen, conscious, inner
- M9: **−** remarkably, brilliantly, culminate, incredibly, brilliant, worst, formidable  /  **+** consciousness, concern, notice, concern, sense, conscious, worry