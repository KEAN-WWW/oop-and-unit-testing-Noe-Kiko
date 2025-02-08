import pytest
from app.division import divide

def test_division():
    """ Divide the numbers"""
    assert divide(4, 4) == 1

def test_divide_zero_exception():
    """Divide by zero"""
    with pytest.raises(ZeroDivisionError):
        divide(2,0)