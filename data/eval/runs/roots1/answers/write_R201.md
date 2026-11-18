1. { BIG(=+3) | a } || { BIG(=+3) | a } || { BIG(=+3) | a }
2. { FIGHT(=+1) SAY(=+4) | i } || { FIGHT(=+2) SAY(=+5) | i } || { FIGHT(=+2) SAY(=+5) | i }
3. { DO | o agent } || { DO | o agent } FOR { MOVE | o tool } || { DO | o agent } FOR { MOVE | o tool }
4. { GOOD(=-5) THINK | i I+5 } || { GOOD(=-5) THINK | i I+5 } || { GOOD(=-5) THINK | i I+5 }
5. { DO GOOD | o quality } || { DO | o quality } || { DO GOOD | o quality }
6. { KNOW DO GOOD | o agent } || { DO | o agent } AGAINST { GOOD(=-3) | o quality } || { KNOW(=+5) | o agent } FOR { DO | i } AGAINST { GOOD(=-3) | o quality }
7. { GIVE(=0) | i } || { GIVE(=0) | i } || { GIVE(=0) | i }
8. { GOOD | a C+3 } || { GOOD | a C+3 } || { GOOD | a C+3 }
9. { RULE(=+5) SAY THINK(=+5) | o } || { SAY THINK(=+5) | o } PI { RULE(=+5) | o } || { SAY THINK(=+5) | o } PI { RULE(=+5) | o } PI { PART(=+5) SOMEONE | o }
10. { SAME(=+3) PART | o } || { SAME(=+3) PART | o } || { SAME(=+3) PART | o }
11. { GIVE(=+5) KNOW | i } || { GIVE(=+5) KNOW | i } FOR { PART(=+5) SOMEONE | o } || { GIVE(=+5) KNOW | i } FOR { PART(=+5) SOMEONE | o }
12. { TIME(=-5) TEXT | o } || { TIME(=-5) PART(=+2) | o } || { TIME(=-5) PART(=+2) TEXT | o }
13. { VALUE(=+5) KNOW | o quality } || { VALUE(=+5) KNOW | o quality } || { VALUE(=+5) KNOW | o quality }
14. { JOIN INSIDE PART(=+5) | o } || { JOIN INSIDE | o } PI { PART(=+5) | o } || { JOIN INSIDE | o } PI { PART(=+5) | o }
15. { PART(=-2) SOMEONE | o } || { PART(=-2) SOMEONE | o } || { PART(=-2) SOMEONE | o }
16. { TEXT SAY KNOW | o } || { TEXT | o } FOR { SAY KNOW | o } || { TEXT | o } FOR { SAY KNOW | o } FOR { PART(=+5) SOMEONE | o }
17. { THINK SAME(=+5) | i } || { SAME(=+5) THINK | i } || { SAME(=+5) THINK | i }
18. { PART(=-5) GOOD | o } || { PART(=-5) | o } FOR { GOOD | a } || { PART(=-5) | o } FOR { GOOD | a }
19. { GIVE(=+5) MOVE | o } || { GIVE(=+5) MOVE | o } || { GIVE(=+5) MOVE | o }
20. { BIG(=+2) | a } || { BIG(=+2) | a } || { BIG(=+2) | a }
21. { DO | o result } || { DO | o result } || { TIME(=+1) DO | o result }
22. { TIME(=0) BIG(=-5) | o } || { TIME(=0) BIG(=-5) | o } || { TIME(=0) BIG(=-5) | o }
23. { PART(=+5) | o N+1 } || { SAME(=+3) PART | o N+1 } || { PART(=+5) | o N+1 }
24. { FIGHT(=+3) | a M-5 } || { FIGHT(=+3) | a M-5 } || { FIGHT(=+3) | a M-5 }
25. { PART(=+5) VALUE(=-5) | o } || { PART(=+5) | o } FOR { VALUE(=-5) | o } || { PART(=+5) | o } FOR { VALUE(=-5) | o }
26. { JOIN(=-5) PART | i } || { JOIN(=-5) PART | i } || { JOIN(=-5) PART | i }
27. { DO FIGHT(=+1) | a } || { DO | a M-5 } || { DO FIGHT(=+1) | a }
28. { FIGHT INSIDE PART | a } || { FIGHT | a } AGAINST { BIG INSIDE | o } || { FIGHT | a } AGAINST { BIG INSIDE | o }
29. { PART JOIN | o } || { PART | o } FOR { INSIDE(=0) JOIN | i } || { PART | o } FOR { INSIDE(=0) JOIN | i }
30. { SAY ABOVE(=+5) | o agent } || { SAY | o agent } PI { RULE(=+4) ABOVE(=+5) | o } || { SAY | o agent } PI { RULE(=+4) ABOVE(=+5) | o }
31. { THINK SAME(=-5) | i } || { THINK SAME(=-5) | i } || { THINK SAME(=-5) | i }
32. { PART(=+2) | o } || { PART(=+2) | o } || { PART(=+2) | o }
33. { ABOVE BIG | a } || { ABOVE BIG | a } || { ABOVE BIG | a }
34. { THINK | a } || { THINK | a } || { THINK | a }
35. { GOOD(=+5) BIG | o quality } || { GOOD(=+5) BIG | o quality } || { GOOD(=+5) BIG | o quality }
36. { TIME PART | o } || { TIME PART | o } || { TIME PART | o }
37. { SAME(=-4) | a } || { SAME(=-4) | a } || { SAME(=-4) | a }
38. { INSIDE BIG | a } || { INSIDE BIG | a } || { INSIDE BIG | a }
39. { PART(=+5) | o } || { PART(=+5) | o } || { PART(=+5) | o }
40. { SAY FIGHT GOOD(=-3) | i } || { SAY FIGHT GOOD(=-3) | i } || { SAY FIGHT GOOD(=-3) | i }
41. { MOVE DO | i V+4 } || { MOVE DO | i V+4 } || { MOVE DO | i V+4 }
42. { PLACE INSIDE(=0) | o } || { PLACE INSIDE(=0) | o } || { PLACE MOVE INSIDE | o }
43. { INSIDE(=0) PART | o } || { INSIDE(=0) PART | o } || { INSIDE(=0) PART | o }
44. { MOVE GOOD(=+3) | o } || { MOVE GOOD(=+3) | o } || { MOVE GOOD(=+3) | o }
45. { BIG(=-3) | a } || { BIG(=-3) | a } || { BIG(=-3) | a }
46. { PLACE | o } || { PLACE | o } || { PLACE | o }
47. { DO MOVE | o tool } || { DO MOVE | o tool } || { DO MOVE | o tool }
48. { BIG(=+2) DO | o } || { BIG(=+2) DO | o } || { BIG(=+2) DO | o }
49. { RULE(=+5) FIGHT(=+5) | i } || { RULE(=+5) FIGHT(=+5) | i } || { RULE(=+5) FIGHT(=+5) | i }
50. { ABOVE SOMEONE | o quality } || { ABOVE SOMEONE | o quality } || { ABOVE SOMEONE | o quality }
51. { RULE(=+4) | a } || { RULE(=+4) | a } || { RULE(=+4) | a }
52. { JOIN(=-5) TEXT | i } || { JOIN(=-5) TEXT | i } || { JOIN(=-5) TEXT | i }
53. { BIG DO | o } || { BIG DO | o } || { BIG DO | o }
54. { JOIN INSIDE | o tool } || { JOIN INSIDE | o tool } || { JOIN INSIDE | o tool }
55. { DO PART(=+5) | o result } || { DO PART(=+5) | o result } || { DO PART(=+5) | o result }
56. { PLACE RULE | o } || { PLACE RULE | o } PI { PART(=+5) | o } || { PLACE RULE | o } PI { PART(=+5) | o }
57. { INSIDE(=+5) PART | o } || { INSIDE(=+5) PART | o } || { INSIDE(=+5) PART | o }
58. { INSIDE(=+5) | i K+5 } || { INSIDE(=+5) | i K+5 } || { INSIDE(=+5) | i K+5 }
59. { RULE BIG | o } || { RULE BIG | o } || { RULE BIG | o }
60. { THINK(=-3) KNOW(=-5) | i } || { THINK(=-3) KNOW(=-5) | i } || { THINK(=-3) KNOW(=-5) | i }
