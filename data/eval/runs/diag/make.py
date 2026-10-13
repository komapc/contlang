# Диагноз: что в кодах модели H несёт смысл. HP — корни H голыми (без значений), HO — H без роли и меток (форма «| o»/«| i»…).
import json, os, re
D = os.path.dirname(os.path.abspath(__file__)); items = json.load(open(f"{D}/../taxonomy/items.json"))
def hp(c): s, _, f = c.partition("|"); return re.sub(r"\(=[^)]*\)", "", s).strip() + " |" + f
def ho(c): s, _, f = c.partition("|"); return s.strip() + " | " + (f.split() or ["o"])[0]
for v, fn in (("hp", hp), ("ho", ho)):
    os.makedirs(f"{D}/{v}", exist_ok=True)
    for k in (1, 2): open(f"{D}/{v}/codes_{k}.md", "w").write("".join(f"{i + 1}. {fn(it['H'])}\n" for i, it in enumerate(items[(k - 1) * 50:k * 50])))
print(sum(hp(it["H"]) != it["H"] for it in items), "кодов меняет HP;", sum(ho(it["H"]) != it["H"] for it in items), "— HO")
