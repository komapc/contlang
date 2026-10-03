# Корни по смыслу + суффикс части речи (numberbatch, режим sense, 3571 записей)

Форма (3 LDA-направления) вычтена перед выбором корней, поэтому корни не зависят от части речи. Слово = корень + суффикс эсперанто (`-o -i -a -e`, 2 бита) + u универсальных смысловых осей. Сравнение со схемой «корень + 3 непрерывные оси формы + u осей» и с глобальными осями при той же длине кода.

| схема | биты на слово | wup | pos | top50 |
| :-- | --: | --: | --: | --: |
| **корни 30 + суффикс + 6 осей** | 27.7 | 0.404 | 65% | 61% |
| корни 30 + 3 непрерывные формы + 6 осей | 36.0 | 0.416 | 68% | 62% |
| глобальные plain, 8 осей | 27.7 | 0.348 | 76% | 43% |
| глобальные split (3+5) | 27.7 | 0.361 | 81% | 40% |
| **корни 30 + суффикс + 9 осей** | 38.0 | 0.422 | 67% | 64% |
| корни 30 + 3 непрерывные формы + 9 осей | 46.4 | 0.423 | 70% | 64% |
| глобальные plain, 11 осей | 38.1 | 0.364 | 76% | 54% |
| глобальные split (3+8) | 38.1 | 0.373 | 83% | 53% |

## Омонимы и конверсии: корень и суффикс записи

- **march**: 
- **rent**: noun → BEDROOM-o; verb → BEDROOM-i
- **issue**: noun → REQUEST-o; verb → REQUEST-i
- **point**: noun → PARTICULAR-o; verb → PARTICULAR-i
- **order**: noun → REQUEST-o; verb → REQUEST-i
- **close**: verb → CONNECT-i; adj → CONNECT-a
- **work**: noun → DEVELOP-o; verb → DEVELOP-i
- **play**: noun → EMOTION-o; verb → EMOTION-i
- **love**: noun → EMOTION-o; verb → EMOTION-i
- **pretty**: adj → TERRIBLY-a; adv → TERRIBLY-e

## Корни (30), выбранные по смыслу, и их формы

Для каждого корня — ближайшие слова каждого суффикса.

- **TUMBLE** (159): `-o` fall, collapse, slide; `-i` tumble, fall, plunge; `-a` headlong, rough, wild; `-e` headlong, down, sharply
- **REQUEST** (157): `-o` request, demand, appeal; `-i` request, demand, ask; `-a` formal, brief, verbal; `-e` hereby, politely, apologetically
- **DEVELOP** (152): `-o` development, progress, growth; `-i` develop, mature, build; `-a` mature, creative, productive; `-e` commercially, jointly
- **VICTORY** (141): `-o` victory, defeat, success; `-i` win, defeat, prevail; `-a` decisive, final, upset; `-e` triumphantly
- **AMOUNT** (138): `-o` amount, quantity, total; `-i` total, expend, average; `-a` least, less, equal; `-e` proportionately, enough, roughly
- **SOUTHWARD** (137): `-o` south, north, west; `-i` veer, wind, curve; `-a` southern, northern, eastern; `-e` southward, northward, north
- **EMOTION** (136): `-o` emotion, love, fear; `-i` sense, rage, regret; `-a` emotional, romantic, nervous; `-e` emotionally, unconsciously, mentally
- **AFFIRM** (133): `-o` claim, belief, proof; `-i` affirm, assert, claim; `-a` pursuant, true, positive; `-e` conclusively, solemnly, unanimously
- **CERTAINLY** (132): `-o` doubt, thing, nothing; `-i` suppose, presume, think; `-a` sure, likely, unlikely; `-e` certainly, surely, definitely
- **WATER** (131): `-o` water, stream, sewage; `-i` stream, drown, swim; `-a` aqueous, liquid, dry; `-e` overboard
- **REDUCE** (129): `-o` decrease, reduction, increase; `-i` reduce, lessen, decrease; `-a` smaller, minimal, greater; `-e` significantly, dramatically, considerably
- **PARTICULAR** (127): `-o` instance, matter, subject; `-i` specify, pertain, regard; `-a` particular, specific, special; `-e` specifically, particularly, specially
- **NECK** (124): `-o` neck, throat, shoulder; `-i` bow, choke, wrap; `-a` sore, upper, tight; `-e` around, tightly, loosely
- **PERFECTLY** (123): `-o` ideal, manner, match; `-i` fit, suit, match; `-a` perfect, fine, ideal; `-e` perfectly, beautifully, nicely
- **OFFICER** (121): `-o` officer, lieutenant, police; `-i` command, escort, guard; `-a` chief, official, administrative; `-e` aboard
- **MURMUR** (121): `-o` murmur, whisper, groan; `-i` murmur, mutter, whisper; `-a` loud, silent, quiet; `-e` loudly, silently, aloud
- **DEPICT** (120): `-o` picture, photograph, representation; `-i` depict, portray, illustrate; `-a` mythological, representative, realistic; `-e` vividly, realistically, prominently
- **PROVIDE** (120): `-o` supply, support, provision; `-i` provide, supply, feed; `-a` adequate, sufficient, reliable; `-e` helpfully
- **CONNECT** (120): `-o` link, connection, tie; `-i` connect, link, associate; `-a` parallel, intimate, cooperative; `-e` directly, together, indirectly
- **EXAMINE** (111): `-o` study, survey, examination; `-i` examine, probe, inspect; `-a` curious, relative, analytic; `-e` carefully, closely, cautiously
- **REMAIN** (110): `-o` rest, safe, secret; `-i` remain, stay, persist; `-a` motionless, alive, persistent; `-e` forever, permanently, stubbornly
- **BEDROOM** (104): `-o` bedroom, room, apartment; `-i` sleep, awake, awaken; `-a` upstairs, residential, asleep; `-e` upstairs, downstairs, home
- **TERRIBLY** (100): `-o` affair, worst, mess; `-i` feel, miss, frighten; `-a` awful, terrible, pretty; `-e` terribly, awful, awfully
- **GLEAM** (99): `-o` gleam, glow, glare; `-i` gleam, glow, shine; `-a` bright, light, dim; `-e` dimly, visibly
- **ACADEMIC** (98): `-o` college, graduate, university; `-i` graduate, institute, peer; `-a` academic, educational, vocational; `-e` academically, abroad, algebraically
- **QUICKLY** (96): `-o` hurry, swift, instant; `-i` hurry, speed, rush; `-a` quick, fast, rapid; `-e` quickly, swiftly, rapidly
- **EARLIER** (92): `-o` yesterday, past, morning; `-i` precede, postpone, recall; `-a` previous, early, past; `-e` earlier, previously, yesterday
- **USUALLY** (84): `-o` tendency, ordinary, occurrence; `-i` tend, occur, prefer; `-a` frequent, customary, usual; `-e` usually, normally, typically
- **FURIOUSLY** (78): `-o` fist, attack, quarrel; `-i` attack, erupt, whip; `-a` furious, frantic, angry; `-e` furiously, frantically, angrily
- **TREMENDOUS** (78): `-o` magnitude, plenty, surprise; `-i` swell, admire, appreciate; `-a` tremendous, enormous, huge; `-e` mighty, literally

## Универсальные смысловые оси (30 корней, 9 осей)

Оси найдены по отклонениям слов от центра своего корня; полюса — записи с крайними значениями. Знак и порядок осей нестабильны между запусками.

- M1: **−** flat, point, relatively, curve, solid, steady, stem  /  **+** repay, owe, spare, participate, trade, reserve, hereafter
- M2: **−** everywhere, lovely, beautiful, shiver, kneel, pack, little  /  **+** result, consequence, result, reflect, influence, objective, outcome
- M3: **−** set, assign, able, select, place, pick, pick  /  **+** hurt, hurt, upset, disagree, relate, resent, familiar
- M4: **−** halt, halt, delay, hurt, force, delay, hurt  /  **+** popular, name, name, equally, formerly, fifth, place
- M5: **−** find, discover, create, locate, destroy, retrieve, found  /  **+** cautiously, progress, advance, heed, regard, ahead, anxiously
- M6: **−** struggle, struggle, force, fight, persuade, compel, challenge  /  **+** note, note, remark, comment, notice, mark, mention
- M7: **−** alternative, alternative, abandon, conclusion, proposal, possibility, endless  /  **+** aware, maintain, secure, skilled, recognize, hard, rugged
- M8: **−** attain, reach, chance, encounter, farther, achieve, seek  /  **+** destroy, compound, abolish, sever, main, fundamentally, dissolve
- M9: **−** grasp, realistically, contemplate, close, consider, comprehend, abstract  /  **+** surge, prompt, appreciably, excite, active, notably, stimulate