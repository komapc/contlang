"""Раскрытие вариантов и подсчёт оценок судьи.

    python3 scripts/eval/score.py --map RUN/judge_map.json --scores RUN/scores_words.tsv [--scores ...] [--base full] [--label words]

scores.tsv: строки `id<TAB>оценка A<TAB>оценка B…`. Варианты вида `имя_X` (несколько
кодировщиков на условие) группируются по имени до первого `_`. Печатает среднее, долю
≥2 и 3 по группам, а для каждой группы против --base — среднюю парную разницу с
95%-ным бутстреп-интервалом по пунктам.
"""
import argparse
import json
import random
import statistics as st
from collections import defaultdict


def load(map_path, score_paths):
    mp = json.load(open(map_path))
    per = defaultdict(dict)  # группа -> id -> [оценки]
    for sp in score_paths:
        for line in open(sp, encoding="utf8"):
            p = line.split()
            if len(p) < 2 or p[0] not in mp:
                continue
            for var, s in zip(mp[p[0]], p[1:]):
                per[var.split("_")[0]].setdefault(p[0], []).append(int(s))
    return {g: {i: sum(v) / len(v) for i, v in d.items()} for g, d in per.items()}


def boot_ci(diffs, n=10000, seed=1):
    rnd = random.Random(seed)
    m = len(diffs)
    means = sorted(sum(diffs[rnd.randrange(m)] for _ in range(m)) / m for _ in range(n))
    return means[int(0.025 * n)], means[int(0.975 * n)]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--map", required=True)
    p.add_argument("--scores", action="append", required=True)
    p.add_argument("--base")
    p.add_argument("--label", default="")
    a = p.parse_args()
    G = load(a.map, a.scores)
    print(f"## {a.label}" if a.label else "##")
    print("| группа | n | среднее | ≥2 | 3 |\n| :-- | :-- | :-- | :-- | :-- |")
    for g, d in G.items():
        x = list(d.values())
        print(f"| {g} | {len(x)} | {st.mean(x):.2f} | {sum(v >= 2 for v in x)} | {sum(v >= 2.99 for v in x)} |")
    if a.base:
        for g, d in G.items():
            if g == a.base:
                continue
            ids = [i for i in d if i in G[a.base]]
            diffs = [d[i] - G[a.base][i] for i in ids]
            lo, hi = boot_ci(diffs)
            print(f"\n{g} − {a.base}: {st.mean(diffs):+.2f}  95% ИИ [{lo:+.2f}, {hi:+.2f}], n={len(ids)}"
                  + ("  (значимо)" if lo > 0 or hi < 0 else "  (в пределах шума)"))


if __name__ == "__main__":
    main()
