class ShoppingCart:
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.total_price = 0.0

    def add_item(self, item_name, price):
        self.items.append(item_name)
        self.total_price += price
        print(f"Added {item_name} (${price}) to cart.")

    def remove_item(self, item_name, price):
        if item_name in self.items:
            self.items.remove(item_name)
            self.total_price -= price
            print(f"Removed {item_name}.")
        else:
            print(f"Item {item_name} is not in your cart!")

    def checkout(self):
        if not self.items:
            print("Your cart is empty!")
        else:
            print(f"Customer: {self.customer_name}")
            print(f"Items: {self.items}")
            print(f"Grand Total: ${self.total_price}")


# Testing
cart = ShoppingCart("Shoaib")

cart.add_item("Keyboard", 50)
cart.add_item("Mouse", 25)
cart.add_item("Headphones", 75)

cart.remove_item("Mouse", 25)

cart.checkout()