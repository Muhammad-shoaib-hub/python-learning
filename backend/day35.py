# day35.py

# not by me 
# not by me 
# not by me 
# not by me 
# not by me 
# not by me 


# ---------------------------------------------------------
# Day 35: Interactive Notes-Saving App
# ---------------------------------------------------------

def add_note():
    note = input("✍️ Enter your note: ")
    
    # Save the note to a file in append mode
    with open("my_notes.txt", "a") as file:
        file.write(note + "\n")
        
    print("✅ Note saved successfully!\n")


def view_notes():
    try:
        print("\n--- 📄 YOUR SAVED NOTES ---")
        with open("my_notes.txt", "r") as file:
            notes = file.readlines()
            
            if not notes:
                print("Your notes file is currently empty.")
            else:
                for index, line in enumerate(notes, 1):
                    # .strip() removes the extra line break from the file
                    print(f"{index}. {line.strip()}")
        print("---------------------------\n")
        
    except FileNotFoundError:
        print("⚠️ No notes file found yet! Add a note first.\n")


def main_menu():
    while True:
        print("=== 📝 NOTES MANAGER ===")
        print("1. Add a new note")
        print("2. View all notes")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("👋 Goodbye Shoaib! See you tomorrow for Day 36!")
            break
        else:
            print("❌ Invalid option. Please enter 1, 2, or 3.\n")

# Run the app
main_menu()