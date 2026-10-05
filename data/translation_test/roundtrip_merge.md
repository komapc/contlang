# Слияние MATTER и GRAIN, PARTICULAR → SAME, ось «роль в действии» у DO: слепой тест

Вопрос: можно ли убрать корни без потерь и выразить орудие осью вместо метки `U` ([roundtrip_tools.md](roundtrip_tools.md)). Слова: *water*, *steam*, *smoke*, *ice*, *stone*, *sand*, *flour*, *honey*, *gas*, *liquid*, *melt*, *breathe*, *special*, *unique*, *specific*, *general*, *universal*, *typical*, *ordinary*, *rare*, *individual*, *especially*, *exception*, *detail*, *knife*, *hammer*, *saw*, *needle*, *key*, *spoon*, *brush*, *scissors*, *pen*, *broom*, *ladder*, *thermometer*.

Кодировщик видит `docs/tables.md`, SKILL.md, `docs/encoding.md`; декодер — только таблицы и правила чтения, оригиналов не видит, коды перемешаны. Наборы A — нынешняя спецификация (без орудий: их база уже есть), наборы B — с изменениями (кодировщик и декодер видят описание ниже). Модель sonnet, 2 кодировщика и 1 декодер на набор. Счёт строгий: ✓ лучшее слово = оригинал, ~ оригинал среди трёх.

| корень | что меняется |
| :-- | :-- |
| MATTER | **в этом тесте корня нет**, его заменяет GRAIN |
| GRAIN | **новая ось — насколько вещество держится вместе**: −5 газ, пар, дым … −3 жидкость, течёт (вода, мёд) … 0 сыпучее (песок, мука, крупа) … +5 цельный твёрдый кусок (камень, слиток, монолит). `GRAIN(=-5) \| o` газ, `GRAIN(=-3) \| o` жидкость, `GRAIN(=+5) \| a` цельный, сплошной, твёрдый. Еда и питьё: есть = `CONSUME(=+5) GRAIN(=+3) \| i`, пить = `CONSUME(=+5) GRAIN(=-3) \| i`, вдыхать = `CONSUME(=+5) GRAIN(=-5) \| i` |
| PARTICULAR | **в этом тесте корня нет**; особое и общее — через SAME: особенный, уникальный = `SAME(=-4)` («не такой, как другие»), общий, всеобщий = `SAME(=+4) MANY(=+5)`, обычный = `SAME(=+3)` |
| DO | **новая ось — роль в действии**: −5 тот, кто делает (деятель) … 0 само действие … +5 то, чем делают (орудие, инструмент, средство). Без значения — делать, как раньше. Орудие: корни описывают действие, `DO(=+5)` делает из него инструмент: `SEE DO(=+5) \| o` — очки, бинокль. Деятель: `JOIN(=-4) DO(=-5) \| o` — тот, кто режет |

| изменение | сейчас (A1 + A2) | с изменением (B1 + B2) |
| :-- | :-- | :-- |
| MATTER + GRAIN → GRAIN | 11 / 20 из 24 | 17 / 21 из 24 |
| PARTICULAR → SAME | 13 / 17 из 24 | 12 / 16 из 24 |
| орудия: ось у DO | 1 / 3 из 24 без метки; 13 / 17 из 24 с меткой `U` (прошлый тест) | 17 / 17 из 24 |

Что видно:

- **Ось у `DO` для орудий — лучше метки `U`**: 17 из 24 против 13. Узнаются нож, ножницы, пила, молоток, щётка, ручка (`TEXT DO(=+5)`), градусник, лестница — в обоих наборах, ключ — в одном. Не собираются: ложка (`CONSUME(=+5) GRAIN(=-3) DO(=+5)` → *cup, glass*), метла, иголка. Цена: ось занимает одно из трёх мест под корни, метка `U` — нет.
- **Слияние `MATTER` и `GRAIN` не теряет, а выигрывает**: 11 → 17. Одна шкала (−5 газ … −3 жидкость … 0 сыпучее … +5 цельное) снимает путаницу двух осей с противоположным направлением (*liquid* был `MATTER(=0) GRAIN(=-5)`). Мёд не собирается ни там, ни там (читается как вино, сок).
- **`PARTICULAR` убирается без потерь**: 13 → 12, в пределах шума. Особенный = `SAME(=-4)`, общий = `SAME(=+4) MANY(=+5)`, обычный = `SAME(=+3)`. Не собираются и сейчас, и после: *rare* (`MANY(=+1)` → *few*), *specific* (→ *famous, known*).

Оговорки: в описании изменений были готовые примеры (вдыхать, очки), часть выигрыша B от них; по одному декодеру на набор; шум порядка ±3 из 24.

## Набор A1 (сейчас)

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| smoke | `MATTER(=+5) HEAT(=+5) \| o` | smoke / steam / flame | ✓ |
| flour | `THING(=0) GRAIN(=0) CONSUME(=+5) \| o` | rice / wheat / grain |  |
| ice | `MATTER(=-5) HEAT(=-5) \| o` | ice / frost / snow | ✓ |
| steam | `MATTER(=+5) HEAT(=+2) \| o` | steam / vapor / fog | ✓ |
| individual | `PARTICULAR(=+4) PART(=-2) \| a` | individual / single / particular | ✓ |
| stone | `THING(=-5) \| o` | stone / rock / pebble | ✓ |
| melt | `CHANGE MATTER(=0) HEAT(=+3) \| i` | boil / melt / cook | ~ |
| gas | `MATTER(=+5) \| o` | air / gas / wind | ~ |
| exception | `PARTICULAR(=+4) JOIN(=-5) RULE \| o` | divorce / separation / exception | ~ |
| detail | `PART(=-2) PARTICULAR(=+3) KNOW \| o` | specialist / expert / scholar |  |
| general | `PARTICULAR(=-4) \| a` | general / common / universal | ✓ |
| universal | `PARTICULAR(=-5) MANY(=+5) \| a` | universal / all / every | ✓ |
| breathe | `CONSUME(=0) MATTER(=+5) LIVE(=+3) \| i` | breathe / inhale / smoke | ✓ |
| water | `MATTER(=0) CONSUME(=+5) \| o` | drink / water / beverage | ~ |
| especially | `PARTICULAR(=+4) \| e I+3` | especially / particularly / specifically | ✓ |
| sand | `THING(=-5) GRAIN(=0) \| o` | sand / gravel / dust | ✓ |
| typical | `PARTICULAR(=0) SAME(=+4) MANY(=+3) \| a` | typical / usual / common | ✓ |
| honey | `CONSUME(=+5) GRAIN(=-5) GOOD(=+3) \| o` | soup / juice / broth |  |
| rare | `MANY(=+1) PARTICULAR(=+3) \| a` | some / several / certain |  |
| unique | `PARTICULAR(=+5) SAME(=-5) \| a` | unique / different / other | ✓ |
| specific | `PARTICULAR(=+3) KNOW(=+5) \| a` | familiar / known / aware |  |
| liquid | `MATTER(=0) GRAIN(=-5) \| o` | water / liquid / juice | ~ |
| special | `PARTICULAR(=+4) \| a` | special / specific / particular | ✓ |
| ordinary | `PARTICULAR(=0) \| a` | ordinary / normal / usual | ✓ |

## Набор A2 (сейчас)

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| rare | `MANY(=+1) \| a` | few / some / several |  |
| ordinary | `PARTICULAR(=0) \| a` | specific / particular / certain |  |
| specific | `PARTICULAR(=+4) KNOW(=+5) \| a` | famous / known / well-known |  |
| universal | `PARTICULAR(=-5) MANY(=+5) \| a` | general / universal / common | ~ |
| special | `PARTICULAR(=+3) \| a` | special / particular / specific | ✓ |
| water | `MATTER(=0) LIVE(=+3) \| o` | blood / water / milk | ~ |
| honey | `CONSUME GRAIN(=-5) GOOD(=+3) \| o` | wine / beer / juice |  |
| stone | `THING(=-5) TOUCH(=+5) \| o` | rock / stone / metal | ~ |
| unique | `PARTICULAR(=+5) SAME(=-5) \| a` | different / unique / other | ~ |
| liquid | `MATTER(=0) \| o` | water / liquid / oil | ~ |
| detail | `PART(=-4) PARTICULAR(=+3) KNOW \| o` | detail / fact / information | ✓ |
| typical | `PARTICULAR(=-3) SAME(=+4) \| a` | similar / same / equal |  |
| especially | `PARTICULAR(=+5) \| e` | especially / only / specially | ✓ |
| general | `PARTICULAR(=-4) \| a` | common / general / usual | ~ |
| exception | `PARTICULAR(=+4) JOIN(=-5) RULE \| o` | exception / privilege / law | ✓ |
| melt | `CHANGE(=+3) HEAT(=+3) MATTER(=0) \| i` | melt / dissolve / boil | ✓ |
| ice | `MATTER(=-5) HEAT(=-5) \| o` | ice / snow / frost | ✓ |
| smoke | `MATTER(=+4) HEAT(=+5) \| o` | steam / smoke / fire | ~ |
| sand | `THING(=-5) GRAIN(=0) PART(=-5) \| o` | sand / dust / gravel | ✓ |
| flour | `CONSUME GRAIN(=0) PART(=-5) \| o` | rice / salt / sugar |  |
| individual | `PART(=-2) PARTICULAR(=+4) \| a` | individual / partial / single | ✓ |
| gas | `MATTER(=+5) \| o` | air / gas / wind | ~ |
| steam | `MATTER(=+3) HEAT(=+3) \| o` | steam / vapor / smoke | ✓ |
| breathe | `CONSUME(=0) MATTER(=+5) LIVE \| i` | breathe / inhale / smoke | ✓ |

## Набор B1 (с изменениями)

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| stone | `GRAIN(=+5) THING(=-5) \| o` | stone / rock / brick | ✓ |
| ice | `GRAIN(=+5) HEAT(=-5) \| o` | ice / frost / glacier | ✓ |
| scissors | `JOIN(=-4) MANY(=2) DO(=+5) \| o` | scissors / shears / knife | ✓ |
| steam | `GRAIN(=-5) HEAT(=+2) \| o` | steam / vapor / smoke | ✓ |
| thermometer | `MEASURE HEAT DO(=+5) \| o` | thermometer / thermostat / heater | ✓ |
| hammer | `TOUCH(=+5) MOVE(=+4) DO(=+5) \| o` | hammer / club / bullet | ✓ |
| liquid | `GRAIN(=-3) \| o` | water / liquid / milk | ~ |
| unique | `SAME(=-5) \| a I+5` | different / unique / opposite | ~ |
| sand | `GRAIN(=0) THING(=-5) \| o` | sand / flour / dust | ✓ |
| brush | `TOUCH(=-3) MOVE DO(=+5) \| o` | brush / broom / sponge | ✓ |
| universal | `SAME(=+5) MANY(=+5) \| a I+5` | universal / all / every | ✓ |
| general | `SAME(=+4) MANY(=+4) \| a` | common / general / universal | ~ |
| especially | `SAME(=-4) \| e I+4` | especially / particularly / very | ✓ |
| spoon | `CONSUME(=+5) GRAIN(=-3) DO(=+5) \| o` | cup / glass / straw |  |
| gas | `GRAIN(=-5) \| o` | gas / air / smoke | ✓ |
| flour | `GRAIN(=0) CONSUME(=+5) \| o` | rice / cereal / wheat |  |
| broom | `JOIN(=-4) PLACE DO(=+5) \| o` | shovel / spade / plow |  |
| saw | `JOIN(=-4) MOVE(=+1) DO(=+5) \| o` | saw / axe / knife | ✓ |
| specific | `SAME(=-4) KNOW(=+5) \| a` | famous / known / unique |  |
| needle | `LONG(=-1) JOIN(=+3) DO(=+5) \| o` | nail / screw / glue |  |
| breathe | `CONSUME(=+5) GRAIN(=-5) LIVE \| i` | breathe / inhale / live | ✓ |
| typical | `SAME(=+4) PART(=-2) \| a` | typical / average / member | ✓ |
| smoke | `GRAIN(=-5) HEAT(=+5) \| o` | flame / fire / smoke | ~ |
| exception | `SAME(=-4) JOIN(=-5) RULE \| o` | exception / crime / rebel | ✓ |
| rare | `MANY(=1) \| a` | few / some / little |  |
| pen | `TEXT DO(=+5) \| o` | pen / pencil / keyboard | ✓ |
| water | `GRAIN(=-3) CONSUME(=+5) \| o` | drink / beverage / water | ~ |
| knife | `JOIN(=-4) DO(=+5) \| o` | knife / scissors / axe | ✓ |
| detail | `PART(=-3) KNOW \| o` | fact / idea / detail | ~ |
| key | `INSIDE(=+4) CAN(=+4) DO(=+5) \| o` | key / door / tool | ✓ |
| honey | `GRAIN(=-3) CONSUME(=+5) GOOD(=+4) \| o` | wine / juice / tea |  |
| individual | `SAME(=-4) PART(=-2) \| a` | individual / single / particular | ✓ |
| melt | `CHANGE(=+4) GRAIN(=-3) HEAT(=+3) \| i` | melt / boil / dissolve | ✓ |
| special | `SAME(=-4) \| a` | special / unique / strange | ✓ |
| ladder | `MOVE ABOVE(=+4) DO(=+5) \| o` | ladder / elevator / crane | ✓ |
| ordinary | `SAME(=+3) \| a` | usual / normal / regular |  |

## Набор B2 (с изменениями)

| слово | код | ответ декодера | |
| :-- | :-- | :-- | :-: |
| exception | `SAME(=-4) JOIN(=-5) RULE \| o` | exception / outlaw / freedom | ✓ |
| melt | `CHANGE(=+4) HEAT(=+3) GRAIN(=-3) \| i` | melt / boil / dissolve | ✓ |
| stone | `GRAIN(=+5) THING(=-5) \| o` | stone / rock / brick | ✓ |
| detail | `PART(=-3) SEE \| o` | eye / pupil / glance |  |
| broom | `JOIN(=-4) PLACE DO(=+5) \| o` | wall / fence / door |  |
| hammer | `TOUCH(=+4) MOVE(=+4) DO(=+5) \| o` | hammer / bullet / arrow | ✓ |
| ice | `GRAIN(=+5) HEAT(=-5) \| o` | ice / frost / snow | ✓ |
| sand | `GRAIN(=0) THING(=-5) \| o` | sand / dust / gravel | ✓ |
| typical | `SAME(=+4) MANY(=+3) \| a` | common / similar / usual |  |
| unique | `SAME(=-5) \| a I+4` | different / opposite / strange |  |
| smoke | `GRAIN(=-5) HEAT(=+5) \| o` | fire / steam / smoke | ~ |
| breathe | `CONSUME(=+5) GRAIN(=-5) LIVE \| i` | breathe / inhale / smoke | ✓ |
| needle | `LONG(=0) JOIN(=+3) DO(=+5) \| o` | nail / pin / rod |  |
| ladder | `MOVE(=+2) ABOVE(=+4) DO(=+5) \| o` | ladder / elevator / stairs | ✓ |
| general | `SAME(=+4) MANY(=+5) \| a` | general / universal / every | ✓ |
| water | `GRAIN(=-3) CONSUME(=+5) LIVE \| o` | water / milk / drink | ✓ |
| key | `CAN(=+4) INSIDE(=+4) DO(=+5) \| o` | box / bag / pocket |  |
| specific | `SAME(=-3) KNOW(=+5) \| a` | famous / unusual / familiar |  |
| especially | `SAME(=-4) \| e I+4` | especially / particularly / extremely | ✓ |
| pen | `TEXT DO(=+5) \| o` | pen / pencil / book | ✓ |
| honey | `GRAIN(=-3) CONSUME(=+5) GOOD(=+4) \| o` | wine / juice / soup |  |
| spoon | `CONSUME(=+5) GRAIN(=-3) DO(=+5) \| o` | cup / glass / straw |  |
| gas | `GRAIN(=-5) \| o` | gas / air / smoke | ✓ |
| knife | `JOIN(=-4) TOUCH(=+4) DO(=+5) \| o` | knife / axe / saw | ✓ |
| saw | `JOIN(=-4) MOVE(=+2) DO(=+5) \| o` | saw / scissors / razor | ✓ |
| ordinary | `SAME(=+3) \| a` | ordinary / normal / usual | ✓ |
| rare | `MANY(=+1) \| a` | few / some / little |  |
| universal | `SAME(=+5) MANY(=+5) PLACE \| a` | universal / global / everywhere | ✓ |
| scissors | `JOIN(=-4) MANY(=+1) DO(=+5) \| o` | scissors / filter / sieve | ✓ |
| individual | `SAME(=-4) PART(=-2) \| a` | individual / particular / single | ✓ |
| liquid | `GRAIN(=-3) \| o` | liquid / water / oil | ✓ |
| flour | `GRAIN(=0) CONSUME(=+5) THING(=0) \| o` | flour / rice / sugar | ✓ |
| special | `SAME(=-4) \| a` | unique / special / different | ~ |
| steam | `GRAIN(=-5) HEAT(=+3) \| o` | steam / vapor / smoke | ✓ |
| thermometer | `MEASURE HEAT DO(=+5) \| o` | thermometer / thermostat / heater | ✓ |
| brush | `TOUCH(=-4) MOVE DO(=+5) \| o` | brush / broom / sponge | ✓ |
