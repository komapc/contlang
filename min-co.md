# min-co

**min-co** (*minimal + continuous*) — минимальный непрерывный философский язык (artlang) для точной и гибкой мысли.

Источник: Google Doc «min-co» (апрель 2025). Здесь — перенос в Markdown с правками.

## Философия

- Минимум грамматики и словаря (вдохновлено Toki Pona).
- Максимум выразительности через непрерывные семантические признаки.
- Понятия — не категории, а позиции в концептуальном пространстве.
- Текучесть вместо дискретности, нюанс вместо ярлыка.

## Принципы

1. **Минимальные корни.** Небольшой набор абстрактных корней (`GO`, `HUM`, `DOM`, ...). Сложные идеи — комбинации и модификации корней.
2. **Непрерывные признаки.** Слово — это вызов функции с параметрами: `DOM(SIZE=3)` — большой дом, `GO(TENSE=-2)` — пошёл, `HUM(QUANTITY=5)` — все люди.
3. **Признаки необязательны.** Если признак не указан, он **не важен** (не задан, а не «нейтральный 0»). `GO` без признаков — «идти» в самом общем смысле. Нейтральное значение (`0`) нужно писать явно, если оно семантически значимо.
4. **Минимальная грамматика.** Частицы из Toki Pona, вложенные и композиционные конструкции:
   - `LI` — маркер сказуемого
   - `E` — прямое дополнение
   - `PI` — группировка модификаторов
   - `LA` — условие / контекстная клауза
5. **Бесконечный словарь.** Слова порождаются на лету как корень + признаки. Фиксированный словарь не нужен.

## Семантические признаки

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

## Примеры

Ошибки оригинала исправлены: в таблице нет признака `VALUE` (есть `COLOR VALUE` и `GOODNESS`), а `QUANTITY=0` — это «many», а не «some».

**All humans are born free and equal.**

```
HUM(QUANTITY=5) LI BE-BORN(TENSE=-2) LA HUM PI AGENCY=5 PI IMPORTANCE=0
```

**Some people fear authority.**

```
HUM(QUANTITY=-3) LI FEAR(INTENSITY=4) E RULE(AGENCY=5)
```

**If someone acts freely, society benefits.**

```
HUM(QUANTITY=-3) LI DO(AGENCY=5, CERTAINTY=4) LA SOCIAL-LIFE LI GROW(GOODNESS=4)
```

> Конкретные числа (`QUANTITY=-3`, `IMPORTANCE=0` для «equal») — моя интерпретация, шкалы пока не откалиброваны.

## Структура слова (прототип)

Корни можно менять повтором гласной или аффиксами:

- Повтор гласной = интенсивность значения: `DOM-T-a`, `DOM-T-aa`, `DOM-T-aaa` — дом возрастающего размера.
- Пара T/D задаёт направление признака (T = +, D = -): `GO-T-aa` — идти в будущее, `GO-D-aa` — в прошлое.

Открытый вопрос: 11 уровней на признак плохо ложатся на схему «повтор гласной».

## Открытые вопросы

- Дублирующиеся оси: CERTAINTY / SURENESS, SPATIALITY / DEIXIS, QUANTITY / DISCRETENESS.
- COLOR HUE — круг, а не линия; центр EMOTION NEG («nervous») неочевиден как нейтраль.
- Фонетическая схема кодирования признаков.
- Калибровка шкал (какие числа соответствуют якорям «some», «all» и т.д.).

## Планы

- Глоссатор: разбор фраз min-co в английские глоссы.
- Генератор текста: из семантических графов в линейный язык.
- Синтезатор произношения: звуковые значения для признаков.
- Подсветка грамматики: частицы и вложенность.
- Уточнение списка корней, диаграмма признаков, корпус переводов, числительные и счёт.
