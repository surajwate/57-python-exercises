from exercises import exercise02
import pytest


def test_count():
    assert exercise02.count('Homer') == 'Homer has 5 characters.'
