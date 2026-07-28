# day19.py

# 1. We start with a smart dictionary containing a student's marks
stu_sc = {
    "Maths": 90,
    "science": 95,
    "English": 88
}

print("\n--- using .key() to see all lables---")
# .keys() acts like a magnifying glass that ONLY looks at the sticker labels!
all_subjects = stu_sc.keys()
print("The all subjects are = ", all_subjects)

print("\n--- using .values to see all data ---")
# .values() ignores the labels and ONLY looks at the raw numbers/data inside!
all_marks = stu_sc.values()
print("the all marks = ", all_marks)


# most important


print("\n--- using a loop to print everythin nicely")
# We use .items() when we want to pull out BOTH the key and the value at the same time.
# In the loop, 'subject' grabs the key, and 'score' grabs the value!

for subject, score in stu_sc.items():
    print("shoaib scored = ", score, "in= ",subject)




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




shop_inventory = {
    "laptop": 5,
    "phone": 12,
    "headphne": 15
}

all_products = shop_inventory.keys()
print("The all products are here = ", all_products)

total_products = shop_inventory.values()
print("The totale products that we have = ", total_products)

for name, remain in shop_inventory.items():
    print("the products name = ", name, " --- total remains with us = ", remain)