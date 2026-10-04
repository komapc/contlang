# Метка K (побуждение, каузатив): слепой тест

16 глаголов, два независимых кодировщика (видели только спецификацию с меткой `K`), два декодера. Оценки мои.

| слово | код (A / B) | → A | → B |
| :-- | :-- | :-- | :-- |
| make | `DO \| i K+3` | make | make |
| force | `DO WANT(=-5) \| i K+5` | force | force |
| compel | `DO RULE(=+3) \| i K+4` | order (рядом) | order (рядом) |
| induce | `DO \| i K+2` | have (мимо) | get (запасным induce) |
| persuade | `SAY THINK(=+5) \| i K+3` | convince | convince |
| encourage | `WANT(=+4) \| i K+2` (A) / `K+3` (B) | entice (запасным encourage) | entice (мимо) |
| tempt | `WANT(=+4) GOOD(=-3) \| i K+2` (A) / `K+3` (B) | tempt | tempt |
| provoke | `FEEL(=+4) FIGHT \| i K+4` | provoke | enrage (запасным provoke) |
| let | `DO \| i K0` | let | let |
| allow | `RULE(=+3) \| i K0` | permit | permit |
| discourage | `DO \| i K-2` (A) / `WANT(=-3) \| i K-2` (B) | discourage | discourage |
| prevent | `DO \| i K-4` | prevent | prevent |
| forbid | `RULE(=+4) DO \| i K-5` (A) / `SAY RULE(=+3) \| i K-5` (B) | forbid | forbid |
| feed | `CONSUME \| i K+4` | feed | feed |
| teach | `KNOW \| i K+4` | teach | teach |
| frighten | `FEEL(=+4) GOOD(=-4) \| i K+4` | terrify | horrify |

Итого из 32 прочтений: верно или близким синонимом 25, запасным 3, рядом 2, мимо 2.

- Направление и сила побуждения читаются уверенно: `K+4…5` — принуждение, `K0` — разрешение, `K-2…-5` — отговорить / помешать / запретить.
- Корень действия под `K` задаёт, что именно вызывается: `CONSUME` → *feed*, `KNOW` → *teach*, `FEEL GOOD(-)` → *frighten*, `DO` → *make / prevent*.
- Слабо различаются средние степени: *induce / encourage* (`K+2…3`) читаются как *have / get / entice*.
