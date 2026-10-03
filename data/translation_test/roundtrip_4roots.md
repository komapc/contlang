# Проверка: 3 или 4 корня в слове (слепой тест, 100 новых слов)

Выборка: 100 случайных слов (seed 13). Каждое слово закодировано в пределах 3 корней (A) и, где можно осмысленно уточнить, с 4-м корнем (B, 78 слов; у остальных 22 один код). Декодировали четыре слепых субагента, не зная пары. Оценки ставил ассистент.

**Итог по парам (78 слов):** B лучше в 18, A лучше в 18, одинаково в 42. Слово или синоним: A 34 из 100 (24 из 78 слов с парой), с четвёртым корнем 22 из 78. Четвёртый корень выигрыша не даёт: он чаще смещает смысл (*rescue* → *kill*, *betray* → *hit*, *detective* → *enemy*), чем уточняет. Константа остаётся 3.

| № | слово | A (≤3) | A прочитано | B (≤4) | B прочитано | лучше |
| --: | :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | primarily | `BEGIN-e(=-4) BIG(=+3)` | first | — | — | — |
| 2 | unable | `CAN-a(=-5)` | impossible | — | — | — |
| 3 | operator | `SOMEONE-o DO-i THING-o` | someone does a thing | `SOMEONE-o DO-i THING-o MOVE-a` | driver | = |
| 4 | retire | `DO-i BEGIN(=+5) DO-o` | finish | `DO-i BEGIN(=+5) DO-o BIG(=+3)` | start | = |
| 5 | press | `TOUCH-i BIG(=+3)` | hug | `DO-i E THING-o TOUCH-i BIG(=+3)` | hit | B |
| 6 | quick | `MOVE-a BIG(=+3)` | run | — | — | — |
| 7 | aid | `DO-i E SOMEONE-o GOOD(=+3)` | help | `DO-i E SOMEONE-o GOOD(=+3) WANT(=+3)` | please | A |
| 8 | analysis | `THINK-o KNOW-o PART-o` | education | `THINK-o KNOW-o PART-o MANY(=+4)` | wisdom | = |
| 9 | mass | `THING-o BIG(=+4) TOUCH-a` | rock | `THING-o MANY(=+4) BIG(=+4) TOUCH-a` | crowd | B |
| 10 | violent | `DO-a GOOD(=-4) BIG(=+4)` | disaster | `DO-a TOUCH-a GOOD(=-4) BIG(=+4)` | rough | B |
| 11 | busy | `DO-a BIG(=+4)` | powerful | — | — | — |
| 12 | cook | `DO-i E CONSUME-o HEAT(=+4)` | cook | `DO-i E THING-o CONSUME-o HEAT(=+4)` | cook | = |
| 13 | offer | `SAY-i GIVE(=+3)` | offer | `SAY-i GIVE(=+3) WANT(=+3)` | ask | A |
| 14 | recover | `HAPPEN-i GOOD(=+3) LIVE(=+3)` | recover | `HAPPEN-i GOOD(=+3) LIVE(=+3) SAME(=+3)` | heal | A |
| 15 | season | `TIME-o HEAT-a` | summer | `TIME-o BIG(=+3) HEAT-a SAME(=+3)` | summer | = |
| 16 | least | `BIG-a(=-5)` | tiny | — | — | — |
| 17 | receive | `GIVE-i(=-4)` | steal | `GIVE-i(=-4) E THING-o` | take | B |
| 18 | resist | `DO-i WANT(=-4) E SOMEONE-o` | annoy | `DO-i WANT(=-4) E SOMEONE-o CAN(=+3)` | force | = |
| 19 | energy | `CAN-o BIG(=+4) HEAT` | fire | `CAN-o DO-i BIG(=+4) HEAT(=+3)` | oven | = |
| 20 | base | `THING-o ABOVE(=-5)` | floor | `THING-o ABOVE(=-5) BEGIN(=-4)` | root | = |
| 21 | duty | `DO-o GOOD(=+3)` | benefit | `DO-o GOOD(=+3) WANT(=-2) SOMEONE-o` | servant | = |
| 22 | worthy | `GOOD-a(=+4) WANT(=+3)` | delicious | — | — | — |
| 23 | personally | `SOMEONE-e SAME(=+5)` | alike | `SOMEONE-e SAME(=+5) NEAR(=+5)` | together | = |
| 24 | worry | `FEEL-i GOOD(=-3) MAYBE(=-3)` | worry | `FEEL-i GOOD(=-3) MAYBE(=-3) THINK-i` | worry | = |
| 25 | struggle | `DO-o SAME(=-4) BIG(=+4)` | difference | `DO-o E SOMEONE-o SAME(=-4) BIG(=+4)` | attack | B |
| 26 | reduction | `HAPPEN-o BIG(=-3)` | detail | — | — | — |
| 27 | bottle | `CONTAINER-o CONSUME-o` | cup | `CONTAINER-o CONSUME-o TOUCH-a` | cup | = |
| 28 | doubtful | `THINK-a(=-4)` | stupid | `THINK-a(=-4) MAYBE(=-3)` | doubtful | B |
| 29 | invest | `GIVE-i(=+3) THING-o TIME(=+3)` | lend | `GIVE-i(=+3) THING-o WANT(=+3) TIME(=+3)` | present | A |
| 30 | native | `BEGIN-a(=-5) PLACE-o` | end | `BEGIN-a(=-5) PLACE-o LIVE-i` | birth | B |
| 31 | tap | `TOUCH-i BIG(=-3)` | tap | — | — | — |
| 32 | bet | `DO-i MAYBE(=-3) WANT(=+4)` | hope | `DO-i MAYBE(=-3) WANT(=+4) GIVE(=+3)` | offer | A |
| 33 | tumble | `MOVE-i ABOVE(=-4)` | fall | `MOVE-i ABOVE(=-4) CAN(=-4) BODY-o` | crawl | A |
| 34 | anticipate | `THINK-i TIME(=+3)` | plan | `THINK-i TIME(=+3) WANT(=+3) HAPPEN-o` | plan | = |
| 35 | vary | `HAPPEN-i SAME(=-3)` | change | `HAPPEN-i SAME(=-3) TIME(=+3) MANY(=+3)` | change | = |
| 36 | identical | `SAME-a(=+5)` | same | — | — | — |
| 37 | hail | `SAY-i E SOMEONE-o GOOD(=+3)` | praise | `SAY-i E SOMEONE-o GOOD(=+3) NEAR(=+3)` | greet | B |
| 38 | assuredly | `MAYBE-e(=+4)` | certainly | `MAYBE-e(=+4) KNOW(=+5)` | surely | = |
| 39 | folklore | `SAY-o KNOW-o BEGIN(=-4)` | beginning | `SAY-o KNOW-o TIME(=-4) SOMEONE-o` | history | B |
| 40 | evidently | `SEE-e KNOW(=+4)` | clearly | `SEE-e KNOW(=+4) MAYBE(=+4)` | clearly | = |
| 41 | enthusiastic | `FEEL-a GOOD(=+4) WANT(=+4)` | delicious | `FEEL-a GOOD(=+4) WANT(=+4) BIG(=+3)` | excited | B |
| 42 | curiously | `WANT-e KNOW-o` | curiously | — | — | — |
| 43 | image | `SEE-o THING-o SAME(=+3)` | copy | — | — | — |
| 44 | wise | `THINK-a GOOD(=+4) KNOW(=+4)` | wise | `SOMEONE-a THINK-i GOOD(=+4) TIME(=-3)` | ancestor | A |
| 45 | freeze | `HEAT-i(=-5)` | freeze | — | — | — |
| 46 | silver | `SEE-a TOUCH-a` | soft | `SEE-a TOUCH-a HEAT(=-2) GOOD(=+2)` | soft | = |
| 47 | disappear | `SEE-i MAYBE(=-5)` | overlook | `SEE-i MAYBE(=-5) BEGIN(=+5)` | blind | = |
| 48 | arrangement | `DO-o PART-o SAME(=+3)` | member | `DO-o PART-o SAME(=+3) GOOD(=+3)` | harmony | B |
| 49 | companion | `SOMEONE-o NEAR(=+4) SAME(=+3)` | neighbor | `SOMEONE-o NEAR(=+4) SAME(=+3) MOVE-i` | neighbor | = |
| 50 | divide | `DO-i E THING-o PART(=-3)` | break | `DO-i E THING-o PART(=-3) MANY(=+2)` | share | A |
| 51 | reckon | `THINK-i MAYBE(=-1)` | probably | `THINK-i MAYBE(=-1) KNOW(=+2)` | suppose | B |
| 52 | resolution | `THINK-o(=+5)` | decision | `THINK-o(=+5) WANT-o DO-o` | decision | = |
| 53 | ability | `CAN-o(=+4)` | ability | `CAN-o(=+4) DO-o` | ability | = |
| 54 | telephone | `THING-o SAY-i NEAR(=-4)` | whisper | `THING-o SAY-i NEAR(=-4) CAN(=+3)` | whisper | = |
| 55 | operational | `DO-a CAN(=+3)` | able | `DO-a CAN(=+3) LIVE(=+3)` | healthy | A |
| 56 | description | `SAY-o SEE-o` | speech | `SAY-o SEE-o THING-o` | show | = |
| 57 | independently | `DO-e SOMEONE-o NEAR(=-3)` | nearby | `DO-e SOMEONE-o NEAR(=-3) CAN(=+4)` | neighbor | = |
| 58 | belief | `THINK-o MAYBE(=+3)` | idea | `THINK-o MAYBE(=+3) KNOW(=-2)` | suspicion | = |
| 59 | respectively | `SAME-e(=-3) MANY(=+2)` | differently | — | — | — |
| 60 | court | `PLACE-o THINK-i(=+5)` | school | `PLACE-o THINK-i(=+5) SOMEONE-o GOOD(=+3)` | school | = |
| 61 | anonymous | `SOMEONE-a SAY-o MANY(=0)` | talkative | `SOMEONE-a SAY-o MANY(=0) KNOW(=-4)` | silent | B |
| 62 | publicly | `SAY-e SOMEONE-o MANY(=+5)` | publicly | `SAY-e SOMEONE-o MANY(=+5) SEE-a` | publicly | = |
| 63 | ponder | `THINK-i BIG(=+3)` | consider | `THINK-i BIG(=+3) TIME(=+3)` | plan | A |
| 64 | doubt | `THINK-o(=-4)` | doubt | `THINK-o(=-4) MAYBE(=-3)` | doubt | = |
| 65 | silly | `THINK-a GOOD(=-3)` | stupid | — | — | — |
| 66 | error | `DO-o GOOD(=-3)` | crime | `DO-o GOOD(=-3) KNOW(=-3)` | mistake | B |
| 67 | firm | `TOUCH-a BIG(=+4)` | rough | — | — | — |
| 68 | garden | `PLACE-o LIVE-o` | garden | `PLACE-o LIVE-o DO-i GOOD(=+3)` | hospital | A |
| 69 | dictionary | `THING-o SAY-o KNOW-o` | teacher | `THING-o SAY-o KNOW-o MANY(=+4)` | encyclopedia | B |
| 70 | right | `CAN-o GOOD(=+3)` | talent | `CAN-o GOOD(=+3) SOMEONE-o` | doctor | = |
| 71 | exaggerate | `SAY-i BIG(=+4)` | shout | `SAY-i BIG(=+4) MAYBE(=-3)` | exaggerate | B |
| 72 | separately | `SAME-e(=-3) PART` | except | `SAME-e(=-3) PART-e(=-3) NEAR(=-3)` | apart | B |
| 73 | fine | `GOOD-a(=+2)` | fine | — | — | — |
| 74 | stick | `THING-o LIVE-a(=-3) BIG(=+2)` | corpse | `THING-o LIVE-a(=-3) BIG(=+2) TOUCH-a` | animal | = |
| 75 | use | `DO-i E THING-o WANT(=+3)` | order | `DO-i E THING-o WANT(=+3) CAN(=+3)` | repair | = |
| 76 | linguist | `SOMEONE-o KNOW-o SAY-o` | teacher | `SOMEONE-o KNOW-i SAY-o THING-o` | teacher | = |
| 77 | big | `BIG-a(=+4)` | huge | — | — | — |
| 78 | instant | `TIME-o BIG(=-5)` | ancient | — | — | — |
| 79 | deliver | `MOVE-i E THING-o SOMEONE-o` | carry | `MOVE-i E THING-o SOMEONE-o NEAR(=+5)` | bring | = |
| 80 | rescue | `DO-i E SOMEONE-o LIVE(=+4)` | heal | `DO-i E SOMEONE-o LIVE(=+4) GOOD(=-4)` | kill | A |
| 81 | betray | `DO-i E SOMEONE-o GOOD(=-4)` | harm | `DO-i E SOMEONE-o NEAR(=+4) GOOD(=-4)` | hit | A |
| 82 | detective | `SOMEONE-o SEE-i KNOW-o` | witness | `SOMEONE-o SEE-i KNOW-o GOOD(=-3)` | enemy | A |
| 83 | tax | `GIVE-o(=+4) THING-o` | gift | `GIVE-o(=+4) THING-o WANT(=-3) SOMEONE-o` | bribe | = |
| 84 | suspend | `DO-i E DO-o BEGIN(=+2)` | finish | `DO-i E DO-o BEGIN(=+2) TIME(=+3)` | repeat | = |
| 85 | nice | `GOOD-a(=+3)` | good | — | — | — |
| 86 | despair | `FEEL-o GOOD(=-5)` | pain | `FEEL-o GOOD(=-5) WANT(=-3)` | pain | = |
| 87 | congregation | `SOMEONE-o MANY(=+4) NEAR(=+4)` | neighbor | `SOMEONE-o MANY(=+4) NEAR(=+4) "God"` | prayer | B |
| 88 | tightly | `TOUCH-e NEAR(=+5)` | hug | `TOUCH-e NEAR(=+5) BIG(=+3)` | hug | = |
| 89 | comfortable | `FEEL-a GOOD(=+3)` | pleasant | `FEEL-a GOOD(=+3) TOUCH-a` | soft | A |
| 90 | dwell | `LIVE-i PLACE-o` | live | `LIVE-i PLACE-o TIME(=+3)` | wait | A |
| 91 | local | `PLACE-a NEAR(=+4)` | local | — | — | — |
| 92 | angrily | `FEEL-e GOOD(=-4) BIG(=+3)` | horribly | `FEEL-e GOOD(=-4) BIG(=+3) SOMEONE-o` | torment | = |
| 93 | notion | `THINK-o` | thought | `THINK-o KNOW-o BIG(=-2)` | wisdom | A |
| 94 | exploit | `DO-i E THING-o WANT(=+4)` | require | `DO-i E THING-o WANT(=+4) GOOD(=-2)` | spoil | = |
| 95 | dance | `MOVE-i BODY-o GOOD(=+3)` | dance | `MOVE-i BODY-o GOOD(=+3) FEEL-a` | dance | = |
| 96 | ultimately | `BEGIN-e(=+5)` | finally | `BEGIN-e(=+5) TIME(=+4)` | finally | = |
| 97 | hope | `WANT-i MAYBE(=-2)` | hope | `WANT-i MAYBE(=-2) GOOD(=+3)` | hope | = |
| 98 | motionless | `MOVE-a MAYBE(=-5)` | impossible | — | — | — |
| 99 | unconscious | `THINK-a(=-5) LIVE(=-2)` | dream | — | — | — |
| 100 | room | `PLACE-o INSIDE(=+4)` | room | `PLACE-o INSIDE(=+4) LIVE-i` | womb | A |
