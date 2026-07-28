# Day 39 Class variables vs instance variables

print("--- 1. CLASS VARIABLES VS INSTANCE VARIABLES ---")

class Student:
    # Class Variable (Shared across all instances)
    school_name = "Coding Acadmy"
    total_student = 0

    def __init__(self, name):
        # Instance Variable (Unique to each instance)
        self.name = name

        # Every time a new student is created, increment the class variable!
        Student.total_student += 1

# Create instances
Student1 = Student("shoaib")
Student2 = Student("Ali")

# Instance variables are unique
print(f"Student 1 : {Student1.name}")
print(f"Student 2 : {Student2.name}")

# Class variables are shared by all instances
print(f"Studen 1 : {Student1.name} - School name {Student.school_name}")
print(f"Studen 2 : {Student2.name} - School name {Student.school_name}")

# Total count tracked across the entire class
print(f"total student in school is = {Student.total_student}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# 1.. Define a Class

class Employee:
    company_name = "khan"
    total_empolyees = 0

    def __init__(self, name, position):

        #Set instance variables self.name and self.position.
        self.name = name
        self.position = position
        Employee.total_empolyees += 1

    def display_info(self):
        print(f"Name: {self.name}- postion :{self.position}- company name: {Employee.company_name}- total number of empolyees {Employee.total_empolyees}")

Employee1 = Employee("shoaib", "Student1")
Employee2 = Employee("Ali", "Student2")
Employee3 = Employee("khan", "Student3")

Employee1.display_info()
Employee2.display_info()
Employee3.display_info()