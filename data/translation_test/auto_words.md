# Автоматическое кодирование слов предложений: слово → корень + суффикс + градиент + 9 осей → ближайшее слово

Словарь для декодирования: 3000 слов списка + 3 слов предложений (3003 записей). Все слова предложений исключены из обучения осей и корней (корни из списка NSM заданы заранее). Декодирование — ближайшая запись по косинусу в пространстве X (без частотности); «сам» — слово вернулось само.

| слово | код | вернулось (топ-5) | сам |
| :-- | :-- | :-- | :-- |
| dog (noun) | SOMEONE-o [1.0,-0.0,1.0,-0.0,-1.0,0.0,0.0,1.0,-0.0] | someone, person, guy, woman, man | нет |
| sleep (verb) | TIME-i [2.0,0.0,1.0,1.0,0.0,0.0,1.0,-1.0,-1.0] | time, spend, pause, break, wait | нет |
| house (noun) | INSIDE-o [1.0,2.0,-0.0,0.0,-0.0,2.0,-0.0,0.0,1.0] | inside, room, basement, house, outside | в топ-5 |
| want (verb) | WANT-i [2.0,0.0,0.0,0.0,-2.0,1.0,1.0,1.0,1.0] | want, need, require, wish, desire | да |
| see (verb) | SEE-i [2.0,0.0,-1.0,1.0,-1.0,0.0,-2.0,0.0,-0.0] | look, see, observe, examine, glance | в топ-5 |
| friend (noun) | SOMEONE-o [1.0,1.0,-2.0,-0.0,-0.0,2.0,-1.0,-1.0,-2.0] | someone, friend, guy, woman, fellow | в топ-5 |
| hear (verb) | HEAR-i [0.0,0.0,0.0,-0.0,-2.0,1.0,-0.0,0.0,0.0] | hear, shout, listen, sing, exclaim | да |
| noise (noun) | HEAR-o [2.0,-3.0,3.0,3.0,-0.0,1.0,-0.0,0.0,1.0] | murmur, noise, loud, whisper, groan | в топ-5 |
| die (verb) | LIVE-i(=-5) [2.0,0.0,-0.0,-0.0,-1.0,0.0,0.0,-0.0,1.0] | die, suffer, survive, starve, kill | да |
| war (noun) | FEEL-o [1.0,0.0,-1.0,-1.0,0.0,-0.0,0.0,-1.0,-0.0] | feel, uneasy, sensation, emotion, emotionally | нет |
| rain (noun) | HAPPEN-o [4.0,0.0,-0.0,1.0,1.0,1.0,-1.0,-0.0,1.0] | happen, occur, erupt, arise, disappear | нет |
| stay (verb) | LIVE-i(=1) [3.0,-0.0,1.0,2.0,2.0,-0.0,4.0,0.0,1.0] | live, remain, stay, persist, reside | в топ-5 |
| big (adj) | BIG-a(=5) [2.0,-0.0,0.0,0.0,0.0,1.0,0.0,2.0,0.0] | big, huge, enormous, gigantic, massive | да |
| car (noun) | BODY-o [2.0,1.0,1.0,-1.0,-0.0,1.0,-1.0,0.0,0.0] | body, corpse, flesh, chest, skin | нет |
| move (verb) | MOVE-i [1.0,-2.0,0.0,0.0,-0.0,-0.0,1.0,-1.0,-1.0] | move, push, pull, lurch, turn | да |
| quickly (adv) | MOVE-e [1.0,-2.0,4.0,-3.0,1.0,-1.0,2.0,-2.0,-0.0] | swiftly, quickly, methodically, briskly, slowly | в топ-5 |
| king (noun) | PEOPLE-o [1.0,2.0,0.0,-2.0,-1.0,1.0,1.0,-1.0,2.0] | people, crowd, declare, society, proclaim | нет |
| say (verb) | KNOW-i [2.0,1.0,-2.0,-0.0,0.0,0.0,1.0,1.0,5.0] | know, tell, say, acknowledge, recognize | в топ-5 |
| dead (adj) | BODY-a [3.0,0.0,-1.0,0.0,-1.0,1.0,1.0,-3.0,3.0] | body, faint, corpse, dead, flesh | в топ-5 |
| think (verb) | THINK-i [2.0,-1.0,-2.0,0.0,-2.0,-0.0,-0.0,3.0,1.0] | think, suppose, believe, presume, imagine | да |
| water (noun) | ABOVE-o(=-2) [3.0,0.0,1.0,1.0,-1.0,2.0,1.0,0.0,-2.0] | below, above, down, descend, bottom | нет |
| cold (adj) | FEEL-a [3.0,-2.0,1.0,1.0,1.0,2.0,1.0,-0.0,0.0] | uneasy, nervous, feel, weary, faint | нет |
| child (noun) | SOMEONE-o [1.0,-0.0,0.0,-1.0,-1.0,-1.0,-0.0,-1.0,-2.0] | someone, guy, woman, person, man | нет |
| learn (verb) | KNOW-i [2.0,-2.0,2.0,-2.0,-1.0,-2.0,-3.0,0.0,-5.0] | learn, understand, identify, discover, educate | да |
| language (noun) | WORD-o [1.0,-2.0,-0.0,0.0,-1.0,-0.0,1.0,1.0,-3.0] | word, definition, expression, context, concept | нет |
| listen (verb) | HEAR-i [0.0,0.0,1.0,-2.0,-1.0,1.0,-0.0,2.0,-2.0] | hear, listen, sing, shout, yell | в топ-5 |
| meeting (noun) | PLACE-o [-1.0,1.0,-3.0,-2.0,2.0,3.0,-1.0,-1.0,-0.0] | place, fifth, location, sixth, appoint | нет |
| love (verb) | WANT-i [4.0,0.0,-5.0,1.0,-4.0,-0.0,-2.0,0.0,-0.0] | want, wish, desire, love, cherish | в топ-5 |
| book (noun) | PLACE-o [1.0,-1.0,-2.0,-3.0,0.0,2.0,-1.0,-1.0,2.0] | place, location, spot, fifth, eighth | нет |
| good (adj) | GOOD-a(=4) [2.0,-0.0,-1.0,1.0,-0.0,1.0,-1.0,1.0,1.0] | good, nice, excellent, great, wonderful | да |
| come (verb) | HAPPEN-i [3.0,1.0,1.0,1.0,-2.0,1.0,-0.0,-2.0,-1.0] | happen, occur, come, arise, disappear | в топ-5 |
| happy (adj) | GOOD-a(=1) [2.0,2.0,-4.0,-1.0,1.0,1.0,-2.0,-2.0,0.0] | good, excellent, wonderful, nice, fantastic | нет |
| know (verb) | KNOW-i [3.0,0.0,-0.0,1.0,-2.0,-0.0,1.0,2.0,1.0] | know, recognize, understand, tell, realize | да |
| answer (noun) | HEAR-o [-3.0,0.0,2.0,-2.0,-0.0,1.0,1.0,-2.0,3.0] | confirm, hear, declare, say, tell | нет |

Слово вернулось само первым: 9 из 34.