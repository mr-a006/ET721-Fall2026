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
    assert multiply(-1,5) == 5

def test_divide():
    assert divide(10,2) == 5
    # with tolerance up to two decimal places
    assert divide(10,3) == pytest.approx(0.33, abs=0.01)

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