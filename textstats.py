"""Offline text statistics (no API needed)."""
import re
from collections import Counter

WORD_RE = re.compile(r"\w+", re.UNICODE)
SENT_RE = re.compile(r"[.!?…]+")


def stats(text, top_n=5, min_len=4, wpm=200):
    """Return basic statistics about a text."""
    words = WORD_RE.findall(text.lower())
    sentences = [s for s in SENT_RE.split(text) if s.strip()]
    top = Counter(w for w in words if len(w) >= min_len).most_common(top_n)
    return {
        "characters": len(text),
        "words": len(words),
        "sentences": len(sentences),
        "reading_minutes": round(len(words) / wpm, 1),
        "top_words": top,
    }
