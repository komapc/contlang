# Коды математического кодера, прочитанные слепым декодером (24 слова)

Коды построены **без языковой модели**: `scripts/19_math_codes.py` кодирует слово точным перебором (до трёх корней, уровни −5…+5, главный корень первым) по вектору Numberbatch, двумя словарями — корни из полюсов `roots.yaml` и обученный словарь (`data/sparse_dict_learned.npz`, [docs/math.md](../../docs/math.md)). Коды — `data/math_codes.tsv` (словарь 45 корней, до добавления `TEXT` и оси `FIGHT`). Слова: 12 орудий из [roundtrip_tools.md](roundtrip_tools.md) и 12 случайных существительных из отложенной части.

Декодер (sonnet) видит только таблицы и правила чтения, оригиналов не видит, коды перемешаны. Счёт строгий, как в остальных тестах.

| словарь | точно | среди трёх |
| :-- | :-- | :-- |
| корни из полюсов | 1 из 24 | 1 из 24 |
| обученный | 3 из 24 | 4 из 24 |

Для сравнения: те же 12 орудий у кодировщика-модели без метки `U` — 1 из 24, с меткой — 13 из 24.

Что видно:

- Математический код **человеку пока не читается**. Сумма векторов попадает в область смысла (top50 в Numberbatch 95–98%), но выбранные корни — не те, которыми человек описал бы слово: кодер берёт любой корень, вектор которого хоть немного тянет в нужную сторону.
- Многозначность пространства: *saw* (пила) закодирована как `SEE TIME(=-4)` — вектор слова смешан с прошедшим временем *see*.
- `ABSTRACT` и `PARTICULAR` служат «заполнителем» — двигают вектор, но для читателя ничего не значат.
- Обученный словарь чуть лучше (узнаны *connection, woman, flow*, ещё *garden* среди трёх), но это в пределах шума.

Вывод: математика годится как **инструмент анализа** (найти лакуны, проверить полюса осей, сравнить варианты), а не как переводчик. Кодировщиком остаётся модель со спецификацией.

## корни из полюсов

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| flow | `GRAIN(=-3) MEASURE(=0) CHANGE(=0) \| o` | flow / current / tide | ✓ |
| saw | `SEE TIME(=-4) FEEL(=+2) \| o` | memory / nostalgia / recollection |  |
| court | `RULE(=+2) SIDE(=+2) FIGHT \| o` | front / battlefront / offensive |  |
| connection | `JOIN(=+2) LONG(=-2) HAPPEN(=-2) \| o` | link / knot / chain |  |
| scissors | `LONG(=-5) TOUCH(=+3) ABSTRACT(=-4) \| o` | wire / string / needle |  |
| thermometer | `HEAT(=-1) MEASURE(=+2) INSIDE(=0) \| o` | temperature / climate / warmth |  |
| woman | `SEX(=-3) THING(=+1) RULE(=+1) \| o` | queen / lady / goddess |  |
| brush | `LONG(=-1) ART(=+3) TOUCH(=0) \| i` | draw / sketch / paint |  |
| practice | `DO ABSTRACT(=+2) TOUCH(=+2) \| o` | effort / task / duty |  |
| oath | `WANT(=+1) SAY(=-4) RULE(=0) \| o` | prayer / request / plea |  |
| needle | `LONG(=-2) BIG(=-1) PLACE \| o` | trail / path / alley |  |
| garden | `ABSTRACT(=-3) INSIDE(=-1) ART(=+2) \| o` | decoration / facade / ornament |  |
| college | `ART(=0) RULE(=+1) MEASURE(=+3) \| o` | budget / ratio / proportion |  |
| responsibility | `RULE(=0) CAN(=-2) DO \| o` | job / labor / chore |  |
| earthquake | `HAPPEN(=+2) ABSTRACT(=-5) HEAT(=+2) \| o` | fever / burn / sweat |  |
| broom | `ABSTRACT(=-2) ABOVE(=+2) LONG(=-1) \| o` | mast / pole / antenna |  |
| hammer | `ABSTRACT(=-3) MATTER(=-5) GIVE(=-5) \| o` | loot / trophy / prize |  |
| pen | `THING(=+1) CONSUME(=-2) LONG(=+1) \| o` | sap / resin / bark |  |
| religion | `ART(=+2) ABSTRACT(=+3) RULE(=-2) \| o` | fantasy / imagination / joke |  |
| ladder | `ABSTRACT(=-2) ABOVE(=+1) LONG(=0) \| o` | beam / rafter / lever |  |
| key | `PARTICULAR(=0) LIVE(=+3) ABSTRACT(=-2) \| o` | creature / being / organism |  |
| spoon | `GRAIN(=-1) PART(=-4) CONSUME(=+5) \| o` | sip / swallow / lick |  |
| machinery | `ART(=-2) DO \| o` | craft / skill / technique |  |
| knife | `LONG(=-1) PART(=-5) TOUCH(=+5) \| o` | thorn / needle / splinter |  |

## обученный словарь

| слово | код | ответ декодера (лучшее / альтернативы) | |
| :-- | :-- | :-- | :-: |
| spoon | `GRAIN(=-1) PART(=-2) CONSUME(=+4) \| o` | sip / gulp / drop |  |
| court | `RULE(=+2) SIDE(=+2) FIGHT \| o` | offensive / battle / front |  |
| knife | `BODY PART(=-4) TOUCH(=+5) \| o` | tooth / bone / nail |  |
| saw | `SEE TIME(=-3) FEEL(=+1) \| o` | memory / recollection / nostalgia |  |
| college | `ART(=0) RULE(=+1) ABOVE(=+3) \| o` | director / boss / authority |  |
| thermometer | `HEAT(=-1) MEASURE(=+1) BODY \| o` | fever / temperature / warmth |  |
| ladder | `ABOVE(=+1) ABSTRACT(=-2) LONG(=+1) \| o` | pole / mast / tower |  |
| oath | `WANT(=+1) RULE(=+2) SAY(=-2) \| o` | request / petition / plea |  |
| key | `PARTICULAR(=+1) HAPPEN(=-3) GIVE(=-3) \| o` | motive / reason / purpose |  |
| hammer | `MATTER(=-3) GIVE(=-4) LONG(=+2) \| o` | hook / tongs / handle |  |
| pen | `LONG(=+1) THING(=+3) CONSUME(=-2) \| o` | worm / snake / caterpillar |  |
| connection | `HAPPEN(=-1) JOIN(=+3) NEAR(=0) \| o` | connection / contact / link | ✓ |
| machinery | `ART(=-3) MATTER(=-1) DO \| o` | machine / technology / industry |  |
| brush | `PART(=-1) LONG(=-1) HEAT(=+4) \| i` | singe / scorch / ignite |  |
| scissors | `LONG(=-4) TOUCH(=+3) ABSTRACT(=-4) \| o` | wire / cable / string |  |
| woman | `SEX(=-3) SOMEONE(=+1) THING(=+2) \| o` | woman / girl / female | ✓ |
| garden | `ABSTRACT(=-3) INSIDE(=-1) PLACE \| o` | yard / garden / courtyard | ~ |
| earthquake | `HEAT(=+1) HAPPEN(=+4) SAY(=+1) \| o` | compliment / praise / welcome |  |
| flow | `GRAIN(=-2) MOVE(=+1) CHANGE(=+1) \| o` | flow / current / stream | ✓ |
| needle | `LONG(=-2) BODY BIG(=-1) \| o` | tail / limb / leg |  |
| religion | `ART(=+3) ABSTRACT(=+4) RULE(=-2) \| o` | fantasy / imagination / fancy |  |
| responsibility | `RULE(=+1) KNOW(=+1) DO \| o` | skill / expertise / profession |  |
| broom | `ABSTRACT(=-2) LONG(=0) ABOVE(=+2) \| o` | column / pillar / pole |  |
| practice | `DO ABSTRACT(=+2) PART(=+3) \| o` | organization / system / method |  |
