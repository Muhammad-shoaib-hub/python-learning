# day50.py
# Day 50: Modules and Imports

# 1. Standard Import (import module_name)
# Imports the entire module. You access its contents using module_name.function_name().

# 2. Specific Import (from module_name import function_name)

# 3. Alias Import (import module_name as alias)


print("--- 1. USING BUILT-IN PYTHON MODULES ---\n")

# Method 1: Standard Import
import math

print("Standard import math")
print(f"the square root of 64 is = {math.sqrt(64)}")
print(f"Fectorial of 5 is = {math.factorial(5)}")

# Method 2: Specific Import
from random import randint, choice

print("2. Specific Import (random):")
random_number = randint(1, 10)
print(f" this is random numbre : {random_number}")

fruits = ["Apple", "Banana", "Mango", "Orange"]
selected_fruit = choice(fruits)
print(f"the selected fruit is :", selected_fruit)

# Method 3: Alias Import
import datetime as dt

print("3. Alias Import (datetime as dt):")
current_time = dt.datetime.now()
print(f"the current time is : {current_time}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# Option 1: Import the whole page/file

import day50pr
result = day50pr.add(4,6)
print(result)

# Option 2: Import specific functions/classes from that page

from day50pr import add, Helper
result1 = day50pr.add(2,5)
print(result1)

# remember here, we creat object for class
h = Helper()
h.greet()    # Output: Hello from day50pr.py!


# Option 3: Import the page with a shortcut name (Alias)
import day50pr as dp
result3 = dp.multiply(5, 8)
print(result3)