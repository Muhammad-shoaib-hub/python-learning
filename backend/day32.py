# day 32 ( Day 32 Working with CSV files )

import csv
print("--- 1. WRITING TO A CSV FILE ---")

# Data to write (header row + data rows)
headers = ["name", "as role", "hours completed"]
students = [
    ["shoaib","python learner", 32],
    ["khan", "HTMl learner", 33],
    ["shan", "C++ learner", 44]
]

# newline="" prevents extra blank lines on Windows
with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(headers)

    # Write multiple rows at once
    writer.writerows(students)

print("studets.csv file created and written successfully")

print("\n--- 2. READING FROM A CSV FILE ---")
with open("student.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV file contant : ")
    for row in reader:
        print(row)




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")


import csv
def add_expense(item, category, cost):
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([item, category, cost])
    print(f"saved expense : {item} - ${cost}")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            print("this is expense :")
            for row in reader:
                print(row)
    
    except FileNotFoundError:
        print("no expense record found yet")


add_expense("Coffee", "Food", 3.50)
add_expense("Notebook", "Supplies", 5.00)
view_expenses()