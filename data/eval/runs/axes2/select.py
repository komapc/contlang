# Шаг 2б: кандидаты-шкалы (два Haiku), оси корней (semaxis roots.yaml и обученные атомы), Осгуд; жадный отбор по покрытию
# при |cos| ≤ 0,3; k = 10, 15, 20.   python select.py SCRATCH → candidates.json, selection.md, chosen.json
import json, re, sys
from pathlib import Path
import numpy as np, yaml
sys.path.insert(0, str(Path(__file__).resolve().parent))
from space import D, Z, X, P, unit, direction, top, words, m, IDX

S = sys.argv[1]; R = D.parents[3]; KS = (10, 15, 20); CMAX = 0.3
cands = []
for src in ("c1", "c2"):
    for line in open(f"{S}/{src}/candidates.md"):
        if not (g := re.match(r"\s*\d+\.\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*$", line)): continue
        neg, pos = g[2].lower().split(), g[3].lower().split()
        cands.append({"src": f"haiku-{src[1]}", "name": g[1], "neg": neg, "pos": pos})
for r in yaml.safe_load(open(R / "roots.yaml"))["roots"]:
    if r.get("semaxis"): cands.append({"src": "roots", "name": r["name"], "pos": r["semaxis"][0].split(), "neg": r["semaxis"][1].split()})
OSG = [("bad - good", "bad awful unpleasant ugly cruel nasty", "good nice pleasant beautiful kind lovely"),
       ("weak - strong", "weak feeble light soft small fragile", "strong powerful heavy hard big mighty"),
       ("passive - active", "passive slow still calm quiet lazy", "active fast lively quick energetic busy")]
cands += [{"src": "osgood", "name": n, "neg": a.split(), "pos": b.split()} for n, a, b in OSG]
for c in cands:
    d, c["np"], c["nn"] = direction(c["pos"], c["neg"]); c["d"] = d
drop = [c for c in cands if c["d"] is None]; cands = [c for c in cands if c["d"] is not None]
# дубли среди новых кандидатов (между собой и с осями корней): |cos| > 0,7 — остаётся ось с большим числом слов-полюсов
new = [c for c in cands if c["src"].startswith("haiku")]; old = [c for c in cands if not c["src"].startswith("haiku")]
kept = []
for c in sorted(new, key=lambda c: -(c["np"] + c["nn"])):
    if all(abs(c["d"] @ k["d"]) <= 0.7 for k in kept): kept.append(c)
RT = [o for o in old if o["src"] == "roots"]
dup_roots = [(c["name"], max(RT, key=lambda o: abs(c["d"] @ o["d"]))["name"]) for c in kept if max(abs(c["d"] @ o["d"]) for o in RT) > 0.7]
new = kept
atoms = [{"src": "atoms", "name": nm, "d": unit(P(np.array(m["dict"]["A"][r])[None])[0])} for r, nm in enumerate(m["names"]) if m["has_axis"][r]]

big = [IDX[w] for w in json.load(open(R / "data/eval/runs/big1000/words.json")) if w in IDX]
pos_in_keep = {w: i for i, w in enumerate(words)}
ZB = Z[[pos_in_keep[w] for w in json.load(open(R / "data/eval/runs/big1000/words.json")) if w in pos_in_keep]]


def cover(B, ZZ=Z):
    if not len(B): return 0.0
    Qs, _ = np.linalg.qr(np.stack(B).T); return float(np.linalg.norm(ZZ @ Qs) ** 2 / np.linalg.norm(ZZ) ** 2)


def ceiling(k, ZZ=Z):
    s = np.linalg.svd(ZZ - ZZ.mean(0), compute_uv=False) ** 2; return float(s[:k].sum() / (np.linalg.norm(ZZ) ** 2))


def greedy(pool, k):
    ch, Qs = [], np.zeros((Z.shape[1], 0))
    for _ in range(k):
        Zr = Z - (Z @ Qs) @ Qs.T; best = None
        for c in pool:
            if c in ch or any(abs(c["d"] @ x["d"]) > CMAX for x in ch): continue
            dr = c["d"] - Qs @ (Qs.T @ c["d"]); nr = np.linalg.norm(dr)
            if nr < 1e-6: continue
            g = float(np.linalg.norm(Zr @ (dr / nr)) ** 2)
            if not best or g > best[0]: best = (g, c, dr / nr)
        if not best: break
        ch.append(best[1]); Qs = np.hstack([Qs, best[2][:, None]])
    return ch


def gram(B):
    G = np.abs(np.stack([b["d"] for b in B]) @ np.stack([b["d"] for b in B]).T) - np.eye(len(B)); n = len(B)
    return (G.max(), G.sum() / (n * n - n)) if n > 1 else (0.0, 0.0)


pools = {"новые": new, "оси корней (semaxis)": [c for c in old if c["src"] == "roots"], "оба": new + [c for c in old if c["src"] == "roots"],
         "атомы корней (обученные)": atoms}
L = ["# Шаг 2б: отбор осей", "", f"Кандидатов от Haiku {sum(c['src'].startswith('haiku') for c in cands)} (после отбрасывания осей с < 5 словами в Numberbatch; "
     f"отброшено {len(drop)}), после слияния дублей |cos| > 0,7 — {len(new)}. Дубли с осями корней (|cos| > 0,7): "
     + (", ".join(f"{a} ≈ {b}" for a, b in dup_roots) or "нет") + ".", "",
     "Покрытие — доля дисперсии очищенных векторов в линейной оболочке набора, в скобках — доля потолка (PCA того же k). "
     "Набор — жадный отбор при |cos| ≤ 0,3.", "",
     "| пул | k | покрытие, 5949 лемм | покрытие, big1000 | наиб. / сред. abs(cos) |", "|---|--:|---|---|---|"]
chosen = {}
for name, pool in pools.items():
    for k in KS:
        ch = greedy(pool, k); B = [c["d"] for c in ch]; chosen[(name, k)] = ch; g = gram(ch)
        L.append(f"| {name} | {len(ch)} | {cover(B):.1%} ({cover(B) / ceiling(len(ch)):.0%}) | {cover(B, ZB):.1%} ({cover(B, ZB) / ceiling(len(ch), ZB):.0%}) | {g[0]:.2f} / {g[1]:.2f} |")
for name, B in (("Осгуд, 3 оси", [c for c in old if c["src"] == "osgood"]), ("все 39 осей корней", [c for c in old if c["src"] == "roots"]), ("все новые", new)):
    g = gram(B); L.append(f"| {name} | {len(B)} | {cover([c['d'] for c in B]):.1%} ({cover([c['d'] for c in B]) / ceiling(len(B)):.0%}) | {cover([c['d'] for c in B], ZB):.1%} | {g[0]:.2f} / {g[1]:.2f} |")
L.append(f"| PCA (потолок) | 20 | {ceiling(20):.1%} | {ceiling(20, ZB):.1%} | 0 |")

roots_d = [c for c in old if c["src"] == "roots"]
for name in ("новые", "оба"):
    ch = chosen[(name, 20)]
    L += ["", f"## Набор «{name}», 20 осей (по порядку отбора)", "", "| # | ось | источник | прирост покрытия | ближайшая ось корня | − полюс (по проекции) | + полюс (по проекции) |", "|---|---|---|--:|---|---|---|"]
    for j, c in enumerate(ch):
        inc = cover([x["d"] for x in ch[:j + 1]]) - cover([x["d"] for x in ch[:j]])
        nr = max(roots_d, key=lambda o: abs(c["d"] @ o["d"])); ex = set(c["pos"]) | set(c["neg"])
        L.append(f"| {j + 1} | {c['name']} | {c['src']} | {inc:.2%} | {nr['name']} {c['d'] @ nr['d']:+.2f} | {', '.join(top(c['d'], 8, -1, ex))} | {', '.join(top(c['d'], 8, 1, ex))} |")
(D / "selection.md").write_text("\n".join(L) + "\n")
json.dump([{k: v for k, v in c.items() if k != "d"} for c in cands], open(D / "candidates.json", "w"), indent=0, ensure_ascii=False)
json.dump({f"{n}|{k}": [c["name"] + "|" + c["src"] for c in v] for (n, k), v in chosen.items()}, open(D / "chosen.json", "w"), indent=0, ensure_ascii=False)
print("\n".join(L[:20]))
