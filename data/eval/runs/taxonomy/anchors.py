# Род по таксономии: полюса спецификации (dec.md) как узлы WordNet. Главный корень слова — корень ближайшего узла среди
# гиперонимов первого смысла (по числу шагов вверх; при равенстве — первый в списке). Значение None — корень без значения.
#   .venv/bin/python data/eval/runs/taxonomy/anchors.py   → heads.json (100 слов ../twowords2 и 300 существительных ../definition/wn.json)
import json, os
from nltk.corpus import wordnet as wn
D = os.path.dirname(os.path.abspath(__file__))
ANCH = [  # (синсет, корень, значение) — из строк спецификации
    ("person.n.01", "SOMEONE", None), ("people.n.01", "SOMEONE", None), ("social_group.n.01", "PART", 5), ("group.n.01", "PART", 5),
    ("animal.n.01", "THING", 4), ("plant.n.02", "THING", 0), ("rock.n.01", "THING", -5), ("mineral.n.01", "THING", -5),
    ("body_part.n.01", "BODY", None), ("illness.n.01", "BODY", None), ("disease.n.01", "BODY", None), ("infection.n.01", "BODY", None), ("body.n.01", "BODY", None),
    ("gas.n.02", "GRAIN", -5), ("liquid.n.01", "GRAIN", -3), ("fluid.n.02", "GRAIN", -3), ("body_of_water.n.01", "GRAIN", -3), ("powder.n.01", "GRAIN", 0), ("metal.n.01", "GRAIN", 5), ("substance.n.01", "GRAIN", None), ("material.n.01", "GRAIN", None),
    ("location.n.01", "PLACE", None), ("structure.n.01", "PLACE", None), ("geological_formation.n.01", "PLACE", None), ("area.n.05", "PLACE", None),
    ("writing.n.02", "TEXT", None), ("document.n.01", "TEXT", None), ("written_communication.n.01", "TEXT", None),
    ("military_action.n.01", "FIGHT", 5), ("war.n.01", "FIGHT", 5), ("dispute.n.01", "FIGHT", 0), ("game.n.01", "FIGHT", -5), ("sport.n.01", "FIGHT", -5), ("contest.n.01", "FIGHT", -5),
    ("time_period.n.01", "TIME", None), ("measure.n.02", "MEASURE", None), ("unit_of_measurement.n.01", "MEASURE", -5),
    ("feeling.n.01", "FEEL", None), ("belief.n.01", "THINK", None), ("cognition.n.01", "THINK", None),
    ("organization.n.01", "RULE", 4), ("institution.n.01", "RULE", 4), ("law.n.02", "RULE", 5), ("rule.n.01", "RULE", 5),
    ("money.n.01", "VALUE", None), ("financial_gain.n.01", "VALUE", None), ("assets.n.01", "VALUE", None),
    ("food.n.01", "CONSUME", 5), ("food.n.02", "CONSUME", 5), ("beverage.n.01", "CONSUME", 5),
    ("art.n.01", "ART", 5), ("music.n.01", "ART", 5), ("container.n.01", "INSIDE", 5), ("device.n.01", "ART", -5), ("instrumentality.n.03", "ART", -5),
    ("speech.n.02", "SAY", 0), ("sound.n.01", "SAY", None), ("communication.n.02", "SAY", None),
    ("fire.n.01", "HEAT", 5), ("particle.n.02", "PART", -5), ("part.n.01", "PART", -2), ("part.n.03", "PART", -2), ("proportion.n.01", "MEASURE", 5), ("gift.n.01", "GIVE", 5), ("change.n.01", "CHANGE", None), ("event.n.01", "HAPPEN", None), ("act.n.02", "DO", None), ("activity.n.01", "DO", None),
    ("transfer.n.06", "GIVE", 5), ("acquisition.n.01", "GIVE", -5), ("commerce.n.01", "GIVE", 0),
]
for s, _, _ in ANCH: wn.synset(s)  # опечатка в имени синсета — сразу ошибка
def head(w):
    ss = wn.synsets(w, "n")
    if not ss: return None
    dist = {ss[0]: 0}; frontier = [ss[0]]
    while frontier:
        nxt = []
        for s in frontier:
            for h in s.hypernyms() + s.instance_hypernyms():
                if h not in dist: dist[h] = dist[s] + 1; nxt.append(h)
        frontier = nxt
    best = None
    for i, (s, r, v) in enumerate(ANCH):
        d = dist.get(wn.synset(s))
        if d is not None and (best is None or (d, i) < best[0]): best = ((d, i), r, v, s)
    return best and {"root": best[1], "v": best[2], "via": best[3], "steps": best[0][0]}
WN = json.load(open(f"{D}/../definition/wn.json"))
out = {w: head(w) for w in WN}
json.dump(out, open(f"{D}/heads.json", "w"), indent=1)
test = [w for w in WN if WN[w]["test"]]
print("с родом:", sum(1 for w in test if out[w]), "/", len(test))
print(", ".join(f"{w}→{out[w]['root']}{'' if out[w]['v'] is None else '(=%+d)' % out[w]['v']}" if out[w] else f"{w}→—" for w in test))
