1. { VALUE | o D+3 } { SAME(=+5) | i T-2 } "Af" LA [ { TEXT ABOVE(=+5) | o D+3 N+3 } ]
2. { VALUE | o D+3 PI } { TEXT | o D+3 } { NEAR(=+5) | i M+4 } ; { NEAR(=-5) | i M-5 }
3. { SOMEONE(=+5) | o } { KNOW | i T-2 } E [ { SOMEONE(=+5) | o } { MOVE(=-5) | i T-2 } { PLACE INSIDE(=0) | o D-3 } ; { SOMEONE(=+5) | o } { SEE | i } E { "Jessica" } { DO | i } E { SOMEONE | o } { GIVE(=+5) CONSUME | i } E { GRAIN(=-3) CONSUME | o N+3 } ]
4. { SAME | o D+3 } { CAN(=+5) | i T-2 M+4 I+4 C+3 }
5. { SOMEONE(=+5) FRIEND | o SEX(=+5) PI } { SEX(=-5) | o D+3 } { TOUCH | i T-2 } ; { SOMEONE(=+5) | o } { MOVE ABOVE(=-5) | i T-2 }
6. { SAME(=-4) | a } { THING(=0) LONG(=+5) | o D-3 } { MOVE ABOVE(=+5) | i T-2 } { PART(=+5) THING(=0) | o D-3 }
7. { SOMEONE(=+5) | o } { WANT(=-5) | i T-2 } E { SOMEONE(=+3) | o } LA [ { BEGIN(=-5) INSIDE(=+5) MOVE | i T-2 } ]
8. { SOMEONE(=+5) | o } { MOVE ABOVE(=-5) SAY(=+3) | i T-2 } ; { MOVE INSIDE(=-5) | i T-2 }
9. { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE(=+5) | o } { BIG(=+3) CHANGE | i A-5 }
10. { SOMEONE(=-5) | o } { MOVE LAND(=+5) GRAIN(=-3) | i T-2 } { PLACE LONG(=+5) | o }
11. { SOMEONE(=-5) | o } { MOVE(=-5) | i T-2 } { CONSUME SAY | i } E { GRAIN(=-3) | o N+3 }
12. { KNOW(=+5) | i T-2 } E [ { SOMEONE | o } { FIGHT | i } ]
13. { SOMEONE(=+5) SEX(=+5) | o } { MOVE SIDE(=+5) | i T-2 } ; { SEE | i T-2 } E { SOMEONE | o }
14. { "Greg" } { MOVE ABOVE(=+5) | i T-2 } ; { SIDE(=+5) | i T-2 } E { SOMEONE(=-5) | o }
15. { TIME(=-1) | e } { KNOW(=+5) | i T-2 } E { THINK | o }
16. { SOMEONE(=+5) | o } { MOOD(=+5) SAY(=-3) | i T-2 } ; { BODY | o D+3 } { MOVE ABOVE(=-5) | i T-2 }
17. { "Mike" } { JOIN(=+5) | i T-2 } ; { SOMEONE | o } { MOVE | i T-2 }
18. { SOMEONE(=+5) | o } { LIVE(=-2) | i T-2 } ; { CAN(=+5) THINK(=+5) | o }
19. { "Fortman" } { SAY | i } E [ { MOVE | o } { CAN(=+5) | i T+2 } ]
20. { SOMEONE(=+5) | o } { THINK | i T-2 M+4 } E [ { SOMEONE(=+5) | o } { MOVE(=-5) PLACE | o } ]
