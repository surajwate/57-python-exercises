
from exercises import exercise01
import pytest


def test_hello():
    assert exercise01.hello('Suraj') == f'Hello Suraj, nice to meet you!'
