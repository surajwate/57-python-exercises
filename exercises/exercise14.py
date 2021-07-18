# Exercise 14: Tax Calculator

def tax_calculator(order_amount, state_wi):
    order_amount = float(order_amount)
    if (state_wi == True):
        tax = order_amount * 0.055
        total = order_amount + tax
        return f"""The subtotal is ${order_amount:.2f}.
The tax is ${tax:.2f}.
The total is ${total:.2f}."""
    if (state_wi == False):
        return f"""The total is ${order_amount:.2f}"""

def state_wi(state):
    if state == 'WI':
        return True
    else:
        return False


if __name__ == '__main__':
    order_amount = float(input("What is the order amount? "))
    state = input("What is the state? ")
    state_wi = state_wi(state)
    print(tax_calculator(order_amount, state_wi))
