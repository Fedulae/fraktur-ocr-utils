from fraktur_ocr import clean, dehyphenate, fix_long_s


def test_long_s():
    assert fix_long_s("Geſchichte") == "Geschichte"
    assert fix_long_s("Geſchichte", keep=True) == "Geſchichte"


def test_dehyphenate():
    assert dehyphenate("Kon-\nitz") == "Konitz"
    assert dehyphenate("Stadt-\n  verordneten") == "Stadtverordneten"


def test_headers_removed():
    assert clean("12\nDer Gymnasiast\n") == "Der Gymnasiast"
