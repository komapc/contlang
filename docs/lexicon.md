# Словарь

Фиксированного словаря нет: слова порождаются как **корень + признаки**.

## Корни

Небольшой набор абстрактных корней. Пока определены в примерах: `GO`, `HUM`, `DOM`, `FEAR`, `RULE`, `DO`, `GROW`, `BE-BORN`, `SOCIAL-LIFE`. Полный список корней ещё предстоит составить.

## Рабочая гипотеза nano-10 (из данных)

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

## Исходная гипотеза: 30 ручных признаков

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
