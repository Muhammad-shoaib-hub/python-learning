# Day 38 Methods and self
# very very important 
# very very important 
# very very important 
# very very important 
# very very important 




print("--- 1..Adding methods to a class---")

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course
        self.completed_lessons = 0  # Default attribute

    # Method 1: Display profile
    def introduce(self):
        print(f"Hi i am {self.name} and i am learning {self.course}")

    # Method 2: Perform an action that modifies data
    def complete_lesson(self, lesson_name):
        self.completed_lessons += 1
        print(f"{self.name} completed lessons {self.course} ! total completed: {self.completed_lessons}")

# Step 2: Create an object
Student1 = Student("shoaib", "python")

# Step 3: Call the methods on the object!
Student1.introduce()
Student1.complete_lesson("java and C++")
Student1.complete_lesson("HTML")
Student1.complete_lesson("C")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"your new balance = {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("new balance = ", self.balance)
        else:
            print("Insufficient funds!")

    def display_balance(self):
        print(f"{self.account_holder} and current balance is : {self.balance}")

account = BankAccount("shoaib", 100)

account.deposit(50)
account.withdraw(30)
account.withdraw(200)

account1 = BankAccount("shoaib1", 100)
account1.deposit(20)
account1.withdraw(40)
account1.withdraw(200)
            