"""roots2 → size1/axes.svg: one clear chart "learn X roots → how often is a word guessed".
    .venv/bin/python data/eval/runs/roots2/plot.py
"""
import json
import math
from pathlib import Path

D = Path(__file__).resolve().parent
S1 = D.parent / "size1"
P = json.load(open(D / "points.json"))
A = json.load(open(S1 / "axes.json"))
P3 = json.load(open(D.parent / "roots3/points.json"))
C = {(x["lang"], x["k"]): x["U"] for x in json.load(open(S1 / "curve.json")) if x["N"] == 0 and x["a_lex"] == 0.9}
BLUE, BLUE_BAND, ORANGE, AQUA = "#2a78d6", "#d6e5f7", "#eb6834", "#1baf7a"
BLUE4, BLUE5 = "#1c5aa6", "#123d73"
ORANGE4, ORANGE5 = "#b8461a", "#7d2e10"
INK, INK2, GRID, SURF = "#0b0b0b", "#52514e", "#e4e3de", "#fcfcfb"
W, H = 820, 582
px, py, pw, ph = 70, 132, 560, 340
X0, X1 = 1, 300
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="13">', f'<rect width="{W}" height="{H}" fill="{SURF}"/>']


def T(x, y, s, c=INK2, a="start", fs=13, fw="normal"):
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{c}" text-anchor="{a}" font-size="{fs}" font-weight="{fw}">{s}</text>')


lx = lambda X: px + math.log10(X / X0) / math.log10(X1 / X0) * pw
ly = lambda v: py + ph - v / 100 * ph
T(16, 30, "Learn X roots: how often is a word guessed?", c=INK, fs=17, fw="bold")
T(16, 52, "A reader who knows only the X roots sees a min-co code for a word and names the word; share named right (judges),")
T(16, 70, "weighted by how often words occur in English texts. Each word is one code of up to 3 min-co words.")
# legend: two rows
lg = [[(BLUE, "", 3, "min-co, free (band = 95 % interval)"), (BLUE4, "6 3", 2, "min-co, exactly 4 roots"), (BLUE5, "2 3", 2, "exactly 5 roots")],
      [(ORANGE, "", 2, "PCA axes, 3 values per word"), (ORANGE4, "", 2, "4 values"), (ORANGE5, "", 2, "5 values"), (AQUA, "dot", 0, "Toki Pona")]]
for row, items in enumerate(lg):
    x, y = 16, 91 + 20 * row
    for c, dash, sw, s_ in items:
        if dash == "dot":
            out.append(f'<circle cx="{x + 11}" cy="{y}" r="5" fill="{c}"/>')
        else:
            out.append(f'<line x1="{x}" x2="{x + 22}" y1="{y}" y2="{y}" stroke="{c}" stroke-width="{sw}" stroke-dasharray="{dash}"/>')
        T(x + 28, y + 4, s_, c=INK)
        x += 28 + 6.8 * len(s_) + 22
# word-root zone
out.append(f'<rect x="{lx(51):.1f}" y="{py}" width="{lx(X1) - lx(51):.1f}" height="{ph}" fill="#f2f1ec"/>')
T(lx(51) + 8, py + 16, "above 51: + the most frequent", fs=11.5)
T(lx(51) + 8, py + 31, "English words as roots", fs=11.5)
for v in (0, 20, 40, 60, 80, 100):
    out.append(f'<line x1="{px}" x2="{px + pw}" y1="{ly(v):.1f}" y2="{ly(v):.1f}" stroke="{GRID}" stroke-width="0.8"/>')
    T(px - 8, ly(v) + 4, f"{v}%", a="end")
for X in (1, 3, 10, 30, 51, 100, 300):
    T(lx(X), py + ph + 18, f"{X}", a="middle")
T(px + pw / 2, py + ph + 40, "roots to learn (X), log scale", a="middle")
# v2c band + line
P = sorted(P, key=lambda p: p["X"])
band = [f"{lx(p['X']):.1f},{ly(100 * p['hi']):.1f}" for p in P] + [f"{lx(p['X']):.1f},{ly(100 * p['lo']):.1f}" for p in P[::-1]]
out.append(f'<polygon points="{" ".join(band)}" fill="{BLUE_BAND}" opacity="0.8"/>')
# machine 3 / 4 / 5 values
mm = {}
for r, c in ((3, ORANGE), (4, ORANGE4), (5, ORANGE5)):
    mm[r] = sorted((x["X"], 100 * x["U"]) for x in A["res"] if x["r"] == r)
    out.append(f'<polyline points="{" ".join(f"{lx(X):.1f},{ly(u):.1f}" for X, u in mm[r])}" fill="none" stroke="{c}" stroke-width="2"/>')
m = mm[3]
# min-co exactly 4 / 5 roots (roots3)
for n, c, dash in ((4, BLUE4, "6 3"), (5, BLUE5, "2 3")):
    q = sorted((p["X"], 100 * p["U"]) for p in P3 if p["N"] == n)
    out.append(f'<polyline points="{" ".join(f"{lx(X):.1f},{ly(u):.1f}" for X, u in q)}" fill="none" stroke="{c}" stroke-width="2" stroke-dasharray="{dash}"/>')
out.append(f'<polyline points="{" ".join(f"{lx(p["X"]):.1f},{ly(100 * p["U"]):.1f}" for p in P)}" fill="none" stroke="{BLUE}" stroke-width="3"/>')
for p in P:
    out.append(f'<circle cx="{lx(p["X"]):.1f}" cy="{ly(100 * p["U"]):.1f}" r="4.5" fill="{BLUE}" stroke="{SURF}" stroke-width="2"/>')
    T(lx(p["X"]) + (0 if p["X"] < 10 or p["X"] > 150 else 4), ly(100 * p["U"]) + (-10 if p["X"] < 10 or p["X"] > 150 else 19), f"{100 * p['U']:.0f}", c=INK, a="middle", fs=11)
# direct labels at the right
T(lx(X1) + 8, ly(100 * P[-1]["U"]) + 8, "min-co", c=INK, fw="bold")
T(lx(X1) + 8, ly(100 * P[-1]["U"]) + 23, "(free / 4 / 5 roots)", c=INK, fs=11)
for r, dy in ((3, 4), (4, -2), (5, 4)):
    T(lx(X1) + 8, ly(mm[r][-1][1]) + dy, f"PCA, {r} values", c=INK, fs=11.5)
tp = 100 * C[("tp", 3)]
out.append(f'<circle cx="{lx(120):.1f}" cy="{ly(tp):.1f}" r="6" fill="{AQUA}" stroke="{SURF}" stroke-width="2"/>')
T(lx(120) + 10, ly(tp) + 18, f"Toki Pona: 120 words, {tp:.0f}", c=INK, fs=12)
T(16, H - 44, "PCA lines: a word is written as r values (-5..+5) on r of X automatic meaning axes (PCA of word vectors); its reader knows the exact", fs=10.5)
T(16, H - 30, "position of all 21,514 words. min-co: roots2 (free number of roots) and roots3 (exactly 4 / 5), 120 words; Toki Pona: size1. "
              "Above 51,", fs=10.5)
T(16, H - 16, "up to 29 of the 120 test words are themselves roots (see roots2/README).", fs=10.5)
out.append("</svg>")
(S1 / "axes.svg").write_text("\n".join(out))
print("axes.svg")
