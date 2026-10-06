# Кавычки и здоровье: слепой тест

Два вопроса в одном прогоне (40 слов):

1. **Где граница кавычек.** Нынешнее правило: в кавычках «институты, должности, технические термины, для которых нет корня» — граница размыта (`"official"`, `"company"` в примерах, а суд, школу, правительство мы собрали из корней). Новое правило (набор B): из корней — **категории и назначения**; в кавычках, в международной или латинской форме, — **конкретные члены семейства**, которые корнями не отличить (виды — латынь, вещества — химия, органы — латынь анатомии `"hepar"`, `"ren"`, небесные тела — имена `"Sol"`, `"Luna"`, игры — названия `"football"`), и **узкие термины** (`"enzyme"`, `"orbit"`, `"Parliament"`). 24 слова: *protein, enzyme, vitamin, oxygen, bacteria, liver, kidney, organ, football, chess, game, sport, sun, moon, star, planet, satellite, orbit, parliament, company, official, railway, broadcasting, newspaper*.
2. **Здоровье и сон через середину `LIVE`** (предложение автора): `LIVE(=0)` — «жив наполовину», `GOOD` — какая середина: спать `LIVE(=0) GOOD(=+3)`, болеть `LIVE(=0) GOOD(=-4)`. 16 слов: *sleep, wake, tired, rest, dream, sick, disease, healthy, heal, doctor, hospital, medicine, die, wound, pain, patient*.

Протокол как в [roundtrip_lacunae4](roundtrip_lacunae4.md): A — нынешняя спецификация, B — с правилом и рецептами (их видят кодировщик и декодер); sonnet, 2 кодировщика, по 1 декодеру; ✓ лучшее слово, ~ среди трёх.

| | A1 | A2 | B1 | B2 |
| :-- | --: | --: | --: | --: |
| кавычки и категории (24) | 22 / 23 | 18 / 19 | 24 / 24 | 24 / 24 |
| здоровье и сон (16) | 15 / 15 | 10 / 11 | 16 / 16 | 16 / 16 |
| совпадение решений «кавычки или корни» у двух кодировщиков | 18 из 24 | | 24 из 24 | |

Что видно:

- **Новое правило однозначно**: оба кодировщика B приняли одинаковые решения во всех 24 словах; в A — расхождение в 6 (*football, chess, planet, orbit* — один в кавычки, другой из корней; *sun, moon* — из корней, но разными кодами). Кодировщики A по старому правилу ставили в кавычки *company, official, railway, broadcasting* — их рецепты из корней читаются (4 из 4).
- **Латинские и международные формы читаются**: `"hepar"`, `"ren"`, `"Sol"`, `"Luna"` — 8 из 8. Луна из корней (`ABOVE(=+5) SEE BEGIN(=+5)`) — 0 из 2 (*horizon, sunset*).
- **Здоровье без нового корня**: середина `LIVE` работает (16 из 16). Кодировщик A1 и без рецепта писал `LIVE GOOD(=±4)` (15 из 15); A2 писал `BODY GOOD` — хуже (*gym*, *food*). `LIVE(=0) CAN(=-3)` — усталый, `LIVE(=0) SEE ABSTRACT(=+5)` — сновидение, `BODY JOIN(=-3)` — рана (у A с `GOOD(=-4)` — *surgery*).
- Оговорка: декодер B видел правило и рецепты.

## По словам

| слово | A1 | A2 | B1 | B2 | код B |
| :-- | :-: | :-: | :-: | :-: | :-- |
| protein | ✓ | ✓ | ✓ | ✓ | `"protein"` |
| enzyme | ✓ | ✓ | ✓ | ✓ | `"enzyme"` |
| vitamin | ✓ | ✓ | ✓ | ✓ | `"vitamin"` |
| oxygen | ✓ | ✓ | ✓ | ✓ | `"oxygen"` |
| bacteria | ✓ | ✓ | ✓ | ✓ | `"bacteria"` |
| liver | ✓ | ✓ | ✓ | ✓ | `"hepar"` |
| kidney | ✓ | ✓ | ✓ | ✓ | `"ren"` |
| organ | ✓ | ~ limb | ✓ | ✓ | `BODY INSIDE(=+5) PART(=-2) \| o` |
| football | ✓ | ✗ exercise | ✓ | ✓ | `"football"` |
| chess | ✓ | ✓ | ✓ | ✓ | `"chess"` |
| game | ✓ | ✓ | ✓ | ✓ | `FIGHT(=-5) \| o` |
| sport | ~ exercise | ✗ athlete | ✓ | ✓ | `FIGHT(=-5) BODY \| o` |
| sun | ✓ | ✓ | ✓ | ✓ | `"Sol"` |
| moon | ✗ horizon | ✗ sunset | ✓ | ✓ | `"Luna"` |
| star | ✓ | ✓ | ✓ | ✓ | `HEAT(=+5) ABOVE(=+5) PART(=-2) \| o` |
| planet | ✓ | ✗ airport | ✓ | ✓ | `PLACE ABOVE(=+5) MOVE \| o` |
| satellite | ✓ | ✓ | ✓ | ✓ | `DO(=+5) ABOVE(=+5) MOVE \| o` |
| orbit | ✓ | ✗ road | ✓ | ✓ | `"orbit"` |
| parliament | ✓ | ✓ | ✓ | ✓ | `"Parliament"` |
| company | ✓ | ✓ | ✓ | ✓ | `PART(=+5) DO VALUE \| o` |
| official | ✓ | ✓ | ✓ | ✓ | `SOMEONE RULE(=+4) \| o` |
| railway | ✓ | ✓ | ✓ | ✓ | `PLACE MOVE LONG(=+5) \| o` |
| broadcasting | ✓ | ✓ | ✓ | ✓ | `SAY GIVE(=+3) MANY(=+5) \| o` |
| newspaper | ✓ | ✓ | ✓ | ✓ | `TEXT TIME(=0) PART(=+5) \| o` |
| sleep | ✓ | ✓ | ✓ | ✓ | `LIVE(=0) GOOD(=+3) \| i` |
| wake | ✓ | ✗ surprise | ✓ | ✓ | `LIVE(=+5) BEGIN(=-4) \| i` |
| tired | ✓ | ✗ numb | ✓ | ✓ | `LIVE(=0) CAN(=-3) \| a` |
| rest | ✓ | ✓ | ✓ | ✓ | `MOVE(=-5) GOOD(=+3) \| i` |
| dream | ✓ | ✗ observe | ✓ | ✓ | `LIVE(=0) SEE ABSTRACT(=+5) \| o` |
| sick | ✓ | ✓ | ✓ | ✓ | `LIVE(=0) GOOD(=-4) \| a` |
| disease | ✓ | ✓ | ✓ | ✓ | `LIVE(=0) GOOD(=-4) \| o` |
| healthy | ✓ | ✓ | ✓ | ✓ | `LIVE(=+5) GOOD(=+4) \| a` |
| heal | ✓ | ✓ | ✓ | ✓ | `LIVE GOOD(=+4) \| i K+3` |
| doctor | ✓ | ✓ | ✓ | ✓ | `SOMEONE LIVE GOOD(=+4) \| o` |
| hospital | ✓ | ~ gym | ✓ | ✓ | `PLACE LIVE(=0) GOOD(=-4) \| o` |
| medicine | ✓ | ✗ food | ✓ | ✓ | `DO(=+5) LIVE GOOD(=+4) \| o` |
| die | ✓ | ✓ | ✓ | ✓ | `LIVE(=-5) \| i` |
| wound | ✗ surgery | ✗ medicine | ✓ | ✓ | `BODY JOIN(=-3) \| o` |
| pain | ✓ | ✓ | ✓ | ✓ | `BODY FEEL(=+4) GOOD(=-4) \| o` |
| patient | ✓ | ✓ | ✓ | ✓ | `SOMEONE LIVE(=0) GOOD(=-4) \| o` |
