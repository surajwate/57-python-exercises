def pizza_party(people, pizza):
    pizza_pieces = pizza * 8
    pizza_pieces_per_person = pizza_pieces//people
    leftover_pizza_pieces = pizza_pieces % people
    return f"""{people} people with {pizza} pizzas
Each person gets {pizza_pieces_per_person} pieces of pizza.
There are {leftover_pizza_pieces} leftover pieces."""


if __name__ == '__main__':
    people = int(input("How many people? "))
    pizza = int(input("How many pizzas do you have?"))
    print(pizza_party(people, pizza))
