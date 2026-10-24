class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def generate_bill(self):
        total = 0

        print("----- BILL -----")

        for product in self.products:
            amount = product.total_price()
            print(product.name, ":", amount)
            total += amount

        if total >= 5000:
            discount = total * 0.10
        else:
            discount = 0

        print("Total:", total)
        print("Discount:", discount)
        print("Final amount:", total - discount)


cart = ShoppingCart()

cart.add_product(Product("Laptop", 45000, 1))
cart.add_product(Product("Mouse", 500, 2))

cart.generate_bill()