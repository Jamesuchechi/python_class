def calculate_total(price: float, quantity: int) -> float:
    return price * quantity

def calculate_discount(total: float) -> float:
    return total * 0.2

def calculate_final_price(price: float, quantity: int) -> float:
    total = calculate_total(price, quantity)
    discount = calculate_discount(total)

    return total - discount

final_price = calculate_final_price(8000, 19)
print(final_price)