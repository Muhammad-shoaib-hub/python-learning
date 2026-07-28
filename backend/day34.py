# day34.py
import csv
import json

print("--- 1. SAVING TO FILES ---")

def save_contact_txt(name, phone):
    with open("contacts.txt", "a") as file:
        file.write(f"Name: {name} | Phone: {phone}\n")
    print(f"✅ TXT saved: {name}")

def save_contact_csv(name, phone, email):
    with open("contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])
    print(f"✅ CSV saved: {name}")

def save_contacts_json(contacts_list):
    with open("contacts.json", "w") as file:
        json.dump(contacts_list, file, indent=4)
    print("✅ JSON saved all contacts")


# Step 1: Run the save functions first to create the files
save_contact_txt("Shoaib", "123-456-7890")
save_contact_csv("Shoaib", "123-456-7890", "shoaib@example.com")

all_contacts = [
    {"name": "Shoaib", "phone": "123-456-7890", "email": "shoaib@example.com"},
    {"name": "Ali", "phone": "987-654-3210", "email": "ali@example.com"}
]
save_contacts_json(all_contacts)


print("\n" + "="*50 + "\n")


print("--- 2. READING FROM FILES ---")

def read_txt():
    try:
        print("\n📄 TXT Contacts:")
        with open("contacts.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("sorry the file not founded yet")

def read_csv():
    try:
        print("\n📊 CSV Contacts:")
        with open("contacts.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("the csv file not founded yet")

def read_json():
    try:
        print("\n⚙️ JSON Contacts:")
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
            for contact in contacts:
                print(f"Name : {contact['name']}")
                print(f"Email : {contact['email']}")
    except FileNotFoundError:
        print("the json file not founded yet")


# Step 2: Now run your reading functions!
read_txt()
read_csv()
read_json()