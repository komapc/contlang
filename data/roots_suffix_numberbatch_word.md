# Корни по смыслу + суффикс части речи (numberbatch, режим word, 3000 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 10 + суффикс + 3 осей** | 15.7 | 0.398 | 63% | 36% |
| корни 10 + 3 непрерывные формы + 3 осей | 24.1 | 0.386 | 66% | 37% |
| глобальные plain, 5 осей | 17.3 | 0.374 | 56% | 26% |
| глобальные split (3+2) | 17.3 | 0.372 | 73% | 21% |
| **корни 10 + суффикс + 6 осей** | 26.1 | 0.405 | 66% | 43% |
| корни 10 + 3 непрерывные формы + 6 осей | 34.5 | 0.389 | 68% | 45% |
| глобальные plain, 8 осей | 27.7 | 0.393 | 58% | 39% |
| глобальные split (3+5) | 27.7 | 0.377 | 68% | 38% |
| **корни 30 + суффикс + 3 осей** | 17.3 | 0.411 | 65% | 62% |
| корни 30 + 3 непрерывные формы + 3 осей | 25.7 | 0.405 | 69% | 64% |
| глобальные plain, 5 осей | 17.3 | 0.374 | 56% | 26% |
| глобальные split (3+2) | 17.3 | 0.372 | 73% | 21% |
| **корни 30 + суффикс + 6 осей** | 27.7 | 0.417 | 68% | 66% |
| корни 30 + 3 непрерывные формы + 6 осей | 36.0 | 0.407 | 71% | 66% |
| глобальные plain, 8 осей | 27.7 | 0.393 | 58% | 39% |
| глобальные split (3+5) | 27.7 | 0.377 | 68% | 38% |
| **корни 30 + суффикс + 9 осей** | 38.0 | 0.426 | 70% | 70% |
| корни 30 + 3 непрерывные формы + 9 осей | 46.4 | 0.418 | 72% | 68% |
| глобальные plain, 11 осей | 38.1 | 0.400 | 65% | 50% |
| глобальные split (3+8) | 38.1 | 0.400 | 70% | 51% |

## Корни (30), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **THINK** (169): `-o` idea, thing, doubt; `-i` think, suppose, believe; `-a` sure, likely, afraid; `-e` probably, maybe, perhaps
- **MOVE** (127): `-o` movement, motion, step; `-i` move, shift, push; `-a` quick, rapid, fast; `-e` forward, swiftly, backward
- **DEFEAT** (124): `-o` victory, loss, battle; `-i` defeat, win, overcome; `-a` decisive, final, formidable; `-e` triumphantly, stoutly, easily
- **DESIRE** (121): `-o` desire, impulse, necessity; `-i` wish, want, urge; `-a` eager, desperate, unable; `-e` desperately, eagerly, simply
- **PROVIDE** (118): `-o` provision, assistance, complement; `-i` provide, furnish, give; `-a` adequate, reliable, ample; `-e` helpfully, uniquely, sufficiently
- **AMOUNT** (116): `-o` amount, quantity, sum; `-i` expend, allot, pay; `-a` total, considerable, minimum; `-e` proportionately, roughly, approximately
- **CORRESPOND** (112): `-o` address, letter, description; `-i` correspond, coincide, pertain; `-a` identical, similar, equal; `-e` respectively, exactly, precisely
- **REGARD** (111): `-o` respect, consideration, relation; `-i` regard, concern, commend; `-a` particular, careful, worthy; `-e` particularly, especially, notably
- **INCREASE** (110): `-o` reduction, growth, improvement; `-i` increase, decrease, augment; `-a` higher, greater, larger; `-e` significantly, dramatically, considerably
- **ROAD** (109): `-o` road, street, path; `-i` trail, drive, veer; `-a` narrow, suburban, straight; `-e` along, southward, westward
- **STICK** (106): `-o` stick, finger, hand; `-i` adhere, glue, cling; `-a` wooden, rigid, hard; `-e` firmly, stubbornly, doggedly
- **OCCURRENCE** (106): `-o` occurrence, incident, event; `-i` occur, happen, encounter; `-a` unusual, rare, occasional; `-e` ordinarily, rarely, seldom
- **NOISE** (105): `-o` noise, sound, din; `-i` clamor, roar, murmur; `-a` loud, shrill, quiet; `-e` loudly, aloud, quietly
- **MONTH** (105): `-o` month, week, year; `-i` march, rent, fall; `-a` lunar, twentieth, fourth; `-e` annually, sometime, twice
- **MIXTURE** (102): `-o` mixture, combination, powder; `-i` mix, blend, mingle; `-a` liquid, aqueous, pure; `-e` mostly, together, alternately
- **COLOR** (99): `-o` color, shade, texture; `-i` paint, blush, stain; `-a` purple, yellow, blue; `-e` vividly, beautifully, instantly
- **EVIDENCE** (97): `-o` evidence, proof, explanation; `-i` prove, testify, rebut; `-a` evident, scientific, apparent; `-e` conclusively, empirically, clearly
- **RESTRAIN** (96): `-o` control, limit, block; `-i` restrain, confine, restrict; `-a` calm, protective, bound; `-e` tightly, violently, temporarily
- **EXAMINE** (95): `-o` examination, investigation, study; `-i` examine, inspect, investigate; `-a` curious, analytic, subjective; `-e` carefully, thoroughly, intently
- **ROOM** (89): `-o` room, bedroom, hall; `-i` huddle, sit, separate; `-a` comfortable, private, homely; `-e` upstairs, downstairs, inside
- **RELIGION** (88): `-o` religion, faith, theology; `-i` profess, preach, pray; `-a` religious, christian, spiritual; `-e` radically
- **CREATE** (86): `-o` form, environment, illusion; `-i` create, generate, produce; `-a` creative, unique, new; `-e` thereby, newly, deliberately
- **INFORM** (82): `-o` information, news, message; `-i` inform, notify, advise; `-a` aware, public, educational; `-e` promptly, shortly, immediately
- **COMMITTEE** (81): `-o` committee, commission, board; `-i` appoint, elect, vote; `-a` legislative, democratic, municipal; `-e` unanimously, formally
- **COMPANY** (79): `-o` company, corporation, manufacturer; `-i` venture, invest, sell; `-a` firm, industrial, commercial; `-e` commercially, wholly, privately
- **CUT** (78): `-o` shear, throat, half; `-i` cut, slash, trim; `-a` sharp, short, thin; `-e` off, sharply, finely
- **OFFICER** (75): `-o` officer, lieutenant, police; `-i` escort, warrant, associate; `-a` chief, administrative, principal; `-e` formerly, drunkenly, apologetically
- **WRITER** (72): `-o` writer, author, editor; `-i` write, publish, read; `-a` literary, artistic, fictional; `-e` brilliantly
- **WEATHER** (72): `-o` weather, rain, winter; `-i` forecast, hail, predict; `-a` cold, warm, wet; `-e` coldly, bitterly, fortunately
- **DISEASE** (70): `-o` disease, lung, tumor; `-i` plague, cure, spread; `-a` infectious, chronic, bacterial; `-e` sexually

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** fundamental, principle, term, objective, requirement, adhere, basic  /  **+** grateful, shudder, dear, glad, joy, friendly, hungry
- M2: **−** broad, profound, extensive, impulse, sudden, intensity, shudder  /  **+** oblige, fortunate, lucky, certify, owe, insist, reside
- M3: **−** real, truly, genuine, uniquely, wholly, possess, true  /  **+** impatiently, anxiously, cautiously, nervously, hastily, angrily, wearily
- M4: **−** hereafter, somewhere, forever, eternal, inevitable, await, constant  /  **+** tremendously, vastly, impressive, remarkably, big, large, particularly
- M5: **−** ask, invoke, beckon, lend, invite, borrow, grant  /  **+** fairly, perfectly, reasonably, remarkably, extremely, vitally, sufficiently
- M6: **−** flatly, unadjusted, tax, ratio, totally, wildly, rate  /  **+** linger, foresee, considerable, farther, significant, emerge, entail
- M7: **−** strive, mentally, educate, engage, collaborate, vigorous, celebrate  /  **+** vague, shortly, sadly, nevertheless, mention, notice, though
- M8: **−** stubbornly, exist, stare, falter, underlie, sullen, increasingly  /  **+** select, arrange, able, ideally, dispose, device, locate
- M9: **−** incredible, brilliant, fantastic, magnificent, remarkable, impressive, headlong  /  **+** frequent, tend, sometimes, usually, external, frequently, mostly