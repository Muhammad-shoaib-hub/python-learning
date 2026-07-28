# day51.py
# Day 51: Creating your own modules/packages

# Module: A single .py file that contains reusable functions, classes, or variables.
# Package: A folder containing multiple modules (multiple .py files) grouped together.


print("--- 1. IMPORTING FROM A CUSTOM MODULE ---")

# Importing from our custom module math_tools.py

import math_tools
from math_tools import Calculater

result_sum = math_tools.add_numbers(10, 20)
print(f"10 + 20 = {result_sum}")

calc = Calculater()
print(f"2 to the power 3 = {calc.power(2, 3)}")


print("\n" + "-"*50 + "\n")


print("--- 2. IMPORTING FROM A CUSTOM PACKAGE ---")

# Importing from modules inside my_package folder
from my_package.greeting import say_hello
from my_package.formater import make_bold

message = say_hello("Shoaib")
formatted_msg = make_bold(message)

print(message)
print(f"Formatted: {formatted_msg}")