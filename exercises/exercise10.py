def get_details(total_items:int):
    quantity_list:list = []
    price_list:list = []
    for i in range(total_items):
        quantity = int(input(f"Enter the quantity of item {i+1}: "))
        price = int(input(f"Enter the price of item {i+1}: "))
        quantity_list.append(quantity)
        price_list.append(price)
    return (quantity_list, price_list)

def self_checkout(quantity_list, price_list)->str:
    subtotal:int = 0
    for i in range(len(quantity_list)):
        subtotal += (quantity_list[i] * price_list[i])
    subtotal = float(subtotal)
    tax = subtotal * 0.055
    total = subtotal + tax
    return f"""Subtotal: ${subtotal:.2f}
Tax: ${tax}
Total: ${total}"""

def calculate_total(total_items):
    a, b = get_details(total_items)
    return self_checkout(a, b)


if __name__ == '__main__':
    total_items = int(input("How many items do you have? "))
    print(calculate_total(total_items))
