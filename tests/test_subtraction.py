"""This is the subtraction test file"""
from app.subtraction import subtract


def test_subtraction():
    """Subtract the numbers """
    # Test positive numbers
    assert subtract(4, 2) == 1
    # Test negative numbers
    assert subtract(-2, -5) == 3
    # Test with zero
    assert subtract(20, 0) == 20