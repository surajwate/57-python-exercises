# Test for Exercise 17: Temperature Converter
import pytest
from exercises.exercise18 import temperature_converter


@pytest.mark.parametrize("convert, temperature, result",
                         [("C", 32, ("Celsius", 0)), ("C", 77, ("Celsius", 25)),
                          ("C", 95, ("Celsius", 35)), ("F", 30, ("Fahrenheit", 86)),
                          ("F", 35, ("Fahrenheit", 95)), ("F", 40, ("Fahrenheit", 104))])
def test_temperature_converter(convert, temperature, result):
    assert temperature_converter(convert, temperature) == result
