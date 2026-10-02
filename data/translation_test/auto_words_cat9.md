# Автоматическое кодирование слов предложений: слово → корень + суффикс + градиент + 9 осей → ближайшее слово

Словарь для декодирования: 3000 слов списка + 3 слов предложений (3003 записей). Все слова предложений исключены из обучения осей и корней (корни из списка NSM заданы заранее). Декодирование — ближайшая запись по косинусу в пространстве X (без частотности); «сам» — слово вернулось само.

| слово | код | вернулось (топ-5) | сам |
| :-- | :-- | :-- | :-- |
| dog (noun) | FOOD-o [-1.0,1.0,-1.0,0.0,0.0,1.0,-1.0,1.0,-0.0] | food, eat, meal, feed, milk | нет |
| sleep (verb) | ROOM-i [-2.0,-0.0,1.0,-2.0,0.0,-0.0,0.0,-1.0,1.0] | room, bedroom, upstairs, basement, downstairs | нет |
| house (noun) | ROOM-o [-1.0,1.0,-0.0,0.0,1.0,1.0,-0.0,-2.0,-0.0] | room, bedroom, basement, upstairs, hall | нет |
| want (verb) | WANT-i [-2.0,0.0,-2.0,-1.0,0.0,2.0,-1.0,0.0,1.0] | want, need, require, wish, necessitate | да |
| see (verb) | SEE-i [-2.0,0.0,-1.0,-0.0,0.0,0.0,-1.0,-0.0,-2.0] | look, see, observe, gaze, sight | в топ-5 |
| friend (noun) | SOMEONE-o [-1.0,1.0,1.0,2.0,-2.0,2.0,-0.0,1.0,-3.0] | someone, woman, man, guy, person | нет |
| hear (verb) | HEAR-i [-0.0,1.0,-1.0,-0.0,0.0,2.0,-1.0,1.0,-1.0] | hear, listen, shout, sing, exclaim | да |
| noise (noun) | HEAR-o [-1.0,-3.0,0.0,-3.0,0.0,0.0,-0.0,-1.0,2.0] | noise, murmur, loud, sound, whisper | да |
| die (verb) | LIVE-i(=-5) [-2.0,1.0,-1.0,-1.0,1.0,1.0,1.0,0.0,-0.0] | die, survive, suffer, endure, leave | да |
| war (noun) | OFFICER-o [-2.0,-1.0,-1.0,1.0,1.0,-3.0,1.0,-0.0,0.0] | officer, lieutenant, captain, soldier, chief | нет |
| rain (noun) | EVENT-o [-3.0,-2.0,1.0,-0.0,2.0,-0.0,0.0,-3.0,1.0] | event, occurrence, night, fling, competition | нет |
| stay (verb) | LIVE-i(=0) [-2.0,0.0,3.0,-1.0,-0.0,1.0,0.0,-1.0,4.0] | remain, stay, live, persist, dwell | в топ-5 |
| big (adj) | BIG-a(=5) [-3.0,0.0,0.0,-0.0,0.0,1.0,-1.0,1.0,2.0] | big, huge, enormous, gigantic, massive | да |
| car (noun) | BODY-o [-2.0,1.0,-1.0,-1.0,1.0,1.0,0.0,1.0,-0.0] | body, corpse, flesh, skin, chest | нет |
| move (verb) | MOVE-i [-1.0,-1.0,0.0,-0.0,-2.0,0.0,1.0,-0.0,1.0] | move, push, pull, lurch, turn | да |
| quickly (adv) | MOVE-e [-1.0,-0.0,1.0,-2.0,-0.0,2.0,4.0,3.0,4.0] | swiftly, calmly, quickly, quietly, methodically | в топ-5 |
| king (noun) | ROOM-o [-0.0,3.0,-0.0,1.0,2.0,-0.0,1.0,0.0,-1.0] | room, bedroom, hall, basement, house | нет |
| say (verb) | KNOW-i [-2.0,1.0,0.0,2.0,5.0,-0.0,-0.0,-0.0,-0.0] | tell, know, say, acknowledge, recognize | в топ-5 |
| dead (adj) | BODY-a [-3.0,0.0,-1.0,1.0,3.0,2.0,2.0,-2.0,-1.0] | body, dead, corpse, flesh, faint | в топ-5 |
| think (verb) | THINK-i [-2.0,0.0,-2.0,1.0,1.0,-0.0,-3.0,1.0,-0.0] | think, suppose, consider, presume, believe | да |
| water (noun) | FOOD-o [-1.0,-1.0,0.0,-0.0,-0.0,1.0,-0.0,-1.0,0.0] | food, meal, feed, eat, milk | нет |
| cold (adj) | FEEL-a [-3.0,-3.0,1.0,-1.0,1.0,1.0,-0.0,-1.0,1.0] | uneasy, feel, faint, ache, weary | нет |
| child (noun) | SOMEONE-o [0.0,0.0,1.0,-0.0,-3.0,1.0,1.0,1.0,-0.0] | someone, woman, man, person, guy | нет |
| learn (verb) | KNOW-i [-2.0,-1.0,-1.0,-2.0,-5.0,-1.0,1.0,3.0,-0.0] | understand, learn, identify, comprehend, discover | в топ-5 |
| language (noun) | WORD-o [-1.0,-0.0,-1.0,-0.0,-4.0,0.0,-2.0,1.0,1.0] | word, definition, expression, concept, term | нет |
| listen (verb) | HEAR-i [-0.0,1.0,-1.0,-1.0,-2.0,2.0,-1.0,3.0,0.0] | hear, listen, sing, shout, loudly | в топ-5 |
| meeting (noun) | EVENT-o [1.0,0.0,3.0,1.0,-0.0,3.0,1.0,1.0,-1.0] | event, attend, meeting, participate, discussion | в топ-5 |
| love (verb) | EMOTION-i [-3.0,3.0,-4.0,2.0,-0.0,2.0,-1.0,-0.0,-2.0] | love, emotion, hate, admire, hatred | да |
| book (noun) | TEXT-o [-2.0,-0.0,-1.0,1.0,0.0,-0.0,1.0,2.0,-0.0] | text, article, write, read, page | нет |
| good (adj) | GOOD-a(=4) [-2.0,-0.0,-0.0,0.0,1.0,0.0,-2.0,-0.0,-1.0] | good, nice, excellent, great, respectable | да |
| come (verb) | HAPPEN-i [-3.0,0.0,-1.0,-1.0,-1.0,2.0,1.0,-1.0,-1.0] | happen, occur, come, arise, disappear | в топ-5 |
| happy (adj) | GOOD-a(=1) [-2.0,2.0,1.0,3.0,0.0,2.0,1.0,0.0,-4.0] | good, excellent, wonderful, nice, lovely | нет |
| know (verb) | KNOW-i [-3.0,1.0,-3.0,0.0,1.0,0.0,-2.0,0.0,1.0] | know, recognize, understand, tell, realize | да |
| answer (noun) | HEAR-o [3.0,1.0,0.0,-1.0,2.0,3.0,2.0,2.0,1.0] | hear, listen, tell, say, aloud | нет |

Слово вернулось само первым: 10 из 34.