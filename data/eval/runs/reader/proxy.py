# Предсказывает ли модель читателя оценку судьи? Для каждого чтения: прочтённый вектор кода g, близость cos(g, слово).
# Мерим: AUC «близко» по всем чтениям и средняя по словам корреляция Спирмена между вариантами (это и нужно кодеру — выбрать код для слова).
import json, os, sys, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import lib
from scipy.stats import spearmanr, rankdata
D = lib.D; R = json.load(open(f"{D}/readings.json")); LAB = json.load(open(f"{D}/labels.json"))
m = json.load(open(f"{lib.REPO}/site/data/math.json")); MC, MA = np.array(m["dict"]["C"]), np.array(m["dict"]["A"]); MI = {n: i for i, n in enumerate(m["names"])}
V = lib.vecs({o["w"] for o in R})
gloss = lambda c, **k: lib.gloss(V, c, **k)
def mathy(code):
    rs, _, _ = lib.parse(code); y = 0
    for k, (r, v) in enumerate(rs[:3]): y = y + (1 if k == 0 else m["head_w"]) * (MC[MI[r]] + m["s"] * (v or 0) * MA[MI[r]])
    return y / np.linalg.norm(y)
lab = np.array([LAB[f"{o['w']}\t{o['ans'][0] if o['ans'] else '—'}"] for o in R])
def evalp(name, f):
    s = np.array([float(f(o["code"]) @ V[o["w"]]) for o in R]); y = (lab == 2).astype(float)
    auc = (rankdata(s)[y == 1].sum() - y.sum() * (y.sum() + 1) / 2) / (y.sum() * (len(y) - y.sum()))
    ws = {}; 
    for o, si, li in zip(R, s, lab): ws.setdefault(o["w"], {}).setdefault(o["v"], []).append((si, li))
    rho = [spearmanr([np.mean([a for a, _ in x]) for x in d.values()], [np.mean([b for _, b in x]) for x in d.values()])[0] for d in ws.values()]
    rho = [r for r in rho if r == r]
    print(f"{name}: AUC {auc:.3f}, корреляция внутри слова {np.mean(rho):.3f} (по {len(rho)} словам)")
    return s
evalp("математика cos(y, x)", mathy)
evalp("читатель по спецификации", lambda c: gloss(c, plain_mix=0))
evalp("  + голый корень в значении 0,5", gloss)
evalp("  веса 1/1/1", lambda c: gloss(c, w=(1, 1, 1)))
evalp("  веса 1/.4/.3", lambda c: gloss(c, w=(1, .4, .3)))
