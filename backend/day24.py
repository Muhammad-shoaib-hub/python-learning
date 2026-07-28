#Day 24 *args and **kwargs
#  *args (Arguments with 1 Star):
#  **kwargs (Keyword Arguments with 2 Stars)
print("--- 1. Testing *args (Infinite Plain Inputs) ---")
def make_pizza(size, *types):
    print(f"make a {size} pizza with these types :")
    for type in types:
        print(f"{type}")

# Test A: Pizza with 2 toppings
make_pizza("medium", "didl", "iekd")

# Test B: Pizza with 4 toppings!
make_pizza("large", "dkdkd", "diee", "dkdk", "iedk")

print("\n" + "="*40)
print("--- 2. Testing **kwargs (Infinite Labeled Inputs) ---")

# The ** tells Python: "Accept any extra named labels!"

def built_profile(first, last, **extra_info):
    print(f"{first} {last}")
    for key, value in extra_info.items():
        print(f"{key} : {value}")

# We pass extra details using equal signs (=)
built_profile("shan", "sha", city = "alie", Country = "pakistan", age = 44)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("\n---Part 1: Testing *args (The Grocery Cart)---")
def show_cart(cus_name, *items):
    print(f"{cus_name}'s shoping cart contains ")
    for item in items:
        print(f"{item}")


show_cart("shoaib khan", "milk", "eggs", "bread")

print("\n---Part 2: Testing **kwargs (The Shipping Label)---")

def print_shipping_label(traking_id, **address):
    print(f"{traking_id}")
    for location, name in address.items():
        print(f"{location} : {name}")

print_shipping_label("khan1", country="pakistan", provenic="kpk", city="peshawar")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("\n--- User Input with *args ---")

user_grocery_list = []

print("Enter items for your cart (type 'stop' when you are done):")
while True:
    user_item = input("> ")
    if user_item.lower() == "stop":
        break
    user_grocery_list.append(user_item)

# The MAGIC trick: Putting a * before the list unpacks it into *args!
show_cart("Shoaib", *user_grocery_list)



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("\n--- User Input with **kwargs ---")

user_address_dict = {}

print("Enter address details (like city, country, etc.)")
print("Type 'stop' as the label name when finished.\n")

while True:
    label = input("Enter label name (e.g., city, country): ")
    if label.lower() == "stop":
        break
    value = input(f"Enter value for {label}: ")
    
    # Save it into our temporary dictionary
    user_address_dict[label] = value

# The MAGIC trick: Putting ** before the dictionary unpacks it into **kwargs!
print_shipping_label("TRACK123", **user_address_dict)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("\n  example 1: using *args in function getting data from user")
print("\n--- Part 1: Grocery Cart (All Inputs Inside) ---")

def user_cart():
    cus_name = input("please enter customer name = ")

    # We create an empty list inside the machine to hold the items
    
    items_list = []
    while True:
        item = input("please enter you item (type 'stop' when you done = )")
        if item.lower()== "stop":
            break
        items_list.append(item)

    # Now print the final summary
    print(f"{cus_name} shoping cart containes :")
    for single_item in items_list:
        print(f"{single_item}")

# Call the function completely empty!
user_cart()


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("\n example 2: **kwargs in function to get data from user")
print("--- Part 2: Shipping Label (All Inputs Inside) ---")
print("\n")

def user_shoping_lable():
    user_ID = input("please enter your ID = " )

    # We create an empty dictionary inside the machine to hold the address labels
    
    address_dict = {}
    while True:
        label = input(" please enter a lable name e.g city, country (and type ' stop ' when you done) = ")
        if label.lower() == "stop":
            break
        value = input(f" please enter value for {label}: ")

        # Save it directly into our dictionary
        address_dict[label] = value

    # Now print the final summary
    print(f"\n user ID = {user_ID}")
    for location, name in address_dict.items():
        print(f"{location} : {name}")

# Call the function completely empty!
user_shoping_lable()
