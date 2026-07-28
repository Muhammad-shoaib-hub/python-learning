# day49.py
# Day 49 Review + Build: Library Management System (OOP)

print("=== 📚 LIBRARY MANAGEMENT SYSTEM (DAY 49 BUILD) ===\n")

# 1. Base Class (Inheritance + Encapsulation + Polymorphism)
class LibraryItem:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.__is_borrowed = False  # Private attribute

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow_item(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            print(f"✅ Successfully borrowed: '{self.title}'")
        else:
            print(f"❌ '{self.title}' is already borrowed!")

    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            print(f"🔄 Successfully returned: '{self.title}'")
        else:
            print(f"⚠️ '{self.title}' was not borrowed.")

    def get_details(self):
        return f"'{self.title}' by {self.author}"


# 2. Child Class 1: Book
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author)
        self.pages = pages

    def get_details(self):
        return f"📖 Book: '{self.title}' by {self.author} ({self.pages} pages)"


# 3. Child Class 2: AudioBook
class AudioBook(LibraryItem):
    def __init__(self, title, author, duration_hours):
        super().__init__(title, author)
        self.duration_hours = duration_hours

    def get_details(self):
        return f"🎧 AudioBook: '{self.title}' by {self.author} ({self.duration_hours} hrs)"


# 4. Container Class with Dunder Methods
class Library:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"➕ Added to library: {item.title}")

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"🏛️ {self.name} | Total Catalog Items: {len(self.items)}"

    def show_catalog(self):
        print(f"\n--- Catalog for {self.name} ---")
        if not self.items:
            print("No items in the library.")
            return

        for index, item in enumerate(self.items, 1):
            status = "❌ Borrowed" if item.is_borrowed() else "✅ Available"
            print(f"{index}. {item.get_details()} -> {status}")


# --- 🧪 TESTING OUR OOP SYSTEM ---

# Create Library instance
my_lib = Library("Shoaib's Tech Library")

# Create Items
book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Clean Code", "Robert C. Martin", 464)
audio1 = AudioBook("Atomic Habits", "James Clear", 5.5)

# Add Items
print("--- 1. Adding Items to Library ---")
my_lib.add_item(book1)
my_lib.add_item(book2)
my_lib.add_item(audio1)

# Test Dunder Methods
print("\n--- 2. Testing Dunder Methods ---")
print(my_lib)             # Calls __str__
print(f"Total count: {len(my_lib)} items") # Calls __len__

# Show initial catalog
my_lib.show_catalog()

# Borrowing & Returning operations
print("\n--- 3. Testing Borrow & Return (Encapsulation) ---")
book1.borrow_item()
book1.borrow_item()  # Attempting to borrow again (should fail)
audio1.borrow_item()

# Show catalog after borrowing
my_lib.show_catalog()

# Return item
print("\n--- 4. Returning Item ---")
book1.return_item()

# Final Catalog state
my_lib.show_catalog()