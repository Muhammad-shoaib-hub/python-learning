# day22.py (Day 22 Defining functions, parameters, return values)

print("--- 1.  Making our first custom function machine ")

# We use 'def' to define/build our machine. 
# 'name' is the input slot (Parameter)

def greet_user(name):
    print("hello", name)
    print(" welcome to Day 22 Defining functions, parameters, return values ")

# Now we press the start button on our machine by calling it!
greet_user("shoaib")


print("\n--- 2. A machine that returns data back to us ---")
def add_numbers(num1, num2):
    result = num1 + num2
    return result

totl = add_numbers(4,5)
print("the total amount is = ", totl)



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


def calculate_squre(number):
    result1 = number * number
    return result1

squre = calculate_squre(5)
print("the squre of 5 is = ", squre)

ans = calculate_squre(7)
print("the squre of 7 is = ", ans)



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("---- Its for taking inputer from user ---")
def user_squre():
    user_number = int(input("please enter number for squre = "))
    result2 = user_number * user_number
    return result2

user_sq = user_squre()
print("user squre is = ", user_sq)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("---- 2 . Its for taking inputer from user ---")
def enter_value():
    en_value = int(input("please enter 2 valure for squre = "))
    result3 =  en_value * en_value
    return result3

user2_sq = enter_value()
print("its the 2 squre of user value = ", user2_sq)



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("--- 5. this is for trying multi operation in function ---")
def dynamic_calculater(numb1, numb2,operation):
    if operation == "+":
        return numb1 + numb2
    elif operation == "-":
        return numb1 - numb2
    elif operation == "*":
        return numb1 * numb2
    elif operation == "%":
        return numb1 % numb2
    else:
        return "invalied opereation"

# 1. Let's try Multiplcation (*)
multi_ans = dynamic_calculater(4,5,"*")
print("the multiplication are here = ", multi_ans)

# 2. Let's try Subtraction (-)
sub_ans = dynamic_calculater(4,3,"-")
print("the subtract are here = ", sub_ans)

# 3. Let's try Addition (+)
add_ans = dynamic_calculater(7,4,"+")
print("the addition are here = ", add_ans)



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("--- 6. this is for trying multi operation (from user side ) in function ---")

def user_calculater():
    nu1 = int(input("please enter first number = "))
    nu2 = int(input("please enter second number = "))
    operation = input("Enter operation symbol (+, -, *, /) = ")

    # 2. Check the operation and calculate the result
    
    if operation == "+":
        return nu1 + nu2
    elif operation == "-":
        return nu1 - nu2
    elif operation == "*":
        return nu1 * nu2
    elif operation == "/":
        return nu1 / nu2
    else:
        return "sorry wrong operation"

final_ans = user_calculater()
print("the output is here of what you types = ", final_ans)