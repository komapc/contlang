# Форма и смысл (numberbatch, 3000 слов, частотность вычтена)

Форма: 3 LDA-направления по частям речи (train). Смысл: PCA+varimax в ортогональном дополнении к форме. Сравнение при одинаковой длине кода.

Форма сама по себе предсказывает часть речи на test: **90%** (базовый уровень 33%).

- **leakage** — точность предсказания части речи только по смысловым координатам (меньше = чище);
- **coherence** — связность полюсов смысловых осей (в raw-пространстве; случайные слова ≈ 0.04);
- **wup / pos / top50** — round trip по всему коду (форма + смысл).

| схема | длина кода | leakage | coherence | wup | pos | top50 |
| :-- | --: | --: | --: | --: | --: | --: |
| plain | 10 | 82% | 0.326 | 0.379 | 64% | 48% |
| split (3+7) | 10 | 39% | 0.321 | 0.389 | 68% | 46% |
| plain | 30 | 85% | 0.265 | 0.443 | 75% | 89% |
| split (3+27) | 30 | 54% | 0.271 | 0.449 | 76% | 86% |

## Форма: 3 оси (слова на полюсах)

1. **−** plainly, practically, subsequently, mildly, similarly, largely, presently, consequently  /  **+** give, seek, invoke, summon, assign, ask, arrange, appoint
2. **−** peculiar, vivid, practical, severe, intelligent, logical, formidable, vigorous  /  **+** come, move, give, bring, tell, raise, turn, reflect
3. **−** significant, nice, serious, strong, big, obvious, major, great  /  **+** guy, attitude, aspect, image, scene, element, thing, location

## Смысловые оси при коде 10 (7 осей смысла)

1. **−** specify, determine, define, entail, pursuant, pertain, affirm, establish  /  **+** roar, swoop, gasp, shiver, shudder, scream, heave, slam
2. **−** complete, subtract, minimum, off, eliminate, remove, total, maximum  /  **+** concern, uneasy, resent, regard, regret, wonder, particularly, admire
3. **−** educate, help, collaborate, strengthen, foster, promote, assist, vigorously  /  **+** suppose, probably, guess, though, presume, presumably, reckon, anyway
4. **−** later, after, impatiently, late, postpone, anxiously, before, thereafter  /  **+** uniquely, truly, perfectly, really, pretty, incredibly, absolutely, beautifully
5. **−** assuredly, hope, surely, believe, finally, concede, absolutely, glad  /  **+** vary, various, mainly, specific, primarily, different, variety, nonspecific
6. **−** greater, tremendous, enormous, considerable, increase, huge, bigger, considerably  /  **+** notify, designate, instruct, briefly, inform, report, shortly, morning
7. **−** achieve, happen, occur, attain, accomplish, emerge, realize, possible  /  **+** denounce, reject, endorse, unanimously, condemn, approve, plead, refuse

## Для сравнения: plain, 10 осей

1. **−** truly, incredibly, perfectly, absolutely, extremely, totally, fantastic, excellent  /  **+** linger, reappear, interrupt, precede, falter, disturb, disappear, occur
2. **−** pursuant, relevant, requirement, evaluate, consideration, regard, assess, specify  /  **+** knock, rip, tear, slam, throw, heave, off, slap
3. **−** concede, insist, admit, accept, surely, believe, deem, hope  /  **+** characteristic, geometric, density, variation, measurement, pattern, structure, diameter
4. **−** item, description, interview, report, owner, thing, substitute, dinner  /  **+** greater, bigger, considerable, larger, increase, significantly, considerably, massive
5. **−** concern, sad, uneasy, strange, profound, peculiar, wonder, emotion  /  **+** arrange, remove, assemble, dispose, terminate, eliminate, proceed, finish
6. **−** though, presumably, probably, latter, nevertheless, anyway, anyhow, similarly  /  **+** educate, uphold, protect, strengthen, foster, help, strive, maintain
7. **−** happen, occur, realize, discover, achieve, accomplish, find, emerge  /  **+** unanimously, heartily, recommendation, commission, committee, angrily, solemnly, sanction
8. **−** represent, portray, characterize, depict, describe, include, relate, contain  /  **+** soon, after, shortly, thereafter, later, impatiently, anxiously, hour
9. **−** incredible, fantastic, tremendous, extraordinary, great, magnificent, wonderful, remarkable  /  **+** cautiously, firmly, gently, deliberately, mildly, conversely, accordingly, quietly
10. **−** numerous, prominently, various, promptly, several, brilliantly, repeatedly, prominent  /  **+** guess, believe, suppose, think, belief, reckon, assumption, faith