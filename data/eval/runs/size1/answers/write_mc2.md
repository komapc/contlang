1. { SAY TRUE | o result } || { SAY | o result } FOR { KNOW(=+5) | i } || { SAY TRUE | o result } FOR { KNOW(=+5) | i } LIKE { TEXT | o }
2. { HAPPEN FEEL(=+5) GOOD(=-5) | o } || { HAPPEN GOOD(=-5) | o } LIKE { FEEL(=+5) | o } || { HAPPEN GOOD(=-5) | o } LIKE { FEEL(=+5) | o } FOR { CARE | i }
3. { BEGIN(=-5) DO | i } || { DO | i } FOR { BEGIN(=-5) | o } || { DO | i } FOR { BEGIN(=-5) | o } PI { PLACE | o }
4. { DO ART | o agent } || { ART | o agent } FOR { DO | o tool } || { ART | o agent } FOR { DO | i } FROM { MOVE STRONG | o tool }
5. { HEAT(=+4) GRAIN(=-5) | o } || { GRAIN(=-5) | o } FROM { HEAT(=+4) GRAIN(=-3) | o } || { GRAIN(=-5) | o } FROM { HEAT(=+4) GRAIN(=-3) | o } PI { ABOVE | o }
6. { THINK VALUE(=+5) | o } || { VALUE(=+5) THINK(=-5) | o } FOR { THINK(=+5) | i } || { VALUE(=+5) THINK(=-5) | o } FOR { FIGHT | o } FOR { THINK(=+5) | i }
7. { TEXT DO | o result } || { TEXT | o } FOR { DO | i } || { TEXT | o } FOR { DO | i } PI { TIME(=+3) | o }
8. { THINK SAME(=+3) | o } || { THINK | o } FROM { PART(=-5) | o } || { THINK | o } FROM { PART(=-5) | o } FOR { PART(=+5) | o }
9. { GOOD SEE | a } || { GOOD(=+5) | a } LIKE { SEE | i } || { GOOD(=+5) | a } LIKE { SEE | i } FOR { FEEL(=+4) | o }
10. { PLACE GOOD(=+5) | o } || { PLACE | o } FOR { GOOD(=+5) FEEL(=-5) | o } || { PLACE ABOVE(=+5) | o } FOR { GOOD(=+5) FEEL(=-5) | o }
11. { SEE | i agent } || { SAY | o tool } FOR { KNOW | i } || { SEE | i tool } FOR { KNOW | i } LIKE { HAPPEN | o }
12. { SAY(=+5) | i } || { SAY(=+5) | i } LIKE { FEEL(=+5) | o } || { SAY(=+5) | i } LIKE { FEEL(=+5) | o } FROM { MOVE(=+5) | o }
13. { TEXT TRUE(=-5) | o } || { TEXT | o } FROM { THINK TRUE(=-5) | o } || { TEXT | o } FROM { THINK ART | o } LIKE { TRUE(=-5) | o }
14. { ABOVE JOIN | i } || { JOIN | i } FOR { ABOVE | a } || { JOIN | i } FOR { ABOVE | a } FROM { MOVE(=-5) | o }
15. { STRONG MEASURE | o } || { STRONG | o } FOR { MEASURE(=+5) | o } || { STRONG | o } FOR { MEASURE(=-5) | o } PI { SHAPE(=+5) | o }
16. { FEEL BODY CONSUME(=+5) | o } || { FEEL | o result } FOR { BODY | o } || { FEEL | o } FOR { BODY | o } FROM { GRAIN(=-5) | o }
17. { SAY TEXT | o } || { SAY | o tool } FOR { KNOW(=+5) | i } || { SAY | o tool } FOR { KNOW(=+5) | i } PI { PART(=+5) | o }
18. { RULE(=+4) VALUE | o agent } || { RULE(=+4) | o agent } FOR { VALUE | o } || { RULE(=+4) | o agent } FOR { VALUE | o } FOR { GIVE | i }
19. { BODY MOVE STRONG | o } || { BODY | o } FOR { MOVE | i } || { BODY | o } FOR { MOVE STRONG | i } PI { BODY | o }
20. { VALUE(=-5) GIVE | o } || { GIVE(=0) | i } FOR { VALUE(=-5) | o } || { GIVE(=0) | o } FOR { VALUE(=-5) | o } FOR { THING | o }
21. { VALUE GIVE | o } || { VALUE(=-5) | o } FOR { GIVE(=0) | i } || { VALUE(=-5) | o } FOR { GIVE(=0) | i } FOR { MEASURE | o }
22. { LAND MEASURE | o } || { PLACE | o } FOR { RULE | o } || { PLACE | o } FOR { STRONG | o } FOR { MEASURE(=-5) | o }
23. { PART(=+5) FRIEND | o } || { PART(=+5) | o } FOR { FRIEND(=+5) | o } || { PART(=+5) | o } FOR { FRIEND(=+5) | o } FOR { SAME(=+3) | o }
24. { MOVE(=-5) ABOVE | i } || { MOVE(=-5) | i } FOR { ABOVE | a } || { MOVE(=-5) | i } LIKE { ABOVE(=+5) | a } LIKE { SHAPE(=-5) | o }
25. { GIVE(=+5) STRONG | i } || { GIVE(=+5) | i } FOR { CAN | o } || { GIVE(=+5) | i } FOR { CAN | o } FOR { FRIEND(=+5) | o }
26. { SAY TEXT PART(=-2) | o } || { TEXT PART(=-2) | o } || { TEXT | o } PI { TEXT | o } LIKE { PART(=-2) | o }
27. { TEXT LONG(=-5) | i } || { JOIN(=+5) | i } FROM { LONG(=-5) | o } || { JOIN(=+5) | i } FROM { LONG(=-5) | o } LIKE { TOUCH(=-5) | o }
28. { FIGHT BODY | i } || { FIGHT(=0) | i } LIKE { BODY | o } || { FIGHT(=-5) | i } FOR { BODY STRONG | o } LIKE { MOVE | i }
29. { RULE(=+4) DO | i } || { DO | i } FOR { RULE(=+4) | o } || { DO | i } FOR { RULE(=+4) | o } FOR { KNOW | i }
30. { WANT CAN | a } || { CAN(=+3) | a } FOR { DO | i } || { CAN(=+3) | a } FOR { WANT | i } FOR { DO | i }
31. { KNOW SAY | i } || { KNOW(=+5) | i } FOR { TEXT | o } || { KNOW(=+5) | i } FOR { TEXT | o } FOR { SAY | o }
32. { DO CHANGE | o } || { DO | o } FOR { HAPPEN | o result } || { DO | o } FOR { CHANGE | o } FOR { HAPPEN | o result }
33. { CHANGE GOOD(=+3) | i } || { GOOD(=+3) | i } FOR { CHANGE | i } || { CHANGE GOOD(=+3) | i } FOR { VALUE | o }
34. { DO ART(=-5) | a } || { ART(=-5) | a } FOR { DO | i } || { ART(=-5) | a } FOR { DO | i } FROM { MEASURE(=-5) | o }
35. { SAY(=-5) | i } || { SAY(=-5) | i } LIKE { FEEL(=-5) | a } || { SAY(=-5) | i } LIKE { FEEL(=-5) | a } FOR { FRIEND | o }
36. { JOIN(=-5) | i } || { JOIN(=-5) | i } FOR { MOVE | i } || { JOIN(=-5) | i } FOR { MOVE | i } FROM { PLACE | o }
37. { RULE KNOW FRIEND | a } || { FRIEND | a } FOR { KNOW(=+5) | i } || { THING | a } FOR { KNOW(=+5) | i } PI { RULE(=+4) | o }
38. { TEXT TRUE | o N+3 } || { TRUE | o N+3 } PI { TEXT | o } || { TRUE | o N+3 } PI { TEXT | o } FOR { THINK | i }
39. { THING(=+4) CONSUME | o agent } || { DO | o agent } FOR { THING(=+4) | o } || { DO | o agent } FOR { THING(=+4) | o } PI { LAND(=-5) | o }
40. { TIME DO | i } || { TIME | i } FOR { DO | i } || { TIME | i } FOR { DO | i } LIKE { MOVE | i }
41. { FEEL TOUCH(=-5) | a } || { FEEL | a } FOR { TOUCH | o } || { FEEL | a } FOR { TOUCH | o } FOR { BODY | o }
42. { SIDE(=0) | i } || { JOIN(=-5) | i } FOR { SIDE | o } || { INSIDE(=0) | i } FOR { SIDE | o } PI { JOIN(=-5) | o }
43. { SEX(=-5) SOMEONE TIME(=-2) | o } || { SEX(=-5) | o agent } LIKE { TIME(=-3) | a } || { SEX(=-5) | o agent } LIKE { TIME(=-3) | a } PI { BODY | o }
44. { VALUE(=+5) | a } || { VALUE(=+5) | a } || { VALUE(=+5) | a I+4 }
45. { RULE(=+4) STRONG | a } || { RULE(=+5) | a } AGAINST { RULE(=+4) | o } || { RULE(=+5) | a } AGAINST { RULE(=+4) | o } PI { PART(=+5) | o }
46. { JOIN(=+5) | i } || { JOIN(=+5) | i } FOR { MANY(=+3) | o } || { JOIN(=+5) | i } FOR { MANY(=+3) | o } FOR { BIG | o }
47. { HEAT LIGHT | o } || { HEAT(=+5) LIGHT(=+5) | o } || { HEAT(=+5) LIGHT(=+5) | o } PI { HEAT(=+5) | o }
48. { BODY PART(=+2) | o } || { BODY | o } || { BODY LIVE | o }
49. { LIGHT | o tool } || { LONG(=0) | o } FOR { LIGHT | o } || { LONG | o } FOR { LIGHT | o } FROM { GRAIN(=-3) | o }
50. { ART(=+5) | o result } || { ART(=+5) | o result } FOR { SOMEONE(=+5) | o } || { ART(=+5) | o result } FOR { MANY(=+3) | o } FOR { SAY | o }
51. { SEE | i K+5 } || { DO | i } FOR { SEE | i } || { DO | i } FOR { SEE | i } FOR { KNOW | i }
52. { DO CAN | i } || { DO | i } FOR { CAN | o } || { DO | i } FOR { CAN | o } FOR { VALUE | o }
53. { LIVE(=-5) DO | i } || { LIVE(=-5) | i V+4 } || { LIVE(=-5) | i K+5 } FOR { FIGHT | o }
54. { SAY SAME(=-4) | i } || { SAY | i } FOR { SAME(=-4) | o } || { SAY | i } FOR { SAME(=-4) | o } FOR { KNOW | i }
55. { SAME TEXT MEASURE | o } || { SAME | o } FOR { MEASURE(=-5) | o } || { SAME(=+5) | o } FOR { MEASURE | o } FOR { ART(=-5) | o }
56. { CHANGE SAME(=-5) | i } || { CHANGE(=+5) | i } FOR { SAME(=-5) | o } || { CHANGE(=+5) | i } FOR { SIDE(=-5) | o }
57. { MEASURE(=-5) VALUE | o } || { MEASURE(=-5) | o } FOR { VALUE(=-5) | o } || { MEASURE(=-5) | o } FOR { VALUE(=-5) | o } FOR { GIVE | o }
58. { JOIN(=+5) | a } || { JOIN(=+5) | a result } || { MANY(=+3) | a } FOR { JOIN(=+5) | i }
59. { RULE(=-5) | a } || { RULE(=+5) | a M-5 } || { RULE(=+4) | a M-5 }
60. { THINK(=+5) WANT | i } || { WANT | i } FOR { RULE(=+4) | o } || { THINK(=+5) | i } FOR { RULE(=+4) | o } FOR { MANY(=+3) | o }
