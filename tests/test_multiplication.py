"""Multiplication Test File"""
from app.multiplication import multiply


def test_multiplication():
    """ Multiply the numbers"""
    # Test positive numbers
    assert multiply(3, 3) == 9
    # Test negative with positive
    assert multiply(-4, 4) == -16
    # Test with zero
    assert multiply(10, 0) == 0