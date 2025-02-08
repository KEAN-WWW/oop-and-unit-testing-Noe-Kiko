import pytest
from app.division import divide

def test_division():
    """Divide with numbers """
    # Positive division
    assert divide(9, 9) == 1
    # Float division
    assert divide(5, 2) == 2.5
    # Negative division
    assert divide(-14, 2) == -7


def test_divide_zero_exception():
    """Division testing by zero"""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)