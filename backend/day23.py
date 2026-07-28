# Day 23 Default & keyword arguments

print("--- 1. testing default arguments (Backup values)")

def describe_user(name, country="pakistan"):
    print(f"user name: {name} | country_name: {country}")

# Test A: We provide both values
describe_user("shoaib", "UAE")

# Test B: We leave country blank! It uses the backup default
describe_user("Ali")

print("\n--- 2. Testing Keyword Arguments (Out of Order)")

def show_bill(name, items, price):
    print(f"{name} baught {items} items for RS {price}")

# Normally, we must pass arguments in order: name, items, price.
# But using keywords, we can mix up the order completely!

show_bill(price=100, name="khan", items="cards")


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("my own test")

def make_order(customer_name, food_item, drink = "cock"):
    print(f"oder for {customer_name} food {food_item} with a {drink}")

print("\n Call 1 (Testing Default)")

make_order("shoaib", "burger")
make_order("ali", "sweet", "7up")

print("\n Call 2 (Testing Keywords out of order): ")
make_order(food_item="pizza", customer_name="jan",drink="fanta")