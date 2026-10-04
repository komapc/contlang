# Корень TONE (грубо … вежливо): слепой тест

16 слов, два независимых кодировщика (видели только спецификацию), два декодера. Оценки мои.

| слово | код A | → A | код B | → B |
| :-- | :-- | :-- | :-- | :-- |
| polite | `TONE(=+3) \| a` | polite | `TONE(=+4) \| a` | polite |
| rude | `TONE(=-3) \| a` | rude | `TONE(=-4) \| a` | rude |
| kind | `TONE(=+3) CARE(=+3) \| a` | tactful (рядом: considerate) | `CARE(=+3) TONE(=+4) \| a` | courteous (рядом) |
| harsh | `TONE(=-4) TOUCH(=+4) \| a` | harsh | `TONE(=-5) TOUCH(=+4) \| a` | harsh |
| warm | `TONE(=+4) HEAT(=+2) \| a` | warm | `TONE(=+5) HEAT(=+3) \| a` | warm |
| cold | `TONE(=-4) HEAT(=-3) \| a` | cold | то же | cold |
| sincere | `TONE(=+5) SAME(=+5) \| a` | sincere | `FEEL SAME(=+5) TONE(=+5) \| a` | sympathetic (мимо) |
| courteous | `TONE(=+4) CARE(=+3) RULE(=+2) \| a` | formal (запасным courteous) | `TONE(=+4) CARE(=+3) \| a` | tactful (рядом) |
| hostile | `TONE(=-5) FIGHT \| a` | hostile | то же | hostile |
| blunt | `TONE(=-2) CARE(=-3) \| a` | tactless (близко) | `SAY CARE(=-4) TONE(=-2) \| a` | blunt |
| tactful | `TONE(=+3) CARE(=+5) \| a` | considerate (рядом) | `SAY CARE(=+4) TONE(=+3) \| a` | diplomatic (запасным tactful) |
| friendly | `TONE(=+4) WANT(=+3) \| a` | friendly | `TONE(=+4) NEAR(=+4) \| a` | friendly |
| politely | `TONE(=+3) \| e` | politely | `TONE(=+4) \| e` | politely |
| rudely | `TONE(=-3) \| e` | rudely | `TONE(=-4) \| e` | rudely |
| coldly | `TONE(=-4) HEAT(=-3) \| e` | coldly | то же | coldly |
| cordially | `TONE(=+5) HEAT(=+2) \| e` | warmly (запасным cordially) | `TONE(=+5) CARE(=+2) HEAT(=+3) \| e` | warmly (запасным cordially) |

Итого из 32 прочтений: верно или близким синонимом 26, рядом 5 (*kind, courteous, tactful* путаются между собой), мимо 1 (*sincere* → *sympathetic*).

- Полюса читаются безупречно: *polite, rude, harsh, warm, cold, hostile, friendly* и все четыре наречия.
- Оттенки внутри «вежливого» полюса (*kind, courteous, tactful, considerate*) сливаются; различить их ось не помогает, но смысл «вежливо, внимательно» сохраняется.
- Работают приёмы: *harsh* = `TONE(-) TOUCH(+)`, *cold / warm* = `TONE` + `HEAT`, *hostile* = `TONE(-5) FIGHT`, *friendly* = `TONE(+4)` + `WANT` или `NEAR`, *tactful / blunt* = `TONE` + `CARE` (+ `SAY`).
