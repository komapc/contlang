# Лестница на оси PART: частица — часть — целое — группа

Ось PART расширена: −5 крошка, −2 часть / член, +2 целое / «полностью», +5 группа. Один слепой декодер видел спецификацию с новой шкалой, но не слова; коды писал я.

| # | код | хотел | декодировано |
| --: | :-- | :-- | :-- |
| 1 | `SOMEONE PART(=+5) \| o` | society / group of people | society [community; humanity; team] |
| 2 | `PART(=+5) \| o` | group, set, union | set [collection; group; union] |
| 3 | `SOMEONE PART(=-2) \| o` | member | member [participant; colleague; associate] |
| 4 | `PART(=-5) \| o` | crumb | crumb [particle; speck; grain] |
| 5 | `PART(=+2) \| a` | whole (adj) | whole [entire; complete; full] |
| 6 | `PART(=+2) \| o` | whole (noun) | whole [totality; entirety; unit] |
| 7 | `PLACE RULE PART(=+5) \| o` | union of states | state [country; nation; government] |
| 8 | `THING(=0) PART(=+5) \| o` | herd, grove | herd [flock; crowd of things; bunch] |
| 9 | `PART(=+2) \| e` | entirely | entirely [completely; wholly; totally] |
| 10 | `SOMEONE PART(=+3) \| o` | family / population | family [crowd; population; people] |

Читается всё (10 из 10): *crumb, member, whole, entirely, set / group, society, herd*. №7 (`PLACE RULE PART(=+5)`) прочитан как *state / country* вместо *union* и №10 (`SOMEONE PART(=+3)`) как *family / population* — между +2 и +5 шкала даёт расплывчатые «семья, народ». Ограничения: один декодер, коды писал я, не независимый кодировщик. Нужен повторный тест с независимыми кодировщиками на словах *group, union, class, party, team, committee, society, forest, fleet*.
