import argparse

user_age = argparse.ArgumentParser(description="🎯 Challenge: The User Age Classifier CLI")

user_age.add_argument("--name", type=str, default="Guest", help="here we have a Guest")
user_age.add_argument("--age", type=int, default=18, help="here we have a user age")

u_a = user_age.parse_args()

if u_a.age < 13:
    status = "child"

elif u_a.age > 13 and u_a.age < 19:
    status = "Teenager"

elif u_a.age >= 20:
    status = "Adult"


print(f"👤 Name: {u_a.name}")
print(f"🎂 Age: {u_a.age}")
print(f"🏷️ Category: {status}")