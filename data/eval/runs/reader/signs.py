# Знак значения в кодах модели H (|v| ≥ 3): как часто его угадывает выбор по подписям шкалы (spec.md) — без обучения.
# Значение по подписи: v* = argmax_v cos(interp(r, v), x) по v ∈ {−5, −3, 0, +3, +5}; сравниваем знак.
import json, os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lib
items = json.load(open(f"{lib.D}/../taxonomy/items.json")); V = lib.vecs({it["w"] for it in items})
def best_v(x, r, levels=(-5, -3, 0, 3, 5), c=0.0):
    s = {v: float(lib.interp(V, r, v) @ x / np.linalg.norm(lib.interp(V, r, v))) for v in levels}; return max(s, key=s.get), s
n = ok = 0; rows = []
for it in items:
    x = V[it["w"]]
    for r, v in lib.parse(it["H"] or "")[0]:
        if v is None or abs(v) < 3 or not lib.SPEC[r]["axis"]: continue
        b, s = best_v(x, r, (-5, 5)); n += 1; ok += np.sign(b) == np.sign(v)
        if np.sign(b) != np.sign(v): rows.append(f"{it['w']} {r}({v:+d}) → {b:+d}")
print(f"знак по подписям шкалы совпал с моделью {ok}/{n} = {ok / n:.0%}"); print("; ".join(rows[:40]))
# центрированный вариант: разность близостей к полюсам минус её среднее по словарю сайта
W = [w for w in json.load(open(f"{lib.REPO}/site/data/math.json"))["words"][::5] if w in V]; M = np.stack([V[w] for w in W])
n = ok = 0; bad = {}
for it in items:
    x = V[it["w"]]
    for r, v in lib.parse(it["H"] or "")[0]:
        if v is None or abs(v) < 3 or not lib.SPEC[r]["axis"]: continue
        p, q = lib.interp(V, r, 5), lib.interp(V, r, -5); p, q = p / np.linalg.norm(p), q / np.linalg.norm(q)
        d = M @ (p - q); z = (x @ (p - q) - d.mean()) / d.std(); n += 1; ok += np.sign(z) == np.sign(v)
        if np.sign(z) != np.sign(v): bad[r] = bad.get(r, 0) + 1
print(f"центрированно: {ok}/{n} = {ok / n:.0%}", sorted(bad.items(), key=lambda x: -x[1])[:8])
