1. { HEAT(=+5) TIME | o I+4 } AND { HEAT(=+5) PLACE | o N+3 } { TIME(=+3) HEAT | o } { FRIEND(=-5) | i M-5 } { BODY LONG | o D+3 N+3 } ; { HAPPEN FRIEND(=-5) | i } E { BODY LONG | o D+3 N+3 }
2. { SOMEONE | o N+3 } { THINK(=+3) | i } [ { SAME | o } ] ; { SEE | i M-5 T+2 } E { SAME(=-5) | o } { RULE(=+5) THING | o N+3 } AND { SAME(=+3) THING | o N+3 }
3. { WANT(=+5) | o } { SOMEONE(=+5) | o } { GIVE(=+5) | i T-2 } { SOMEONE | o } { MANY(=-5) | o } AND { WANT | o } { CARE(=+5) | i }
4. { KNOW CARE | o agent } { PLACE | o PI } { MOVE ABOVE(=-5) | i T-2 } [ { SEE | i } E { SOMEONE | o } { FIGHT(=-5) | o agent } { HAPPEN FRIEND(=-5) | i } ]
5. "White" { SAY | i } E [ { THINK | i } ] { CARE | e } AND { FEEL(=-5) | e } ; { JOIN(=-5) SEE | i M-5 }
6. { SOMEONE | o } { SEE | i V-4 T-2 } { TIME | e I-2 } ; { SOMEONE | o } { BODY MOVE | i T-2 SIDE(=-5) } E { BODY | o } [ { MOVE(=+4) | i } ]
7. { GOOD(=+4) TEXT | o D+3 I+4 } AND { KNOW(=+4) WANT(=+4) INSIDE(=+5) | o } { ABOVE(=+5) | o }
8. { SOMEONE | o } { ART(=-5) KNOW | o agent } ; { SOMEONE | o } { KNOW(=+4) | i } E { TEXT | o N+3 } { TIME(=-5) | o } ; { SOMEONE | o } { GOOD DO PLACE | o agent } AND { GOOD }
9. { SOMEONE | o } { KNOW | i T-2 } [ { MANY(=+3) SOMEONE | o } { DO | i T-2 } E { WANT | o result } { SOMEONE(=+5) | o } ]
10. { SEE | o result I-2 } { SEE | i } [ { LONG(=+5) ABOVE(=+5) PART | o D+3 } { PART | o PI } { LONG | o } { LONG | o } ] { LONG | i }
11. { SOMEONE | o N+5 } { PLACE | o D+3 N+5 } { DO | i } E { CONSUME(=+5) GRAIN(=-3) | o N+3 } { PART(=-5) THING | o N+3 }
12. { SOMEONE | o } { CONSUME(=+5) | i T-2 M-5 } E { MANY(=-5) THINK | o } AND { MANY(=-5) SAY | o } ; { SAY | i T-2 } [ { WANT | i T-2 I+4 } ]
13. { MANY(=+3) TOUCH | o } { SEE | i } [ { SOMEONE | o N+3 } { SEE KNOW | i } E { THING | o } { FEEL | o } ]
14. "John" { MOVE(=+4) SIDE(=+5) | i T-2 } [ { JOIN(=+5) | i } ] ; { THING(=+4) SAME(=-5) | o N+3 } { MOVE(=+4) SIDE(=-5) | i T-2 } E { SOMEONE | o } { LONG | o } ; { MANY(=+3) | o } { THING | o } { GRAIN(=-3) BODY | o } { BODY | i T-2 }
15. { SOMEONE | o N+3 } { DO | i T-2 } E { DO | o tool } [ { BEGIN(=-5) HEAT SEE | i } ] ; { DO | o tool } { DO | i T-2 } E { MOVE(=+5) | o N+3 }
16. "Martin" { SAY | i T-2 } [ { LAND | o N+3 D+3 } { SOMEONE | o agent N+3 } ] { MOVE(=-5) TIME | i ! } AND { CARE | i ! }
17. { SOMEONE(=+5) | o N+3 } { KNOW | i } [ { SOMEONE | o } { GIVE(=+5) | i T-2 } E { RULE(=+5) | o D+3 } { MANY(=+5) | o } { SOMEONE | o agent N+3 } ]
18. { SOMEONE | o N+3 } { KNOW(=+5) | i T-2 C+3 } { CAN(=+3) | i T+2 } E { HAPPEN | o N+3 }
19. LA [ { SOMEONE(=+5) | o N+3 } { THINK | i } E [ { SOMEONE | o N+5 } { CHANGE | i } { TIME(=-1) | e } { SAME(=+5) | e } ] ] ; { MOVE | i V+4 } E { PLACE SAME(=-5) | o }
20. { DO | o N+1 } { DO | i T-2 } E [ { BEGIN(=-5) | i } { MOVE(=+4) | e } ] ; { MOVE | i T-2 }
21. { SOMEONE | o N+3 } { DO | i T-2 } E { GRAIN | o } ; { CAN(=-3) SEE | i } [ { SOMEONE | o N+3 } { FIGHT | i } { TIME(=+1) BEGIN | e } ]
22. { SOMEONE | o } { MOVE ABOVE(=+5) | i T-2 } { SEE | i } E "Kate" ; { BODY SAY | o N+3 } { MOVE(=+5) | i T-2 }
23. { NEAR(=+5) | e } { SOMEONE(=-5) | i } ; { NEAR(=+5) | e } { THINK | o result } { SOMEONE(=+5) | o } AND { THINK(=+5) | o result }
24. { THING(=+4) | o N+5 } { MOVE(=-5) | i } ; { THING(=+4) BIG | o N+3 } { LIVE(=-2) | i } { HEAT(=-5) TIME | e }
25. { MANY(=+5) SOMEONE | o N+3 } { WANT | i I+4 } E { VALUE(=-5) | i }
26. { TIME(=-2) SAME | e } "Hengesbach" { WANT(=-3) FRIEND(=-3) | i T-2 A-2 } AND { MOOD(=-3) }
27. { DO | i } E { PART | o } { CAN(=+5) | i C+3 } { CHANGE(=+5) THING(=-5) | o N+3 } ; { TIME | o } AND { VALUE | o } { GIVE(=+5) | i }
28. { VALUE(=-5) PLACE | o N+3 } { VALUE(=-5) | i } E { CONSUME(=+5) | o N+3 } ; { SOMEONE | o N+3 } { SAY | i } [ { CONSUME(=+5) | o N+3 D+3 } { GOOD | i } ] ; { MANY(=-1) GOOD INSIDE(=+5) | i } E { BODY | o }
29. { THING | o D+3 } { WANT | i } [ { PART | o N+3 } { LAND | o N+3 } { GIVE(=0) | i K0 } E { VALUE | o } { MEASURE(=-5) MANY(=+5) | e } { DO | o result } { SOMEONE(=-5) | o } ]
30. { TIME(=-1) | e } "Claude" { SEE | i T-2 } E [ { CARE(=-5) | o } ] ; { KNOW(=+5) CAN | i T-2 I+4 } [ { DO CHANGE | i } ]
---
1. Very hot seasons and hot places bring future heat that does not harm the beams; harm comes to the beams.
2. People decide the same thing; they will not see the difference between laws and ordinary things.
3. My love gave someone nothing, and love takes care.
4. A caregiver in a place went down while seeing an athlete come to harm.
5. White says to think carefully and calmly; they do not see the separation.
6. Someone was seen a little while ago; someone went back carrying a body, hurrying.
7. Very good writing and a strong inner desire to learn, above all.
8. Someone is a scientist; someone teaches ancient texts; someone does good for a place, and is good.
9. Someone knew that many people did what I wanted.
10. I catch a glimpse of the top part, a section within the long rods, which is long.
11. All people in all the places drink liquids and eat crumbs of things.
12. Someone read no thought and no speech; they said they very much wanted it.
13. One sees many touches, as people understand things and feelings.
14. John rushed ahead and joined in; different animals hurried back to someone's rod; many things, bodies of liquid, took form.
15. People made tools and saw fire begin; the tools worked to speed things up.
16. Martin said to the lands and the people: stop now, and be careful!
17. We know that someone gave the law to all the people.
18. People knew more, and will manage events more easily.
19. If we think all people change just now in exactly the same way, we deliberately move to another place.
20. Someone did a few things by starting quickly; then they moved.
21. People made grain; it is hard to see people beginning to quarrel soon.
22. Someone went up and sees Kate; gestures rushed.
23. Here they are; here is my idea and a decision.
24. All animals stand still; big animals sleep through the winter.
25. All people very much want to buy and sell.
26. Earlier, Hengesbach started to dislike someone, and felt sad.
27. Do your part; you can change inanimate things more easily; give time and value.
28. Markets sell food; people say the food is good; a few are good inside and look after the body.
29. The thing wants its parts and lands to let value be given in full, as a result for others.
30. Claude just saw a mistake; they knew very well how to make changes.
