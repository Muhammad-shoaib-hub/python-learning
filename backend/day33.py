# Day 33 Working with JSON files

# json.dump(data, file): Takes Python data (like a dictionary) and writes (dumps) it directly into a .json file.
# json.load(file): Reads data from a .json file and loads it directly back into a Python dictionary or list.


import json
print("---- 1. writing to a json file")

# Step 1: Create a Python dictionary with user/student data

user_profile = {
    "name" : "shoaib",
    "role" : "backend developer",
    "day" : 33,
    "skills" : ["python", "HTMl", "file i/o"],
    "is_active" : True
}

# Step 2: Write dictionary to JSON file using json.dump()
# indent=4 formats the JSON file with clean indentations!

with open("user.json", "w",) as file:
    json.dump(user_profile, file, indent=4)
    #indent=4 argument makes the file nicely formatted instead of a single long line.

print("user.json ! created successfully ")

print("\n")
print("\n")

print("--- 2. reading from json file---")
with open("user.json", "r") as file:
    read = json.load(file)
print(f"name : {read['name']}")
print(f"role : {read['role']}")
print(f"Day : {read['day']}")
print(f"skills : {read['skills']}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")

import json
def save_settings(settings_dict): 
    with open("setting.json", "w") as file:
        json.dump(settings_dict, file, indent=4)
    
    print("settings saved successfully ")

def load_settings():
    try:
        with open("setting.json", "r") as file:
            just = json.load(file)
            return just
    except FileNotFoundError:
        print("settings file not founded ")
        return None

my_settings = {
    "theme" : "darek",
    "font_size" : 16,
    "notification" : True
}

save_settings(my_settings)
loaded_data = load_settings()
print(f"theme : {loaded_data['theme']}")