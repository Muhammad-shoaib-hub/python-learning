# Day 37 __init__ constructor and attributes

print("--- 1. USING THE __INIT__ CONSTRUCTOR ---")

# Step 1: Define a Class with __init__
class Student:
    def __init__(self, name, course, hours_completed):

        # Attach parameters to the instance using self.attribute_name
        self.name = name
        self.course = course
        self.hours = hours_completed

# Step 2: Create objects by passing arguments directly!
Student1 = Student("shoaib", "python", 38)
Student2 = Student("Ali", "HTML", 39)

# Step 3: Access attributes
print(f"Studen 1 : {Student1.name} - {Student1.course} - {Student1.hours}")
print(f"Studen 2 : {Student2.name} - {Student2.course} - {Student2.hours}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



#self: Python's way of saying "MY OWN" attribute/data.
#Instance Attributes: Data attached to specific objects via self.attribute_name.


# 1.. Define a Class Laptop:
class Laptop:
    def __init__(self, brand, price, ram):
        self.brand = brand
        self.price = price
        self.ram = ram

# 2.. Create Two Laptop Objects:
laptop1 = Laptop("Dell", 800, "16GB")
laptop2 = Laptop("Apple", 1200, "8GB")

# 3.. Print Details:
print(f"Laptop 1..: {laptop1.brand} - {laptop1.price} - {laptop1.ram}")
print(f"Laptop 2..: {laptop2.brand} - {laptop2.price} - {laptop2.ram}")