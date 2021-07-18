# test for Exercise 21: Numbers to Names
from exercises.exercise21 import number_to_name
import pytest

@pytest.mark.parametrize("number, month", [(1, "The name of the month is January."), (7, "The name of the month is July."), (11, "The name of the month is November.")])
def test_number_to_name(number, month):
    assert number_to_name(number) == month