1. { VALUE | o D+3 } { SAME(=+5) | i T-2 } "Af" { TEXT MEASURE | o D+3 } { TEXT ABOVE(=+5) TIME(=-1) | o D+3 }
2. { JOIN | e } { VALUE | o D+3 } { TEXT | o D+3 } { PART(=+2) VALUE | o } { NEAR(=+5) INSIDE(=+5) | i M+4 } ; { NEAR(=-3) INSIDE(=0) | i M-5 }
3. { SOMEONE(=+5) | o } { THING(=-5) THINK(=-1) | i T-2 } E [ { SOMEONE(=+5) | o } { MOVE(=-5) PLACE INSIDE(=0) | i } { SOMEONE(=+5) | o } { SEE | i } E { SOMEONE(=-5) | o } { DO SOMEONE | i } E { GIVE(=+5) CONSUME | o agent } { GIVE(=+5) | i } E { GRAIN(=-3) TOUCH(=-5) CONSUME | o N+3 } { SOMEONE(=-5) | o N+3 } ]
4. { SOMEONE(=+5) | o } LA { HAPPEN | i T-2 } { CAN(=+5) | e I+4 } { HAPPEN | o N+3 D+3 }
5. { SOMEONE(=+5) SEX(=-5) | o agent D+3 } { MOVE TOUCH(=-3) | i T-2 A-5 } E { SOMEONE(=-5) SEX(=+5) | o } ; { SOMEONE(=-5) SEX(=+5) | o } { ABOVE(=-5) MOVE | i T-2 A0 }
6. { SAME(=-4) | a } { LONG(=+5) THING | o } { ABOVE MOVE(=-1) | i T-2 } { PLACE THING(=0) | o } { THING(=0) | o N+3 }
7. { SOMEONE(=+5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=+3) | o } LA { SOMEONE(=+5) | o } { SIDE(=+5) INSIDE(=+5) MOVE | i T-2 } { BEGIN(=-5) | e }
8. { SOMEONE(=-5) SEX(=+5) | o } { SAY(=+3) MOVE ABOVE(=-5) | i T-2 } { LONG SHAPE | o N+3 } AND { OPEN(=+5) INSIDE(=-5) MOVE | i T-2 } { OPEN(=+5) | o D+3 }
9. { SOMEONE(=+5) SEE | o tool } { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=-5) SEX(=+5) | o } { BIG(=+3) CHANGE | i I+4 }
10. { SOMEONE(=-5) | o N+3 } { LAND(=+5) GRAIN(=-3) | o } { MOVE | i T-2 } { LONG SHAPE(=+5) THING(=0) LAND(=+5) | o } AND { LONG(=-5) SHAPE(=+5) | o }
11. { SOMEONE(=-5) | o N+3 } { MOVE(=-5) SIDE(=-5) INSIDE(=+5) | i T-2 } { OPEN(=0) GRAIN(=-3) | o N+3 } { CONSUME | i T-2 } E { SAY LAND(=-5) | o N+3 } { GRAIN(=-3) SAY | i } { ABOVE(=-5) SHAPE(=+5) | o }
12. { SOMEONE(=-5) SEX(=+5) | o } { KNOW(=+5) | i T-2 } E [ { FIGHT(=0) SIDE(=+5) | o D+3 } { SOMEONE(=-5) SEX(=+5) | o } { NEAR | i } ]
13. { SOMEONE(=-5) SEX(=+5) | o } { MOVE SIDE(=+5) | i T-2 } { NEAR(=+5) SAME(=+5) | e } E { SOMEONE SEX(=+5) | o } [ { MOVE(=-5) LAND(=+5) | i } ] AND { ABOVE(=-5) | i T-2 } { SEE | i T-2 } E { SOMEONE(=-5) SEX(=+5) | o }
14. "Greg" { ABOVE(=+5) MOVE | i T-2 } { NEAR(=+5) TOUCH | e } { ABOVE(=+5) SHAPE(=+5) PLACE INSIDE | o D+3 } ; { SOMEONE(=-5) | o N+3 } { SIDE(=-5) MOVE | i K+5 T-2 } { GIVE SIDE(=+5) | o } { NEAR(=+5) PLACE LIVE | o }
15. { TIME(=-1) | e } { SOMEONE(=+5) | o } { KNOW(=+5) | i T-2 } E [ { HAPPEN | o quality } { SOMEONE(=-5) SEX(=-5) | o } { OPEN(=-5) ABOVE LIGHT(=-2) | o tool } { NEAR | i T-2 } ]
16. { SOMEONE(=+5) | o } { MOOD(=+4) SAY(=+1) | i T-2 } ; { CONSUME(=+5) SHAPE(=-5) OPEN | o tool D+3 } { ABOVE(=-5) MOVE INSIDE(=-5) | i T-2 }
17. "Mike" { GIVE(=-5) | i T-2 } E { SHAPE(=0) FIGHT(=-5) | o D+3 } { TIME(=-1) | e } LA { FIGHT(=-5) SIDE(=-5) | o agent D+3 } { MOVE | i T-2 } { OPEN(=-5) | o D+3 }
18. { SOMEONE(=-5) SEX(=-5) | o } { BEGIN(=+5) MOVE(=-5) LIVE(=-2) | i T-2 } { TRUE | e } AND { WANT | e } ; { THINK(=+5) SOMEONE(=+3) | o quality } { STRONG VALUE | a }
19. "Fortman" { KNOW(=+5) ART(=+5) | o agent } { SAY | i } E [ { MOVE LAND(=-5) | o quality } { CHANGE GOOD(=+3) | i M-3 } E { BODY LONG | o D+3 } ]
20. { SOMEONE(=-5) SEX(=+5) | o } { THINK | i T-2 M+4 } E [ { SOMEONE(=+5) | o } { NEAR(=-5) MOVE SEE | o agent } ]
