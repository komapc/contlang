1. LA [ { THINK(=+5) TEXT | o result D+3 } { SAME(=-4) | i T-2 M-3 C+3 I+4 } ] ; { THINK(=+5) TEXT | o result D+3 } { TOUCH(=+5) | i T-2 C+3 I+3 } { TIME(=-2) | a C+3 } { THINK(=+5) TEXT | o result }
2. { RULE(=+4) DO | o agent D-3 } { RULE(=+4) | o agent } { KNOW(=+5) SEE | i T0 V-4 } E { THING(=-5) | o }
3. { VALUE(=-5) | o N+3 D+3 } { CHANGE(=-5) | i T-2 V-4 } ; LA [ { TIME HEAT(=-4) | o D-3 I+4 } ]
4. { TIME(=+5) TIME(=+3) | o D+3 } { BEGIN(=-5) | i T+2 M-3 } ; LA [ { PART SAME(=-5) | o } { CARE(=-5) GOOD(=-3) | a C+5 } ]
5. { SOMEONE(=-5) | o D+3 } { SAY | i A-5 T-2 } E { SOMEONE(=-4) | o } ; LA [ { SOMEONE | o } { SEE | i T-2 } E { TIME GOOD | o D+3 } ]
6. { WANT | o quality T-2 } { CONSUME(=+5) | i } E { SAY | o result D+3 } [ { RULE(=-5) KNOW | o N+3 M-5 } { HAPPEN | i T+2 } ]
7. { SOMEONE(=-5) | o } { SAY | i T-2 } ; { SOMEONE | o } { CONSUME(=+5) SAY | i T-2 R-3 } E [ { THING(=0) DO | o D+3 } { SIDE(=-5) BEGIN | i T-2 } ]
8. { TIME(=-1) KNOW(=+5) | o D+3 } ; { MANY(=+5) SOMEONE | o } { SEE | i T-2 CAN } E [ { LAND SOMEONE(=+5) | o D+3 } { RULE(=+4) SAME(=+5) | i T-2 } ]
9. { SEE | e } { KNOW(=+5) FIGHT(=-5) | o M-5 } ; { MANY(=-5) KNOW(=+5) FIGHT | o M-5 }
10. LA [ { MANY SOMEONE | o } { BEGIN(=-5) | i T-2 } E { SAY | o result N+3 } ] ; { MANY(=-5) | o } { KNOW | i } E [ { PLACE | o } { SAY | o result N+3 } { BEGIN(=+5) | i T+2 } ]
11. { LAND DO | o agent N+3 D+3 } { KNOW(=+5) GOOD CHANGE | i T-2 } E { RULE(=+4) LAND | o D+3 } ; { NEAR(=-5) CHANGE(=-5) | o D+3 } { BIG(=-3) | i } AND { GRAIN(=0) GIVE(=+5) LAND | i }
12. { BODY ABOVE(=-5) SIDE | o N+3 } { SEE | i } E { BODY LONG(=+3) BIG | o D+3 }
13. { SOMEONE(=-3) | o D+3 } { FRIEND WANT | o agent I+4 } ; { FEEL(=+5) WANT | o quality } { MOOD(=-3) | a } ; { FRIEND WANT | i V-4 }
14. { CARE GOOD | o quality N+5 M-5 } { WANT | o } { CARE | o } { RULE(=+4) DO | a M-5 }
15. { SOMEONE(=+5) | o } { SAY | i } ; { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 } E { ART DO | o D+3 } [ { TOUCH(=+5) | a } { PLACE INSIDE(=0) | o } { HAPPEN | i } ]
16. { FEEL(=-3) | o quality } { HAPPEN | i } ; { TEXT | o D+3 } { SAY | i } AND { ART(=+5) CAN | o result N+3 } { SEE | i }
17. { SOMEONE(=+5) | o } { BEGIN(=-5) | i T-2 } E { SAY | o tool N+3 } { SOMEONE(=+5) | o } { DO | i }
18. { ART GOOD KNOW | o result N+3 } { MOOD(=+3) | a } { FEEL(=+3) | i I+4 M-3 } ; { MOOD(=-5) ART | o result N+3 } { FEEL(=+5) | i I+1 }
19. { BODY MANY | o } { BODY TOUCH(=+5) | o quality } { LONG(=+5) TOUCH(=+5) | o tool } { GOOD KNOW | i V-4 }
20. { DO RULE | o result N+3 } { JOIN | i } E { MANY PART | o } { FIGHT(=-5) | o }
21. { JOIN PLACE | i ! } E { LONG(=-5) | o } { INSIDE(=0) BODY | o } AND { LONG(=-5) | o } { ABOVE BODY | o }
22. { KNOW(=+5) FIGHT(=-5) BODY | o } { VALUE(=+5) | i } ; { BEGIN(=-5) | i V-4 CAN I+4 } { TIME(=-5) LIVE | e }
23. { SIDE(=-5) NEAR | e } { PLACE | o } { LONG(=+5) | o } { LONG(=+5) JOIN | o N+3 } { LONG(=0) JOIN | i }
24. { NEAR(=+5) | e } { SAY | o result } { KNOW(=+5) | o result } ; LA [ { SOMEONE(=+3) | o } { VALUE(=-5) | i } E { THING(=0) | o } ]
25. { NEAR(=+5) | e } { SOMEONE(=+3) | o } { GIVE | i CAN } E { MOVE LONG(=+3) | o } AND { MOVE RULE(=+4) | o } ; { SIDE(=-5) MOVE | i } { NEAR(=+5) PLACE | o }
26. { SOMEONE(=+5) PART | o } { MOVE | i T-2 } E { SOMEONE PLACE LIVE | o } AND { KNOW(=+5) PLACE | o }
27. { SOMEONE(=-5) | o } { DO | i T-2 } E { THINK(=+5) DO | o result } ; [ { LAND | o D+3 } { PART(=-2) | i V-4 T-2 } E { MANY(=+3) PART | o } ]
28. { HAPPEN | o result D+3 } { SOMEONE SEX(=+5) | o N+3 } { WANT | i } [ { SAME | i V-4 } E { SOMEONE SEX(=+5) | o N+3 } ]
29. { SAY | o } { SAME(=+5) | i M-5 } { SAY | o } { MANY(=-1) | i M-5 }
30. { PART(=+5) MOVE LAND(=-5) | o } { SAY | i T-2 } E { SOMEONE | o } [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T+2 M-5 } { NEAR(=-5) | e C+3 } ]
31. { SOMEONE(=0) | o } { SAY | i CAN M-5 } E { LIVE | o } ; { SOMEONE(=0) | o } { SAY | i V+4 } E { SAME(=-4) CARE(=-5) | o }
32. { SOMEONE(=0) | o } { GIVE(=-5) VALUE(=-5) FEEL | i V-4 M-3 T-2 } ; { FRIEND(=+5) PART | o } { FEEL(=-5) FRIEND(=-5) | i V-4 M-3 T-2 }
33. { SEE | i N+3 } LA [ { DO ART TOUCH | i V-4 T-2 } { LONG TOUCH(=+5) BIG(=-5) | o tool } { TOUCH(=-5) | a } ]
34. { SAME | i } { PLACE | o D+3 } { DO | i } { WANT(=+5) KNOW | o quality }
35. { SOMEONE(=+5) | o } { TIME(=-5) HAPPEN | o } { MOVE | i V-4 T-2 } { PLACE VALUE(=-5) | o } ; { SOMEONE(=-3) | o } { CHANGE SEE | i } E { SOMEONE(=-3) | o } { RULE(=-5) SEE KNOW | o agent }
36. { CARE(=-5) | i V-4 T-2 } ; { BEGIN(=-5) | a } { BEGIN(=-5) HAPPEN | i T-2 } LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ]
37. { PLACE INSIDE LONG(=0) | o D-3 } { GIVE | i T-2 K0 } E { SOMEONE(=+5) | o N+3 } { JOIN(=-5) BIG(=-5) TOUCH(=+5) | i } { MEASURE(=-5) | o D+3 } { ABOVE(=-5) | e C+3 }
38. { GOOD CHANGE | o N+3 } { HAPPEN | i M-5 } E { BODY | o } ; { SAME(=-4) GOOD | o N+3 } { JOIN(=-5) | i }
39. { SOMEONE(=-5) THINK | i V-4 } LA [ { GOOD CHANGE | o } AND { FEEL(=+5) DO | o } { JOIN | i } E { SAME(=-4) | o } ; { THINK ART | o } { JOIN | i } E { SAME(=-4) | o } ]
40. { SOMEONE(=-5) | o N+3 } { VALUE | i T-2 M-5 } ; { SOMEONE(=-5) | o N+3 } { KNOW(=+5) CARE | a M-5 } { RULE(=+4) | o agent } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { MANY(=+5) PART RULE(=+4) | o }
41. LA [ { TIME | o N+3 } { MOVE | i T-2 } ] ; { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY | e } { HEAT(=+5) CHANGE | o }
42. { CAN(=-3) | i T-2 M-5 I+2 } ; { DO KNOW(=+5) | i } E { KNOW | o result } AND { RULE | o result } [ { SAME(=+5) | i } E { PLACE | o N+3 } ]
43. { SOMEONE(=-5) | o } { SEE | i T-2 } E [ { SOMEONE PLACE | o N+3 } { SAME | i } { PART(=+5) SOMEONE(=0) | o } ] ; { LAND(=-5) PART(=-5) | o D+3 } { JOIN(=-5) | i } E { MOOD(=-5) | o }
44. { SOMEONE(=-3) | o D+3 } { KNOW(=+5) | i A-5 T-2 } E { SOMEONE PART(=+5) | o N+3 } [ { GIVE | i } E { THING(=0) CONSUME | o N+3 } { NEAR | e } "Rome" ]
45. { MANY SOMEONE | o } { SAME | i } { RULE(=-5) | i } E { SAME(=+5) | o } { PLACE | o }
46. { WANT FRIEND | o D+3 } { BEGIN | i T-2 } { GOOD | e } { TIME(=-1) | o } ; { SOMEONE | o } { LIVE(=-2) | i T-2 A-5 }
47. { THING(=0) GRAIN(=+5) | o D+3 } { TOUCH(=-5) | a } { CONSUME(=+5) | i T-2 } { BODY CONSUME | o }
48. { RULE(=+4) BIG | o } { LIVE(=-2) | i } AND { CONSUME(=+5) | i } { NEAR(=+5) | e } LA [ { RULE(=+4) PART | o } ]
49. { SOMEONE(=-3) | o } { WANT(=-5) | i T-2 } E { SOMEONE | o } { TIME(=-3) | e } [ { SOMEONE | o } { SEE | i T-2 R+3 } ]
50. { BODY ABOVE | o D+3 } { LIVE(=-3) | i } ; { SOMEONE | o } { MOVE | i T-2 } E { PLACE MOVE | o }
51. { TIME(=-5) | o } { SOMEONE | o } { CHANGE | i T-2 } E { INSIDE(=-5) | e } ; { TIME(=-3) HEAT TOUCH | o } AND { MOVE | o }
52. { LIVE(=-5) | i T-2 } ; { TIME(=-1) | e } LA [ { SOMEONE | o } { TOUCH | i T-2 } E { LAND(=+5) | o } ]
53. { HEAT ABOVE | o D-3 } { LONG | o } { ABOVE | i T-2 } { LONG LAND | e } ; { GIVE HEAT | i }
54. LA [ { BODY ABOVE(=+5) JOIN(=-5) | o D+3 } { FEEL(=+5) TOUCH(=-3) | i } ] ; { SOMEONE | o } { KNOW(=+5) | i T-2 } E [ { CHANGE GOOD(=+5) | i T+2 M+4 } ]
55. { SOMEONE | o } { WANT(=-3) | i T-2 } LA [ { SEE | i } E { SOMEONE | o } { FEEL(=+5) | a } AND { LONG(=-5) BIG(=-3) | a } AND { BIG | o } { BODY ABOVE | o } { MOVE(=-5) | i } { NEAR | e } { PLACE | o } ]
56. { SOMEONE | o } { JOIN BIG | i } E { BODY LONG | o N+3 } ; { SOMEONE | o } { GIVE(=-5) | i T-2 } E { BODY | o } ; { SOMEONE | o } { MOVE(=+3) | i T-2 } E { PLACE INSIDE LIVE | o }
57. { PLACE NEAR MOVE | o } { MOVE LONG(=+3) | o N+3 } { FEEL(=-5) MOOD | i I+4 }
58. { SOMEONE | o } { SAY | i T-2 } E { SOMEONE | o } { THINK | o result } [ { HEAT LONG(=-5) TIME | o D+3 } { MOOD(=-3) WANT(=-5) | i } ]
59. { VALUE | o M-5 } { BIG | i I+3 M-5 } LA [ { WANT(=+5) | o D+3 } { SAME(=+5) | a } { LIVE(=-3) | i } ]
60. { SOMEONE | o } { SAY(=-3) | i T-2 } AND { MOVE | i T-2 } ; { SEE | e } { SOMEONE | o } { FEEL | i } E { KNOW(=-5) SOMEONE | o }
---
1. the decision / might be far more special / the decision / was much harder / earlier / a decision => Although the decision might be far more special, the decision was much harder earlier, as a decision.
2. administrator / official / is informed / object => An administrator is informed of an object by an official.
3. bargains / were kept unchanged / a very cold season => The bargains were left unchanged in a very cold season.
4. the distant future / might begin / a different part / more careless => The distant future might begin if a different part is more careless.
5. the others / began to speak / them / someone / saw / the good times => The others began to speak to them, while someone saw the good times.
6. past desire / consume / the words / no informal knowledge / will happen => Past desire consumed the words, and no informal knowledge will happen.
7. they / said / someone / had heard / the deed / restarted => They said, and someone had heard the deed restart.
8. the news / everyone / could see / the native / were governed alike => The news came out; everyone could see the natives governed alike.
9. visibly / no sports information / none of the sports information => Clearly there is no sports news, and nobody lacks sports news.
10. many people / began / statements / none / know / place / reports / will end => When many people began to speak, none knew a place where reports would end.
11. farmers / advocated improvement / the state / the far stagnation / is smaller / grain farming => Farmers advocated improvement to the state; the far stagnation is shrinking, and grain farming continues.
12. lower backs / see / the tall body => The lower backs are looking at the tall body.
13. the others / great lover / passion / sad / is loved => The others have a devoted lover; passion turns sad, and the lover is loved.
14. none of the good care / desire / care / not official => No good care is desired, and care is not done officially.
15. I / speak / I / liked / the art / hard / entrance / happen => I speak; I liked the art, while a hard entrance happens.
16. calm / happens / the text / says / works of art / seen => A calm settles in; the text says so, and works of art can be seen.
17. I / began / using words / I / act => I began using words as tools, and I act.
18. good art lessons / glad / might feel intensely / tragedies / feel somewhat excited => Good art lessons leave us glad and might stir us intensely; tragedies leave us somewhat excited.
19. crowd / bodily hardness / hard club / is taught well => A crowd's toughness, through a hard club, is taught well.
20. regulations / join / crowds / a sport => Regulations join the crowds at a sport.
21. enter! / cloth / skin / cloth / head => Enter! Cloth covers the skin, and cloth covers the head.
22. coach / is important / can be begun / long ago => A coach is important; it can be begun long ago.
23. back nearby / place / beam / frames / to fasten => Back nearby in the place, beams are made into frames and fastened.
24. here / statement / lesson / you / buy / plant => Here is a statement and a lesson: when you buy a plant.
25. here / you / can give / wood transport / public transit / go back / downtown => Here you can give wood transport and public transit; go back downtown.
26. we / moved / residents / school => We moved the residents and the school.
27. they / did / a decision / the land / was divided / many groups => They did make a decision; the land was divided into many groups.
28. the consequence / men / want / equalized / men => The consequence is that men want to be made equal to men.
29. words / are not identical / words / are not few => Words are not the same as words, and they are not few.
30. a fleet / was said / someone / they / will not sail / farther => A fleet was said to someone: they will not sail any farther.
31. someone / cannot say / life / someone / deliberately says / a particular mistake => Someone cannot say life; someone deliberately names a particular mistake.
32. someone / might have been swindled / a circle of friends / might have been provoked => Someone might have been swindled, and a circle of friends might have been provoked.
33. see / was crafted / small hard rod / soft => They see it, since it was crafted with a small hard rod and is soft.
34. is the same / place / act / curiosity => The place stays the same, and we act out of curiosity.
35. I / a past event / was moved / market / others / observe change / others / casual observers => I was moved to the market by a past event; others observe change as casual observers.
36. was neglected / initial / began / the match / began => It was neglected; an initial event began when the match began.
37. a closet / let / us / crush / the amount / lower => The closet let us crush the amount lower.
38. improvements / do not happen / body / special goods / separate => Improvements do not happen to the body; special goods separate.
39. is doubted / improvement / zeal / join / something special / philosophy / join / something special => Someone is doubted when improvement and zeal join something special; philosophy joins something special too.
40. they / did not value / they / not careful / officials / they / did not get / all officials => They did not value it; they were not careful officials, and they did not get all the officials.
41. times / passed / I / saw / them / often / revolution => As times passed, I often saw them go through a revolution.
42. was not quite able / to teach / knowledge / law / match / places => It was not quite possible to teach knowledge and law, which match in places.
43. they / saw / residents / are the same / a crowd / spray / separate / tragedy => They saw residents, who are the same as a crowd; the spray separates tragedy.
44. the others / began to teach / us / give / crops / nearby => The others began to teach us to give crops near Rome.
45. many people / are alike / rule informally / the same / place => Many people are alike and informally govern the same place.
46. the affection / began / well / just now / someone / fell asleep => The affection began well just now; someone fell asleep.
47. the seed / soft / ate / nourishment => The soft seed consumed nourishment.
48. large institution / sleeps / consumes / here / a committee => A large institution sleeps and consumes here when a committee does.
49. others / hated / someone / earlier / someone / later saw => Others hated someone earlier, and someone later saw them.
50. the head / is faint / someone / moved / transport => The head is faint; someone moved transport.
51. old times / someone / changed / outside / harsh winter / motion => Someone changed the old times outside: a harsh winter and motion.
52. died / just now / someone / touched / ground => They died; just now, someone touched the ground.
53. a sun / ray / rose / across the land / warms => A sun's ray rose across the land and warms it.
54. the neck / is tickled / someone / taught / will surely improve => When the neck is tickled, someone taught that things will surely improve.
55. someone / disliked / see / someone / excited / slim / giant / head / stay still / nearby / place => Someone disliked seeing another person who is excited and slim, while a giant head stays still nearby.
56. someone / enlarged / tall bodies / someone / seized / body / someone / hurried / home => Someone enlarged the tall bodies, someone seized a body, and someone hurried home.
57. station / vehicles / very calm => A station of vehicles is very calm.
58. someone / said / someone / idea / the winter / dreads => Someone told someone an idea; the winter dreads.
59. no value / is not very large / the love / identical / lies dormant => There is no value; it is not very large, since the love is identical and lies dormant.
60. someone / murmured / moved / clearly / someone / feels / fool => Someone murmured and moved; clearly someone feels like a fool.
