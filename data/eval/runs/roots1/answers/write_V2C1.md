1. { BIG(=+3) | a } || { BIG(=+3) | a } || { BIG(=+3) | a }
2. { TOUCH(=+5) MOVE(=+5) | i } || { TOUCH(=+5) MOVE(=+5) | i } || { TOUCH(=+5) MOVE(=+5) | i }
3. { MOVE(=+2) DO | o agent } || { SOMEONE | o agent } FOR { MOVE(=+2) | o tool } || { SOMEONE | o agent } FOR { MOVE(=+2) | o tool } FOR { MOVE(=+2) | i }
4. { WANT(=-5) | i } || { WANT(=-5) | i } || { WANT(=-5) | i I+4 }
5. { CAN | o quality } || { CAN | o quality } || { CAN | o quality }
6. { LIVE(=+3) KNOW(=+5) | o agent } || { LIVE(=+3) | o agent } FOR { LIVE(=-3) | a } || { KNOW(=+5) | o agent } FOR { LIVE(=+3) | i } FOR { LIVE(=-3) | a }
7. { GIVE(=-2) | i } || { GIVE(=-2) | i } || { GIVE(=-2) | i }
8. { GOOD | a C+3 } || { GOOD | a C+3 } || { GOOD | a C+3 }
9. { RULE(=+5) SOMEONE(=+3) | o } || { RULE(=+5) | o quality } FOR { SAY(=-5) TRUE | i } || { RULE(=+5) | o quality } FOR { SOMEONE(=+3) MANY(=+5) | o } FOR { THINK(=+5) SAY(=-5) | i }
10. { SHAPE SAME | o } || { SHAPE SAME | o } || { SHAPE SAME | o }
11. { SEE(=+5) | i K+4 } || { SEE(=+3) | i K+4 } || { SEE(=+5) | i K+4 }
12. { TIME(=-5) HAPPEN | o } || { HAPPEN | o result T-2 } || { TEXT(=+5) | o } FOR { HAPPEN | o T-2 }
13. { SEE(=+5) CARE | o } || { CARE | o } FOR { TEXT(=+3) | o } || { TEXT(=+3) | o agent } FOR { CARE | o } FOR { SAY | i }
14. { JOIN(=+3) DO | o } || { JOIN(=+3) DO | o } || { JOIN(=+3) DO | o } PI { PART(=+5) | o }
15. { BODY(=-3) | o } || { BODY(=-3) | o } || { BODY(=-3) | o }
16. { TEXT(=+3) SAY(=-5) | o } || { TEXT(=+3) | o } FOR { SAY(=-5) | i } || { TEXT(=+3) | o } FOR { SAY(=-5) | i } FOR { MEASURE(=+5) | o }
17. { TRUE(=+5) SEE(=+5) | i K+4 } || { TRUE(=+5) | i K+4 } || { TRUE(=+5) | i K+4 }
18. { THING GRAIN(=0) | o } || { THING(=0) | o } FOR { CONSUME(=+5) HEAT(=+3) | i } || { THING(=0) | o } FOR { CONSUME(=+5) HEAT(=+3) | i } FROM { COLOR(=-5) | o }
19. { GIVE(=+5) MOVE | i } || { GIVE(=+5) MOVE | o result } || { GIVE(=+5) MOVE | o result }
20. { BIG(=+2) | a } || { BIG(=+2) | a } || { BIG(=+2) | a }
21. { HAPPEN | o result } || { HAPPEN | o result } || { HAPPEN | o result }
22. { TIME(=-1) BIG(=-5) | o } || { TIME(=-1) BIG(=-5) | o } || { TIME(=-1) BIG(=-5) | o }
23. { MEASURE(=-2) PART(=+5) | o } || { MEASURE(=-2) | o } PI { PART(=+5) | o } || { MEASURE(=-2) | o } PI { PART(=+5) | o }
24. { STRONG(=-4) | a } || { STRONG(=-4) | a } || { STRONG(=-4) | a }
25. { RULE(=+3) VALUE | o } || { PLACE | o } FOR { VALUE | i } || { RULE(=+3) PART(=+5) | o } FOR { VALUE | i }
26. { PART(=-2) JOIN(=-5) | i } || { PART(=-2) JOIN(=-5) | i } || { PART(=-2) JOIN(=-5) | i }
27. { CAN(=-3) | a } || { CAN(=-3) | a } || { CAN(=-3) | a }
28. { STRONG(=-2) | a } AGAINST { BODY(=0) HEAT(=+4) | a } || { HAPPEN | o } AGAINST { BODY(=-3) STRONG(=+5) | o } || { BODY(=-3) | a } AGAINST { STRONG(=+4) | a } AGAINST { BODY(=0) HEAT(=+4) | o }
29. { SHAPE(=+5) | o } || { SHAPE(=+5) | o } FOR { OPEN(=0) | i } || { SHAPE(=+5) | o } FOR { OPEN(=0) | i } FROM { LAND(=+5) GRAIN(=+2) | o }
30. { SOMEONE RULE(=+3) KNOW | o agent } || { SOMEONE | o agent } FOR { TRUE(=+2) SAY | i } || { SOMEONE | o agent } FOR { RULE(=+3) TRUE(=+5) | o } FOR { SAY | i }
31. { TRUE(=-5) | i K+4 } || { TRUE(=-5) | i K+4 } || { TRUE(=-5) | i K+4 }
32. { GRAIN(=+5) | o } || { GRAIN(=+5) SHAPE(=0) | o } || { GRAIN(=+5) SHAPE(=0) | o }
33. { ABOVE(=+2) | a } || { ABOVE(=+2) | a } || { ABOVE(=+2) | a }
34. { THINK | a } || { THINK | a } || { THINK | a }
35. { LIGHT(=+5) GOOD(=+5) | o quality } || { LIGHT(=+5) | o quality } || { LIGHT(=+5) | o quality }
36. { TIME(=+5) | o } PI { TIME MEASURE(=-2) | o } || { TIME PART(=+5) | o } || { TIME PART(=+5) | o }
37. { SAME(=-3) | a } || { SAME(=-3) | a } || { SAME(=-3) | a }
38. { GRAIN(=-3) | a } || { GRAIN(=-3) MANY(=+3) | a } || { GRAIN(=-3) MANY(=+3) | a }
39. { PART(=+5) | o } || { PART(=+5) | o } || { PART(=+5) | o }
40. { SAY(=+3) FIGHT | i } || { SAY(=+3) | i } AGAINST { SOMEONE | o } || { SAY(=+3) TRUE(=-2) | i }
41. { MOVE(=+2) | i V+4 } || { MOVE(=+2) | i V+4 } || { MOVE(=+2) | i V+4 }
42. { OPEN(=+5) PLACE(=0) | o } || { OPEN(=+5) | o } PI { PLACE(=-3) | o } || { OPEN(=+5) | o } FOR { MOVE | i } PI { PLACE(=-3) | o }
43. { SHAPE(=0) INSIDE(=0) | o } || { SHAPE INSIDE(=0) | o } || { SHAPE INSIDE(=0) | o }
44. { ART(=+5) MOVE | o } || { ART(=+5) MOVE | o } || { ART(=+5) MOVE | o }
45. { BIG(=-3) | a } || { BIG(=-3) | a } || { BIG(=-3) | a }
46. { PLACE | o } || { PLACE(=-5) | o } || { PLACE(=-5) | o }
47. { LONG SHAPE(=0) | o } || { SHAPE(=0) | o } FOR { FIGHT(=-5) MOVE(=+5) | i } || { LONG(=+5) SHAPE(=0) | o } FOR { FIGHT(=-5) | o } FOR { MOVE(=+5) | i }
48. { CHANGE BIG(=+2) | o } || { LIVE(=+3) BIG(=+2) | i } || { LIVE(=+3) CHANGE BIG(=+2) | i }
49. { LIVE(=-5) RULE(=+5) | i } || { LIVE(=-5) | i K+5 } || { LIVE(=-5) | i K+5 } FOR { RULE(=+5) | o }
50. { RULE ABOVE | o } || { RULE ABOVE | o } || { RULE ABOVE | o } PI { SOMEONE(=+3) PART(=+5) | o }
51. { RULE(=+5) | a } || { RULE(=+3) | a } || { RULE(=+3) | a }
52. { KNOW(=-5) CHANGE | i K+4 } || { KNOW(=-5) | i K+4 } || { KNOW(=-5) | i K+4 }
53. { STRONG(=+5) | o } || { STRONG(=+5) | o } || { STRONG(=+5) | o }
54. { JOIN(=-5) OPEN(=+5) | o tool } || { LONG(=0) | o tool } FOR { OPEN(=+5) | i } || { LONG(=0) | o tool } FOR { OPEN(=+5) | i } FOR { PLACE(=0) | o }
55. { DO(=+3) PART(=+5) | o result } || { DO(=+3) PART(=+5) | o result } || { DO(=+3) PART(=+5) | o result }
56. { PLACE(=+5) RULE(=+3) | o } || { PLACE(=+3) | o } PI { PLACE(=+5) RULE(=+3) | o } || { PLACE(=+3) | o } PI { PLACE(=+5) RULE(=+3) | o }
57. { INSIDE(=+5) | o } || { INSIDE(=+5) | o } PI { LIVE PART(=-2) | o } || { INSIDE(=+5) | o } FOR { LIVE(=+5) BIG(=+2) | o } PI { LIVE PART(=-2) | o }
58. { INSIDE(=+5) | i } || { INSIDE(=+5) CHANGE | i } || { INSIDE(=+5) CHANGE(=+3) | i }
59. { STRONG RULE | o } || { STRONG RULE(=+3) | o } || { STRONG RULE(=+3) | o }
60. { KNOW(=-5) | i K+4 } || { KNOW(=-5) | i K+4 } || { KNOW(=-5) THINK(=-2) | i K+4 }
