1. { TEXT DO | o agent N+3 D+3 } { SAY | i T-2 } E { VALUE(=+5) | o D+3 } ; { TEXT DO | o agent N+3 D+3 } { JOIN(=-5) | i T-2 } E { SAME | o } { RULE(=+5) TEXT | o D+3 }
2. { SEE | i } E { PLACE SHAPE | o D+3 } LA [ { SOMEONE | o N+3 } { SEE | i } E { "Af" | o } { JOIN LONG | o N+3 } { MOVE INSIDE(=+5) | i } { PART(=-2) | o D+3 N+5 } ]
3. { SOMEONE | o D+3 } { SAME(=-4) | o quality } { BEGIN(=-5) | i } { AGAINST } { FEEL(=-5) TIME(=+3) | o quality }
4. { MANY(=+5) | a } { CAN | o quality } { DO TRUE | i } { SOMEONE(=+5) | o } { HAPPEN TIME(=+3) | o D+3 } { BEGIN(=+5) | i }
5. { SOMEONE(=+5) | o N+3 } { FEEL(=+4) GOOD(=-4) | i M-5 T0 } E { HEAT BIG | o N+3 } { SAME | e } { SOMEONE(=-5) | o N+3 D+3 } { TIME(=-3) FEEL(=+4) GOOD(=-4) | i T-2 } E { SEE HEAT | o N+3 }
6. { SOMEONE(=-5) | o N+3 } { FEEL(=+4) GOOD(=-4) | i T-2 } E { HAPPEN | o result D+3 } ; { WANT | i } E { THING | o }
7. { JOIN(=+4) TEXT | o result N+3 } { DO | i V-4 M+4 } { MANY(=0) TIME | e }
8. { CAN | o N+1 } { MANY(=-1) | a } ; { MEASURE(=-5) RULE | o N+3 D+3 } { BIG | a C+3 } { CAN | e M-3 }
9. { DO KNOW(=+5) | i M+4 } { SAME(=-5) | a } { THING | o N+3 } E { THINK MEASURE | o N+3 }
10. { SOMEONE | o } { JOIN(=+4) | i T-2 } E { SOMEONE(=+5) FEEL(=+4) | o } { SAY | o N+3 }
11. { VALUE | o D+3 } { MEASURE(=-5) | i T-2 } { "Af" | e } { ABOVE KNOW TRUE | o N+3 D+3 }
12. { TEXT | o D+3 } { PART(=+2) | i M-5 } { SIDE(=0) | a } ; { SIDE(=+5) INSIDE(=+5) | a }
13. { SOMEONE(=+5) | o } { KNOW | i T-2 } E [ { SOMEONE(=+5) | o } { MOVE(=-5) ABOVE | i } { PLACE | o } { SEE | i } E { SOMEONE(=-5) SEX(=-5) | o } { DO | i } E { SOMEONE | o } { CONSUME(=+5) | i } { GRAIN(=-3) TOUCH(=-5) | o N+3 } ]
14. { HAPPEN | o D+3 } { DO CAN(=+5) | i T-2 R-3 } E { THING | o N+3 } { CAN(=+5) | a I+4 C+3 }
15. { SOMEONE SEX(=-5) | o D+3 } { TOUCH(=+3) | i T-2 } E { SOMEONE SEX(=+5) | o D+3 } ; { SOMEONE SEX(=+5) | o D+3 } { MOVE ABOVE(=-5) | i A-5 T-2 }
16. { THING(=+4) BODY LAND | a } { MOVE ABOVE(=+5) | i T-2 } { GRAIN(=+5) THING(=0) | o N+3 } { PLACE | o }
17. { SOMEONE(=+5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=+3) | o } { TIME(=-1) BEGIN(=-5) NEAR(=+5) INSIDE(=+5) | e }
18. { SOMEONE | o D+3 } { MOVE(=+3) ABOVE(=-5) | i T-2 } E { SHAPE(=+5) ABOVE | o N+3 } AND { MOVE INSIDE(=-5) OPEN(=+5) | i T-2 }
19. { SEE | i T-2 } E { SOMEONE | o D+3 } [ { BIG | i C+3 } ] ; { SEE | o tool D+3 }
20. { SOMEONE(=-5) | o N+3 } { MOVE NEAR | i T-2 } E { GRAIN(=0) LAND | o } { SHAPE(=+5) LONG(=+5) | o D+3 } AND { LONG(=-5) SHAPE(=+5) | o D+3 }
21. { SOMEONE(=-5) | o N+3 } { MOVE(=-3) FEEL | i T-2 } { TOUCH(=-5) GRAIN(=-3) | o } { OPEN(=0) | o N+3 } ; { CONSUME(=+5) | i } E { GRAIN(=-3) SAY | o N+3 }
22. { SOMEONE | o D+3 } { KNOW(=+5) | i T-2 } { TIME(=0) } E [ { THING | o } { SOMEONE | o } { FIGHT | i } ]
23. { SOMEONE | o D+3 } { MOVE | i T-2 } { SIDE(=+5) ABOVE(=+5) | e } E { SOMEONE | o D+3 } [ { MOVE(=-5) LAND(=+5) | i } ] ; { ABOVE(=-5) CHANGE SEE | i T-2 }
24. { SOMEONE "Greg" | o } { MOVE ABOVE | i T-2 } { PLACE ABOVE INSIDE(=0) | e } ; { SIDE(=-5) MOVE | i K+5 T-2 } E { SOMEONE(=-5) | o N+3 }
25. { TIME(=-1) | e } { SOMEONE(=+5) | o } { KNOW | i T-2 } E [ { SOMEONE SEX(=-5) | o } { OPEN(=-5) ABOVE | o } { PART(=+2) | i T-2 } ]
26. { SOMEONE(=+5) | o } { MOOD(=+5) SAY | i T-2 } ; { SAY | o tool D+3 } { MOVE ABOVE(=-5) INSIDE(=-5) | i T-2 }
27. { "Mike" | o } { GIVE(=-5) | i T-2 } E { FIGHT(=-5) SHAPE(=0) | o D+3 } { TIME(=-1) | e } ; { FIGHT(=-5) SOMEONE | o agent D+3 } { MOVE ABOVE(=-5) | i T-2 } { SHAPE(=+5) | o D+3 }
28. { SOMEONE SEX(=-5) | o } { MOVE(=-5) | i T-2 } { TIME(=+5) | e } { TRUE | e } ; { THINK(=+5) | o result } { SAME(=+5) | a } { RULE(=-5) STRONG | a } AND { FRIEND | a }
29. { KNOW(=+5) "Fortman" | o agent } { SAY | i } [ { MOVE LAND(=-5) | o } { GIVE CAN(=+4) | i T+2 } E { BODY | o D+3 } ]
30. { SOMEONE | o D+3 } { THINK | i T-2 R-3 M+4 } E [ { SOMEONE(=+5) | o } { MOVE NEAR(=-5) | o agent } ]
