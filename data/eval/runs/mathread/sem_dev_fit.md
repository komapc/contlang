## dev/fit: 200 прочтений (100 слов × декодеры)

- Haiku: cos первого 0.31, лучший из трёх 0.40, близко (cos ≥ 0,5) 37, точно 22
- математика (те же коды): первыми 85/100, cos первого 0.94
- часть речи o: n 90, Haiku cos 0.29, близко 15
- часть речи i: n 50, Haiku cos 0.34, близко 11
- часть речи a: n 40, Haiku cos 0.27, близко 4
- часть речи e: n 20, Haiku cos 0.45, близко 7
- одно слово: n 154, Haiku cos 0.33, близко 31
- пара: n 46, Haiku cos 0.28, близко 6

## Признаки кода и читаемость (корреляция Спирмена с cos первого ответа Haiku)

- наименьшая близость корня к слову: +0.21
- средняя близость корней: +0.34
- близость главного корня: +0.38
- худшее место корня среди ближайших к слову: -0.13
- число корней: -0.04
- корней со слабым уровнем (|v| ≤ 2): -0.04
- cos первого прочтения математики: -0.02
- место у математики: +0.04

## По словам

| слово | код | Haiku первым (cos) | математика |
|---|---|---|---|
| satellite | `NEAR(=-2) ART(=-3) ABOVE(=+4) | o` | satellite (1.00), satellite (1.00) | satellite (1) |
| adjacent | `NEAR(=+3) SIDE(=0) INSIDE(=-1) | a` | adjacent (1.00), adjacent (1.00) | adjacent (1) |
| invite | `GIVE(=+1) TONE(=+3) WANT(=0) | i PI JOIN(=+2) MOVE(=0) | o` | invite (1.00), invite (1.00) | invite (1) |
| read | `TEXT KNOW(=+1) SEE | i` | read (1.00), read (1.00) | read (1) |
| roughly | `MEASURE(=+1) CARE(=-2) NEAR(=+1) | e` | roughly (1.00), roughly (1.00) | roughly (1) |
| adjust | `CHANGE(=+2) MEASURE(=0) CARE(=+1) | i` | adjust (1.00), adjust (1.00) | adjust (1) |
| ahead | `SIDE(=+2) TIME(=+1) MOVE(=+1) | e` | ahead (1.00), forward (0.56) | ahead (1) |
| dinner | `CONSUME(=+3) PART(=+3) TIME(=+1) | o` | meal (0.77), meal (0.77) | dinner (1) |
| fee | `VALUE(=0) GIVE(=+5) MEASURE(=+1) | o` | price (0.53), fee (1.00) | premium (2) |
| breakfast | `CONSUME(=+4) FEEL(=-4) BEGIN(=-5) | o` | breakfast (1.00), appetizer (0.37) | breakfast (1) |
| drive | `MOVE(=+2) DO(=+3) NEAR(=0) | i` | push (0.35), drive (1.00) | drive (1) |
| firmly | `CARE(=0) CHANGE(=-4) TOUCH(=+1) | e` | still (0.28), firmly (1.00) | firmly (1) |
| suburb | `NEAR(=+2) PLACE VALUE(=-2) | o PI PART(=-1) FEEL(=-5) | o` | suburb (1.00), hamlet (0.28) | outskirts (2) |
| follow | `MOVE(=0) CARE(=+3) SAME(=+2) | i` | tread (0.27), follow (1.00) | follow (1) |
| announcement | `TIME(=+1) RULE(=+1) SAY(=0) | o` | announcement (1.00), schedule (0.25) | announcement (1) |
| source | `HAPPEN(=-4) INSIDE(=0) CAN(=+1) | o` | source (1.00), cause (0.20) | source (1) |
| sometime | `TIME(=+1) | e` | soon (0.58), soon (0.58) | sometime (1) |
| municipality | `RULE(=+3) PART(=+1) PLACE | o` | district (0.52), province (0.52) | municipality (1) |
| magnitude | `MEASURE(=0) BIG(=+2) HAPPEN(=0) | o` | scale (0.51), scale (0.51) | magnitude (1) |
| forecast | `MEASURE(=+2) TIME(=+4) HEAT(=-1) | i` | forecast (1.00), age (0.02) | forecast (1) |
| house | `ABSTRACT(=-2) PLACE INSIDE(=+2) | o` | room (0.46), room (0.46) | house (1) |
| massive | `BIG(=+2) | a PI MEASURE(=-1) HAPPEN(=0) | o` | large (0.75), volume (0.17) | huge (3) |
| change | `CHANGE(=+1) | i PI GIVE(=0) CONSUME(=-2) | o` | adjust (0.51), exchange (0.37) | change (1) |
| sentence | `RULE(=+5) ABSTRACT(=+1) BEGIN(=+2) | o` | decree (0.28), verdict (0.53) | sentence (1) |
| electrical | `ART(=-2) LONG(=0) HEAT(=+2) | a` | thermal (0.38), thermal (0.38) | electrical (1) |
| charitable | `GIVE(=+4) TONE(=+5) RULE(=-2) | a` | generous (0.52), kind (0.24) | charitable (1) |
| beef | `CONSUME(=+3) THING(=+5) GRAIN(=+3) | o` | food (0.36), food (0.36) | meat (2) |
| supermarket | `NEAR(=+2) VALUE(=-4) CONSUME(=+5) | o` | fast food (0.45), snack (0.27) | supermarket (1) |
| maintain | `CHANGE(=-3) GIVE(=-1) THINK(=+3) | i PI MOVE(=-3) ABOVE(=+4) | o` | keep (0.69), ponder (0.02) | maintain (1) |
| please | `WANT(=+1) TONE(=+5) CAN(=-1) | i` | implore (0.45), plead (0.24) | please (1) |
| repair | `CHANGE(=+1) ART(=-2) ABOVE(=+4) | i` | upgrade (0.35), upgrade (0.35) | repair (1) |
| virtually | `MANY(=0) SAME(=+1) CARE(=0) | e PI CAN(=-1) | o` | evenly (0.31), consistently (0.36) | practically (4) |
| account | `MEASURE(=+1) GIVE(=+2) TEXT | o` | invoice (0.42), bill (0.20) | account (1) |
| discount | `VALUE(=-2) GIVE(=+2) MEASURE(=+1) | i PI PART(=+3) JOIN(=+2) | o` | subscribe (0.27), pay (0.35) | discount (1) |
| vehicle | `MOVE(=+3) DO(=+5) BODY | o PI PART(=+3) FIGHT(=+5) | o` | tank (0.30), tank (0.30) | vehicle (1) |
| nevertheless | `MANY(=-1) TIME(=+1) TONE(=+1) | e PI SAME(=0) THINK(=-1) | o` | briefly (0.26), seldom (0.32) | nevertheless (1) |
| harassment | `RULE(=0) GOOD(=-5) FIGHT(=+2) | o` | quarrel (0.15), violence (0.43) | casualty (2) |
| assistant | `DO(=-1) SOMEONE(=+2) RULE(=+2) | o PI KNOW(=0) BIG(=-3) | o` | official (0.29), official (0.29) | administrator (27) |
| eligible | `CAN(=+1) GIVE(=+2) RULE(=+2) | a` | generous (0.14), permitted (0.43) | eligible (1) |
| withdrawal | `MOVE(=0) JOIN(=-3) FIGHT(=+2) | o PI MOOD(=-2) RULE(=+3) | o` | strike (0.07), retreat (0.49) | withdrawal (1) |
| social | `RULE(=-2) MOOD(=0) ART(=-1) | a` | informal (0.27), informal (0.27) | social (1) |
| cafe | `NEAR(=+2) CONSUME(=+3) ABSTRACT(=-2) | o` | food (0.27), food (0.27) | cafe (1) |
| altogether | `MANY(=0) JOIN(=0) TONE(=0) | e` | normally (0.23), alone (0.28) | altogether (1) |
| hang | `LONG(=-1) MOVE(=-3) JOIN(=+3) | i` | stick (0.29), sew (0.20) | hang (1) |
| format | `TEXT PART(=0) FIGHT(=-2) | i` | to write (0.16), edit (0.33) | format (1) |
| enrollment | `MEASURE(=+1) BEGIN(=-1) GIVE(=+3) | o` | deposit (0.24), deposit (0.24) | enrollment (1) |
| nomination | `THINK(=+3) RULE(=+3) MANY(=+4) | o PI GIVE(=+2) FIGHT(=-2) | o` | council (0.24), council (0.24) | election (2) |
| outbreak | `HAPPEN(=0) THING(=+3) FIGHT(=+3) | o` | battle (0.24), battle (0.24) | outbreak (1) |
| critically | `CARE(=+2) TONE(=-4) SOMEONE(=-2) | e` | rudely (0.22), coldly (0.25) | critically (1) |
| normal | `SAME(=+2) MEASURE(=+3) FEEL(=-2) | a` | steady (0.24), similar (0.22) | normal (1) |
| specify | `THINK(=+2) MEASURE(=-2) SAME(=0) | i` | estimate (0.23), estimate (0.23) | specify (1) |
| implement | `DO(=+1) CHANGE(=+2) THINK(=+4) | i` | decide (0.21), solve (0.24) | implement (1) |
| immune | `BODY LIVE(=+4) WANT(=-4) | a` | healthy (0.24), sick (0.20) | immune (1) |
| create | `JOIN(=+1) CHANGE(=+2) DO(=-2) | i` | collect (0.21), mix (0.22) | create (1) |
| dramatic | `MOOD(=-1) HAPPEN(=+2) BIG(=+1) | a` | unfortunate (0.17), serious (0.26) | dramatic (1) |
| painful | `MOOD(=-1) VALUE(=+3) CAN(=-2) | a` | unaffordable (0.22), unaffordable (0.22) | painful (1) |
| bomber | `FIGHT(=+3) GRAIN(=0) LONG(=+1) | o PI NEAR(=+1) PLACE | o` | trench (0.21), trench (0.21) | aircraft (2) |
| internationally | `MANY(=+3) BIG(=+5) FIGHT(=-5) | e` | greatly (0.21), greatly (0.21) | internationally (1) |
| elaborate | `CARE(=+1) SAME(=-3) ABSTRACT(=0) | a` | particular (0.21), particular (0.21) | elaborate (1) |
| intelligent | `MOOD(=+2) CAN(=+5) ART(=-4) | a` | convenient (0.19), cheerful (0.23) | intelligent (1) |
| adult | `LIVE(=+2) SEX(=-1) SAME(=-1) | o PI BIG(=-3) FIGHT(=-5) | o` | hen (0.18), woman (0.24) | adult (1) |
| handful | `MANY(=-1) BIG(=-1) PART(=0) | o` | crumbs (0.28), fragment (0.12) | handful (1) |
| preliminary | `BEGIN(=0) RULE(=+1) ABSTRACT(=0) | a` | ongoing (0.19), ongoing (0.19) | preliminary (1) |
| installation | `ART(=-1) BEGIN(=-1) ABSTRACT(=-4) | o` | ignition (0.19), starter (0.20) | installation (1) |
| ten | `MEASURE(=-1) TIME(=-3) MANY(=0) | a` | old (0.18), old (0.18) | ten (1) |
| mosque | `PLACE NEAR(=+3) ABSTRACT(=-3) | o PI SEX(=+2) RULE(=+3) | o` | barracks (0.21), court (0.15) | palace (2) |
| corporate | `RULE(=0) PART(=+3) DO(=-2) | a` | collective (0.26), participating (0.10) | corporate (1) |
| city | `PLACE NEAR(=+2) RULE(=+3) | o` | office (0.18), office (0.18) | courthouse (4) |
| associate | `JOIN(=+2) DO(=-2) KNOW(=+1) | i` | combine (0.20), assemble (0.14) | associate (1) |
| wide | `BIG(=+3) CAN(=+3) SIDE(=0) | a` | strong (0.16), powerful (0.17) | wide (1) |
| southeastern | `NEAR(=+1) SIDE(=+1) BIG(=0) | a` | near (0.18), nearby (0.15) | southeastern (1) |
| sanctuary | `PLACE INSIDE(=0) NEAR(=0) | o PI ART(=+4) TONE(=+5) | o` | salon (0.20), theatre (0.12) | sanctuary (1) |
| submarine | `GRAIN(=-2) FIGHT(=+3) DO(=+3) | o PI ABOVE(=-2) MOVE(=+3) | o` | bomb (0.24), bullet (0.07) | submarine (1) |
| agenda | `SIDE(=+2) TIME(=+3) RULE(=0) | o` | future (0.16), future (0.16) | agenda (1) |
| elder | `SEX(=0) LIVE(=-1) TIME(=-1) | o` | embryo (-0.02), ancestor (0.33) | age (2) |
| random | `SAME(=-1) KNOW(=-5) CARE(=-3) | a` | careless (0.20), ignorant (0.11) | random (1) |
| current | `CHANGE(=0) TIME(=-1) ABOVE(=-1) | o` | fall (0.08), history (0.22) | current (1) |
| curious | `KNOW(=0) THINK(=-4) MOOD(=+3) | a` | hopeful (0.16), optimistic (0.13) | curious (1) |
| namely | `SAME(=-1) MANY(=0) HAPPEN(=-2) | e` | sometimes (0.15), sometimes (0.15) | namely (1) |
| note | `TEXT BIG(=-2) SEE | i` | skim (0.05), read (0.23) | note (1) |
| realistic | `ABSTRACT(=0) CAN(=+2) MOOD(=0) | a PI FEEL(=+2) CHANGE(=-2) | o` | calm (0.12), steady (0.15) | realistic (1) |
| hat | `LONG(=-4) ABOVE(=+3) JOIN(=+4) | o PI SEE CONSUME(=+3) | o` | eyebrow (0.14), eyebrow (0.14) | cap (2) |
| pump | `GRAIN(=-2) MOVE(=+1) BODY | i` | sweat (0.12), swim (0.15) | pump (1) |
| economy | `VALUE(=-1) ART(=-1) CHANGE(=-1) | o` | money (0.13), money (0.13) | economy (1) |
| danger | `GOOD(=-4) VALUE(=+5) CAN(=-4) | o` | debt (0.13), debt (0.13) | danger (1) |
| telegraph | `TEXT LONG(=0) NEAR(=0) | o` | line (0.13), line (0.13) | telegram (5) |
| negotiate | `THINK(=+3) VALUE(=-3) GIVE(=+2) | i` | undervalue (0.12), undervalue (0.12) | negotiate (1) |
| trade | `VALUE(=-2) GIVE(=0) CONSUME(=-1) | o PI DO(=-1) THINK(=+4) | o` | consumer (0.20), snack (0.02) | trade (1) |
| mix | `PART(=+1) JOIN(=+1) MEASURE(=+1) | i PI HEAT(=+1) MOVE(=-1) | o` | count (0.02), assemble (0.18) | mix (1) |
| zero | `MEASURE(=0) MANY(=-4) KNOW(=-2) | o` | uncertainty (0.12), scarcity (0.04) | zero (1) |
| suit | `SAME(=0) LONG(=-4) THINK(=+4) | o` | thread (0.08), thread (0.08) | suit (1) |
| bet | `THINK(=+1) FIGHT(=-2) MEASURE(=+1) | i` | to compare (0.07), compare (0.07) | bet (1) |
| respect | `WANT(=0) TONE(=+3) SAME(=+1) | o` | friend (0.07), friend (0.07) | respect (1) |
| institute | `KNOW(=0) PART(=+3) PLACE | i` | contain (0.03), map (0.04) | institute (1) |
| palace | `ABSTRACT(=-3) NEAR(=+2) SEX(=+3) | o` | man (-0.04), son (0.07) | palace (1) |
| removal | `JOIN(=-2) CHANGE(=0) CAN(=+1) | o` | adapter (-0.01), crack (0.03) | removal (1) |
| vice | `DO(=0) RULE(=+4) TIME(=-2) | o` | tradition (-0.04), precedent (0.04) | executive (3) |
| recommend | `THINK(=+1) WANT(=-2) CAN(=+2) | i PI SEE CONSUME(=-2) | o` | display (-0.02), show (-0.00) | recommend (1) |
| compound | `INSIDE(=0) PART(=+2) PLACE | i PI GRAIN(=-1) ART(=-3) | o` | install (0.02), fill (-0.04) | compound (1) |
| tank | `GRAIN(=-2) FIGHT(=+3) LONG(=0) | o` | club (-0.03), club (-0.03) | tank (1) |
