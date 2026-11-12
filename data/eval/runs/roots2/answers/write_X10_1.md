1. { PART(=+5) | a I+4 }
2. { MOVE(=+5) DO | i I+5 }
3. { MOVE DO(=+3) | o agent }
4. { THINK GOOD(=-5) | i I+5 }
5. { KNOW(=+5) DO(=+3) | o quality }
6. { KNOW(=+5) DO GOOD | o agent }
7. { GIVE(=-2) | i }
8. { GOOD | a C+3 }
9. { RULE(=+5) THINK(=+5) | o } FOR { SOMEONE | o N+5 }
10. { KNOW PART(=+5) | o result }
11. { GIVE(=+2) KNOW | i }
12. { SAY PART(=+5) | o result T-2 }
13. { SAY(=+5) KNOW | o quality }
14. { DO PART(=-2) | o } PI { PART(=+5) SOMEONE | o }
15. { PART(=-2) | o } PI { SOMEONE | o }
16. { SAY(=-5) PART(=+5) | o result }
17. { KNOW(=+5) GOOD | i K+5 }
18. { PART(=-5) | o } FOR { DO(=+3) GOOD | o }
19. { GIVE(=+5) MOVE | o }
20. { PART(=+5) | a I+2 }
21. { DO | o result }
22. { PART(=-5) MOVE(=+5) | o }
23. { PART(=+2) PART(=+2) | o }
24. { DO(=+3) GOOD(=-3) | a }
25. { RULE(=+3) DO(=+3) | o }
26. { PART(=-2) DO | i }
27. { DO GOOD(=-3) | a I+3 }
28. { DO | a } AGAINST { DO(=+5) PART(=-2) | o I+4 }
29. { PART(=-2) | o } FOR { DO(=+3) | i }
30. { SAY KNOW RULE(=+3) | o agent }
31. { KNOW(=+5) KNOW(=-5) | i }
32. { PART(=0) | o }
33. { PART(=+5) MOVE(=+5) | a }
34. { THINK | a }
35. { GOOD(=+5) KNOW | o quality }
36. { PART(=+5) PART(=-2) | o }
37. { PART(=0) GOOD(=+2) | a }
38. { GIVE(=+5) | a }
39. { PART(=+5) | o }
40. { SAY(=+3) GOOD(=-3) | i }
41. { MOVE DO | i }
42. { MOVE | o } PI { PART(=-2) | o }
43. { PART(=-5) | o }
44. { MOVE GOOD | o }
45. { PART(=-5) | a }
46. { PART(=0) MOVE(=-5) | o }
47. { DO | o tool }
48. { DO PART(=+5) | o }
49. { RULE(=+5) DO | i K+5 }
50. { RULE(=+3) PART | o }
51. { RULE(=+3) | a }
52. { KNOW(=-5) DO | i }
53. { DO(=+5) | o }
54. { GIVE MOVE | o tool }
55. { DO(=+3) PART(=+5) | o result }
56. { RULE(=+3) | o } PI { RULE(=+5) | o }
57. { PART | o } PI { PART(=-2) | o }
58. { RULE(=+3) PART(=+5) | i }
59. { RULE(=+3) DO | o quality }
60. { KNOW(=-5) | i K+5 }
