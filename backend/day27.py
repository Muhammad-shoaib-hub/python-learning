print("Today's Exercises: The Function Master Challenge")
print("\n")
print("Exercise 1: Standard Function with Default Argument")

def calculate_total(price, tax_rate= 0.05):
    total_price = price + (price * tax_rate)
    print(f"total price including the tax is = {total_price}")

calculate_total(100)
calculate_total(200, 0.10)

print("\n")
print("\n")

print("Exercise 2: Dynamic Arguments (*args)")
print("\n")

def find_max_num(*numbers):
    # max(numbers) automatically picks the biggest number in *args!
    biggest = max(numbers)
    print("the biggest number is = ", biggest)

find_max_num(4, 5, 2, 9, 20, 22, 40)


print("\n")
print("\n")

print("Exercise 3: Scope & Global Update")
print("\n")

total_score = 0
def add_score(points):
    global total_score
    total_score = total_score + points

add_score(50)
add_score(25)
print("the total score outisde the function is = ", total_score)

print("\n")
print("\n")

print("Exercise 4: Lambda Function")
print("\n")

is_positive = lambda a: a > 0
print("is the number is grater (10) than 0 = ", is_positive(10))
print("is the number is grater (-4) than 0 = ", is_positive(-4))