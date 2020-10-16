import pytest

def f(x):
    return x + 2

def test_f():
    assert f(2) == 4
