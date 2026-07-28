#  Day 43 Inheritance - basics

# parent Class

class Animals:
    def eat(self):
        print("this animal eat food ")

# Child Class inherits from Animal

class Dog(Animals):
    def bark(self):
        print("woof! woof!")

# Create a Dog object
my_dog = Dog()

# Dog can call both its OWN method and its PARENT'S method!
my_dog.eat()      # Inherited from Animal
my_dog.bark()     # Defined inside Dog


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


print("--- 1. INHERITANCE BASICS ---")

# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"i am {self.name}, and my age is {self.age}")

# Child Class inheriting from Person
class Student(Person):
    def study(self, subjects):
        print(f"{self.name} is studing {subjects}.")

# Creating a Student instance
Student1 = Student("shoaib", 23)

# Calling inherited method from Person
Student1.introduce()

# Calling Student's own method
Student1.study("python")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

# parent class
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(f"The P{self.brand} is driving at {self.speed} km/h")

# child class

class Car(Vehicle):
    def play_music(self, song_name):
        print(f"playing {song_name} in the {self.brand}")


# Test Your Classes:
# Create a Car object

car1 = Car("BMW", 120)

# call
car1.drive()
car1.play_music("--The end of begining--")