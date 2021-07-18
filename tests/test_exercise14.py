""" pytest for 14: Tax Calculator """
import pytest
from exercises.exercise14 import tax_calculator


def test_tax_calculator_wi():
    assert tax_calculator(10, True) == """The subtotal is $10.00.
The tax is $0.55.
The total is $10.55."""

def test_tax_calculator_others():
    assert tax_calculator(10, False) == """The total is $10.00"""
