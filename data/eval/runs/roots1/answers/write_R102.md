1. { SAY KNOW | o result } || { SAY | o result } FOR { KNOW(=+5) | o } || { SAY | o result } FOR { KNOW(=+5) | o } FROM { THINK(=+5) | o result }
2. { GOOD(=-5) | o quality I+4 } || { GOOD(=-5) | o quality I+4 } LIKE { MOVE(=+5) | o } || { GOOD(=-5) | o quality I+4 } LIKE { MOVE(=+5) | o } FOR { THINK(=+5) | i }
3. { DO RULE | i A-5 } || { DO | i A-5 } FOR { RULE(=+4) | o } || { DO | i A-5 } FOR { PART(=+5) | o } FOR { RULE(=+4) | o }
4. { DO DO | o agent } || { DO | o agent } FOR { DO | o tool } || { DO | o agent } FOR { DO | o tool } FOR { MOVE | o }
5. { MOVE PART(=-5) | o } || { PART(=-5) | o } FROM { DO MOVE(=+5) | i } || { PART(=-5) | o } FROM { DO MOVE(=+5) | i } LIKE { SAY(=-5) | o }
6. { THINK KNOW | o result } || { THINK(=-5) | o result } FOR { THINK(=+5) | i } || { THINK(=-5) | o result } FOR { THINK(=+5) | i } FROM { PART(=+5) SOMEONE | o }
7. { DO PART | o result } || { PART | o result } FOR { DO | i } || { PART(=+5) | o result } FOR { DO | i } FOR { THINK(=+5) | o result }
8. { THINK PART(=+5) | o result } || { THINK | o result } FROM { PART(=-5) KNOW | o } || { THINK(=+5) | i } FROM { PART(=-5) KNOW | o } FOR { PART(=+5) KNOW | o }
9. { GOOD(=+4) | a } || { GOOD(=+5) | a } FOR { KNOW | o agent } || { GOOD(=+5) | a I+4 } FOR { KNOW | o agent } FOR { THINK(=+5) | i }
10. { GOOD(=+5) | o quality } || { PART | o } FROM { GOOD(=+5) | o quality } || { PART | o } FROM { GOOD(=+5) | o quality } PI { KNOW(=+5) PART(=+5) | o }
11. { KNOW(=+5) DO | i } || { DO | i } FOR { KNOW(=+5) | o } || { DO | i } FOR { KNOW(=+5) | o } FROM { SAY | o result }
12. { SAY(=+5) | i } || { SAY(=+5) | i A-5 } || { SAY(=+5) | i A-5 } LIKE { SAY(=+3) | o }
13. { SAY THINK | o result } || { SAY | o result } FROM { THINK | o } || { SAY | o result } FROM { THINK | o } LIKE { KNOW(=-3) | o }
14. { MOVE(=-5) | i } || { MOVE(=-5) | i } PI { MOVE(=-3) | a } || { MOVE(=-5) | i V-4 } FROM { GOOD(=-3) | a } PI { PART | o }
15. { DO MOVE(=+3) | o } || { MOVE | o } LIKE { DO(=+5) | o } || { MOVE | o } LIKE { DO | i } FOR { MOVE(=-5) | i }
16. { SAY KNOW | o result } || { KNOW | o } FOR { SOMEONE | o tool } || { KNOW | o } FOR { SOMEONE | o tool } FROM { GOOD | a }
17. { SAY KNOW | o tool } || { SAY | o tool } FOR { KNOW | o } || { SAY | o tool } FOR { KNOW | o } FROM { RULE | o result }
18. { RULE GIVE | o agent } || { RULE(=+4) | o agent } FOR { GIVE | o } || { RULE(=+4) | o agent } FOR { GIVE | o } FOR { DO | o }
19. { MOVE PART(=-2) | o } || { PART(=-2) | o } FOR { MOVE | i } || { PART(=-2) | o } FOR { MOVE | i } PI { SOMEONE | o }
20. { GIVE(=0) | o } || { GIVE | i N+3 } || { GIVE | o } FOR { GIVE(=0) | i } FROM { DO | o result }
21. { GIVE(=0) | o tool } || { GIVE | o tool } FOR { GIVE(=0) | i } || { GIVE | o tool } FOR { GIVE(=0) | i } FROM { RULE(=+4) | o }
22. { RULE PART(=+2) | o } || { PART(=+2) | o } FOR { RULE | i } || { PART(=+2) | o } FOR { RULE | i } FOR { DO | i }
23. { SOMEONE PART(=+5) | o } || { PART(=+5) | o } FROM { SOMEONE | o N+3 } || { PART(=+5) | o } FROM { SOMEONE | o N+3 } FOR { THINK | o }
24. { MOVE(=-5) | i } || { MOVE(=-5) | i A+5 } || { MOVE(=-5) | i A+5 } LIKE { GOOD | a }
25. { GIVE DO | i } || { DO | i } FOR { GOOD | o } || { GIVE(=+5) | i } FOR { DO | i } FOR { SOMEONE | o }
26. { SAY PART | o } || { SAY | o result } PI { SAY | o result } || { SAY | o result } PI { SAY | o result } FOR { KNOW | o }
27. { DO | i } FROM { PART(=-5) | o } || { DO | i } FROM { PART(=-5) | o N+3 } || { DO | i } FROM { PART(=-5) | o N+3 } LIKE { GOOD | a }
28. { MOVE DO | i } || { DO | i } AGAINST { SOMEONE | o } || { DO | i } AGAINST { SOMEONE | o } LIKE { MOVE(=+3) | i }
29. { DO RULE | i } || { DO | i } FOR { RULE | o } || { DO | i } FOR { RULE(=+4) | o } FOR { SAY | o result }
30. { THINK DO | a } || { DO | a } FOR { DO | i } || { THINK | a } FOR { DO | i } LIKE { GOOD | a }
31. { KNOW THINK | i } || { KNOW | i } FOR { SAY | o result } || { KNOW | i } FOR { SAY | o result } FROM { THINK | i }
32. { DO PART | o } || { DO | o result } FOR { PART | o } || { DO | o result } FOR { PART | o N+3 } FOR { THINK(=+5) | o }
33. { GOOD DO | i } || { DO | i } FOR { GOOD(=+3) | a } || { GOOD(=+3) | i } FOR { GIVE | i }
34. { DO | a } FOR { DO | o } || { DO | a } FOR { DO | o } FROM { SOMEONE | o N+3 } || { DO | a } FOR { DO | o } FROM { SOMEONE | o N+3 } FOR { GIVE | i }
35. { SAY(=-5) | i } || { SAY(=-5) | i } LIKE { MOVE(=-3) | a } || { SAY(=-5) | i } LIKE { MOVE(=-3) | a } PI { SAY | o }
36. { MOVE GIVE(=-5) | i } || { GIVE(=-5) | i } LIKE { MOVE | i } || { GIVE(=-5) | i } LIKE { MOVE | i } FROM { PART | o }
37. { RULE KNOW | a } || { KNOW(=+5) | o agent } FOR { SOMEONE | o N+3 } || { KNOW(=+5) | o agent } FOR { SOMEONE | o N+3 } PI { PART(=+5) | o }
38. { KNOW PART(=+5) | o } || { KNOW | o result } PI { PART(=+5) | o } || { KNOW | o result } N+3 FOR { THINK | i } FROM { PART(=+5) | o }
39. { GIVE(=-5) DO | o agent } || { GIVE(=-5) | o agent } FROM { MOVE | o } || { GIVE(=-5) | o agent } FOR { DO | i } FROM { MOVE | o }
40. { MOVE DO | i } || { DO | i } FOR { MOVE | o } || { DO | i } FOR { MOVE | o } LIKE { GOOD | a }
41. { KNOW MOVE | a } || { KNOW | a } FOR { DO | i } || { KNOW | a I+4 } FOR { DO | i } FROM { MOVE | o }
42. { MOVE PART | i } || { PART | i } FOR { MOVE(=-5) | i } || { PART | i } FOR { MOVE(=-5) | i } AGAINST { SOMEONE | o }
43. { SOMEONE GOOD | o } || { SOMEONE | o } LIKE { GOOD | a } || { SOMEONE | o D+3 } LIKE { GOOD | a } PI { PART(=-2) | o }
44. { GOOD(=+5) KNOW | a } || { GOOD(=+5) | a I+4 } || { GOOD(=+5) | a I+4 } FOR { THINK(=+5) | i }
45. { RULE(=+5) | a } || { RULE(=+5) | a } AGAINST { RULE(=+4) | o } || { RULE(=+5) | a } AGAINST { RULE(=+4) | o } LIKE { SOMEONE(=+5) | a }
46. { GIVE PART | i } || { GIVE | i } FOR { PART | o } || { GIVE(=+5) | i } FOR { PART | o } LIKE { GOOD | a }
47. { MOVE DO | o } || { DO | o } LIKE { MOVE(=+3) | o } || { DO | o } LIKE { MOVE(=+3) | o } PI { DO | i }
48. { PART(=+2) | o } || { PART(=+2) | o } PI { DO | o } || { PART(=+2) | o } PI { DO | o } FOR { MOVE | i }
49. { DO | o tool } || { DO | o tool } FOR { DO | i } || { DO | o tool } FOR { DO | i } FROM { PART | o }
50. { DO SAY | o result N+1 } || { SAY | o result } FOR { SOMEONE | o N+1 } || { SAY | o result } FOR { SOMEONE | o N+1 } PI { DO | i }
51. { KNOW(=+5) DO | i } || { DO | i } FOR { KNOW(=+5) | o } || { DO | i } FOR { KNOW(=+5) | o } FOR { SOMEONE | o N+3 }
52. { DO GOOD | i } || { DO | i } FOR { DO | o } || { DO | i } FOR { DO | o } FOR { GOOD | a }
53. { DO | i } AGAINST { MOVE | o } || { DO | i } AGAINST { MOVE | o } || { DO | i K+5 } AGAINST { MOVE | o } LIKE { RULE(=-5) | a }
54. { SAY KNOW | i } || { SAY | i } FOR { KNOW | o quality } || { SAY | i } FOR { KNOW | o quality } PI { SOMEONE | o }
55. { THINK PART | o } || { SAY | o result } FOR { PART | o } || { SAY | o result } FOR { PART(=+2) | o } LIKE { THINK | o result }
56. { MOVE GIVE | i } || { DO | i } AGAINST { DO | i } || { DO | i } AGAINST { DO | i } LIKE { MOVE | i }
57. { GIVE PART | o } || { PART | o } FOR { GIVE | o } || { PART | o } FOR { GIVE | o } PI { GIVE | o }
58. { GIVE PART | a } || { PART | a } LIKE { GIVE | i } || { PART | a } LIKE { GIVE | i } FOR { DO | i }
59. { RULE(=-5) | a } || { SOMEONE | a } AGAINST { RULE(=+4) | o } || { SOMEONE | a } AGAINST { RULE(=+4) | o } LIKE { SOMEONE(=+5) | a }
60. { THINK RULE | i } || { THINK(=+5) | i } FOR { RULE | o } || { THINK(=+5) | i } FOR { RULE | o } FOR { SOMEONE | o N+3 }
