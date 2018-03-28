
from citest.main import square


def test_zero():
    assert square(0) == 0


def test_positive():
    assert square(5) == 25
    assert square(1) == 1
    assert square(1000) == 1000000


def test_negative():
    assert square(-5) == 25
    assert square(-1) == 1
    assert square(-1000) == 1000000
