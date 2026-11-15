# fraktur-ocr-utils

Small helpers for cleaning up OCR output from Fraktur (blackletter) prints.
Tesseract's `deu_frak` model gets most of the text right, but old newspapers
still come out with long-s confusion, broken ligatures and hyphenation at line ends.
This package fixes the boring 90%.

## Install

```
pip install -e .
```

## Use

```python
from fraktur_ocr import clean

text = open("seite_04.txt", encoding="utf-8").read()
print(clean(text))
```

## What it fixes

- long s (ſ) to s, optionally kept
- common ligature misreads (ſt, ch, ck, tz)
- line-end hyphenation (`Kon-\nitz` to `Konitz`)
- stray margin numbers and page headers

Tested against a few hundred pages of 1890s to 1910s regional papers. PRs welcome.
