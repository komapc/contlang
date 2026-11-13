1. { PART(=+5) PART(=+5) | a C+3 } LIKE { PART(=+5) PART(=+5) PART(=+5) | a I+4 }
2. { DO(=+4) MOVE(=+5) | i } LIKE { SAY(=+5) DO(=+3) | i I+5 } FOR { GOOD(=-3) | a }
3. { MOVE DO | o agent } FOR { MOVE(=+2) DO(=+3) SOMEONE | o tool }
4. { THINK(=-5) GOOD(=-5) SOMEONE(=-3) | i I+5 } LIKE { MOVE(=-5) GOOD(=-5) | i }
5. { DO KNOW(=+5) | o quality } FOR { DO(=+3) GOOD(=+3) SOMEONE | i }
6. { KNOW(=+5) DO(=+3) | o agent } FOR { GOOD SOMEONE PART(=-2) | o }
7. { GIVE(=-2) GOOD | i } FROM { SOMEONE(=-3) | o } FROM { GIVE(=+5) SOMEONE(=+5) | i }
8. { GOOD(=+3) GOOD | a C+3 } LIKE { GOOD(=+1) GOOD(=0) GOOD(=-1) | a }
9. { RULE(=+5) GIVE(=+5) | o } FOR { THINK(=+5) SAY SOMEONE | i }
10. { PART(=+5) KNOW(=0) | o result } LIKE { PART(=+2) PART(=+2) RULE | o }
11. { GIVE(=+5) KNOW(=0) | i } FOR { SOMEONE(=+3) PART(=+5) KNOW(=+3) | o }
12. { PART(=+5) DO | o result T-2 } FOR { KNOW(=+3) SAY SOMEONE | i }
13. { SAY(=+5) DO(=+3) | o quality I+4 } FOR { SOMEONE(=+3) KNOW(=0) THINK | i K+5 }
14. { DO(=+3) PART(=-2) | o } PI { SOMEONE PART(=+5) DO | o }
15. { PART(=-2) KNOW SAY | o } PI { SOMEONE(=-3) PART(=-2) | o }
16. { SAY(=-5) PART(=+5) | o result } FOR { SOMEONE PART(=+5) KNOW | i }
17. { GIVE(=+5) KNOW(=+3) | i } FOR { SAY(=+3) GOOD RULE | a }
18. { PART(=-5) GOOD(=+2) | o } FOR { DO(=+3) GOOD(=+3) | i } LIKE { MOVE(=+5) | a I+4 }
19. { MOVE GIVE(=+5) | o } FOR { SOMEONE(=+3) GIVE(=-2) PART(=-2) | i }
20. { PART(=+4) PART(=+3) | a } LIKE { PART(=+5) GOOD(=+1) GOOD(=0) | a }
21. { DO(=+3) PART(=-2) | o result } FROM { DO(=+3) THINK(=+3) KNOW | i T-2 }
22. { PART(=-5) MOVE(=+5) | o } LIKE { DO(=+5) KNOW(=0) PART(=-5) | i }
23. { PART(=+5) PART(=+2) | o } FROM { PART(=+2) PART(=+2) PART(=0) | o }
24. { DO(=-3) MOVE(=-3) GOOD(=-3) | a } LIKE { SOMEONE(=-3) PART(=-5) | a }
25. { RULE(=+3) PART(=+5) | o } FOR { GIVE(=0) DO(=+3) GOOD | i }
26. { DO(=+3) PART(=-2) PART(=-2) | i } FROM { PART(=+5) PART(=0) | o }
27. { DO(=+5) GOOD(=-2) | a } LIKE { THINK(=+5) DO(=+5) KNOW(=-2) | a }
28. { DO(=-5) GOOD | a } AGAINST { DO(=+5) PART(=-2) SOMEONE | o }
29. { PART(=-2) PART(=0) | o } FOR { DO(=+3) GOOD | i } PI { PART(=+5) | o }
30. { SAY KNOW | o agent } FOR { RULE(=+3) THINK(=+5) GOOD | o }
31. { GIVE KNOW(=+3) | i } FOR { SAY(=+3) THINK(=-5) GOOD(=-5) | i }
32. { PART(=0) PART(=-2) | o } FOR { DO(=+3) | i } PI { PART(=+5) PART(=+5) | o }
33. { PART(=+5) MOVE(=+5) | a } LIKE { PART(=+5) MOVE(=-5) SOMEONE(=-3) | a }
34. { THINK KNOW(=+3) | a } PI { SOMEONE PART(=-2) THINK | o }
35. { GOOD(=+5) KNOW(=0) | o quality } LIKE { GOOD(=+5) GOOD(=+5) PART(=+5) | a C+5 }
36. { PART(=+5) PART(=0) | o } FROM { PART(=+3) PART(=+3) PART(=+1) | o }
37. { PART(=0) GOOD(=+2) | a } FOR { SOMEONE PART(=0) PART(=0) | o }
38. { PART(=+5) MOVE(=+2) GOOD | a } PI { PART(=0) PART(=+5) | o }
39. { PART(=+5) PART(=+5) | o } FROM { PART(=-2) PART(=0) PART(=0) | o }
40. { SAY(=+3) RULE | i } FOR { SOMEONE(=-3) DO GOOD(=-5) | i }
41. { MOVE DO | i } FOR { MOVE(=+2) DO(=+3) SOMEONE | o }
42. { PART(=-2) MOVE | o } FOR { SOMEONE MOVE | i } PI { PART(=0) | o }
43. { PART(=-5) MOVE(=0) | o } FOR { KNOW(=0) PART(=0) PART(=-2) | i }
44. { MOVE DO(=+3) GOOD | o } LIKE { SAY KNOW | i }
45. { PART(=-5) PART(=-5) | a C-3 } LIKE { PART(=-5) PART(=-5) PART(=-5) | a I+4 }
46. { PART(=-2) KNOW | o } PI { PART(=+5) | o } FOR { SOMEONE MOVE | i }
47. { MOVE(=+5) DO | o tool } FOR { MOVE(=+5) DO(=+3) | i } LIKE { PART(=+5) | o }
48. { GOOD(=+2) PART(=+3) | o quality } LIKE { MOVE(=-2) PART(=+3) DO | i }
49. { RULE(=+5) DO(=+5) | i } FOR { DO(=-5) SOMEONE GOOD(=-5) | i }
50. { GOOD RULE(=+3) | o quality C+3 } PI { SOMEONE PART(=+5) KNOW | o }
51. { RULE(=+3) SAY | a } FOR { SOMEONE PART(=+5) DO(=+3) | o }
52. { DO(=+3) KNOW(=-5) | i } AGAINST { SAY KNOW PART(=-2) | o }
53. { DO(=+5) MOVE(=+5) | o } FOR { SOMEONE MOVE DO(=+3) | i K+5 }
54. { PART(=-2) DO(=+3) | o tool } FOR { MOVE(=+2) PART(=-2) | i } AGAINST { MOVE(=-5) | i }
55. { DO(=+3) PART(=+5) | o result } FROM { PART(=-2) PART(=+5) DO | o }
56. { PART(=-2) PART(=0) | o } FOR { RULE(=+3) SOMEONE | o } PI { RULE(=+5) | o }
57. { PART(=-2) THINK | o } PI { PART(=0) PART(=-5) | o } FOR { DO(=+3) | i }
58. { DO MOVE | i } FROM { PART(=+5) | o } FOR { RULE(=+3) PART(=0) | o }
59. { RULE(=+3) DO(=+5) | o quality } FOR { SOMEONE(=+3) MOVE DO | i K+5 }
60. { THINK(=-2) KNOW(=-3) | i K+4 } FROM { KNOW(=-5) PART SAY(=-5) | o }
