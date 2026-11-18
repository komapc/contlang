1. { PART(=+5) PART(=+5) | a } LIKE { PART(=+5) PART(=+5) | a I+4 }
2. { GIVE(=+5) DO(=+5) MOVE(=+5) | i } LIKE { SAY | i I+5 }
3. { DO(=+3) MOVE | o agent } FOR { MOVE PART(=+2) | o }
4. { THINK GOOD(=-5) | i I+4 } LIKE { DO(=+5) GOOD(=-5) | i }
5. { DO(=+3) KNOW(=+5) | o quality } FOR { GOOD DO | o result }
6. { GIVE GOOD | o agent } FROM { KNOW(=+5) RULE(=+3) | o }
7. { GIVE(=-2) SOMEONE(=+5) | i } FROM { SOMEONE(=-3) GIVE(=+5) | i }
8. { GOOD(=+3) GOOD(=+4) | a C+3 } PI { PART(=+5) GOOD | o }
9. { RULE(=+5) GIVE(=+5) | o } FOR { THINK(=+5) SAY | o }
10. { PART(=+5) KNOW | o } LIKE { RULE(=-2) PART | o }
11. { GIVE(=+2) KNOW(=0) | i } FOR { SOMEONE(=-3) PART(=+5) | o N+3 }
12. { SAY KNOW | o result } FROM { DO PART(=+5) | o T-2 }
13. { SAY(=+5) MOVE(=+5) | o quality } FOR { KNOW(=0) THINK | o }
14. { PART(=+2) DO(=+3) | o } PI { PART(=+5) DO | o }
15. { PART(=-2) SOMEONE | o } FOR { KNOW SOMEONE | o }
16. { SAY(=-5) PART(=+5) | o result } FOR { SOMEONE(=-5) KNOW | o N+3 }
17. { GIVE KNOW | i } FOR { GOOD(=+3) THINK | a }
18. { PART(=-5) GOOD | o } FOR { DO(=+3) GIVE | i }
19. { GIVE(=+5) MOVE | o } FOR { SOMEONE PART | o }
20. { PART(=+5) GOOD(=+2) | a } LIKE { PART(=+5) PART(=+2) | a }
21. { DO(=+3) PART(=+1) | o result } FROM { DO(=+3) MOVE | o }
22. { PART(=-5) MOVE(=+5) | o } LIKE { THINK(=0) PART(=-5) | o }
23. { PART(=+2) PART(=+2) | o } LIKE { PART(=+2) PART(=+2) | o }
24. { DO(=+3) GOOD(=-3) | a } LIKE { DO(=-5) GOOD(=-2) | a }
25. { RULE(=+3) DO(=+3) | o } FOR { GIVE(=0) GIVE(=0) | i }
26. { DO(=+3) PART(=-2) | i } FROM { PART(=0) PART(=+5) | o }
27. { GOOD(=-3) DO(=+3) | a } LIKE { DO(=+5) THINK | a }
28. { DO(=-5) | a } AGAINST { PART(=-2) DO(=+5) GOOD(=-2) | o }
29. { PART(=-2) MOVE(=-5) | o } FOR { PART(=+5) DO | i }
30. { SAY GIVE(=+5) | o agent } FOR { RULE(=+3) THINK(=+5) | o }
31. { GIVE KNOW(=+3) | i } AGAINST { GOOD(=-5) THINK | a }
32. { PART(=0) MOVE(=-5) | o } LIKE { PART(=+5) PART(=-2) | o }
33. { PART(=+5) MOVE(=-5) | a I+4 } LIKE { MOVE(=+5) PART(=+5) | a }
34. { THINK KNOW | a } LIKE { THINK DO | a }
35. { GOOD(=+5) KNOW | o quality } LIKE { SAY(=+5) GOOD(=+5) | o }
36. { PART(=+5) PART(=+2) | o } LIKE { PART(=+5) PART(=+5) | o }
37. { PART(=0) GOOD(=+2) | a } LIKE { PART(=0) SOMEONE | a }
38. { PART(=+5) MOVE(=+2) | a } FROM { PART(=-5) MOVE | o }
39. { PART(=+5) PART(=0) | o } FROM { PART(=-2) PART(=-2) | o N+3 }
40. { SAY GOOD(=-5) | i } AGAINST { SOMEONE(=-3) DO | o }
41. { DO(=+3) MOVE | i } FOR { MOVE PART(=+2) | o }
42. { PART(=-2) MOVE | o } FOR { MOVE(=0) SOMEONE | i }
43. { PART(=-2) PART(=-5) | o } PI { PART(=0) KNOW | o }
44. { MOVE GOOD | o } FOR { SAY KNOW | o }
45. { PART(=-5) PART(=-5) | a } LIKE { PART(=-5) PART(=-2) | a }
46. { MOVE(=-5) PART(=0) | o } PI { PART(=+5) MOVE | o }
47. { PART MOVE(=-5) | o } FOR { MOVE(=+5) DO(=+3) | i }
48. { MOVE(=-2) PART(=+5) | o } FROM { PART(=-5) PART(=+3) | i }
49. { DO(=+3) GOOD(=-5) | i } FROM { RULE(=+5) SAY(=+5) | o }
50. { GOOD(=+2) PART(=-2) | o } PI { PART(=+5) SOMEONE | o }
51. { RULE(=+3) PART(=+5) | a } FOR { SOMEONE(=-3) DO | o }
52. { GIVE(=-5) KNOW(=+3) | i } FROM { THINK(=0) PART | o }
53. { DO(=+5) GOOD(=+3) | o quality } FOR { MOVE DO | i }
54. { PART(=-2) DO | o tool } FOR { GIVE MOVE | i }
55. { DO(=+3) PART(=+5) | o result } FROM { PART(=-2) PART(=+5) | o }
56. { RULE(=+3) PART | o } PI { RULE(=+5) PART(=+5) | o }
57. { PART(=-2) | o } FOR { RULE KNOW | o } PI { PART(=-5) | o }
58. { DO(=+3) PART(=0) | i } FOR { RULE(=+3) PART(=+5) | o }
59. { RULE(=+3) DO(=+5) | o quality } FOR { SAY(=+5) GIVE(=-5) | i }
60. { THINK(=-2) KNOW(=-5) | i K+5 } LIKE { SAY(=-5) THINK | i }
