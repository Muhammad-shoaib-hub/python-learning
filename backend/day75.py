# A super simple generator function

def popcorn_machine ():
    print("poping bag 1.. ")
    yield "Bag 1"

    print("poping bag 2.. ")
    yield "Bag 2"

    print("poping bag 3.. ")
    yield "Bag 3"

# Start the machine
Snaks = popcorn_machine()

# Ask for bags one by one using next()
print(next(Snaks))
print(next(Snaks))
print(next(Snaks))




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# ==========================================
# DAY 75: GENERATORS AND ITERATORS
# ==========================================

import sys

# 1. Custom Generator Function
def popcorn_machine():
    yield "Bag 1"
    yield "Bag 2"
    yield "Bag 3"

print("--- 1. Loop through popcorn_machine() ---")
for bag in popcorn_machine():
    print(bag)


# 2. Generator Expression vs List Comprehension
# Note: Generator uses (), List uses []
print("\n")

list_nums = [x for x in range(1,6)]
get_nums = (x for x in range(1,6))

print("\n--- 2. Generator Expression Output ---")
for num in get_nums:
    print("Numbers : ", num)

print("\n--- 3. List Expression Output ---")
for nums in list_nums:
    print("Numbers : ", nums)

# 3. Why Generators Matter: Memory Check!

big_list = [x for x in range(100000)]
big_gen = (x for x in range(100000))

print("\n--- 3. Memory Usage ---")

print("100,000 items in list is = ", sys.getsizeof(big_list), bytes)
print("100,000 itesm in generater is = ", sys.getsizeof(big_gen), bytes)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


def even_streamer(numbers):
    for num in numbers:
        if num % 2 ==0:
            yield num

# Testing 

text_numbers = [12, 7, 19, 24, 30, 41, 58, 99]

for even_num in even_streamer(text_numbers):
    print(even_num)




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# Deal! Here is your Day 75 Challenge #2.

def valid_password_streamer(passwords):
    for password in passwords:
        if len(password) > 8:
            yield password
        else:
            False

# must remember this part please
# must remember this part please

user_passwords = ["pass123", "SecurePass2026!", "12345", "SuperSecretCode", "admin", "PythonDev789!"]

for u_password in valid_password_streamer(user_passwords):
    print(u_password)