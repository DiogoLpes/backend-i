from sample import add
from sample import multiply
import math

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0  
    
def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 1) == 0

def test_factorial():
    
    for i in range (1, n+1):
        if n >= 1:
            factorial = factorial *i