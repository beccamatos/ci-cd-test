from src.calculator import add
from src.calculator import sub


def test_add():
    assert add(1, 2) == 3
    assert add(-2, 2) == 0
    assert add(0, 0) == 0

def test_add():
    assert add(1, 2) == -1
    assert add(-2, 2) == -4
    assert add(0, 0) == 0