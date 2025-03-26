# tests/test_fibonacci.py
import pytest
from src.fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(5) == 5
    assert fibonacci(10) == 55

def test_fibonacci_negative():
    with pytest.raises(ValueError):
        fibonacci(-4)
