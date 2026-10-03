# Туда-обратно: вторые 200 слов (словарь из 33 корней, слепой тест)

Выборка: 200 новых случайных слов из `data/wordlist_en_x5.tsv` (seed 11, слова первого теста исключены; омографы — первое значение). Кодировал ассистент по словарю после правок (HEAT, BEGIN, GIVE, CONSUME, CONTAINER; без HEAR, KIND, WORD, PEOPLE), по одному разу, без подгонки. Декодировали четыре слепых субагента (sonnet). Оценки ставил ассистент.

**Итог:** точно 35, синоним 34, рядом 61, мимо 70. Слово или синоним — 69 (34,5%). Без 8 слов в кавычках (*west, brass, biblical, theology, anode, polynomial, anaconda, fourth*) — 61 из 192 (32%).

Для сравнения: первые 200 слов после перекодирования «мимо» — 91 (45,5%); но те слова уже были подогнаны под декодер. Честная оценка на новых словах — около трети.

| № | слово | код | обратный перевод | оценка |
| --: | :-- | :-- | :-- | :-- |
| 1 | yesterday | `TIME-o(=-2)` | yesterday | точно |
| 2 | dispel | `DO-i E THING-o BEGIN(=+5)` | begin | мимо |
| 3 | restrain | `DO-i E SOMEONE-o CAN(=-4)` | prevent | синоним |
| 4 | aside | `PLACE-e SIDE(=0)` | beside | рядом |
| 5 | exclaim | `SAY-i FEEL-o BIG(=+4)` | shout | синоним |
| 6 | certify | `SAY-i E KNOW-o MAYBE(=+4)` | promise | рядом |
| 7 | sign | `DO-i E SAY-o TOUCH-i` | write | рядом |
| 8 | count | `THINK-i E MANY-o` | believe | мимо |
| 9 | skeletal | `BODY-a PART-o LIVE(=-5)` | corpse | рядом |
| 10 | acre | `PLACE-o BIG(=+3)` | city | мимо |
| 11 | vulnerable | `DO-a CAN(=-4) GOOD(=-3)` | spoil | мимо |
| 12 | shrink | `HAPPEN-i BIG(=-3)` | accident | мимо |
| 13 | paint | `DO-i E THING-o SEE-o` | show | рядом |
| 14 | rifle | `THING-o DO-i E SOMEONE-o LIVE(=-5)` | kill | рядом |
| 15 | excellent | `GOOD-a(=+5)` | excellent | точно |
| 16 | western | `PLACE-a "west"` | west | синоним |
| 17 | heavy | `CAN-a(=-3) MOVE-i` | clumsy | мимо |
| 18 | improve | `HAPPEN-i GOOD(=+3)` | succeed | синоним |
| 19 | frighten | `DO-i FEEL-o GOOD(=-4)` | torture | рядом |
| 20 | anatomical | `BODY-a KNOW-o` | mind | рядом |
| 21 | describe | `SAY-i E SEE-o` | describe | точно |
| 22 | distal | `NEAR-a(=-4) BODY-o` | stranger | рядом |
| 23 | loan | `GIVE-o(=+3) TIME(=+3)` | gift | мимо |
| 24 | brass | `"brass"` | brass | точно |
| 25 | neatly | `DO-e SAME(=+4) GOOD(=+3)` | imitate | мимо |
| 26 | loose | `TOUCH-a NEAR(=-3)` | rough | мимо |
| 27 | downstairs | `PLACE-e ABOVE(=-3)` | downstairs | точно |
| 28 | element | `PART-o THING-o` | component | синоним |
| 29 | detectable | `SEE-a CAN(=+3)` | visible | синоним |
| 30 | part | `PART-o` | part | точно |
| 31 | lightly | `DO-e BIG(=-4)` | gently | синоним |
| 32 | achieve | `DO-i BEGIN(=+5) GOOD(=+3)` | improve | рядом |
| 33 | maintain | `DO-i E THING-o SAME(=+5)` | copy | мимо |
| 34 | regiment | `SOMEONE-o MANY(=+4) DO-i` | crowd | рядом |
| 35 | class | `SOMEONE-o MANY(=+3) KNOW-i` | scholars | рядом |
| 36 | accompany | `MOVE-i NEAR(=+5) SOMEONE-o` | approach | рядом |
| 37 | sad | `FEEL-a GOOD(=-3)` | sick | рядом |
| 38 | possible | `CAN-a(=+2)` | able | синоним |
| 39 | forbid | `SAY-i CAN(=-5) DO-o` | forbid | точно |
| 40 | occupy | `GIVE-i(=-5) E PLACE-o` | rob | мимо |
| 41 | texture | `TOUCH-o THING-o` | texture | точно |
| 42 | lurk | `DO-i SEE-a MAYBE(=-5)` | blind | мимо |
| 43 | escape | `MOVE-i INSIDE(=-5) CAN(=+3)` | enter | мимо |
| 44 | trot | `MOVE-i BIG(=+3)` | jump | рядом |
| 45 | exceed | `BIG-i(=+4) SAME` | equal | мимо |
| 46 | gleam | `DO-i SEE-o BIG(=+2)` | look | мимо |
| 47 | disease | `HAPPEN-o BODY-o GOOD(=-4)` | wound | рядом |
| 48 | glad | `FEEL-a GOOD(=+3)` | pleasant | рядом |
| 49 | look | `SEE-i` | look | точно |
| 50 | nervously | `FEEL-e GOOD(=-2)` | badly | мимо |
| 51 | national | `PLACE-a SOMEONE-o MANY(=+5)` | crowd | мимо |
| 52 | jacket | `THING-o BODY-o ABOVE(=+2)` | hat | рядом |
| 53 | safely | `DO-e GOOD(=-4) MAYBE(=-5)` | do badly | мимо |
| 54 | scale | `THING-o KNOW-i BIG(=+3)` | teacher | мимо |
| 55 | furthermore | `MANY-e(=+2) SAME(=+2)` | together | рядом |
| 56 | parallel | `SIDE-a SAME(=+4) NEAR(=+3)` | next | рядом |
| 57 | sound | `SAY-o THING-o` | word | мимо |
| 58 | abandon | `DO-i E SOMEONE-o NEAR(=-5)` | avoid | рядом |
| 59 | industrial | `DO-a THING-o MANY(=+4)` | work | рядом |
| 60 | absence | `NEAR-o(=-5)` | distance | мимо |
| 61 | gently | `DO-e BIG(=-3) GOOD(=+3)` | gently | точно |
| 62 | arrange | `DO-i E PART-o SAME(=+3)` | repeat | мимо |
| 63 | carry | `MOVE-i E THING-o BODY-o` | carry | точно |
| 64 | money | `THING-o GIVE-a(=0) WANT(=+3)` | gift | мимо |
| 65 | rotate | `MOVE-i SAME(=+5) PLACE-o` | stay | мимо |
| 66 | animal | `LIVE-o MOVE-a` | animal | точно |
| 67 | tension | `FEEL-o GOOD(=-2) BIG(=+3)` | pride | мимо |
| 68 | before | `TIME-e(=-3)` | long ago | рядом |
| 69 | curious | `WANT-a KNOW-o` | curious | точно |
| 70 | connect | `DO-i NEAR(=+5) TOUCH-i` | hug | мимо |
| 71 | fill | `DO-i E CONTAINER-o INSIDE(=+5)` | pack | синоним |
| 72 | area | `PLACE-o BIG(=+3)` | country | рядом |
| 73 | man | `SOMEONE-o SEX(=+5)` | man | точно |
| 74 | chest | `PART-o BODY-o SIDE(=+4)` | right | мимо |
| 75 | fix | `DO-i E THING-o GOOD(=+3)` | fix | точно |
| 76 | prove | `DO-i KNOW-o MAYBE(=+4)` | promise | рядом |
| 77 | anyway | `SAME-e(=+5) GOOD(=0)` | fairly | мимо |
| 78 | arrow | `THING-o MOVE-a LIVE(=-5)` | corpse | мимо |
| 79 | professor | `SOMEONE-o KNOW-o SAY-i` | teacher | синоним |
| 80 | seat | `THING-o PLACE-o BODY-o` | body part | мимо |
| 81 | morning | `TIME-o BEGIN(=-4)` | beginning | точно |
| 82 | false | `SAY-a MAYBE(=-5)` | lie | синоним |
| 83 | verbal | `SAY-a` | verbal | точно |
| 84 | happy | `FEEL-a GOOD(=+4)` | happy | точно |
| 85 | momentarily | `TIME-e BIG(=-4)` | quickly | рядом |
| 86 | sink | `MOVE-i ABOVE(=-4) INSIDE(=+4)` | sink | точно |
| 87 | papa | `SOMEONE-o SEX(=+5) HAPPEN(=-4)` | father | синоним |
| 88 | save | `DO-i E SOMEONE-o LIVE(=+4)` | revive | рядом |
| 89 | years | `TIME-o BIG(=+5) MANY(=+3)` | century | рядом |
| 90 | expenditure | `GIVE-o(=+4) THING-o` | donation | мимо |
| 91 | reach | `MOVE-i NEAR(=+5)` | approach | синоним |
| 92 | gold | `THING-o TOUCH-a WANT(=+4)` | soft | мимо |
| 93 | deep | `ABOVE-a(=-4) INSIDE(=+3)` | low | рядом |
| 94 | inch | `PART-o BIG(=-2)` | pinch | мимо |
| 95 | curve | `SEE-o MOVE-a SIDE(=+2)` | runner | мимо |
| 96 | modern | `TIME-a(=0) BEGIN(=-3)` | first | мимо |
| 97 | own | `SAME-a(=+5) SOMEONE-o` | friend | мимо |
| 98 | pressure | `TOUCH-o BIG(=+4)` | hug | рядом |
| 99 | necessitate | `WANT-i(=+5) E DO-o` | wish | мимо |
| 100 | dig | `DO-i E PLACE-o INSIDE(=+4)` | dig | точно |
| 101 | title | `SAY-o PI SOMEONE-o` | noun | мимо |
| 102 | anew | `BEGIN-e(=-5) SAME(=+3)` | again | синоним |
| 103 | depend | `HAPPEN-i(=+4) E THING-o` | result | рядом |
| 104 | oppose | `DO-i E SOMEONE-o SAME(=-4)` | harm | рядом |
| 105 | precise | `DO-a GOOD(=+4) SAME(=+5)` | same | рядом |
| 106 | secede | `MOVE-i PART-o NEAR(=-4)` | leave | рядом |
| 107 | contact | `TOUCH-o` | touch | синоним |
| 108 | eliminate | `DO-i E THING-o MANY(=0)` | nothing | мимо |
| 109 | request | `SAY-i WANT(=+4) E THING-o` | ask | синоним |
| 110 | sip | `CONSUME-i BIG(=-4)` | nibble | рядом |
| 111 | rub | `TOUCH-i MOVE-e` | feel | рядом |
| 112 | army | `SOMEONE-o MANY(=+5) DO-i` | everyone | мимо |
| 113 | gate | `THING-o PLACE-o INSIDE(=0)` | room | мимо |
| 114 | swallow | `CONSUME-i INSIDE(=+4)` | swallow | точно |
| 115 | blow | `HAPPEN-o TOUCH-i BIG(=+4)` | hit | синоним |
| 116 | group | `THING-o MANY(=+3) SAME(=+3)` | group | точно |
| 117 | verify | `DO-i E KNOW-o MAYBE(=+4)` | certainly | мимо |
| 118 | appeal | `SAY-o WANT-o` | wish | рядом |
| 119 | boy | `SOMEONE-o SEX(=+5) BIG(=-3)` | boy | точно |
| 120 | score | `MANY-o KNOW-o` | knowledge | мимо |
| 121 | vote | `SAY-i WANT-o` | ask | рядом |
| 122 | entry | `MOVE-o INSIDE(=+5)` | enter | синоним |
| 123 | furiously | `FEEL-e GOOD(=-4) BIG(=+4)` | pain | мимо |
| 124 | hint | `SAY-i KNOW-o BIG(=-3)` | whisper | рядом |
| 125 | tender | `TOUCH-a GOOD(=+3)` | soft | синоним |
| 126 | contribute | `GIVE-i(=+3) PART-o` | share | рядом |
| 127 | reduce | `DO-i E THING-o BIG(=-3)` | fix | мимо |
| 128 | propose | `SAY-i WANT-o DO-o` | order | рядом |
| 129 | bullet | `THING-o MOVE-a LIVE(=-5) BIG(=-4)` | toy | мимо |
| 130 | awaken | `DO-i E SOMEONE-o LIVE(=+2)` | wake | синоним |
| 131 | hole | `PLACE-o THING-o MANY(=0)` | warehouse | мимо |
| 132 | eye | `PART-o BODY-o SEE-i` | eye | точно |
| 133 | centrifuge | `DO-i E THING-o MOVE-i SAME(=+5)` | repeat | мимо |
| 134 | musical | `SAY-a MOVE-a GOOD(=+3)` | song | рядом |
| 135 | peace | `FEEL-o GOOD(=+4) SOMEONE-o MANY(=+5)` | happiness | рядом |
| 136 | truck | `CONTAINER-o MOVE-a BIG(=+4)` | truck | точно |
| 137 | ride | `MOVE-i E LIVE-o ABOVE(=+2)` | lift | мимо |
| 138 | cut | `DO-i E THING-o PART(=-3)` | break | синоним |
| 139 | visit | `MOVE-i NEAR(=+4) SOMEONE-o` | approach | рядом |
| 140 | regular | `TIME-a SAME(=+4) MANY(=+4)` | often | рядом |
| 141 | quiver | `MOVE-i BIG(=-4) MANY(=+4)` | scatter | мимо |
| 142 | net | `PART-a(=+5)` | complete | рядом |
| 143 | ahead | `SIDE-e(=+5)` | forward | синоним |
| 144 | hand | `PART-o BODY-o TOUCH-i` | hand | точно |
| 145 | unspeakable | `SAY-a CAN(=-5)` | mute | рядом |
| 146 | sex | `DO-o BODY-o SEX(=0)` | hermaphrodite | мимо |
| 147 | withdraw | `MOVE-i SIDE(=-5)` | retreat | синоним |
| 148 | biblical | `"Bible"-a` | biblical | точно |
| 149 | bunk | `THING-o BODY-o LIVE(=-2)` | corpse | мимо |
| 150 | miss | `FEEL-i WANT(=+3) NEAR(=-3)` | miss | точно |
| 151 | perfectly | `DO-e GOOD(=+5) SAME(=+5)` | identical | рядом |
| 152 | substantially | `BIG-e(=+3) PART(=+4)` | majority | рядом |
| 153 | payment | `GIVE-o(=+4) THING-o` | gift | рядом |
| 154 | accomplish | `DO-i BEGIN(=+5)` | finish | синоним |
| 155 | presidential | `SOMEONE-a ABOVE(=+5) MANY(=+5)` | crowd | мимо |
| 156 | sky | `PLACE-o ABOVE(=+5) SEE-a` | viewpoint | мимо |
| 157 | wagon | `CONTAINER-o MOVE-a BIG(=+2)` | truck | синоним |
| 158 | fourth | `4-a` | fourth | точно |
| 159 | chant | `SAY-i SAME(=+5) MANY(=+3)` | agree | мимо |
| 160 | stream | `MOVE-o CONSUME-o` | food | мимо |
| 161 | sale | `GIVE-o(=+3) THING-o SAME(=-3)` | exchange | рядом |
| 162 | unaware | `KNOW-a(=-3)` | unknown | синоним |
| 163 | entail | `HAPPEN-i(=+3) PART-o` | result | мимо |
| 164 | judgment | `THINK-o(=+5) GOOD(=0)` | decision | синоним |
| 165 | qualify | `DO-i E SOMEONE-o CAN(=+4)` | enable | рядом |
| 166 | remarkable | `GOOD-a(=+3) SEE-a BIG(=+3)` | beautiful | рядом |
| 167 | seemingly | `SEE-e MAYBE(=-1)` | perhaps | рядом |
| 168 | air | `THING-o MOVE-a MANY(=+5)` | traffic | мимо |
| 169 | theology | `KNOW-o "God"` | theology | точно |
| 170 | home | `PLACE-o LIVE-i` | habitat | рядом |
| 171 | expression | `SAY-o FEEL-o` | emotion | рядом |
| 172 | anode | `"anode"` | anode | точно |
| 173 | door | `THING-o MOVE-a INSIDE(=0)` | pocket | мимо |
| 174 | barely | `BIG-e(=-4)` | slightly | синоним |
| 175 | career | `DO-o TIME-o BIG(=+4)` | holiday | мимо |
| 176 | connection | `TOUCH-o NEAR(=+5)` | contact | синоним |
| 177 | principal | `BEGIN-a(=-4) BIG(=+3)` | giant | мимо |
| 178 | drug | `THING-o CONSUME-i BODY-o` | digest | рядом |
| 179 | gigantic | `BIG-a(=+5)` | huge | синоним |
| 180 | illuminate | `DO-i SEE-a GOOD(=+3)` | improve | мимо |
| 181 | relative | `SAME-a NEAR(=+3)` | similar | рядом |
| 182 | accelerate | `HAPPEN-i MOVE-a BIG(=+3)` | explode | мимо |
| 183 | particular | `PART-a SAME(=+5)` | equal | мимо |
| 184 | center | `PLACE-o INSIDE(=+5)` | center | точно |
| 185 | bad | `GOOD-a(=-4)` | awful | синоним |
| 186 | dirty | `TOUCH-a GOOD(=-3)` | rough | мимо |
| 187 | disagree | `THINK-i SAME(=-4)` | disagree | точно |
| 188 | madly | `FEEL-e GOOD(=-2) THINK(=-5)` | sad | мимо |
| 189 | muddy | `TOUCH-a GOOD(=-2) PLACE-o` | dirty | синоним |
| 190 | span | `PLACE-o BIG(=+3) SIDE(=0)` | neighborhood | мимо |
| 191 | therefore | `HAPPEN-e(=+4)` | eventually | рядом |
| 192 | justify | `SAY-i GOOD(=+4) E DO-o` | promise | мимо |
| 193 | polynomial | `"polynomial"` | polynomial | точно |
| 194 | daily | `TIME-a MANY(=+4) BIG(=-2)` | long | мимо |
| 195 | long | `BIG-a(=+3) PLACE-o` | spacious | рядом |
| 196 | social | `SOMEONE-a MANY(=+4)` | public | синоним |
| 197 | politics | `DO-o SOMEONE-o MANY(=+5)` | society | рядом |
| 198 | anaconda | `"anaconda"` | anaconda | точно |
| 199 | vanish | `SEE-i MAYBE(=-5)` | blind | мимо |
| 200 | store | `PLACE-o GIVE-o(=0) THING-o` | market | синоним |
