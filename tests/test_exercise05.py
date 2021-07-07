from exercises import exercise05


def test_simple_math():
    assert exercise05.simple_math(10, 5) == """10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2"""
