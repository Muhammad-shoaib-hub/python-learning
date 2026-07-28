# day31.py

# ---------------------------------------------------------
# 1. WRITING TO A FILE ("w" mode)
# --------------------------------------------------------

print("---- 1. writing to a file (w)")
with open("notes.text", "w") as file:
    file.write("hello shoaib \n")
    file.write("welcome to the day 31 of you python journey ")

print("notes.txt' has been created and written to.")


# ---------------------------------------------------------
# 2. APPENDING TO A FILE ("a" mode)
# ---------------------------------------------------------

print("---- 2. appending to the file (a)")
with open("notes.text", "a") as file:
    file.write("today we are learning how to handle the text file \n")

print("the new text (line) has been added through (a) appending ")

# ---------------------------------------------------------
# 3. READING FROM A FILE ("r" mode)
# this is must to learn in it (contant = file.read())
# ---------------------------------------------------------

print("---- 3. reading from a file (r)")
with open("notes.text", "r") as file:
    contant = file.read()
    print("file contant \n", contant)


print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


def add_entry(entry_text):
    with open("journal.text", "a") as file:
        file.write(entry_text + "\n")
    
    print("entery saved to journal.text ")

def view_journal():
    try:
        with open("journal.text", "r") as file:
            cont = file.read()
            print("check ", cont)
    
    except FileNotFoundError:
        print("no jurnal entries found yet")


add_entry("Day 31: Learned file I/O in Python!")
add_entry("Built a simple journal logger.")
view_journal()
        