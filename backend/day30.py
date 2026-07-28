# day30.py

print("--- 1. Creating and Raising a Custom Exception ---")

# Step 1: Define custom exception classes
class negative_value_error(Exception):
    pass

class balance_too_loo_Error(Exception):
    pass

# Step 2: Function that uses the custom exceptions
def withdraw_money(balance, amount):
    if amount < 0:
        raise negative_value_error("withdraw amount must be gratter than 0 ")
    if amount > balance:
        raise balance_too_loo_Error(f"you try to draw the amount {amount} but your balance is {balance} is this ")
    
    new_balance = balance - amount
    print("you new balance is this = ", new_balance)
    return new_balance

# Step 3: Handling the custom exceptions safely with try/except

try:
    my_balance = 100
    print("current balance is = ", my_balance)

    # Test 1: Valid withdrawal
    my_balance = withdraw_money(my_balance, 20)
    
    # Test 2: Triggering BalanceTooLowError
    my_balance = withdraw_money(my_balance, 140)

except negative_value_error as e:
    print(f"costum error : {e}")

except balance_too_loo_Error as e:
    print(f"NOtice : {e}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



# 1. Define two custom error names (just 1 line each!)

class invalid_age_error(Exception): pass
class under_age_error(Exception): pass

# 2. Function that checks age rules

def Check_voting_aligibitlity(age):
    if age < 0:
        raise invalid_age_error("age cannot be negative ")
    if age < 18:
        raise under_age_error("you are too younge for voting ")
    else:
        print("yes you can vote")

# 3. Test with try/except

try:
    Check_voting_aligibitlity(3)

except invalid_age_error as e:
    print(f"look it : {e}")
except under_age_error as e:
    print(f"Note it : {e}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("---- Day 30 Practice Challenge----")
class password_too_short_error(Exception): pass

def check_password(password):
    if len(password) < 6:
        raise password_too_short_error("the password must be 6 latter long ")
    else:
        print("password accepted")

try:
    check_password("shoaib khan")
except password_too_short_error as e:
    print(f"Note it : {e}")