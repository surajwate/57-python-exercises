# Test for Exercise 15: Password validation
import pytest
from exercises.exercise15 import password_validation

@pytest.mark.parametrize("test_input,expected", [("12345", "I don't know you."), ("abc$123", "Welcome!")])
def test_password_validation(test_input,expected):
    assert password_validation(test_input) == expected
