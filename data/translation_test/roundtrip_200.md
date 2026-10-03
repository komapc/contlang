# Туда-обратно: 200 слов (слепой тест)

Выборка: 200 случайных слов из `data/wordlist_en_x5.tsv` (seed 7). Кодировал ассистент по списку из 32 корней, декодировали четыре слепых субагента (sonnet) только по спецификации, без оригиналов. Оценки ставил ассистент.

**Итог:** точно 36 (18%), синоним 50 (25%), рядом 50 (25%), мимо 64 (32%). Слово или синоним — 43%.

| № | слово | код | обратный перевод | оценка |
| --: | :-- | :-- | :-- | :-- |
| 1 | detergent | `THING-o DO-i TOUCH-a` | touchable | мимо |
| 2 | collect | `MOVE-i E THING-o NEAR(=+5)` | bring | синоним |
| 3 | stain | `DO-i E THING-o GOOD(=-3)` | spoil | рядом |
| 4 | precipitate | `MOVE-i ABOVE(=-5)` | fall | синоним |
| 5 | down | `ABOVE-a(=-4)` | low | рядом |
| 6 | realize | `HAPPEN-i KNOW-o` | discover | синоним |
| 7 | plain | `SAME-a(=+2) BIG(=-3)` | small | мимо |
| 8 | conduct | `MOVE-i E PEOPLE-o SIDE(=+5)` | face | мимо |
| 9 | occasional | `HAPPEN-a MANY(=+1)` | rare | синоним |
| 10 | infectious | `MOVE-a LIVE-o GOOD(=-3)` | pet | мимо |
| 11 | young | `LIVE-a TIME(=-3)` | old | мимо |
| 12 | smart | `THINK-a GOOD(=+4)` | smart | точно |
| 13 | stock | `THING-o MANY(=+4) PLACE-o` | everywhere | мимо |
| 14 | woman | `SOMEONE-o SEX(=-5)` | girl | синоним |
| 15 | bear | `MOVE-i E THING-o BODY-o` | carry | синоним |
| 16 | grim | `FEEL-a GOOD(=-4)` | sad | синоним |
| 17 | normally | `TIME-e MANY(=+4)` | often | синоним |
| 18 | section | `PART-o` | part | синоним |
| 19 | jump | `MOVE-i ABOVE(=+4)` | rise | рядом |
| 20 | reflect | `THINK-i INSIDE(=+4)` | believe | рядом |
| 21 | altogether | `PART-e(=+5)` | fully | синоним |
| 22 | laboratory | `PLACE-o KNOW-o DO-i` | skill | мимо |
| 23 | history | `KNOW-o TIME(=-4)` | history | точно |
| 24 | unstructured | `SAME-a(=-5) PART-o` | opposite | мимо |
| 25 | forward | `SIDE-a(=+5)` | front | рядом |
| 26 | submit | `MOVE-i E THING-o ABOVE(=+3)` | lift | мимо |
| 27 | congratulate | `SAY-i GOOD(=+4) E SOMEONE-o` | praise | синоним |
| 28 | whistle | `DO-i HEAR-o ABOVE(=+4)` | shout | рядом |
| 29 | draw | `DO-i E SEE-o` | show | мимо |
| 30 | weary | `FEEL-a LIVE(=-2)` | sleepy | синоним |
| 31 | supreme | `ABOVE-a(=+5) BIG(=+5)` | highest | синоним |
| 32 | appoint | `THINK-i(=+5) E SOMEONE-o ABOVE(=+4)` | respect | мимо |
| 33 | early | `TIME-a(=-2)` | past | рядом |
| 34 | gas | `THING-o ABOVE(=+3)` | roof | мимо |
| 35 | later | `TIME-a(=+3)` | future | синоним |
| 36 | allot | `MOVE-i E PART-o SOMEONE-o` | share | синоним |
| 37 | property | `THING-o SOMEONE-o NEAR(=+5)` | neighbor | мимо |
| 38 | smell | `FEEL-i THING-o NEAR(=+3)` | smell | точно |
| 39 | effluent | `THING-o MOVE-a INSIDE(=-5)` | outsider | мимо |
| 40 | recommend | `SAY-i GOOD(=+4) E THING-o` | recommend | точно |
| 41 | designate | `SAY-i THINK-o(=+5) E SOMEONE-o` | decide | рядом |
| 42 | suffer | `FEEL-i GOOD(=-4)` | suffer | точно |
| 43 | steady | `SAME-a(=+4) TIME-o MANY(=+3)` | always | рядом |
| 44 | shoe | `THING-o BODY-o ABOVE(=-5)` | foot | рядом |
| 45 | presume | `THINK-i MAYBE(=-1)` | suppose | синоним |
| 46 | grand | `BIG-a(=+4) GOOD(=+4)` | great | синоним |
| 47 | college | `PLACE-o KNOW-o PEOPLE-o` | nation | мимо |
| 48 | community | `PEOPLE-o NEAR(=+4) SAME(=+3)` | neighbor | рядом |
| 49 | finite | `PART-a(=+3) BIG(=-2)` | slight | мимо |
| 50 | stupid | `THINK-a GOOD(=-4)` | stupid | точно |
| 51 | economical | `DO-a BIG(=-3) GOOD(=+3)` | masterpiece | мимо |
| 52 | near | `NEAR-a(=+4)` | near | точно |
| 53 | cheek | `PART-o BODY-o SIDE(=+3)` | face | рядом |
| 54 | member | `PART-o PEOPLE-o` | crowd | мимо |
| 55 | afterward | `TIME-e(=+2)` | soon | рядом |
| 56 | reluctantly | `DO-e WANT(=-3)` | refuse | рядом |
| 57 | buy | `DO-i E THING-o SOMEONE-o` | use | мимо |
| 58 | regardless | `SAME-e(=+4)` | exactly | мимо |
| 59 | tree | `LIVE-o ABOVE(=+4) BIG(=+3)` | bird | мимо |
| 60 | suspect | `THINK-i GOOD(=-3) MAYBE(=-3)` | suspect | точно |
| 61 | labor | `DO-o BODY-o` | action | рядом |
| 62 | deduct | `MOVE-i E PART-o INSIDE(=-5)` | extract | синоним |
| 63 | collective | `PEOPLE-a MANY(=+4)` | popular | рядом |
| 64 | elsewhere | `PLACE-e SAME(=-4)` | elsewhere | точно |
| 65 | southerner | `SOMEONE-o PI "south"` | southerner | точно |
| 66 | over | `ABOVE-a(=+3)` | upper | синоним |
| 67 | glue | `DO-i E TOUCH-o SAME(=+5)` | match | мимо |
| 68 | beg | `SAY-i WANT(=+5) E THING-o` | request | синоним |
| 69 | sin | `DO-o GOOD(=-5)` | crime | синоним |
| 70 | appreciate | `FEEL-i GOOD(=+4) KNOW-o` | intuition | мимо |
| 71 | danger | `HAPPEN-o GOOD(=-4) MAYBE(=-3)` | danger | точно |
| 72 | model | `THING-o SAME(=+3) SEE-o` | image | синоним |
| 73 | eagerly | `WANT-e(=+5)` | eagerly | точно |
| 74 | university | `PLACE-o KNOW-o BIG(=+4)` | university | точно |
| 75 | answer | `SAY-i E KNOW-o TIME(=+1)` | announce | рядом |
| 76 | nail | `DO-i E THING-o INSIDE(=+4)` | insert | рядом |
| 77 | investigate | `SEE-i E KNOW-o` | recognize | мимо |
| 78 | enlist | `MOVE-i INSIDE(=+4) PEOPLE-o` | immigrate | мимо |
| 79 | spin | `MOVE-i PLACE-o SAME(=+5)` | stay | мимо |
| 80 | integration | `DO-o PART-o SAME(=+5)` | repetition | мимо |
| 81 | westward | `MOVE-e "west"` | westward | точно |
| 82 | pitcher | `THING-o INSIDE(=+5)` | core | мимо |
| 83 | imagination | `THINK-o SEE-o MAYBE(=-3)` | opinion | рядом |
| 84 | incredible | `THINK-a CAN(=-5)` | stupid | мимо |
| 85 | earth | `PLACE-o BIG(=+5) LIVE-a` | forest | мимо |
| 86 | similar | `SAME-a(=+3)` | similar | точно |
| 87 | devise | `THINK-i DO-o` | plan | синоним |
| 88 | beat | `TOUCH-i BIG(=+4)` | hit | синоним |
| 89 | desk | `THING-o DO-o ABOVE(=+2)` | hat | мимо |
| 90 | reply | `SAY-i SAME(=+3) TIME(=+1)` | repeat | мимо |
| 91 | horizon | `PLACE-o NEAR(=-5) SEE-a` | horizon | точно |
| 92 | curiosity | `WANT-o KNOW-o` | curiosity | точно |
| 93 | well | `LIVE-a GOOD(=+3)` | healthy | синоним |
| 94 | fortunate | `HAPPEN-a GOOD(=+4)` | successful | синоним |
| 95 | forget | `KNOW-i(=-5) TIME(=-2)` | forget | точно |
| 96 | comprehend | `KNOW-i(=+5) THINK-o` | understand | синоним |
| 97 | drip | `MOVE-i ABOVE(=-4) BIG(=-4)` | sink | рядом |
| 98 | official | `SOMEONE-o ABOVE(=+3) PEOPLE-o` | leader | рядом |
| 99 | tomorrow | `TIME-o(=+2)` | future | рядом |
| 100 | physically | `BODY-e` | physically | точно |
| 101 | largely | `BIG-e(=+3)` | greatly | синоним |
| 102 | dash | `MOVE-i BIG(=+5)` | leap | рядом |
| 103 | descend | `MOVE-i ABOVE(=-4)` | fall | синоним |
| 104 | supervise | `SEE-i E DO-o ABOVE(=+3)` | look | рядом |
| 105 | numerous | `MANY-a(=+4)` | most | рядом |
| 106 | effort | `DO-o BIG(=+4)` | effort | точно |
| 107 | less | `BIG-a(=-2)` | small | рядом |
| 108 | otherwise | `SAME-e(=-4)` | differently | синоним |
| 109 | contend | `DO-i E SOMEONE-o SAME(=-4)` | oppose | синоним |
| 110 | sometime | `TIME-e MAYBE(=-3)` | perhaps | рядом |
| 111 | reappear | `SEE-i SAME(=+4) TIME(=+2)` | remember | мимо |
| 112 | drop | `MOVE-i E THING-o ABOVE(=-5)` | drop | точно |
| 113 | already | `TIME-e(=-1)` | recently | мимо |
| 114 | arbitrarily | `DO-e KNOW(=-5)` | ignorantly | мимо |
| 115 | overboard | `MOVE-e INSIDE(=-5)` | outside | рядом |
| 116 | attract | `MOVE-i E SOMEONE-o NEAR(=+5)` | approach | рядом |
| 117 | significantly | `BIG-e(=+4)` | extremely | синоним |
| 118 | erupt | `MOVE-i INSIDE(=-5) BIG(=+5)` | escape | мимо |
| 119 | eighteenth | `18-a` | eighteenth | точно |
| 120 | hypothalamus | `"hypothalamus"` | hypothalamus | точно |
| 121 | thyroid | `"thyroid"` | thyroid | точно |
| 122 | annually | `TIME-e MANY(=+3) BIG(=+4)` | often | рядом |
| 123 | article | `WORD-o MANY(=+3)` | words | мимо |
| 124 | helpless | `SOMEONE-a CAN(=-5)` | unable | синоним |
| 125 | breathe | `MOVE-i LIVE-o INSIDE(=+5)` | enter | мимо |
| 126 | state | `PLACE-o PEOPLE-o ABOVE(=+3)` | city | рядом |
| 127 | baby | `SOMEONE-o LIVE-a TIME(=-5)` | ancestor | мимо |
| 128 | distinction | `SAME-o(=-4)` | opposite | рядом |
| 129 | vocational | `DO-a KNOW-o` | useful | мимо |
| 130 | productive | `DO-a THING-o MANY(=+4)` | industrious | синоним |
| 131 | pull | `MOVE-i E THING-o NEAR(=+4)` | bring | рядом |
| 132 | scan | `SEE-i MOVE-e` | wander | мимо |
| 133 | ground | `PLACE-o ABOVE(=-4)` | basement | рядом |
| 134 | examine | `SEE-i E KNOW-o BIG(=+3)` | discover | рядом |
| 135 | food | `THING-o BODY-o INSIDE(=+4)` | organ | мимо |
| 136 | party | `PEOPLE-o HAPPEN-o GOOD(=+4)` | holiday | синоним |
| 137 | colonel | `SOMEONE-o ABOVE(=+4) PEOPLE-o` | leader | рядом |
| 138 | detect | `SEE-i KNOW(=+3)` | recognize | синоним |
| 139 | jerk | `MOVE-i HAPPEN-e BIG(=+3)` | explode | рядом |
| 140 | condition | `HAPPEN-o SAME-a` | coincidence | мимо |
| 141 | ship | `THING-o MOVE-a BIG(=+5)` | vehicle | синоним |
| 142 | proposal | `SAY-o WANT-o` | request | синоним |
| 143 | gay | `WANT-a SAME(=+5) SEX-o` | homosexual | точно |
| 144 | aesthetic | `SEE-a GOOD(=+4)` | beautiful | синоним |
| 145 | petitioner | `SOMEONE-o SAY-a WANT-o` | beggar | синоним |
| 146 | color | `SEE-o KIND-o` | type | мимо |
| 147 | celebrate | `DO-i E HAPPEN-o GOOD(=+4)` | celebrate | точно |
| 148 | eighth | `8-a` | eighth | точно |
| 149 | quote | `SAY-i SAME(=+5) WORD-o` | repeat | рядом |
| 150 | centrally | `INSIDE-e(=+4)` | inside | рядом |
| 151 | inspire | `DO-i E SOMEONE-o WANT(=+4)` | please | рядом |
| 152 | leader | `SOMEONE-o SIDE(=+5) PEOPLE-o` | leader | точно |
| 153 | intimate | `NEAR-a(=+5) INSIDE(=+4)` | intimate | точно |
| 154 | behave | `DO-i KIND-o` | classify | мимо |
| 155 | flow | `MOVE-o SAME(=+4)` | pace | мимо |
| 156 | top | `PART-o ABOVE(=+5)` | top | точно |
| 157 | stare | `SEE-i TIME-o BIG(=+4)` | gaze | синоним |
| 158 | coffee | `THING-o INSIDE(=+4) BODY-o` | organ | мимо |
| 159 | dust | `THING-o BIG(=-5) MANY(=+4)` | dust | точно |
| 160 | pair | `THING-o 2` | pair | точно |
| 161 | steer | `DO-i E MOVE-o SIDE(=+3)` | lead | синоним |
| 162 | roof | `PART-o PLACE-o ABOVE(=+5)` | ceiling | синоним |
| 163 | life | `LIVE-o` | life | точно |
| 164 | bag | `THING-o INSIDE(=+4) BIG(=-2)` | seed | мимо |
| 165 | though | `HAPPEN-e SAME(=-3)` | otherwise | мимо |
| 166 | murder | `DO-o SOMEONE-o LIVE(=-5)` | killer | рядом |
| 167 | primary | `TIME-a(=-4) BIG(=+3)` | ancient | мимо |
| 168 | capable | `CAN-a(=+4)` | possible | рядом |
| 169 | now | `TIME-a(=0)` | current | синоним |
| 170 | jew | `"Jew"` | jew | точно |
| 171 | found | `DO-i E THING-o TIME(=-1)` | finish | мимо |
| 172 | conjugate | `WORD-o SAME-a` | synonym | мимо |
| 173 | mighty | `DO-a BIG(=+4)` | active | рядом |
| 174 | invariably | `TIME-e SAME(=+5) MANY(=+5)` | always | синоним |
| 175 | sheet | `THING-o BIG(=-4)` | grain | мимо |
| 176 | regard | `SEE-i THINK-o` | imagine | рядом |
| 177 | snarl | `SAY-i GOOD(=-5) HEAR(=+2)` | curse | рядом |
| 178 | utilize | `DO-i E THING-o GOOD(=+3)` | improve | мимо |
| 179 | neutral | `GOOD-a(=0)` | average | синоним |
| 180 | clamp | `TOUCH-i BIG(=+5)` | hug | рядом |
| 181 | duly | `SAME-e(=+4) GOOD(=+2)` | equally | мимо |
| 182 | level | `PART-o ABOVE(=0)` | middle | рядом |
| 183 | residential | `PLACE-a LIVE-i` | inhabited | синоним |
| 184 | compulsive | `WANT-a(=+5) CAN(=-4)` | desperate | рядом |
| 185 | equip | `DO-i E SOMEONE-o CAN(=+4)` | enable | синоним |
| 186 | philosophy | `THINK-o KNOW-o BIG(=+4)` | wisdom | рядом |
| 187 | dominate | `ABOVE-i(=+5) E SOMEONE-o` | lift | мимо |
| 188 | famous | `KNOW-a MANY(=+4)` | learned | мимо |
| 189 | responsibility | `DO-o SOMEONE-o NEAR(=+5)` | neighbor | мимо |
| 190 | hang | `TOUCH-i ABOVE(=+4)` | reach | мимо |
| 191 | concrete | `THING-o TOUCH-a BIG(=+4)` | blanket | мимо |
| 192 | resign | `MOVE-i DO-o INSIDE(=-5)` | exit | рядом |
| 193 | seriously | `THINK-e BIG(=+4)` | deeply | синоним |
| 194 | kill | `DO-i E SOMEONE-o LIVE(=-5)` | kill | точно |
| 195 | desire | `WANT-o BIG(=+4)` | desire | точно |
| 196 | plant | `LIVE-o THING-o` | creature | мимо |
| 197 | sharp | `TOUCH-a BIG(=-5)` | soft | мимо |
| 198 | waste | `DO-i E THING-o GOOD(=-4)` | ruin | синоним |
| 199 | board | `THING-o SIDE-a BIG(=-3)` | edge | мимо |
| 200 | swing | `MOVE-i SIDE(=+3) MANY(=+3)` | march | мимо |

## Перекодирование 64 слов «мимо» (новые корни и правила)

После правок словаря (убраны HEAR, KIND, WORD; добавлены CONSUME, CONTAINER; ABOVE/INSIDE/BIG только в прямом смысле) ассистент заново закодировал 64 слова с оценкой «мимо»; два слепых декодера (sonnet) раскодировали их по обновлённой спецификации.

**Итог:** точно 3, синоним 2, рядом 15, мимо 44. Из 64 вернулось 5 (8%) слов или синонимов, ещё 15 «рядом». Общий результат на 200 словах: слово или синоним 91 (45,5%) против 86 (43%).

| слово | новый код | обратный перевод | оценка |
| :-- | :-- | :-- | :-- |
| detergent | `THING-o DO-i E TOUCH-a GOOD(=+4)` | glove \| mitten \| sock | мимо |
| plain | `SEE-a GOOD(=0)` | look \| glance \| appear | мимо |
| conduct | `DO-i E PEOPLE-o MOVE-i` | dance \| march \| parade | мимо |
| infectious | `MOVE-a FEEL-o GOOD(=-4) E PEOPLE-o` | fear \| terror \| dread | мимо |
| young | `LIVE-a(=+4) BIG(=-3)` | young \| baby \| child | точно |
| stock | `THING-o MANY(=+4) CONTAINER-o` | library \| shelf \| warehouse | мимо |
| laboratory | `PLACE-o SEE-i KNOW-o` | museum \| window \| observatory | рядом |
| unstructured | `PART-a SAME(=-5)` | different \| other \| piece | мимо |
| submit | `DO-i WANT(=-3) E SOMEONE-o` | annoy \| bother \| refuse | мимо |
| draw | `DO-i E SEE-o TOUCH-i` | massage \| caress \| examine | мимо |
| appoint | `THINK-i(=+5) E SOMEONE-o DO-o` | judge \| resolve \| decide | мимо |
| gas | `THING-o MOVE-a SEE-a MAYBE(=-4)` | ghost \| invisible \| mirage | мимо |
| property | `THING-o PI SOMEONE-o` | possession \| ownership \| belonging | синоним |
| effluent | `THING-o GOOD(=-3) MOVE-a` | clumsy \| awkward \| junk | мимо |
| college | `PLACE-o KNOW-i SOMEONE-o` | teacher \| guide \| informant | мимо |
| finite | `MANY-a(=+3) PART(=+5)` | most \| majority \| many | мимо |
| economical | `CONSUME-a BIG(=-3) GOOD(=+3)` | snack \| bite \| nibble | мимо |
| member | `SOMEONE-o PART-a PEOPLE-o` | neighbor \| citizen \| member | рядом |
| buy | `MOVE-i E THING-o SAME(=-3)` | replace \| exchange \| swap | рядом |
| regardless | `SAME-e(=+5) GOOD(=0)` | fine \| okay \| average | мимо |
| tree | `LIVE-o TOUCH-a BIG(=+3)` | elephant \| whale \| beast | мимо |
| glue | `DO-i E PART-o TOUCH-i` | repair \| fix \| handle | рядом |
| appreciate | `KNOW-i E THING-o GOOD(=+4)` | recommend \| advise \| appreciate | рядом |
| investigate | `SEE-i E HAPPEN-o(=-4)` | predict \| foresee \| witness | мимо |
| enlist | `DO-i PART-a PEOPLE-o` | participate \| join \| serve | рядом |
| spin | `MOVE-i E BODY-o SAME(=+5)` | imitate \| copy \| mirror | мимо |
| integration | `DO-o PART(=+5) NEAR(=+5)` | here \| present \| embrace | мимо |
| pitcher | `CONTAINER-o CONSUME-o` | plate \| bowl \| cup | рядом |
| incredible | `GOOD-a(=+5) THINK(=-4)` | brilliant \| genius \| wise | мимо |
| earth | `PLACE-o MANY(=+5) LIVE-o` | forest \| jungle \| zoo | мимо |
| desk | `THING-o PLACE-o THINK-i` | library \| school \| study | рядом |
| reply | `SAY-i HAPPEN-e(=+4)` | announce \| proclaim \| explain | рядом |
| reappear | `SEE-i SAME-e(=+5) MANY(=+2)` | watch \| crowd \| audience | рядом |
| already | `TIME-e(=-2)` | recently \| lately \| earlier | рядом |
| arbitrarily | `DO-e MAYBE(=-3)` | try \| attempt \| perhaps | мимо |
| erupt | `HAPPEN-i BIG(=+5) MOVE-e` | explode \| crash \| burst | синоним |
| article | `SAY-o MANY(=+3) THING-o` | language \| speech \| vocabulary | мимо |
| breathe | `CONSUME-i THING-o MOVE-a` | food \| meal \| feed | мимо |
| baby | `SOMEONE-o LIVE-a(=+3) BIG(=-5)` | baby \| infant \| child | точно |
| vocational | `KNOW-a DO-o` | skill \| expert \| professional | рядом |
| scan | `SEE-i MOVE-e MANY(=+4)` | parade \| march \| run | мимо |
| food | `THING-o CONSUME-i` | eat \| food \| meal | рядом |
| condition | `HAPPEN-o TIME(=0)` | now \| moment \| today | мимо |
| color | `SEE-o PART-o THING-o` | view \| scene \| landscape | мимо |
| behave | `DO-i SOMEONE-a GOOD(=+2)` | help \| serve \| assist | мимо |
| flow | `MOVE-o CONSUME-o` | diet \| feast \| hunger | мимо |
| coffee | `CONSUME-o THINK-i LIVE(=+3)` | cook \| restaurant \| kitchen | мимо |
| bag | `CONTAINER-o MOVE-a` | bag \| suitcase \| carry | точно |
| though | `HAPPEN-e(=+4) SAME(=-3)` | suddenly \| quickly \| unexpectedly | мимо |
| primary | `HAPPEN-a(=-4)` | unfortunate \| accidental \| unlikely | мимо |
| found | `DO-i E HAPPEN-o(=-5)` | cause \| create \| start | рядом |
| conjugate | `DO-i E SAY-o MANY(=+3)` | talk \| discuss \| converse | мимо |
| sheet | `THING-o TOUCH-a BIG(=-4)` | pebble \| button \| crumb | мимо |
| utilize | `DO-i E THING-o WANT(=+3)` | desire \| request \| ask | мимо |
| duly | `DO-e GOOD(=+3) MAYBE(=+4)` | definitely \| surely \| certainly | рядом |
| dominate | `DO-i E SOMEONE-o WANT(=-4)` | refuse \| reject \| dislike | мимо |
| famous | `SOMEONE-a PEOPLE-o KNOW-i` | teacher \| scholar \| wise | мимо |
| responsibility | `DO-o PI SOMEONE-o GOOD(=+3)` | hero \| benefactor \| helper | мимо |
| hang | `DO-i E THING-o ABOVE(=+3) TOUCH-i` | climb \| lift \| hug | мимо |
| concrete | `THING-o TOUCH-a PLACE-o` | location \| spot \| surface | мимо |
| plant | `LIVE-o MOVE-a MAYBE(=-5)` | statue \| corpse \| stone | мимо |
| sharp | `TOUCH-a GOOD(=-4)` | cruel \| harsh \| ugly | мимо |
| board | `THING-o LIVE-a(=-3) TOUCH-a` | fossil \| corpse \| bone | мимо |
| swing | `MOVE-i MANY(=+4) SAME(=+3)` | flock \| swarm \| gather | мимо |
