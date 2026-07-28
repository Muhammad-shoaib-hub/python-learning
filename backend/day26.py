# day26.py

print("--- 1. Simple Lambda (Single Input) ---")

# Standard def vs Lambda
# Lambda format = lambda input: expression

squre = lambda num: num * num 
print("the squre of 5 is = ", squre(5))
print("the squre of 6 is = ", squre(6))
print("the squre of 8 is = ", squre(8))

print("\n")
print("\n--- 2. Lambda with Multiple Inputs ---")

# A lambda that adds two numbers together
add_number = lambda a,b: a + b
print("the addition of 10 and 44 is = ", add_number(10,44))
print("the addition of 4 and 10 is = ", add_number(4,10))

print("\n")
print("\n--- 3. Quick Decision Lambda ---")

# Check if a number is even (returns True or False)
is_even = lambda y : y % 2 == 0
print("is 9 even = ", is_even(9))
print("is 40 even = ", is_even(40))
print("is 4 even = ", is_even(4))


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("Test 1 (Multiply by 10):")
multiply_by_ten = lambda x: x * 10
print("the multiply of 5 by 10 is here = ", multiply_by_ten(5))

print("\n")
print("Test 2 (Calculate Discount Price):")
apply_discount = lambda price, discount : price - discount
print("the discount for you is here = ", apply_discount(100, 15))

print("\n")
print("Test 3 (Uppercase Name Formatter):")
format_name = lambda name : name.upper()
print("the upercase of our input is = ", format_name("shoaib"))