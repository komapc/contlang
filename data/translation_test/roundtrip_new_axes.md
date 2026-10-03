# Проверка: новые оси (TOUCH, MATTER) и 3 против 2 корней (слепой тест, 100 новых слов)

Выборка: 100 случайных слов (seed 17), словарь из 34 корней (TOUCH: мягкое … твёрдое; MATTER: твёрдое … жидкое … газ). Вариант X — до 3 корней, вариант Y — до 2 корней (перекодированы 82 слова; у 18 код один). Декодировали четыре слепых субагента; оценки ставил ассистент.

**Итог:** вариант X: слово или синоним 26 из 100 (точно 9, синоним 17, рядом 33, мимо 41). Попарно на 82 словах: X 17 против Y 16 (X лучше в 20, Y лучше в 17, одинаково в 45). Два корня дают столько же, сколько три.

MATTER: *substance, sea, dirt* — синоним (3 из 6 слов с осью), *saline* рядом, *cigarette, weep* мимо. TOUCH(=∓): *strictly, column, scratch* — мимо.

| № | слово | X (≤3) | X прочитано | оценка X | Y (≤2) | Y прочитано | оценка Y |
| --: | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | revise | `DO-i E SAY-o GOOD(=+3)` | praise | мимо | `HAPPEN-i GOOD(=+3)` | improve | рядом |
| 2 | endure | `LIVE-i TIME(=+3) GOOD(=-2)` | mediocre | мимо | `FEEL-i GOOD(=-3)` | suffer | рядом |
| 3 | powerful | `CAN-a(=+5) BIG(=+3)` | powerful | точно | `CAN-a(=+5)` | able | рядом |
| 4 | formal | `DO-a SAME(=+4) GOOD(=+2)` | behave | мимо | `DO-a SAME(=+4)` | similar | мимо |
| 5 | scientific | `KNOW-a THINK-a MAYBE(=+4)` | certain | мимо | `KNOW-a MAYBE(=+4)` | certain | мимо |
| 6 | hurry | `MOVE-i BIG(=+4) WANT(=+3)` | rush | синоним | `MOVE-i BIG(=+4)` | rush | синоним |
| 7 | strictly | `DO-e SAME(=+5) CAN(=-3)` | awkwardly | мимо | `DO-e TOUCH(=+4)` | hit | мимо |
| 8 | brilliant | `THINK-a GOOD(=+5) SEE-a` | beautiful | мимо | `THINK-a GOOD(=+5)` | smart | синоним |
| 9 | touch | `TOUCH-i` | touch | точно | — | — | — |
| 10 | produce | `DO-i E THING-o BEGIN(=-4)` | start | рядом | `DO-i E THING-o` | make | синоним |
| 11 | cool | `HEAT-a(=-2) GOOD(=+2)` | cool | точно | `HEAT-a(=-2)` | cool | точно |
| 12 | unknown | `KNOW-a(=-5)` | ignorant | рядом | — | — | — |
| 13 | equally | `SAME-e(=+5) GOOD(=0)` | okay | мимо | `SAME-e(=+4)` | exactly | рядом |
| 14 | gesture | `MOVE-o BODY-o SAY-i` | dance | рядом | `MOVE-o SAY-i` | gesture | точно |
| 15 | notify | `SAY-i E KNOW-o` | teach | рядом | `SAY-i KNOW-o` | tell | синоним |
| 16 | govern | `DO-i E SOMEONE-o MANY(=+5)` | enslave | рядом | `DO-i E SOMEONE-o` | help | мимо |
| 17 | absolute | `SAME-a(=+5) MANY(=+5)` | all | рядом | `MANY-a(=+5)` | all | рядом |
| 18 | demonstrate | `DO-i E SEE-o KNOW-o` | investigate | мимо | `DO-i SEE-o` | show | синоним |
| 19 | despise | `FEEL-i WANT(=-5) GOOD(=-3)` | dislike | рядом | `WANT-i(=-5)` | refuse | мимо |
| 20 | catch | `TOUCH-i E THING-o MOVE-a` | push | мимо | `TOUCH-i MOVE-a` | handle | мимо |
| 21 | check | `SEE-i E KNOW-o MAYBE(=+3)` | guess | мимо | `SEE-i KNOW-o` | witness | мимо |
| 22 | county | `PLACE-o BIG(=+3) SOMEONE-o` | city | рядом | `PLACE-o SOMEONE-o` | home | мимо |
| 23 | assign | `DO-i E SOMEONE-o DO-o` | command | рядом | `GIVE-i DO-o` | donate | мимо |
| 24 | decisive | `THINK-a(=+5) BIG(=+3)` | genius | мимо | `THINK-a(=+5)` | decide | рядом |
| 25 | mid | `PART-a SIDE(=0)` | neutral | рядом | `SIDE-a(=0)` | neutral | рядом |
| 26 | technical | `DO-a KNOW-o THING-o` | skill | рядом | `DO-a KNOW-o` | skill | рядом |
| 27 | substance | `THING-o MATTER-o` | material | синоним | — | — | — |
| 28 | solely | `MANY-e(=+1) SAME(=+4)` | similar | мимо | `MANY-e(=+1)` | few | мимо |
| 29 | mile | `PLACE-o BIG(=+4) MOVE-i` | road | рядом | `PLACE-o BIG(=+4)` | city | мимо |
| 30 | full | `CONTAINER-a INSIDE(=+5)` | full | точно | `INSIDE-a(=+5)` | inner | мимо |
| 31 | bedroom | `PLACE-o LIVE-i(=-2)` | cemetery | мимо | — | — | — |
| 32 | nucleus | `PART-o INSIDE(=+5) THING-o` | core | синоним | `PART-o INSIDE(=+5)` | core | синоним |
| 33 | data | `KNOW-o THING-o MANY(=+3)` | knowledge | рядом | `KNOW-o MANY(=+3)` | knowledge | рядом |
| 34 | fictional | `THINK-a SEE-o MAYBE(=-5)` | imaginary | синоним | `THINK-a MAYBE(=-5)` | doubtful | мимо |
| 35 | literal | `SAY-a SAME(=+5)` | consistent | мимо | — | — | — |
| 36 | finely | `DO-e GOOD(=+3) BIG(=-4)` | gently | рядом | `DO-e BIG(=-4)` | shrink | мимо |
| 37 | column | `THING-o ABOVE(=+4) TOUCH(=+4)` | top | мимо | `THING-o ABOVE(=+4)` | top | мимо |
| 38 | inning | `TIME-o DO-o PART-o` | job | мимо | `TIME-o DO-o` | moment | рядом |
| 39 | educational | `KNOW-a DO-i E SOMEONE-o` | teach | рядом | `KNOW-a SAY-i` | admit | мимо |
| 40 | category | `PART-o THING-o SAME(=+3)` | copy | мимо | `PART-o SAME(=+3)` | half | мимо |
| 41 | happen | `HAPPEN-i` | happen | точно | — | — | — |
| 42 | raw | `CONSUME-a HEAT(=+4) MAYBE(=-5)` | cold | мимо | `CONSUME-a HEAT(=-1)` | drink | мимо |
| 43 | instruction | `SAY-o DO-o KNOW-o` | language | мимо | `SAY-o DO-o` | speech | мимо |
| 44 | gouge | `DO-i E THING-o INSIDE(=+4)` | insert | рядом | `DO-i INSIDE(=+4)` | enter | мимо |
| 45 | war | `DO-o MANY(=+5) LIVE(=-5)` | massacre | рядом | `DO-o LIVE(=-5)` | corpse | мимо |
| 46 | safety | `HAPPEN-o GOOD(=-4) MAYBE(=-5)` | disaster | мимо | `GOOD-o MAYBE(=+4)` | certainly | мимо |
| 47 | month | `TIME-o BIG(=+4) MANY(=+1)` | era | рядом | `TIME-o BIG(=+3)` | era | рядом |
| 48 | bore | `DO-i FEEL-o GOOD(=-2)` | pain | мимо | `FEEL-i GOOD(=-2)` | dislike | рядом |
| 49 | scratch | `TOUCH-i E BODY-o TOUCH(=+4)` | hit | мимо | `TOUCH-i TOUCH(=+4)` | hit | мимо |
| 50 | unexpectedly | `HAPPEN-e KNOW(=-4)` | suddenly | синоним | — | — | — |
| 51 | try | `DO-i MAYBE(=-2) WANT(=+3)` | hope | мимо | `DO-i MAYBE(=-2)` | try | точно |
| 52 | cigarette | `THING-o CONSUME-i MATTER(=+5)` | drink | мимо | `CONSUME-o MATTER(=+5)` | water | мимо |
| 53 | tear | `DO-i E THING-o PART(=-4)` | break | рядом | `DO-i PART(=-4)` | break | рядом |
| 54 | instead | `SAME-e(=-4) GIVE(=0)` | exchange | мимо | `SAME-e(=-4)` | differently | мимо |
| 55 | distinctive | `SAME-a(=-4) GOOD(=+2)` | different | рядом | `SAME-a(=-4)` | different | рядом |
| 56 | probability | `MAYBE-o KNOW-o` | secret | мимо | `MAYBE-o` | possibility | рядом |
| 57 | nevertheless | `HAPPEN-e(=+4) SAME(=-3)` | unexpectedly | мимо | `SAME-e(=-3)` | almost | мимо |
| 58 | consume | `CONSUME-i` | eat | синоним | — | — | — |
| 59 | plead | `SAY-i WANT(=+5) FEEL-o` | complain | мимо | `SAY-i WANT(=+5)` | ask | рядом |
| 60 | shoot | `MOVE-i E THING-o LIVE(=-5)` | kill | рядом | `MOVE-i E THING-o` | carry | мимо |
| 61 | dirt | `MATTER-o(=-3) GOOD(=-2)` | mud | синоним | `MATTER-o(=-3)` | liquid | мимо |
| 62 | plan | `THINK-i TIME(=+3) DO-o` | plan | точно | `THINK-i TIME(=+3)` | plan | точно |
| 63 | advise | `SAY-i GOOD(=+3) E SOMEONE-o` | praise | мимо | `SAY-i GOOD(=+3)` | praise | мимо |
| 64 | devote | `GIVE-i(=+4) TIME-o` | lend | мимо | — | — | — |
| 65 | politely | `DO-e GOOD(=+3) SOMEONE-o` | kindly | синоним | `DO-e GOOD(=+3)` | well | рядом |
| 66 | veer | `MOVE-i SIDE(=+3) HAPPEN-e` | advance | мимо | `MOVE-i SIDE(=+3)` | advance | мимо |
| 67 | dumb | `THINK-a GOOD(=-4)` | bad | рядом | — | — | — |
| 68 | profess | `SAY-i KNOW(=+4) E THING-o` | explain | рядом | `SAY-i KNOW(=+4)` | promise | мимо |
| 69 | roll | `MOVE-i TOUCH-a MANY(=+3)` | throw | мимо | `MOVE-i SAME(=+5)` | follow | мимо |
| 70 | saline | `MATTER-o(=0) BODY-o GOOD(=+2)` | blood | рядом | `MATTER-o(=0)` | water | рядом |
| 71 | negro | `SOMEONE-o PI "Africa"` | african | рядом | — | — | — |
| 72 | stimulate | `DO-i E SOMEONE-o LIVE(=+3)` | revive | рядом | `DO-i LIVE(=+3)` | revive | рядом |
| 73 | sympathetic | `FEEL-a SAME(=+4) SOMEONE-o` | sympathize | синоним | `FEEL-a SAME(=+4)` | similar | мимо |
| 74 | sea | `MATTER-o(=0) PLACE-o BIG(=+5)` | ocean | синоним | `MATTER-o(=0) BIG(=+5)` | ocean | синоним |
| 75 | compel | `DO-i E SOMEONE-o WANT(=-4)` | refuse | мимо | `DO-i WANT(=-4)` | refuse | мимо |
| 76 | together | `SAME-e(=+4) NEAR(=+4)` | together | точно | `NEAR-e(=+5)` | nearby | мимо |
| 77 | adjacent | `NEAR-a(=+5) SIDE(=0)` | beside | синоним | `NEAR-a(=+5)` | near | рядом |
| 78 | lately | `TIME-e(=-1)` | recently | синоним | — | — | — |
| 79 | motion | `MOVE-o` | movement | синоним | — | — | — |
| 80 | expert | `SOMEONE-o KNOW-o BIG(=+5)` | genius | рядом | `SOMEONE-o KNOW(=+5)` | expert | точно |
| 81 | little | `BIG-a(=-3)` | small | синоним | — | — | — |
| 82 | week | `TIME-o BIG(=+2) MANY(=+2)` | century | мимо | `TIME-o BIG(=+2)` | era | мимо |
| 83 | weep | `FEEL-i GOOD(=-4) MATTER-o(=0)` | vomit | мимо | `FEEL-i GOOD(=-4)` | suffer | рядом |
| 84 | indicate | `SAY-i E SEE-o` | show | синоним | `SAY-i SEE-o` | show | синоним |
| 85 | repel | `DO-i E THING-o NEAR(=-5)` | remove | рядом | `DO-i NEAR(=-5)` | avoid | рядом |
| 86 | calm | `FEEL-a MOVE-a MAYBE(=-4)` | nervous | мимо | `FEEL-a GOOD(=+2)` | nice | мимо |
| 87 | low | `ABOVE-a(=-4)` | low | точно | — | — | — |
| 88 | hire | `GIVE-i(=+3) DO-o SOMEONE-o` | donate | мимо | `GIVE-i(=+3) DO-o` | donate | мимо |
| 89 | cite | `SAY-i E SAY-o SOMEONE-o` | tell | рядом | `SAY-i E SAY-o` | repeat | рядом |
| 90 | chicken | `LIVE-o CONSUME-o` | food | рядом | — | — | — |
| 91 | human | `SOMEONE-a LIVE-a` | alive | мимо | `SOMEONE-a` | personal | мимо |
| 92 | immediate | `TIME-a(=+1) BIG(=-5)` | immediate | точно | `TIME-a(=+1)` | recent | рядом |
| 93 | require | `WANT-i(=+5) E DO-o` | volunteer | мимо | `WANT-i(=+5)` | love | мимо |
| 94 | inevitably | `HAPPEN-e CAN(=-5)` | impossibly | мимо | — | — | — |
| 95 | abolish | `DO-i E THING-o BEGIN(=+5)` | finish | мимо | `DO-i BEGIN(=+5)` | finish | мимо |
| 96 | clearly | `SEE-e KNOW(=+4)` | surely | рядом | — | — | — |
| 97 | double | `DO-i E THING-o MANY(=+2)` | repeat | рядом | `DO-i MANY(=+2)` | multiply | синоним |
| 98 | heartily | `FEEL-e GOOD(=+4) BIG(=+4)` | happily | синоним | `FEEL-e GOOD(=+4)` | happily | синоним |
| 99 | oath | `SAY-o MAYBE(=+4) DO-o` | promise | рядом | `SAY-o MAYBE(=+4)` | promise | рядом |
| 100 | train | `DO-i E SOMEONE-o KNOW-o` | teach | синоним | `DO-i KNOW-o` | teach | синоним |
