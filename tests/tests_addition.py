"""Addition"""
from app.addition import add


def test_addition():
    """ Add the numbers"""
    assert add(3, 3) == 6
    # Test with negative
    assert add(-2, -2) == -4
    # Test with larger numbers
    assert add(300, 300) == 600
    # Test with zero
    assert add(0, 20) == 20
