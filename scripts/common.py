"""Shared paths and loaders for the axis-selection experiments."""
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "data" / "raw"
os.environ["GENSIM_DATA_DIR"] = str(RAW / "gensim")


def load_wordnet():
    import nltk
    nltk.data.path.insert(0, str(RAW / "nltk"))
    from nltk.corpus import wordnet as wn
    return wn


def load_glove():
    import gensim.downloader as api
    api.BASE_DIR = str(RAW / "gensim")
    return api.load("glove-wiki-gigaword-100")
