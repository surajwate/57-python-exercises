# Test for Exercise 17: Blood Alcohol Calculator
import pytest
from exercises.exercise17 import blood_alcohol_calculator

@pytest.mark.parametrize("A, W, G, H, result", [(4, 176, "M", 4, "not legal"), (3, 176, "M", 4, "legal"), (4, 176, "F", 4, "not legal"), (3, 176, "F", 4, "legal"), (4, 176, "M", 6, "legal"), (4, 150, "F", 9, "legal")])
def test_blood_alcohol_calculator(A, W, G, H, result):
    assert blood_alcohol_calculator(A, W, G, H) == result