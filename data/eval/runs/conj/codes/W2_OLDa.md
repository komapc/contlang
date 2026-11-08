1. INTENDED: Although the resolution might have been far more specific, it was considerably tougher than the earlier one.
   CODE: LA [ { THINK(=+5) TEXT | o result D+3 } { SAME(=-4) | i T-2 M-3 C+3 I+4 } ] ; { THINK(=+5) TEXT | o result D+3 } { TOUCH(=+5) | i T-2 C+3 I+3 } { TIME(=-2) | a C+3 } { THINK(=+5) TEXT | o result }
   READ AS: the decision / might be far more special / the decision / was much harder / earlier / a decision => Although the decision might be far more special, the decision was much harder earlier, as a decision.
2. INTENDED: An assistant attorney general is directed to investigate.
   CODE: { RULE(=+4) DO | o agent D-3 } { RULE(=+4) | o agent } { KNOW(=+5) SEE | i T0 V-4 } E { THING(=-5) | o }
   READ AS: administrator / official / is informed / object => An administrator is informed of an object by an official.
3. INTENDED: Costs were held down, despite a bitter winter.
   CODE: { VALUE(=-5) | o N+3 D+3 } { CHANGE(=-5) | i T-2 V-4 } ; LA [ { TIME HEAT(=-4) | o D-3 I+4 } ]
   READ AS: bargains / were kept unchanged / a very cold season => The bargains were left unchanged in a very cold season.
4. INTENDED: The year will probably start out with segregation still the most troublesome issue.
   CODE: { TIME(=+5) TIME(=+3) | o D+3 } { BEGIN(=-5) | i T+2 M-3 } ; LA [ { PART SAME(=-5) | o } { CARE(=-5) GOOD(=-3) | a C+5 } ]
   READ AS: the distant future / might begin / a different part / more careless => The distant future might begin if a different part is more careless.
5. INTENDED: Gilman started talking to him until he saw his chance.
   CODE: { SOMEONE(=-5) | o D+3 } { SAY | i A-5 T-2 } E { SOMEONE(=-4) | o } ; LA [ { SOMEONE | o } { SEE | i T-2 } E { TIME GOOD | o D+3 } ]
   READ AS: the others / began to speak / them / someone / saw / the good times => The others began to speak to them, while someone saw the good times.
6. INTENDED: The inclination was to accept the statement that there would be no formal negotiations.
   CODE: { WANT | o quality T-2 } { CONSUME(=+5) | i } E { SAY | o result D+3 } [ { RULE(=-5) KNOW | o N+3 M-5 } { HAPPEN | i T+2 } ]
   READ AS: past desire / consume / the words / no informal knowledge / will happen => Past desire consumed the words, and no informal knowledge will happen.
7. INTENDED: She had, she said, heard that the plant was closing.
   CODE: { SOMEONE(=-5) | o } { SAY | i T-2 } ; { SOMEONE | o } { CONSUME(=+5) SAY | i T-2 R-3 } E [ { THING(=0) DO | o D+3 } { SIDE(=-5) BEGIN | i T-2 } ]
   READ AS: they / said / someone / had heard / the deed / restarted => They said, and someone had heard the deed restart.
8. INTENDED: But in the moment of truth everyone could see that the U.S. was in reality the principal.
   CODE: { TIME(=-1) KNOW(=+5) | o D+3 } ; { MANY(=+5) SOMEONE | o } { SEE | i T-2 CAN } E [ { LAND SOMEONE(=+5) | o D+3 } { RULE(=+4) SAME(=+5) | i T-2 } ]
   READ AS: the news / everyone / could see / the native / were governed alike => The news came out; everyone could see the natives governed alike.
9. INTENDED: There apparently is no school of propaganda or psychological warfare.
   CODE: { SEE | e } { KNOW(=+5) FIGHT(=-5) | o M-5 } ; { MANY(=-5) KNOW(=+5) FIGHT | o M-5 }
   READ AS: visibly / no sports information / none of the sports information => Clearly there is no sports news, and nobody lacks sports news.
10. INTENDED: If either one ever started making promises, there is no telling where the promises would end.
   CODE: LA [ { MANY SOMEONE | o } { BEGIN(=-5) | i T-2 } E { SAY | o result N+3 } ] ; { MANY(=-5) | o } { KNOW | i } E [ { PLACE | o } { SAY | o result N+3 } { BEGIN(=+5) | i T+2 } ]
   READ AS: many people / began / statements / none / know / place / reports / will end => When many people began to speak, none knew a place where reports would end.
11. INTENDED: But the farmers outsmarted Washington by shortening the distance between the rows and pouring on the fertilizer.
   CODE: { LAND DO | o agent N+3 D+3 } { KNOW(=+5) GOOD CHANGE | i T-2 } E { RULE(=+4) LAND | o D+3 } ; { NEAR(=-5) CHANGE(=-5) | o D+3 } { BIG(=-3) | i } AND { GRAIN(=0) GIVE(=+5) LAND | i }
   READ AS: farmers / advocated improvement / the state / the far stagnation / is smaller / grain farming => Farmers advocated improvement to the state; the far stagnation is shrinking, and grain farming continues.
12. INTENDED: Heels place emphasis on the long legged silhouette.
   CODE: { BODY ABOVE(=-5) SIDE | o N+3 } { SEE | i } E { BODY LONG(=+3) BIG | o D+3 }
   READ AS: lower backs / see / the tall body => The lower backs are looking at the tall body.
13. INTENDED: He was above all a friend seeker, almost pathetic in his eagerness to be liked.
   CODE: { SOMEONE(=-3) | o D+3 } { FRIEND WANT | o agent I+4 } ; { FEEL(=+5) WANT | o quality } { MOOD(=-3) | a } ; { FRIEND WANT | i V-4 }
   READ AS: the others / great lover / passion / sad / is loved => The others have a devoted lover; passion turns sad, and the lover is loved.
14. INTENDED: Not all the concern for health is well directed.
   CODE: { CARE GOOD | o quality N+5 M-5 } { WANT | o } { CARE | o } { RULE(=+4) DO | a M-5 }
   READ AS: none of the good care / desire / care / not official => No good care is desired, and care is not done officially.
15. INTENDED: I must say, however, that I preferred the acting that had something of a biting edge to it.
   CODE: { SOMEONE(=+5) | o } { SAY | i } ; { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 } E { ART DO | o D+3 } [ { TOUCH(=+5) | a } { PLACE INSIDE(=0) | o } { HAPPEN | i } ]
   READ AS: I / speak / I / liked / the art / hard / entrance / happen => I speak; I liked the art, while a hard entrance happens.
16. INTENDED: There is fear in the fifties as his title suggests and as his competent drawings show.
   CODE: { FEEL(=-3) | o quality } { HAPPEN | i } ; { TEXT | o D+3 } { SAY | i } AND { ART(=+5) CAN | o result N+3 } { SEE | i }
   READ AS: calm / happens / the text / says / works of art / seen => A calm settles in; the text says so, and works of art can be seen.
17. INTENDED: So I started making some calls of my own.
   CODE: { SOMEONE(=+5) | o } { BEGIN(=-5) | i T-2 } E { SAY | o tool N+3 } { SOMEONE(=+5) | o } { DO | i }
   READ AS: I / began / using words / I / act => I began using words as tools, and I act.
18. INTENDED: Clever light songs were overly coy, tragic songs a little too melodramatic.
   CODE: { ART GOOD KNOW | o result N+3 } { MOOD(=+3) | a } { FEEL(=+3) | i I+4 M-3 } ; { MOOD(=-5) ART | o result N+3 } { FEEL(=+5) | i I+1 }
   READ AS: good art lessons / glad / might feel intensely / tragedies / feel somewhat excited => Good art lessons leave us glad and might stir us intensely; tragedies leave us somewhat excited.
19. INTENDED: For arm and shoulder strength a chinning bar is recommended.
   CODE: { BODY MANY | o } { BODY TOUCH(=+5) | o quality } { LONG(=+5) TOUCH(=+5) | o tool } { GOOD KNOW | i V-4 }
   READ AS: crowd / bodily hardness / hard club / is taught well => A crowd's toughness, through a hard club, is taught well.
20. INTENDED: Rodding formulas apply to many phases of the sport.
   CODE: { DO RULE | o result N+3 } { JOIN | i } E { MANY PART | o } { FIGHT(=-5) | o }
   READ AS: regulations / join / crowds / a sport => Regulations join the crowds at a sport.
21. INTENDED: Place sleeve seam at center underarm and center of sleeve cap at shoulder seam.
   CODE: { JOIN PLACE | i ! } E { LONG(=-5) | o } { INSIDE(=0) BODY | o } AND { LONG(=-5) | o } { ABOVE BODY | o }
   READ AS: enter! / cloth / skin / cloth / head => Enter! Cloth covers the skin, and cloth covers the head.
22. INTENDED: Another reason gymnastic study is valuable is that it can be started very early in life.
   CODE: { KNOW(=+5) FIGHT(=-5) BODY | o } { VALUE(=+5) | i } ; { BEGIN(=-5) | i V-4 CAN I+4 } { TIME(=-5) LIVE | e }
   READ AS: coach / is important / can be begun / long ago => A coach is important; it can be begun long ago.
23. INTENDED: Close behind the plane of the tappets are the locking bars.
   CODE: { SIDE(=-5) NEAR | e } { PLACE | o } { LONG(=+5) | o } { LONG(=+5) JOIN | o N+3 } { LONG(=0) JOIN | i }
   READ AS: back nearby / place / beam / frames / to fasten => Back nearby in the place, beams are made into frames and fastened.
24. INTENDED: Here is a word of advice when you go shopping for your pansy seeds.
   CODE: { NEAR(=+5) | e } { SAY | o result } { KNOW(=+5) | o result } ; LA [ { SOMEONE(=+3) | o } { VALUE(=-5) | i } E { THING(=0) | o } ]
   READ AS: here / statement / lesson / you / buy / plant => Here is a statement and a lesson: when you buy a plant.
25. INTENDED: Here you can pick up a taxi or public transport to return to the center of the city.
   CODE: { NEAR(=+5) | e } { SOMEONE(=+3) | o } { GIVE | i CAN } E { MOVE LONG(=+3) | o } AND { MOVE RULE(=+4) | o } ; { SIDE(=-5) MOVE | i } { NEAR(=+5) PLACE | o }
   READ AS: here / you / can give / wood transport / public transit / go back / downtown => Here you can give wood transport and public transit; go back downtown.
26. INTENDED: We passed his house and school on the way.
   CODE: { SOMEONE(=+5) PART | o } { MOVE | i T-2 } E { SOMEONE PLACE LIVE | o } AND { KNOW(=+5) PLACE | o }
   READ AS: we / moved / residents / school => We moved the residents and the school.
27. INTENDED: They adopted a program by which Louisiana was divided into five districts.
   CODE: { SOMEONE(=-5) | o } { DO | i T-2 } E { THINK(=+5) DO | o result } ; [ { LAND | o D+3 } { PART(=-2) | i V-4 T-2 } E { MANY(=+3) PART | o } ]
   READ AS: they / did / a decision / the land / was divided / many groups => They did make a decision; the land was divided into many groups.
28. INTENDED: What happened is that Negroes want to be treated like men.
   CODE: { HAPPEN | o result D+3 } { SOMEONE SEX(=+5) | o N+3 } { WANT | i } [ { SAME | i V-4 } E { SOMEONE SEX(=+5) | o N+3 } ]
   READ AS: the consequence / men / want / equalized / men => The consequence is that men want to be made equal to men.
29. INTENDED: But it is not really only a conversation.
   CODE: { SAY | o } { SAME(=+5) | i M-5 } { SAY | o } { MANY(=-1) | i M-5 }
   READ AS: words / are not identical / words / are not few => Words are not the same as words, and they are not few.
30. INTENDED: A group of sailors announced to Hudson that they would sail no farther.
   CODE: { PART(=+5) MOVE LAND(=-5) | o } { SAY | i T-2 } E { SOMEONE | o } [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T+2 M-5 } { NEAR(=-5) | e C+3 } ]
   READ AS: a fleet / was said / someone / they / will not sail / farther => A fleet was said to someone: they will not sail any farther.
31. INTENDED: One cannot speak anymore of being, one must speak only of the mess.
   CODE: { SOMEONE(=0) | o } { SAY | i CAN M-5 } E { LIVE | o } ; { SOMEONE(=0) | o } { SAY | i V+4 } E { SAME(=-4) CARE(=-5) | o }
   READ AS: someone / cannot say / life / someone / deliberately says / a particular mistake => Someone cannot say life; someone deliberately names a particular mistake.
32. INTENDED: He could have been blackmailed, or his family might have been threatened.
   CODE: { SOMEONE(=0) | o } { GIVE(=-5) VALUE(=-5) FEEL | i V-4 M-3 T-2 } ; { FRIEND(=+5) PART | o } { FEEL(=-5) FRIEND(=-5) | i V-4 M-3 T-2 }
   READ AS: someone / might have been swindled / a circle of friends / might have been provoked => Someone might have been swindled, and a circle of friends might have been provoked.
33. INTENDED: They look as if they had been sculptured with an unsharpened chisel.
   CODE: { SEE | i N+3 } LA [ { DO ART TOUCH | i V-4 T-2 } { LONG TOUCH(=+5) BIG(=-5) | o tool } { TOUCH(=-5) | a } ]
   READ AS: see / was crafted / small hard rod / soft => They see it, since it was crafted with a small hard rod and is soft.
34. INTENDED: Such is the field for exercising our reverence.
   CODE: { SAME | i } { PLACE | o D+3 } { DO | i } { WANT(=+5) KNOW | o quality }
   READ AS: is the same / place / act / curiosity => The place stays the same, and we act out of curiosity.
35. INTENDED: Driven from the marketplace by the course of history, our hero disguises himself as a private detective.
   CODE: { SOMEONE(=+5) | o } { TIME(=-5) HAPPEN | o } { MOVE | i V-4 T-2 } { PLACE VALUE(=-5) | o } ; { SOMEONE(=-3) | o } { CHANGE SEE | i } E { SOMEONE(=-3) | o } { RULE(=-5) SEE KNOW | o agent }
   READ AS: I / a past event / was moved / market / others / observe change / others / casual observers => I was moved to the market by a past event; others observe change as casual observers.
36. INTENDED: For it was neglected, not to say nascent, when the struggle began.
   CODE: { CARE(=-5) | i V-4 T-2 } ; { BEGIN(=-5) | a } { BEGIN(=-5) HAPPEN | i T-2 } LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ]
   READ AS: was neglected / initial / began / the match / began => It was neglected; an initial event began when the match began.
37. INTENDED: A valve in the handle let us cut the pressure still lower.
   CODE: { PLACE INSIDE LONG(=0) | o D-3 } { GIVE | i T-2 K0 } E { SOMEONE(=+5) | o N+3 } { JOIN(=-5) BIG(=-5) TOUCH(=+5) | i } { MEASURE(=-5) | o D+3 } { ABOVE(=-5) | e C+3 }
   READ AS: a closet / let / us / crush / the amount / lower => The closet let us crush the amount lower.
38. INTENDED: These drugs have no effect on the iodide concentrating mechanism, but they inhibit organification.
   CODE: { GOOD CHANGE | o N+3 } { HAPPEN | i M-5 } E { BODY | o } ; { SAME(=-4) GOOD | o N+3 } { JOIN(=-5) | i }
   READ AS: improvements / do not happen / body / special goods / separate => Improvements do not happen to the body; special goods separate.
39. INTENDED: It is believed that drug therapy and electroshock involve the former and psychotherapy the latter mechanism.
   CODE: { SOMEONE(=-5) THINK | i V-4 } LA [ { GOOD CHANGE | o } AND { FEEL(=+5) DO | o } { JOIN | i } E { SAME(=-4) | o } ; { THINK ART | o } { JOIN | i } E { SAME(=-4) | o } ]
   READ AS: is doubted / improvement / zeal / join / something special / philosophy / join / something special => Someone is doubted when improvement and zeal join something special; philosophy joins something special too.
40. INTENDED: They were inadequately financed, without experienced leadership, and lacked the general support of organized labor as a whole.
   CODE: { SOMEONE(=-5) | o N+3 } { VALUE | i T-2 M-5 } ; { SOMEONE(=-5) | o N+3 } { KNOW(=+5) CARE | a M-5 } { RULE(=+4) | o agent } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { MANY(=+5) PART RULE(=+4) | o }
   READ AS: they / did not value / they / not careful / officials / they / did not get / all officials => They did not value it; they were not careful officials, and they did not get all the officials.
41. INTENDED: So as the years passed, I saw them each time in the light of an accelerated personal conflagration.
   CODE: LA [ { TIME | o N+3 } { MOVE | i T-2 } ] ; { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY | e } { HEAT(=+5) CHANGE | o }
   READ AS: times / passed / I / saw / them / often / revolution => As times passed, I often saw them go through a revolution.
42. INTENDED: It was not always easy to develop theory and doctrine which would square the two conditions.
   CODE: { CAN(=-3) | i T-2 M-5 I+2 } ; { DO KNOW(=+5) | i } E { KNOW | o result } AND { RULE | o result } [ { SAME(=+5) | i } E { PLACE | o N+3 } ]
   READ AS: was not quite able / to teach / knowledge / law / match / places => It was not quite possible to teach knowledge and law, which match in places.
43. INTENDED: The Skopas people seemed to him of that breed of human beings whose insularity frees them from tragedy.
   CODE: { SOMEONE(=-5) | o } { SEE | i T-2 } E [ { SOMEONE PLACE | o N+3 } { SAME | i } { PART(=+5) SOMEONE(=0) | o } ] ; { LAND(=-5) PART(=-5) | o D+3 } { JOIN(=-5) | i } E { MOOD(=-5) | o }
   READ AS: they / saw / residents / are the same / a crowd / spray / separate / tragedy => They saw residents, who are the same as a crowd; the spray separates tragedy.
44. INTENDED: The boy was becoming acquainted with the contadini families that brought produce into Rome.
   CODE: { SOMEONE(=-3) | o D+3 } { KNOW(=+5) | i A-5 T-2 } E { SOMEONE PART(=+5) | o N+3 } [ { GIVE | i } E { THING(=0) CONSUME | o N+3 } { NEAR | e } "Rome" ]
   READ AS: the others / began to teach / us / give / crops / nearby => The others began to teach us to give crops near Rome.
45. INTENDED: All pricks like Coughlin run it anyway, one way or another.
   CODE: { MANY SOMEONE | o } { SAME | i } { RULE(=-5) | i } E { SAME(=+5) | o } { PLACE | o }
   READ AS: many people / are alike / rule informally / the same / place => Many people are alike and informally govern the same place.
46. INTENDED: But the liaison successfully started in the last days of autumn was now languishing.
   CODE: { WANT FRIEND | o D+3 } { BEGIN | i T-2 } { GOOD | e } { TIME(=-1) | o } ; { SOMEONE | o } { LIVE(=-2) | i T-2 A-5 }
   READ AS: the affection / began / well / just now / someone / fell asleep => The affection began well just now; someone fell asleep.
47. INTENDED: And indeed the young garden beans were brackish in her mouth.
   CODE: { THING(=0) GRAIN(=+5) | o D+3 } { TOUCH(=-5) | a } { CONSUME(=+5) | i T-2 } { BODY CONSUME | o }
   READ AS: the seed / soft / ate / nourishment => The soft seed consumed nourishment.
48. INTENDED: Top dog, sleeping and eating right there with the Staff.
   CODE: { RULE(=+4) BIG | o } { LIVE(=-2) | i } AND { CONSUME(=+5) | i } { NEAR(=+5) | e } LA [ { RULE(=+4) PART | o } ]
   READ AS: large institution / sleeps / consumes / here / a committee => A large institution sleeps and consumes here when a committee does.
49. INTENDED: Actually, she had hated him before she ever saw him.
   CODE: { SOMEONE(=-3) | o } { WANT(=-5) | i T-2 } E { SOMEONE | o } { TIME(=-3) | e } [ { SOMEONE | o } { SEE | i T-2 R+3 } ]
   READ AS: others / hated / someone / earlier / someone / later saw => Others hated someone earlier, and someone later saw them.
50. INTENDED: His face pale, Summers headed for the street.
   CODE: { BODY ABOVE | o D+3 } { LIVE(=-3) | i } ; { SOMEONE | o } { MOVE | i T-2 } E { PLACE MOVE | o }
   READ AS: the head / is faint / someone / moved / transport => The head is faint; someone moved transport.
51. INTENDED: A time before the white lightning and the bumming had turned him inside out.
   CODE: { TIME(=-5) | o } { SOMEONE | o } { CHANGE | i T-2 } E { INSIDE(=-5) | e } ; { TIME(=-3) HEAT TOUCH | o } AND { MOVE | o }
   READ AS: old times / someone / changed / outside / harsh winter / motion => Someone changed the old times outside: a harsh winter and motion.
52. INTENDED: He was dead before he hit the ground.
   CODE: { LIVE(=-5) | i T-2 } ; { TIME(=-1) | e } LA [ { SOMEONE | o } { TOUCH | i T-2 } E { LAND(=+5) | o } ]
   READ AS: died / just now / someone / touched / ground => They died; just now, someone touched the ground.
53. INTENDED: A lantern hung from a peg, giving light.
   CODE: { HEAT ABOVE | o D-3 } { LONG | o } { ABOVE | i T-2 } { LONG LAND | e } ; { GIVE HEAT | i }
   READ AS: a sun / ray / rose / across the land / warms => A sun's ray rose across the land and warms it.
54. INTENDED: From the way the wound in his head was itching, Dan knew that it would heal.
   CODE: LA [ { BODY ABOVE(=+5) JOIN(=-5) | o D+3 } { FEEL(=+5) TOUCH(=-3) | i } ] ; { SOMEONE | o } { KNOW(=+5) | i T-2 } E [ { CHANGE GOOD(=+5) | i T+2 M+4 } ]
   READ AS: the neck / is tickled / someone / taught / will surely improve => When the neck is tickled, someone taught that things will surely improve.
55. INTENDED: He was disappointed to find a nervous, scrawny woman with a big hat standing at the door.
   CODE: { SOMEONE | o } { WANT(=-3) | i T-2 } LA [ { SEE | i } E { SOMEONE | o } { FEEL(=+5) | a } AND { LONG(=-5) BIG(=-3) | a } AND { BIG | o } { BODY ABOVE | o } { MOVE(=-5) | i } { NEAR | e } { PLACE | o } ]
   READ AS: someone / disliked / see / someone / excited / slim / giant / head / stay still / nearby / place => Someone disliked seeing another person who is excited and slim, while a giant head stays still nearby.
56. INTENDED: Extending her fingers another inch, she caught up the shorts, and swiftly left the room.
   CODE: { SOMEONE | o } { JOIN BIG | i } E { BODY LONG | o N+3 } ; { SOMEONE | o } { GIVE(=-5) | i T-2 } E { BODY | o } ; { SOMEONE | o } { MOVE(=+3) | i T-2 } E { PLACE INSIDE LIVE | o }
   READ AS: someone / enlarged / tall bodies / someone / seized / body / someone / hurried / home => Someone enlarged the tall bodies, someone seized a body, and someone hurried home.
57. INTENDED: In the street the traffic was really frightening.
   CODE: { PLACE NEAR MOVE | o } { MOVE LONG(=+3) | o N+3 } { FEEL(=-5) MOOD | i I+4 }
   READ AS: station / vehicles / very calm => A station of vehicles is very calm.
58. INTENDED: He then offered his own estimate of the weather, which was unenthusiastic.
   CODE: { SOMEONE | o } { SAY | i T-2 } E { SOMEONE | o } { THINK | o result } [ { HEAT LONG(=-5) TIME | o D+3 } { MOOD(=-3) WANT(=-5) | i } ]
   READ AS: someone / said / someone / idea / the winter / dreads => Someone told someone an idea; the winter dreads.
59. INTENDED: No price is too high when true love is at stake.
   CODE: { VALUE | o M-5 } { BIG | i I+3 M-5 } LA [ { WANT(=+5) | o D+3 } { SAME(=+5) | a } { LIVE(=-3) | i } ]
   READ AS: no value / is not very large / the love / identical / lies dormant => There is no value; it is not very large, since the love is identical and lies dormant.
60. INTENDED: He muttered, and took off, obviously feeling like a fool.
   CODE: { SOMEONE | o } { SAY(=-3) | i T-2 } AND { MOVE | i T-2 } ; { SEE | e } { SOMEONE | o } { FEEL | i } E { KNOW(=-5) SOMEONE | o }
   READ AS: someone / murmured / moved / clearly / someone / feels / fool => Someone murmured and moved; clearly someone feels like a fool.
---
1. LA [ { THINK(=+5) TEXT | o result D+3 } { SAME(=-4) | i T-2 M-3 C+3 I+4 } ] ; { THINK(=+5) TEXT | o result D+3 } { TOUCH(=+5) | i T-2 C+3 I+3 } E { TIME(=-2) THINK(=+5) TEXT | o result D+3 }
2. { PART(=-2) RULE(=+5) | o agent D-3 } { SAY(=+4) | i V-4 } E [ { SEE CARE(=+5) | i T+2 } ]
3. LA [ { TIME HEAT(=-4) | o D-3 I+4 } ] ; { MEASURE(=-5) VALUE | o N+3 D+3 } { CHANGE(=-5) | i T-2 V-4 }
4. { TIME PART(=+2) BIG | o D+3 } { BEGIN(=-5) | i T+2 M+2 } ; { JOIN(=-5) SOMEONE | o quality D+3 } { BEGIN(=0) | e } { CAN(=-3) HAPPEN | i C+5 }
5. LA [ { SOMEONE(=-5) | o } { SEE | i T-2 A+5 } E { TIME CAN | o D+3 } ] ; "Gilman" { SAY | i A-5 T-2 } E { SOMEONE(=-5) | o }
6. { WANT | o quality D+3 } { CONSUME(=+5) SAY | i T-2 } E [ { RULE(=+5) SAY JOIN | o N+3 M-5 } { HAPPEN | i T+2 } ]
7. { SOMEONE SEX(=-5) | o } { SAY | i T-2 } ; { SOMEONE SEX(=-5) | o } { CONSUME(=+5) SAY | i T-2 R-3 } E [ { PLACE DO | o D+3 } { BEGIN(=+5) | i T-2 A-3 } ]
8. { TIME(=0) KNOW(=0) SAME(=+5) | o D+3 } ; { MANY(=+5) SOMEONE | o } { SEE | i T-2 CAN } E [ "U.S." { KNOW(=0) SAME(=+5) | e } { RULE(=+4) | i T-2 C+5 } ]
9. { SEE | e } { KNOW(=+5) PLACE | o M-5 } FOR { SAY CHANGE | o } AND { THINK FIGHT(=+5) | o }
10. LA [ { MANY(=0) SOMEONE | o } { BEGIN(=-5) | i T-2 } E { SAY TIME(=+2) GIVE | o result N+3 } ] ; { MANY(=-5) | o } { KNOW | i } E [ { PLACE | o } { SAY TIME(=+2) GIVE | o result N+3 } { BEGIN(=+5) | i T+2 } ]
11. { LAND DO | o agent N+3 D+3 } { KNOW | i T-2 C+3 } E "Washington" ; { LAND DO | o agent N+3 D+3 } { CHANGE NEAR(=+3) | i T-2 } E { NEAR(=-5) LONG | o D+3 } AND { GIVE(=+5) | i T-2 } E { GRAIN LAND(=+5) | o }
12. { BODY ABOVE(=-5) SIDE(=-5) | o N+3 } { DO VALUE(=+5) | i } E { SEE BODY LONG | o D+3 }
13. { SOMEONE SEX(=+5) | o D+3 } { FRIEND SEE | i C+5 } ; { FEEL(=+5) WANT | o quality D+3 } { MOOD(=-3) | i } ; { SOMEONE SEX(=+5) | o } { FRIEND WANT(=+3) | i V-4 }
14. { CARE LIVE | o D+3 N+5 M-5 } { SIDE(=+5) GOOD | i V-4 }
15. { SOMEONE(=+5) | o } { SAY | i V+4 } ; { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 C+3 } E { ART(=+5) DO | o D+3 } [ { TOUCH(=+5) INSIDE(=0) | o D-3 } { JOIN | i } ]
16. { FEEL(=+5) GOOD(=-5) | o quality } { HAPPEN | i } { TIME(=-3) | e } "1950" ; { TEXT | o D+3 } { SAY | i } AND { ART(=+5) CAN | o result N+3 } { SEE | i K+3 }
17. { SOMEONE(=+5) | o } { BEGIN(=-5) | i T-2 } E { SAY NEAR(=-5) | o result N+1 }
18. { ART(=+5) SAY | o result N+3 D+3 } { KNOW(=+3) | a } AND { MOOD(=+3) | a } { FEEL(=-3) CARE | i I+5 } ; { MOOD(=-5) ART(=+5) SAY | o result N+3 } { FEEL(=+5) | i C+3 I+1 }
19. LA [ { BODY ABOVE | o N+3 } { CAN TOUCH(=+5) | o quality } ] ; { LONG(=0) TOUCH(=+5) | o D-3 } { SAY GOOD | i V-4 }
20. { RULE ART(=-5) | o result N+3 } { JOIN | i } E { MANY(=+3) PART(=-2) TIME | o N+3 } PI { FIGHT(=-5) | o }
21. { JOIN | i ! } E { LONG(=-5) JOIN | o D+3 } { NEAR(=+5) | e } { ABOVE(=-5) BODY | o } AND { LONG(=-5) ABOVE BODY | o }
22. { KNOW(=+5) BODY MOVE | o D+3 } { VALUE(=+5) | i } ; { BEGIN(=-5) | i V-4 CAN } { TIME(=-2) LIVE(=+5) | e I+4 }
23. { SIDE(=-5) NEAR(=+3) | e } { PLACE | o D+3 } FOR { MOVE LONG(=0) | o N+3 } ; { LONG(=0) JOIN | o N+3 D+3 } { PLACE | i }
24. LA [ { SOMEONE(=+3) | o } { MOVE VALUE(=-5) | i } E { THING(=0) GRAIN(=0) | o N+3 } ] ; { NEAR(=+5) | e } { SAY(=0) KNOW(=+5) | o result D-3 }
25. { NEAR(=+5) | e } { SOMEONE(=+3) | o } { GIVE(=0) | i CAN } E { MOVE | o tool D-3 } AND { MOVE RULE(=+4) | o tool } ; { SIDE(=-5) MOVE | i } { NEAR(=+5) PLACE | o }
26. { SOMEONE(=+5) PART | o } { MOVE | i T-2 } { NEAR(=0) | e } E { PLACE LIVE | o D+3 } AND { KNOW(=+5) PLACE | o D+3 }
27. { SOMEONE(=-5) | o } { CONSUME(=+5) | i T-2 } E { RULE DO | o result D-3 } ; "Louisiana" { PART(=-2) | i V-4 T-2 } E { LAND PART(=-2) | o N+3 } "5"
28. { HAPPEN | o result D+3 } { SOMEONE(=-5) | o N+3 D+3 } { WANT | i } [ { SAME | i V-4 } E { SOMEONE SEX(=+5) | o N+3 } ]
29. { HAPPEN | o D+3 } { SAME(=+5) | i M-5 I+4 } E { SAY JOIN | o D-3 }
30. { PART(=+5) MOVE LAND(=-5) | o agent } { SAY | i T-2 } E "Hudson" [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T+2 M-5 } { NEAR(=-5) | e C+3 } ]
31. { SOMEONE(=0) | o } { SAY | i CAN M-5 } E { LIVE | o quality } ; { SOMEONE(=0) | o } { SAY | i V+4 } E { SAME(=-5) CARE(=-5) | o D+3 }
32. { SOMEONE SEX(=+5) | o } { FRIEND(=-5) GIVE(=-5) VALUE | i V-4 M-3 T-2 } ; { LIVE JOIN PART | o D+3 } { FRIEND(=-5) SAY | i V-4 M-3 T-2 }
33. { SEE | i N+3 } LA [ { DO ART | i V-4 T-2 } { JOIN(=-4) TOUCH(=+4) | a M-5 } { JOIN(=-4) TOUCH(=+4) | o tool } ]
34. { SAME | e } { PLACE | o D+3 } FOR { DO VALUE(=+5) WANT | o quality }
35. { TIME(=-5) HAPPEN | o D+3 } { MOVE(=+3) | i K+5 T-2 } E { SOMEONE SEX(=+5) | o D+3 } { NEAR(=-5) | e } { PLACE VALUE(=-5) | o } ; { SOMEONE SEX(=+5) | o } { CHANGE SEE | i V+4 } E { SOMEONE SEX(=+5) | o } { RULE(=-5) SEE CARE | o agent }
36. LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ] ; { CARE(=-5) | i V-4 T-2 } AND { BEGIN(=-5) | a }
37. { JOIN(=-5) GRAIN(=-3) | o tool D-3 } PI { LONG(=0) | o D+3 } { DO | i T-2 K0 } E { SOMEONE(=+5) | o N+3 } { JOIN(=-5) MEASURE(=-5) | i } E { TOUCH(=+5) MEASURE(=0) | o D+3 } { ABOVE(=-5) | e C+3 }
38. { CHANGE LIVE GRAIN | o N+3 D+3 } { DO | i M-5 } E "iodide" { JOIN DO | o tool } ; { CHANGE LIVE GRAIN | o N+3 D+3 } { DO JOIN(=-5) | i } E { LIVE DO | o quality }
39. { THINK(=+2) | i V-4 } E [ { CHANGE LIVE GRAIN | o } AND { FEEL(=+5) ART(=-5) | o } { JOIN | i } E { DO PART(=-2) | o D+3 } ; { THINK CHANGE LIVE | o } { JOIN | i } E { DO PART(=-2) | o D+3 } ]
40. { SOMEONE(=-5) | o N+3 } { GIVE(=+5) VALUE | i V-4 T-2 C-3 } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { KNOW(=+5) RULE(=+4) | o agent } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { FRIEND GIVE(=+5) | o result D+3 } FOR { DO JOIN | o agent N+5 }
41. LA [ { TIME PART(=+2) BIG | o N+3 } { MOVE | i T-2 } ] ; { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY(=+5) TIME | e } { HEAT(=+5) HAPPEN MOVE(=+5) | o }
42. { MANY(=+5) | e M-5 } { CAN(=+5) | i T-2 } ; { CHANGE(=+3) | i } E { THINK KNOW | o result } AND { RULE THINK | o result } [ { SAME(=+5) | i T+2 } E "2" { HAPPEN | o result } ]
43. { SOMEONE SEX(=+5) | o D+3 } { SEE | i T-2 } E [ "Skopas" { SOMEONE PLACE | o N+3 } { SAME | i } ] ; { LAND(=+5) INSIDE LAND(=-5) | o quality D+3 } { JOIN(=-5) | i } E { MOOD(=-5) | o }
44. { SOMEONE SEX(=+5) BIG(=-3) | o D+3 } { KNOW(=+1) | i A-3 T-2 } E { LAND DO PART(=+5) | o N+3 } [ { MOVE GIVE | i T-2 } E { THING(=0) CONSUME | o N+3 } { INSIDE(=+5) | e } "Rome" ]
45. { MANY(=+5) SOMEONE FRIEND(=-5) | o } LIKE "Coughlin" { RULE(=+4) | i } E { HAPPEN | o D+3 } { MANY(=+5) SAME(=-5) | e }
46. { JOIN FRIEND | o D+3 } { GOOD BEGIN(=-5) | i T-2 V-4 } { TIME(=-3) HEAT(=-2) BEGIN(=+5) | e } ; { JOIN FRIEND | o D+3 } { LIVE(=-1) | i T-2 A-3 } { TIME(=0) | e }
47. { TIME(=-2) | a } { THING(=0) GRAIN(=+5) | o N+3 D+3 } { CONSUME(=+5) LAND(=-5) | i T-2 } PI { BODY CONSUME | o }
48. { RULE(=+4) BIG | o agent } AND { RULE(=+4) PART | o N+3 D+3 } { LIVE(=-2) | i } AND { CONSUME(=+5) | i } { NEAR(=+5) | e }
49. LA [ { SOMEONE SEX(=-5) | o } { SEE | i T-2 } E { SOMEONE SEX(=+5) | o } ] ; { SOMEONE SEX(=-5) | o } { WANT(=-5) | i T-2 R-3 } E { SOMEONE SEX(=+5) | o }
50. LA [ { BODY SEE | o D+3 } { LIVE(=-1) SEE | i } ] ; "Summers" { MOVE | i T-2 } E { PLACE MOVE LAND(=+5) | o D+3 }
51. { TIME(=-3) | o D-3 } ; { GRAIN(=-3) HEAT CONSUME | o D+3 } AND { MOVE GIVE | o } { CHANGE | i T-2 R-3 } E { SOMEONE SEX(=+5) | o } { INSIDE(=-5) | e }
52. LA [ { SOMEONE SEX(=+5) | o } { TOUCH(=+5) | i T-2 } E { LAND(=+5) | o D+3 } ] ; { SOMEONE SEX(=+5) | o } { LIVE(=-5) | i T-2 R-3 }
53. { HEAT SEE | o tool D-3 } { JOIN ABOVE | i V-4 T-2 } { LONG(=0) BIG(=-3) | o D-3 } ; { GIVE(=+5) | i } E { SEE HEAT | o }
54. LA [ { BODY JOIN(=-5) | o D+3 } PI { BODY ABOVE | o D+3 } { FEEL(=+3) TOUCH(=-3) | i } ] ; "Dan" { KNOW(=0) | i T-2 } E [ { CHANGE(=+3) LIVE(=+5) | i T+2 M+4 } ]
55. LA [ { SOMEONE SEX(=+5) | o } { SEE | i T-2 } E { SOMEONE SEX(=-5) | o D-3 } { FEEL(=+3) | a } AND { BODY BIG(=-3) | a } AND { LONG(=-5) BODY ABOVE | o D-3 } { BIG | a } { MOVE(=-5) | i } { NEAR | e } { PLACE INSIDE(=0) | o D+3 } ] ; { SOMEONE SEX(=+5) | o } { WANT(=-3) | i T-2 }
56. { SOMEONE SEX(=-5) | o } { CHANGE BIG | i } E { BODY LONG(=0) | o N+3 } ; { SOMEONE SEX(=-5) | o } { GIVE(=-2) | i T-2 } E { LONG(=-5) BODY | o N+3 D+3 } ; { SOMEONE SEX(=-5) | o } { MOVE(=+3) INSIDE(=-5) | i T-2 } E { PLACE INSIDE | o D+3 }
57. { MOVE | o tool N+3 D+3 } PI { PLACE MOVE | o D+3 } { FEEL(=+5) GOOD(=-5) | i T-2 I+3 }
58. { SOMEONE SEX(=+5) | o } { SAY | i T-2 } E { THINK MEASURE | o result } PI { HEAT HAPPEN | o D+3 } ; { THINK MEASURE | o result D+3 } { FEEL(=-3) | i T-2 }
59. LA [ { SAME(=+5) KNOW | a } { WANT(=+5) | o D+3 } { VALUE(=+5) | i } ] ; { MEASURE(=-5) VALUE | o M-5 } { BIG | i I+5 }
60. { SOMEONE SEX(=+5) | o } { SAY(=-3) | i T-2 } AND { MOVE(=+3) | i T-2 } ; { SEE | e } { SOMEONE SEX(=+5) | o } { FEEL | i } E { KNOW(=-5) SOMEONE | o }
