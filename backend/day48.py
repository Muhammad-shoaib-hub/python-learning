# day48.py

# not did by myself
# in 2nd try


print("=== 📚 LIBRARY MANAGEMENT SYSTEM (OOP MINI PROJECT) ===\n")

# 1. BASE CLASS (Inheritance & Encapsulation)
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False  # Private attribute (Encapsulation)

    # Getter for private attribute
    def is_borrowed(self):
        return self.__is_borrowed

    # Controlled methods to modify private state
    def borrow_item(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"✅ Successfully borrowed: '{self.title}'")
        else:
            print(f"❌ Sorry, '{self.title}' is already borrowed!")

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"🔄 Successfully returned: '{self.title}'")
        else:
            print(f"⚠️ '{self.title}' was not borrowed.")

    # Base method for Polymorphism
    def get_details(self):
        return f"'{self.title}' by {self.author}"


# 2. CHILD CLASS 1 (Inheritance + super() + Polymorphism)
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)  # Chaining parent constructor
        self.pages = pages

    # Overriding method (Polymorphism)
    def get_details(self):
        return f"📖 Book: '{self.title}' by {self.author} ({self.pages} pages)"


# 3. CHILD CLASS 2 (Inheritance + super() + Polymorphism)
class AudioBook(LibraryItem):
    def __init__(self, title, author, duration_hours):
        super().__init__(title, author)
        self.duration_hours = duration_hours

    # Overriding method (Polymorphism)
    def get_details(self):
        return f"🎧 AudioBook: '{self.title}' by {self.author} ({self.duration_hours} hrs)"


# 4. CONTAINER CLASS (Dunder Methods)
class Library:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"➕ Added to library: {item.title}")

    # Dunder Method 1: __len__
    def __len__(self):
        return len(self.items)

    # Dunder Method 2: __str__
    def __str__(self):
        return f"🏛️ {self.name} (Total Items: {len(self.items)})"

    # Displaying items using Polymorphism
    def show_all_items(self):
        print(f"\n--- Catalog for {self.name} ---")
        for item in self.items:
            status = "Borrowed" if item.is_borrowed() else "Available"
            # Calls each item's specific get_details() method!
            print(f"- {item.get_details()} | Status: {status}")


# --- 🧪 TESTING OUR FULL OOP PROJECT ---

# Create Library
my_library = Library("Central City Library")

# Create Items
b1 = Book("Python Crash Course", "Eric Matthes", 544)
b2 = Book("Clean Code", "Robert C. Martin", 464)
a1 = AudioBook("Atomic Habits", "James Clear", 5.5)

# Add items to Library
print("--- Adding Items ---")
my_library.add_item(b1)
my_library.add_item(b2)
my_library.add_item(a1)

# Testing Dunder Methods
print(f"\n{my_library}")  # Triggers __str__
print(f"Total count: {len(my_library)} items")  # Triggers __len__

# Display Initial Catalog (Polymorphism in loop)
my_library.show_all_items()

# Test Borrowing & Returning (Encapsulation)
print("\n--- Borrowing & Returning Items ---")
b1.borrow_item()
b1.borrow_item()  # Should fail (already borrowed)

a1.borrow_item()

# Display Catalog after borrowing
my_library.show_all_items()

b1.return_item()

# Final Catalog check
my_library.show_all_items()