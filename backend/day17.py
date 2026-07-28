# day17.py
# the main difference between ( list and Tuples ), is we cannot any changes in Tuples like a list, otherwise it will give us an error
# 1. Creating a tuple (Notice the regular parentheses!)
fixed_dimensions = (1920, 1080)
print("Screen Dimensions:", fixed_dimensions)

# 2. Indexing works exactly like a list!
print("Width:", fixed_dimensions[0])
print("Height:", fixed_dimensions[1])

print("\n--- Let's try to change a tuple item ---")
# Python will block this and throw an error to protect the data!
try:
    fixed_dimensions[0] = 2560
except TypeError as error:
    print("Blocked by Python! Error message:", error)




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



base_location = (34.15 , 71.73)
print("home base coordinate = ", base_location)

print("first number = ", base_location[0])
print("second number = ", base_location[1])



# the main difference between ( list and Tuples ), is we cannot any changes in Tuples like a list, otherwise it will give us an error