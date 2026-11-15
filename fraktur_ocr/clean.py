"""Cleanup passes for OCR text from Fraktur prints."""
import re

_LIGATURES = {
    "ſt": "st",
    "ſſ": "ss",
    "ﬅ": "st",
    "c̷h": "ch",
    "Ɖ": "tz",
}

_HEADER = re.compile(r"^\s*(\d{1,3}|Seite \d+|[IVXLC]+\.)\s*$", re.MULTILINE)
_HYPHEN = re.compile(r"(\w)[-¬‐]\s*\n\s*(\w)")


def fix_long_s(text: str, keep: bool = False) -> str:
    """Replace long s with round s unless keep=True."""
    for bad, good in _LIGATURES.items():
        text = text.replace(bad, good)
    return text if keep else text.replace("ſ", "s")


def dehyphenate(text: str) -> str:
    """Join words split across line ends."""
    return _HYPHEN.sub(r"\1\2", text)


def strip_headers(text: str) -> str:
    """Drop lines that are only page numbers or running heads."""
    return _HEADER.sub("", text)


def clean(text: str, keep_long_s: bool = False) -> str:
    text = strip_headers(text)
    text = dehyphenate(text)
    text = fix_long_s(text, keep=keep_long_s)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()
