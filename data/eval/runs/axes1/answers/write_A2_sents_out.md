1. { TEXT(=+3) DO | o agent N+3 D+3 } { SAY THINK | i T-2 } E { PLACE(=-5) VALUE(=+5) | o D+3 } ; { SOMEONE(=-3) | o N+3 } { JOIN(=+3) | i T-2 M-5 } E { PLACE(=-5) VALUE(=+5) | o D+3 } PI { RULE(=+5) TEXT(=+5) | o D+3 }
2. LA [ { SOMEONE(=+5) | o N+3 } { SEE(=+3) | i } E { SHAPE(=+5) TEXT(=-5) | o D+3 } ] ; { SOMEONE(=+5) | o N+3 } { KNOW(=+3) | i } E [ "Af" { JOIN(=+3) LONG | o N+3 } { MOVE INSIDE(=+2) | i } E { PART(=-2) | o N+5 } ]
3. { SAME(=-3) SOMEONE(=-3) | o quality D+3 } { BEGIN(=-5) | i } ; { SAME(=+5) | o } { STRONG(=+5) | i } AGAINST { MOOD FEEL(=-5) | o quality }
4. { CAN | o N+5 D+3 } [ { SOMEONE(=+5) | o } { DO BEGIN(=+5) | i } E { TIME(=+5) HAPPEN | o D+3 } ] { BEGIN(=+5) | i T-2 A+5 }
5. { SOMEONE(=+5) | o N+3 } { FEEL(=+2) GOOD(=-5) | i M-5 } { TIME | e } E { HEAT(=+5) FIGHT(=+5) PART(=-5) | o N+3 } { SAME(=+5) | e } ; { SOMEONE(=-5) | o N+3 } { FEEL(=+2) GOOD(=-5) | i T-2 } { TIME(=-5) | e } E { ABOVE(=+5) LIGHT(=+5) MOVE | o N+3 }
6. { SAME(=+5) | o D+3 } { WANT(=+2) | i K+3 } E { SOMEONE(=-5) | o N+3 } [ { SOMEONE(=-5) | o } { FEEL(=+2) GOOD(=-5) | i T-2 } E { HAPPEN | o result D+3 } PI "Hungary" ]
7. { MANY(=+1) JOIN(=+3) TEXT(=-2) | o N+3 } { DO(=+3) | i V-4 M+4 } { TIME MANY(=0) | e }
8. { CAN | o N+3 D+3 } { MANY(=-1) | i } ; { MEASURE(=-2) MANY(=+5) RULE | o D+3 } { MANY(=+3) | i C+3 M-3 }
9. LA [ { SAY SEE(=+5) | o N+3 C+3 } ] ; { SOMEONE | o } { SAME(=-3) KNOW | i V+4 M+4 } E { SAME(=-3) PART(=-2) | o N+3 } PI { THINK PART(=-5) | o result N+3 }
10. { SAME(=+5) | o D+3 } { JOIN(=+3) | i T-2 } E { RULE(=-5) FEEL(=+5) | o D-3 } PI { KNOW(=+3) PART(=+5) SAY | o N+3 } AND { PART(=-2) DO | o quality }
11. { TRUE MEASURE(=-2) TEXT | o D+3 } { ABOVE(=+2) SAY | a } { GIVE(=+5) | i T-2 } E { VALUE | o D+3 }
12. LA [ { PART(=+5) | o D+3 } PI { TEXT(=+5) | o D+3 } ] ; { SAME(=+5) | o D+3 } { INSIDE(=0) | i M-5 } ; { SAME(=+5) | o D+3 } { INSIDE(=+5) | i }
13. { SOMEONE(=+5) | o } { THINK(=0) TIME(=-2) | i } E [ { SOMEONE(=+5) | o } { MOVE(=-5) ABOVE(=+2) | i T-2 } { PLACE(=-5) INSIDE(=0) | e } ] ; { SOMEONE(=+5) | o } { SEE(=+3) | i T-2 } E [ "Jessica" { DO | i } E { FRIEND(=+2) GIVE(=+5) SEX(=-5) | o agent } ] ; "Jessica" { GIVE(=+2) | i } E { CONSUME(=+5) GRAIN(=-3) TOUCH(=-5) | o N+3 }
14. { SAME(=+5) | o D+3 } { CAN(=+3) | i K+4 T-2 M-3 I+4 } E { HAPPEN | o N+3 D+3 }
15. { SEX(=-5) BEGIN(=-5) LIVE | o agent D+3 } { TOUCH MOVE(=-2) | i T-2 A-3 } E { SOMEONE(=-3) | o } ; { SOMEONE(=-3) | o } { MOVE ABOVE(=-5) | i T-2 A-3 } { TIME | e }
16. { SAME(=-3) | a } { THING(=+4) | o D-3 } LIKE { THING(=0) | o } { MOVE(=-2) ABOVE(=+2) | i T-2 } { BEGIN(=-5) | e } { LAND(=+2) THING(=0) PART(=+5) | o D-3 }
17. LA [ { SOMEONE(=+5) | o } { MOVE INSIDE(=+2) | i T-2 } { BEGIN(=-5) | e } ] ; { SOMEONE(=+5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=+3) | o }
18. { SOMEONE(=-3) | o } { MOVE(=+2) | i T-2 I+4 } { ABOVE(=-5) | e } E { MOVE ABOVE(=-2) | o tool N+3 D+3 } AND { INSIDE(=-5) | e } E { OPEN(=+5) | o D+3 }
19. { SOMEONE(=+5) | o } { SEE(=+3) | i T-2 } E [ { SOMEONE(=-3) | o } { BIG(=+2) | i C+3 } { NEAR(=+3) | e C+3 } ] LA [ { SEE(=+3) FIGHT(=+2) | o tool D+3 } ]
20. { SOMEONE(=-5) | o N+3 } { MOVE GIVE(=+5) | i T-2 } E { GRAIN(=-1) | o } { ABOVE(=0) | e } E { SHAPE(=+5) LONG(=+5) | o D+3 } AND { LONG(=-5) SHAPE(=+5) | o D+3 }
21. { SOMEONE(=-5) | o N+3 } { MOVE(=-2) STRONG(=-5) | i T-2 } { ABOVE(=-2) | e } E { OPEN(=0) GRAIN(=-3) | o N+3 } ; { SOMEONE(=-5) | o N+3 } { CONSUME(=+3) | i T-2 } E [ { LAND(=-2) MOVE | o N+3 D+3 } { JOIN(=0) | i } E { ABOVE(=-5) | o D+3 } ]
22. { SOMEONE(=-3) | o } { KNOW(=+3) | i T-2 } { TIME | e } E { FIGHT(=+2) | o agent D+3 }
23. { SOMEONE(=-3) | o } { MOVE | i T-2 } { SIDE(=+2) | e } E { SOMEONE SEX(=+5) | o D+3 } [ { MOVE(=-5) ABOVE(=0) | i } { LAND(=+5) | e } ] ; { SOMEONE(=-3) | o } { MOVE ABOVE(=-2) | i T-2 } { SEE(=+3) | e } E { SOMEONE(=-3) | o }
24. "Greg" { MOVE ABOVE(=+5) | i T-2 } { JOIN(=+3) | e } E { ABOVE(=+5) PLACE(=-3) | o D+3 } ; "Greg" { MOVE SIDE(=+2) | i T-2 } E { SOMEONE(=-5) | o N+3 } { SIDE(=-5) | e } E { PLACE LIVE | o D+3 }
25. { SOMEONE(=+5) | o } { KNOW(=+3) | i T-2 } { TIME(=-1) | e I+5 } E { HAPPEN | o agent D+3 } [ { SOMEONE(=-3) SEX(=-5) | o } { GIVE(=-2) | i T-2 } E { OPEN(=0) | o } AGAINST { LAND(=-2) ABOVE(=+2) | o } ]
26. { SOMEONE(=+5) | o } { MOOD(=+3) SAY(=-3) | i T-2 } { SAY | e I+4 } ; { BODY(=-3) | o tool D+3 } { MOVE ABOVE(=-5) | i T-2 } { INSIDE(=-5) | e }
27. LA [ { GIVE(=-2) | o agent D+3 } { MOVE TOUCH(=-2) | i T-2 } E { PLACE(=-5) | o D+3 } ] ; "Mike" { GIVE(=-2) | i T-2 } E { FIGHT(=-5) SHAPE(=0) | o D+3 } { TIME(=-1) | e }
28. { SOMEONE(=-3) SEX(=-5) | o } { DO(=-5) | i T-2 } { BEGIN(=+5) | e } { TRUE(=+5) | e } ; { SOMEONE(=-3) SEX(=-5) | o } { THINK(=+5) | i T-2 } { RULE(=-5) | e } { MOOD(=+3) VALUE(=+2) | e }
29. { LIVE(=+3) KNOW(=+5) | o agent } "Fortman" { SAY | i } E [ { MOVE LAND(=-2) | o D+3 } { GIVE DO(=+3) FRIEND(=+2) | i M-3 } E { BODY(=+5) | o D+3 } PI { SOMEONE(=+3) | o } ]
30. { SOMEONE(=-3) | o } { THINK | i T-2 M+3 } E [ { SOMEONE(=+5) | o } { MOVE NEAR(=-5) | i T-2 } ]
