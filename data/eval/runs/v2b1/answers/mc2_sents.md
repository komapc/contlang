1. { TEXT | o } { SAME(=+5) | o } { BODY LONG(=-5) | o N+3 } { HEAT | a } { LIVE | o D+3 } { RULE | i T-2 }
2. { FIGHT(=+5) PART | o } { MEASURE(=-3) FIGHT | a } { CAN(=-3) | i } ; { MOOD(=-3) FIGHT | a } { CAN(=-3) | i }
3. { SEE | i ! } E { TEXT | o D+3 } ; { SOMEONE(=-5) | o } { VALUE(=-5) | a }
4. { TEXT | o agent } { TEXT | i T-2 } E { TEXT | o N+3 } { MANY(=+3) | a }
5. { FEEL(=+4) THINK | o N+3 } { MOVE(=+5) | i T-2 } E { SOMEONE | o } ; { SOMEONE | o } { HEAT(=+5) | i T-2 } E { CONSUME HEAT | o } AND { MOVE PLACE | i T-2 }
6. { THINK(=-3) | i ! } { SOMEONE(=5) JOIN | i } { SAME | a }
7. { GIVE(=+5) KNOW(=-5) | o } { SAY(=-5) KNOW(=-5) | o D+3 } ?
8. LA [ { CARE(=-5) KNOW | o quality } AND { RULE(=+4) CARE(=-5) | o quality } AND { FRIEND SAME(=-4) | o quality } { MANY(=+3) | i } ] ; { VALUE(=-5) DO | o D+3 } { GIVE(=0) | i M-5 CAN C+5 } E { VALUE THING(=-5) | o N+3 }
9. { SOMEONE | o } { FEEL | i T-2 } E { BODY | o N+3 } { MOVE | i } ; { NEAR(=+4) PLACE TOUCH(=+5) | o D+3 } PI { PLACE | o }
10. { SAY(=+5) | o } { LIVE | o N+3 } { SAY(=+5) | i T-2 }
11. { THING(=+4) LAND(=-5) | o N+3 } AND { THING(=+4) SAME(=-5) | o N+3 } { JOIN(=+5) WANT | i T+2 M-3 } E { WANT KNOW | o } { LAND(=0) PLACE | o N+3 }
12. { SOMEONE(=+1) | o } { SAY(=-5) | i M-5 } { PLACE INSIDE(=+5) | o D+3 } { JOIN(=-5) | i T-2 } E { THING(=-5) INSIDE | o D+3 } ; { SOMEONE(=+1) | o } { DO | i T-2 } E { LONG(=+5) ABOVE(=+5) | o D-3 } PI { THING(=0) BIG(=-3) | o D+3 } ; { SOMEONE(=+1) | o } { GIVE | i R-3 } E { THING(=-5) | o }
13. { SAME | o D+3 } { DO | i V-4 } [ { MEASURE(=-5) NEAR(=-5) | i } E { MEASURE(=-5) NEAR(=-5) | o } { INSIDE(=0) PLACE | o } { MOVE(=-5) | i } E { MOVE LONG | o } { INSIDE(=+5) SIDE(=-5) | o } ]
14. { TIME(=-1) | e } { GIVE(=+5) TOUCH(=+5) | o } { TOUCH(=+5) | a } { HEAT(=-5) BODY | a N+3 } { CAN(=-3) | i M-5 } { DO | i T+2 V-4 }
15. { CONSUME(=-5) LONG(=-5) | o } { MANY INSIDE(=-5) | a } { BODY LONG | o tool N+3 } { HEAT SEE | i } { GOOD SEE | o } AND { LONG(=-5) MOVE | o } { TOUCH(=+5) SEE | o }
16. { SOMEONE(=0) FRIEND(=+5) | o N+3 D+3 } { BEGIN(=-5) | i ! } E { KNOW BODY | o D+3 } ; { KNOW CARE(=+5) | o D+3 }
17. { SOMEONE(=+5) | o } { SAY KNOW | i T-2 } E { SOMEONE | o } [ { THINK(=+5) | a } ? ]
18. { SOMEONE | o } { SEE GIVE | i T-2 } E { HEAT | o tool } AND { HEAT(=+5) JOIN | i T-2 } E { MANY | o } { HEAT | o tool } { GIVE | e }
19. { MEASURE(=-5) | o } { CAN(=+5) | i T+2 } ; { MANY | a } { JOIN(=-5) | i V-4 } AND { SAME(=+5) | a } { MEASURE(=-5) | o }
20. { SOMEONE | o } { RULE(=+4) | o agent } { PLACE | o } { RULE(=-5) | o } { TIME(=-1) | a } { MEASURE(=+3) | e } { GIVE(=+5) | i T-2 } ; { TIME(=0) | e } { PART(=-2) | o } { GIVE(=+5) | a }
21. { CARE | e } { SOMEONE | o } { DO JOIN(=-5) | i T+2 } AND { DO JOIN(=-5) | i T+2 } E { JOIN(=-5) | o tool N+3 }
22. { SOMEONE(=+3) | o } { SEE | o tool N+3 } { HEAT(=-2) GOOD | a } AND { INSIDE(=+5) BODY | a } { SEE | i A-3 I+4 }
23. { TIME(=+1) MANY(=-1) | e M-5 } { JOIN(=+5) CARE(=+5) LONG | i T-2 } ; { SIDE(=-5) MOVE | i T-2 }
24. { SOMEONE(=-5) | o N+3 } { SAME(=+5) | i } ; { SOMEONE(=-5) | o N+3 } { FIGHT(=-5) PLACE | i T+2 }
25. { SAY(=-5) | o M-5 } AND { MOVE(=-5) | o M-5 } { INSIDE PLACE LIVE | o } ; { HEAT FEEL SEE | o } { INSIDE(=0) PLACE | o } { FEEL | i }
26. { TEXT | o N+3 } { BEGIN(=+5) | i T-2 } ; { SOMEONE(=-5) | o } { FRIEND(=-5) KNOW | i M-5 }
27. { SAME(=+5) | i } E { PLACE BIG | o } [ { PART(=+5) SOMEONE KNOW | o N+3 } ] { PLACE BIG SOMEONE | o N+3 } AND { PLACE BIG SOMEONE | o N+3 }
28. { TEXT | o } LA ; { LONG PART(=+2) | o N+3 } { DO | i T-2 V-4 } E { DO PLACE | o agent }
29. { TIME(=0) | e } { SOMEONE(=+5) | o } { SEE | i T-2 } E { SOMEONE | o } { SAME(=+5) | i M+4 } ; { SOMEONE | o } { CHANGE ART | i V-4 } { THING | o }
30. { SOMEONE | o } { CARE(=+5) | i T-2 } ; { SOMEONE | o } { CONSUME HEAT | i T-2 }
31. { SOMEONE(=+3) SAY | i } E { SOMEONE(=+3) TEXT | o } ; { SOMEONE | o } { RULE PART | o agent } { SOMEONE | o } { CARE KNOW ART | i T-2 } AND { TOUCH(=+5) | a } AND { KNOW(=+5) | a }
32. { SOMEONE | o } { MOVE(=-5) | i T-2 } { PLACE ABOVE | o } ; { BODY CALM | i } { BODY MOVE | i } { SEE | i T-2 } E { SAME(=+5) PLACE INSIDE | o }
33. { SOMEONE | o D+3 } { GIVE(=0) | i T-2 } E { THING(=-5) MOVE | o D+3 } { NEAR | e } { LONG PART | o } AND { GIVE(=+5) | i T-2 } E { SOMEONE | o }
34. { TIME(=-1) | o D+3 } { HAPPEN | i T-2 } ; { GOOD(=-5) | o }
35. { HAPPEN | o agent } { SAME(=+5) | a } ?
36. { SOMEONE | o } { WANT(=+5) | i T-2 } E { FIGHT(=-5) PART | o }
37. { MANY SOMEONE | o D+3 } { TIME(=0) | e } { GIVE(=+5) KNOW(=+5) | i T-2 A+5 V-4 } E { KNOW(=+5) ART | o quality } AND { MANY TEXT SAY | o N+3 } { FIGHT(=-5) | a }
38. { SAME(=-5) | e } { SOMEONE(=-5) | o N+3 } { SEE GIVE | i T-2 } E { SAME(=+3) WANT | o N+3 }
39. { RULE(=+4) FIGHT | o D+3 } { GOOD | i T-2 } ; { MANY(=+3) | o N+3 } { VALUE(=+3) | i T-2 } E { PLACE LIVE | o N+3 }
40. { PLACE BIG SOMEONE(=+3) | o N+5 } { SOMEONE(=+3) SIDE(=+5) KNOW(=+5) | o agent N+3 } { RULE(=+4) | a } AND { KNOW(=+5) | a } { DO CARE(=+4) | i T-2 A-2 I+4 } E { SOMEONE PART(=+5) THINK | o D+3 } [ { SOMEONE PART(=+5) | o } { WANT GIVE | i K+5 } E { SAME(=+5) GIVE | o } ]
41. { TIME(=0) | e } { RULE(=+4) | o D+3 } { MANY(=-1) THINK | i T+2 } E { WANT | o }
42. { SOMEONE(=-5) | o } { MOVE ABOVE(=+5) | i T-2 } E { SEE | o tool N+3 } [ { SEE | i } E { PLACE SEE | o } ] ; { BODY SAY | o tool N+3 } { CONSUME TOUCH(=-5) | i T-2 } E { THING(=0) WANT(=-3) | o N+3 }
43. { SEE LIVE(=+5) | o } { VALUE(=+5) THINK | i }
44. { LAND BIG ABOVE | o N+3 } { NEAR(=-5) SEE | e } { COLOR | o } { LIVE(=-5) | a }
45. { LONG(=+5) | o N+3 } { CARE(=+4) | e } { SAME(=+5) | i V-4 } ; { SOMEONE(=-5) | o } { THING(=-5) | o N+3 } { VALUE | o } { NEAR | e }
46. { SOMEONE | o } { NEAR(=-5) GOOD | i T-2 } ; { MANY(=+5) SOMEONE | o } { LIVE(=-2) FEEL | i T-2 }
47. { TIME(=+1) | e } { SOMEONE(=-5) | o N+3 } { GIVE ABOVE | i T-2 } E { BIG(=-3) | a } { SEE TOUCH(=+5) | o N+3 } { LAND | o PI } { SIDE(=+5) SOMEONE | o }
48. { DO | i ! } E { BODY(=-2) | o N+3 } ; { SIDE | o } { NEAR(=+3) BODY | o D+3 } { PART(=-2) | o N+3 } ; { SIDE(=+5) | i }
49. { THINK(=+5) SAME | o } { MEASURE(=0) GOOD | a } { FIGHT | o } { CHANGE | i T-2 } E { THINK(=+5) FIGHT(=+5) FRIEND(=-5) | o } ; { HAPPEN CARE(=-5) | o result } { JOIN(=-5) | i T-2 A+5 } ; { BIG HAPPEN | o }
50. { MANY(=+3) | a } { LONG | o N+3 } { LAND(=+5) | o } { JOIN(=+5) | i V-4 } E { LAND(=+5) | o }
51. { MANY(=-1) | a } { JOIN(=+5) TOUCH | o tool N+3 } { MOVE(=-5) | i V-4 } ; { MANY(=-1) | a } { JOIN(=+5) TOUCH | o tool N+3 } { MOVE | i } E { LONG(=+5) | o tool } { SAME(=-5) | a }
52. { TIME(=-1) | e } { SOMEONE | o agent } { DO | i T-2 } E { SAY | o N+3 } { LIVE(=-5) | a }
53. LA { REMOVE | i } ; { MEASURE(=-5) JOIN(=-5) | o } { SAME(=+5) | i } E { MEASURE(=-5) LONG(=-5) | o } ; { SEE MEASURE(=-5) | o tool } { JOIN(=+5) | i T-2 V-4 } E { DO MEASURE | o tool } [ { CARE(=+5) | e } { MEASURE(=-5) | i } E { MEASURE(=-5) TOUCH(=-5) | o } ]
54. { PLACE LIVE | o D+3 } { LIVE(=-2) | i T-2 } ; { LIVE(=+3) SEE | o } { MOVE | i T-2 } AND { LIVE(=-2) | i T-2 } E { INSIDE(=-5) PLACE SEE | o }
55. { MANY LIVE | o N+3 } { LIVE SEE | o N+3 } { SEE CAN(=+5) | i M-5 } ; { CONSUME JOIN(=-5) | i } AND { SIDE(=-5) JOIN(=-5) | i } E { LONG(=-5) MEASURE(=-5) SEE | o N+3 }
56. { THING(=+4) | o D+3 } { JOIN(=-5) | i M+4 } E { THING(=+4) BIG(=-3) | o } { CARE | e } AND { JOIN(=-5) PART(=-5) | i }
57. { SOMEONE | o } { TOUCH(=+5) THING(=+4) | i } ; { TOUCH(=-5) FRIEND | i }
58. { SOMEONE | o } { KNOW(=+5) | i T-2 } E { MANY(=+5) | o } PI { WANT | o }
59. { HEAT(=+5) | o } { ABOVE(=+5) | o } { CHANGE | i T+2 } E { LAND(=-5) | o D+3 } ; { GOOD(=-5) | a }
60. LA { TIME(=-1) SAME | e M-5 } ; { FIGHT(=+5) SOMEONE | o agent N+3 } { MANY(=-1) TIME | e } { CONSUME WANT | i T-2 } E { TEXT LONG | o tool } AND { LONG PLACE | o }
