## dev/g: 200 прочтений (100 слов × декодеры)

- Haiku: cos первого 0.26, лучший из трёх 0.35, близко (cos ≥ 0,5) 22, точно 10
- математика (те же коды): первыми 85/100, cos первого 0.92
- часть речи o: n 90, Haiku cos 0.23, близко 6
- часть речи i: n 50, Haiku cos 0.30, близко 8
- часть речи a: n 40, Haiku cos 0.26, близко 5
- часть речи e: n 20, Haiku cos 0.30, близко 3
- одно слово: n 158, Haiku cos 0.28, близко 19
- пара: n 42, Haiku cos 0.21, близко 3

## Признаки кода и читаемость (корреляция Спирмена с cos первого ответа Haiku)

- наименьшая близость корня к слову: +0.18
- средняя близость корней: +0.15
- близость главного корня: +0.22
- худшее место корня среди ближайших к слову: -0.08
- число корней: -0.03
- корней со слабым уровнем (|v| ≤ 2): -0.07
- cos первого прочтения математики: -0.16
- место у математики: +0.04

## По словам

| слово | код | Haiku первым (cos) | математика |
|---|---|---|---|
| adjacent | `NEAR(=+3) JOIN(=+1) SIDE(=-1) | a` | adjacent (1.00), adjacent (1.00) | adjacent (1) |
| discount | `VALUE(=-2) GIVE(=+2) MEASURE(=+1) | i` | discount (1.00), discount (1.00) | pay (3) |
| read | `TEXT KNOW(=+1) CONSUME(=0) | i` | read (1.00), read (1.00) | read (1) |
| invite | `GIVE(=+1) JOIN(=+3) TONE(=+4) | i` | welcome (0.48), invite (1.00) | invite (1) |
| firmly | `CARE(=0) CHANGE(=-3) TOUCH(=+1) | e` | firmly (1.00), steadily (0.44) | firmly (1) |
| social | `RULE(=-2) JOIN(=+2) ART(=0) | a` | social (1.00), informal (0.27) | social (1) |
| mix | `PART(=0) JOIN(=+2) SAME(=-1) | i PI FEEL(=0) HAPPEN(=0) | o` | blend in experience (0.49), mingle (0.72) | mix (1) |
| drive | `MOVE(=+3) DO(=+2) NEAR(=+1) | i` | approach (0.14), drive (1.00) | drive (1) |
| ahead | `SIDE(=+2) TIME(=+1) MOVE(=0) | e` | forward (0.56), forward (0.56) | ahead (1) |
| beef | `THING(=+3) CONSUME(=+5) GRAIN(=+3) | o` | carnivore (0.32), meat (0.80) | meat (2) |
| trade | `VALUE(=-3) CHANGE(=+2) DO(=-1) | o` | trader (0.56), trader (0.56) | trade (1) |
| agenda | `RULE(=+1) TIME(=+3) ABSTRACT(=+1) | o` | plan (0.48), plan (0.48) | agenda (1) |
| breakfast | `CONSUME(=+4) FEEL(=-4) ABSTRACT(=-3) | o` | food (0.32), meal (0.61) | breakfast (1) |
| house | `ABSTRACT(=-3) INSIDE(=+1) PLACE | o` | room (0.46), room (0.46) | residence (2) |
| dinner | `CONSUME(=+3) ABSTRACT(=-3) PART(=+3) | o` | food (0.45), food (0.45) | dinner (1) |
| implement | `THINK(=+4) DO(=+3) BEGIN(=-3) | i` | initiate (0.42), initiate (0.42) | implement (1) |
| cafe | `NEAR(=+2) CONSUME(=+4) ABSTRACT(=-3) | o PI VALUE(=-2) PLACE | o` | street food (0.30), canteen (0.52) | cafe (1) |
| charitable | `GIVE(=+4) RULE(=-3) TONE(=+4) | a` | hospitable (0.30), generous (0.52) | charitable (1) |
| harassment | `RULE(=0) GOOD(=-4) FEEL(=0) | o` | complaint (0.43), grievance (0.38) | harassment (1) |
| nomination | `RULE(=+3) GIVE(=+2) FIGHT(=-2) | o` | prize (0.40), prize (0.40) | nomination (1) |
| electrical | `ART(=-3) HEAT(=+3) LONG(=0) | a` | thermal (0.38), thermal (0.38) | electrical (1) |
| respect | `WANT(=0) KNOW(=+3) TONE(=+3) | o PI THINK(=0) SAME(=0) | o` | manners (0.37), manners (0.37) | respect (1) |
| maintain | `CHANGE(=-3) THINK(=+3) GIVE(=0) | i PI MOVE(=-3) ABOVE(=+4) | o` | keep (0.69), trade (0.03) | maintain (1) |
| wide | `BIG(=+3) CAN(=+3) SIDE(=0) | a` | spacious (0.53), powerful (0.17) | wide (1) |
| suburb | `PLACE NEAR(=+4) VALUE(=-3) | o` | store (0.13), neighborhood (0.57) | mall (2) |
| announcement | `TIME(=+1) RULE(=+2) TEXT | o` | schedule (0.25), notice (0.44) | announcement (1) |
| adjust | `CHANGE(=+2) THINK(=+2) MEASURE(=0) | i` | recalculate (0.44), estimate (0.21) | adjust (1) |
| critically | `TONE(=-2) CARE(=+3) VALUE(=+3) | e` | carefully (0.33), cautiously (0.31) | critically (1) |
| pump | `GRAIN(=-2) CONSUME(=-2) ABOVE(=0) | i PI LONG(=+3) MOVE(=+4) | o` | leak (0.37), pour (0.27) | drip (3) |
| realistic | `CAN(=+2) ABSTRACT(=+2) TOUCH(=+1) | a` | conceivable (0.28), possible (0.35) | realistic (1) |
| nevertheless | `MANY(=-1) TONE(=+1) TIME(=0) | e` | rarely (0.31), rarely (0.31) | nevertheless (1) |
| internationally | `MANY(=+4) NEAR(=-3) TONE(=-1) | e` | mostly (0.14), widely (0.46) | internationally (1) |
| please | `TONE(=+4) WANT(=+3) MOVE(=-1) | i` | caress (0.14), welcome (0.46) | please (1) |
| assistant | `DO(=-2) RULE(=+1) | o PI SOMEONE(=+1) JOIN(=+2) | o` | official (0.29), official (0.29) | member (25) |
| city | `PLACE NEAR(=+3) RULE(=+3) | o` | town hall (0.38), office (0.18) | courthouse (6) |
| sentence | `RULE(=+5) BEGIN(=+2) TEXT | o` | statute (0.28), statute (0.28) | sentence (1) |
| intelligent | `CAN(=+3) MOOD(=+3) ART(=-3) | a` | playful (0.32), cheerful (0.23) | intelligent (1) |
| supermarket | `NEAR(=+2) VALUE(=-4) CONSUME(=+4) | o` | snack (0.27), snack (0.27) | supermarket (1) |
| vice | `DO(=-1) RULE(=+4) TIME(=-2) | o` | former ruler (0.35), ruler (0.18) | deputy (4) |
| tank | `GRAIN(=-2) FIGHT(=+3) LONG(=+1) | o PI THING(=-1) PLACE | o` | trench (0.25), trench (0.25) | tanker (2) |
| normal | `SAME(=+1) FEEL(=-2) MEASURE(=+2) | a` | moderate (0.25), steady (0.24) | normal (1) |
| municipality | `RULE(=+3) NEAR(=+2) PLACE | o PI GRAIN(=-2) THING(=-1) | o` | harbor office (0.23), port (0.26) | river (2) |
| enrollment | `MEASURE(=+1) BEGIN(=-2) GIVE(=+4) | o` | deposit (0.24), deposit (0.24) | enrollment (1) |
| altogether | `MANY(=0) TONE(=-1) JOIN(=-1) | e` | alone (0.28), individually (0.20) | altogether (1) |
| adult | `LIVE(=+2) SEX(=-3) RULE(=-2) | o` | woman (0.24), woman (0.24) | adult (1) |
| withdrawal | `FIGHT(=+1) JOIN(=-5) GIVE(=+3) | o` | truce (0.21), divorce (0.25) | withdrawal (1) |
| specify | `THINK(=+2) MEASURE(=-2) SAME(=0) | i` | estimate (0.23), estimate (0.23) | specify (1) |
| magnitude | `MEASURE(=-1) BIG(=+2) HAPPEN(=+2) | o` | effect (0.22), effect (0.22) | magnitude (1) |
| fee | `GIVE(=+3) MEASURE(=+2) VALUE(=-1) | o` | tip (0.12), donation (0.32) | fee (1) |
| outbreak | `HAPPEN(=+1) THING(=+3) HEAT(=+1) | o` | offspring (0.02), fever (0.42) | outbreak (1) |
| hang | `MOVE(=-2) LONG(=-2) JOIN(=+2) | i` | weave (0.22), sew (0.20) | hang (1) |
| repair | `THINK(=+4) ART(=-2) SIDE(=-4) | i PI CHANGE(=-2) GIVE(=+4) | o` | refund (0.27), calculate (0.14) | repair (1) |
| account | `MEASURE(=+1) RULE(=-1) TEXT | o` | recipe (0.11), note (0.29) | account (1) |
| massive | `BIG(=+2) | a PI TOUCH(=+2) GOOD(=-3) | o` | severe (0.38), dangerous (0.02) | massive (1) |
| installation | `ART(=-2) BEGIN(=-2) ABSTRACT(=-4) | o` | starter (0.20), ignition (0.19) | installation (1) |
| dramatic | `BIG(=+1) HAPPEN(=+4) ART(=+4) | a` | influential (0.10), artistic (0.27) | dramatic (1) |
| elaborate | `THINK(=+1) CARE(=+3) BIG(=+2) | a` | thoughtful (0.18), thoughtful (0.18) | elaborate (1) |
| economy | `ART(=0) MEASURE(=+5) VALUE(=-2) | o PI ABOVE(=-2) HAPPEN(=+3) | o` | discount (0.09), depreciation (0.27) | economy (1) |
| painful | `MOOD(=-1) GOOD(=-3) BODY | a` | sick (0.18), ill (0.17) | painful (1) |
| random | `SAME(=-1) KNOW(=-5) CARE(=-3) | a` | oblivious (0.14), careless (0.20) | random (1) |
| curious | `THINK(=-2) FEEL(=+2) MOOD(=+3) | a` | hopeful (0.16), hopeful (0.16) | curious (1) |
| associate | `DO(=-2) JOIN(=+4) SAME(=+1) | i` | unite (0.18), assemble (0.14) | associate (1) |
| change | `CHANGE(=+2) | i PI MOVE(=+1) HAPPEN(=+2) | o` | development (0.16), development (0.16) | change (1) |
| roughly | `MEASURE(=+1) CARE(=-1) TIME(=-2) | e` | once (0.19), formerly (0.13) | roughly (1) |
| source | `HAPPEN(=-3) TEXT CONSUME(=-1) | o` | author (0.15), author (0.15) | source (1) |
| sometime | `TIME(=+1) SOMEONE(=+2) CARE(=-2) | e` | hastily (0.15), hastily (0.15) | sometime (1) |
| namely | `MANY(=0) SAME(=-1) HAPPEN(=-2) | e` | sometimes (0.15), sometimes (0.15) | namely (1) |
| note | `TEXT BIG(=-2) SEE | i` | skim (0.05), read (0.23) | note (1) |
| bet | `THINK(=0) FIGHT(=-2) MEASURE(=+2) | i` | compare (0.07), compete (0.20) | bet (1) |
| satellite | `ART(=-3) ABOVE(=+4) SEE | o PI SOMEONE(=-3) INSIDE(=-2) | o` | contact lens (0.08), periscope (0.19) | satellite (1) |
| eligible | `CAN(=+2) GIVE(=+4) FIGHT(=-2) | a` | generous (0.14), generous (0.14) | eligible (1) |
| recommend | `THINK(=0) WANT(=-2) CAN(=+3) | i PI RULE(=+3) GIVE(=+4) | o` | grant (0.07), tolerate (0.20) | recommend (1) |
| ten | `BEGIN(=+2) TIME(=-5) MEASURE(=0) | a` | old (0.18), former (0.08) | forty (2) |
| follow | `MOVE(=0) SAME(=+4) CARE(=+4) | i` | maintain (0.19), preserve (0.05) | follow (1) |
| hat | `LONG(=-3) ABOVE(=+3) DO(=+1) | o` | antenna (0.11), rope (0.13) | hat (1) |
| telegraph | `TEXT LONG(=-1) NEAR(=+1) | o PI RULE(=0) ART(=-4) | o` | note (0.20), formula (0.04) | communication (5) |
| create | `JOIN(=0) THINK(=+3) LIVE(=+4) | i` | survive (0.13), believe (0.09) | create (1) |
| danger | `GOOD(=-5) CAN(=-3) VALUE(=+5) | o` | expense (0.11), bankruptcy (0.11) | danger (1) |
| submarine | `LONG(=+2) FIGHT(=+3) GRAIN(=-3) | o PI ABOVE(=-2) GIVE(=-1) | o` | spear (0.10), rifle (0.11) | submarine (1) |
| compound | `INSIDE(=0) PART(=+1) SAME(=0) | i PI GRAIN(=-1) ART(=-3) | o` | contain (0.14), insert (0.05) | compound (1) |
| format | `TEXT PART(=+1) CHANGE(=+1) | i PI MOVE(=0) DO(=+3) | o` | cobble (0.04), revise (0.15) | format (1) |
| corporate | `RULE(=-1) PART(=+4) ART(=-3) | a` | technical (0.21), homemade (-0.02) | corporate (1) |
| sanctuary | `PLACE INSIDE(=0) VALUE(=+3) | o` | bank (0.09), bank (0.09) | sanctuary (1) |
| immune | `LIVE(=+2) HAPPEN(=+1) WANT(=-4) | a` | stubborn (0.11), reluctant (0.07) | immune (1) |
| negotiate | `THINK(=+2) VALUE(=-5) CAN(=-1) | i` | dismiss (0.09), dismiss (0.09) | negotiate (1) |
| preliminary | `BEGIN(=0) CARE(=+2) RULE(=+1) | a` | regular (0.08), consistent (0.09) | preliminary (1) |
| virtually | `MANY(=0) CARE(=-1) | e` | carelessly (0.08), carelessly (0.08) | simply (33) |
| elder | `SEX(=0) LIVE(=0) RULE(=+1) | o` | person (0.08), person (0.08) | elder (1) |
| palace | `ABSTRACT(=-3) NEAR(=+2) INSIDE(=+1) | o PI RULE(=+1) SEX(=+2) | o` | testicle (0.01), heart (0.13) | palace (1) |
| current | `CHANGE(=0) SAME(=+1) TIME(=-1) | o` | news (0.14), habit (-0.00) | current (1) |
| removal | `JOIN(=-3) HAPPEN(=0) RULE(=+4) | o PI GIVE(=0) CAN(=+4) | o` | bank branch (0.01), tariff (0.12) | removal (1) |
| forecast | `MEASURE(=+2) TIME(=+4) HEAT(=-1) | i` | cool (0.05), cool (0.05) | forecast (1) |
| mosque | `NEAR(=+2) WANT(=-2) ABSTRACT(=-1) | o` | neighbor (0.09), enemy (0.00) | mosque (1) |
| zero | `MEASURE(=0) MANY(=-4) ABOVE(=0) | o` | scarcity (0.04), scarcity (0.04) | zero (1) |
| institute | `ART(=-1) PART(=+5) PLACE | i` | assemble (0.04), assemble (0.04) | institute (1) |
| suit | `SAME(=0) LONG(=-3) THINK(=+3) | o` | thread (0.08), thought (-0.01) | suit (1) |
| vehicle | `LONG(=+3) DO(=+3) MOVE(=+4) | o` | oar (0.06), bat (-0.02) | car (2) |
| southeastern | `PLACE SIDE(=+1) BIG(=0) | a PI NEAR(=-4) MANY(=+4) | o` | foreign (0.00), foreign (0.00) | eastern (2) |
| bomber | `FIGHT(=+3) LONG(=+2) GRAIN(=0) | o` | club (0.00), club (0.00) | bomber (1) |
| handful | `BIG(=-1) PART(=0) SOMEONE(=-3) | o` | child (-0.02), child (-0.02) | handful (1) |
