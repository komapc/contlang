1. { SAY TEXT | o result } || { SAY | o result } LIKE { KNOW(=+5) | o result D+3 } || { SAY | o result } FOR { KNOW(=+5) } LIKE { SAME(=+5) | a }
2. { FIGHT(=+3) BIG | o } || { FIGHT BIG(=+4) | o } FOR { GOOD(=-5) TIME | o } || { FIGHT BIG(=+4) | o quality } FOR { GOOD(=-5) | o } LIKE { MOVE(=+5) | i }
3. { DO GIVE(=+5) | i } || { DO PLACE | i } FOR { RULE | o } || { DO | i A-5 } FOR { PLACE | o } FOR { RULE(=+4) | o }
4. { DO | o agent } || { DO | o agent } FOR { DO | o tool } || { DO | o agent } FOR { DO | o tool } FOR { MOVE | i }
5. { MOVE ABOVE(=+5) | o } || { MOVE ABOVE(=+5) | o } FROM { FIGHT(=+3) | a } || { MOVE ABOVE(=+5) | o } FROM { FIGHT(=+3) | a } FROM { DO | o }
6. { THINK(=-5) BIG | o } || { THINK(=-5) VALUE(=+5) | o } || { THINK(=-5) VALUE(=+5) | o } FOR { THINK(=+5) | i }
7. { DO TEXT | o } || { TEXT | o } FOR { DO | o N+3 } || { TEXT | o result } FOR { DO | i } FOR { TIME(=+3) | o }
8. { THINK PART(=+2) | o } || { THINK PART(=+2) | i } FROM { PART(=-2) | o N+3 } || { THINK PART(=+5) | o result } FROM { PART(=-2) | o N+3 } FOR { KNOW(=+5) | o }
9. { GOOD(=+5) | a } || { GOOD(=+5) KNOW | a } || { GOOD(=+5) | a } FOR { KNOW | i } FOR { THINK(=+5) | i }
10. { PLACE GOOD(=+5) ABOVE(=+5) | o } || { PLACE GOOD(=+5) | o } PI { ABOVE(=+5) | o } || { PLACE GOOD(=+5) | o } PI { ABOVE(=+5) | o } FOR { SOMEONE(=-5) | o N+5 }
11. { KNOW(=+5) SAY | i } || { KNOW(=+5) | i } FROM { MOVE ABOVE | o } || { KNOW(=+5) | i } FROM { MOVE ABOVE | o } FOR { SAY | o }
12. { SAY(=+5) | i } || { SAY(=+5) | i } LIKE { FIGHT(=+3) | o } || { SAY(=+5) | i A-5 } LIKE { FIGHT(=+3) | o } FOR { MOVE(=+5) | i }
13. { TEXT THINK | o } || { TEXT | o } FROM { THINK | o } || { TEXT | o } FROM { THINK | o } LIKE { SAME(=-5) | a } FOR { KNOW | i }
14. { ABOVE(=+5) JOIN(=-5) | i } || { ABOVE(=+5) | i } LIKE { MOVE(=-5) | a } || { ABOVE(=+5) | i } LIKE { MOVE(=-5) | a } FOR { JOIN(=+5) ABOVE | i }
15. { FIGHT(=+2) ABOVE(=-5) | o } || { DO ABOVE(=-5) | o } || { DO BIG | o } FOR { ABOVE(=-5) | i } FOR { INSIDE(=0) | o }
16. { SAY(=-5) INSIDE | o } || { INSIDE(=0) | o } FOR { THINK(=+5) | i } || { MOVE(=-5) | o } FOR { THINK(=+5) | i }
17. { SAY TEXT | o } || { SAY | o } FOR { KNOW(=+5) | o } || { SAY | o } FOR { KNOW(=+5) | o } FOR { SOMEONE N+3 | o }
18. { RULE(=+4) VALUE | o agent } || { RULE(=+4) | o agent } FOR { VALUE | o } || { RULE(=+4) | o agent } FOR { VALUE | o } FOR { GIVE(=+5) | i }
19. { MOVE | o tool } || { PART(=-2) | o } PI { MOVE | o } || { PART(=-2) | o } PI { INSIDE(=+5) | o } FOR { MOVE BIG | i }
20. { VALUE(=-5) | o } || { VALUE(=-5) GIVE(=0) | o } || { VALUE(=-5) GIVE(=0) | o } FOR { DO | o N+3 }
21. { VALUE GIVE(=0) | o tool } || { VALUE | o } FOR { GIVE(=0) | i } || { VALUE | o } FOR { GIVE(=0) | i } FOR { RULE(=+5) | o }
22. { PLACE BIG | o } || { PLACE | o } FOR { RULE(=+4) | o } || { PLACE | o } FOR { DO | i } FOR { RULE(=+4) | o }
23. { SOMEONE PART(=+5) SAME | o } || { PART(=+5) | o } FOR { SAME(=+5) | a } || { PART(=+5) SOMEONE | o } FOR { SAME(=+5) THINK | o } FOR { JOIN(=+5) | i }
24. { MOVE(=-5) ABOVE(=+5) | i } || { MOVE(=-5) | i } LIKE { ABOVE(=+5) | a } || { MOVE(=-5) | i } LIKE { ABOVE(=+5) | a } FOR { SOMEONE | o }
25. { GIVE(=+5) GOOD | i } || { DO GOOD | i } FOR { SOMEONE | o } || { DO GOOD | i } FOR { SOMEONE | o } FOR { GIVE(=+5) | i }
26. { SAY PART(=-2) | o } || { SAY PART(=-2) | o } PI { TEXT | o } || { SAY PART(=-2) | o } PI { TEXT | o } FOR { THINK | o }
27. { JOIN DO | i } || { JOIN(=+5) | i } LIKE { TEXT | o } || { JOIN(=+5) PART(=-5) | i } FOR { DO | i } LIKE { ABOVE(=-5) | o }
28. { FIGHT(=-5) | i } || { FIGHT(=-5) JOIN | i } || { FIGHT(=-5) JOIN | i } LIKE { FIGHT(=+3) | o } FOR { SOMEONE | o }
29. { RULE(=+4) DO | i } || { DO | i } FOR { RULE(=+5) | o } || { DO | i } FOR { RULE(=+5) | o } FOR { SOMEONE(=+3) | o }
30. { DO THINK | a } || { THINK | a } FOR { DO | i } || { THINK | a } FOR { DO | i } FOR { SAME(=+3) | a }
31. { KNOW(=+5) THINK | i } || { THINK | i } FOR { KNOW(=+5) | o } || { THINK | i } FOR { KNOW(=+5) | o } FOR { TEXT | o }
32. { DO TIME | o } || { DO | o } FOR { TIME | o } || { DO | o } FOR { TIME | o } FOR { DO | o result }
33. { GOOD(=+3) DO | i } || { DO GOOD | i } FOR { GIVE(=+5) | o } || { DO GOOD | i } FOR { GIVE(=+5) | o } FOR { JOIN(=+5) | i }
34. { DO PLACE | a } || { DO | a } FOR { PLACE | o } || { DO | a } FOR { PLACE | o } FOR { DO BIG | o N+3 }
35. { SAY(=-5) | i } || { SAY(=-5) | i } FOR { SOMEONE | o } || { SAY(=-5) | i } LIKE { MOVE(=-5) | a } FOR { SOMEONE | o }
36. { JOIN(=-5) | i } || { JOIN(=-5) MOVE | i } || { JOIN(=-5) | i } FOR { MOVE | i } FOR { PLACE | o }
37. { RULE(=-5) KNOW | a } || { SOMEONE | o agent } FOR { KNOW(=+5) | i } || { SOMEONE | o agent } FOR { KNOW(=+5) | i } FOR { GOOD | a }
38. { KNOW | o result N+3 } || { KNOW(=+5) | o result N+3 } FROM { TEXT | o } || { KNOW(=+5) | o result N+3 } FOR { THINK | i } FROM { TEXT | o }
39. { SOMEONE DO | o agent } || { SOMEONE | o agent } FOR { GIVE(=-5) | i } || { SOMEONE | o agent } FOR { GIVE(=-5) | i } FOR { PLACE | o }
40. { TIME DO | i } || { DO | i } FOR { TIME | o } || { DO | i } FOR { TIME | o } FOR { SAME | a }
41. { INSIDE(=0) KNOW | a } || { KNOW(=0) | a } FOR { INSIDE(=0) | o } || { KNOW(=0) | a } FOR { INSIDE(=0) | o } FOR { MOVE | i }
42. { JOIN(=-5) | i } LIKE { INSIDE(=0) | o } || { JOIN(=-5) INSIDE(=0) | i } || { JOIN(=-5) | i } LIKE { INSIDE(=0) | o } FOR { PLACE | o }
43. { SOMEONE | o } AGAINST { BIG(=+3) | a } || { SOMEONE(=-5) BIG(=-3) | o } || { SOMEONE | o } LIKE { BIG(=-3) | a } FOR { SOMEONE | o agent }
44. { VALUE(=+5) | a } || { VALUE(=+5) BIG | a } || { VALUE(=+5) | a } FOR { SOMEONE | o N+5 }
45. { RULE(=+4) INSIDE(=+5) | a } || { RULE(=+4) | a } FROM { INSIDE(=+5) | o } || { RULE(=+4) | a } AGAINST { SOMEONE(=-5) | o } FOR { RULE | i }
46. { JOIN(=+5) | i } || { JOIN(=+5) PART | i } || { JOIN(=+5) BIG | i }
47. { MOVE FIGHT | o } || { ABOVE(=+5) | o } FROM { FIGHT(=+3) | a } || { MOVE ABOVE(=+5) | o } FROM { FIGHT(=+3) | a } FOR { TIME(=0) | o }
48. { PART(=+2) | o } || { PART(=+2) | o } PI { SOMEONE | o } || { PART(=+2) | o } PI { SOMEONE | o } FROM { PART(=-2) | o N+3 }
49. { FIGHT(=+3) | o } FOR { ABOVE | o } || { FIGHT(=+3) | o } FOR { DO ABOVE | o } || { ABOVE | o } FOR { FIGHT(=+3) | o } FOR { SAY(=-5) | o }
50. { SAY | o } FOR { PART | o } || { DO GOOD SAY | o result } FOR { PART(=+5) | o } || { DO GOOD SAY | o result } FOR { SOMEONE | o N+3 } FOR { PART(=+5) | o }
51. { DO | i } FOR { SOMEONE | o } || { DO | i } FOR { KNOW(=+5) | i } || { DO | i } FOR { KNOW(=+5) | i } FOR { SOMEONE | o N+3 }
52. { DO | i } FOR { DO | i } || { DO | i } FOR { GIVE(=+5) | i } || { DO | i } FOR { PART(=-2) | o } FOR { DO | o }
53. { FIGHT(=+5) | i } || { DO | i } FOR { SOMEONE | o M-5 } || { FIGHT(=+5) | i } FOR { DO | i } FOR { SOMEONE | o M-5 }
54. { SAY SOMEONE | i } || { SAY | i } FOR { KNOW(=+5) | i } || { SAY | i } FOR { SOMEONE | o } FOR { GOOD | a }
55. { TEXT | o } FOR { SAME(=+5) | a } || { SAME(=+5) | o } FROM { TEXT | o } || { TEXT SAME(=+5) | o } FOR { THINK | i } FOR { PART | o N+3 }
56. { SAME(=-5) DO | i } || { SAME(=-5) | i } FOR { MOVE | i } || { SAME(=-5) | i } FOR { MOVE | i } FOR { TIME(=-5) | o }
57. { PART(=-2) VALUE | o } || { VALUE | o } FOR { BIG | o } || { VALUE | o } FOR { BIG | o } FOR { GIVE | i }
58. { JOIN(=+5) | a } || { JOIN(=+5) PART | a } || { JOIN(=+5) | a } FOR { PART(=-2) | o }
59. { RULE(=-5) | a } || { RULE(=+4) | a M-5 } || { RULE(=+4) M-5 | a } FOR { SOMEONE | o }
60. { THINK(=+5) SOMEONE | i } || { THINK(=+5) | i } FOR { RULE | o } || { THINK(=+5) | i } FOR { RULE | o } FOR { SOMEONE | o N+3 }
