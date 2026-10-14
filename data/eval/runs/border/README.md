# Как записать «границу»: слепой тест кандидатов

Спецификация с LAND (../adopt3/spec_land.md). 6 кандидатов, по 2 в списке среди 8 чужих кодов (meta.json), 4 слепых читателя Haiku
на список; первые ответы — result.json, ответы целиком — answers/.

| код | первые ответы (4 читателя) |
|---|---|
| `LAND RULE LONG(=-5) \| o` | **border, border, border, border** |
| `SIDE \| o PI LAND RULE \| o` | **border, border, border, border** |
| `LONG(=-5) \| o PI LAND RULE \| o` | border, border, border, strand |
| `PLACE JOIN(=-5) LONG(=-5) \| o` | boundary, boundary, fence, gap |
| `PLACE NEAR LONG(=-5) \| o` | edge, border, roadside, cord |
| `PLACE LONG(=-5) \| o` | path ×4 |

`LAND RULE` — страна, область (земля под властью); `LONG(=-5)` — тонкая линия; `SIDE` — край. Граница вообще (не
государственная) — `PLACE JOIN(=-5) LONG(=-5)` «линия, разделяющая место»: читается как boundary, divide, но слабее.
