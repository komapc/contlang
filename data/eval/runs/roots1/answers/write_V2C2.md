1. { TEXT(=0) SAY | o result } || { TEXT(=0) | o } FROM { SAY(=+3) | i } || { TEXT(=0) | o } FROM { SAY(=+3) | i } LIKE { TRUE(=+5) | a }
2. { HAPPEN STRONG(=+4) GOOD(=-4) | o } || { HAPPEN GOOD(=-4) | o } LIKE { FEEL(=+5) | o } || { HAPPEN GOOD(=-4) | o } LIKE { FEEL(=+5) | o } FOR { CARE(=+5) | o }
3. { BEGIN(=-5) DO(=+3) | i } || { DO(=+3) | i } FROM { BEGIN(=-5) | o } || { DO(=+3) | i } FROM { BEGIN(=-5) | o } FOR { PLACE | o }
4. { ART(=-2) DO(=+3) | o agent } || { ART(=-2) | o agent } FOR { STRONG LONG(=0) | o tool } || { ART(=-2) | o agent } FOR { DO(=+3) | i } LIKE { STRONG | o tool }
5. { HEAT(=+4) GRAIN(=-5) | o } || { GRAIN(=-5) | o } FROM { GRAIN(=-3) HEAT(=+5) | o } || { GRAIN(=-5) | o } FROM { GRAIN(=-3) HEAT(=+5) | o } PI { ABOVE | o }
6. { SAY(=-5) THINK(=-2) | o } || { SAY(=-5) | o result } FOR { FIGHT(=0) | i } || { SAY(=-5) VALUE(=+5) | o result } FOR { FIGHT(=0) | i }
7. { DO(=+3) THINK(=+3) | o result } || { TEXT(=0) | o } FOR { DO(=+3) | i } || { TEXT(=0) | o } FOR { DO(=+3) | i } FROM { THINK(=+3) | o }
8. { THINK(=+5) MANY(=+5) | i } || { THINK(=+3) | i } FROM { PART(=-5) | o } || { THINK(=+3) | o result } FROM { PART(=-5) | o } FOR { MANY(=+5) | a }
9. { GOOD(=+5) SEE(=+5) | a } || { GOOD(=+5) | a } FOR { SEE(=+5) | i } || { GOOD(=+5) SEE(=+5) | a } LIKE { WANT(=+5) | a }
10. { PLACE GOOD(=+5) | o } || { PLACE(=+3) GOOD(=+5) | o } PI { ABOVE(=+5) | o } || { PLACE GOOD(=+5) FEEL(=-5) | o } PI { ABOVE(=+5) | o }
11. { SEE(=+5) | i } || { SEE(=+5) | i } FROM { HAPPEN | o } || { SEE(=+5) | i } FOR { KNOW(=+3) | i }
12. { SAY I+5 | i } || { SAY | i I+5 } || { SAY | i I+5 T-1 }
13. { TEXT(=+5) TRUE(=-5) | o } || { TEXT(=+5) | o } FROM { TRUE(=-5) | o } || { TEXT(=+5) | o } FROM { THINK(=0) | o } LIKE { TRUE(=-5) | a }
14. { ABOVE(=+2) JOIN | i } || { JOIN(=+3) | i } FOR { ABOVE | a } || { JOIN(=+3) | i } FOR { ABOVE(=+3) | a } AGAINST { LONG(=0) | o }
15. { STRONG MEASURE | o } || { STRONG(=+3) | o } FOR { MEASURE(=-5) | o } || { STRONG(=+3) | o } FOR { MEASURE(=+2) | o } PI { SHAPE(=+5) | o }
16. { FEEL(=0) NEAR(=+3) | o } || { FEEL(=0) | o } FROM { GRAIN(=-5) | o } || { FEEL(=0) | o } FROM { GRAIN(=-5) | o } FOR { BODY(=-3) | o }
17. { TEXT(=-2) CONSUME(=-3) | o } || { TEXT(=-2) | o } FOR { SAY | i } || { TEXT(=-2) | o N+5 } FOR { SAY | i } FROM { RULE | o }
18. { RULE(=+3) VALUE(=0) | o agent } || { SOMEONE | o } FOR { RULE(=+3) | i } || { SOMEONE | o } FOR { RULE(=+3) | i } FROM { VALUE(=0) | o }
19. { BODY(=0) STRONG | o } || { BODY(=+3) | o } PI { STRONG | o } || { PART(=-2) | o } PI { BODY | o } FOR { STRONG | o }
20. { VALUE(=0) GIVE(=0) | o } || { GIVE(=0) | i } FOR { VALUE(=0) | o } || { GIVE(=0) | i } FOR { VALUE(=0) | o } FROM { MANY(=+3) | o }
21. { VALUE(=0) GIVE(=0) | o tool } || { VALUE(=0) | o tool } FOR { GIVE(=0) | i } || { VALUE(=0) | o } FOR { GIVE(=0) | i } FROM { RULE(=+5) | o }
22. { MEASURE(=-5) RULE(=+3) | o } || { LAND(=+2) | o } FOR { STRONG | o } || { PLACE | o } FROM { RULE(=+3) | o } FOR { DO | i }
23. { FRIEND(=+5) PART(=+5) | o } || { PART(=+5) | o } FROM { FRIEND(=+5) | o } || { PART(=+5) | o } FROM { FRIEND(=+5) | o } LIKE { THINK(=0) SAME(=+5) | o }
24. { MOVE(=-5) ABOVE(=+2) | i } || { MOVE(=-5) | i } FOR { ABOVE(=+2) | a } || { MOVE(=-5) | i } LIKE { LONG(=+2) | o }
25. { GIVE(=+5) CAN(=+3) | i } || { GIVE(=+2) | i } FOR { CAN(=+3) | o } || { GIVE(=+5) | i } FOR { CAN(=+3) | o } FROM { FRIEND(=+5) | o }
26. { TEXT(=-2) PART(=+5) | o } || { TEXT(=0) | o } PI { TEXT(=-2) PART(=+5) | o } || { TEXT(=-2) PART(=+5) | o } PI { TEXT(=0) | o }
27. { TEXT(=-5) JOIN(=+5) | i } || { JOIN(=+5) | i } FROM { TEXT(=-5) | o } || { JOIN(=+5) | i } FROM { TEXT(=-5) | o } FOR { HEAT(=+2) | o }
28. { FIGHT(=+2) BODY | i } || { FIGHT(=+2) | i } LIKE { BODY(=0) JOIN | o } || { FIGHT(=+2) | i } LIKE { BODY(=0) JOIN | o } FOR { FIGHT(=-5) | o }
29. { RULE(=0) DO(=0) | i } || { DO | i } FOR { RULE | o } || { DO | i } FOR { SAY(=+5) | o } FROM { RULE(=+3) | o }
30. { CAN(=+3) WANT | a } || { CHANGE(=+3) | a } FOR { DO | i } || { SAME(=+3) | a } FOR { DO | i } FROM { THING(=+4) | o }
31. { KNOW(=+3) TEXT(=-2) | i } || { KNOW(=+3) | i } FROM { TEXT(=-2) | o } || { KNOW(=+3) | i } FROM { TEXT(=0) | o } FOR { THINK(=0) | i }
32. { DO(=+3) BEGIN(=0) | o } || { DO(=+3) | o } FOR { HAPPEN | o result } || { DO(=+3) | o } FOR { BEGIN(=+5) | o } PI { HAPPEN | o }
33. { GOOD(=+3) CHANGE(=+3) | i } || { CHANGE(=+3) | i } FROM { GOOD(=+3) | a } || { GIVE(=+5) | i } FOR { GOOD(=+3) VALUE(=+2) | o }
34. { ART(=-2) DO(=+3) | a } || { DO(=+3) | a } FROM { ART(=-2) | o } || { DO(=+3) | a } FROM { ART(=-2) MANY | o } PI { PLACE | o }
35. { SAY(=0) FEEL(=-5) | i } || { SAY(=0) | i I-4 } || { SAY(=0) | i I-4 } FOR { MANY(=-5) | o }
36. { JOIN(=-5) | i } || { JOIN(=-5) | i } FROM { NEAR(=+3) | o } || { JOIN(=-5) | i V+4 }
37. { RULE(=0) PLACE(=0) | a } || { SOMEONE | o agent } FOR { THING(=+4) | o } || { SOMEONE | o agent } FOR { THING(=+4) | o } PI { LAND(=+2) | o }
38. { MANY(=0) TRUE | o } || { PART(=+5) | o } FROM { TRUE(=+5) | o } || { PART(=+5) | o } FROM { TRUE(=+5) | o } FOR { KNOW(=+3) | i }
39. { CONSUME(=+5) THING(=+4) LAND(=-2) | o agent } || { SOMEONE | o } FOR { CONSUME(=+5) THING(=+4) | i } || { SOMEONE | o } FOR { CONSUME(=+5) | i } FROM { THING(=+4) LAND(=-2) | o }
40. { TIME(=0) DO | i } || { MOVE(=0) | i } FROM { TIME | o } || { MOVE(=0) | i } FROM { TIME | o } FOR { DO(=0) | i }
41. { FEEL(=+2) TOUCH(=-5) | a } || { FEEL(=+3) | a } FOR { TOUCH | o } || { FEEL(=+3) | a } FOR { TOUCH(=0) | o } LIKE { BODY(=-3) | o }
42. { SIDE(=0) JOIN(=-5) | i } || { JOIN(=-5) | i } FOR { SIDE(=0) | o } || { JOIN(=-5) | i } FOR { SIDE(=0) | o } LIKE { SHAPE(=+5) | o }
43. { SOMEONE SEX(=-5) LIVE(=+5) | o } || { SOMEONE SEX(=-5) | o } FROM { BEGIN(=-2) | o } || { SOMEONE SEX(=-5) | o } PI { BEGIN(=-2) | o }
44. { VALUE(=+5) | a } || { VALUE(=+5) | a } FOR { MANY | o } || { VALUE(=+5) | a } FOR { MANY(=+3) | o } FROM { THINK | o }
45. { RULE(=+5) STRONG(=+5) | a } || { RULE(=+3) | a } AGAINST { SIDE(=-5) | o } || { RULE(=+5) | a } AGAINST { RULE(=+3) SAME(=-3) | o }
46. { JOIN(=+3) | i } || { JOIN(=+3) | i } FOR { MEASURE(=-2) | o } || { JOIN(=+3) | i } FOR { MEASURE(=-2) | o } FROM { MANY(=+3) | o }
47. { HEAT(=+5) LIGHT(=+5) | o } || { HEAT(=+5) LIGHT(=+5) | o } FROM { HAPPEN | o } || { HEAT(=+5) LIGHT(=+5) | o } FROM { GRAIN(=-5) | o } PI { MOVE(=+2) | o }
48. { BODY LIVE | o } || { BODY(=0) | o } PI { LIVE | o } || { BODY | o } PI { LIVE | o } FROM { THING | o }
49. { LONG(=+2) HEAT LIGHT | o } || { LONG(=+2) | o } FOR { LIGHT(=+5) | o } || { LONG(=+2) | o } FOR { LIGHT(=+5) | o } FROM { GRAIN(=+2) | o }
50. { ART(=+5) MEASURE(=-2) | o result } || { ART(=+5) | o result } FOR { PART(=+2) | o } || { ART(=+5) | o result } FOR { MEASURE(=-2) SOMEONE | o }
51. { SEE(=+3) | i V+4 } || { DO | i } FOR { SEE(=+3) | i } || { DO | i } FOR { SEE(=+3) | i } FROM { KNOW(=+3) | o }
52. { DO(=+3) | i } || { DO(=+3) | i } FOR { CAN | o } || { DO(=+3) | i } FOR { GIVE(=+5) | i } FROM { CAN | o }
53. { LIVE(=-5) CHANGE(=+3) | i } || { LIVE(=-5) | i K+5 } || { LIVE(=-5) | i K+5 V+4 }
54. { TEXT(=0) SAME(=-3) | i } || { SAY(=0) | i } FOR { SAME(=-3) | o } || { SAY(=0) | i } FOR { SAME(=-3) | o } LIKE { SEE | i }
55. { SAME(=+5) MEASURE(=-2) | o } || { TEXT(=0) | o } FOR { SAME(=+5) | o } || { TEXT(=0) | o } FOR { SAME(=+5) | o } FROM { MEASURE(=-2) | o }
56. { SAME(=-5) CHANGE | i } || { CHANGE(=+3) | i } FOR { SIDE(=-5) | o } || { CHANGE(=+3) SAME(=-5) | i } LIKE { SIDE(=-5) | o }
57. { MEASURE(=-5) VALUE | o } || { MEASURE(=-5) | o } FOR { VALUE(=0) | o } || { MEASURE(=-5) | o } FOR { VALUE(=0) | o } FROM { GIVE(=0) | i }
58. { JOIN(=+3) MANY | a } || { MANY(=+3) | a } FOR { JOIN(=+3) | i } || { SAME(=-3) | a } FOR { JOIN(=+3) | i }
59. { RULE(=-5) STRONG | a } || { CAN | a } FOR { RULE(=+3) | o } || { CAN | a } AGAINST { RULE(=+3) | o } FROM { SOMEONE(=+5) | o }
60. { SAY(=+3) WANT | i } || { SAY(=+3) | i } FOR { RULE(=+3) | o } || { SAY(=+3) WANT | i } FOR { RULE(=+3) | o } FROM { MANY(=+3) | o }
