# day52.py
# Day 52: Python Standard Library Tour

import datetime
import os
import random
import math

print("=== 🧰 PYTHON STANDARD LIBRARY TOUR ===\n")

# 1. DATETIME MODULE
print("--- 1. datetime Module ---")
now = datetime.datetime.now()
print(f"Current Date & Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")

# Calculating a future date (10 days from now)
# must remember
future_date = now + datetime.timedelta(days=10)
print(f"Date 10 Days From Now: {future_date.strftime('%Y-%m-%d')}\n")


# 2. OS MODULE
print("--- 2. os Module ---")
current_dir = os.getcwd()  # Get Current Working Directory
print(f"Current Directory: {current_dir}")

# List files in the current folder
files = os.listdir(".")
print(f"Total files/folders in current path: {len(files)}\n")


# 3. RANDOM MODULE
print("--- 3. random Module ---")
dice_roll = random.randint(1, 6)
print(f"🎲 Rolled a dice: {dice_roll}")

skills = ["Python", "HTML", "CSS", "SQL", "JavaScript"]
chosen_skill = random.choice(skills)
print(f"🎯 Random Skill Picked: {chosen_skill}")

random.shuffle(skills)
print(f"🔀 Shuffled Skills List: {skills}\n")


# 4. MATH MODULE
print("--- 4. math Module ---")
print(f"Square root of 144: {math.sqrt(144)}")
print(f"Ceiling of 4.2 (Round up): {math.ceil(4.2)}")
print(f"Floor of 4.8 (Round down): {math.floor(4.8)}")



print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



import random
import datetime
import os

usernames = ["Shoaib", "Ali", "Usman", "Sara", "Zain"]

winner = random.choice(usernames)
print(winner)

current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(f"🏆 Winner selected on [{current_time}]: {winner}!")


# must remember it 
print(os.path.exists("day52.py"))