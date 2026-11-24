from calculator import add, divide, multiply, subtract


def test_add():
    assert add(3, 2) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5
