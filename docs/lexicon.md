# Словарь

Фиксированного словаря нет: слова порождаются как **корень + суффикс + признаки** ([синтаксис](syntax.md)). Ниже — рабочая схема, полученная экспериментами на английском (ConceptNet Numberbatch, 3000 слов; метрики и сравнения в [плане](plan.md)). Всё здесь **рабочая гипотеза**, а не окончательный словарь.

## Структура кода слова

| Часть | Что это | Размер |
| :-- | :-- | :-- |
| корень | одно из ~30 общих понятий, не привязанных к части речи | log2(30) ≈ 5 бит |
| суффикс | `-o`, `-i`, `-a`, `-e` | 2 бита |
| признаки | универсальные оси, значения -5..+5 (11 уровней); порядка 6–9 осей, корень может использовать часть из них | ≈ 3.5 бита на ось |

При такой схеме (30 корней + суффикс + 6 осей, 27.7 бит на слово) ближайшее по смыслу и форме слово находится заметно лучше, чем при глобальных осях той же длины (8 осей): top50 66% против 39%.

## Корни

Корни выбираются жадно: среди общих слов (по числу гипонимов в WordNet) берутся те, что лучше всего покрывают остальные. Форма (часть речи) предварительно вычитается, чтобы корни не зависели от части речи.

**Нестабильность.** При смене разбиения данных набор корней меняется: в двух запусках совпало около половины (14 из 30). Поэтому корни ниже — рабочий пример, а не окончательный список.

**Устойчивое ядро** (выбрано в обоих запусках):

| Корень | `-o` | `-i` | `-a` | `-e` |
| :-- | :-- | :-- | :-- | :-- |
| THINK | idea, thing | think, suppose | sure, likely | probably, maybe |
| MOVE | movement, motion | move, shift | quick, rapid | forward, swiftly |
| PROVIDE | provision, assistance | provide, furnish | adequate, reliable | helpfully, sufficiently |
| AMOUNT | amount, quantity | expend, allot | total, minimum | roughly, approximately |
| CORRESPOND | address, letter | correspond, coincide | identical, similar | respectively, exactly |
| REGARD | respect, consideration | regard, concern | particular, careful | particularly, especially |
| OCCURRENCE | occurrence, incident | occur, happen | unusual, rare | rarely, seldom |
| NOISE | noise, sound | clamor, roar | loud, shrill | loudly, quietly |
| COLOR | color, shade | paint, stain | purple, blue | vividly, beautifully |
| EXAMINE | examination, study | examine, inspect | analytic, curious | carefully, thoroughly |
| ROOM | room, bedroom | huddle, sit | comfortable, private | upstairs, inside |
| CREATE | form, environment | create, generate | creative, unique | thereby, deliberately |
| COMMITTEE | committee, board | appoint, elect | legislative, municipal | unanimously, formally |

**Остальные корни одного из запусков:** DEFEAT, DESIRE, INCREASE, ROAD, STICK, MIXTURE, EVIDENCE, RESTRAIN, RELIGION, INFORM, COMPANY, CUT, OFFICER, WRITER, WEATHER, DISEASE. В другом запуске вместо них были EMOTION, HIT, REQUEST, AREA, IMPROVE, DESCEND, TERMINATE, FAITH, SOLDIER, ACHIEVEMENT, FASTEN, COMPETE, METAL, FOOD, AUTHOR, OFFICIAL.

**Известные проблемы корней.**
- Часть семей нерегулярна: у *AREA* глагол `-i` — *sprawl, locate*; у *MONTH* глагол `-i` был *march, rent* (теперь снято: месяцы и дни недели идут числами, см. «Послабления»).
- 30 корней — грубое покрытие: *love* попадает в THINK, а не в EMOTION.
- Конверсии (*work, play, love, order*) размечены WordNet как производные формы и получают общий корень (`TOOL-o` / `TOOL-i`); настоящие омонимы (*close* «закрыть» и «близкий») получают разные корни.

## Послабления (слова вне 30 корней)

Часть лексики не имеет смысла кодировать через общие корни и оси. Она выносится за пределы бюджета в 30 корней и не расходует оси:

- **Названия стран** (и вообще имена собственные-топонимы) — заимствуются как есть, без корня и признаков.
- **Числа** — отдельная система счёта, не корни.
- **Месяцы и дни недели** — по номеру: месяц 3, день недели 2 (а не слова *March*, *Tuesday*).

Следствие: корень MONTH больше не нужен, а с ним уходит и ошибка с омонимами *march* (шагать) и *rent* (аренда): их отнесли в MONTH из-за «месячного» контекста. Остаётся открытым, как записывать сами числа, как отличить заимствованное имя от слова языка (метка или фонологический признак) и как склонять/присоединять суффиксы к ним ([фонология](phonology.md)).

## Суффиксы

`-o` имя, `-i` глагол, `-a` признак, `-e` обстоятельство — суффиксы эсперанто. Любой корень берёт любой суффикс (см. [синтаксис](syntax.md)). В экспериментах суффикс стоит 2 бита вместо ~10 бит у трёх непрерывных осей формы при тех же или лучших метриках. Потеряны промежуточные формы (причастия, герундий); они могут вернуться позже как операторы слоя 2 ([план](plan.md)).

## Универсальные смысловые оси

Оси найдены по отклонениям слов от центра своего корня (пулом по всем корням), поэтому значат одно и то же для любого корня. Названий у них пока нет. Ниже — слова на полюсах осей одного из запусков (знак и порядок осей между запусками не стабильны):

| № | полюс − | полюс + |
| :-: | :-- | :-- |
| M1 | fundamental, principle, term, objective, requirement, basic | grateful, shudder, dear, glad, joy, friendly |
| M2 | broad, profound, extensive, impulse, sudden, intensity | oblige, fortunate, lucky, certify, owe, insist |
| M3 | real, truly, genuine, uniquely, wholly, true | impatiently, anxiously, cautiously, nervously, hastily |
| M4 | hereafter, somewhere, forever, eternal, inevitable | tremendously, vastly, impressive, remarkably, big, large |
| M5 | ask, invoke, beckon, lend, invite, borrow | fairly, perfectly, reasonably, extremely, sufficiently |
| M6 | flatly, tax, ratio, totally, wildly, rate | linger, foresee, considerable, farther, significant, emerge |
| M7 | strive, mentally, educate, engage, collaborate | vague, shortly, sadly, nevertheless, mention, notice |
| M8 | stubbornly, exist, stare, falter, underlie | select, arrange, able, ideally, dispose, locate |
| M9 | incredible, brilliant, fantastic, magnificent, remarkable | frequent, tend, sometimes, usually, frequently, mostly |

Честная оценка: оси читаются плохо (степень, манера, оценка, но без чёткой темы), и это главная слабость текущей схемы. Рассматривается замена на оси, заданные по полюсам вручную (*small ↔ large*, *bad ↔ good*, …) с проверкой качества на данных. Одна локальная ось на корень (0/1) прибавляла бы лишь 2–3 пункта точности за +30 осей в описании языка, поэтому не используется.


## Архив: глобальные оси nano-10 (из данных)

Получена экспериментом на английском (Numberbatch, 3000 слов, частотность вычтена): 3 оси формы + 7 смысловых. Подробности и метрики: [план](plan.md), `data/form_meaning_numberbatch.md`. Названия полюсов автоматические (слова с наибольшей нагрузкой); колонка «ярлык» — ручная интерпретация, а не результат метода. Знак и порядок осей зависят от выборки и не стабильны между запусками.

### Форма (части речи как непрерывные координаты)

| № | полюс − | полюс + | ярлык |
| :-: | :-- | :-- | :-- |
| F1 | plainly, practically, subsequently, mildly, similarly, largely | give, seek, invoke, summon, assign, ask | наречие ↔ глагол |
| F2 | peculiar, vivid, practical, severe, intelligent, logical | come, move, give, bring, tell, raise | прилагательное ↔ глагол |
| F3 | significant, nice, serious, strong, big, obvious | guy, attitude, aspect, image, scene, element | прилагательное ↔ существительное |

### Смысл

| № | полюс − | полюс + | ярлык | близкая ручная ось |
| :-: | :-- | :-- | :-- | :-- |
| M1 | specify, determine, define, entail, pursuant, affirm | roar, swoop, gasp, shiver, scream, slam | формальное определение ↔ физическая экспрессия | — |
| M2 | complete, subtract, minimum, eliminate, remove, total | concern, uneasy, resent, regret, wonder, admire | удаление и полнота ↔ переживание | EMOTION POS / NEG |
| M3 | educate, help, collaborate, strengthen, foster, promote | suppose, probably, guess, presume, reckon, anyway | поддержка ↔ предположение | CERTAINTY |
| M4 | later, after, late, postpone, before, thereafter | uniquely, truly, perfectly, really, pretty, absolutely | время ↔ степень | TENSE, TEMPORALITY |
| M5 | assuredly, hope, surely, believe, finally, concede | vary, various, mainly, specific, primarily, variety | уверенность ↔ разнообразие | CERTAINTY, QUANTITY |
| M6 | greater, tremendous, enormous, considerable, huge | notify, designate, instruct, inform, report, briefly | размер и степень ↔ сообщение | SIZE, INTENSITY |
| M7 | achieve, happen, occur, attain, accomplish, realize | denounce, reject, endorse, condemn, approve, refuse | свершение ↔ оценка и отказ | GOODNESS (смутно) |

Ярлыки у M1, M5 и M7 слабые: полюса смешанные. Чёткие оси: F1–F3, M2, M3, M4, M6.

## Архив: исходная гипотеза, 30 ручных признаков

Список ниже составлен вручную до экспериментов. Он используется как гипотеза для сравнения с осями из данных, а не как окончательный набор.

Каждый признак — непрерывная шкала от **-5 до +5**.

| Признак | Спектр |
| :-- | :-- |
| SIZE | tiny ← small ← medium → large → vast |
| TENSE | far past ← recent past ← now → near future → far future |
| GOODNESS | bad ← flawed ← neutral → good → excellent |
| ENERGY | inert ← passive ← stable → active → hyper |
| SPEED | frozen ← slow ← normal → fast → instant |
| INTENSITY | faint ← weak ← average → strong → overwhelming |
| CERTAINTY | unsure ← guess ← probable → certain → obvious |
| FAMILIARITY | unknown ← distant ← neutral → familiar → intimate |
| HUMANNESS | object ← machine ← animal → human → divine |
| TEMPORALITY | ancient ← old ← modern → futuristic → timeless |
| SPATIALITY | far ← yonder ← near → here → internal |
| LIQUIDITY | solid ← gel ← liquid → vapor → formless |
| SHARPNESS | dull ← soft ← crisp → sharp → piercing |
| COLOR VALUE | dark ← muted ← normal → bright → radiant |
| COLOR HUE | red ← orange ← green → blue → purple |
| EMOTION POS | sad ← bored ← neutral → happy → euphoric |
| EMOTION NEG | calm ← uneasy ← nervous → afraid → terrified |
| TOGETHERNESS | alone ← few ← group → crowd → swarm |
| ABSTRACTION | tangible ← concrete ← idea → symbol → metaphysical |
| AGENCY | passive ← dependent ← neutral → active → autonomous |
| DEFINITENESS | vague ← ambiguous ← referenced → definite → specific |
| DEIXIS | far ← that ← here/this → immediate |
| SURENESS | doubtful ← unsure ← probable → confident → evident |
| FORMALITY | playful ← casual ← polite → formal → ceremonial |
| DISCRETENESS | individual ← few ← many → mass → undifferentiated |
| QUANTITY | none ← some ← many → all → universal existence |
| TRUTH | lie ← ironic ← true → sacred |
| IMPORTANCE | trivial ← helpful ← important → vital |
| TIME_SCALE | momentary ← brief ← long → eternal |
| SERIOUSNESS | humorous ← light ← serious → solemn → ritual |
