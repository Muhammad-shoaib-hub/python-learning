# for super()

class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, num_doors):
        # Pass brand & speed to Vehicle's __init__
        super().__init__(brand, speed)
        # Add new attribute specific to Car
        self.num_doors = num_doors


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# for Multiple Inheritance

class Flyer:
    def fly(self):
        print("Flying high!")

class Swimmer:
    def swim(self):
        print("Swimming fast!")

# Duck inherits from BOTH Flyer and Swimmer!
class Duck(Flyer, Swimmer):
    pass


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



print("--- 1. USING super() ---")

# parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Child Class using super()

class Student(Person):
    def __init__(self, name, age, id):
        # Call Person's __init__ to handle name and age
        super().__init__(name, age)

        # Handle student_id inside Student
        self.id = id

    def display_student(self):
        print(f"Student : {self.name}-- Age : {self.age}-- ID : {self.id} ")

Student1 = Student("shoaib", 23, "32loo")
Student1.display_student()

print("\n")
print("\n")

print("\n--- 2. MULTIPLE INHERITANCE ---")

# parent 1
class Camera:
    def take_photo(self):
        print("photo taken")

# parent 2
class Phone:
    def make_call(self):
        print("calling")

# Child inheriting from BOTH Camera and Phone
class Smartphone(Camera, Phone):
    def __init__(self, model):
        self.model = model

device = Smartphone("ViVo")
device.take_photo()
device.make_call()

# remember this point 
# remember this point 
print(f"Device : {device.model}")


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# 1 .. Part A: Using super()

# parent class

class Vechile:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

# child class
class Car(Vehicle):
    def __init__(self, brand, speed, self_doors):
        super().__init__(brand, speed)
        self.doors = self_doors

    def car_info(self):
        print(f"Brand : {self.brand}-- Speed : {self.speed} -- number of doors : {self.doors}")

car1 = Car("BMW", 120, 4)
car1.car_info()


print("\n")
print("\n")


# 2.. Part B: Multiple Inheritance

class Battery:
    def charge(self):
        print("🔋 Battery is charging...")


class ElectricCar(Car, Battery):
    pass


# Testing
tesla = ElectricCar("Tesla", 200, 4)

tesla.car_info()
tesla.charge()