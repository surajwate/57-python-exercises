from exercises.exercise12 import simple_interest

def test_simple_interest():
    assert simple_interest(1500, 4.3, 4) == """After 4 years at 4.3%, the investment will
be worth $1758."""