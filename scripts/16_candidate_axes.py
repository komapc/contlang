"""Candidate new axes on top of the 27 (see 15_semaxis.py).

For each candidate (pole sets) report the gain in mean R^2 over the 3000 words,
the gain on the probe words from the failure list, and the words that gain most.
Compared with the gain from one random pair-difference axis.
Writes data/semaxis_candidates.md.
"""
import importlib.util
import random

import numpy as np

from common import ROOT

spec = importlib.util.spec_from_file_location("sx", ROOT / "scripts" / "15_semaxis.py")
sx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sx)

CANDS = {
    "CHANGE_dir": ("increase grow rise expand improve", "decrease shrink fall reduce decline"),
    "CHANGE_any": ("change transform alter vary shift", "remain stay constant stable unchanged"),
    "AUTHORITY": ("authority committee agency commission government", "individual private personal informal citizen"),
    "PARTICULAR": ("particular specific unique peculiar distinct", "general common universal generic typical"),
}
OUT = ROOT / "data" / "semaxis_candidates.md"


def main():
    words, poles = sx.words_needed()
    extra = [w for a, b in CANDS.values() for w in (a + " " + b).split()]
    vec = sx.load_subset(set(words) | set(poles) | set(sx.PROBES) | set(extra))
    words = [w for w in dict.fromkeys(words + sx.PROBES) if w in vec]
    X = sx.unit(np.stack([vec[w] for w in words]))

    def axis(p, n):
        P = [sx.unit(vec[w]) for w in p.split() if w in vec]
        N = [sx.unit(vec[w]) for w in n.split() if w in vec]
        return sx.unit(np.mean(P, 0) - np.mean(N, 0))

    base = np.stack([axis(*v) for v in sx.AXES.values()])

    def r2(B):
        Q, _ = np.linalg.qr(B.T)
        res = X - (X @ Q) @ Q.T
        return 1 - (res ** 2).sum(1)

    r0 = r2(base)
    pi = [words.index(w) for w in sx.PROBES if w in words]
    rng = random.Random(1)
    allw = list(vec)
    rg = [r2(np.vstack([base, sx.unit(vec[rng.choice(allw)] - vec[rng.choice(allw)])])).mean() - r0.mean()
          for _ in range(30)]

    L = ["# Кандидаты в новые оси (SemAxis, Numberbatch)", "",
         f"База: 27 осей, средняя R² {r0.mean():.4f}. Одна случайная ось добавляет {np.mean(rg):+.4f} ± {np.std(rg):.4f}.", "",
         "| кандидат | ΔR² (все слова) | ΔR² (слова-провалы) | в разах от случайной |", "| :-- | --: | --: | --: |"]
    detail = []
    new = {}
    for k, (p, n) in CANDS.items():
        a = axis(p, n)
        new[k] = a
        r1 = r2(np.vstack([base, a]))
        d = r1 - r0
        L.append(f"| {k} | {d.mean():+.4f} | {d[pi].mean():+.4f} | {d.mean() / np.mean(rg):.1f}× |")
        top = np.argsort(-d)[:25]
        detail.append(f"**{k}** — больше всего выигрывают: " + ", ".join(f"{words[i]} ({d[i]:+.2f})" for i in top))
        pr = ", ".join(f"{words[i]} {d[i]:+.2f}" for i in pi)
        detail.append(f"  слова-провалы: {pr}")
    allc = np.vstack([base] + list(new.values()))
    d = r2(allc) - r0
    L += ["", f"Все четыре вместе: ΔR² {d.mean():+.4f} (все слова), {d[pi].mean():+.4f} (слова-провалы).", ""]
    # coordinates of probe words on the new axes (cosine with axis)
    L += ["## Координаты слов на новых осях (косинус)", "",
          "| слово | " + " | ".join(CANDS) + " |", "| :-- | " + " | ".join("--:" for _ in CANDS) + " |"]
    for w in sx.PROBES + ["increase", "decrease", "committee", "authority", "specific", "general", "change", "stay"]:
        if w in vec:
            L.append(f"| {w} | " + " | ".join(f"{sx.unit(vec[w]) @ a:+.2f}" for a in new.values()) + " |")
    L += [""] + detail
    OUT.write_text("\n".join(L) + "\n")
    print("\n".join(L[:12]))


if __name__ == "__main__":
    main()
