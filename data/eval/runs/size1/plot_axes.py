"""size1: "learn X axes → how surely is a word guessed" → axes_detail.svg (all machine lines, roots1 points).  .venv/bin/python data/eval/runs/size1/plot_axes.py"""
import json, math
from pathlib import Path

D = Path(__file__).resolve().parent
A = json.load(open(D / "axes.json"))
C = {(x["lang"], x["k"]): x["U"] for x in json.load(open(D / "curve.json")) if x["N"] == 0 and x["a_lex"] == 0.9}
BLUE, ORANGE, GREEN, INK, INK2, GRID = "#2a78d6", "#eb6834", "#1f9e6e", "#1f1f1e", "#6b6a64", "#e4e3de"
RAMP = {1: "#d9c7f0", 2: "#bfa3e6", 3: "#a07fd8", 6: "#7f5bc4", 9: "#5f3da8", "all": "#3e2378"}
RN = {1: "1 value", 2: "2 values", 3: "3 values", 6: "6 values", 9: "9 values", "all": "all X values"}
DASH = {1: 'stroke-dasharray="2 4"', 2: 'stroke-dasharray="7 4"', 3: ""}
KN = {1: "1 word", 2: "up to 2 words", 3: "up to 3 words"}
P = json.load(open(D.parent / "roots1/points.json"))
W, H = 880, 560
px, py, pw, ph = 70, 90, 520, 340
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="13">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def T(x, y, s, c=INK2, a="start", fs=13, fw="normal"):
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{c}" text-anchor="{a}" font-size="{fs}" font-weight="{fw}">{s}</text>')
lx = lambda X: px + (math.log10(X) - math.log10(5)) / (math.log10(300) - math.log10(5)) * pw
ly = lambda v: py + ph - v / 100 * ph
T(10, 30, "Learn X axes: how surely is a word guessed?", c=INK, fs=16, fw="bold")
T(10, 50, "people: min-co with its X most used roots (blind readers, judges); machine: X principal axes of word vectors, values on r axes")
T(10, 74, "read as close, % of word tokens, no lexicon")
for v in (0, 20, 40, 60, 80, 100):
    out.append(f'<line x1="{px}" x2="{px + pw}" y1="{ly(v):.1f}" y2="{ly(v):.1f}" stroke="{GRID}" stroke-width="0.7"/>')
    T(px - 8, ly(v) + 4, f"{v}%", a="end")
for X in (5, 10, 20, 51, 120, 300):
    out.append(f'<line x1="{lx(X):.1f}" x2="{lx(X):.1f}" y1="{py}" y2="{py + ph}" stroke="{GRID}" stroke-width="0.7"/>')
    T(lx(X), py + ph + 18, f"{X}", a="middle")
T(px + pw / 2, py + ph + 40, "axes (roots) to learn X, log scale", a="middle")
for r in (1, 2, 3, 6, 9, "all"):
    pts = sorted((x["X"], 100 * x["U"]) for x in A["res"] if x["r"] == r and x["X"] >= 5)
    d = " ".join(f"{lx(X):.1f},{ly(u):.1f}" for X, u in pts)
    out.append(f'<polyline points="{d}" fill="none" stroke="{RAMP[r]}" stroke-width="2"/>')
    X, u = pts[-1]
    T(lx(X) + 6, ly(u) + 4 + {6: 10, 9: -1, "all": -12}.get(r, 0), RN[r], c=RAMP[r] if r not in (1, 2) else "#8f78b8", fs=11)
for k in (1, 2, 3):
    pts = sorted((p["X"], 100 * p["U"]) for p in P if p["arm"] in ("R10", "R20", "R30", "V2B") and p["k"] == k)
    d = " ".join(f"{lx(X):.1f},{ly(u):.1f}" for X, u in pts)
    out.append(f'<polyline points="{d}" fill="none" stroke="{BLUE}" stroke-width="2.5" {DASH[k]}/>')
    for X, u in pts:
        out.append(f'<circle cx="{lx(X):.1f}" cy="{ly(u):.1f}" r="4" fill="{BLUE}" stroke="#fff" stroke-width="1.5"/>')
    u = next(100 * p["U"] for p in P if p["arm"] == "V2C" and p["k"] == k)
    out.append(f'<rect x="{lx(51) + 6 * (k - 2) - 4:.1f}" y="{ly(u) - 4:.1f}" width="8" height="8" fill="{GREEN}" stroke="#fff" stroke-width="1.5"/>')
    u = 100 * C[("tp", k)]
    out.append(f'<circle cx="{lx(120) + 6 * (k - 2):.1f}" cy="{ly(u):.1f}" r="5" fill="{ORANGE}" stroke="#fff" stroke-width="1.5"/>')
T(lx(120) + 14, ly(100 * C[("tp", 3)]) - 8, "Toki Pona", c=ORANGE, fw="bold", fs=12)
lgx, lgy = px + pw + 80, py + 10
T(lgx, lgy, "min-co (v2b roots)", c=INK, fw="bold")
for k in (1, 2, 3):
    y = lgy + 18 * k
    out.append(f'<line x1="{lgx}" x2="{lgx + 30}" y1="{y - 4}" y2="{y - 4}" stroke="{BLUE}" stroke-width="2.5" {DASH[k]}/>')
    T(lgx + 36, y, KN[k], c=INK)
T(lgx, lgy + 86, "■ v2c roots (51)", c=GREEN, fw="bold")
T(lgx, lgy + 104, "● Toki Pona (120 words)", c=ORANGE, fw="bold")
T(lgx, lgy + 140, "machine (PCA axes)", c=INK, fw="bold")
T(lgx, lgy + 158, "values per word:", c=INK2, fs=12)
T(lgx, lgy + 174, "light 1 → dark all X", c=INK2, fs=12)
T(lgx, lgy + 200, "3 points per marker:", c=INK2, fs=11)
T(lgx, lgy + 214, "1 / ≤2 / ≤3 words", c=INK2, fs=11)
T(10, H - 30, f"Machine reader: nearest word vector among 21,514 Brown lemmas with a frequency prior — it knows every word's exact position. "
              f"Close = same word,", fs=10.5)
T(10, H - 15, f"WordNet synonym or cosine ≥ {A['theta']:.2f} (agrees with human judges on 91%). People: measured (size1, roots1), "
              f"roots = the most used v2b roots.", fs=10.5)
out.append("</svg>")
(D / "axes_detail.svg").write_text("\n".join(out))
print("axes_detail.svg")
