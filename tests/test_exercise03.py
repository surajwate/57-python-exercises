from exercises import exercise03


def test_quote():
    assert exercise03.quote('The purpose of our lives is to be happy.',
                            'Dalai Lama') == 'Dalai Lama says, "The purpose of our lives is to be happy."'
