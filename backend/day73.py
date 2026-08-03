# ❌ Old Way (Standard for loop):

numbers = [1, 2, 3, 4, 5, 6, 7]
squares = []

for num in numbers:
    squares.append(num*num)
print(squares)

# ===============================================================================
# ===============================================================================

print("\n")
print("\n")
# ===============================================================================

# ✅ New Way (List Comprehension):

numbers = [1, 2, 3, 4, 5, 6, 7]
squares = [num * num for num in numbers]

print(squares)


# ===============================================================================
# ===============================================================================

print("\n")
print("\n")
# ===============================================================================


# ==========================================
# DAY 73: LIST COMPREHENSIONS
# ==========================================


# Filter Data (Only keep even numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)

# ===============================================================================
# ===============================================================================

# Clean String Data (Backend use-case: format user input)
raw_names = ["  shoaib ", "  ALI", "  Ahmad  "]
clean_name = [name.strip().title() for name in raw_names]
print("clean Name : ", clean_name)


# ===============================================================================
# ===============================================================================

# Combine Filtering & Transformation (Double only odd numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
double_data = [x*2 for x in numbers if x % 2 != 0]
print("double data : ", double_data)