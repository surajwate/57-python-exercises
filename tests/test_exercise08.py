# Pizza Party Test

from exercises import exercise08


def test_pizza_party():
    assert exercise08.pizza_party(8, 2) == """8 people with 2 pizzas
Each person gets 2 pieces of pizza.
There are 0 leftover pieces."""
