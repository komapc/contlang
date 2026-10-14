# Очищенное пространство шага 0 (space.npz из scripts/23_pca_axes.py) и направления по словам-полюсам.
import json
from pathlib import Path
import numpy as np
D = Path(__file__).resolve().parent; SITE = D.parents[3] / "site" / "data"
m = json.loads((SITE / "math.json").read_text()); W = m["words"]; IDX = {w: i for i, w in enumerate(W)}
X = np.frombuffer((SITE / "vocab.bin").read_bytes(), dtype=np.int8).reshape(len(W), m["dim"]).astype(float)
X /= np.linalg.norm(X, axis=1, keepdims=True)
s = np.load(D / "space.npz"); keep, Q, MU, V, Bv = s["keep"], s["Q"], s["mean"], s["V"], s["Bv"]
P = lambda Z: Z - (Z @ Q) @ Q.T
Z = P(X[keep] - MU); Z /= np.linalg.norm(Z, axis=1, keepdims=True); ZM = Z.mean(0); Z = Z - ZM
words = [W[i] for i in keep]; rank = np.array(keep)
unit = lambda v: v / np.linalg.norm(v)
# векторы слов-полюсов из полного Numberbatch (poles_nb.npz): в словаре сайта мало базовых слов (chilly, icy, soggy),
# а пространство то же (cos с vocab.bin 0,999)
_nb = np.load(D / "poles_nb.npz"); NB = {w: unit(v.astype(float)) for w, v in zip(_nb["words"], _nb["vecs"])}
def direction(pos, neg):
    """среднее(+) − среднее(−) по словам-полюсам (Numberbatch), очищенное; None, если на стороне < 5 слов"""
    p = [NB[w] for w in pos if w in NB]; n = [NB[w] for w in neg if w in NB]
    if len(p) < 5 or len(n) < 5: return None, len(p), len(n)
    return unit(P((np.mean(p, 0) - np.mean(n, 0))[None])[0]), len(p), len(n)
def top(d, k=20, sign=1, excl=(), maxrank=6000):
    o = np.argsort(-sign * (Z @ d)); return [words[i] for i in o if rank[i] < maxrank and words[i] not in excl][:k]
