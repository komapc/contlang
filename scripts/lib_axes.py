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


def nearest_other(R, Xn, ids, k, group=None):
    """Indices of the k nearest rows to each reconstruction, excluding the word itself.

    With `group` (word id per row), every row of the same word is excluded, so a homograph's
    other-POS entry cannot be returned as its own neighbour.
    """
    Rn = R / np.linalg.norm(R, axis=1, keepdims=True)
    sims = Rn @ Xn.T
    if group is None:
        sims[np.arange(len(ids)), ids] = -np.inf
    else:
        sims[group[None, :] == group[ids][:, None]] = -np.inf
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


def recon_plain(X, train, k, seed=0):
    """Reconstruction of all rows from k quantized varimax axes."""
    mean, W = fit_axes("varimax", X[train], k, np.random.default_rng(seed))
    S = (X - mean) @ W
    std = S[train].std(axis=0)
    return dequantize(quantize(S, std), std) @ W.T + mean


def recon_split(X, train, pos, k, nform=3, seed=0):
    """Reconstruction from nform LDA 'form' axes + (k - nform) meaning axes (see 05_form_meaning.py)."""
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
    lda = LinearDiscriminantAnalysis(solver="eigen", shrinkage="auto").fit(X[train], pos[train])
    F, _ = np.linalg.qr(lda.scalings_[:, :nform])
    mean0 = X[train].mean(axis=0)
    Xc = X - mean0
    f = Xc @ F
    Xr = Xc - f @ F.T
    mean_r, Wm = fit_axes("varimax", Xr[train], k - nform, np.random.default_rng(seed))
    M = (Xr - mean_r) @ Wm
    sf, sm = f[train].std(axis=0), M[train].std(axis=0)
    return (dequantize(quantize(f, sf), sf) @ F.T + dequantize(quantize(M, sm), sm) @ Wm.T
            + mean0 + mean_r)


def generality(words, pos, cache_path):
    """Hyponym-closure size of each noun/verb's dominant-POS first synset (cached; slow)."""
    from pathlib import Path
    cache = Path(cache_path)
    if cache.exists():
        g = np.load(cache)
        if len(g) == len(words):
            return g
    wn = load_wordnet()
    tag = {"noun": "n", "verb": "v"}
    g = np.zeros(len(words))
    for i, w in enumerate(words):
        if pos[i] in tag:
            syns = wn.synsets(w, tag[pos[i]])
            if syns:
                g[i] = len(set(syns[0].closure(lambda s: s.hyponyms())))
    np.save(cache, g)
    return g


def greedy_roots(S, train, pool, R):
    """Greedy facility location: pick R words from pool maximizing summed best cosine on train."""
    best = np.full(len(train), -1.0)
    chosen = []
    St = S[train]
    for _ in range(R):
        gains = [np.maximum(best, St[:, c]).sum() - best.sum() for c in pool]
        c = pool[int(np.argmax(gains))]
        chosen.append(c)
        best = np.maximum(best, St[:, c])
    return chosen
