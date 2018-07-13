"""
Test module for Fibonacci function.
"""
import pytest
from operations.trampoline import fibonacci


FIBONACCI = [1, 1, 2, 3, 5, 8]


def test_fibonacci_of_0():
    assert fibonacci(0) == []


def test_fibonacci_of_1():
    assert fibonacci(1) == FIBONACCI[:1]


def test_fibonacci_of_2():
    assert fibonacci(2) == FIBONACCI[:2]


def test_fibonacci_of_3():
    assert fibonacci(3) == FIBONACCI[:3]


def test_fibonacci_of_4():
    assert fibonacci(4) == FIBONACCI[:4]


def test_fibonacci_of_5():
    assert fibonacci(5) == FIBONACCI[:5]

@pytest.mark.fibo
def test_fibonacci_of_10_000():
    assert len(fibonacci(10_000)) == 10_000

