
# its remain 
# its remain 
# its remain 
# its remain 
# its remain 





# day28.py - Simple To-Do List App

# Global list to store our tasks
todo_list = []

def show_menu():
    print("\n--- 📋 TO-DO LIST MENU ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

def view_tasks():
    if len(todo_list) == 0:
        print("\nYour to-do list is empty! 🎉")
    else:
        print("\n--- Your Tasks ---")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

def add_task():
    task_name = input("\nEnter the task you want to add: ")
    if task_name.strip() != "":
        todo_list.append(task_name)
        print(f"✅ Task '{task_name}' added successfully!")
    else:
        print("⚠️ Task cannot be empty!")

def delete_task():
    view_tasks()
    if len(todo_list) > 0:
        try:
            task_num = int(input("\nEnter the number of the task to delete: "))
            if 1 <= task_num <= len(todo_list):
                removed = todo_list.pop(task_num - 1)
                print(f"🗑️ Task '{removed}' has been deleted!")
            else:
                print("⚠️ Invalid task number!")
        except ValueError:
            print("⚠️ Please enter a valid number!")

# Main Application Loop
while True:
    show_menu()
    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("\nThanks for using the To-Do List App! Goodbye! 👋")
        break
    else:
        print("⚠️ Invalid choice! Please enter a number from 1 to 4.")