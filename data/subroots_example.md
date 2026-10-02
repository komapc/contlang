# Пример: подкорни (кластеры слов внутри корня)

Корни NSM (27) + градиенты, назначение слов по ближайшему корню (скрипт `11_sentences_auto.py`, 3000 слов); внутри корня слова разбиты k-means (k=6) на подкорни. Показаны 7 ближайших к центру слов (v/n/a — часть речи записи).

## MOVE (168 слов) -> 6 подкорней
- MOVE.1 (36): resign(v), withdraw(v), abandon(v), relinquish(v), quit(v), retire(v), leave(v)
- MOVE.2 (13): change(v), alter(v), modify(v), transform(v), amend(v), revise(v), radically(a)
- MOVE.3 (28): swiftly(a), rapidly(a), quickly(a), slowly(a), briskly(a), rapid(a), fast(a)
- MOVE.4 (49): move(v), backward(a), lurch(v), motion(n), movement(n), whirl(v), push(v)
- MOVE.5 (25): jump(v), heave(v), fling(v), haul(v), leap(v), pull(v), swoop(v)
- MOVE.6 (17): sell(v), purchase(v), sale(n), acquire(v), trade(n), invest(v), bid(v)

## WANT (115 слов) -> 6 подкорней
- WANT.1 (11): choose(v), select(v), choice(n), elect(v), buy(v), decide(v), afford(v)
- WANT.2 (22): require(v), need(v), necessitate(v), requirement(n), want(v), necessary(a), necessity(n)
- WANT.3 (22): allow(v), authorize(v), enable(v), permit(v), able(a), forbid(v), compel(v)
- WANT.4 (20): wish(v), sincerely(a), hope(v), eagerly(a), promise(v), beg(v), profess(v)
- WANT.5 (28): desire(n), attempt(v), try(v), urge(v), strive(v), eager(a), desperate(a)
- WANT.6 (12): dislike(v), hate(v), hatred(n), love(v), prefer(v), tendency(n), tend(v)

## PLACE (107 слов) -> 6 подкорней
- PLACE.1 (21): establish(v), appoint(v), arrange(v), designate(v), organize(v), furnish(v), create(v)
- PLACE.2 (18): eighth(a), sixth(a), ninth(a), fifth(a), eighteenth(a), round(a), title(n)
- PLACE.3 (27): seat(n), sit(v), position(n), place(n), hold(v), chair(n), firmly(a)
- PLACE.4 (19): earth(n), planet(n), world(n), planetary(a), land(n), soil(n), anywhere(a)
- PLACE.5 (10): liquor(n), bar(n), establishment(n), whisky(n), institution(n), store(n), resort(v)
- PLACE.6 (12): safely(a), safe(a), secure(v), preserve(v), calm(a), shelter(n), neatly(a)

## PEOPLE (92 слов) -> 6 подкорней
- PEOPLE.1 (9): personnel(n), military(a), army(n), civilian(a), staff(n), crew(n), police(n)
- PEOPLE.2 (12): group(n), collective(a), community(n), society(n), congregation(n), unite(v), company(n)
- PEOPLE.3 (15): democratic(a), presidential(a), congress(n), president(n), government(n), communist(a), openly(a)
- PEOPLE.4 (23): crowd(n), people(n), audience(n), mingle(v), fewer(a), entertain(v), lot(n)
- PEOPLE.5 (21): cultural(a), culture(n), civilization(n), folk(n), human(a), social(a), citizen(n)
- PEOPLE.6 (12): violently(a), wildly(a), savagely(a), madly(a), rage(n), drunkenly(a), arbitrarily(a)

## GOOD (112 слов) -> 6 подкорней
- GOOD.1 (10): glad(a), happy(a), fortunate(a), lucky(a), congratulate(v), luck(n), thank(v)
- GOOD.2 (23): wonderful(a), lovely(a), fantastic(a), beautiful(a), delightful(a), magnificent(a), beautifully(a)
- GOOD.3 (20): perfectly(a), correctly(a), perfect(a), properly(a), nicely(a), good(a), proper(a)
- GOOD.4 (14): bad(a), terrible(a), awful(a), badly(a), poorly(a), poor(a), worst(a)
- GOOD.5 (20): useful(a), efficient(a), improve(v), helpful(a), effective(a), efficiency(n), enhance(v)
- GOOD.6 (25): reasonably(a), adequate(a), sufficiently(a), sufficient(a), reasonable(a), adequately(a), satisfactory(a)
