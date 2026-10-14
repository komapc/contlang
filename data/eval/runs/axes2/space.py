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
def direction(pos, neg):
    """среднее(+) − среднее(−) по словам словаря, очищенное; None, если на стороне < 5 слов"""
    p = [IDX[w] for w in pos if w in IDX]; n = [IDX[w] for w in neg if w in IDX]
    if len(p) < 5 or len(n) < 5: return None, len(p), len(n)
    return unit(P((X[p].mean(0) - X[n].mean(0))[None])[0]), len(p), len(n)
def top(d, k=20, sign=1, excl=(), maxrank=6000):
    o = np.argsort(-sign * (Z @ d)); return [words[i] for i in o if rank[i] < maxrank and words[i] not in excl][:k]
