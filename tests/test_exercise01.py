import pytest

from exercise01 import Greetings


def test_hello():
    assert Greetings.hello('Suraj') == f'Hello, {"Suraj"}, nice to meet you!'
