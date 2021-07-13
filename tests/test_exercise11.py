# Test for currency conversion
from exercises.exercise11 import currency_conversion

def test_currency_conversion():
    assert currency_conversion(81, 137.51) == """81 euros at an exchange rate of 137.51 is
111.38 U.S. dollars."""