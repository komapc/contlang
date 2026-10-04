"""SemAxis on our hand-defined axes (An, Kwak, Ahn 2018).

Each axis is a pair of pole word sets; axis = mean(S+) - mean(S-) in Numberbatch.
Reports: pole quality (leave-one-out accuracy), axis correlations, how much of
the embedding of 3000 common words the axes explain (against random axes and
the best possible PCA subspace), the worst-explained words and the main
directions of the residual (candidate missing axes).
Writes data/semaxis_report.md.
"""
import gzip
import random
from pathlib import Path

import numpy as np

from common import RAW, ROOT

AXES = {
    "GOOD": ("good excellent great wonderful fine", "bad terrible awful horrible poor"),
    "BIG": ("big large huge enormous vast", "small tiny little minor miniature"),
    "NEAR": ("near close here nearby adjacent", "far distant remote away faraway"),
    "ABOVE": ("above up high over upward", "below down low under downward"),
    "LIVE": ("alive living lively vital animate", "dead death lifeless dying deceased"),
    "SAME": ("same identical equal similar alike", "different opposite unlike distinct dissimilar"),
    "MAYBE": ("certain sure definitely surely absolutely", "impossible never unlikely doubtful improbable"),
    "TIME": ("future later soon tomorrow upcoming", "past ago earlier yesterday former"),
    "INSIDE": ("inside within interior internal indoors", "outside external exterior outer outdoors"),
    "PART": ("whole entire complete total full", "part piece fragment bit fraction"),
    "SIDE": ("front forward ahead fore frontal", "back rear behind backward posterior"),
    "KNOW": ("know knowing aware informed knowledgeable", "ignorant unaware unknown clueless uninformed"),
    "WANT": ("love desire want crave adore", "hate loathe refuse reject detest"),
    "HEAT": ("hot fire burning warm scorching", "cold ice freezing cool frosty"),
    "BEGIN": ("end finish final last conclude", "begin start first initial commence"),
    "GIVE": ("give donate present offer grant", "take steal seize grab snatch"),
    "TOUCH": ("hard sharp rough solid rigid", "soft gentle smooth tender delicate"),
    "MATTER": ("gas vapor air steam smoke", "solid rock stone metal brick"),
    "SEX": ("brother son father husband uncle", "sister daughter mother wife aunt"),
    "HAPPEN": ("result consequence effect outcome aftermath", "cause reason origin source root"),
    "THINK": ("decide conclude choose determine resolve", "doubt hesitate wonder uncertain ponder"),
    "CAN": ("able easy possible capable feasible", "unable difficult incapable impossible hard"),
    "MANY": ("all every everyone everything always", "none nothing nobody zero never"),
    "SOMEONE": ("i me my myself mine", "they them their others themselves"),
    "THING": ("animal dog cat horse cow", "stone pebble boulder mineral gravel"),
    "MOVE": ("run sprint fast rush hurry", "stand still stop rest motionless"),
    "FEEL": ("excited intense passionate thrilled frantic", "calm sluggish bored quiet sleepy"),
}
PROBES = "member regime function union party committee institution specific influence protect group team society class".split()
OUT = ROOT / "data" / "semaxis_report.md"


def words_needed():
    ws = [l.split("\t")[0] for l in open(ROOT / "data" / "wordlist_en_x5.tsv")][1:]
    poles = [w for a, b in AXES.values() for w in (a + " " + b).split()]
    return ws, poles


def load_subset(need):
    cache = RAW / "cache_semaxis_vecs.npz"
    if cache.exists():
        d = np.load(cache, allow_pickle=True)
        if set(d["words"]) >= need:
            return dict(zip(d["words"], d["X"]))
    got = {}
    with gzip.open(RAW / "numberbatch-en-19.08.txt.gz", "rt", encoding="utf8") as f:
        next(f)
        for line in f:
            w, rest = line.split(" ", 1)
            if w in need:
                got[w] = np.array(rest.split(), dtype=np.float32)
                if len(got) == len(need):
                    break
    np.savez(cache, words=np.array(list(got)), X=np.stack(list(got.values())))
    return got


def unit(v):
    return v / (np.linalg.norm(v, axis=-1, keepdims=True) + 1e-9)


def main():
    words, poles = words_needed()
    need = set(words) | set(poles) | set(PROBES)
    vec = load_subset(need)
    words = [w for w in dict.fromkeys(words + PROBES) if w in vec]
    X = unit(np.stack([vec[w] for w in words]))
    missing = sorted({w for w in poles if w not in vec})

    A, loo = {}, {}
    for name, (p, n) in AXES.items():
        P = [w for w in p.split() if w in vec]
        N = [w for w in n.split() if w in vec]
        A[name] = unit(np.mean([unit(vec[w]) for w in P], 0) - np.mean([unit(vec[w]) for w in N], 0))
        ok = 0
        for side, S, O, sgn in (("p", P, N, 1), ("n", N, P, -1)):
            for w in S:
                rest = [x for x in S if x != w]
                a = np.mean([unit(vec[x]) for x in rest], 0) - np.mean([unit(vec[x]) for x in O], 0) if sgn == 1 \
                    else np.mean([unit(vec[x]) for x in O], 0) - np.mean([unit(vec[x]) for x in rest], 0)
                ok += (unit(vec[w]) @ unit(a)) * sgn > 0
        loo[name] = ok / (len(P) + len(N))
    names = list(A)
    AM = np.stack([A[k] for k in names])  # 27 x d

    corr = AM @ AM.T
    pairs = [(abs(corr[i, j]), names[i], names[j], corr[i, j]) for i in range(len(names)) for j in range(i)]
    pairs.sort(reverse=True)

    def r2(basis):
        Q, _ = np.linalg.qr(basis.T)  # d x k orthonormal
        res = X - (X @ Q) @ Q.T
        return 1 - (res ** 2).sum(1), res

    r2_axes, res = r2(AM)
    rng = random.Random(0)
    allw = list(vec)
    rand = []
    for _ in range(20):
        B = np.stack([unit(vec[rng.choice(allw)] - vec[rng.choice(allw)]) for _ in range(len(names))])
        rand.append(r2(B)[0].mean())
    U, S, Vt = np.linalg.svd(X - X.mean(0), full_matrices=False)
    r2_pca = r2(Vt[: len(names)])[0].mean()

    order = np.argsort(r2_axes)
    # residual directions
    Ur, Sr, Vr = np.linalg.svd(res - res.mean(0), full_matrices=False)
    comps = []
    for k in range(6):
        load = res @ Vr[k]
        hi = [words[i] for i in np.argsort(-load)[:14]]
        lo = [words[i] for i in np.argsort(load)[:14]]
        comps.append((Sr[k] ** 2 / (Sr ** 2).sum(), hi, lo))

    L = ["# SemAxis на наших осях (Numberbatch, 3000 слов)", "",
         f"Оси: {len(names)}; слов: {len(words)}; полюса заданы руками в `scripts/15_semaxis.py`. Не нашлось в словаре: {', '.join(missing) or 'нет'}.", "",
         "## Качество полюсов (leave-one-out: слово-полюс на своей стороне оси, построенной без него)", "",
         "| ось | LOO |", "| :-- | --: |"]
    for k in sorted(loo, key=loo.get):
        L.append(f"| {k} | {loo[k]:.2f} |")
    L += ["", "## Оси, похожие друг на друга (|cos| ≥ 0,35)", "", "| ось 1 | ось 2 | cos |", "| :-- | :-- | --: |"]
    L += [f"| {a} | {b} | {c:+.2f} |" for m, a, b, c in pairs if m >= 0.35] or ["| — | — | — |"]
    L += ["", "## Какую долю вектора слова объясняют оси (R², средняя по словам)", "",
          f"- наши {len(names)} осей: **{r2_axes.mean():.3f}**",
          f"- случайные {len(names)} осей (20 прогонов): {np.mean(rand):.3f} ± {np.std(rand):.3f}",
          f"- лучшие {len(names)} направлений PCA (верхний предел для {len(names)} измерений): {r2_pca:.3f}", "",
          "## Хуже всего объяснённые слова (R², 40 слов)", ""]
    L.append(", ".join(f"{words[i]} ({r2_axes[i]:.2f})" for i in order[:40]))
    L += ["", "## Слова из списка провалов (R²)", ""]
    L.append(", ".join(f"{w} ({r2_axes[words.index(w)]:.2f})" for w in PROBES if w in words))
    L += ["", "## Главные направления остатка (кандидаты на недостающие оси)", ""]
    for i, (share, hi, lo) in enumerate(comps, 1):
        L += [f"**{i}** (доля остатка {share:.1%}): + {', '.join(hi)}", f"  − {', '.join(lo)}", ""]
    OUT.write_text("\n".join(L) + "\n")
    print("\n".join(L[:12]))
    print(f"axes R2={r2_axes.mean():.3f} random={np.mean(rand):.3f} pca={r2_pca:.3f}")


if __name__ == "__main__":
    main()
