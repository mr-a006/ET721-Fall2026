"""
Aqeel Hussain
Oct 5, 2026
lab 9: unit testing using Pytest
"""

import pytest

from math_utils import *

#exercise 1
def test_multiply():
    assert multiply(3,4) == 12
    assert multiply(-1,5) == -5

def test_divide():
    assert divide(10,2) == 5
    # with tolerance up to two decimal places
    assert divide(10,3) == pytest.approx(3.33, abs=0.01)

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10,0)

# exercise 2
def test_valid_password():
    assert validate_password("pass12345") is True

def test_short_password():
    assert validate_password("pass1") is False

def test_no_number():
    assert validate_password("testingpassword") is False

# exercise 3
# use parametrize to set multiple testing input/output sets
@pytest.mark.parametrize(
    "n, expected",[(2, True),(3,False),(0,True),(-2,True),(7,False)]
)
def test_is_even(n, expected):
    assert is_even(n) == expected

# exercise 4
