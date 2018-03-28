
from citest import main


def test_zero():
    assert main.square(0) == 0


def test_positive():
    assert main.square(5) == 25
    assert main.square(1) == 1
    assert main.square(1000) == 1000000


def test_negative():
    assert main.square(-5) == 25
    assert main.square(-1) == 1
    assert main.square(-1000) == 1000000
