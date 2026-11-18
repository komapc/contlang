1. { TEXT(=+3) | o agent N+3 } { SAY(=0) THINK(=0) | i T-2 } E { VALUE(=+5) | o D+3 } ; { TEXT(=+3) | o agent N+3 } { JOIN(=-5) | i T-2 } E { VALUE(=+5) | o D+3 } PI { RULE(=+5) | o D+3 }
2. LA [ { SOMEONE(=+5) | o N+3 } { SEE(=+3) | i } E { TEXT(=-5) | o D+3 } ] ; { JOIN(=+3) | o N+3 } { MOVE(=0) INSIDE(=+2) | i } { PART(=-2) | o N+5 }
3. { SOMEONE(=-3) | o } { SAME(=-3) | o quality } { BEGIN(=-5) | i } { FIGHT(=+2) | e } { MOOD(=-3) | o quality M-5 }
4. { TRUE(=+2) | o N+5 } { DO(=+3) | o } { BEGIN(=+5) | i }
5. LA [ { SOMEONE(=-5) | o } { FEEL(=+2) | i T-2 M-5 } E { HAPPEN | o D+3 } ] ; { SOMEONE(=+5) | o N+3 } { FEEL(=+2) | i M-5 } E { FIGHT(=+5) | o tool N+3 } { SAME(=+5) | e }
6. { HAPPEN | o D+3 } { WANT(=+2) | i } E { SOMEONE(=-5) | o N+3 } [ { SOMEONE(=-5) | o } { FEEL(=-3) | i T-2 } ]
7. { JOIN(=+3) | a } { TEXT(=-5) | o N+3 } { DO(=+3) | i V-4 T+2 M+4 } { TIME(=0) | e N+3 }
8. { CAN(=0) | o N+1 } { MANY(=-1) | i } ; { RULE(=0) | o N+3 } { MEASURE(=-2) | o D+3 } { MANY(=+3) | i C+3 M-3 }
9. LA [ { SOMEONE(=0) | o } { KNOW(=+3) | i } E { SAME(=-3) | o N+3 } ] ; { SOMEONE(=0) | o } { SEE(=+3) THINK(=0) | i M+4 } E { SAME(=-5) | o N+3 }
10. { SOMEONE(=-3) | o D+3 } { JOIN(=+3) | i T-2 } E { SOMEONE(=-5) | o } { GOOD(=+2) | o } { PART(=+5) | o N+3 } { SAY(=0) | o N+3 }
11. { VALUE(=0) | o D+3 } { JOIN(=-5) | i T-2 } { TEXT(=0) | o N+3 }
12. LA [ { VALUE(=0) | o } PI { TEXT(=+5) | o D+3 } ] ; { INSIDE(=0) | i M-5 } ; { INSIDE(=+5) | i }
13. { SOMEONE(=+5) | o } { KNOW(=0) | i R-3 } E [ { SOMEONE(=+5) | o } { MOVE(=-5) ABOVE(=+2) BODY(=+5) | i } { INSIDE(=0) | e } { PLACE(=-5) | o } ; { SOMEONE(=+5) | o } { SEE(=+3) | i } E "Jessica" { DO(=+3) | i } E { SOMEONE(=-3) | o agent } ; { SOMEONE(=-3) | o } { GIVE(=+5) | i } E { CONSUME(=+5) | o } { TOUCH(=-5) | a } { SOMEONE(=-5) | o N+3 } ]
14. { HAPPEN | o D+3 } { CAN(=+3) | i T-2 C+3 R-3 }
15. { SOMEONE(=-3) | o agent } { TOUCH(=0) | i T-2 } E { SOMEONE(=-3) | o } ; { SOMEONE(=-3) | o } { MOVE(=-2) ABOVE(=-5) | i T-2 }
16. { THING(=0) | o } { SAME(=-3) | o } { MOVE(=+5) ABOVE(=+2) | i T-2 } { NEAR(=-2) | e } { LAND(=+2) | o } { THING(=0) | o N+3 }
17. { SOMEONE(=+5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=+3) | o } { BEGIN(=-5) | e } { MOVE(=0) INSIDE(=+2) | i T-2 }
18. { SOMEONE(=-3) | o } { MOVE(=0) ABOVE(=-5) SIDE(=0) | i T-2 I+3 } E { LONG(=+5) | o N+3 } AND { OPEN(=+5) | o D+3 }
19. { SOMEONE(=+5) | o } { SEE(=+3) | i T-2 } E { SOMEONE(=-3) | o } { BIG(=+2) | i C+3 } AND { BIG(=+3) | i C+3 }
20. { SOMEONE(=-5) | o N+3 } { TOUCH(=0) GRAIN(=-1) | i T-2 } { LAND(=+5) | o D+3 } { LONG(=+5) | o } AND { LONG(=-5) | o D+3 }
21. { SOMEONE(=-5) | o N+3 } { SHAPE(=0) STRONG(=-5) | i T-2 } { OPEN(=0) | o N+3 } ; { SOMEONE(=-5) | o N+3 } { CONSUME(=+3) | i T-2 } E { LAND(=-2) | o N+3 } { MOVE(=-2) | i } { NEAR(=+3) | e } { ABOVE(=-5) | o D+3 }
22. { SOMEONE(=-3) | o } { KNOW(=+3) | i T-2 } E [ { SOMEONE(=-3) | o } { FIGHT(=+2) | i } ]
23. { SOMEONE(=-3) | o } { MOVE(=0) | i T-2 } { SIDE(=+2) ABOVE(=+2) | e } E { SOMEONE(=0) | o } [ { SOMEONE(=0) | o } { MOVE(=-5) ABOVE(=+2) | i } { LAND(=+5) | o D+3 } ] ; { SOMEONE(=-3) | o } { CHANGE(=0) BODY(=0) | i T-2 } AND { SEE(=+3) | i T-2 } E { SOMEONE(=0) | o }
24. { SOMEONE(=0) | o } { MOVE(=+2) ABOVE(=+5) | i T-2 } { NEAR(=+5) | e } { ABOVE(=+5) | o D+3 } ; { SOMEONE(=0) | o } { SIDE(=+2) | i T-2 } E { SOMEONE(=-5) | o N+3 } { SIDE(=-5) | e } { PLACE(=0) | o }
25. { TIME(=-1) | e } { SOMEONE(=+5) | o } { KNOW(=+3) | i T-2 } E [ { HAPPEN | o agent D+3 } ; { SOMEONE(=-3) | o } { GIVE(=-2) | i T-2 } E { OPEN(=0) | o D+3 } AGAINST { GRAIN(=-3) | o } ]
26. { SOMEONE(=+5) | o } { MOOD(=+3) | i T-2 } { SAY(=0) | e I+3 } ; { SAY(=0) | o tool } { MOVE(=0) ABOVE(=-5) INSIDE(=-5) | i T-2 }
27. { SOMEONE(=0) | o } { GIVE(=-2) | i T-2 } E { FIGHT(=-5) | o D+3 } LA [ { SOMEONE(=0) | o } { MOVE(=+2) | i T-2 } { INSIDE(=+2) | e } ]
28. { SOMEONE(=-3) | o } { DO(=-5) | i T-2 } { BEGIN(=+5) | e } { TRUE(=+5) | e } LA [ { SOMEONE(=-3) | o } { THINK(=+5) | i T-2 V+4 } { RULE(=-5) | e } { JOIN(=-5) | e } ]
29. { SOMEONE(=0) | o } { SAY(=0) | i } E [ { FIGHT(=-5) | o } { DO(=+3) GOOD(=+2) | i T+2 M-3 } E { SOMEONE(=+3) | o } { BODY(=+5) | o } ]
30. { SOMEONE(=-3) | o } { THINK(=0) | i T-2 M+4 } E [ { SOMEONE(=+5) | o } { NEAR(=-5) | o agent } ]
