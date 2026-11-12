"""size1: chart → size.svg (plain SVG, no dependencies).  .venv/bin/python data/eval/runs/size1/plot.py"""
import json, math
from pathlib import Path

D = Path(__file__).resolve().parent
C = [x for x in json.load(open(D / "curve.json")) if x["a_lex"] == 0.9]
BLUE, ORANGE, INK, INK2, GRID = "#2a78d6", "#eb6834", "#1f1f1e", "#6b6a64", "#e4e3de"
DASH = {1: 'stroke-dasharray="2 4"', 2: 'stroke-dasharray="7 4"', 3: ""}
NAME = {1: "1 word", 2: "up to 2", 3: "up to 3"}
W, H = 760, 520
px, py, pw, ph = 70, 90, 520, 340
out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       f'font-family="Helvetica, Arial, sans-serif" font-size="13">', f'<rect width="{W}" height="{H}" fill="#ffffff"/>']
def T(x, y, s, c=INK2, a="start", fs=13, fw="normal"):
    out.append(f'<text x="{x:.1f}" y="{y:.1f}" fill="{c}" text-anchor="{a}" font-size="{fs}" font-weight="{fw}">{s}</text>')
lx = lambda L: px + (math.log10(L) - math.log10(70)) / (math.log10(12000) - math.log10(70)) * pw
ly = lambda v: py + ph - v / 100 * ph
T(10, 30, "Share of text understood vs units to learn, by phrase limit", c=INK, fs=16, fw="bold")
T(10, 50, "size1: 120 words in 4 frequency bands, measured; curve = lexicon of the N most frequent words + composition")
T(10, 74, "read as close, % of word tokens")
for v in (0, 20, 40, 60, 80, 100):
    out.append(f'<line x1="{px}" x2="{px + pw}" y1="{ly(v):.1f}" y2="{ly(v):.1f}" stroke="{GRID}" stroke-width="0.7"/>')
    T(px - 8, ly(v) + 4, f"{v}%", a="end")
for L in (100, 300, 1000, 3000, 10000):
    out.append(f'<line x1="{lx(L):.1f}" x2="{lx(L):.1f}" y1="{py}" y2="{py + ph}" stroke="{GRID}" stroke-width="0.7"/>')
    T(lx(L), py + ph + 18, f"{L:,}", a="middle")
T(px + pw / 2, py + ph + 40, "units to learn L = base (min-co 82, Toki Pona 120) + lexicon entries N, log scale", a="middle")
for lang, col in (("tp", ORANGE), ("mc", BLUE)):
    for k in (1, 2, 3):
        pts = sorted((x["L"], 100 * x["U"]) for x in C if x["lang"] == lang and x["k"] == k)
        d = " ".join(f"{lx(L):.1f},{ly(u):.1f}" for L, u in pts)
        out.append(f'<polyline points="{d}" fill="none" stroke="{col}" stroke-width="2" {DASH[k]}/>')
        L0, u0 = pts[0]
        out.append(f'<circle cx="{lx(L0):.1f}" cy="{ly(u0):.1f}" r="4.5" fill="{col}" stroke="#fff" stroke-width="1.5"/>')
# legend
lgx, lgy = px + pw + 20, py + 10
for j, (lang, col, nm) in enumerate((("mc", BLUE, "min-co"), ("tp", ORANGE, "Toki Pona (cipher)"))):
    T(lgx, lgy + j * 95, nm, c=INK, fw="bold")
    for k in (1, 2, 3):
        y = lgy + j * 95 + 18 * k
        out.append(f'<line x1="{lgx}" x2="{lgx + 30}" y1="{y - 4}" y2="{y - 4}" stroke="{col}" stroke-width="2" {DASH[k]}/>')
        u0 = next(100 * x["U"] for x in C if x["lang"] == lang and x["k"] == k and x["N"] == 0)
        T(lgx + 36, y, f"{NAME[k]}: {u0:.0f}%", c=INK)
T(lgx, lgy + 205, "dots = no lexicon", fs=11)
T(lgx, lgy + 222, "lexicon entries read", fs=11)
T(lgx, lgy + 237, "right 90% of the time", fs=11)
out.append("</svg>")
(D / "size.svg").write_text("\n".join(out))
print("size.svg")
