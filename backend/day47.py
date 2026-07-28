# Day 47 Magic/dunder methods (__str__, __len__, etc.)


# 1... __init__(self, ...): The constructor method used to initialize attributes.

# 2... __str__(self): Controls what gets displayed when you pass your object to print() or str(). It returns a user-friendly string!

# 3... __len__(self): Controls what gets returned when you pass your object to the built-in len() function.

# 4 ... __eq__(self, other): Controls how objects are compared using the equality operator (==).

# and must remember we use (return) in it please

print("--- 1. MAGIC / DUNDER METHODS ---")

class Book:
    def __init__(self, title, auther, pages):
        self.title = title
        self.auther = auther
        self.pages = pages

    # 1. Custom string representation for print()
    def __str__(self):
        return (f"{self.title} by {self.auther}")    # look here we use return 

    # 2. Custom length for len()
    def __len__(self):
        return self.pages

    # 3. Custom equality for == operator
    def __eq__(self, other):
        return self.title == other.title and self.auther == other.auther

# Creating Book instances
book1 = Book("khan", "shoaib", 500)
book2 = Book("shan", "jan", 550)
book3 = Book("Ali", "Noor", 540)

# Testing __str__
print(book1)
print(book2)   # Automatically triggers book1.__str__()


# Testing __len__
print(f"pages Counted : {len(book1)}")
print(f"pages counted : {len(book2)}")

# Testing __eq__
print(f"is book1 equal to book2? {book1 == book2}")
print(f" is book2 equal to book3? {book2 == book3}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def __str__(self):
        return f"Playlist : {self.name} ({len(self.songs)} songs)"

    def __len__(self):
        return len(self.songs)   # remember this, its because we have a list for it that is why

my_playlist = Playlist("coding vibes", ["song 1", "song 2", "song 3"])

print(my_playlist)

print(len(my_playlist))