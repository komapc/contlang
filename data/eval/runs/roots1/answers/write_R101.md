1. { PART(=+4) | a } || { PART(=+4) | a } || { PART(=+4) | a I+3 }
2. { DO MOVE(=+5) | i } || { DO MOVE(=+5) | i } LIKE { SAY(=+5) | o } || { DO MOVE(=+5) | i } LIKE { SAY(=+5) | o }
3. { DO MOVE | o agent } || { DO | o agent } FOR { MOVE(=+4) | i } || { DO | o agent } FOR { MOVE(=+4) | o tool }
4. { GOOD(=-5) THINK | i } || { GOOD(=-5) THINK | i I+4 } || { GOOD(=-5) THINK | i I+5 }
5. { DO GOOD | o quality } || { DO GOOD | o quality } || { DO | o quality } FOR { DO GOOD | i }
6. { DO GOOD KNOW | o agent } || { DO GOOD | o agent } FOR { SOMEONE GOOD(=-3) | o } || { DO GOOD(=+4) | o agent } FOR { SOMEONE GOOD(=-3) | o }
7. { GIVE(=0) | i } || { GIVE(=0) | i } || { GIVE(=-1) | i }
8. { GOOD | a C+3 } || { GOOD | a C+3 } || { GOOD | a C+3 }
9. { RULE(=+5) THINK(=+5) | o quality } || { RULE(=+5) | o quality } FOR { THINK(=+5) | i } || { RULE(=+5) | o quality } FOR { THINK(=+5) | i } FOR { SOMEONE(=0) N+3 | o }
10. { PART(=+2) KNOW | o } || { PART(=+2) | o } LIKE { KNOW | o } || { PART(=+2) | o } FOR { KNOW | i }
11. { GIVE(=+5) KNOW | i } || { GIVE(=+5) KNOW | i } || { DO KNOW(=+5) | i } FOR { SOMEONE N+3 | o }
12. { KNOW PART(=+5) | o T-2 } || { KNOW | o result T-2 } || { KNOW | o result } PI { PART(=+5) | o T-2 }
13. { SAY(=+5) KNOW | o quality } || { SAY(=+5) KNOW | o quality } || { SAY(=+5) KNOW | o quality }
14. { PART(=-2) DO | o quality } || { PART(=-2) DO | o quality } || { DO | o } PI { PART(=+5) SOMEONE | o }
15. { PART(=-2) SOMEONE | o } || { PART(=-2) | o } PI { SOMEONE | o } || { PART(=-2) | o } PI { SOMEONE | o } PI { THINK | o }
16. { SAY KNOW | o result } || { SAY | o result } FOR { KNOW | i ? } || { SAY | o result } FOR { KNOW | i ? } FOR { SOMEONE N+3 | o }
17. { KNOW(=+5) GOOD | i } || { KNOW(=+5) GOOD | i } || { KNOW(=+5) | i } FOR { GOOD | a }
18. { GOOD(=+2) PART(=-5) | o } || { PART(=-3) | o } FOR { DO GOOD | i } || { PART(=-3) | o } FOR { DO GOOD | i } FROM { PART(=+2) | o }
19. { GIVE(=+5) MOVE | o } || { GIVE(=+5) MOVE | o result } || { GIVE(=+5) MOVE | o result }
20. { PART(=+3) | a } || { PART(=+3) | a } || { PART(=+3) | a I+2 }
21. { DO | o result } || { DO | o result } || { DO | o result }
22. { PART(=-5) MOVE | o } || { PART(=-5) | o } PI { MOVE | o } || { PART(=-5) | o } PI { MOVE | o }
23. { PART(=+1) | o N+1 } || { PART(=+1) | o N+1 } || { PART(=+1) | o N+1 }
24. { GOOD(=-3) MOVE | a } || { GOOD(=-3) MOVE | a } || { GOOD(=-3) MOVE | a }
25. { PART(=+5) DO | o } || { RULE(=+4) | o } FOR { GIVE DO | o } || { RULE(=+4) | o } FOR { GIVE DO | o }
26. { PART(=-3) DO | i } || { PART(=-3) DO | i } || { PART(=-3) DO | i }
27. { DO GOOD(=-3) | a } || { DO GOOD(=-3) | a } || { DO GOOD(=-3) | a }
28. { DO | a } AGAINST { PART(=-2) DO | o } || { DO | a } AGAINST { PART(=-2) DO | o } || { DO GOOD | a } AGAINST { PART(=-2) DO | o I+4 }
29. { PART(=-2) | o } || { PART(=-2) | o } FOR { PART(=+2) | o } || { PART(=-2) | o } FOR { PART(=+2) | o }
30. { SAY KNOW(=+5) GOOD | o agent } || { SAY KNOW(=+5) | o agent } FOR { THINK | o } || { RULE(=+4) | o agent } FOR { SAY KNOW(=+5) | o }
31. { KNOW(=+5) GOOD(=-5) | i } || { KNOW(=+5) GOOD(=-5) | i } || { KNOW(=+5) GOOD(=-5) | i }
32. { PART(=+2) | o } || { PART(=+2) | o } || { PART(=+2) | o }
33. { PART(=+4) | a } || { PART(=+4) | a } || { PART(=+4) | a }
34. { THINK | a } || { THINK | a } || { THINK | a }
35. { GOOD(=+5) | o quality I+5 } || { GOOD(=+5) | o quality I+5 } || { GOOD(=+5) | o quality I+5 }
36. { PART(=+3) MOVE | o } || { PART(=+3) MOVE | o } || { PART(=+3) MOVE | o }
37. { SOMEONE GOOD | a } || { SOMEONE GOOD | a } || { SOMEONE GOOD | a }
38. { PART(=+5) GIVE | a } || { PART(=+5) GIVE | a } || { PART(=+5) GIVE | a }
39. { PART(=+5) | o } || { PART(=+5) | o } || { PART(=+5) | o }
40. { SAY GOOD(=-5) | i } || { SAY RULE | i } || { SAY GOOD(=-5) | i } FOR { RULE | o }
41. { DO MOVE | i } || { DO MOVE | i } || { DO MOVE | i }
42. { MOVE PART | o } || { MOVE | o } PI { PART(=-2) | o } || { MOVE | o } PI { PART(=-2) | o }
43. { PART(=-2) | o } || { PART(=-2) | o } || { PART(=-2) | o }
44. { MOVE GOOD | o } || { MOVE GOOD | o } || { MOVE GOOD | o }
45. { PART(=-4) | a } || { PART(=-4) | a } || { PART(=-4) | a }
46. { MOVE(=-5) | o } || { MOVE(=-5) | o } || { MOVE(=-5) | o }
47. { MOVE(=+5) | o } || { MOVE(=+5) | o } || { MOVE(=+5) | o }
48. { PART(=+3) MOVE | o } || { PART(=+3) MOVE | o } || { PART(=+3) MOVE | o }
49. { DO GOOD(=-5) | i } || { DO GOOD(=-5) | i V+4 } || { RULE(=+5) DO | i }
50. { RULE SOMEONE | o } || { RULE SOMEONE | o } || { RULE SOMEONE | o }
51. { RULE | a } || { RULE | a } || { RULE | a }
52. { DO KNOW(=-5) | i } || { DO KNOW(=-5) | i } || { DO KNOW(=-5) | i }
53. { MOVE(=+5) DO | o } || { MOVE(=+5) DO | o } || { MOVE(=+5) DO | o }
54. { MOVE | o tool } || { MOVE | o tool } FOR { RULE(=-5) | o } || { MOVE | o tool } FOR { RULE(=-5) | o }
55. { PART(=+5) DO | o result } || { PART(=+5) DO | o result } || { PART(=+5) DO | o result }
56. { RULE(=+4) PART | o } || { RULE(=+4) PART | o } || { RULE(=+4) PART | o }
57. { PART(=+2) | o } || { PART(=-2) | o } PI { PART(=+2) | o } || { PART(=-2) | o } PI { PART(=+2) | o }
58. { PART(=+2) DO | i } || { RULE(=+4) DO | i } || { RULE(=+4) DO | i }
59. { RULE(=+4) | o quality } || { RULE(=+4) | o quality } || { RULE(=+4) | o quality }
60. { KNOW(=-3) | i } || { KNOW(=-3) | i } || { KNOW(=-3) | i }
