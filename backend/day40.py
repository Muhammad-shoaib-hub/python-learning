#Day 40 Practice: build 2-3 small classes
#Day 40 Practice: build 2-3 small classes
#Day 40 Practice: build 2-3 small classes
#Day 40 Practice: build 2-3 small classes




class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.battry = 100

    def use_phone(self, app_name, battry_cost):
        if self.battry >= battry_cost:
            self.battry -= battry_cost
            print(f"Used {app_name} battry is now {self.battry}%")
        else:
            print(f"battry is too low for this app {app_name} please charge you phone")

    def charge(self, amount):
        self.battry += amount
        if self.battry > 100:
            self.battry = 100
        # Move print outside so it always displays the updated battery!
        print(f"phone is charged now ! battery is now {self.battry}")

phone1 = Smartphone("samsung", "skeil")
phone1.use_phone("Youtube", 40)
phone1.use_phone("AI", 80)
phone1.charge(50)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


# day40.py

print("--- 1. BOOK CLASS PRACTICE ---")

class Book:
    # Class variable
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False  # Default state: available
        Book.total_books += 1

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"✅ You borrowed '{self.title}' by {self.author}.")
        else:
            print(f"❌ Sorry, '{self.title}' is already borrowed!")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"🔁 You returned '{self.title}'.")
        else:
            print(f"❓ '{self.title}' was not borrowed.")

# Testing the Book class
book1 = Book("Python Crash Course", "Eric Matthes")
book2 = Book("Clean Code", "Robert C. Martin")

print(f"Total books in library: {Book.total_books}")

book1.borrow()
book1.borrow()       # Try borrowing again to test logic
book1.return_book()
