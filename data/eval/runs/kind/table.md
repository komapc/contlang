| слово | old → ответ | new → ответ |
|---|---|---|
| sample | `PART(=-1) THINK(=+3) TEXT | o` → essay (0) | `KIND(=-3) PART(=0) CONSUME(=0) | o` → sample (2) |
| demonstration | `SEE BEGIN(=-1) ART(=-1) | o` → view (0) | `KIND(=-4) ART(=-1) GIVE(=+2) | o` → example (1) |
| picture | `SEE ART(=+2) TEXT | o` → fiction (0) | `KIND(=-3) SEE ART(=+2) | o PI DO SAME(=-2) | o` → image (2) |
| instance | `HAPPEN TIME(=-3) SAME(=0) | o` → history (1) | `KIND(=-2) TIME(=-2) HAPPEN | o` → precedent (2) |
| photograph | `SEE ART(=+2) TEXT | o` → literature (0) | `KIND(=-4) SEE ART(=+2) | o PI TEXT RULE(=+1) | o` → illustration (2) |
| image | `SEE ART(=+1) TEXT | o` → poster (2) | `KIND(=-2) SEE ART(=+1) | o` → picture (2) |
| evidence | `RULE(=+2) MANY(=-5) SEE | o` → secret (0) | `RULE(=+2) MANY(=-5) KIND(=-5) | o` → exception (0) |
| demonstrate | `DO THINK(=+4) MANY(=-4) | i` → quit (0) | `THINK(=+3) KIND(=-5) MANY(=-4) | i` → assume (0) |
| photo | `SEE TEXT ART(=+1) | o` → literature (0) | `KIND(=-3) TEXT SEE | o PI BIG(=+1) CHANGE(=+3) | o` → excerpt (0) |
| comparison | `SAME(=0) MEASURE(=+3) VALUE(=-3) | o` → average (1) | `SAME(=0) MEASURE(=+3) KIND(=-4) | o` → unit (0) |
| proof | `MANY(=-4) RULE(=+3) SEE | o` → neglect (0) | `MANY(=-3) KIND(=-5) RULE(=+2) | o` → exception (0) |
| testimony | `RULE(=+2) TEXT SEE | o` → notice (0) | `RULE(=+2) KIND(=-5) SEE | o` → case (1) |
| experiment | `ART(=-1) BEGIN(=-1) THINK(=+1) | o PI CAN(=0) GIVE(=-1) | o` → method (1) | `KIND(=-3) ART(=-1) BEGIN(=-1) | o PI CAN(=0) GIVE(=-1) | o` → stage (0) |
| case | `HAPPEN LONG(=+2) TEXT | o` → story (1) | `HAPPEN KIND(=-4) LONG(=+2) | o` → episode (1) |
| prototype | `ART(=-2) BEGIN(=-3) PART(=-2) | o` → element (0) | `KIND(=-2) ART(=-2) BEGIN(=-1) | o` → prototype (2) |
| contrast | `SAME(=-2) MEASURE(=+2) SEE | o` → comparison (2) | `SAME(=-2) KIND(=-4) MEASURE(=+2) | o PI LIVE(=+3) MOOD(=0) | o` → nutrient (0) |
| presentation | `TEXT GIVE(=+4) SEE | o` → notice (1) | `TEXT KIND(=-5) GIVE(=+4) | o` → leaflet (1) |
| examination | `RULE(=+1) CARE(=+4) SEE | o` → inspection (2) | `RULE(=+1) CARE(=+5) KIND(=-5) | o` → precaution (0) |
| footage | `SEE TIME(=-2) TEXT | o PI SAY(=+1) ART(=-1) | o` → transcript (1) | `SEE KIND(=-5) TEXT | o PI SAY(=+1) ART(=+2) | o` → sign (0) |
| trial | `BEGIN(=-1) RULE(=+5) FIGHT(=-1) | o` → kickoff (0) | `BEGIN(=-1) KIND(=-5) RULE(=+4) | o` → constitution (0) |
| argument | `THINK(=-1) FIGHT(=-1) TEXT | o` → debate (2) | `THINK(=-1) KIND(=-4) FIGHT(=-1) | o` → debate (2) |
| model | `ART(=-1) SAME(=+1) GRAIN(=+1) | o` → component (1) | `KIND(=-1) ART(=-1) | o PI MEASURE(=-1) BIG(=0) | o` → clock (1) |
| exhibit | `SEE ART(=+2) GIVE(=+3) | i` → show (2) | `GIVE(=+2) KIND(=-5) ART(=+3) | i` → exhibit (2) |
| protesters | `MOVE(=-4) FRIEND(=-4) SAY(=+5) | o N+3` → protests (2) | `KIND(=-5) MOVE(=-5) SAY(=+4) | o N+3` → cries (1) |
| interview | `TEXT RULE(=-1) TIME(=0) | i` → record (1) | `TEXT RULE(=-2) KIND(=-5) | i` → jot (0) |
| videotape | `SEE TIME(=-2) TEXT | o PI PART(=+1) SIDE(=-3) | o` → record (1) | `KIND(=-5) TIME(=-1) VALUE(=+2) | o PI SAY(=+1) ART(=-1) | o` → antique (0) |
| video | `SEE TEXT ART(=-2) | o` → diagram (0) | `SEE KIND(=-5) ART(=-2) | o` → observation (0) |
| pattern | `SAME(=-1) LONG(=-3) GRAIN(=+2) | o` → fiber (1) | `KIND(=-1) LONG(=-1) CHANGE(=0) | o` → thread (1) |
| explanation | `TEXT THINK(=-2) SAME(=-2) | o` → critique (0) | `THINK(=-1) KIND(=-3) TEXT | o` → essay (1) |
| lesson | `KNOW(=+2) ART(=+3) BEGIN(=0) | o` → culture (0) | `KIND(=-3) KNOW(=+4) ART(=+3) | o` → illustration (1) |
| precedent | `RULE(=+3) HAPPEN SAME(=-2) | o` → revolution (0) | `RULE(=+3) KIND(=-2) HAPPEN | o` → ruling (1) |
| scenario | `HAPPEN TEXT CAN(=+2) | o` → news (0) | `KIND(=-1) HAPPEN TEXT | o` → report (1) |
| reminder | `SEE TIME(=-3) GIVE(=+4) | o` → memory (1) | `KNOW(=+2) KIND(=-5) BIG(=-3) | o` → hint (1) |
| prove | `MANY(=-3) THINK(=+3) GIVE(=+1) | i` → limit (0) | `MANY(=-3) THINK(=+3) KIND(=-4) | i` → sample (0) |
| findings | `TEXT THINK(=+1) SEE | o` → essay (0) | `RULE(=+2) THINK(=0) KIND(=-5) | o PI MEASURE(=+2) WANT(=-2) | o` → precedent (0) |
| allegation | `RULE(=+2) THINK(=-2) TEXT | o PI TIME(=-3) MANY(=-5) | o` → document (1) | `RULE(=+2) THINK(=-2) KIND(=-4) | o` → accusation (2) |
| exam | `RULE(=+1) CARE(=+4) BEGIN(=+2) | o` → settlement (0) | `RULE(=+1) KIND(=-4) BEGIN(=+1) | o` → precedent (0) |
| exhibition | `ART(=+1) FIGHT(=-2) SEE | o` → spectacle (1) | `ART(=+2) FIGHT(=-3) KIND(=-5) | o` → puzzle (0) |
| interrogation | `RULE(=+2) THINK(=-3) CARE(=+5) | o PI FIGHT(=0) FRIEND(=-1) | o` → discipline (0) | `RULE(=+1) THINK(=-3) KIND(=-5) | o` → assumption (0) |
| study | `ART(=0) CARE(=+5) CONSUME(=+2) | o` → connoisseur (0) | `ART(=+1) CARE(=+5) KIND(=-3) | o` → craft (0) |
| display | `SEE GIVE(=+2) LONG(=+2) | i` → show (2) | `SEE KIND(=-2) GIVE(=+2) | i` → show (2) |
| lab | `ART(=-3) THING(=+3) PART(=0) | o` → machine (1) | `ART(=-3) KIND(=-5) THING(=+2) | o` → specimen (1) |
| laboratory | `ART(=-3) CARE(=+1) NEAR(=0) | o` → technique (1) | `ART(=-3) KIND(=-4) INSIDE(=+1) | o` → formula (1) |
| present | `GIVE(=+3) MOVE(=-3) HAPPEN | i` → deliver (2) | `GIVE(=+3) TIME(=+1) KIND(=-3) | i` → show (2) |
| interpretation | `TEXT ART(=+2) THINK(=-1) | o` → fiction (0) | `RULE(=+2) ART(=+3) KIND(=-3) | o PI THINK(=+1) DO | o` → masterpiece (1) |
| abstract | `ART(=+2) TEXT KNOW(=-3) | i` → draft (1) | `ART(=+2) KIND(=-3) TEXT | i` → compose (1) |
| gesture | `FRIEND(=+2) BODY DO | o` → helper (0) | `FRIEND(=+2) KIND(=-3) SAY(=-1) | o` → greeting (2) |
| prosecution | `RULE(=+4) FRIEND(=-2) SIDE(=+2) | o` → opposition (1) | `RULE(=+4) KIND(=-4) FRIEND(=-2) | o` → dissident (1) |
| method | `CAN(=+1) BEGIN(=-1) ART(=0) | o` → opportunity (0) | `KIND(=-1) CAN(=+1) ART(=0) | o` → technique (2) |
| context | `TEXT SAME(=-2) LIVE(=+3) | o` → biography (0) | `KIND(=-1) TEXT LIVE(=+3) | o` → biography (0) |
| impression | `SEE THINK(=-4) GRAIN(=+1) | o` → illusion (1) | `KIND(=-2) THINK(=-4) TEXT | o PI GIVE(=-1) GOOD(=+3) | o` → hearsay (0) |
| perspective | `SEE RULE(=0) ART(=+1) | o` → exhibition (0) | `SEE CHANGE(=+2) KIND(=-2) | o` → sign (0) |
| description | `TEXT MEASURE(=-1) SAME(=-1) | o` → note (1) | `TEXT KIND(=-1) SAME(=-1) | o` → passage (1) |
| demonstrators | `PART(=+5) FEEL(=+5) MOVE(=-5) | o N+3` → crowds (1) | `PART(=+5) FEEL(=+3) KIND(=-5) | o N+3` → feelings (0) |
| scene | `PLACE LIVE(=-1) SEE | o` → museum (0) | `PLACE KIND(=-2) LIVE(=-1) | o` → grave (0) |
| pose | `DO MOVE(=-5) THINK(=-1) | i` → hesitate (0) | `DO MOVE(=-5) KIND(=-3) | i` → show (0) |
| technique | `ART(=0) CAN(=+1) PART(=0) | o` → method (2) | `ART(=0) KIND(=-2) CAN(=+1) | o` → skill (1) |
| documentary | `TEXT ART(=+2) SEE | o PI HAPPEN BEGIN(=+1) | o` → script (1) | `TEXT ART(=+3) KIND(=-5) | o PI TIME(=-1) INSIDE(=-5) | o` → manuscript (1) |
| artwork | `ART(=+3) TEXT GOOD(=+1) | o` → literature (1) | `ART(=+3) TEXT KIND(=-3) | o` → literature (1) |
| defendant | `RULE(=+4) FRIEND(=-1) SOMEONE(=-1) | o` → officer (1) | `RULE(=+4) KIND(=-4) SOMEONE(=-2) | o` → deputy (1) |
| sort | `PART(=0) SAME(=0) FRIEND(=+3) | o` → companion (0) | `KIND(=+2) PART(=0) THINK(=+1) | o` → concept (1) |
| kind | `FRIEND(=+2) MANY(=0) PART(=0) | o` → group (1) | `KIND(=+1) FRIEND(=+2) MANY(=0) | o` → companion (0) |
| typical | `SAME(=-1) HAPPEN | a` → accidental (0) | `SAME(=-1) KIND(=0) HAPPEN | a` → usual (2) |
| style | `SAME(=-1) ART(=+3) MEASURE(=-3) | o` → nuance (1) | `KIND(=0) ART(=+3) SAME(=0) | o` → style (2) |
| thing | `MANY(=0) PART(=-1) HAPPEN | o` → instance (0) | `MANY(=0) KIND(=0) PART(=-1) | o` → portion (0) |
| characteristic | `SAME(=-3) HAPPEN MEASURE(=0) | o` → incident (0) | `SAME(=-2) KIND(=0) | o PI GOOD(=+2) BIG(=+1) | o` → nutrient (0) |
| mode | `MOVE(=0) CAN(=+3) SAME(=-2) | o` → mobility (0) | `KIND(=0) CAN(=+2) MOVE(=0) | o` → path (1) |
| form | `GRAIN(=+1) JOIN(=+3) TEXT | o` → book (1) | `KIND(=0) GRAIN(=+1) JOIN(=+2) | o` → joint (0) |
| manner | `SOMEONE(=-2) FRIEND(=+1) DO | o` → helper (0) | `KIND(=0) SOMEONE(=-3) FRIEND(=0) | o` → stranger (0) |
| category | `PART(=+2) MEASURE(=-1) ABOVE(=-3) | o` → base (0) | `KIND(=+3) PART(=+2) ABOVE(=-2) | o` → foundation (0) |
| variant | `SAME(=-1) CHANGE(=+2) PART(=0) | o` → variation (2) | `KIND(=0) SAME(=-2) CHANGE(=+1) | o PI TEXT TIME(=+1) | o` → variant (2) |
| classification | `PART(=+2) MEASURE(=+1) RULE(=+2) | o` → budget (0) | `KIND(=+3) PART(=+2) RULE(=+3) | o` → institution (0) |
| shape | `CHANGE(=+2) MEASURE(=-3) GRAIN(=+4) | o` → chip (0) | `KIND(=0) CHANGE(=+2) GRAIN(=+2) | o` → pattern (1) |
| concept | `ART(=+1) BEGIN(=-3) THINK(=-2) | o` → hypothesis (2) | `KIND(=-1) ART(=+1) THINK(=-2) | o` → hypothesis (2) |
| class | `PART(=+2) BEGIN(=0) ART(=+1) | o PI KNOW(=+2) GIVE(=+1) | o` → tradition (0) | `KIND(=+2) PART(=+2) ABOVE(=+1) | o` → category (2) |
| aspect | `PART(=-2) MANY(=+3) SAME(=-5) | o` → variety (1) | `KIND(=0) PART(=-3) SAME(=-4) | o` → trait (2) |
| particular | `SAME(=-2) CARE(=+3) HAPPEN | a` → incidental (0) | `SAME(=-2) KIND(=+1) CARE(=+3) | a` → precise (2) |
| approach | `NEAR(=0) BEGIN(=-2) CARE(=+2) | i` → approach (2) | `KIND(=0) NEAR(=0) SIDE(=+2) | i` → face (1) |
| structure | `GRAIN(=+3) INSIDE(=0) CHANGE(=+1) | o` → crust (0) | `GRAIN(=+2) KIND(=+1) INSIDE(=0) | o` → shell (1) |
| attitude | `FRIEND(=+1) CHANGE(=+2) ART(=+1) | o` → reform (0) | `KIND(=-1) CHANGE(=+1) FRIEND(=0) | o` → variation (0) |
| genre | `ART(=+2) LAND(=0) SAME(=-1) | o` → landscape (2) | `ART(=+2) KIND(=+5) LAND(=0) | o` → landscape (2) |
| element | `PART(=-1) GRAIN(=-1) LIVE(=+4) | o` → blood (1) | `PART(=-1) KIND(=+1) LIVE(=+3) | o` → organism (1) |
| way | `SOMEONE(=0) NEAR(=-1) CAN(=+2) | o` → stranger (0) | `SOMEONE(=-1) KIND(=0) NEAR(=-1) | o` → stranger (0) |
| standard | `SAME(=0) RULE(=+2) LONG(=+2) | o` → ruler (1) | `RULE(=+2) SAME(=+1) KIND(=0) | o PI MEASURE(=+1) BIG(=-1) | o` → standard (2) |
| behavior | `FRIEND(=0) CHANGE(=+1) DO | o` → negotiation (1) | `KIND(=-1) CHANGE(=+1) FRIEND(=-1) | o PI SEE HAPPEN | o` → crisis (0) |
| arrangement | `PART(=+2) FRIEND(=+3) VALUE(=-5) | o` → charity (0) | `KIND(=-1) PART(=+3) VALUE(=-4) | o` → junk (0) |
| criteria | `RULE(=+2) THINK(=+2) SAME(=-1) | o N+3` → principles (2) | `KIND(=+1) THINK(=+1) RULE(=+3) | o N+3` → rules (2) |
| variety | `SAME(=-3) PART(=+3) MEASURE(=-2) | o` → variety (2) | `SAME(=-3) KIND(=+2) BIG(=+2) | o` → genre (1) |
| formula | `ART(=0) SAME(=+3) TEXT | o` → document (1) | `KIND(=+1) MEASURE(=+1) TEXT | o` → table (1) |
| specific | `SAME(=-1) RULE(=0) CARE(=+2) | a` → particular (2) | `SAME(=-1) KIND(=+2) CARE(=+3) | a` → specific (2) |
| routine | `DO FEEL(=-3) HAPPEN | o` → activity (1) | `KIND(=-1) FEEL(=-3) DO | o` → actor (0) |
| guy | `SEX(=+3) FRIEND(=+3) MANY(=+1) | o` → boyfriend (1) | `SEX(=+3) KIND(=0) MANY(=+1) | o` → gender (1) |
| phase | `BEGIN(=-1) ART(=-1) PART(=0) | o PI PLACE LAND(=+1) | o` → trade (0) | `BEGIN(=-1) KIND(=0) | o` → start (1) |
| scheme | `PART(=+1) BEGIN(=-3) CAN(=+2) | o` → chance (0) | `KIND(=0) BEGIN(=-2) GIVE(=+1) | o` → gift (0) |
| level | `ABOVE(=0) MEASURE(=0) PLACE | o PI CAN(=0) FIGHT(=-1) | o` → floor (2) | `ABOVE(=0) KIND(=+2) MEASURE(=0) | o` → level (2) |
| person | `RULE(=-1) MANY(=+2) FRIEND(=+3) | o` → club (0) | `KIND(=0) RULE(=-1) MANY(=+1) | o` → habit (0) |
| variation | `SAME(=-1) CHANGE(=+2) MEASURE(=0) | o` → variation (2) | `SAME(=-1) CHANGE(=+2) MEASURE(=0) | o PI KIND(=-1) LONG(=-1) | o` → variable (1) |
| idea | `THINK(=-2) BEGIN(=-3) ART(=+2) | o PI TEXT GIVE(=+4) | o` → hypothesis (2) | `THINK(=-2) ART(=+1) KIND(=-1) | o PI TEXT GIVE(=+4) | o` → editorial (1) |
| array | `PART(=+2) BIG(=+3) ART(=-2) | o` → structure (2) | `PART(=+2) BIG(=+3) KIND(=-1) | o` → mass (1) |
| layout | `TEXT INSIDE(=+1) ART(=-1) | o` → manual (1) | `TEXT KIND(=0) INSIDE(=+1) | o` → passage (1) |
| designation | `RULE(=+2) SAME(=-2) PLACE | o` → office (1) | `RULE(=+2) KIND(=+3) GIVE(=+3) | o` → service (1) |
| fashion | `ART(=+2) LONG(=-4) HAPPEN | o` → weaving (1) | `KIND(=0) LONG(=-4) ART(=+2) | o` → embroidery (1) |
| batch | `PART(=+2) GRAIN(=0) TIME(=+1) | o` → crop (1) | `PART(=+2) KIND(=-2) TIME(=+1) | o` → preview (0) |
| scale | `MEASURE(=-1) BIG(=0) | o PI ABOVE(=+1) BEGIN(=+2) | o` → level (1) | `MEASURE(=-1) BIG(=0) KIND(=0) | o` → unit (1) |
| tactic | `FIGHT(=+1) CHANGE(=+2) CAN(=+1) | o` → conflict (0) | `KIND(=-1) FIGHT(=+2) CAN(=+1) | o` → contest (0) |
| species | `PART(=+1) THING(=+3) SAME(=-3) | o` → creature (2) | `THING(=+2) KIND(=+5) SAME(=-4) | o` → species (2) |
| behaviour | `FRIEND(=0) CHANGE(=+1) DO | o PI CARE(=-1) WANT(=-5) | o` → interaction (2) | `KIND(=0) FRIEND(=-1) CHANGE(=+1) | o PI CARE(=-1) WANT(=-5) | o` → conflict (1) |
| personality | `RULE(=-1) SAME(=-5) MEASURE(=-3) | o` → exception (0) | `RULE(=-1) KIND(=+2) SAME(=-5) | o` → exception (0) |
| phrase | `TEXT SAME(=-1) SAY(=0) | o` → transcript (1) | `TEXT KIND(=+1) SAY(=0) | o` → transcript (1) |
| breed | `THING(=+3) PART(=+2) SAME(=-1) | i` → gather (0) | `THING(=+3) KIND(=+2) JOIN(=+1) | i` → breed (2) |
| size | `MEASURE(=-2) BIG(=-1) | o` → portion (1) | `MEASURE(=-2) BIG(=0) KIND(=-1) | o` → quantity (1) |
| object | `WANT(=0) PART(=-2) LONG(=+1) | o` → need (0) | `WANT(=0) PART(=-2) KIND(=-1) | o` → need (0) |
| ways | `SOMEONE(=-2) CAN(=+1) CHANGE(=+3) | o` → reformer (0) | `SOMEONE(=-2) KIND(=0) CAN(=+1) | o` → professional (0) |
| recipe | `TEXT SAME(=+2) CONSUME(=+3) | o` → reading (0) | `TEXT CONSUME(=+3) KIND(=0) | o` → reading (0) |
| notion | `THINK(=-2) ART(=+1) MANY(=+1) | o` → uncertainty (0) | `THINK(=-2) ART(=+1) KIND(=-1) | o PI KNOW(=+1) WANT(=+5) | o` → question (1) |
| habit | `WANT(=+1) BEGIN(=-4) FEEL(=-4) | o` → desire (0) | `KIND(=0) WANT(=+1) FEEL(=-3) | o` → contentment (0) |
| mechanism | `ART(=-2) SIDE(=-2) CAN(=+1) | o` → backup (1) | `ART(=-2) KIND(=+1) CAN(=+1) | o` → method (2) |
| rank | `MEASURE(=+1) FIGHT(=+2) RULE(=+2) | o` → competition (1) | `MEASURE(=+1) FIGHT(=+3) KIND(=+4) | o` → campaign (0) |
| grade | `ABOVE(=+1) MEASURE(=0) BEGIN(=+2) | o PI ART(=+1) INSIDE(=+1) | o` → roof (0) | `ABOVE(=+2) KIND(=+4) BEGIN(=+2) | o` → peak (1) |
| genus | `PART(=+2) SAME(=-1) | o PI THING(=0) ART(=-4) | o` → variety (2) | `PART(=+2) KIND(=+4) SAME(=-1) | o PI THING(=0) ART(=-4) | o` → variety (2) |
| name | `TEXT MEASURE(=-5) GIVE(=+4) | o` → bill (0) | `TEXT KIND(=+4) MEASURE(=-5) | o PI MANY(=-2) GIVE(=+3) | o` → word (2) |
| specialty | `SAME(=-4) PART(=+4) ART(=-2) | o` → specialty (2) | `SAME(=-5) KIND(=+5) PART(=+5) | o` → variety (1) |
| tier | `LONG(=+1) ABOVE(=0) BEGIN(=-1) | o` → line (1) | `ABOVE(=0) KIND(=+3) LONG(=+2) | o` → pillar (0) |
| generic | `SAME(=0) VALUE(=-3) TEXT | a` → trivial (1) | `VALUE(=-2) KIND(=+2) SAME(=0) | a` → cheap (1) |
| brand | `VALUE(=-1) MEASURE(=-4) PART(=+4) | o PI SAME(=0) ART(=-1) | o` → cost (0) | `VALUE(=-1) KIND(=+5) MEASURE(=-5) | o` → price (1) |
| system | `ART(=-2) MANY(=+2) RULE(=+2) | o` → code (1) | `ART(=-3) KIND(=+2) INSIDE(=+2) | o` → method (2) |
| lifestyle | `LIVE(=+2) CHANGE(=+2) INSIDE(=-2) | o` → nature (0) | `LIVE(=+2) KIND(=+2) CHANGE(=+2) | o` → organism (0) |
| specializes | `ART(=0) SAME(=-3) KNOW(=+4) | i` → distinguish (0) | `ART(=-1) KIND(=+5) SAME(=-5) | i` → classify (0) |
| racial | `FIGHT(=-1) RULE(=-2) MEASURE(=0) | a` → casual (0) | `FIGHT(=-1) RULE(=-2) KIND(=+4) | a` → informal (0) |
| disorder | `FEEL(=-1) HAPPEN SAME(=-2) | o` → surprise (0) | `FEEL(=0) KIND(=+2) HAPPEN | o` → experience (0) |
| nickname | `SAME(=0) FIGHT(=-2) PLACE | o` → arena (0) | `KIND(=+3) FIGHT(=-3) VALUE(=+5) | o PI TEXT MEASURE(=-3) | o` → trophy (0) |
| oriented | `SIDE(=+1) CARE(=+2) SAME(=-2) | i` → prepare (0) | `SIDE(=+1) CARE(=+2) KIND(=+2) | i` → prepare (0) |
| guild | `PART(=+4) GIVE(=+3) FIGHT(=-1) | o PI ART(=+1) LONG(=+1) | o` → team (1) | `PART(=+5) KIND(=+5) JOIN(=+5) | o` → association (2) |
| pictures | `SEE ART(=+2) TEXT | o N+3` → illustrations (2) | `KIND(=-3) SEE ART(=+2) | o N+3 PI DO SAME(=-2) | o` → artworks (2) |
| figure | `MEASURE(=+1) THINK(=+1) ART(=+2) | o` → theory (0) | `KIND(=-1) MEASURE(=+1) THINK(=0) | o` → standard (0) |
| embassy | `INSIDE(=0) RULE(=+2) TEXT | o` → regulation (0) | `INSIDE(=0) KIND(=-5) RULE(=+2) | o` → loophole (0) |
| bombers | `GRAIN(=-1) FIGHT(=+5) ABOVE(=-2) | o N+3` → mines (1) | `GRAIN(=-1) FIGHT(=+5) KIND(=-1) | o N+3` → bullets (1) |
| representation | `RULE(=+2) ART(=+2) GRAIN(=+2) | o` → monument (1) | `KIND(=-2) ART(=+2) RULE(=+2) | o` → genre (0) |
| classes | `PART(=+2) BEGIN(=0) ART(=+1) | o N+3 PI KNOW(=+2) GIVE(=+1) | o` → disciplines (1) | `KIND(=+2) PART(=+2) ABOVE(=+1) | o N+3` → categories (2) |
| step | `SIDE(=0) BEGIN(=-1) DO | o PI SOMEONE(=-2) SAY(=-4) | o` → rumor (0) | `SIDE(=0) BEGIN(=0) KIND(=-1) | o` → edge (0) |
| hybrid | `SAME(=-1) ART(=-3) THING(=+2) | o` → robot (0) | `KIND(=+1) ART(=-3) THING(=+3) | o` → robot (0) |
| fighters | `FIGHT(=+1) | o N+3 PI GRAIN(=-3) MOVE(=+1) | o` → waves (0) | `FIGHT(=+1) | o N+3 PI GRAIN(=-3) KIND(=0) | o` → germs (0) |
| example | `SAME(=-1) HAPPEN TEXT | o PI SEE TIME(=-2) | o` → record (0) | `KIND(=-2) SAME(=-1) | o` → variant (1) |
| norm | `SAME(=-1) MEASURE(=+3) RULE(=+3) | o PI MANY(=+2) SOMEONE(=-5) | o` → custom (2) | `KIND(=0) MEASURE(=+3) RULE(=+3) | o PI SAME(=+1) FEEL(=-3) | o` → norm (2) |
| thriller | `TEXT FIGHT(=0) MOOD(=-1) | o PI GOOD(=-2) FEEL(=0) | o` → complaint (0) | `TEXT FIGHT(=0) MOOD(=-1) | o PI ART(=+2) KIND(=+5) | o` → criticism (0) |
| elephant | `THING(=+3) BIG(=+2) MOVE(=-1) | o` → beast (2) | `THING(=+3) BIG(=+2) KIND(=-3) | o` → beast (2) |
| aerial | `GRAIN(=-3) FIGHT(=+4) LAND(=+4) | o PI TEXT SEE | o` → navy (1) | `GRAIN(=-3) FIGHT(=+4) LAND(=+4) | o PI KIND(=-3) TEXT | o` → trench (1) |
| instances | `HAPPEN TIME(=-3) SAME(=0) | o N+3` → history (1) | `KIND(=-2) TIME(=-2) HAPPEN | o N+3` → precedents (2) |
| styles | `SAME(=-1) ART(=+3) MEASURE(=-3) | o N+3` → patterns (1) | `KIND(=0) ART(=+3) SAME(=0) | o N+3` → genres (2) |
| cameras | `SEE ART(=-3) NEAR(=-2) | o N+3 PI HEAT(=+2) MOVE(=+3) | o` → instruments (2) | `SEE ART(=-3) NEAR(=-2) | o N+3 PI KIND(=-3) TEXT | o` → diagrams (1) |
| protocol | `RULE(=+2) BEGIN(=-2) TEXT | o` → charter (1) | `RULE(=+2) KIND(=0) TEXT | o` → regulation (2) |
| backdrop | `SEE INSIDE(=-3) MOVE(=-2) | o` → glance (0) | `KIND(=-2) INSIDE(=-2) MOVE(=-2) | o` → fixture (1) |
| dictatorship | `FRIEND(=-2) RULE(=+5) ART(=-1) | o` → litigation (0) | `FRIEND(=-3) RULE(=+5) KIND(=+2) | o` → dictator (2) |
| tabloid | `TEXT TIME(=0) VALUE(=-2) | o PI RULE(=-2) ART(=+4) | o` → graffiti (0) | `TEXT TIME(=0) VALUE(=-2) | o PI RULE(=-2) KIND(=+4) | o` → receipt (0) |
| format | `TEXT MEASURE(=-2) FIGHT(=-2) | i` → chat (0) | `TEXT KIND(=+1) MEASURE(=-2) | i` → record (1) |
| definition | `RULE(=+2) MEASURE(=0) SEE | o` → review (0) | `KIND(=+1) RULE(=+3) SEE | o` → standard (1) |
| shows | `SEE DO MANY(=-1) | i` → glance (0) | `SEE KIND(=-1) DO | i` → show (2) |
| gender | `RULE(=-1) CHANGE(=+2) MEASURE(=-2) | o` → adjustment (0) | `RULE(=-1) KIND(=+5) CHANGE(=+3) | o` → fashion (1) |
| interface | `ART(=-3) JOIN(=+2) TEXT | o` → program (1) | `JOIN(=+2) ART(=-5) KIND(=0) | o` → machine (1) |
| creatures | `THING(=+2) PART(=-1) FRIEND(=-1) | o N+3` → insects (2) | `THING(=+2) KIND(=+1) LIVE(=+2) | o N+3` → creatures (2) |
| character | `TEXT SAME(=-4) MEASURE(=-2) | o` → excerpt (0) | `TEXT KIND(=+2) SAME(=-3) | o PI FIGHT(=+1) GOOD(=+3) | o` → record (0) |
| testament | `TEXT LIVE(=-1) RULE(=+4) | o PI GOOD(=+2) BIG(=+1) | o` → testament (2) | `RULE(=+3) LIVE(=-1) KIND(=-4) | o` → victim (0) |
| script | `TEXT | o PI DO ART(=+2) | o` → literature (1) | `TEXT | o PI KIND(=-1) HAPPEN | o` → report (0) |
| amir | `WANT(=-5) MEASURE(=-5) CARE(=-5) | o` → waste (0) | `KIND(=-5) MEASURE(=-5) WANT(=-5) | o` → lack (0) |
| warriors | `FIGHT(=+3) FRIEND(=+1) TOUCH(=+2) | o N+3` → blows (0) | `FIGHT(=+2) TOUCH(=+2) KIND(=0) | o N+3` → weapons (1) |
| strains | `TOUCH(=+1) BODY JOIN(=0) | o N+3` → contacts (0) | `TOUCH(=+1) KIND(=0) JOIN(=0) | o N+3 PI BODY SIDE(=-1) | o` → joints (1) |
| status | `RULE(=+1) CHANGE(=-1) PLACE | o` → office (1) | `RULE(=+1) KIND(=+2) CHANGE(=-1) | o` → tradition (0) |
| scenes | `PLACE LIVE(=-1) SEE | o N+3` → ruins (0) | `PLACE KIND(=-2) LIVE(=-1) | o N+3` → homes (0) |
| showing | `SEE GIVE(=+3) SAME(=-3) | i` → show (2) | `SEE KIND(=-3) GIVE(=+3) | i` → indicate (2) |
| exhibited | `SAME(=-2) SEE GIVE(=+2) | i` → reveal (2) | `SAME(=-2) KIND(=-5) GIVE(=+2) | i` → demonstrate (2) |
| ratings | `MEASURE(=+1) RULE(=+2) | o N+3 PI ABOVE(=+1) BEGIN(=+2) | o` → limits (0) | `MEASURE(=+1) KIND(=+2) RULE(=+3) | o N+3 PI THINK(=+1) CARE(=+3) | o` → standards (1) |
| test | `THINK(=+2) ART(=-3) FIGHT(=-1) | i` → plan (0) | `KIND(=-3) THINK(=+3) ART(=-2) | i` → prove (1) |
| poster | `TEXT LONG(=+1) SEE | o` → poster (2) | `TEXT KIND(=-3) LONG(=+2) | o` → excerpt (0) |
| process | `BEGIN(=-1) ART(=-1) CARE(=+1) | o` → basics (0) | `BEGIN(=-1) ART(=-1) KIND(=-2) | o PI MOVE(=+3) BIG(=+1) | o` → start (1) |
| instead | `SOMEONE(=-1) MOVE(=-2) SAME(=0) | e` → slowly (0) | `SOMEONE(=-2) MOVE(=-2) KIND(=0) | e` → slowly (0) |
| interviews | `TEXT RULE(=-2) TIME(=0) | i` → scribble (0) | `TEXT RULE(=-3) KIND(=-5) | i` → quote (1) |
| document | `TEXT RULE(=+1) | o` → document (2) | `TEXT KIND(=-2) RULE(=+1) | o` → instruction (1) |
| plaintiffs | `RULE(=+3) SOMEONE(=-5) THING(=-2) | o N+3` → property (0) | `RULE(=+3) SOMEONE(=-4) KIND(=-3) | o N+3` → officials (0) |
| genes | `PART(=0) ART(=-2) THING(=+4) | o N+3` → livestock (1) | `KIND(=+1) ART(=-2) THING(=+4) | o N+3` → machines (0) |
| sequence | `BEGIN(=-1) LONG(=-1) HAPPEN | o` → beginning (0) | `BEGIN(=-1) KIND(=-1) LONG(=-1) | o` → beginning (0) |
| theory | `ART(=0) THINK(=-2) RULE(=+1) | o` → doctrine (2) | `ART(=0) THINK(=-2) KIND(=-1) | o PI MANY(=-2) CARE(=+5) | o` → puzzle (0) |
| unspecified | `TIME(=+1) RULE(=-2) MEASURE(=-3) | a` → temporary (0) | `TIME(=+1) KIND(=+3) BIG(=+1) | a` → upcoming (0) |
| symbol | `SAME(=0) VALUE(=+2) LONG(=0) | o` → stick (0) | `KIND(=-1) VALUE(=+2) LONG(=0) | o` → bar (0) |
| protests | `SAY(=+1) WANT(=-3) FRIEND(=-3) | i` → criticize (1) | `SAY(=+1) WANT(=-4) KIND(=-5) | i` → object (2) |
| procedure | `HAPPEN RULE(=+4) CARE(=+3) | o` → procedure (2) | `KIND(=-1) RULE(=+4) HAPPEN | o PI DO ART(=-5) | o` → case (1) |
| checkpoints | `NEAR(=+1) FIGHT(=+4) BEGIN(=+1) | o N+3` → fronts (1) | `NEAR(=+1) FIGHT(=+4) KIND(=-5) | o N+3` → battles (1) |
| documents | `TEXT RULE(=+1) | o N+3` → documents (2) | `TEXT KIND(=-2) RULE(=+1) | o N+3` → guidelines (2) |
| type | `SAME(=0) MEASURE(=-4) FRIEND(=+3) | o` → companion (0) | `KIND(=+1) | o` → kind (2) |
| entity | `RULE(=0) PART(=0) LAND(=-1) | o` → coast (0) | `RULE(=0) KIND(=+1) PART(=0) | o` → standard (0) |
| setting | `PLACE HEAT(=+3) PART(=+4) | i` → gather (0) | `KIND(=0) HEAT(=+3) PLACE | i` → heat (0) |
| suggestions | `THINK(=-2) GIVE(=+4) TEXT | o N+3` → suggestions (2) | `THINK(=-2) GIVE(=+4) KIND(=-2) | o N+3` → suggestions (2) |
| portrait | `SEE ART(=+5) TEXT | o` → poster (1) | `KIND(=-3) ART(=+4) SEE | o` → picture (2) |
| methods | `CAN(=+1) BEGIN(=-1) ART(=0) | o N+3` → opportunities (0) | `KIND(=-1) CAN(=+1) ART(=0) | o N+3` → skills (1) |
| thoughts | `THINK(=-2) SOMEONE(=+2) KNOW(=+1) | o N+3 PI MANY(=0) GOOD(=0) | o` → skeptics (0) | `THINK(=-2) SOMEONE(=+1) KIND(=0) | o N+3 PI KNOW(=+1) WANT(=+5) | o` → skeptics (0) |
| proposition | `THINK(=-1) RULE(=+4) TEXT | o` → constitution (1) | `THINK(=-1) RULE(=+4) KIND(=-2) | o` → principle (1) |
| syndrome | `HAPPEN BODY MOOD(=-2) | o PI SAME(=-1) CHANGE(=+2) | o` → accident (0) | `BODY KIND(=+1) HAPPEN | o` → reaction (1) |
| creditors | `RULE(=+1) CAN(=-2) PART(=+4) | o N+3 PI MEASURE(=+1) GRAIN(=-2) | o` → restrictions (0) | `RULE(=+1) CAN(=-2) PART(=+4) | o N+3 PI WANT(=+2) MEASURE(=+3) | o` → restrictions (0) |
| dissidents | `PART(=+2) SAME(=-5) TOUCH(=+5) | o N+3` → rocks (0) | `PART(=+2) SAME(=-5) TOUCH(=+5) | o N+3 PI FIGHT(=+3) FRIEND(=-4) | o` → weapons (0) |
| pair | `PART(=+2) SAME(=+3) SOMEONE(=-3) | o PI SEE LONG(=0) | o` → audience (0) | `PART(=+2) SAME(=+3) SOMEONE(=-3) | o` → public (0) |
| dictionary | `TEXT ART(=+1) CAN(=+1) | o` → writing (1) | `TEXT ART(=0) VALUE(=-1) | o PI BEGIN(=+1) MEASURE(=0) | o` → paper (0) |
| managers | `RULE(=+2) ART(=-4) PART(=+5) | o N+3 PI THING(=+2) VALUE(=-2) | o` → systems (0) | `RULE(=+2) ART(=-4) PART(=+5) | o N+3 PI CAN(=0) THINK(=+5) | o` → protocols (0) |
| burke | `LIVE(=-1) MOVE(=+3) JOIN(=-2) | o PI SIDE(=+4) TIME(=-5) | o` → insect (0) | `LIVE(=-1) MOVE(=+3) JOIN(=-2) | o PI TEXT INSIDE(=+4) | o` → page (0) |
| budget | `RULE(=+2) MEASURE(=+1) VALUE(=-2) | o PI BEGIN(=-1) THINK(=+1) | o` → tax (1) | `RULE(=+2) MEASURE(=+1) VALUE(=-2) | o` → tax (1) |
| journals | `TEXT | o N+3 PI TIME(=0) MEASURE(=+4) | o` → data (1) | `TEXT | o N+3 PI TIME(=0) RULE(=-2) | o` → notes (2) |
| yearly | `MEASURE(=+2) TIME(=-1) PART(=+4) | o PI MANY(=+3) SOMEONE(=-5) | o` → frequency (1) | `MEASURE(=+2) TIME(=-1) PART(=+4) | o` → schedule (1) |
| defining | `THINK(=+2) SAME(=-3) LIVE(=+2) | i` → imagine (0) | `SAME(=-2) THINK(=+3) BEGIN(=+1) | i` → revise (0) |
| quest | `BEGIN(=0) WANT(=+5) FIGHT(=0) | o PI THINK(=+2) SEE | o` → competition (1) | `BEGIN(=0) WANT(=+5) FIGHT(=0) | o PI SEE THINK(=+2) | o` → desire (1) |
| gilbert | `TEXT FEEL(=+5) THING(=-4) | o` → inscription (0) | `THING(=-3) FEEL(=+5) GOOD(=-5) | o` → agony (0) |
| layer | `PART(=-1) TOUCH(=-3) ABOVE(=0) | o` → dust (1) | `PART(=-1) TOUCH(=-2) HEAT(=-1) | o` → cushion (0) |
| kohl | `SEE THING(=-2) VALUE(=-2) | o` → sale (0) | `SEE THING(=-2) TIME(=-3) | o` → relic (0) |
| multimedia | `ART(=-1) JOIN(=+3) BIG(=+2) | o PI SEE TEXT | o` → database (1) | `ART(=-1) JOIN(=+3) BIG(=+2) | o PI TEXT TIME(=+1) | o` → system (1) |
| professor | `ART(=+1) KNOW(=+2) TIME(=-1) | o` → history (1) | `ART(=+1) KNOW(=+2) TIME(=-1) | o PI PART(=+4) ABOVE(=+5) | o` → news (0) |
| highway | `NEAR(=+1) THING(=-1) SIDE(=+3) | o PI MEASURE(=+1) MOVE(=+2) | o` → front (0) | `NEAR(=+1) THING(=-1) SIDE(=+3) | o` → front (0) |
| advertising | `ART(=0) VALUE(=-3) TEXT | o` → pamphlet (2) | `ART(=0) VALUE(=-3) TEXT | o PI GIVE(=+2) FIGHT(=-1) | o` → flyer (2) |
| warnings | `KNOW(=+1) SAY(=+2) TEXT | o N+3 PI CARE(=+1) THINK(=-2) | o` → newspaper (0) | `KNOW(=+1) SAY(=+2) TEXT | o N+3` → news (0) |
| creator | `ART(=+1) WANT(=+1) LIVE(=0) | o PI DO JOIN(=+1) | o` → hobby (0) | `ART(=+1) WANT(=+2) MOOD(=+3) | o PI DO JOIN(=+1) | o` → entertainment (0) |
