1. { PART(=+5) MOVE LAND(=-5) | o agent } { SAY | i T-2 } E "Hudson" [ { SOMEONE(=-5) | o } { MOVE LAND(=-5) | i T+2 M-5 } { NEAR(=-5) | e C+3 } ]
2. { RULE(=+4) BIG | o agent } AND { RULE(=+4) PART | o N+3 D+3 } { LIVE(=-2) | i } AND { CONSUME(=+5) | i } { NEAR(=+5) | e }
3. { HAPPEN | o result D+3 } { SOMEONE(=-5) | o N+3 D+3 } { WANT | i } [ { SAME | i V-4 } E { SOMEONE SEX(=+5) | o N+3 } ]
4. { CHANGE LIVE GRAIN | o N+3 D+3 } { DO | i M-5 } E "iodide" { JOIN DO | o tool } ; { CHANGE LIVE GRAIN | o N+3 D+3 } { DO JOIN(=-5) | i } E { LIVE DO | o quality }
5. { TIME(=0) KNOW(=0) SAME(=+5) | o D+3 } ; { MANY(=+5) SOMEONE | o } { SEE | i T-2 CAN } E [ "U.S." { KNOW(=0) SAME(=+5) | e } { RULE(=+4) | i T-2 C+5 } ]
6. { SOMEONE(=+5) PART | o } { MOVE | i T-2 } { NEAR(=0) | e } E { PLACE LIVE | o D+3 } AND { KNOW(=+5) PLACE | o D+3 }
7. { TIME(=-2) | a } { THING(=0) GRAIN(=+5) | o N+3 D+3 } { CONSUME(=+5) LAND(=-5) | i T-2 } PI { BODY CONSUME | o }
8. { SOMEONE(=+5) | o } { SAY | i V+4 } ; { SOMEONE(=+5) | o } { WANT(=+3) | i T-2 C+3 } E { ART(=+5) DO | o D+3 } [ { TOUCH(=+5) INSIDE(=0) | o D-3 } { JOIN | i } ]
9. LA [ { SOMEONE(=-5) | o } { SEE | i T-2 A+5 } E { TIME CAN | o D+3 } ] ; "Gilman" { SAY | i A-5 T-2 } E { SOMEONE(=-5) | o }
10. { SAME | e } { PLACE | o D+3 } FOR { DO VALUE(=+5) WANT | o quality }
11. LA [ { SAME(=+5) KNOW | a } { WANT(=+5) | o D+3 } { VALUE(=+5) | i } ] ; { MEASURE(=-5) VALUE | o M-5 } { BIG | i I+5 }
12. { ART(=+5) SAY | o result N+3 D+3 } { KNOW(=+3) | a } AND { MOOD(=+3) | a } { FEEL(=-3) CARE | i I+5 } ; { MOOD(=-5) ART(=+5) SAY | o result N+3 } { FEEL(=+5) | i C+3 I+1 }
13. { SOMEONE SEX(=+5) | o D+3 } { FRIEND SEE | i C+5 } ; { FEEL(=+5) WANT | o quality D+3 } { MOOD(=-3) | i } ; { SOMEONE SEX(=+5) | o } { FRIEND WANT(=+3) | i V-4 }
14. LA [ { BODY SEE | o D+3 } { LIVE(=-1) SEE | i } ] ; "Summers" { MOVE | i T-2 } E { PLACE MOVE LAND(=+5) | o D+3 }
15. { JOIN | i ! } E { LONG(=-5) JOIN | o D+3 } { NEAR(=+5) | e } { ABOVE(=-5) BODY | o } AND { LONG(=-5) ABOVE BODY | o }
16. { RULE ART(=-5) | o result N+3 } { JOIN | i } E { MANY(=+3) PART(=-2) TIME | o N+3 } PI { FIGHT(=-5) | o }
17. { MOVE | o tool N+3 D+3 } PI { PLACE MOVE | o D+3 } { FEEL(=+5) GOOD(=-5) | i T-2 I+3 }
18. LA [ { TIME HEAT(=-4) | o D-3 I+4 } ] ; { MEASURE(=-5) VALUE | o N+3 D+3 } { CHANGE(=-5) | i T-2 V-4 }
19. { TIME PART(=+2) BIG | o D+3 } { BEGIN(=-5) | i T+2 M+2 } ; { JOIN(=-5) SOMEONE | o quality D+3 } { BEGIN(=0) | e } { CAN(=-3) HAPPEN | i C+5 }
20. LA [ { SOMEONE SEX(=-5) | o } { SEE | i T-2 } E { SOMEONE SEX(=+5) | o } ] ; { SOMEONE SEX(=-5) | o } { WANT(=-5) | i T-2 R-3 } E { SOMEONE SEX(=+5) | o }
21. LA [ { SOMEONE SEX(=+5) | o } { SEE | i T-2 } E { SOMEONE SEX(=-5) | o D-3 } { FEEL(=+3) | a } AND { BODY BIG(=-3) | a } AND { LONG(=-5) BODY ABOVE | o D-3 } { BIG | a } { MOVE(=-5) | i } { NEAR | e } { PLACE INSIDE(=0) | o D+3 } ] ; { SOMEONE SEX(=+5) | o } { WANT(=-3) | i T-2 }
22. { MANY(=+5) | e M-5 } { CAN(=+5) | i T-2 } ; { CHANGE(=+3) | i } E { THINK KNOW | o result } AND { RULE THINK | o result } [ { SAME(=+5) | i T+2 } E "2" { HAPPEN | o result } ]
23. { TIME(=-5) HAPPEN | o D+3 } { MOVE(=+3) | i K+5 T-2 } E { SOMEONE SEX(=+5) | o D+3 } { NEAR(=-5) | e } { PLACE VALUE(=-5) | o } ; { SOMEONE SEX(=+5) | o } { CHANGE SEE | i V+4 } E { SOMEONE SEX(=+5) | o } { RULE(=-5) SEE CARE | o agent }
24. { TIME(=-3) | o D-3 } ; { GRAIN(=-3) HEAT CONSUME | o D+3 } AND { MOVE GIVE | o } { CHANGE | i T-2 R-3 } E { SOMEONE SEX(=+5) | o } { INSIDE(=-5) | e }
25. { SEE | e } { KNOW(=+5) PLACE | o M-5 } FOR { SAY CHANGE | o } AND { THINK FIGHT(=+5) | o }
26. { SOMEONE SEX(=+5) | o } { FRIEND(=-5) GIVE(=-5) VALUE | i V-4 M-3 T-2 } ; { LIVE JOIN PART | o D+3 } { FRIEND(=-5) SAY | i V-4 M-3 T-2 }
27. { SOMEONE SEX(=-5) | o } { SAY | i T-2 } ; { SOMEONE SEX(=-5) | o } { CONSUME(=+5) SAY | i T-2 R-3 } E [ { PLACE DO | o D+3 } { BEGIN(=+5) | i T-2 A-3 } ]
28. LA [ { BODY JOIN(=-5) | o D+3 } PI { BODY ABOVE | o D+3 } { FEEL(=+3) TOUCH(=-3) | i } ] ; "Dan" { KNOW(=0) | i T-2 } E [ { CHANGE(=+3) LIVE(=+5) | i T+2 M+4 } ]
29. { LAND DO | o agent N+3 D+3 } { KNOW | i T-2 C+3 } E "Washington" ; { LAND DO | o agent N+3 D+3 } { CHANGE NEAR(=+3) | i T-2 } E { NEAR(=-5) LONG | o D+3 } AND { GIVE(=+5) | i T-2 } E { GRAIN LAND(=+5) | o }
30. LA [ { THINK(=+5) TEXT | o result D+3 } { SAME(=-4) | i T-2 M-3 C+3 I+4 } ] ; { THINK(=+5) TEXT | o result D+3 } { TOUCH(=+5) | i T-2 C+3 I+3 } E { TIME(=-2) THINK(=+5) TEXT | o result D+3 }
31. { SOMEONE SEX(=+5) | o D+3 } { SEE | i T-2 } E [ "Skopas" { SOMEONE PLACE | o N+3 } { SAME | i } ] ; { LAND(=+5) INSIDE LAND(=-5) | o quality D+3 } { JOIN(=-5) | i } E { MOOD(=-5) | o }
32. LA [ { FIGHT | o D+3 } { BEGIN(=-5) | i T-2 } ] ; { CARE(=-5) | i V-4 T-2 } AND { BEGIN(=-5) | a }
33. { SOMEONE(=-5) | o } { CONSUME(=+5) | i T-2 } E { RULE DO | o result D-3 } ; "Louisiana" { PART(=-2) | i V-4 T-2 } E { LAND PART(=-2) | o N+3 } "5"
34. { SOMEONE(=+5) | o } { BEGIN(=-5) | i T-2 } E { SAY NEAR(=-5) | o result N+1 }
35. { BODY ABOVE(=-5) SIDE(=-5) | o N+3 } { DO VALUE(=+5) | i } E { SEE BODY LONG | o D+3 }
36. { JOIN(=-5) GRAIN(=-3) | o tool D-3 } PI { LONG(=0) | o D+3 } { DO | i T-2 K0 } E { SOMEONE(=+5) | o N+3 } { JOIN(=-5) MEASURE(=-5) | i } E { TOUCH(=+5) MEASURE(=0) | o D+3 } { ABOVE(=-5) | e C+3 }
37. { SOMEONE SEX(=+5) | o } { SAY | i T-2 } E { THINK MEASURE | o result } PI { HEAT HAPPEN | o D+3 } ; { THINK MEASURE | o result D+3 } { FEEL(=-3) | i T-2 }
38. { SOMEONE(=-5) | o N+3 } { GIVE(=+5) VALUE | i V-4 T-2 C-3 } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { KNOW(=+5) RULE(=+4) | o agent } ; { SOMEONE(=-5) | o N+3 } { GIVE(=0) | i T-2 M-5 } E { FRIEND GIVE(=+5) | o result D+3 } FOR { DO JOIN | o agent N+5 }
39. { SEE | i N+3 } LA [ { DO ART | i V-4 T-2 } { JOIN(=-4) TOUCH(=+4) | a M-5 } { JOIN(=-4) TOUCH(=+4) | o tool } ]
40. { PART(=-2) RULE(=+5) | o agent D-3 } { SAY(=+4) | i V-4 } E [ { SEE CARE(=+5) | i T+2 } ]
41. { JOIN FRIEND | o D+3 } { GOOD BEGIN(=-5) | i T-2 V-4 } { TIME(=-3) HEAT(=-2) BEGIN(=+5) | e } ; { JOIN FRIEND | o D+3 } { LIVE(=-1) | i T-2 A-3 } { TIME(=0) | e }
42. { WANT | o quality D+3 } { CONSUME(=+5) SAY | i T-2 } E [ { RULE(=+5) SAY JOIN | o N+3 M-5 } { HAPPEN | i T+2 } ]
43. { CARE LIVE | o D+3 N+5 M-5 } { SIDE(=+5) GOOD | i V-4 }
44. LA [ { SOMEONE(=+3) | o } { MOVE VALUE(=-5) | i } E { THING(=0) GRAIN(=0) | o N+3 } ] ; { NEAR(=+5) | e } { SAY(=0) KNOW(=+5) | o result D-3 }
45. LA [ { TIME PART(=+2) BIG | o N+3 } { MOVE | i T-2 } ] ; { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) | o } { MANY(=+5) TIME | e } { HEAT(=+5) HAPPEN MOVE(=+5) | o }
46. { THINK(=+2) | i V-4 } E [ { CHANGE LIVE GRAIN | o } AND { FEEL(=+5) ART(=-5) | o } { JOIN | i } E { DO PART(=-2) | o D+3 } ; { THINK CHANGE LIVE | o } { JOIN | i } E { DO PART(=-2) | o D+3 } ]
47. { NEAR(=+5) | e } { SOMEONE(=+3) | o } { GIVE(=0) | i CAN } E { MOVE | o tool D-3 } AND { MOVE RULE(=+4) | o tool } ; { SIDE(=-5) MOVE | i } { NEAR(=+5) PLACE | o }
48. { HEAT SEE | o tool D-3 } { JOIN ABOVE | i V-4 T-2 } { LONG(=0) BIG(=-3) | o D-3 } ; { GIVE(=+5) | i } E { SEE HEAT | o }
49. { SOMEONE(=0) | o } { SAY | i CAN M-5 } E { LIVE | o quality } ; { SOMEONE(=0) | o } { SAY | i V+4 } E { SAME(=-5) CARE(=-5) | o D+3 }
50. { KNOW(=+5) BODY MOVE | o D+3 } { VALUE(=+5) | i } ; { BEGIN(=-5) | i V-4 CAN } { TIME(=-2) LIVE(=+5) | e I+4 }
51. { SOMEONE SEX(=+5) BIG(=-3) | o D+3 } { KNOW(=+1) | i A-3 T-2 } E { LAND DO PART(=+5) | o N+3 } [ { MOVE GIVE | i T-2 } E { THING(=0) CONSUME | o N+3 } { INSIDE(=+5) | e } "Rome" ]
52. { SOMEONE SEX(=-5) | o } { CHANGE BIG | i } E { BODY LONG(=0) | o N+3 } ; { SOMEONE SEX(=-5) | o } { GIVE(=-2) | i T-2 } E { LONG(=-5) BODY | o N+3 D+3 } ; { SOMEONE SEX(=-5) | o } { MOVE(=+3) INSIDE(=-5) | i T-2 } E { PLACE INSIDE | o D+3 }
53. { SOMEONE SEX(=+5) | o } { SAY(=-3) | i T-2 } AND { MOVE(=+3) | i T-2 } ; { SEE | e } { SOMEONE SEX(=+5) | o } { FEEL | i } E { KNOW(=-5) SOMEONE | o }
54. { FEEL(=+5) GOOD(=-5) | o quality } { HAPPEN | i } { TIME(=-3) | e } "1950" ; { TEXT | o D+3 } { SAY | i } AND { ART(=+5) CAN | o result N+3 } { SEE | i K+3 }
55. LA [ { SOMEONE SEX(=+5) | o } { TOUCH(=+5) | i T-2 } E { LAND(=+5) | o D+3 } ] ; { SOMEONE SEX(=+5) | o } { LIVE(=-5) | i T-2 R-3 }
56. { SIDE(=-5) NEAR(=+3) | e } { PLACE | o D+3 } FOR { MOVE LONG(=0) | o N+3 } ; { LONG(=0) JOIN | o N+3 D+3 } { PLACE | i }
57. LA [ { MANY(=0) SOMEONE | o } { BEGIN(=-5) | i T-2 } E { SAY TIME(=+2) GIVE | o result N+3 } ] ; { MANY(=-5) | o } { KNOW | i } E [ { PLACE | o } { SAY TIME(=+2) GIVE | o result N+3 } { BEGIN(=+5) | i T+2 } ]
58. { HAPPEN | o D+3 } { SAME(=+5) | i M-5 I+4 } E { SAY JOIN | o D-3 }
59. { MANY(=+5) SOMEONE FRIEND(=-5) | o } LIKE "Coughlin" { RULE(=+4) | i } E { HAPPEN | o D+3 } { MANY(=+5) SAME(=-5) | e }
60. LA [ { BODY ABOVE | o N+3 } { CAN TOUCH(=+5) | o quality } ] ; { LONG(=0) TOUCH(=+5) | o D-3 } { SAY GOOD | i V-4 }
---
1. A sailor said to Hudson that they would not sail any farther.
2. A great ruler and the officials sleep and eat here.
3. As a result, the others want to be treated the same as men.
4. The bacteria do not use iodide as a catalyst; they break down metabolic processes.
5. The present situation is the same; everyone could see that the U.S. once had the greatest authority.
6. We moved close to the house and the school.
7. The former seeds drank water found in the stomach.
8. I deliberately say so; I wanted more of the arts to join a rigid boundary.
9. If they had seen the opportunity, Gilman started telling them.
10. The same place is meant for great ambition.
11. If someone is fully aware of a craving that matters, the cost is not big at all.
12. The poems are famous and cheerful, and they are utterly careful and calm; tragic poems are slightly more intense.
13. The man looks the friendliest; the passion is sad; a man is liked by friends.
14. If the eyes see faintly, Summers moved onto the road.
15. Sew the thread here to the foot and the sock.
16. Technical rules join many rounds in a game.
17. The vehicles in the station were badly upset.
18. If winter is very cold, the prices were kept unchanged.
19. The long era will probably begin; the separation continues and is most unlikely to occur.
20. If a woman saw a man, a woman had earlier hated a man.
21. If a man saw a glad, small woman with big hair standing near the doorway, he disliked her.
22. It was never easy to change understanding and principles; they will equal two outcomes.
23. The ancient event forced the man far to the market; the man deliberately watches a private detective.
24. At an earlier time, the hot drink and a delivery had changed a man outside.
25. Visibly, no school exists for language change or for a battle of ideas.
26. A man may have been robbed; the community may have been denounced.
27. A woman said so; another woman had heard that the workplace was beginning to close.
28. If the neck feels tender, Dan knew he would certainly recover.
29. The farmers knew Washington better; they came closer to the cable and donated soil.
30. If the decree was perhaps much more unusual, it was far harsher than the earlier decree.
31. The man saw that Skopas's people are alike; island isolation keeps tragedy away.
32. If the quarrel began, the carelessness was blamed, and it was the initial one.
33. They adopted a rule; Louisiana was divided into 5 parts.
34. I started saying a few foreign words.
35. The heels greatly value the eyelashes.
36. A filter in the wire let us remove the pressure further down.
37. The man said an assessment of the fire; the assessment was calm.
38. They were paid less; they did not deal with the educators; they got no donation for all members.
39. If art was made with a blunt knife, you see it.
40. A lawyer is loudly told to watch carefully.
41. The marriage was well started late last autumn; it was only just beginning to live now.
42. The wish was heard: no official agreements would happen.
43. No healthcare is being improved.
44. If you trade grains, here is an announcement.
45. If ages passed, I always saw them as a fiery rush.
46. It is thought that bacteria and technology take on the same role; biology does too.
47. Here you can get a vehicle and a travel permit; one returns to this place.
48. A lamp was hung above a small rod; it gives light.
49. Nobody can express life; someone deliberately names the opposite mistake.
50. Physiology is vital; it can be begun very early in life.
51. The little man began to know a bit about the nations that sent food into Rome.
52. A woman grows large with body hair; she borrowed the clothes; she rushed out of the house.
53. A man murmured and hurried; visibly, he feels like a fool.
54. Anguish happens before 1950; the text says so, and it makes skills show.
55. If a man struck the ground, he had already died.
56. The back area is meant for rails; the cables are placed.
57. If some people began making promises, no one knows where promises will end.
58. The event is utterly unlike an agreement.
59. All enemies like Coughlin always rule the event differently.
60. If heads are strong, a rigid rod is praised.
