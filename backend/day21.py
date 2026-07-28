# day21.py

# 1. We create a dictionary inside a dictionary (Nested Dictionary)
# The person's name is the Key. Their phone and email are stored inside another dictionary!

contact_book = {
    "shoaib": {
        "phone": "0208383303",
        "email": "shoaib@email.com"
    },
    "ali": {
        "phone": "2828828828",
        "email": "ali@email.com"
    }
}

print("---1. Reading one contact info ( form ali)")
# To get Ali's phone number, we go to "Ali" first, then grab "phone"
print("Ali phone number is = ", contact_book["ali"]["phone"])

print("---2. Reading another cantact info (shoaib)")
print("Shoaib email is = ", contact_book["shoaib"]["email"])

print("---3. Adding a new contact to ( cantact_book)")
contact_book["Zain"] = {
    "phone": "484848484939",
    "email": "zain@email.com"
}

print("Zain has been added to contact_book")

print("--- adding my new version ( shoaib 1)")
contact_book["shoaib1"] = {
    "phone": "4848484839392",
    "email": "shoaib1@email.com"
}
print("---4. printing all contact using loop")
for name, info in contact_book.items():
    print("Contact Name = ", name)
    print("phone number = ", info["phone"])
    print("Contact email = ", info["email"])

print("*"*70)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

print("--- adding my new version ( shoaib 1)")
contact_book["shoaib1"] = {
    "phone": "4848484839392",
    "email": "shoaib1@email.com"
}


print("---4. printing all contact again after adding shoaib1 using loop")
for name, info in contact_book.items():
    print("Contact Name = ", name)
    print("phone number = ", info["phone"])
    print("Contact email = ", info["email"])

print("*"*70)