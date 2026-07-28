# Day 46 Polymorphism

# 🔑 Method Overriding
# In Python, we achieve polymorphism through Method Overriding. A child class provides its own
# specific implementation of a method that is already defined in its parent class.

print("--- 1. POLYMORPHISM & METHOD OVERRIDING ---")

# parent class
class Animal:
    def make_sound(self):
        print("here are the Animals sounds")

# 1.. child class
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")

# 2.. child class
class Cat(Animal):
    def make_sound(self):
        print("Meow! Meow!")

# 3.. child class
class Cow(Animal):
    def make_sound(self):
        print("Moo! Moo!")

# Demonstration of Polymorphism in a Loop
Animals = [Dog(), Cat(), Cow()]


# remember this part 

for animal in Animals:
    animal.make_sound()   # Same method call, different behaviors!



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# parent class
class Shape:
    def calculate_area(self):
        print("Area calculation not implemented for generic shape.")

# 1.. child class
class Rectengle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        area = self.width * self.height
        print("Rectengle Area = ", area)

# 2.. child class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        area = 3.14 * self.radius * self.radius
        print("Circle area = ", area)


shapes = [ Rectengle(5, 10), Circle(7)]

for sheap in shapes:
    sheap.calculate_area()




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")




# Parent Class (The Blueprint)
class Character:
    def action_button(self):
        print("Generic character action!")

# Superhero Character
class Superhero(Character):
    def action_button(self):
        print("🦸‍♂️ Swoosh! Flying high into the sky!")

# Ninja Character
class Ninja(Character):
    def action_button(self):
        print("🥷 Poof! Throwing a smoke bomb and vanishing!")

# Wizard Character
class Wizard(Character):
    def action_button(self):
        print("🧙‍♂️ Kaboom! Casting a massive fireball!")


# --- PLAYING THE GAME ---

# Pick your hero team!
team = [Superhero(), Ninja(), Wizard()]

# Press the Action Button for every character on the team!
for hero in team:
    hero.action_button()