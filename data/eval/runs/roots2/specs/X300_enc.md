# Encoder instructions (words)

You will encode single English words into min-co.
A different person will decode your codes WITHOUT seeing the English, using only the spec below. Write each code so that its meaning can be recovered.

- Use ONLY the 300 roots below; never invent roots or use English words as roots. At most 3 roots per word.
- Do not quote common words. Give exactly one code per input item, with the same numbering, as `N. CODE`. No other text.

# min-co: how a word is written

A word is `ROOTS | FORM`.

- ROOTS: 1 to 3 roots. The first is the head: what kind of thing, action or quality it is. Each next root narrows everything before it.
- FORM: the part of speech, then optional marks.
  - Parts of speech: `o` noun, `i` verb, `a` adjective, `e` adverb.
  - Example: `PLACE LIVE | o` = a place where one lives = house.

A root may carry a value on its axis, `ROOT(=v)`, with v from -5 to +5.
The anchors listed with each root name some points of its axis. **Every value from -5 to +5 is usable**: a value between
two anchors means something between them (`GOOD(=+1)` = okay, `GOOD(=+4)` = very good, `BIG(=-3)` = quite small).
Pick the value that fits best; do not round to ±5. With no value, the root is meant plainly (`GOOD` = good).
HAPPEN never takes a value.

## Roots (300)

- GOOD: -5 terrible … -2 poor … 0 so-so … +2 fine … +5 excellent
- BIG: -5 tiny … -2 small … 0 medium … +2 large … +5 huge (size only)
- NEAR: -5 far, abroad, journey … -2 away, elsewhere … 0 around, in the area … +3 near, close … +5 here, the centre
- ABOVE: -5 bottom, down … -2 low … 0 level, middle height … +2 high … +5 top, up, sky
- LIVE: -5 dead … -3 dying, ill … -2 asleep … 0 living … +3 healthy … +5 lively, full of life
- SAME: -5 opposite … -3 different, other, special … 0 similar, like … +3 usual, ordinary … +5 identical, the same
- TIME: -5 long ago … -2 recently … -1 just now … 0 now … +1 soon … +2 later … +5 far future
- INSIDE: -5 outside, outdoors … -2 near the outside … 0 surface, edge, border … +2 within … +5 deep inside, core
- PART: -5 particle, crumb … -2 a part, piece, member … 0 one unit, a single whole … +2 a pair, a few together … +5 a group, set, collection
- SIDE: -5 back, behind, backward, return … -2 aside … 0 beside, sideways … +2 ahead … +5 front, forward, coming up
- KNOW: -5 not know, ignorant, absurd … -2 guess … 0 notice, be aware … +3 understand … +5 know well, expert (teach = GIVE KNOW)
- WANT: -5 hate, refuse … -2 dislike … 0 indifferent … +2 like, wish … +5 love, crave
- HEAT: -5 ice cold … -2 cool … 0 lukewarm … +2 warm … +5 fire hot
- BEGIN: -5 start, origin … -2 early stage … 0 ongoing, middle … +2 late stage … +5 end, finish
- GIVE: -5 grab, seize, steal … -2 take, get … 0 exchange, trade … +2 offer, lend … +5 give, donate, grant
- TOUCH: -5 soft, tender … -2 smooth, gentle … 0 touch, contact … +2 firm, rough … +5 hard, stiff, harsh
- SEX: -5 female … +5 male (only for words of explicit sex; nothing in between)
- HAPPEN: event, happen (no axis)
- THINK: -5 doubt … -2 wonder … 0 think … +3 plan, intend … +5 decide
- CAN: -5 impossible … -3 hard … 0 possible … +3 easy … +5 effortless, certain to succeed
- MANY: -5 none, never … -3 rarely, very few … -1 few … 0 some … +3 many, often … +5 all, always
- SOMEONE: -5 they, others … -3 he, she … 0 someone … +3 you … +5 I
- THING: -5 stone, inanimate … -2 material, stuff … 0 plant … +2 small creature, insect … +4 animal
- MOVE: -5 stand still … -2 creep, slow … 0 walk, go … +2 run … +5 rush, fly
- FEEL: -5 numb, calm … -2 mild … 0 feel … +2 strong feeling … +5 excited, intense (pleasant or not is GOOD)
- RULE: -5 private, personal … -2 habit, custom … 0 rule, norm … +3 authority, institution … +5 law, official
- CHANGE: -5 keep, stay the same … -2 adjust, adapt … 0 change … +3 turn into, become … +5 transform completely
- ART: -5 technology, exact science … -2 engineering, trade … 0 skill, craft … +2 design … +5 arts, humanities
- JOIN: -5 separate, remove … -2 loosen, detach … 0 touch, meet … +3 connect, attach, add … +5 merge, unite
- VALUE: -5 worthless … -2 cheap … 0 price, worth, buying and selling … +2 expensive … +5 precious, vital, important
- CARE: -5 careless, a mistake, fault … -2 casual … 0 attention … +2 careful … +5 thorough, diligent
- FRIEND: -5 enemy, hostile, cruel … -2 unfriendly … 0 stranger, neutral … +2 friendly … +5 close friend, kind
- MOOD: -5 tragic … -3 sad … 0 serious … +3 glad … +5 funny
- CONSUME: -5 give out, emit … -3 speak, write … 0 exchange … +3 read, listen … +5 take in, eat, drink
- MEASURE: -5 an amount (size, length, weight) … -2 a count, number … 0 a level, degree … +2 a rate, speed … +5 a ratio, percentage, statistics
- LONG: -5 thread, cloth, textile … -2 rope, cord … 0 wire, rod, fastening … +2 pole, stick … +5 beam, plank, wooden furniture
- SAY: -5 ask, question … -2 answer, reply … 0 say, tell … +3 claim, promise … +5 order, command (loudness is the I mark: `SAY | i I+5` = shout)
- GRAIN: -5 gas … -3 liquid … -1 mud, paste … 0 powder, grain … +2 lump, chunk … +5 one solid piece
- FIGHT: -5 game, sport … -2 contest … 0 quarrel … +2 fight, struggle … +5 war
- LAND: -5 deep sea … -2 water, lake, river … 0 shore, coast … +2 field, countryside … +5 dry land, mountains, ground
- BODY: -5 head … -3 face, eye, mouth … 0 trunk, chest, belly … +3 arm, hand … +5 leg, foot (plain BODY = the body)
- SEE: -5 hidden, unseen … -2 glimpse … 0 see, look … +3 watch, observe … +5 visible, obvious
- DO: -5 rest, idle … -2 try … 0 do, act … +3 make, work … +5 labour, toil
- PLACE: -5 spot, point … -3 room … 0 building … +3 town, city … +5 country, world (plain PLACE = a place)
- TEXT: -5 letter, sign, symbol … -2 word, name … 0 sentence, message … +3 article, document … +5 book
- SHAPE: -5 elongated: stick, rod, tube … -2 slim … 0 compact: ball, lump, cube … +2 broad … +5 flat: sheet, board, table, plate
- OPEN: -5 closed, a container: box, bag, cup … -2 covered … 0 lid, cover … +2 ajar, partly open … +5 open, an opening: hole, door, window
- STRONG: -5 weak, fragile, helpless … -2 feeble … 0 ordinary … +2 sturdy … +5 strong, powerful, force
- TRUE: -5 false, a lie, fiction … -2 doubtful … 0 seeming, unknown … +2 likely … +5 true, real, exists
- LIGHT: -5 black, dark … -2 dim … 0 grey … +2 pale … +5 white, bright, shining
- COLOR: -5 red … -3 orange … -1 yellow … +1 green … +3 blue … +5 violet (the plain root means colour; light and dark are LIGHT)
- MAKE: make — engage in
- GO: go — change location; move, travel, or proceed, also metaphorically
- NEW: new — not of long duration; having just (or relatively recently) come into being or been made or acquired or discovered
- TAKE: take — carry out
- COME: come — move toward, travel toward something or somebody or approach something or somebody
- STATE: state — the territory occupied by one of the constituent administrative districts of a nation
- GET: get — come into the possession of something concrete or abstract
- USE: use — put into service; make work or employ for a particular purpose or for its inherent or natural purpose
- MAN: man — an adult person who is male (as opposed to a woman)
- WORK: work — activity directed toward making or doing something
- LOOK: look — perceive with attention; direct one's gaze towards
- SUCH: such — of so extreme a degree or extent
- WAY: way — how something is done or how it happens
- PEOPLE: people — (plural) any group of human beings (men or women or children) collectively
- SEEM: seem — give a certain impression or have a certain outward aspect
- OWN: own — belonging to or on behalf of a specified person (especially yourself); preceded by a possessive
- WORLD: world — everything that exists anywhere
- LIFE: life — a characteristic state or mode of living
- BECOME: become — enter or assume a certain state or condition
- TELL: tell — express in words
- SHOW: show — give an exhibition of to an interested audience
- HOUSE: house — a dwelling that serves as living quarters for one or more families
- CALL: call — assign a specified (usually proper) proper name to
- SCHOOL: school — an educational institution
- OLD: old — (used especially of persons) having lived for a relatively long time or attained a specific age
- DAY: day — time for Earth to make a complete rotation on its axis
- NEED: need — require as useful, just, or proper
- TURN: turn — change orientation or direction, also in the abstract sense
- LEAVE: leave — go away from a place
- YEAR: year — a period of time containing 365 (or 366) days
- GREAT: great — relatively large in size or number or extent; larger than others of its kind
- POINT: point — a geometric element that has position but no extension
- ASK: ask — inquire about
- FORM: form — the phonological or orthographic sound or appearance of a word that can be used to describe or identify something
- CHILD: child — a young person of either sex
- END: end — either extremity of something that has length
- PROBLEM: problem — a state of difficulty that needs to be resolved
- AREA: area — a particular geographical region of indefinite boundary (usually serving some special purpose or distinguished by its people or culture or geography)
- WRITE: write — produce a literary work
- HIGH: high — greater than normal in degree or intensity or amount
- SMALL: small — limited or below average in number or quantity or magnitude or extent
- PROGRAM: program — a series of steps to be carried out or goals to be accomplished
- SYSTEM: system — instrumentality that combines interrelated interacting artifacts designed to work as a coherent entity
- HEAD: head — the upper part of the human body or the front part of the body in animals; contains the face and brains
- FOLLOW: follow — to travel behind, go after, come after
- HOLD: hold — keep in a certain state, position, or activity; e.g.,
- AMERICAN: american — of or relating to the United States of America or its people or language or culture
- FACT: fact — a piece of information about circumstances that exist or events that have occurred
- FACE: face — the front of the human head from the forehead to the chin and ear to ear
- KEEP: keep — keep in a certain state, position, or activity; e.g.,
- COURSE: course — education imparted in a series of lessons or meetings
- STAND: stand — be standing; be upright
- GROUP: group — any number of entities (members) considered as a unit
- RUN: run — move fast by using one's feet, with one foot off the ground at any given time
- INTEREST: interest — a sense of concern with and curiosity about someone or something
- LINE: line — a formation of people or things one beside another
- PUT: put — put into a certain place or abstract location
- GENERAL: general — applying to all or most members of a category or group
- SET: set — put into a certain place or abstract location
- RIGHT: right — being or located on or directed toward the side of the body to the east when facing north
- CASE: case — an occurrence of something
- ORDER: order — (often plural) a command given by a superior (e.g., a military or law enforcement officer) that must be obeyed
- FIND: find — come upon, as if by accident; meet with
- CITY: city — a large and densely populated urban area; may include several independent administrative districts
- PRESENT: present — temporal sense; intermediate between past and future; now existing or happening or in consideration
- UNITE: unite — act in concert or unite in a common purpose or belief
- FORCE: force — a powerful effect or influence
- WAR: war — the waging of armed conflict against an enemy
- NUMBER: number — the property possessed by a sum or total or indefinite quantity of units or individuals
- BRING: bring — take something or somebody with oneself somewhere
- INCREASE: increase — become bigger or greater in amount
- PROVIDE: provide — give something useful or necessary to
- GOVERNMENT: government — the organization that is the governing authority of a political unit
- TRY: try — make an effort or attempt
- PLAN: plan — a series of steps to be carried out or goals to be accomplished
- COUNTRY: country — a politically organized body of people under a single government
- RESULT: result — a phenomenon that follows and is caused by some previous phenomenon
- HAND: hand — the (prehensile) extremity of the superior limb
- STUDY: study — a detailed critical inspection
- MEMBER: member — one of the persons who compose a social group (especially individuals who have joined and participate in a group organization)
- WATER: water — binary compound that occurs at room temperature as a clear colorless odorless tasteless liquid; freezes into ice below 0 degrees centigrade and boils above 100 degrees centigrade; widely used as a solvent
- PLAY: play — participate in games or sport
- HELP: help — give help or assistance; be of service
- START: start — take the first step or steps in carrying out an action
- QUESTION: question — an instance of questioning
- NIGHT: night — the time after sunset and before sunrise while it is dark outside
- CHURCH: church — one of the groups of Christians who have their own beliefs and forms of worship
- PUBLIC: public — not private; open to or concerning the people as a whole
- HEAR: hear — perceive (sound) via the auditory sense
- LET: let — make it possible through a specific action or lack of action for something to happen
- WOMAN: woman — an adult female person (as opposed to a man)
- MEAN: mean — mean or intend to express or convey
- WEEK: week — any period of seven consecutive days
- LARGE: large — above average in size or number or quantity or magnitude or extent
- BUSINESS: business — a commercial or industrial enterprise and the people who constitute it
- POWER: power — possession of controlling influence
- FAMILY: family — a social unit living together
- PRESIDENT: president — an executive officer of a firm or corporation
- CLOSE: close — move so that an opening or passage is obstructed; make shut
- YOUNG: young — (used of living things especially persons) in an early period of life or development or growth
- REPORT: report — a written document describing the findings of some individual or group
- EXPERIENCE: experience — the accumulation of knowledge or skill that results from direct participation in events or activities
- ROOM: room — an area within a building enclosed by walls and floor and ceiling
- CAR: car — a motor vehicle with four wheels; usually propelled by an internal combustion engine
- MIND: mind — that which is responsible for one's thoughts and feelings; the seat of the faculty of reason
- BOY: boy — a youthful male person
- NAME: name — a language unit by which a person or thing is known
- SOCIAL: social — relating to human society and its members
- NATIONAL: national — of or relating to or belonging to a nation or country
- MATTER: matter — a vaguely specified concern
- COMPANY: company — an institution created to conduct business
- DEVELOPMENT: development — act of improving by expanding or enlarging or refining
- POSSIBLE: possible — capable of happening or existing
- IMPORTANT: important — of great significance or value
- ACT: act — a legal document codifying the result of deliberations of a committee or society or legislative body
- RETURN: return — go or come back to place, condition, or activity where one has been before
- LEAD: lead — take somebody somewhere
- GIRL: girl — a young woman
- WHITE: white — being of the achromatic color of maximum lightness; having little or no hue owing to reflection of almost all incident light
- EARLY: early — at or near the beginning of a period of time or course of events or before the usual or expected time
- PAY: pay — give money, usually in exchange for goods or services
- ACTION: action — something done (usually as opposed to something said)
- FOOT: foot — the part of the leg of a human being below the ankle joint
- APPEAR: appear — give a certain impression or have a certain outward aspect
- REASON: reason — a rational motive for a belief or action
- KIND: kind — a category of things distinguished by some common characteristic or quality
- SENSE: sense — a general conscious awareness
- DOOR: door — a swinging or sliding barrier that will close the entrance to a room or building or vehicle
- MEET: meet — come together
- FIGURE: figure — a diagram or picture illustrating textual material
- EXAMPLE: example — an item of information that is typical of a class or group
- STUDENT: student — a learner who is enrolled in an educational institution
- CONTINUE: continue — continue a certain state, condition, or activity
- REACH: reach — reach a destination, either real or abstract
- REQUIRE: require — require as useful, just, or proper
- IDEA: idea — the content of cognition; the main thing you are thinking about
- EXPECT: expect — regard something as probable or likely
- BELIEVE: believe — accept as true; take to be true
- PASS: pass — go across or through
- WALK: walk — use one's feet to advance; advance by steps
- TYPE: type — a subdivision of a particular kind of thing
- LITTLE: little — limited or below average in number or quantity or magnitude or extent
- DEVELOP: develop — make something new, such as a product or a mental or artistic creation
- LOVE: love — a strong positive emotion of regard and affection
- MONTH: month — one of the twelve divisions of the calendar year
- SERVICE: service — work done by one person or group that benefits another
- CONSIDER: consider — deem to be
- CONTROL: control — power to direct or determine
- TALK: talk — exchange thoughts; talk with
- SIT: sit — be seated
- NATION: nation — a politically organized body of people under a single government
- REMAIN: remain — stay the same; remain in a certain state
- DIFFERENT: different — unlike in nature or quality or form or degree
- PERIOD: period — an amount of time
- WHOLE: whole — including all components without exception; being one unit or constituting the full amount or extent or duration; complete
- SPEAK: speak — express in speech
- COLLEGE: college — the body of faculty and students of a college
- LEVEL: level — a position on a scale of intensity or amount or quality
- CARRY: carry — move while supporting, either in a vehicle or in one's hands or on one's body
- INDIVIDUAL: individual — a human being
- STREET: street — a thoroughfare (usually including sidewalks) that is lined with buildings
- HOME: home — where you live at a particular time
- JOB: job — the principal activity in your life that you do to earn money
- OFFICE: office — place of business where professional or clerical duties are performed
- SERVE: serve — serve a purpose, role, or function
- HOPE: hope — expect and wish
- LAW: law — the collection of rules imposed by authority
- AGE: age — how long something has existed
- SOUND: sound — the particular auditory effect produced by a given cause
- HUMAN: human — characteristic of humanity
- GROW: grow — pass into a condition gradually, take on a specific property or attribute; become
- HISTORY: history — the aggregate of past events
- BOOK: book — a written work or composition that has been published (printed on pages bound together)
- POSITION: position — the particular portion of space occupied by something
- MOMENT: moment — a particular point in time
- PERSON: person — a human being
- CAUSE: cause — give rise to; cause to happen or occur, not always intentionally
- CLASS: class — a collection of things sharing a common attribute
- CENTER: center — an area that is approximately central within some larger region
- RECEIVE: receive — get something; come into possession of
- ADD: add — make an addition (to); join or combine or unite with others; increase the quality, quantity, size or scope of
- NOTE: note — make mention of
- POLICY: policy — a plan of action adopted by an individual or social group
- LOCAL: local — relating to or applicable to or concerned with the administration of a city or town or district rather than a larger area
- RECORD: record — anything (such as a document or a phonograph record or a photograph) providing permanent evidence of or information about past events
- PROCESS: process — a particular course of action intended to achieve a result
- DEATH: death — the event of dying or departure from life
- METHOD: method — a way of doing something, especially a systematic way; implies an orderly logical arrangement (usually in steps)
- COURT: court — an assembly (including one or more judges) to conduct judicial business
- FREE: free — able to act at will; not hampered; not under compulsion or restraint
- CUT: cut — separate with or as if with an instrument
- WORD: word — a unit of language that native speakers can identify
- SOCIETY: society — an extended social group having a distinctive cultural and economic organization
- ANSWER: answer — a statement (either spoken or written) that is made to reply to a question or request or criticism or accusation
- SUPPORT: support — give moral or psychological support, aid, or courage to
- CONCERN: concern — be relevant to
- PARTY: party — an organization to gain political power
- LOW: low — less than normal in degree or intensity or amount
- READ: read — interpret something that is written or printed
- LOSE: lose — fail to keep or to maintain; cease to have, either physically or in an abstract sense
- DETERMINE: determine — establish after a calculation, investigation, experiment, survey, or study
- ISSUE: issue — an important question that is in dispute and must be settled
- EFFORT: effort — earnest and conscientious activity intended to do or accomplish something
- COMMUNITY: community — a group of people living in a particular local area
- VIEW: view — a way of regarding situations or topics etc.
- FIRE: fire — the event of something burning (often destructive)
- MATERIAL: material — the tangible substance that goes into the makeup of a physical object
- FIELD: field — a piece of land cleared of trees and usually enclosed
- INFORMATION: information — a message received and understood
- VOICE: voice — the distinctive quality or pitch or condition of a person's speech
- COMPLETE: complete — having every necessary or normal part or component or step
- TAX: tax — charge against a citizen's person or property or activity for the support of government
- WAIT: wait — stay in one place and anticipate or expect something
- CLEAR: clear — readily apparent to the mind
- MONEY: money — the most common medium of exchange; functions as legal tender
- SUBJECT: subject — the subject matter of a conversation or discussion
- STOP: stop — come to a halt, stop moving
- SURE: sure — having or feeling no doubt or uncertainty; confident and assured
- TOWN: town — an urban area with a fixed boundary that is smaller than a city
- DRIVE: drive — operate or control a vehicle
- INCLUDE: include — have as a part, be made up out of
- AIR: air — a mixture of gases (especially oxygen) required for breathing; the stuff that the wind consists of
- POLITICAL: political — involving or characteristic of politics or parties or politicians; - Daniel Goleman
- DESIGN: design — the act of working out the form of something (as by making a sketch or outline or plan)
- SECTION: section — a self-contained part of a larger composition (written or musical)
- LEARN: learn — gain knowledge or skills
- COVER: cover — provide with a covering or cause to be covered
- RISE: rise — move upward
- SEND: send — cause to go somewhere
- CENTURY: century — a period of 100 years
- BREAK: break — terminate
- DEPARTMENT: department — a specialized division of a large organization
- SPECIAL: special — unique or specific to a person or thing or category
- BUILD: build — make by combining materials and parts
- REMEMBER: remember — recall knowledge from memory; have a recollection
- WIFE: wife — a married woman; a man's partner in marriage
- BOARD: board — a committee having supervisory powers
- INVOLVE: involve — connect closely and often incriminatingly
- SITUATION: situation — the general state of things; the combination of circumstances at a given time; ; ; - Franklin D.Roosevelt
- COST: cost — the total spent for goods or services including money and time and labor
- FEDERAL: federal — national; especially in reference to the government of the United States as distinct from that of its member units
- MAJOR: major — of greater importance or stature or rank
- UNIVERSITY: university — the body of faculty and students at a university
- AVAILABLE: available — obtainable or accessible and ready for use or service
- STAGE: stage — any distinct time period in a sequence of events
- INDICATE: indicate — be a signal for or a symptom of
- REAL: real — being or occurring in fact or actuality; having verified existence; not illusory; ; ; ; ; ; - Longfellow
- ECONOMIC: economic — of or relating to an economy, the system of production and management of material wealth
- TABLE: table — a set of data arranged in rows and columns

Roots after COLOR are **word roots**: each means just that English word (in any of its common senses) and takes no value. Combine them, give them roles and FORM marks like any other root.

## Form marks

Marks go after the part of speech. They are not roots and do not count toward the limit of 3.

Noun roles turn the meaning into a related noun:
- `agent`: the one who does it, or a person of that field (person or thing). `ART(=+5) | o agent` = artist. `TEXT | o agent` = writer, `HAPPEN | o agent` = cause.
- `tool`: the means or instrument. `TEXT | o tool` = pen, `JOIN(=-4) TOUCH(=+4) | o tool` = knife.
- `result`: what comes out of it. `HAPPEN | o result` = consequence, `TEXT | o result` = a text.
- `quality`: the quality or state itself. `GOOD | o quality` = goodness, `CAN | o quality` = ability.

Grammar marks, each with a value from -5 to +5; not written means unspecified:
- T: tense (-2 past, +2 future).
- R: event before (-3) or after (+3) the reference time.
- A: aspect (-5 beginning … +5 completed).
- N: number (+1 few, +3 plural, +5 all).
- M: negation and probability (-5 not, -3 maybe, +4 certainly).
- C: comparison (-3 less, +3 more, +5 most).
- I: intensity (-5 barely … +4 very, +5 utterly).
- D: definiteness (-3 a, +3 the).
- V: voice (-4 passive, +4 deliberate).
- K: make someone do it (-5 prevent … 0 let … +5 force).
- `!`: command.
- `?`: question.

Write the letter and the value together, without `(=`: `MOVE | i T-2` = moved, `SOMEONE | o N+3 D+3` = the people.

## Phrases

A concept is written as ONE word `{ ROOTS | FORM }`, or as a phrase of up to 3 words: `{ X } LINK { Y }` or
`{ X } LINK { Y } LINK { Z }`. X is the head and carries the part of speech of the whole concept; each next word narrows
the one before it. Every word has its own braces, its own FORM and its own limit of 3 roots. LINK is the first of these
that fits:
- `FROM`: X is made of Y, or comes from Y.
- `FOR`: X is made for Y, used to do Y.
- `AGAINST`: X protects from Y, stops or fights Y.
- `LIKE`: X looks like Y, or is done like Y.
- `PI`: X is part of Y, or is found in Y.

## Quotes

Nothing is quoted: every concept is built from roots.

## Task

`list.md` gives numbered English words (noun, verb or adjective) with their intended sense. For each, write ONE code — one
word, or a phrase of at most 3 words — that lets a reader who knows only the spec above guess the English word (or a word
of the same meaning) most surely. Every word in its own braces `{ ROOTS | FORM }`.

Write `answers.md` with exactly one line per item, same numbering: `N. code`. No other text.
