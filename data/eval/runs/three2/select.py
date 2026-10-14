# Умный выбор 2-го и 3-го слова (и головы) моделью читателя (proxy.py, обучена без 188 слов теста, proxy_B_heldout.npy).
# Оценка набора: cos(n(p(голова)) + β·Σ w_k·n(p(слово_k)), цель) − 0,01 за каждое добавленное слово; β = 0,35 (по ../three: лучшее 0,25–0,5).
# Строения: плоское (A L B L C: w_B = w_C = 1) и вложенное (A L (B L C): C уточняет B, w_C = 0,5). Связка — по ребру ConceptNet
# между уточняемым и уточняющим словом (PartOf / AtLocation / HasA⁻¹ → PI, UsedFor → FOR, MadeOf → FROM), иначе LIKE.
# Кандидаты слов: 150 ближайших к цели по cos (Numberbatch) среди кодов кодера сайта (pool: enc*.json, ../swap/remove.json, ../three/pool.json) той же части речи, не того же корня, не синонимы.
#   S  — нынешняя голова + до 2 слов;  HS — голова из 8 кандидатов математики (heads.json) + до 2 слов.   python select.py SCRATCH → codes.json
import json, re, sys, os, collections, numpy as np
from nltk.corpus import wordnet as wn
from proxy import feats, vec, LINK, X, ix, D, W
SP = sys.argv[1]; R = f"{D}/../../../.."; BETA, PEN, NEST = 0.35, 0.01, 0.5
B = np.load(f"{D}/proxy_B_heldout.npy"); n = lambda v: v / (np.linalg.norm(v) + 1e-9); p = lambda c: n(feats(c) @ B)
pool = {}
for k in range(4): pool.update(json.load(open(f"{SP}/enc{k}.json")))
pool.update({w: o["code"] for w, o in json.load(open(f"{D}/../swap/remove.json")).items()})
for o in json.load(open(f"{D}/../three/pool.json")).values(): pool.update({a: c for a, c, _ in o["anchors"]})
pos = lambda c: (re.search(r"\|\s*([oiae])\b", c) or [0, None])[1]
pool = {w: c for w, c in pool.items() if w in ix and pos(c) and not LINK.search(c) and not c.startswith('"')}
PW = list(pool); PV = np.stack([p(pool[w]) for w in PW]); PP = np.array([pos(pool[w]) for w in PW])
g = json.load(open(f"{R}/data/raw/conceptnet/graph.json")); REL = g["rel"]; TY = {"PartOf": "PI", "AtLocation": "PI", "UsedFor": "FOR", "MadeOf": "FROM"}
E = {}
for a, b, r, wt in g["edges"]:
    r = REL[r]
    if r in TY and wt >= 1: E.setdefault((W[a], W[b]), TY[r])
    if r == "HasA" and wt >= 1: E.setdefault((W[b], W[a]), "PI")
link = lambda x, y: E.get((x, y), "LIKE")
syn = lambda w: {l.name().lower() for s in wn.synsets(w) for l in s.lemmas()} | {w}
H = json.load(open(f"{SP}/heads.json")); C3 = json.load(open(f"{D}/../three/codes.json")); out = {}
XV = np.stack([X[ix[x]] for x in PW]); NB = 150  # кандидаты — 150 ближайших к цели по смыслу (Numberbatch)
PT = PV @ PV.T  # cos(p, p) между кандидатами — для векторной оценки пар
PSYN = [syn(x) for x in PW]; P5 = np.array([x[:5] for x in PW])
def best_words(hc, t, w):
    """лучшее из: голова одна; + 1 слово; + 2 слова плоско; + 2 слова вложенно (жадно, 60 лучших первых слов)"""
    sw = syn(w); ok = np.array([PP[i] == pos(hc) and PW[i][:5] != w[:5] and w not in PW[i] and PW[i] not in sw and w not in PSYN[i] for i in range(len(PW))])
    near = XV @ t; ok &= near >= np.sort(near)[-NB]
    ph = p(hc); ht, hb, pt = float(ph @ t), PV @ ph, PV @ t
    s1 = np.where(ok, (ht + BETA * pt) / np.sqrt(1 + 2 * BETA * hb + BETA ** 2), -9)
    best = (ht, hc, [])
    for i in np.argsort(-s1)[:60]:
        b = PW[i]; c1 = float(s1[i]) - PEN
        if c1 > best[0]: best = (c1, f"{hc} {link(w, b)} {pool[b]}", [b])
        u = ph + BETA * PV[i]; uu, ut, ub = float(u @ u), float(u @ t), hb + BETA * PT[i]
        for wC, nest in ((1.0, False), (NEST, True)):
            k = BETA * wC; v2 = (ut + k * pt) / np.sqrt(uu + 2 * k * ub + k * k); v2 = np.where(ok, v2, -9); v2[i] = -9; v2[P5 == b[:5]] = -9
            j = int(np.argmax(v2)); c2 = float(v2[j]) - 2 * PEN; cw = PW[j]
            if c2 > best[0]:
                code = f"{hc} {link(w, b)} ( {pool[b]} {link(b, cw)} {pool[cw]} )" if nest else f"{hc} {link(w, b)} {pool[b]} {link(w, cw)} {pool[cw]}"
                best = (c2, code, [b, cw] + (["nested"] if nest else []))
    return best
for w in sorted(C3):
    t = X[ix[w]]; a = C3[w]["A"]; sA = float(p(a) @ t)
    S = best_words(a, t, w)
    heads = [a] + [h for h in H.get(w, {}).get("top", []) if h != a]; hs = max(heads, key=lambda h: float(p(h) @ t))
    HS = best_words(hs, t, w)
    out[w] = {"A": a, "S": S[1], "HS": HS[1], "sA": round(sA, 3), "sS": round(S[0], 3), "sHS": round(HS[0], 3), "wS": S[2], "wHS": HS[2], "W3": C3[w]["W3"]}
json.dump(out, open(f"{D}/codes.json", "w"), indent=0, ensure_ascii=False)
v = list(out.values()); c = collections.Counter(len([x for x in o["wS"] if x != "nested"]) for o in v)
print("ожидаемый cos с целью A / S / HS:", np.mean([o["sA"] for o in v]).round(3), np.mean([o["sS"] for o in v]).round(3), np.mean([o["sHS"] for o in v]).round(3))
print("S: добавлено слов", dict(c), "вложенных", sum("nested" in o["wS"] for o in v), "; HS: голова сменилась у", sum(o["HS"].split("|")[0] != o["A"].split("|")[0] for o in v))
print("связки в S:", collections.Counter(re.findall(r"\b(PI|FOR|FROM|LIKE)\b", " ".join(o["S"] for o in v))))
