def get_details(total_items: int) -> tuple:
    """Get input from the user and create lists of quantity and price of item purchased.

    Args:
        total_items (int): total items purchased

    Returns:
        tuple: tuple of quantity and price lists
    """
    quantity_list: list = []
    price_list: list = []
    for i in range(total_items):
        quantity = int(input(f"Enter the quantity of item {i+1}: "))
        price = int(input(f"Enter the price of item {i+1}: "))
        quantity_list.append(quantity)
        price_list.append(price)
    return (quantity_list, price_list)


def self_checkout(quantity_list: list, price_list: list) -> str:
    """Return the string of calculated subtotal, tax and total price of purchased items.

    Args:
        quantity_list (list): List of quantity of items purchased.
        price_list (list): List of the prices of the items purchased.

    Returns:
        str: String to display the result i.e. total price.
    """
    subtotal: int = 0
    for i in range(len(quantity_list)):
        subtotal += (quantity_list[i] * price_list[i])
    subtotal = float(subtotal)
    tax = subtotal * 0.055
    total = subtotal + tax
    return f"""Subtotal: ${subtotal:.2f}
Tax: ${tax}
Total: ${total}"""


def display_total(total_items):
    a, b = get_details(total_items)
    return self_checkout(a, b)


if __name__ == '__main__':
    total_items = int(input("How many items do you have? "))
    print(display_total(total_items))
