"""This is the addition test file"""
from app.addition import add


def test_addition():
    """ Add the numbers"""
    assert add(3, 3) == 6