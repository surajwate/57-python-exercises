from exercises import exercise06

def test_retirement_calulator():
    assert exercise06.retirement_calulator(25, 65) == """You have 40 years left until you can retire.
It's 2021, so you can retire in 2061."""