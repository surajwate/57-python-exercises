# Test for Exercise 19: BMI Calculator
import pytest
from exercises.exercise19 import bmi_calculator, get_input


@pytest.mark.parametrize("weight, height, result", [(185, 72, "You are overweight. You should see your doctor."), (165, 72, "You are within the ideal weight range."), (135, 72, "You are underweight. You should see your doctor.")])
def test_bmi_calculator(weight, height, result):
    assert bmi_calculator(weight, height) == result
