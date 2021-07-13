from exercises import exercise10

def test_self_checkout():
    assert exercise10.self_checkout([25, 10, 4], [2, 1, 1]) == """Subtotal: $64.00
Tax: $3.52
Total: $67.52"""