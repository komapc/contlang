## dev/base: 200 прочтений (100 слов × декодеры)

- Haiku: cos первого 0.29, лучший из трёх 0.36, близко (cos ≥ 0,5) 30, точно 14
- математика (те же коды): первыми 87/100, cos первого 0.93
- часть речи o: n 90, Haiku cos 0.24, близко 11
- часть речи i: n 50, Haiku cos 0.33, близко 11
- часть речи a: n 40, Haiku cos 0.27, близко 4
- часть речи e: n 20, Haiku cos 0.42, близко 4
- одно слово: n 158, Haiku cos 0.29, близко 22
- пара: n 42, Haiku cos 0.26, близко 8

## Признаки кода и читаемость (корреляция Спирмена с cos первого ответа Haiku)

- наименьшая близость корня к слову: +0.32
- средняя близость корней: +0.35
- близость главного корня: +0.29
- худшее место корня среди ближайших к слову: -0.06
- число корней: -0.04
- корней со слабым уровнем (|v| ≤ 2): +0.09
- cos первого прочтения математики: -0.12
- место у математики: -0.00

## По словам

| слово | код | Haiku первым (cos) | математика |
|---|---|---|---|
| ahead | `SIDE(=+2) TIME(=+1) MOVE(=0) | e` | ahead (1.00), ahead (1.00) | ahead (1) |
| read | `TEXT CONSUME(=+2) KNOW(=+1) | i` | read (1.00), read (1.00) | read (1) |
| roughly | `MEASURE(=+1) CARE(=-1) NEAR(=+1) | e` | roughly (1.00), roughly (1.00) | roughly (1) |
| source | `HAPPEN(=-3) TEXT | o PI NEAR(=+1) GRAIN(=-1) | o` | source (1.00), source (1.00) | source (1) |
| adjust | `CHANGE(=+2) THINK(=+3) MEASURE(=0) | i` | adjust (1.00), adjust (1.00) | adjust (1) |
| change | `CHANGE(=+2) | i` | change (1.00), alter (0.76) | alter (2) |
| invite | `GIVE(=+2) JOIN(=+4) TONE(=+4) | i` | welcome (0.48), invite (1.00) | invite (1) |
| beef | `THING(=+4) CONSUME(=+3) GRAIN(=+3) | o` | chicken (0.61), meat (0.80) | meat (2) |
| social | `RULE(=-2) ART(=0) JOIN(=+2) | a` | informal (0.27), social (1.00) | social (1) |
| follow | `JOIN(=+2) SAME(=+3) TIME(=+5) | i PI BEGIN(=-1) MOVE(=0) | o` | follow (1.00), converge (0.21) | follow (1) |
| mix | `JOIN(=+2) PART(=+1) SAME(=-2) | i PI FEEL(=0) THINK(=-3) | o` | combine (0.58), combine (0.58) | mix (1) |
| electrical | `ART(=-3) HEAT(=+3) LONG(=-1) | a` | electric (0.76), thermal (0.38) | electrical (1) |
| trade | `VALUE(=-2) CHANGE(=+2) DO(=-3) | o` | trader (0.56), trader (0.56) | trade (1) |
| charitable | `GIVE(=+4) RULE(=-3) TONE(=+4) | a` | generous (0.52), generous (0.52) | charitable (1) |
| magnitude | `MEASURE(=0) BIG(=+2) HAPPEN(=+1) | o` | scale (0.51), scale (0.51) | magnitude (1) |
| cafe | `ABSTRACT(=-2) CONSUME(=+5) NEAR(=+4) | o PI VALUE(=-2) PLACE | o` | cafeteria (0.65), snack (0.34) | cafe (1) |
| normal | `SAME(=0) MEASURE(=+2) FEEL(=-2) | a` | average (0.47), average (0.47) | normal (1) |
| nomination | `RULE(=+3) FIGHT(=-3) GIVE(=+2) | o` | prize (0.40), award (0.53) | nomination (1) |
| house | `ABSTRACT(=-3) INSIDE(=+2) PLACE | o` | room (0.46), room (0.46) | room (3) |
| firmly | `TONE(=0) CARE(=+2) CHANGE(=-4) | e` | steadily (0.44), steadily (0.44) | firmly (1) |
| painful | `MOOD(=-1) VALUE(=+1) TOUCH(=+3) | a` | bitter (0.43), bitter (0.43) | painful (1) |
| please | `SOMEONE(=+1) TONE(=+5) GIVE(=+1) | i` | thank (0.41), thank (0.41) | please (1) |
| recommend | `THINK(=+1) WANT(=-2) TONE(=+3) | i PI RULE(=+2) PART(=+3) | o` | advise (0.70), salute (0.13) | recommend (1) |
| agenda | `RULE(=+1) TIME(=+3) PART(=+2) | o PI ABSTRACT(=+3) ART(=+2) | o` | syllabus (0.41), syllabus (0.41) | agenda (1) |
| virtually | `MANY(=0) CARE(=-1) NEAR(=+1) | e` | roughly (0.40), roughly (0.40) | virtually (1) |
| fee | `MEASURE(=+2) GIVE(=+5) VALUE(=-1) | o` | discount (0.39), discount (0.39) | fee (1) |
| realistic | `CAN(=+2) ABSTRACT(=+1) TOUCH(=+1) | a` | practical (0.48), conceivable (0.28) | realistic (1) |
| satellite | `PLACE ART(=-4) NEAR(=-3) | o` | observatory (0.37), observatory (0.37) | satellite (1) |
| removal | `JOIN(=-5) DO(=+1) HAPPEN(=0) | o` | separation (0.35), separation (0.35) | removal (1) |
| enrollment | `MEASURE(=+2) BEGIN(=-2) GIVE(=+4) | o PI ART(=0) PART(=+5) | o` | grant (0.16), admission (0.54) | enrollment (1) |
| breakfast | `ABSTRACT(=-3) CONSUME(=+5) FEEL(=-3) | o` | food (0.32), food (0.32) | breakfast (1) |
| supermarket | `NEAR(=+3) VALUE(=-5) CONSUME(=+4) | o` | snack (0.27), food (0.36) | grocery (2) |
| critically | `TONE(=-1) CARE(=+3) LIVE(=0) | e` | cautiously (0.31), cautiously (0.31) | critically (1) |
| altogether | `MANY(=0) TONE(=0) JOIN(=-2) | e` | apart (0.34), separately (0.27) | altogether (1) |
| discount | `VALUE(=-2) GIVE(=+2) MEASURE(=+1) | i PI ABOVE(=-1) RULE(=+3) | o` | underpay (0.29), tax (0.30) | discount (1) |
| announcement | `TIME(=+1) RULE(=+2) TEXT | o` | contract (0.15), notice (0.44) | announcement (1) |
| nevertheless | `MANY(=-1) TONE(=+1) TIME(=+1) | e` | soon (0.26), seldom (0.32) | nevertheless (1) |
| respect | `WANT(=+1) TONE(=+3) RULE(=+2) | o` | etiquette (0.29), etiquette (0.29) | respect (1) |
| maintain | `CHANGE(=-3) THINK(=+4) GIVE(=0) | i` | settle (0.19), insist (0.36) | maintain (1) |
| implement | `DO(=+3) THINK(=+4) CHANGE(=+1) | i` | determine (0.25), resolve (0.29) | implement (1) |
| hang | `LONG(=-1) MOVE(=-3) GIVE(=-2) | i` | pull (0.35), draw (0.18) | hang (1) |
| intelligent | `KNOW(=0) CAN(=+5) MOOD(=+3) | a` | confident (0.26), confident (0.26) | intelligent (1) |
| dramatic | `BIG(=+1) HAPPEN(=+3) MOOD(=-1) | a` | consequential (0.32), important (0.20) | dramatic (1) |
| adult | `SEX(=-1) RULE(=-2) BIG(=-1) | o` | girl (0.24), girl (0.24) | adult (1) |
| random | `RULE(=-2) KNOW(=-5) CARE(=-4) | a` | careless (0.20), thoughtless (0.26) | random (1) |
| account | `TEXT RULE(=-1) MEASURE(=+3) | o` | note (0.29), memo (0.17) | account (1) |
| outbreak | `HAPPEN(=+1) FIGHT(=+2) HEAT(=+1) | o` | quarrel (0.22), battle (0.24) | outbreak (1) |
| dinner | `CONSUME(=+5) ABSTRACT(=-5) CARE(=-5) | o` | junk food (0.19), fast food (0.27) | dinner (1) |
| specify | `THINK(=+2) MEASURE(=-2) SAME(=-1) | i` | estimate (0.23), estimate (0.23) | specify (1) |
| curious | `THINK(=-2) FEEL(=+1) MOOD(=+3) | a` | playful (0.29), hopeful (0.16) | curious (1) |
| municipality | `RULE(=+2) PLACE NEAR(=+2) | o PI THING(=-1) GRAIN(=-4) | o` | port (0.26), airport (0.19) | reservoir (3) |
| create | `JOIN(=+1) THINK(=+3) LIVE(=+4) | i` | settle (0.20), connect (0.25) | create (1) |
| sentence | `TEXT RULE(=+5) BEGIN(=+1) | o` | constitution (0.15), statute (0.28) | sentence (1) |
| drive | `MOVE(=+3) LONG(=+3) INSIDE(=-1) | i` | thrust (0.21), thrust (0.21) | drive (1) |
| assistant | `DO(=-2) SEX(=+1) RULE(=+1) | o` | man (0.08), agent (0.32) | deputy (20) |
| massive | `BIG(=+2) GRAIN(=+1) | a` | dense (0.34), coarse (0.05) | massive (1) |
| vice | `TIME(=-1) RULE(=+5) DO(=-4) | o` | ruler (0.18), official (0.21) | deputy (7) |
| associate | `DO(=-3) JOIN(=+5) TIME(=-3) | i` | combine (0.20), unite (0.18) | associate (1) |
| submarine | `FIGHT(=+3) ABOVE(=-5) ART(=-4) | o` | bomb (0.24), mine (0.13) | submarine (1) |
| adjacent | `NEAR(=+3) PLACE SIDE(=0) | a` | local (0.19), local (0.19) | adjacent (1) |
| namely | `SAME(=-1) MANY(=0) HAPPEN(=-2) | e` | rarely (0.11), otherwise (0.24) | namely (1) |
| sanctuary | `PLACE INSIDE(=-1) THING(=+2) | o PI NEAR(=+3) VALUE(=+3) | o` | pet shop (0.19), garden (0.16) | sanctuary (1) |
| southeastern | `PLACE SIDE(=+1) BIG(=0) | a PI HEAT(=-2) FIGHT(=+5) | o` | frontline (0.08), adjacent (0.26) | southeastern (1) |
| withdrawal | `JOIN(=-5) MOOD(=-3) GIVE(=+3) | o` | farewell (0.16), farewell (0.16) | withdrawal (1) |
| preliminary | `BEGIN(=0) RULE(=+1) | a` | current (0.13), ongoing (0.19) | preliminary (1) |
| sometime | `TIME(=+1) SOMEONE(=+2) CARE(=-2) | e` | hastily (0.15), hastily (0.15) | sometime (1) |
| wide | `BIG(=+3) ABOVE(=0) CAN(=+4) | a` | capable (0.12), powerful (0.17) | wide (1) |
| installation | `ART(=-2) BEGIN(=-1) ABSTRACT(=-4) | o` | engine (0.09), starter (0.20) | installation (1) |
| repair | `ART(=-2) THINK(=+5) JOIN(=-3) | i PI CHANGE(=+2) NEAR(=+5) | o` | calculate (0.14), calculate (0.14) | repair (1) |
| bet | `FIGHT(=-1) THINK(=0) MEASURE(=+2) | i` | compete (0.20), compare (0.07) | bet (1) |
| eligible | `CAN(=+2) GIVE(=+4) FIGHT(=-3) | a` | generous (0.14), generous (0.14) | eligible (1) |
| mosque | `ABSTRACT(=-1) NEAR(=+5) PLACE | o PI SEX(=+2) BIG(=+5) | o` | lap (0.06), neighborhood (0.21) | mosque (1) |
| economy | `ART(=-1) MEASURE(=+4) FEEL(=-4) | o` | tempo (0.08), pace (0.18) | economy (1) |
| corporate | `RULE(=0) PART(=+3) ART(=-2) | a` | mechanical (0.05), standard (0.20) | corporate (1) |
| current | `CHANGE(=0) TIME(=-1) ABOVE(=-1) | o` | decline (0.12), decline (0.12) | current (1) |
| harassment | `RULE(=0) FIGHT(=+2) SAY(=+3) | o` | quarrel (0.15), argument (0.07) | harassment (1) |
| elaborate | `BIG(=+1) CARE(=+4) GIVE(=+2) | a PI CAN(=-1) SAME(=-3) | o` | generous (0.11), generous (0.11) | elaborate (1) |
| negotiate | `THINK(=+2) VALUE(=-5) GIVE(=+1) | i` | undervalue (0.12), underestimate (0.08) | negotiate (1) |
| pump | `GRAIN(=-2) ART(=-2) ABOVE(=0) | i` | grind (0.10), grind (0.10) | pump (1) |
| internationally | `TONE(=-1) MANY(=+5) FIGHT(=-5) | e` | playfully (0.10), jokingly (0.07) | internationally (1) |
| ten | `TIME(=-2) BEGIN(=+2) MEASURE(=+1) | a` | early (0.08), former (0.08) | last (6) |
| telegraph | `TEXT LONG(=-1) ART(=-4) | o PI RULE(=+2) SEX(=-1) | o` | code (0.12), formula (0.04) | telegraph (1) |
| hat | `LONG(=-2) HEAT(=-3) THING(=+3) | o PI BODY SIDE(=+1) | o` | fin (0.08), fin (0.08) | foot (2) |
| elder | `SEX(=0) RULE(=+1) | o` | gender (0.08), gender (0.08) | elder (1) |
| compound | `PART(=+1) NEAR(=+4) MEASURE(=+3) | i` | estimate (0.03), approach (0.12) | compound (1) |
| suit | `SAME(=0) THINK(=+3) RULE(=+3) | o PI LONG(=-5) CONSUME(=+2) | o` | recipe (0.07), doctrine (0.07) | suit (1) |
| bomber | `FIGHT(=+3) GRAIN(=-3) LONG(=+3) | o` | gun (0.13), sword (-0.01) | aircraft (4) |
| danger | `KNOW(=0) VALUE(=+4) HAPPEN(=+3) | o` | lesson (0.05), lesson (0.05) | danger (1) |
| note | `TEXT SEE BIG(=-2) | i` | skim (0.05), skim (0.05) | note (1) |
| zero | `MANY(=-3) MEASURE(=+1) ABOVE(=-1) | o` | shortage (0.06), minority (0.04) | zero (1) |
| forecast | `MEASURE(=+2) TIME(=+4) HEAT(=-2) | i` | cool (0.05), cool (0.05) | forecast (1) |
| format | `TEXT MEASURE(=-2) FIGHT(=-2) | i` | argue (0.06), spell (0.04) | format (1) |
| suburb | `PLACE NEAR(=+2) | o PI HEAT(=0) DO(=-4) | o` | hearth (0.04), hearth (0.04) | neighborhood (4) |
| immune | `HAPPEN(=+1) THING(=+5) HEAT(=-3) | a` | cool (0.05), wild (0.04) | immune (1) |
| city | `PLACE NEAR(=+1) RULE(=+3) | o PI HEAT(=0) DO(=-4) | o` | kitchen (0.00), embassy (0.07) | chicago (2) |
| palace | `ABSTRACT(=-3) NEAR(=+3) INSIDE(=+2) | o PI SEX(=+1) MOVE(=-5) | o` | core (0.05), organ (0.02) | palace (1) |
| vehicle | `LONG(=+4) ART(=-2) THING(=+1) | o` | pipe (-0.01), beam (0.07) | vehicle (1) |
| handful | `BIG(=-1) PART(=+2) GIVE(=-2) | o` | tax (-0.11), portion (0.17) | handful (1) |
| tank | `GRAIN(=-2) FIGHT(=+3) LONG(=+3) | o PI ABSTRACT(=-2) CONSUME(=+3) | o` | fang (-0.04), spear (0.08) | bottle (2) |
| institute | `ART(=-1) PART(=+5) GIVE(=+3) | i` | distribute (-0.01), distribute (-0.01) | institute (1) |
