## C: изменённые коды

| слово | O: код | → | N: код | → |
|---|---|---|---|---|
| act | `DO RULE(=+3) FRIEND(=0) | o` | duty (1) | `RULE(=+3) MOVE(=+1) FRIEND(=0) | o` | governor (1) |
| acting | `DO KNOW(=-2) RULE(=+2) | i` | violate (0) | `RULE(=+2) KNOW(=-2) GOOD(=+1) | i` | govern (1) |
| activities | `LIVE(=+3) MEASURE(=+2) HAPPEN | o N+3` | births (0) | `LIVE(=+3) LAW(=-3) MEASURE(=+2) | o N+3` | lives (0) |
| agree | `WANT(=-2) JOIN(=+3) THINK(=0) | i` | object (0) | `WANT(=-2) JOIN(=+3) LAW(=+3) | i` | accept (2) |
| align | `JOIN(=+2) THINK(=+4) CHANGE(=+2) | i` | combine (1) | `JOIN(=+2) CHANGE(=+2) SIDE(=0) | i` | merge (1) |
| alleged | `THINK(=+2) TIME(=-5) MANY(=-5) | i` | forget (0) | `LAW(=+1) TIME(=-4) MANY(=-4) | i` | repeal (0) |
| alleging | `THINK(=+1) TIME(=-5) RULE(=+3) | i` | recall (0) | `LAW(=+2) TIME(=-5) CARE(=-1) | i` | neglect (0) |
| argue | `THINK(=0) WANT(=-3) FIGHT(=-1) | i` | object (2) | `WANT(=-2) MANY(=-2) FIGHT(=-1) | i` | avoid (0) |
| asking | `THINK(=-1) GIVE(=+4) SOMEONE(=+1) | i` | accuse (1) | `GIVE(=+3) KNOW(=0) SOMEONE(=+1) | i` | tell (1) |
| assume | `THINK(=0) GIVE(=0) MANY(=-1) | i` | discuss (0) | `GIVE(=0) MANY(=-1) KNOW(=0) | i` | trade (0) |
| attracting | `FEEL(=+1) INSIDE(=-3) SAME(=-3) | i` | marvel (0) | `FEEL(=+1) SAME(=-4) MAKE(=+4) | i` | celebrate (0) |
| automaker | `ART(=-4) PART(=+3) TOUCH(=+3) | o` | machinery (1) | `ART(=-3) MAKE(=+2) | o` | machine (1) |
| bombings | `FIGHT(=+5) FRIEND(=-3) HEAT(=+5) | o N+3` | bombs (2) | `FIGHT(=+4) MAKE(=-4) HEAT(=+5) | o N+3` | bombs (2) |
| causing | `HAPPEN FEEL(=0) SIDE(=-1) | i` | recur (0) | `HAPPEN MAKE(=0) FEEL(=+1) | i` | occur (1) |
| certain | `SAME(=-1) MANY(=0) THINK(=+1) | a` | various (0) | `SAME(=-1) MANY(=0) LAW(=+2) | a` | certain (2) |
| certification | `RULE(=+2) GIVE(=+2) BEGIN(=0) | o` | permit (2) | `RULE(=+2) LAW(=+5) GIVE(=+2) | o` | license (2) |
| choose | `THINK(=+3) WANT(=0) SAME(=-3) | i` | wonder (0) | `WANT(=0) CAN(=+4) SAME(=-3) | i` | choose (2) |
| claiming | `GIVE(=+1) MANY(=-5) SOMEONE(=-4) | i` | abandon (0) | `MANY(=-2) LAW(=+4) GIVE(=0) | i` | permit (0) |
| complain | `SAY(=+1) WANT(=-2) THINK(=0) | i` | deny (1) | `SAY(=+1) WANT(=-3) MANY(=-1) | i` | complain (2) |
| compliance | `RULE(=+3) CARE(=+2) DO | o` | administration (1) | `RULE(=+3) CARE(=+2) JOIN(=+2) | o` | contract (1) |
| comprising | `PART(=+2) SAME(=-2) BEGIN(=-1) | i` | divide (0) | `PART(=+2) MAKE(=+2) SAME(=-2) | i` | assemble (1) |
| confused | `FEEL(=0) THINK(=-1) KNOW(=-1) | i` | suspect (0) | `FEEL(=0) KNOW(=-1) SAME(=-1) | i` | doubt (1) |
| consensus | `RULE(=+4) BEGIN(=+3) PART(=+3) | o` | office (0) | `PUBLIC(=+2) RULE(=+5) BEGIN(=+3) | o` | term (0) |
| considers | `THINK(=0) WANT(=-2) SEE | i` | expect (1) | `WANT(=-2) KNOW(=+3) SEE | i` | review (1) |
| consolidate | `JOIN(=+1) THINK(=+2) GRAIN(=+2) | i` | assemble (2) | `JOIN(=+1) MAKE(=+1) CHANGE(=+1) | i` | combine (2) |
| contains | `PART(=0) INSIDE(=+3) DO | i` | include (2) | `TEXT INSIDE(=+2) PART(=+1) | i` | record (0) |
| continue | `CHANGE(=-2) BEGIN(=-1) DO | i` | continue (2) | `CHANGE(=-1) MOVE(=-2) BEGIN(=-1) | i` | depart (0) |
| controversial | `THINK(=-1) VALUE(=+4) WANT(=-5) | a` | reluctant (0) | `VALUE(=+2) WANT(=-5) SAME(=-4) | a` | rare (0) |
| convinced | `THINK(=0) MANY(=-2) FEEL(=+2) | i` | wonder (0) | `KNOW(=+1) MANY(=-3) FEEL(=+2) | i` | suspect (1) |
| corruption | `RULE(=+4) FRIEND(=-4) CARE(=-3) | o` | tyrant (1) | `RULE(=+4) LAW(=-5) FRIEND(=-3) | o` | tyranny (1) |
| creator | `ART(=+1) WANT(=+1) LIVE(=0) | o agent` | fan (0) | `ART(=+1) MAKE(=+2) LAW(=+2) | o agent` | lawmaker (0) |
| creatures | `THING(=+2) PART(=-1) FRIEND(=-1) | o N+3` | animals (2) | `THING(=+2) MAKE(=+3) FRIEND(=-1) | o N+3` | livestock (2) |
| creditors | `RULE(=+1) CAN(=-2) PART(=+4) | o agent N+3` | committees (0) | `LAW(=+5) CAN(=-4) PART(=+5) | o agent N+3` | lawyers (0) |
| damaged | `JOIN(=-3) VALUE(=+5) GOOD(=-5) | i` | devalue (1) | `MAKE(=-3) VALUE(=+1) SIDE(=-2) | i` | depreciate (1) |
| damaging | `CHANGE(=+1) VALUE(=+5) GOOD(=-5) | i` | ruin (2) | `MAKE(=-2) VALUE(=+2) LAW(=-2) | i` | violate (0) |
| defining | `THINK(=+2) SAME(=-3) LIVE(=+2) | i` | imagine (0) | `SAME(=-2) BEGIN(=+1) LIVE(=+2) | i` | survive (0) |
| democratic | `RULE(=+3) FIGHT(=-2) SIDE(=0) | a` | competitive (0) | `PUBLIC(=+2) RULE(=+4) FIGHT(=-2) | a` | political (2) |
| designed | `CAN(=+3) MANY(=+3) ART(=-2) | i` | produce (2) | `MAKE(=+1) CAN(=+4) MANY(=+3) | i` | multiply (0) |
| detention | `RULE(=+4) CHANGE(=-3) NEAR(=0) | o` | establishment (0) | `RULE(=+3) LAW(=-5) CHANGE(=-3) | o` | ban (1) |
| determining | `THINK(=+1) MEASURE(=0) SAME(=-2) | i` | compare (1) | `MEASURE(=0) SAME(=-3) RULE(=+3) | i` | distinguish (1) |
| develop | `CHANGE(=+1) BEGIN(=-4) JOIN(=+3) | i` | unite (0) | `MAKE(=+3) BEGIN(=-3) CHANGE(=+1) | i` | establish (2) |
| diplomatic | `RULE(=0) FIGHT(=+2) FRIEND(=+2) | a` | competitive (0) | `RULE(=+1) PUBLIC(=-1) FIGHT(=+2) | a` | military (1) |
| dirty | `CARE(=-1) GOOD(=-4) CONSUME(=-3) | a` | sloppy (2) | `GOOD(=-2) LAW(=-5) CONSUME(=-3) | a` | libelous (0) |
| disclosure | `RULE(=+1) KNOW(=+2) TEXT | o` | manual (0) | `PUBLIC(=-2) KNOW(=+2) RULE(=+5) | o` | secret (1) |
| discussed | `THINK(=0) KNOW(=+2) TIME(=-1) | i` | remember (0) | `TIME(=0) KNOW(=+3) SAME(=-1) | i` | recognize (0) |
| disputes | `FIGHT(=0) THINK(=0) RULE(=+1) | i` | argue (2) | `FIGHT(=0) RULE(=+1) HAPPEN | i` | dispute (2) |
| disrupt | `JOIN(=0) CHANGE(=+2) FEEL(=-2) | i` | mix (0) | `MAKE(=-2) CHANGE(=+2) FEEL(=-2) | i` | weaken (1) |
| downtown | `PLACE NEAR(=+3) LIVE(=+2) | a` | local (1) | `PLACE NEAR(=+3) PUBLIC(=+3) | a` | local (1) |
| drafting | `TEXT SIDE(=+2) ART(=0) | i` | write (2) | `TEXT MAKE(=+3) SIDE(=+2) | i` | draft (2) |
| drive | `DO MOVE(=+4) NEAR(=0) | i` | rush (1) | `SIDE(=0) MOVE(=+4) NEAR(=0) | i` | approach (1) |
| elderly | `LIVE(=-1) TIME(=-4) FRIEND(=+4) | a` | elderly (2) | `FRIEND(=+2) LIVE(=-3) PUBLIC(=+5) | a` | social (0) |
| emerge | `HAPPEN TIME(=+4) BEGIN(=-3) | i` | approach (0) | `HAPPEN TIME(=+3) MAKE(=+2) | i` | develop (1) |
| entity | `RULE(=0) PART(=0) LAND(=-1) | o` | region (0) | `PART(=0) RULE(=-1) LAW(=+2) | o` | section (0) |
| establish | `THINK(=+4) BEGIN(=-3) CHANGE(=-2) | i` | resolve (1) | `MAKE(=+2) RULE(=+1) | i` | establish (2) |
| ethical | `RULE(=+1) LIVE(=+3) THINK(=-1) | a` | social (1) | `RULE(=+1) CARE(=+2) LIVE(=+3) | a` | responsible (1) |
| examining | `THINK(=+1) CARE(=+4) SEE | i` | observe (2) | `SEE CARE(=+5) BEGIN(=-1) | i` | observe (2) |
| explicitly | `TEXT SOMEONE(=-4) MANY(=-2) | e` | anonymously (0) | `SOMEONE(=-2) LAW(=+1) TEXT | e` | officially (1) |
| explore | `THINK(=+1) SEE LAND(=0) | i` | survey (2) | `JOIN(=+1) CARE(=+5) SEE | i` | inspect (2) |
| exposed | `KNOW(=0) INSIDE(=-1) ABOVE(=-1) | i` | understand (0) | `KNOW(=0) PUBLIC(=-1) INSIDE(=-1) | i` | realize (0) |
| film | `TEXT ART(=+1) DO | o` | literature (1) | `TEXT ART(=+1) SEE | o` | literature (1) |
| find | `THINK(=+2) NEAR(=+1) SEE | i` | observe (1) | `SEE MAKE(=+2) CAN(=0) | i` | show (1) |
| fixed | `CHANGE(=-2) LONG(=+2) THINK(=+3) | i` | tie (1) | `CHANGE(=-1) LONG(=+2) SAME(=-1) | i` | alter (0) |
| flood | `HEAT(=+2) LAND(=-4) THING(=-1) | o` | sand (0) | `HEAT(=+1) LAND(=-4) MAKE(=-1) | o` | geyser (1) |
| follow | `DO SAME(=+2) TIME(=+4) | i` | repeat (1) | `SAME(=+1) TIME(=+5) CONSUME(=+3) | i` | last (0) |
| gain | `GIVE(=-1) MEASURE(=+2) BEGIN(=0) | i` | rent (0) | `GIVE(=-1) MEASURE(=+2) PUBLIC(=0) | i` | tax (0) |
| gang | `PART(=+3) JOIN(=+2) FRIEND(=-1) | o` | coalition (1) | `PART(=+3) LAW(=-2) FRIEND(=0) | o` | gang (2) |
| generated | `DO MEASURE(=+3) CONSUME(=-5) | i` | report (0) | `MAKE(=+3) MEASURE(=+2) HEAT(=+3) | i` | heat (0) |
| governed | `RULE(=+3) LAND(=0) CHANGE(=0) | i` | settle (0) | `RULE(=+3) LAW(=+1) MANY(=+2) | i` | regulate (2) |
| governmental | `RULE(=+1) | a` | formal (0) | `RULE(=+1) PUBLIC(=+2) | a` | official (2) |
| grew | `ABOVE(=+2) BEGIN(=-4) CONSUME(=+2) | i` | eat (0) | `ABOVE(=+1) MAKE(=+4) CONSUME(=+1) | i` | feed (0) |
| grown | `BIG(=0) ABOVE(=+4) TOUCH(=-1) | i` | lift (0) | `BIG(=0) ABOVE(=+4) MAKE(=+4) | i` | build (0) |
| handled | `CARE(=+1) THINK(=+5) HAPPEN | i` | arrange (1) | `CARE(=+2) GIVE(=-2) HAPPEN | i` | undergo (0) |
| heated | `HEAT(=+1) FEEL(=+1) RULE(=0) | i` | warm (2) | `HEAT(=+1) FEEL(=+1) PUBLIC(=+1) | i` | protest (1) |
| heir | `TIME(=+2) LIVE(=-5) RULE(=+4) | o agent` | heir (2) | `TIME(=+2) LIVE(=-4) LAW(=+5) | o agent` | heir (2) |
| hide | `INSIDE(=0) JOIN(=-2) SAY(=-3) | i` | mutter (0) | `PUBLIC(=-2) JOIN(=-2) SAY(=-1) | i` | confide (0) |
| hire | `GIVE(=+1) THINK(=+2) VALUE(=-3) | i` | discount (0) | `GIVE(=+1) MAKE(=+1) VALUE(=-3) | i` | sell (0) |
| identified | `SAME(=-2) THINK(=+3) KNOW(=+1) | i` | distinguish (1) | `SAME(=-2) KNOW(=+2) LIVE(=-1) | i` | recall (0) |
| identities | `RULE(=0) INSIDE(=+3) WANT(=+4) | o N+3` | desires (0) | `PUBLIC(=-1) WANT(=+4) ART(=+1) | o N+3` | hobbies (0) |
| implemented | `DO CARE(=+2) ART(=-3) | i` | build (1) | `CHANGE(=+2) MAKE(=+4) CARE(=+4) | i` | improve (1) |
| inform | `KNOW(=+2) THINK(=+3) GIVE(=+3) | i` | advise (2) | `KNOW(=+2) GIVE(=+3) JOIN(=0) | i` | teach (1) |
| information | `TEXT KNOW(=+3) RULE(=0) | o` | manual (1) | `TEXT KNOW(=+2) PUBLIC(=0) | o` | bulletin (1) |
| instrument | `ART(=-1) LONG(=0) DO | o` | engineering (1) | `ART(=-1) PART(=-1) LONG(=+1) | o` | rod (1) |
| instrumental | `ART(=+1) LIVE(=+2) DO | a` | active (0) | `ART(=+1) LIVE(=+2) BEGIN(=0) | a` | lively (0) |
| intercepted | `GIVE(=-2) BEGIN(=+2) NEAR(=-1) | i` | withdraw (0) | `GIVE(=-3) PUBLIC(=-5) BEGIN(=+3) | i` | withdraw (0) |
| international | `RULE(=+1) BIG(=+4) FIGHT(=-5) | a` | athletic (0) | `PUBLIC(=+3) BIG(=+3) FIGHT(=-5) | a` | popular (0) |
| investigating | `THINK(=0) CARE(=+4) LIVE(=-2) | i` | watch (1) | `KNOW(=+1) CARE(=+5) LIVE(=-3) | i` | monitor (1) |
| investigation | `CARE(=+3) THINK(=-1) RULE(=+2) | o` | inspection (2) | `CARE(=+3) RULE(=+2) SEE | o` | inspection (2) |
| investigative | `RULE(=+1) CARE(=+4) THINK(=0) | a` | conscientious (0) | `RULE(=+1) CARE(=+5) FIGHT(=+2) | a` | strict (0) |
| involves | `DO JOIN(=+2) HAPPEN | i` | participate (1) | `HAPPEN JOIN(=+3) SAME(=-1) | i` | arise (0) |
| jay | `SIDE(=-1) MOOD(=+5) RULE(=-2) | o agent` | comedian (0) | `PUBLIC(=0) MOOD(=+5) SIDE(=-1) | o agent` | comedian (0) |
| joint | `BODY JOIN(=+3) GRAIN(=+1) | o` | skeleton (1) | `BODY JOIN(=+2) PUBLIC(=+3) | o` | organization (0) |
| journalism | `TEXT ART(=+1) FIGHT(=0) | o` | polemic (1) | `TEXT ART(=+1) PUBLIC(=+3) | o` | article (1) |
| judge | `RULE(=+4) THINK(=+1) SEE | i` | inspect (1) | `RULE(=+4) SEE | i` | supervise (1) |
| junk | `VALUE(=-1) PART(=0) LONG(=+2) | o` | rope (0) | `VALUE(=-2) PART(=0) MAKE(=-3) | o` | product (1) |
| justified | `THINK(=-1) CAN(=+4) CARE(=-2) | i` | guess (0) | `LAW(=+2) CAN(=+2) CARE(=-1) | i` | permit (0) |
| justify | `THINK(=+1) WANT(=-1) DO | i` | decline (0) | `WANT(=-1) LAW(=+3) MAKE(=+2) | i` | require (0) |
| legal | `RULE(=+2) | a` | formal (1) | `LAW(=+2) RULE(=+2) SIDE(=+1) | a` | legal (2) |
| legislators | `RULE(=+3) | o agent N+3` | authorities (2) | `RULE(=+4) PUBLIC(=+2) | o agent N+3` | officials (2) |
| likelihood | `MEASURE(=+1) THINK(=-1) HAPPEN | o` | chance (2) | `MEASURE(=+1) HAPPEN TIME(=+2) | o` | chance (2) |
| maintain | `CHANGE(=-3) THINK(=+4) GIVE(=-1) | i` | exchange (0) | `CHANGE(=-2) MAKE(=+2) GIVE(=0) | i` | exchange (0) |
| mandatory | `RULE(=+2) WANT(=0) BEGIN(=-1) | a` | initial (0) | `LAW(=+1) RULE(=+2) VALUE(=+1) | a` | legal (1) |
| meet | `TIME(=+2) JOIN(=+5) THINK(=+4) | i` | plan (0) | `TIME(=+2) JOIN(=+4) SAME(=0) | i` | continue (0) |
| merchants | `VALUE(=-5) ART(=-1) KNOW(=+5) | o agent N+3` | economists (1) | `VALUE(=-4) LAW(=+3) KNOW(=+4) | o agent N+3` | merchants (2) |
| miracle | `HAPPEN THINK(=-2) GOOD(=+2) | o` | chance (1) | `HAPPEN GOOD(=+3) CAN(=-1) | o` | luck (1) |
| movies | `TEXT ART(=+1) DO | o N+3` | writings (1) | `TEXT ART(=+1) SEE | o N+3` | writings (1) |
| municipal | `RULE(=+2) PLACE THING(=+1) | a` | public (2) | `PUBLIC(=+3) RULE(=+2) PLACE | a` | civic (2) |
| napoleon | `FIGHT(=+3) MEASURE(=-5) SIDE(=-4) | o agent` | soldier (1) | `FIGHT(=+3) MEASURE(=-5) ART(=+3) | o agent` | martial artist (1) |
| nationwide | `RULE(=+1) LAND(=+2) BIG(=+4) | a` | national (2) | `PUBLIC(=+3) LAND(=+2) BIG(=+3) | a` | extensive (2) |
| nelson | `FIGHT(=-1) SIDE(=-3) THINK(=-2) | o agent` | opponent (1) | `FIGHT(=-1) SIDE(=-3) MOVE(=-2) | o agent` | coward (0) |
| news | `TEXT TIME(=+1) MOOD(=-1) | o` | message (1) | `TEXT TIME(=+1) PUBLIC(=+3) | o` | announcement (2) |
| obscure | `SAME(=-3) SAY(=-4) NEAR(=-2) | i` | lie (0) | `SAME(=-3) PUBLIC(=-2) SAY(=-3) | i` | disagree (0) |
| obtained | `GIVE(=0) CAN(=+2) TIME(=-2) | i` | repay (0) | `GIVE(=0) LAW(=+2) TIME(=-2) | i` | inherit (1) |
| odds | `MEASURE(=+2) FIGHT(=-2) THINK(=-1) | o` | competition (1) | `MEASURE(=+2) FIGHT(=-2) CAN(=-1) | o` | score (1) |
| ordained | `RULE(=+3) LIVE(=-1) SOMEONE(=+2) | i` | govern (0) | `RULE(=+3) LAW(=+3) SOMEONE(=+2) | i` | govern (0) |
| organizing | `PART(=+4) FEEL(=+2) THINK(=+3) | i` | discuss (0) | `PART(=+4) FEEL(=+2) MAKE(=+2) | i` | celebrate (0) |
| parliamentary | `RULE(=+3) INSIDE(=+1) FIGHT(=-1) | a` | civil (1) | `RULE(=+3) PUBLIC(=+2) FIGHT(=-1) | a` | electoral (1) |
| performer | `DO ART(=+2) GOOD(=+2) | o agent` | creator (1) | `ART(=+1) GOOD(=+2) FIGHT(=-2) | o agent` | athlete (1) |
| performs | `DO | i` | do (2) | `HAPPEN CARE(=+2) CONSUME(=-2) | i` | report (0) |
| permits | `GIVE(=+2) RULE(=+4) CAN(=+2) | i` | permit (2) | `LAW(=+1) GIVE(=+2) WANT(=0) | i` | grant (2) |
| placed | `PLACE MOVE(=-3) JOIN(=0) | i` | park (1) | `PLACE MAKE(=+4) ABOVE(=-1) | i` | dig (0) |
| plaintiffs | `RULE(=+3) SOMEONE(=-5) THING(=-2) | o agent N+3` | officials (0) | `LAW(=+5) SOMEONE(=-4) PART(=+2) | o agent N+3` | lawyers (1) |
| politicians | `RULE(=+3) FIGHT(=+1) HAPPEN | o agent N+3` | rebels (1) | `PUBLIC(=+1) RULE(=+5) FIGHT(=+1) | o agent N+3` | politician (2) |
| possibility | `CAN(=+2) THINK(=-3) HAPPEN | o` | chance (2) | `CAN(=+2) HAPPEN WANT(=0) | o` | opportunity (2) |
| posted | `TEXT TIME(=-1) GIVE(=+1) | i` | message (1) | `TEXT TIME(=-1) PUBLIC(=0) | i` | post (2) |
| presidential | `RULE(=+2) FIGHT(=-1) BIG(=+1) | a` | competitive (1) | `RULE(=+3) FIGHT(=-1) PUBLIC(=0) | a` | competitive (1) |
| prison | `INSIDE(=+1) RULE(=+5) FRIEND(=-2) | o` | police (1) | `INSIDE(=+1) LAW(=-5) RULE(=+5) | o` | corruption (0) |
| privilege | `RULE(=+2) GOOD(=+2) WANT(=+1) | o` | right (2) | `LAW(=+2) VALUE(=+3) WANT(=0) | o` | right (2) |
| projects | `ART(=0) GIVE(=+3) SOMEONE(=0) | i` | perform (0) | `ART(=0) MAKE(=+2) SOMEONE(=0) | i` | craft (0) |
| protected | `INSIDE(=-1) CHANGE(=-3) KNOW(=+1) | i` | realize (0) | `INSIDE(=-2) PUBLIC(=-3) CHANGE(=-4) | i` | hide (1) |
| proved | `MANY(=-3) THINK(=+3) GOOD(=+2) | i` | select (0) | `MANY(=-3) CAN(=+1) GOOD(=+2) | i` | save (0) |
| provincial | `RULE(=+2) LAND(=+1) BIG(=-1) | a` | regional (2) | `RULE(=+2) LAND(=0) PUBLIC(=+3) | a` | national (1) |
| qualifying | `FIGHT(=-3) BEGIN(=+1) RULE(=+1) | i` | play (1) | `FIGHT(=-2) BEGIN(=+1) LAW(=+2) | i` | compete (1) |
| question | `THINK(=-1) TEXT | o` | rumor (0) | `TEXT SOMEONE(=+4) KNOW(=+1) | o` | author (0) |
| raising | `ABOVE(=+2) LIVE(=+2) THING(=+2) | i` | grow (2) | `ABOVE(=+2) MAKE(=+2) LIVE(=+1) | i` | raise (2) |
| ratings | `MEASURE(=+1) RULE(=+2) | o N+3` | regulations (0) | `MEASURE(=+1) RULE(=+2) SEE | o N+3` | standards (1) |
| realize | `KNOW(=+1) WANT(=+1) DO | i` | learn (1) | `KNOW(=+1) WANT(=+1) BEGIN(=0) | i` | wonder (0) |
| reflect | `CHANGE(=+1) SEE DO | i` | revise (1) | `CHANGE(=+1) SEE CONSUME(=-1) | i` | show (1) |
| regard | `THINK(=-1) FRIEND(=+2) SEE | i` | respect (2) | `SEE FRIEND(=+2) WANT(=0) | i` | meet (0) |
| requires | `DO WANT(=+1) CAN(=+1) | i` | try (0) | `CAN(=+1) WANT(=+1) GIVE(=+3) | i` | offer (0) |
| reserved | `RULE(=0) MOVE(=-4) FEEL(=-1) | i` | wait (0) | `PUBLIC(=0) MOVE(=-4) LAW(=+2) | i` | stop (0) |
| resolve | `THINK(=+3) CAN(=-2) CHANGE(=-1) | i` | reconsider (1) | `JOIN(=0) CAN(=-2) BEGIN(=+1) | i` | attempt (1) |
| restored | `CHANGE(=0) SIDE(=-5) LIVE(=+1) | i` | revive (2) | `CHANGE(=0) SIDE(=-5) MAKE(=-1) | i` | reverse (1) |
| restoring | `LIVE(=+1) SIDE(=-5) CHANGE(=+1) | i` | revive (2) | `LIVE(=+2) SIDE(=-5) MAKE(=-2) | i` | revive (2) |
| ripped | `JOIN(=-4) LONG(=-5) SAY(=+5) | i` | tear (2) | `MAKE(=-3) LONG(=-3) TOUCH(=+2) | i` | tear (2) |
| ruined | `GOOD(=-2) BEGIN(=+3) JOIN(=-2) | i` | break (1) | `MAKE(=-3) GOOD(=-1) BEGIN(=+2) | i` | spoil (2) |
| sank | `ABOVE(=-3) GIVE(=-1) LAND(=-4) | i` | sink (2) | `ABOVE(=-3) MAKE(=-1) LAND(=-4) | i` | sink (2) |
| searching | `THINK(=0) CARE(=+4) LIVE(=-1) | i` | consider (0) | `SEE CARE(=+5) MOOD(=-3) | i` | worry (0) |
| sect | `PART(=+2) RULE(=+3) PLACE | o` | state (0) | `PART(=+2) RULE(=+4) PUBLIC(=-1) | o` | state (0) |
| sector | `LAND(=0) PART(=+2) MEASURE(=+3) | o` | area (2) | `LAND(=0) MEASURE(=+2) PUBLIC(=+1) | o` | region (1) |
| separate | `JOIN(=-2) RULE(=0) SAME(=-1) | i` | separate (2) | `JOIN(=-2) PUBLIC(=-1) SAME(=-1) | i` | separate (2) |
| setting | `PLACE HEAT(=+3) PART(=+4) | i` | gather (0) | `PLACE HEAT(=+3) MAKE(=+2) | i` | bake (0) |
| shares | `GIVE(=+1) MEASURE(=+2) VALUE(=-2) | i` | discount (0) | `GIVE(=+1) MEASURE(=+2) PUBLIC(=+1) | i` | tax (0) |
| sharing | `FRIEND(=+3) JOIN(=+1) SAME(=+2) | i` | befriend (0) | `PUBLIC(=+1) FRIEND(=+3) JOIN(=+1) | i` | socialize (1) |
| shows | `SEE DO MANY(=-1) | i` | glance (0) | `SEE MANY(=-2) SAME(=-2) | i` | distinguish (0) |
| sin | `WANT(=+1) CARE(=-5) FRIEND(=-5) | o` | greed (1) | `LAW(=-2) CARE(=-4) MOOD(=-4) | o` | crime (1) |
| skeptical | `THINK(=-3) FEEL(=+2) WANT(=-4) | a` | wary (2) | `FEEL(=+1) WANT(=-3) KNOW(=0) | a` | wary (2) |
| societies | `PART(=+3) ART(=+1) FRIEND(=+2) | o N+3` | clubs (2) | `PUBLIC(=+2) PART(=+3) ART(=+1) | o N+3` | exhibitions (0) |
| sound | `SAY(=+1) ART(=0) DO | o` | speech (1) | `SAY(=+1) ART(=0) | o` | speech (1) |
| source | `TEXT CHANGE(=-2) CAN(=+3) | o` | draft (0) | `TEXT PUBLIC(=0) CAN(=+3) | o` | publication (1) |
| step | `SIDE(=0) BEGIN(=-1) DO | o` | start (1) | `SIDE(=0) BEGIN(=-1) PART(=-1) | o` | edge (0) |
| steps | `ABOVE(=0) SIDE(=0) DO | i` | turn (0) | `ABOVE(=0) SIDE(=0) BEGIN(=-1) | i` | float (0) |
| succeed | `CAN(=0) DO BEGIN(=+1) | i` | manage (2) | `CAN(=0) GIVE(=0) BEGIN(=0) | i` | trade (0) |
| sufficient | `CAN(=+1) BIG(=0) RULE(=+3) | a` | possible (1) | `CAN(=+1) LAW(=+3) BIG(=0) | a` | permissible (0) |
| suggestions | `THINK(=-2) GIVE(=+4) TEXT | o N+3` | suggestions (2) | `GIVE(=+3) SOMEONE(=+2) TEXT | o N+3` | letters (0) |
| tackle | `SIDE(=+1) GIVE(=-3) THINK(=+2) | i` | expect (0) | `GIVE(=-1) SIDE(=+2) BODY | i` | carry (0) |
| taxpayer | `MEASURE(=+2) VALUE(=+3) GIVE(=+5) | o agent` | vendor (0) | `PUBLIC(=+2) MEASURE(=+2) GIVE(=+4) | o agent` | donor (1) |
| tears | `MOOD(=-2) SAY(=+1) CONSUME(=-2) | i` | complain (0) | `MOOD(=-2) MAKE(=-3) CONSUME(=-2) | i` | complain (0) |
| test | `THINK(=+2) ART(=-3) FIGHT(=-1) | i` | strategize (0) | `BEGIN(=0) ART(=-3) SEE | i` | calculate (0) |
| theory | `ART(=0) THINK(=-2) RULE(=+1) | o` | question (0) | `ART(=+1) MANY(=-2) RULE(=+2) | o` | professional (0) |
| thoughts | `THINK(=-2) SOMEONE(=+2) KNOW(=+1) | o N+3` | skeptics (0) | `SOMEONE(=+2) KNOW(=+2) MANY(=-3) | o N+3` | specialists (0) |
| troubled | `FEEL(=-1) MOOD(=-3) THINK(=-1) | i` | regret (1) | `FEEL(=-1) MOOD(=-3) TIME(=-1) | i` | regret (1) |
| uncertain | `THINK(=-2) CAN(=-1) CHANGE(=-1) | a` | uncertain (2) | `CHANGE(=-1) CAN(=-4) TIME(=+5) | a` | permanent (0) |
| uncertainty | `THINK(=-2) MOOD(=-2) CHANGE(=-1) | o` | worry (1) | `MEASURE(=+1) MOOD(=-3) TIME(=+4) | o` | worry (1) |
| utilities | `ART(=-3) CAN(=+3) MEASURE(=-1) | o N+3` | devices (1) | `PUBLIC(=+2) ART(=-4) CAN(=+3) | o N+3` | gadgets (1) |
| verify | `THINK(=+3) CARE(=+3) MANY(=-4) | i` | ponder (0) | `SEE LAW(=+4) KNOW(=+1) | i` | judge (1) |
| violating | `RULE(=+3) FRIEND(=-1) JOIN(=-1) | i` | ban (1) | `LAW(=-2) RULE(=+3) MAKE(=-2) | i` | repeal (0) |
| voting | `FIGHT(=-2) RULE(=+5) PART(=+3) | i` | compete (0) | `FIGHT(=-2) RULE(=+5) PUBLIC(=+1) | i` | vote (2) |
| wear | `DO LONG(=-5) CONSUME(=+1) | i` | sew (1) | `CONSUME(=0) LONG(=-5) CHANGE(=0) | i` | weave (1) |
| weighed | `MEASURE(=-1) THINK(=-1) CARE(=+2) | i` | estimate (1) | `MEASURE(=-2) CARE(=+4) WANT(=-3) | i` | restrict (0) |
| wondering | `THINK(=-2) KNOW(=+1) FEEL(=0) | i` | suspect (1) | `KNOW(=+1) SOMEONE(=+2) FEEL(=+1) | i` | understand (1) |

## U: тот же код

| слово | код | old → | new → |
|---|---|---|---|
| academy | `ART(=+1) ABOVE(=+4) FIGHT(=0) | o` | uprising (0) | poster (1) |
| amp | `MEASURE(=-1) ART(=-3) SAY(=+1) | o` | measurement (1) | term (0) |
| arena | `FIGHT(=-1) INSIDE(=-1) PLACE | o` | arena (2) | arena (2) |
| article | `TEXT | o` | text (2) | script (1) |
| backdrop | `SEE INSIDE(=-3) MOVE(=-2) | o` | view (1) | view (1) |
| bargaining | `VALUE(=-2) FIGHT(=-1) RULE(=+2) | i` | bargain (2) | bid (1) |
| basement | `INSIDE(=+1) ABOVE(=-2) PLACE | o` | basement (2) | basement (2) |
| billboard | `TEXT LONG(=+3) ART(=+2) | o` | novel (0) | novel (0) |
| box | `LONG(=+2) INSIDE(=+2) PART(=+1) | o` | pipe (0) | frame (1) |
| button | `LONG(=-1) ABOVE(=-3) MOVE(=+2) | o` | rope (0) | slide (0) |
| cavalry | `FIGHT(=+5) THING(=+3) PART(=+3) | o` | army (2) | army (2) |
| centers | `PLACE NEAR(=+3) SIDE(=0) | o N+3` | neighborhoods (1) | neighborhoods (1) |
| chair | `LONG(=+2) MOVE(=-3) RULE(=+2) | o` | barrier (0) | barrier (0) |
| chairman | `RULE(=+4) TIME(=-2) PART(=+4) | o agent` | veteran (0) | predecessor (1) |
| chapel | `INSIDE(=0) NEAR(=+5) ART(=+4) | o` | frame (0) | studio (1) |
| chief | `RULE(=+3) TIME(=-1) BODY | a` | bodily (0) | physical (0) |
| cigarette | `GRAIN(=-2) HEAT(=+5) CONSUME(=+4) | o` | soup (0) | soup (0) |
| clearing | `GRAIN(=0) JOIN(=-5) LAND(=+4) | i` | dig (0) | dig (0) |
| closest | `NEAR(=+1) FRIEND(=+1) BEGIN(=+1) | a` | close (2) | close (2) |
| content | `TEXT CHANGE(=-1) MEASURE(=-1) | o` | copy (1) | edit (1) |
| coverage | `TEXT INSIDE(=-2) MEASURE(=+1) | o` | caption (1) | footnote (1) |
| cow | `THING(=+3) GRAIN(=+2) | o` | bone (0) | creature (2) |
| cult | `PART(=+3) ART(=+4) LIVE(=-2) | o` | museum (0) | collection (0) |
| deals | `VALUE(=-4) GIVE(=0) FRIEND(=+1) | i` | bargain (2) | trade (2) |
| death | `LIVE(=-2) | o` | sleep (0) | sleep (0) |
| debts | `MEASURE(=+2) GIVE(=+4) CAN(=-2) | o N+3` | rations (0) | payments (1) |
| delivered | `GIVE(=+1) CONSUME(=-2) TIME(=0) | i` | spend (0) | serve (1) |
| descendants | `LIVE(=-1) TIME(=+3) PART(=+2) | o` | mortality (0) | afterlife (0) |
| directly | `SOMEONE(=-1) NEAR(=+1) SIDE(=+1) | e` | nearby (1) | alongside (0) |
| discovery | `BEGIN(=-1) VALUE(=+2) PART(=-2) | o` | deposit (0) | deposit (0) |
| dish | `LONG(=+3) CONSUME(=+3) PART(=-2) | o` | straw (0) | chopstick (1) |
| editorial | `TEXT | o` | text (2) | text (2) |
| ending | `BEGIN(=+1) | i` | end (2) | finish (2) |
| enhancing | `CHANGE(=+2) ABOVE(=+3) LIVE(=+3) | i` | grow (1) | grow (1) |
| enormous | `BIG(=+2) | a` | large (2) | large (2) |
| euros | `VALUE(=0) MEASURE(=+3) GRAIN(=+1) | o N+3` | prices (1) | weights (0) |
| exists | `MANY(=-3) MOVE(=-4) HAPPEN | i` | fail (0) | fail (0) |
| extension | `LONG(=0) BIG(=+3) GIVE(=+4) | o` | channel (0) | pipe (1) |
| finale | `BEGIN(=+2) FIGHT(=-1) | o` | round (2) | finish (2) |
| gilbert | `TEXT FEEL(=+5) THING(=-4) | o` | slogan (0) | poster (0) |
| got | `GIVE(=0) SOMEONE(=+1) TIME(=-2) | i` | repay (0) | repay (0) |
| graduate | `ART(=0) ABOVE(=+4) BEGIN(=+1) | i` | build (0) | launch (0) |
| griffin | `THING(=+3) INSIDE(=-3) GIVE(=-4) | o agent` | predator (2) | predator (2) |
| guards | `INSIDE(=-1) FIGHT(=+4) MOVE(=-3) | o agent N+3` | invaders (1) | soldiers (2) |
| hatch | `INSIDE(=0) LONG(=+3) BEGIN(=-1) | i` | extend (0) | hang (0) |
| header | `TEXT SIDE(=0) FIGHT(=-3) | o` | debate (0) | debate (0) |
| heads | `BODY SIDE(=+1) ABOVE(=0) | o N+3` | faces (1) | faces (1) |
| holidays | `MOOD(=+3) BEGIN(=+3) LAND(=-2) | o N+3` | sailors (0) | holidays (2) |
| including | `SAME(=-1) TIME(=-1) PART(=+4) | i` | mix (0) | repeat (0) |
| island | `LAND(=-2) NEAR(=-2) PLACE | o` | abroad (0) | ocean (1) |
| keeper | `CHANGE(=-3) GIVE(=-3) THING(=+4) | o agent` | predator (0) | predator (0) |
| layer | `PART(=-1) TOUCH(=-3) ABOVE(=0) | o` | fabric (1) | fluff (0) |
| lords | `RULE(=+4) SOMEONE(=+4) FRIEND(=+2) | o agent N+3` | officials (1) | colleagues (0) |
| losers | `FIGHT(=-3) KNOW(=-5) MOOD(=-4) | o agent N+3` | losers (2) | losers (2) |
| managed | `CAN(=0) GIVE(=-1) SOMEONE(=-1) | i` | allow (1) | get (1) |
| marshall | `RULE(=+3) FIGHT(=+4) GOOD(=-1) | o agent` | army (1) | soldier (2) |
| militias | `FIGHT(=+4) PART(=+4) RULE(=+2) | o N+3` | forces (2) | armies (2) |
| monopoly | `VALUE(=-1) FIGHT(=-4) RULE(=+4) | o` | league (1) | tournament (0) |
| mothers | `SEX(=-3) | o agent N+3` | women (2) | women (2) |
| multimedia | `ART(=-1) JOIN(=+3) BIG(=+2) | o` | machine (0) | system (1) |
| navy | `FIGHT(=+4) LAND(=-5) RULE(=+2) | o` | navy (2) | navy (2) |
| number | `MEASURE(=-1) TIME(=-1) SAME(=-2) | o` | period (0) | moment (0) |
| obstacle | `CAN(=-1) THING(=-1) SIDE(=+3) | o` | shield (0) | obstacle (2) |
| organization | `PART(=+4) RULE(=+1) KNOW(=+2) | o` | public (0) | community (1) |
| preliminary | `BEGIN(=-1) CARE(=+2) RULE(=+1) | a` | cautious (0) | preliminary (2) |
| premiered | `BEGIN(=-1) TIME(=-1) GOOD(=+1) | i` | begin (1) | start (1) |
| preparation | `BEGIN(=-1) CARE(=+2) SIDE(=+4) | o` | preparation (2) | priority (0) |
| profession | `RULE(=0) ART(=0) SOMEONE(=+1) | o` | professional (2) | professional (2) |
| projections | `MEASURE(=+3) TIME(=+3) SIDE(=0) | o N+3` | forecasts (2) | forecasts (2) |
| publications | `TEXT TIME(=+1) ART(=0) | o N+3` | notes (1) | news (1) |
| purpose | `BEGIN(=+1) WANT(=+5) RULE(=+1) | o` | demand (0) | desire (1) |
| raw | `TOUCH(=0) FRIEND(=-3) THING(=0) | a` | wild (1) | wild (1) |
| regret | `WANT(=0) MOOD(=-3) TIME(=0) | i` | regret (2) | worry (1) |
| remainder | `BEGIN(=+2) JOIN(=-4) MOVE(=-5) | o` | pause (0) | break (0) |
| request | `GIVE(=+3) WANT(=+2) TEXT | i` | request (2) | apply (2) |
| retail | `VALUE(=-3) NEAR(=+2) PART(=+3) | o` | store (2) | shop (2) |
| rookie | `FIGHT(=-1) BEGIN(=-2) BIG(=-2) | o agent` | beginner (2) | beginner (2) |
| saint | `LIVE(=0) ART(=+5) NEAR(=+4) | o agent` | artist (0) | performer (0) |
| salaries | `MEASURE(=+2) GIVE(=+3) VALUE(=-2) | o N+3` | discounts (1) | fees (1) |
| saving | `VALUE(=+1) LIVE(=+1) MEASURE(=+1) | i` | rate (0) | cost (1) |
| scrutiny | `SEE CARE(=+3) RULE(=+2) | o` | inspection (2) | inspection (2) |
| significantly | `SOMEONE(=-1) MEASURE(=+3) BIG(=+1) | e` | largely (2) | mostly (1) |
| skull | `BODY LIVE(=-1) GRAIN(=+2) | o` | corpse (1) | bone (2) |
| sleeping | `FEEL(=-3) | i` | relax (1) | calm down (0) |
| slowly | `SOMEONE(=-2) SAY(=-5) MOVE(=+3) | e` | quietly (1) | quietly (1) |
| sons | `SEX(=+3) | o agent N+3` | men (1) | men (1) |
| stem | `LONG(=0) JOIN(=-1) SIDE(=+1) | o` | handle (0) | fence (0) |
| strategic | `RULE(=0) FIGHT(=+3) ART(=-2) | a` | military (1) | military (1) |
| teaching | `ART(=+1) KNOW(=+3) RULE(=+1) | i` | teach (2) | teach (2) |
| themes | `SAME(=-1) ART(=+3) TEXT | o N+3` | literature (1) | novels (1) |
| tournaments | `FIGHT(=-2) | o N+3` | contests (2) | games (2) |
| truce | `FIGHT(=+1) FRIEND(=+3) VALUE(=-5) | o` | negotiation (1) | sale (0) |
| truth | `KNOW(=0) MANY(=-3) WANT(=+3) | o` | curiosity (0) | interest (0) |
| type | `SAME(=0) MEASURE(=-4) FRIEND(=+3) | o` | peer (0) | peer (0) |
| ultimate | `BEGIN(=+2) RULE(=0) BIG(=+2) | a` | final (2) | major (0) |
| university | `ART(=0) NEAR(=+2) RULE(=+1) | o` | design (0) | profession (0) |
| upward | `ABOVE(=+1) SIDE(=0) | e` | up (2) | overhead (1) |
| usually | `MANY(=+2) HAPPEN SAME(=-2) | e` | often (2) | often (2) |
| viewed | `SEE | i` | see (2) | see (2) |
| winners | `FIGHT(=-2) BEGIN(=+2) | o agent N+3` | players (1) | finalists (1) |
