from exercises.exercise13 import compound_interest

def test_compound_interest():
    assert compound_interest(1500, 4.3, 6, 4) == """$1500 invested at 4.3% for 6 years
compounded 4 times per year is $1938.84."""