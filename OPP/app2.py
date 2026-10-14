class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

product1 = Product("Laptop", 600000, 4)
print(product1.name)
print(product1.total_value())