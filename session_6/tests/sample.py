def add(a: int, b: int) -> int:
    return a + b


def multiply(a: int, b: int) -> int:
    return a * b


def factorial(a: int) -> int:
    if a < 0:
        raise AssertionError("deu erro")
    if a == 1 or a == 0:
        return 1
    else:
        return (a * factorial(a-1))
