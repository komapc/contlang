"""Shared paths and loaders for the axis-selection experiments."""
import os
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
os.environ["GENSIM_DATA_DIR"] = str(RAW / "gensim")

SOURCES = ("glove100", "numberbatch")


def load_wordnet():
    import nltk
    nltk.data.path.insert(0, str(RAW / "nltk"))
    from nltk.corpus import wordnet as wn
    return wn


def load_vectors(name):
    """Full gensim KeyedVectors for an embedding source (slow for numberbatch)."""
    if name == "glove100":
        import gensim.downloader as api
        api.BASE_DIR = str(RAW / "gensim")
        return api.load("glove-wiki-gigaword-100")
    if name == "numberbatch":
        from gensim.models import KeyedVectors
        return KeyedVectors.load_word2vec_format(
            str(RAW / "numberbatch-en-19.08.txt.gz"), binary=False)
    raise ValueError(name)


# kept for the first prototype script
def load_glove():
    return load_vectors("glove100")


def word_matrix(name, words):
    """Vectors for `words` from source `name`, cached next to the raw data."""
    cache = RAW / f"cache_{name}_{len(words)}.npz"
    if cache.exists():
        d = np.load(cache, allow_pickle=True)
        if list(d["words"]) == list(words):
            return d["X"]
    kv = load_vectors(name)
    X = np.stack([kv[w] for w in words]).astype(np.float32)
    np.savez(cache, words=np.array(words), X=X)
    return X
