# Day 36 Classes and objects - the basics

print("---1.. creating our first class and objects---")
# Step 1: Define a Class (Blueprint)
class Student:
    pass  #'pass' is a placeholder so Python doesn't throw an error empty class

# Step 2: Create Objects (Instances) from the Class
Student1 = Student()
Student2 = Student()

# Print the objects to see what Python sees!
print(Student1)
print(Student2)

print("\n--- 2. ADDING ATTRIBUTES (DATA) TO OBJECTS ---")
Student1.name = "shoaib"
Student1.course = "python backend"

Student2.name = "Ali"
Student2.course = "HTML"

# Print individual properties
print(f"Student 1 : {Student1.name} - {Student1.course}")
print(f"Student 2 : {Student2.name} - {Student2.course}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# 1..Define a Class:
class Cars:
    pass

# 2..Create Two Objects:
Car1 = Cars()
Car2 = Cars()

# 3..Attach Attributes (Data):
Car1.brand = "Toyota"
Car1.model = "Corolla"
Car1.year = 2022

Car2.brand = "Honda"
Car2.model = "Civic"
Car2.year = 2024

# 4..Print Details:
print(f"Car : {Car1.brand} - {Car1.model}, {Car1.year}")
print(f"Car : {Car2.brand} - {Car2.model}, {Car2.year}")