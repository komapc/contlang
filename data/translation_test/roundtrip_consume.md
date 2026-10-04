# Ось CONSUME (выделить … поглотить): слепой тест

16 глаголов, два независимых кодировщика (видели только спецификацию с новой осью), два декодера. Ось предложена пользователем: приём ↔ выдача (есть / испражняться, читать / писать, слушать / говорить). Оценки мои.

| слово | код A | → A | код B | → B |
| :-- | :-- | :-- | :-- | :-- |
| eat | `CONSUME(=+5) MATTER(=-5)` | eat | то же | eat |
| drink | `CONSUME(=+5) MATTER(=0)` | drink | то же | drink |
| swallow | `CONSUME(=+5) BODY MOVE(=-1)` | chew (запасным swallow) | `CONSUME(=+5) INSIDE(=+5) BODY` | swallow |
| devour | `CONSUME(=+5) MATTER(=-5) WANT(=+5)` | devour | то же | hunger (рядом) |
| excrete | `CONSUME(=-5) BODY` | excrete | `CONSUME(=-5) BODY MATTER(=-2)` | defecate |
| spit | `CONSUME(=-5) MATTER(=0) INSIDE(=-5)` | urinate (мимо) | `CONSUME(=-5) MATTER(=0) SAY` | spit |
| vomit | `CONSUME(=-5) BODY ABOVE(=+3)` | vomit | `CONSUME(=-5) MATTER(=0) ABOVE(=+3)` | vomit |
| inhale | `CONSUME(=+5) MATTER(=+5)` | inhale | то же | inhale |
| exhale | `CONSUME(=-5) MATTER(=+5)` | exhale | то же | exhale |
| read | `CONSUME(=+5) SEE` | watch (мимо) | то же | read |
| write | `CONSUME(=-5) SEE` | show (мимо) | то же | show (мимо) |
| listen | `CONSUME(=+5) SAY CARE(=+3)` | listen | то же | listen |
| speak | `CONSUME(=-5) SAY` | speak | то же | speak |
| absorb | `CONSUME(=+5) INSIDE(=+4)` | absorb | `CONSUME(=+5) INSIDE(=+5)` | absorb |
| emit | `CONSUME(=-5) HEAT` | radiate (запасным emit) | то же | radiate (запасным emit) |
| consume | `CONSUME(=+5) MANY(=+5)` | consume | `CONSUME(=+5) PART(=+2)` | devour (запасным consume) |

Итого из 32 прочтений: верно или близким синонимом 26, запасным 1, мимо 5.

- Ось работает на еде и дыхании (*eat, drink, inhale, exhale, vomit, excrete, absorb*) и на речи (*listen, speak*): направление «внутрь / наружу» декодеры различают уверенно.
- Слабое место — письменное: *write* (`CONSUME(=-5) SEE`) читается как *show*, *read* (`CONSUME(=+5) SEE`) как *watch* у одного из двух декодеров. Канал «текст» нужен отдельным корнем или принять потерю.
- *Spit* кодируется через `INSIDE(=-5)` ненадёжно (один декодер прочитал *urinate*).
