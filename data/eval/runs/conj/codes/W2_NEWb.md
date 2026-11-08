1. INTENDED: Although the resolution might have been far more specific, it was considerably tougher than the earlier one.
   CODE: THOUGH [ { THINK(=+5) | o result D+3 } { SAME(=-4) | i T-2 C+3 I+3 M-3 } ] ; { THINK(=+5) | o result D+3 } { TOUCH(=+4) | i T-2 C+3 I+3 } { TIME(=-3) THINK(=+5) | o result D+3 }
   READ AS: the decision / might have been rather special / the decision / was fairly harsher / the earlier decision => Although the decision might have seemed rather special, the decision was fairly harsh, the earlier one.
2. INTENDED: An assistant attorney general is directed to investigate.
   CODE: { RULE(=+4) DO | o agent D-3 } { RULE(=+4) | o agent } { JOIN KNOW | o agent D-3 } { SEE KNOW | i V-4 T-1 } { SEE KNOW(=+2) | i V+4 T2 }
   READ AS: an administrator / an authority / a compiler of knowledge / were just recognized / will deliberately make known => An administrator, an authority, and a compiler of knowledge were just recognized, and they will deliberately make it known.
3. INTENDED: Costs were held down, despite a bitter winter.
   CODE: { VALUE(=-5) | o N+3 D+3 } { CARE | i T-2 V-4 } ; THOUGH [ { HEAT(=-5) TIME | o D-3 } { GOOD(=-5) | a } ]
   READ AS: the bargains / were looked after / a cold spell / terrible => The bargains were looked after, though the cold spell was terrible.
4. INTENDED: The year will probably start out with segregation still the most troublesome issue.
   CODE: { TIME(=+1) | o D+3 } { BEGIN(=-5) | i T2 M+2 } LA [ { RULE(=+4) PART | o D+3 } { SAME(=-4) JOIN(=-5) | o } { CAN(=-3) GOOD(=-4) | a C+5 } { HAPPEN | o } ]
   READ AS: the near future / will probably start / a member of an institution / a special separation / the most difficult / an event => The near future will probably start when a member of an institution faces a special separation, the most difficult event.
5. INTENDED: Gilman started talking to him until he saw his chance.
   CODE: { SOMEONE(=-5) | o } { SAY | i T-2 A-5 } E { SOMEONE(=-5) | o } LA [ { SOMEONE(=-5) | o } { SEE | i T-2 } E { CAN TIME | o D+3 } ]
   READ AS: they / began to say / them / they / saw / the chance => They began to tell them when they saw the chance.
6. INTENDED: The inclination was to accept the statement that there would be no formal negotiations.
   CODE: { WANT | o quality D+3 } { WANT(=+3) | i T-2 } { GIVE(=+3) CONSUME | i } E { SAY | o result D+3 } [ { RULE(=+5) SAY | o N+3 M-5 } ]
   READ AS: the desire / wanted / to receive / the statement / unspoken official rules => The desire wanted to receive the statement of unspoken official rules.
7. INTENDED: She had, she said, heard that the plant was closing.
   CODE: { SOMEONE(=-5) | o } { SAY | i T-2 } E [ { SOMEONE(=-5) | o } { CONSUME SAY(=+1) | i T-2 } E [ { PLACE THING(=0) DO | o D+3 } { BEGIN(=+5) | i T2 A-5 } ] ]
   READ AS: they / said / them / heard / the farm / will begin to end => They said to them that they had heard the farm will begin to close.
8. INTENDED: But in the moment of truth everyone could see that the U.S. was in reality the principal.
   CODE: BUT { MANY(=+5) SOMEONE | o } { CAN SEE | i T-2 } E [ { LAND SOMEONE(=+5) RULE | o D+3 } { SAME(=+5) VALUE | i T-2 } ] LA [ { TIME VALUE(=+5) | o D+3 } ]
   READ AS: everyone / could see / the law of my land / was of equal value / the precious time => But everyone could see that the law of my land was equally valued at the precious time.
9. INTENDED: There apparently is no school of propaganda or psychological warfare.
   CODE: { SEE | e } { RULE(=+4) KNOW | o D-3 M-5 } { KNOW ART(=+5) | o } AND { FIGHT KNOW | o } { HAPPEN | i }
   READ AS: clearly / an unofficial body of knowledge / the humanities / a conflict over knowledge / happens => Clearly, an unofficial body of knowledge, the humanities, and a conflict over knowledge happen.
10. INTENDED: If either one ever started making promises, there is no telling where the promises would end.
   CODE: IF [ { SAME SOMEONE | o } { BEGIN(=-5) | i } { MANY(=+5) TIME | e } { SAY | o N+3 } ] ; { CAN KNOW | i M-5 } { PLACE | o D+3 } [ { SAY | o N+3 D+3 } { BEGIN(=+5) | i T2 } ]
   READ AS: the same person / begins / always / statements / cannot know / the place / the statements / will end => If the same person always begins making statements, one cannot know the place where the statements will end.
11. INTENDED: But the farmers outsmarted Washington by shortening the distance between the rows and pouring on the fertilizer.
   CODE: BUT { THING FIGHT | o agent N+3 } { KNOW | i T-2 C+3 } E { LAND RULE(=+4) | o D+3 } { DO | i V+4 } [ { NEAR(=-2) | o D+3 } { PART(=-2) | o N+3 } { BIG(=-3) | i K+4 } ] AND { THING(=0) GOOD GRAIN | o } { GIVE(=+5) JOIN | i T-2 }
   READ AS: the fighting creatures / knew better / the state / acts deliberately / the neighborhood / members / forced to shrink / crops / gave => But the fighting creatures knew better than to deliberately act against the state, forcing its neighborhood members to shrink, and they gave up crops.
12. INTENDED: Heels place emphasis on the long legged silhouette.
   CODE: { BODY LONG ABOVE | o N+3 } { GIVE(=+5) | i } E { VALUE(=+5) | o } { BODY LONG(=+3) | o D+3 } { BODY BIG | a }
   READ AS: the arms / give / precious things / the limb / massive => The arms give precious things to the massive limb.
13. INTENDED: He was above all a friend seeker, almost pathetic in his eagerness to be liked.
   CODE: { SOMEONE(=-5) | o } { SAME(=+5) FRIEND | i T-2 } { MANY(=+5) | e } { WANT FRIEND | o agent } { WANT FEEL(=+4) | i T-2 I+3 } ; { FEEL(=+4) WANT | o quality } { WANT(=+5) | i V-4 }
   READ AS: they / were all friends / always / a lover / craved excitement / passion / is loved => They were always all friends; a lover craved excitement, and passion is loved.
14. INTENDED: Not all the concern for health is well directed.
   CODE: { MANY(=+5) | a M-5 } { CARE BODY LIVE | o D+3 } { GOOD DO | i V-4 M-5 }
   READ AS: not all / the healthcare / is not done well => Not all healthcare is done well.
15. INTENDED: I must say, however, that I preferred the acting that had something of a biting edge to it.
   CODE: { SOMEONE(=+5) | o } { SAY | i } E [ { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 C+3 } E { ART(=+5) DO | o D+3 } [ { TOUCH(=+3) HEAT | o D-3 } { SAME | i } ] ] ; BUT { MOOD(=0) | e }
   READ AS: I / say / me / wanted more / the arts / a harsh heat / is the same / seriously => I tell myself that I wanted more of the arts, where a harsh heat is the same, but seriously.
16. INTENDED: There is fear in the fifties as his title suggests and as his competent drawings show.
   CODE: { FEEL(=-3) | o D-3 } { TIME(=+0) INSIDE | o N+3 D+3 } BECAUSE [ { TEXT | o D+3 } { SEE | i V+4 } ] AND [ { ART SEE | o N+3 } { CAN | i V+4 } ]
   READ AS: a subdued feeling / the present inner moments / the text / deliberately see / art viewers / can deliberately => A subdued feeling fills the present inner moments, because one deliberately reads the text, and art viewers can do so deliberately.
17. INTENDED: So I started making some calls of my own.
   CODE: SO { SOMEONE(=+5) | o } { BEGIN(=-5) | i T-2 } { DO | i } E { SAY SOMEONE(=+5) | o N+3 }
   READ AS: I / began / carry out / my words => So I began to carry out my words.
18. INTENDED: Clever light songs were overly coy, tragic songs a little too melodramatic.
   CODE: { GOOD KNOW | a } { MOOD(=+3) ART | o N+3 } { MOOD(=+5) | i T-2 I+3 } ; { MOOD(=-5) ART | o N+3 } { MOOD(=-5) | i T-2 I+3 } { FEEL(=+4) | e C+3 }
   READ AS: well-informed / cheerful arts / was quite funny / tragic arts / was quite tragic / more intensely => Well-informed, one sees that cheerful arts were quite funny and tragic arts were quite tragic, even more intensely.
19. INTENDED: For arm and shoulder strength a chinning bar is recommended.
   CODE: { BODY | o N+3 } { BODY | o } { TOUCH(=+4) | o quality } FOR { LONG(=+5) | o tool } { GOOD DO | i V-4 }
   READ AS: bodies / body / hardness / a beam / is well done => Bodies and body hardness, made for a beam, are well done.
20. INTENDED: Rodding formulas apply to many phases of the sport.
   CODE: { DO | o tool N+3 } { MANY(=+3) | a } { PART(=-2) | o N+3 } { FIGHT(=-5) | o } { JOIN | i }
   READ AS: tools / many / members / a game / join => Many tools and members join a game.
21. INTENDED: Place sleeve seam at center underarm and center of sleeve cap at shoulder seam.
   CODE: { JOIN | i ! } E { LONG(=-5) | o } PI { NEAR BODY | o } { NEAR | o } AND { LONG(=-5) JOIN | o } { PART | o } PI { BODY ABOVE | o }
   READ AS: join / the thread / the nearby body / its vicinity / the stitching / part / the upper body => Join the thread that is part of the nearby body and its vicinity, and the stitching part of the upper body.
22. INTENDED: Another reason gymnastic study is valuable is that it can be started very early in life.
   CODE: { THINK(=+5) KNOW(=+5) | o D+3 } { VALUE(=+5) | i } BECAUSE { KNOW ART(=-5) BODY | o } { CAN | i } { BEGIN(=-5) | i V-4 } { TIME(=-5) LIVE(=+5) | e I+4 }
   READ AS: the informed decision / matters / physiology / can / be started / very long-lived => The informed decision matters because physiology can be started and lasts very long.
23. INTENDED: Close behind the plane of the tappets are the locking bars.
   CODE: { SIDE(=-5) NEAR | e } { PLACE SIDE | o } { LONG(=+5) JOIN | o N+3 } { HAPPEN | i }
   READ AS: just behind / the back / beams / happen => Beams happen just behind, at the back.
24. INTENDED: Here is a word of advice when you go shopping for your pansy seeds.
   CODE: { SIDE(=+5) NEAR(=+5) | e } { KNOW | o D-3 } { GIVE(=+5) KNOW | i } LA [ { SOMEONE(=+3) | o } { VALUE(=-5) MOVE | i } ] { THING(=0) GRAIN(=0) | o N+3 }
   READ AS: directly ahead / a piece of knowledge / informs / you / trade / crops => Directly ahead, a piece of knowledge informs you when you trade crops.
25. INTENDED: Here you can pick up a taxi or public transport to return to the center of the city.
   CODE: { NEAR(=+5) | e } { SOMEONE(=+3) | o } { CAN | i } { GIVE(=0) | i } E { MOVE(=+3) | o tool D-3 } OR { RULE(=+4) MOVE | o tool } LA [ { MOVE(=-5) SIDE(=-5) | i } { NEAR(=+5) | o D+3 } PI { PLACE BIG | o } ]
   READ AS: here / you / can / exchange / a vehicle / an official vehicle / step back / the nearby area / a big place => Here, you can exchange a vehicle or an official vehicle when you step back from the nearby area, which is part of a big place.
26. INTENDED: We passed his house and school on the way.
   CODE: { SOMEONE(=-5) | o } { MOVE | i T-2 } E { PLACE INSIDE(=+5) LIVE | o D+3 } AND { PLACE KNOW | o } { SOMEONE(=-5) | o }
   READ AS: they / moved / the home / a school / others => They moved the home and a school, along with others.
27. INTENDED: They adopted a program by which Louisiana was divided into five districts.
   CODE: { SOMEONE(=-5) | o N+3 } { SAME(=+3) DO | i T-2 } E { RULE(=+3) DO | o D-3 } [ { PART(=-2) | i T-2 V-4 } E { LAND | o D+3 } { MANY(=-1) | o } ]
   READ AS: others / acted in the usual way / an official act / was divided / the land / few => Others acted in the usual way, carrying out an official act by which the land was divided, though few.
28. INTENDED: What happened is that Negroes want to be treated like men.
   CODE: { HAPPEN | o result D+3 } { SAME | i } [ { SOMEONE(=-5) | o } { WANT | i } { SAME LIVE SOMEONE(=+3) | o N+3 } ]
   READ AS: the consequence / remains the same / they / want / people like you => The consequence remains the same, since they want people like you.
29. INTENDED: But it is not really only a conversation.
   CODE: BUT { SAY | o } { SAME(=+5) | i M-5 } { SAME | e I+4 }
   READ AS: speech / is not identical / very similarly => But speech is not identical, yet is very similar.
30. INTENDED: A group of sailors announced to Hudson that they would sail no farther.
   CODE: { PART(=+5) SOMEONE | o D-3 } { MOVE LAND(=-5) | o agent N+3 } { SAY | i T-2 } E [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T2 M-5 } { NEAR(=-5) | e C+3 } ]
   READ AS: a crowd / sailors / said / they / will not sail / farther => A crowd of sailors said to them that they will not sail farther.
31. INTENDED: One cannot speak anymore of being, one must speak only of the mess.
   CODE: { KNOW | o } { SAY | i M-5 } { TIME(=+0) | e } ; { SOMEONE(=+3) | o } { SAY | i } E [ { SOMEONE(=+3) GOOD(=-5) | o } ]
   READ AS: knowledge / does not say / now / you / tell / terrible people => Knowledge is not spoken of now, and you tell terrible people.
32. INTENDED: He could have been blackmailed, or his family might have been threatened.
   CODE: { SOMEONE(=-5) | o } { FRIEND(=-5) DO | i T-2 M-3 V-4 } E { SOMEONE(=-5) | o } OR { PART SOMEONE(=-5) | o } { FRIEND(=-5) | i T-2 M-3 V-4 }
   READ AS: they / might be mistreated / them / some of them / might be hated => They might have been treated cruelly, or some of them might have been hated.
33. INTENDED: They look as if they had been sculptured with an unsharpened chisel.
   CODE: { SEE | i } { SAME(=+3) | e } LIKE [ { SOMEONE(=-5) | o } { ART DO | i T-2 R-3 V-4 } { LONG(=-2) TOUCH(=-5) | o tool } { TOUCH(=-5) | a } ]
   READ AS: see / usually / they / had been crafted earlier / a soft thread / soft => One usually sees them, as they had been crafted earlier with a soft thread that was soft.
34. INTENDED: Such is the field for exercising our reverence.
   CODE: { SAME(=+5) | i } { PLACE ART | o D+3 } FOR { DO | i } { VALUE(=+5) | o D+3 } { SOMEONE(=+5) | o N+3 }
   READ AS: is the same / the studio / doing / the precious thing / us => The studio is the same, made for doing the precious thing for us.
35. INTENDED: Driven from the marketplace by the course of history, our hero disguises himself as a private detective.
   CODE: { SOMEONE(=-5) | o } { PLACE VALUE(=-5) | o } { MOVE(=+4) | i V-4 T-2 } { TIME(=-5) | o D+3 } { WANT(=+5) | o } { SOMEONE | o D+3 } { CHANGE SAME(=-5) | i } { SEE KNOW | o agent } { RULE(=-5) | a }
   READ AS: they / a market / were rushed / the old times / love / the one / changes into something different / a witness / informal => In the old times they were rushed at a market, and love for the one changed into something different, with an informal witness watching.
36. INTENDED: For it was neglected, not to say nascent, when the struggle began.
   CODE: BECAUSE { CARE(=-5) | i V-4 T-2 } { BEGIN(=-5) | a } LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ]
   READ AS: were neglected / initial / the fight / began => Because they were neglected at the start, when the fight began.
37. INTENDED: A valve in the handle let us cut the pressure still lower.
   CODE: { PART(=-2) | o } PI { BODY LONG | o D+3 } { CAN | i T-2 K0 } E { SOMEONE(=+5) | o N+3 } { JOIN(=-5) | i } { MEASURE(=-5) HEAT | o } { BIG(=-3) | e C+3 }
   READ AS: a part / the limb / could let / us / separate / the amount of heat / smaller => A part of the limb could let us separate the amount of heat, to a smaller degree.
38. INTENDED: These drugs have no effect on the iodide concentrating mechanism, but they inhibit organification.
   CODE: { DO GIVE(=-5) | o N+3 } { DO | i M-5 } E { MEASURE(=-5) "iodide" | o } ; BUT { SOMEONE(=-5) | o } { JOIN(=-5) | i } E { DO | o }
   READ AS: thefts / do not / the amount of iodide / they / remove / a deed => Thefts do not take the amount of iodide, but they remove the deed.
39. INTENDED: It is believed that drug therapy and electroshock involve the former and psychotherapy the latter mechanism.
   CODE: { THINK | i V-4 } E [ { DO GIVE(=+5) GOOD | o } AND { HEAT ART | o } { SAME | i } E { SAME(=-5) | o D+3 } AND { THINK ART | o } { SAME | i } E { SAME(=-5) | o D+3 } ]
   READ AS: is thought / charity / heating technology / match / the opposite / philosophy / match / the opposite => It is thought that charity and heating technology match the opposite, and philosophy matches the opposite.
40. INTENDED: They were inadequately financed, without experienced leadership, and lacked the general support of organized labor as a whole.
   CODE: { SOMEONE(=-5) | o } { VALUE(=-5) GIVE | i T-2 V-4 I+3 } AND { KNOW GOOD SOMEONE | a M-5 } AND { WANT(=+3) | i T-2 M-5 } E { MANY(=+3) FRIEND | o } PI { PART SOMEONE | o N+3 }
   READ AS: they / were cheaply traded / unknown / did not want / many friends / other people => They were cheaply traded and unknown, and did not want many friends among other people.
41. INTENDED: So as the years passed, I saw them each time in the light of an accelerated personal conflagration.
   CODE: SO LA [ { TIME | o N+3 } { MOVE | i T-2 } ] { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY(=+5) TIME | e } LA [ { HEAT(=+5) FIGHT | o } { SOMEONE(=+5) | o } { TIME(=+1) CHANGE | a C+3 } ]
   READ AS: times / passed / I / saw / them / always / a hot war / me / more imminent => So, as times passed, I saw them always, when a hot war with me grew more imminent.
42. INTENDED: It was not always easy to develop theory and doctrine which would square the two conditions.
   CODE: { CAN(=-3) | i T-2 M-5 } { MANY(=+5) TIME | e } { DO | i } E { KNOW | o } AND { RULE | o } [ { SAME(=+3) JOIN | i T2 } E { SAME(=+5) PART(=-2) | o } ]
   READ AS: could not easily / always / act / knowledge / authority / will typically join / the same member => One could not easily always act on knowledge and authority, which will typically join the same member.
43. INTENDED: The Skopas people seemed to him of that breed of human beings whose insularity frees them from tragedy.
   CODE: { SOMEONE(=-5) | o } { SEE | i T-2 } E { SOMEONE PART | o N+3 } { SAME(=+3) THING SOMEONE | a } ; { PLACE LAND(=-5) | o quality } { JOIN(=-5) | i } E { SOMEONE(=-5) | o } { MOOD(=-5) | o }
   READ AS: they / saw / groups of people / ordinary / the maritime quality / separate / others / tragedy => They saw groups of ordinary people; the maritime quality separates others from tragedy.
44. INTENDED: The boy was becoming acquainted with the contadini families that brought produce into Rome.
   CODE: { LIVE SOMEONE(=-5) | o D+3 } { KNOW | i T-2 A-5 } E { PART SOMEONE | o N+3 } "Rome" AND { THING(=0) GIVE | i T-2 }
   READ AS: the living others / began to know / some people / supplied => The living others began to know some people in Rome, and supplied them.
45. INTENDED: All pricks like Coughlin run it anyway, one way or another.
   CODE: { MANY(=+5) | o } { WANT SOMEONE(=+5) FRIEND(=-5) | o N+3 } { RULE(=-5) DO | i } E { SAME(=+5) | o } { SAME(=-5) | e } { TIME(=+0) | e }
   READ AS: all / my hostile desires / act informally / identity / differently / now => All my hostile desires act informally on identity, differently, now.
46. INTENDED: But the liaison successfully started in the last days of autumn was now languishing.
   CODE: BUT { WANT FRIEND | o D+3 } { BEGIN(=-5) GOOD | i T-2 } { TIME(=-1) | e } { LIVE | e C-3 } { TIME(=-1) | o N+3 } { HEAT(=-3) TIME | o } { TIME(=+0) | e } { LIVE(=-3) | i T-1 }
   READ AS: the affection / began well / just now / less lively / recent times / the cool season / now / have just gone dormant => But the affection began well just now, and recent times in the cool season are now less lively and have just gone dormant.
47. INTENDED: And indeed the young garden beans were brackish in her mouth.
   CODE: { THING(=0) GOOD | o N+3 } { TIME(=-3) LIVE(=+5) | a } { TOUCH(=+4) GOOD(=-5) CONSUME | i T-2 } { INSIDE(=+5) BODY | o } { SOMEONE(=-5) | o }
   READ AS: good plants / formerly living / were consumed harshly / the internal body / they => Good plants, once living, were harshly consumed by their internal bodies.
48. INTENDED: Top dog, sleeping and eating right there with the Staff.
   CODE: { BIG SOMEONE | o } { LIVE(=-2) AND CONSUME | i } { NEAR(=+5) | e } { JOIN | e } { SOMEONE PART | o N+3 }
   READ AS: a big person / sleeps and eats / nearby / together / groups of people => A big person sleeps and eats nearby, together with groups of people.
49. INTENDED: Actually, she had hated him before she ever saw him.
   CODE: { SAME(=+5) | e } { SOMEONE(=-5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=-5) | o } LA [ { SOMEONE(=-5) | o } { SEE | i T-2 M-5 } E { SOMEONE(=-5) | o } ]
   READ AS: exactly / they / hated / them / they / did not see / them => Exactly when they did not see them, they hated them.
50. INTENDED: His face pale, Summers headed for the street.
   CODE: { SOMEONE(=-5) BODY | o } { LIVE(=-2) | a } ; "Summers" { MOVE | i T-2 SIDE(=+5) } E { PLACE MOVE | o D+3 }
   READ AS: their bodies / asleep / moved forward / the depot => Their bodies are asleep; Summers moved forward toward the depot.
51. INTENDED: A time before the white lightning and the bumming had turned him inside out.
   CODE: { TIME(=-3) | o } LA [ { HEAT GRAIN | o } AND { WANT(=-5) VALUE(=-5) | o } { CHANGE | i T-2 } E { SOMEONE(=-5) | o } { INSIDE(=-5) | a } ]
   READ AS: the earlier time / hot grains / scorn for cheapness / changed / them / outside => In the earlier time, when hot grains and scorn for cheapness changed them, they were outside.
52. INTENDED: He was dead before he hit the ground.
   CODE: { SOMEONE(=-5) | o } { LIVE(=-5) | i T-2 } LA [ { TIME(=-1) | o } { SOMEONE(=-5) | o } { TOUCH | i T-2 } E { LAND(=+5) | o D+3 } ]
   READ AS: they / died / a moment ago / they / touched / the ground => They died when, a moment ago, they touched the ground.
53. INTENDED: A lantern hung from a peg, giving light.
   CODE: { HEAT GRAIN | o tool D-3 } { LONG(=0) | o } { MOVE(=-5) ABOVE | i T-2 } ; { GIVE(=+5) | i } E { HEAT SEE | o }
   READ AS: a heater / a wire / were lowered / give / a view of heat => A heater and a wire were lowered, and they give a view of heat.
54. INTENDED: From the way the wound in his head was itching, Dan knew that it would heal.
   CODE: BECAUSE [ { PART(=-2) BODY | o D+3 } { TOUCH(=-5) | i T-2 } ] { SOMEONE(=-5) | o } { KNOW | i T-2 } E [ { PART(=-2) BODY | o D+3 } { LIVE | i T2 } ]
   READ AS: the limb / was touched gently / they / knew / the limb / will live => Because the limb was touched gently, they knew the limb would live.
55. INTENDED: He was disappointed to find a nervous, scrawny woman with a big hat standing at the door.
   CODE: { SOMEONE(=-5) | o } { WANT(=-5) GOOD | i T-2 V-4 } LA [ { SOMEONE(=-5) | o } { SEE | i T-2 } E { SOMEONE | o D-3 } [ { FEEL(=+4) | a } AND { BIG(=-4) BODY | a } { BIG | i } { HEAT(=-3) LONG | o } PI { BODY | o } { MOVE(=-5) PLACE | i } { NEAR | e } { PLACE INSIDE LAND | o } ] ]
   READ AS: they / were despised / they / saw / a person / excited / small-bodied / grew / a cool thread / the body / stopped / nearby / the inland area => They were despised when they saw an excited, small-bodied person grow, with a cool thread in the body, and stop nearby in the inland area.
56. INTENDED: Extending her fingers another inch, she caught up the shorts, and swiftly left the room.
   CODE: { MOVE(=+3) | i } E { PART(=-2) BODY | o D+3 } [ { PART SOMEONE(=-5) | o N+3 } ] ; { SOMEONE(=-5) | o } { GIVE(=-5) | i T-2 } E { LONG | o tool N+3 } AND { MOVE(=+4) | i T-2 } { SIDE(=-5) | e } { PLACE INSIDE LIVE | o D+3 }
   READ AS: hurry / the limb / their members / they / seized / cords / hurried / back / the home => Hurry the limb, their members; they seized cords and hurried back to the home.
57. INTENDED: In the street the traffic was really frightening.
   CODE: { PLACE MOVE | o D+3 } { MOVE | o N+3 D+3 } { FEEL(=+4) GOOD(=-5) | i T-2 I+3 }
   READ AS: the station / the moves / felt intensely bad => The moves at the station felt intensely bad.
58. INTENDED: He then offered his own estimate of the weather, which was unenthusiastic.
   CODE: { SOMEONE(=-5) | o } { GIVE(=+5) KNOW | i T-2 } E { SOMEONE(=-5) | o } { THINK | o result } [ { HEAT TIME | o D+3 } ] [ { SAME | i T-2 } { WANT FEEL(=-3) | a } ]
   READ AS: they / taught / them / an idea / the summer / were the same / content => They taught them an idea about the summer, and they were alike and content.
59. INTENDED: No price is too high when true love is at stake.
   CODE: { VALUE | o D-3 } { BIG | i M-5 } LA [ { SAME(=+5) WANT(=+5) | o } { HAPPEN | i } { LIVE | i } ]
   READ AS: a value / does not grow / perfect love / happens / lives => A value does not grow when perfect love happens and lives.
60. INTENDED: He muttered, and took off, obviously feeling like a fool.
   CODE: { SOMEONE(=-5) | o } { SAY(=-3) | i T-2 } AND { MOVE | i T-2 SIDE(=-5) } ; { SEE | e M+4 } { FEEL | i } E { KNOW(=-5) | o }
   READ AS: they / murmured / returned / certainly / feel / folly => They murmured and returned; certainly, they feel folly.
---
1. THOUGH [ { THINK(=+5) | o result D+3 } { SAME(=-4) | i T-2 C+3 I+4 M-3 } ] ; { THINK(=+5) | o result D+3 } { TOUCH(=+4) | i T-2 C+3 I+3 } { TIME(=-3) THINK(=+5) | o result D+3 }
2. { JOIN DO | o agent D-3 } PI { RULE(=+5) | o agent D+3 } { DO | i V-4 K+5 } E [ { SEE CARE KNOW | i } ]
3. { VALUE | o N+3 D+3 } { ABOVE(=-3) CARE | i T-2 V-4 } ; THOUGH [ { HEAT(=-5) TIME | o D-3 } { TOUCH(=+4) | a } ]
4. { BIG TIME | o D+3 } { BEGIN(=-5) | i T2 M+2 } ; { JOIN(=-5) SOMEONE | o quality D+3 } { CAN(=-3) HAPPEN | i C+5 } { BEGIN(=0) | e }
5. "Gilman" { SAY | i T-2 A-5 } E { SOMEONE(=-5) | o } LA [ { SOMEONE(=-5) | o } { SEE | i T-2 A+5 } E { CAN TIME | o D+3 } ]
6. { WANT | o quality D+3 } { GIVE | i T-2 } E { SAY | o result D+3 } [ { RULE(=+4) SAY GIVE | o N+3 } { HAPPEN | i T2 M-5 } ]
7. { SEX(=-5) SOMEONE | o } { SAY | i T-2 } E [ { SEX(=-5) SOMEONE | o } { CONSUME SAY(=+1) | i T-2 R-3 } E [ { PLACE DO | o D+3 } { BEGIN(=+5) | i T2 A-5 } ] ]
8. BUT { MANY(=+5) SOMEONE | o } { CAN SEE | i T-2 } E [ "U.S." { SAME(=+5) | e } { VALUE(=+5) | i T-2 C+5 } ] LA [ { TIME VALUE(=+5) SAME(=+5) | o D+3 } ]
9. { SEE | e I-3 } { PLACE KNOW | o D-3 } FOR { SAY THINK | o } AND { FIGHT THINK | o } { LIVE | i M-5 }
10. IF [ { SOMEONE | o } { BEGIN(=-5) | i } { MANY(=+5) TIME | e } { SAY TIME(=+2) DO | o N+3 } ] ; { CAN KNOW | i M-5 } { PLACE | o D+3 } [ { SAY TIME(=+2) DO | o N+3 D+3 } { BEGIN(=+5) | i T2 } ]
11. BUT { THING(=0) DO | o agent N+3 D+3 } { KNOW | i T-2 C+3 } E "Washington" BECAUSE { SOMEONE(=-5) | o } { CHANGE BIG(=-3) | i T-2 } E { MEASURE(=-5) NEAR(=-5) | o D+3 } PI { LONG LAND | o N+3 D+3 } AND { GIVE(=+5) | i T-2 } E { LAND GOOD GRAIN | o }
12. { PART(=-2) BODY SIDE(=-5) | o N+3 D+3 } { VALUE(=+5) DO | i } E { SEE | o result D+3 } PI { BODY ABOVE(=-5) LONG | o N+3 }
13. { SOMEONE(=-5) | o } { WANT(=+3) FRIEND | i T-2 } { ABOVE MANY | e } ; { SOMEONE(=-5) | o } { MOOD(=-3) | i T-2 I+2 } BECAUSE { SOMEONE(=-5) | o } { FEEL(=+4) WANT(=+5) | i T-2 } E [ { SOMEONE(=-5) | o } { WANT | i V-4 } ]
14. { MANY(=+5) | a M-5 } { CARE BODY LIVE | o D+3 } { GOOD RULE | i V-4 }
15. BUT { SOMEONE(=+5) | o } { SAY | i V+4 } E [ { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 C+3 } E { ART DO | o D+3 } [ { TOUCH(=+4) INSIDE(=0) | a } ] ]
16. { FEEL(=+3) GOOD(=-4) | o D-3 } { LIVE | i } PI { TIME | o N+3 D+3 } "50" ; { TEXT | o D+3 } { SAY | i } AND { ART SEE | o result N+3 D+3 } { DO SEE | i }
17. SO { SOMEONE(=+5) | o } { DO | i T-2 A-5 } E { SAY NEAR(=-5) | o N+3 }
18. { KNOW(=+3) | a } { MOOD(=+3) ART SAY | o N+3 D+3 } { FEEL(=+4) | i T-2 I+4 } ; { MOOD(=-5) ART SAY | o N+3 D+3 } { FEEL(=+4) MOOD(=-5) | i T-2 I+2 }
19. { LONG(=0) | o D-3 } FOR { TOUCH(=+4) PART BODY | o quality } { SAY GOOD | i V-4 }
20. { RULE(=0) ART(=-5) | o N+3 } { SAME(=+3) | i } E { MANY(=+3) | a } { PART(=-2) | o N+3 } PI { FIGHT(=-5) | o D+3 }
21. { JOIN | i ! } E { LONG(=-5) JOIN | o D+3 } PI { LONG(=-5) BODY | o } { INSIDE(=0) | e } { NEAR(=+5) BODY ABOVE(=-5) | o } AND { PLACE NEAR(=+5) | o D+3 } PI { LONG(=-5) BODY | o } { INSIDE(=0) | e } { LONG(=-5) JOIN | o } PI { BODY ABOVE | o }
22. { KNOW BODY MOVE | o D+3 } { VALUE(=+5) | i } BECAUSE { KNOW BODY MOVE | o D+3 } { CAN | i } { BEGIN(=-5) | i V-4 } { BEGIN(=-5) LIVE | e I+4 }
23. { LONG(=0) JOIN | o N+3 D+3 } { PLACE | i } { NEAR(=+3) SIDE(=-5) | e } { INSIDE(=0) | o D+3 } PI { PART(=-2) MOVE | o N+3 D+3 }
24. { NEAR(=+5) | e } { SAY KNOW | o D-3 } { PLACE | i } LA [ { SOMEONE(=+3) | o } { VALUE(=-5) MOVE | i } E { GRAIN THING(=0) | o N+3 } PI "Viola" ]
25. { NEAR(=+5) | e } { SOMEONE(=+3) | o } { CAN | i } { GIVE(=0) | i } E { MOVE(=+3) | o tool D-3 } OR { RULE(=+4) MOVE | o tool } SO { SOMEONE(=+3) | o } { MOVE SIDE(=-5) | i } E { NEAR(=+5) | o D+3 } PI { PLACE SOMEONE BIG | o D+3 }
26. { SOMEONE(=+5) | o N+3 } { MOVE NEAR | i T-2 } E { PLACE INSIDE(=+5) LIVE | o D+3 } AND { PLACE KNOW | o }
27. { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 } E { RULE(=+4) DO | o D-3 } [ "Louisiana" { PART | i T-2 V-4 } E "5" { PART(=-2) LAND | o N+3 } ]
28. { HAPPEN | o result D+3 } { SAME(=+5) | i } [ "Negroes" { WANT | i } E { FRIEND | o quality } LIKE { SEX(=+5) SOMEONE | o N+3 } ]
29. BUT { SAY JOIN | o D-3 } { SAME(=+5) | e } { SAME(=+5) | i M-5 }
30. { PART(=+5) | o D-3 } FROM { MOVE LAND(=-5) | o agent N+3 } { SAY(=+3) | i T-2 } "Hudson" E [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T2 M-5 } { NEAR(=-5) | e C+3 } ]
31. { SOMEONE | o } { TIME(=0) | e } { SAY | i M-5 } E { LIVE | o quality } ; { SOMEONE | o } { SAY | i V+4 } E { CARE(=-5) | o quality D+3 }
32. { SOMEONE(=-5) | o } { FRIEND(=-5) SAY | i T-2 M-3 V-4 K+5 } OR { PART(=+2) SOMEONE(=-5) | o D+3 } { FRIEND(=-5) SAY | i T-2 M-3 V-4 }
33. { SOMEONE(=-5) | o N+3 } { SEE | i V-4 } LIKE [ { SOMEONE(=-5) | o } { ART DO | i T-2 R-3 V-4 } { ART DO | o tool } { JOIN(=-4) | a M-5 } ]
34. { SAME(=+5) | i } { PLACE LAND | o D+3 } FOR { DO VALUE(=+5) | o quality } PI { SOMEONE(=+5) | o N+3 }
35. { GOOD(=+5) SOMEONE | o D+3 } { CHANGE SEE | i V+4 } E { RULE(=-5) SEE KNOW | o agent D-3 } BECAUSE { HAPPEN TIME(=-5) | o D+3 } { MOVE(=+4) INSIDE(=-5) | i T-2 } E { GOOD(=+5) SOMEONE | o D+3 } PI { PLACE VALUE(=-5) | o D+3 }
36. BECAUSE { THING(=-5) | o D+3 } { CARE(=-5) | i T-2 V-4 } AND { BEGIN(=-5) | a } LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ]
37. { JOIN(=-4) GRAIN(=-3) | o tool D-3 } PI { LONG | o D+3 } { CAN | i T-2 K0 } E [ { SOMEONE(=+5) | o N+3 } { JOIN(=-5) | i } E { MEASURE(=-5) TOUCH(=+4) | o D+3 } { ABOVE(=-3) | e C+3 } ]
38. { CHANGE BODY GRAIN | o N+3 D+3 } { CHANGE | i M-5 } E { DO JOIN | o D+3 } FOR "iodide" ; BUT { SOMEONE(=-5) | o N+3 } { DO | i K-5 } E { CHANGE LIVE | o quality }
39. { THINK | i V-4 } E [ { CARE BODY GRAIN | o } AND { FEEL(=+5) ART(=-5) | o } { JOIN | i } E { SIDE(=+5) DO | o D+3 } ; { CARE THINK | o } { JOIN | i } E { SIDE(=-5) DO | o D+3 } ]
40. { SOMEONE(=-5) | o N+3 } { VALUE GIVE | i T-2 V-4 I-3 } AND { GIVE(=0) | i T-2 M-5 } E { KNOW SIDE(=+5) RULE | o agent } AND { FRIEND | o quality } PI { JOIN DO SOMEONE | o N+3 D+3 }
41. SO LA [ { BIG TIME | o N+3 D+3 } { MOVE | i T-2 } ] { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY(=+5) TIME | e } LA [ { RULE(=-5) HEAT(=+5) BIG | o D+3 } { MOVE(=+4) | a } ]
42. { CAN(=+3) | i T-2 } { MANY(=+5) TIME | e M-5 } { DO | i } E { KNOW THINK | o } AND { KNOW RULE | o } [ { SAME(=+3) JOIN | i T2 } E "2" { HAPPEN | o N+3 D+3 } ]
43. { SOMEONE(=-5) | o } { SEE | i T-2 } E [ "Skopas" { SOMEONE | o N+3 D+3 } { SAME(=-4) | i } ] ; { LAND(=+5) PLACE LAND(=-5) | o quality D+3 } { JOIN(=-5) | i } E { SOMEONE(=-5) | o N+3 } { MOOD(=-5) | o }
44. { SEX(=+5) BEGIN(=-5) SOMEONE | o D+3 } { KNOW | i T-2 A-5 } E { PART(=+2) SOMEONE | o N+3 } [ { GIVE(=+5) | i T-2 } E { THING(=0) GRAIN | o } { MOVE INSIDE(=+5) | e } "Rome" ]
45. { SEX(=+5) FRIEND(=-5) SOMEONE | o N+5 } LIKE "Coughlin" { RULE DO | i } E { THING | o D+3 } { SAME(=-5) | e }
46. BUT { WANT FRIEND | o D+3 } [ { BEGIN(=-5) GOOD | i T-2 } LA [ { BEGIN(=+5) TIME | o N+3 } PI { HEAT(=-3) TIME | o } ] ] { TIME(=0) | e } { LIVE(=-2) | i A0 }
47. { BEGIN(=-5) THING(=0) GRAIN | o N+3 D+3 } { GOOD(=-3) CONSUME | i T-2 } { INSIDE(=+5) | e } { PART(=-2) BODY CONSUME | o D+3 }
48. { ABOVE(=+5) THING(=+4) | o D+3 } { LIVE(=-2) | i } AND { CONSUME | i } { NEAR(=+5) | e } { JOIN | e } { DO SOMEONE | o agent N+3 D+3 }
49. { SAME(=+5) | e } { SEX(=-5) SOMEONE | o } { WANT(=-5) | i T-2 R-3 } E { SEX(=+5) SOMEONE | o } LA [ { SEX(=-5) SOMEONE | o } { SEE | i T-2 } E { SEX(=+5) SOMEONE | o } ]
50. { BODY SIDE(=+5) | o D+3 } { GOOD(=-2) LIVE | i } ; "Summers" { MOVE SIDE(=+5) | i T-2 } E { PLACE LONG MOVE | o D+3 }
51. { TIME(=-3) | o D-3 } LA [ { CONSUME GRAIN(=-3) HEAT | o D+3 } AND { WANT GIVE(=0) | o D+3 } { CHANGE | i T-2 } E { SOMEONE(=-5) | o } { INSIDE(=-5) | e } ]
52. { SEX(=+5) SOMEONE | o } { LIVE(=-5) | i T-2 R-3 } LA [ { SEX(=+5) SOMEONE | o } { TOUCH(=+4) | i T-2 } E { LAND(=+5) | o D+3 } ]
53. { HEAT SEE | o tool D-3 } { JOIN | i T-2 V-4 } { INSIDE(=0) | e } { LONG | o D-3 } ; { GIVE(=+5) | i } E { SEE HEAT(=+3) | o result }
54. "Dan" { KNOW | i T-2 } E [ { PART(=-2) BODY GOOD(=-4) | o D+3 } { CHANGE GOOD(=+3) | i T2 } ] BECAUSE { PART(=-2) BODY GOOD(=-4) | o D+3 } { TOUCH(=-5) FEEL | i T-2 }
55. { SEX(=+5) SOMEONE | o } { GOOD(=-3) FEEL | i T-2 } LA [ { SEX(=+5) SOMEONE | o } { SEE | i T-2 } E { SEX(=-5) SOMEONE | o D-3 } [ { FEEL(=+4) | i } AND { BIG(=-4) BODY | i } ; { JOIN | i } E { BIG LONG(=-5) ABOVE | o D-3 } ; { MOVE(=-5) | i } { INSIDE(=0) | e } { PLACE INSIDE(=0) | o D+3 } ] ]
56. { SEX(=-5) SOMEONE | o } { BIG(=+2) | i T-2 V+4 } E { PART(=-2) BODY | o N+3 } ; { GIVE(=-5) | i T-2 } E { LONG(=-5) BODY ABOVE(=-5) | o N+3 D+3 } ; { SEX(=-5) SOMEONE | o } { MOVE(=+4) INSIDE(=-5) | i T-2 } E { PLACE INSIDE(=+5) | o D+3 }
57. { MOVE MANY(=+3) | o D+3 } PI { PLACE LONG MOVE | o D+3 } { FEEL(=+4) GOOD(=-4) | i T-2 I+3 }
58. { SEX(=+5) SOMEONE | o } { GIVE(=+5) | i T-2 } E { THINK MEASURE | o result } PI { GRAIN(=-5) HEAT TIME | o D+3 } [ { FEEL(=-3) | i T-2 } ]
59. { MANY(=-5) VALUE | o D-3 } { BIG | i I+4 } LA [ { SAME(=+5) WANT(=+5) | o } { VALUE(=+5) | i } ]
60. { SEX(=+5) SOMEONE | o } { SAY(=-3) | i T-2 } AND { MOVE(=+4) | i T-2 } ; { SEE | e } { FEEL | i T-2 } E { KNOW(=-5) SOMEONE | o D-3 }
