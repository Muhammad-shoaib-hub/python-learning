# day 18 (Dictionaries - key/value basics)

# 1. Creating a dictionary of a user profile
# Key : Value




user_profile = {
    "name": "shoaib",
    "role": "python developer",
    "current_day": 18,
    "is_learning_fast": True
}

print("full user profile Dictionary = ", user_profile)

print("\n--- Accessing values using keys---")
# Instead of using numbers like user_profile[0], we use the key name!
print("developer name = ", user_profile["name"])
print("what is his role? = ", user_profile["role"])
print("how many days he covered = ", user_profile["current_day"])
print("is he learning fast? = ", user_profile["is_learning_fast"])



print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



phone_specs = {
    "brand": "samsung",
    "model": "Galaxy S24",
    "ram_gb": 8,
    "is_5g": True
}

print("\n")
print("\n")

print("about mobile = ", phone_specs)
print("mobile brand = ", phone_specs["brand"])
print("mobile model = ", phone_specs["model"])
print("mobile ram = ", phone_specs["ram_gb"])
print("is it 5 G phone ?  = ", phone_specs["is_5g"])