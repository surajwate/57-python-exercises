# Test for Exercise 16: Legal Driving Age
import pytest
from exercises.exercise16 import legal_driving_age


@pytest.mark.parametrize("age, result", [(15, "You are not old enough to legally drive."), (35, "You are old enough to legally drive.")])
def test_legal_driving_age(age, result):
    assert legal_driving_age(age) == result
