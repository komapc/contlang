"""Axis fitting, quantization and WordNet-based evaluation helpers."""
import numpy as np

from common import load_wordnet

LEVELS = 5  # quantized values are -5..+5 (11 levels)
CLIP = 2.5  # z-scores are clipped to +-CLIP then mapped to +-LEVELS


def varimax(phi, iters=100, tol=1e-6):
    p, k = phi.shape
    rot, d = np.eye(k), 0.0
    for _ in range(iters):
        lam = phi @ rot
        u, s, vt = np.linalg.svd(
            phi.T @ (lam ** 3 - lam @ np.diag((lam ** 2).sum(axis=0)) / p))
        rot = u @ vt
        if s.sum() < d * (1 + tol):
            break
        d = s.sum()
    return phi @ rot


def fit_axes(method, Xtr, k, rng):
    """Orthonormal axes W (dim x k); PCA/varimax are ordered by variance carried."""
    mean = Xtr.mean(axis=0)
    if method == "random":
        W, _ = np.linalg.qr(rng.standard_normal((Xtr.shape[1], k)))
        return mean, W
    _, _, vt = np.linalg.svd(Xtr - mean, full_matrices=False)
    W = vt[:k].T
    if method == "varimax":
        W = varimax(W)
    return mean, W


def quantize(scores, std):
    z = np.clip(scores / std, -CLIP, CLIP)
    return np.round(z / CLIP * LEVELS)


def dequantize(q, std):
    return q / LEVELS * CLIP * std


def nearest_other(R, Xn, ids, k):
    """Indices of the k nearest words to each reconstruction, excluding the word itself."""
    Rn = R / np.linalg.norm(R, axis=1, keepdims=True)
    sims = Rn @ Xn.T
    sims[np.arange(len(ids)), ids] = -np.inf
    return np.argsort(-sims, axis=1)[:, :k]


def make_wup(words, pos):
    """Return (wup, mean_wup): WordNet Wu-Palmer between words of the same POS tag."""
    wn = load_wordnet()
    tag = {"noun": "n", "verb": "v", "adj": "a", "adv": "r"}
    cache = {}

    def wup(i, j):
        if pos[i] != pos[j]:
            return None
        for w in (i, j):
            if w not in cache:
                cache[w] = wn.synsets(words[w], tag[pos[w]])
        if not cache[i] or not cache[j]:
            return None
        return cache[i][0].wup_similarity(cache[j][0])

    def mean_wup(pairs):
        v = [x for x in (wup(i, j) for i, j in pairs) if x is not None]
        return float(np.mean(v)) if v else float("nan")

    return wup, mean_wup


def unit(X):
    return X / np.linalg.norm(X, axis=1, keepdims=True)


def remove_freq(X, logfreq, train, ridge=10.0):
    """Project out the direction that predicts log word frequency (ridge fit on train)."""
    Xc = X[train] - X[train].mean(axis=0)
    w = np.linalg.solve(Xc.T @ Xc + ridge * np.eye(X.shape[1]), Xc.T @ logfreq[train])
    u = w / np.linalg.norm(w)
    return unit(X - np.outer(X @ u, u))
