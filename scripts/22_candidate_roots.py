"""Кандидаты в новые корни поверх 44 нынешних (docs/math.md): что даёт каждый математике.

Для каждого кандидата (полюса — английские слова) словарь из полюсов дополняется
одним корнем, и все отложенные слова кодируются заново точным перебором. Отчёт:
прирост top1/top10 на отложенных словах, место «своих» слов кандидата (на которые
он рассчитан) до и после, сколько кодов его берут, и на какой нынешний корень он
больше всего похож (дубль?). Отдельно — все кандидаты сразу и проверка идеи
«тяжёлое = трудное» (оси heavy–light и difficult–easy).

    .venv/bin/python scripts/22_candidate_roots.py             → data/candidate_roots.md
    .venv/bin/python scripts/22_candidate_roots.py --control   контроль: те же замеры с корнями из случайных слов
"""
import sys
import time
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from common import ROOT  # noqa: E402
from lib_code import Coder, Data, encode_all, metrics, root_specs, unit  # noqa: E402

HW = 0.6
OUT = ROOT / "data" / "candidate_roots.md"

# имя: (+полюс, −полюс, свои слова)
CANDS = {
    "PULL": ("pull drag tug haul draw", "push shove thrust propel press", "rope magnet attract tow pump"),
    "SHARP": ("sharp pointed keen jagged spiky", "blunt dull smooth rounded flat", "knife saw needle blade axe sword cut"),
    "LIGHT": ("bright luminous shining sunny glowing", "dark dim shadowy gloomy murky", "day night lamp shadow sun candle"),
    "HEAVY": ("heavy weighty hefty massive ponderous", "lightweight weightless feathery airy buoyant", "weight stone iron lift float feather burden"),
    "STRONG": ("strong powerful mighty robust forceful", "weak feeble frail fragile powerless", "power energy engine muscle force"),
    "FULL": ("full filled packed crowded loaded", "empty hollow vacant bare blank", "fill hungry container bottle"),
    "HELP": ("help assist support aid benefit", "hinder obstruct impede hamper thwart", "defend protect obstacle rescue"),
    "STRAIGHT": ("straight direct linear upright vertical", "curved bent crooked twisted curly", "line road bend curve ruler"),
    "ORDER": ("orderly organized systematic structured regular", "chaotic messy disorderly random haphazard", "mess organize system chaos list"),
    "CLEAN": ("clean pure spotless tidy fresh", "dirty filthy muddy dusty polluted", "wash soap dirt dust bath"),
    "TRUE": ("true truth honest genuine real", "false lie fake dishonest deceptive", "fact lying myth trust"),
    "FREE": ("free freedom independent liberty unrestricted", "captive bound enslaved confined restricted", "prison slave cage jail allow forbid"),
}
HEAVY_HARD = ("difficult hard arduous tough laborious", "easy effortless simple painless straightforward")


def control():
    """Сколько дают корни со случайными полюсами (слова сайта вне списка 2700) — чтобы отделить смысл от лишних степеней свободы."""
    import json
    wl = {l.split("\t")[0] for l in open(ROOT / "data" / "wordlist_en_x5.tsv")}
    pool = [w for w in json.loads((ROOT / "site" / "data" / "math.json").read_text())["words"] if w.isalpha() and w not in wl]
    rng = np.random.default_rng(1)
    rand = [(f"R{k}", " ".join(rng.choice(pool, 5, replace=False)), " ".join(rng.choice(pool, 5, replace=False)), None) for k in range(12)]
    base = root_specs()
    extra = [(n, p, m, None) for n, (p, m, _) in CANDS.items()]
    d = Data([base, base + extra, [("HARD", *HEAVY_HARD, None)], rand])

    def run(specs):
        names, C, A = d.dictionary(specs)
        r = metrics(d, d.test, np.stack([c[2] for c in encode_all(Coder(C, A, head_w=HW), d.V[d.test])]))["ranks"]
        return np.mean(r == 1), np.mean(r <= 10)
    b = run(base)
    for label, specs in [*((f"один случайный ({x[1]} / {x[2]})", base + [x]) for x in rand[:3]),
                         ("12 случайных", base + rand), ("12 кандидатов", base + extra)]:
        r = run(specs)
        print(f"{label}: Δtop1 {r[0] - b[0]:+.1%}, Δtop10 {r[1] - b[1]:+.1%}", flush=True)


def main():
    if "--control" in sys.argv:
        return control()
    t0 = time.time()
    base = root_specs()
    extra = [(n, p, m, None) for n, (p, m, _) in CANDS.items()]
    d = Data([base, base + extra, [("HARD", *HEAVY_HARD, None)]])  # один словарь узнавания для всех вариантов
    vi = {w: i for i, w in enumerate(d.vocab)}
    own = {n: [vi[w] for w in ws.split() if w in vi] for n, (_, _, ws) in CANDS.items()}
    probes = sorted({i for v in own.values() for i in v})
    idx = np.array(sorted(set(d.test) | set(probes)))
    pos = {i: k for k, i in enumerate(idx)}
    test_mask = np.isin(idx, d.test)

    def run(specs):
        names, C, A = d.dictionary(specs)
        codes = encode_all(Coder(C, A, head_w=HW), d.V[idx])
        Y = np.stack([c[2] for c in codes])
        r = metrics(d, idx, Y)["ranks"]
        return names, C, A, codes, r

    def summary(r):
        t = r[test_mask]
        return {"top1": np.mean(t == 1), "top10": np.mean(t <= 10)}

    names0, C0, A0, codes0, r0 = run(base)
    s0 = summary(r0)
    print(f"база: {s0}  ({time.time() - t0:.0f} с)", flush=True)

    L = ["# Кандидаты в новые корни", "",
         f"Скрипт `scripts/22_candidate_roots.py`. Словарь из полюсов (без обучения), 44 корня; к нему добавляется кандидат, "
         f"и {int(test_mask.sum())} отложенных слов кодируются заново (не больше 3 корней, точный перебор). "
         "«Свои слова» — слова, ради которых кандидат предложен: их место среди ближайших к коду (из "
         f"{len(d.vocab)}) до и после. «Похож на» — нынешний корень с наибольшим |cos| оси (дубль, если близко к 1).", "",
         f"База: top1 {s0['top1']:.1%}, top10 {s0['top10']:.1%}.", "",
         "| кандидат | Δtop1 | Δtop10 | кодов с ним | свои слова: место до → после | похож на (cos оси) |",
         "| --- | --: | --: | --: | --- | --- |"]
    for n, (p, m, _) in CANDS.items():
        names, C, A, codes, r = run(base + [(n, p, m, None)])
        s = summary(r)
        k = names.index(n)
        used = np.mean([k in c[0] for c, tm in zip(codes, test_mask) if tm])
        sims = [(abs(float(unit(A[k]) @ unit(A0[j]))), names0[j]) for j in range(len(names0)) if A0[j].any()]
        sim, sn = max(sims)
        ow = ", ".join(f"{d.vocab[i]} {r0[pos[i]]}→{r[pos[i]]}" for i in own[n])
        L.append(f"| {n} | {s['top1'] - s0['top1']:+.1%} | {s['top10'] - s0['top10']:+.1%} | {used:.0%} | {ow} | {sn} ({sim:.2f}) |")
        print(L[-1], f"({time.time() - t0:.0f} с)", flush=True)

    names, C, A, codes, r = run(base + extra)
    s = summary(r)
    use = {n: np.mean([names.index(n) in c[0] for c, tm in zip(codes, test_mask) if tm]) for n in CANDS}
    L += ["", f"Все 12 сразу (56 корней): top1 {s['top1']:.1%} ({s['top1'] - s0['top1']:+.1%}), "
          f"top10 {s['top10']:.1%} ({s['top10'] - s0['top10']:+.1%}). Доля кодов с кандидатом: "
          + ", ".join(f"{n} {u:.0%}" for n, u in sorted(use.items(), key=lambda x: -x[1])) + "."]
    print(L[-1], flush=True)

    # тяжёлое = трудное?
    _, Ch, Ah = d.dictionary([("HEAVY", *CANDS["HEAVY"][:2], None), ("HARD", *HEAVY_HARD, None)])
    can = A0[names0.index("CAN")]
    Au = unit(A0[A0.any(1)])
    off = np.abs(Au @ Au.T)[np.triu_indices(len(Au), 1)]
    L += ["", "## «Тяжёлое» и «трудное»", "",
          f"cos осей heavy–light и difficult–easy: {float(unit(Ah[0]) @ unit(Ah[1])):.2f}; "
          f"heavy–light и CAN (легко … невозможно): {float(unit(Ah[0]) @ unit(can)):.2f}; "
          f"difficult–easy и CAN: {float(unit(Ah[1]) @ unit(can)):.2f}; "
          f"медиана |cos| между осями нынешних корней: {np.median(off):.2f}."]
    print(L[-1], flush=True)
    OUT.write_text("\n".join(L) + "\n", encoding="utf8")


if __name__ == "__main__":
    main()
