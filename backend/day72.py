import re

user_email = input("please enter your email = ")
email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(email_pattern, user_email):
    print("Email is correct")
else:
    print("wrong patteren")


print("\n")

# 2. Simple Password Check (Needs at least 1 number)

user_password = input("please enter your password = ")
if re.search(r"\d", user_password):
    print("password contains a number")
else:
    print("wrong, password mus contain at least one number")