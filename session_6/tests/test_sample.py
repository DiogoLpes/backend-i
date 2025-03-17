from sample import add, multiply, factorial
from pytest import raises


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 1) == 0


def test_factorial():
    with raises(AssertionError, match="deu erro"):
        assert factorial(-1)
        assert factorial(6) == 720
