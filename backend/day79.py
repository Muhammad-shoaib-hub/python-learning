# ==========================================
# DAY 79: WORKING WITH OS AND SYS MODULES
# ==========================================


import os

# 1. Check current directory
current_dir = os.getcwd()
print(f"Current Directory : {current_dir}")

# 2. Check if a folder exists, and create it if it doesn't

folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder : {folder_name}")
else:
    print(f"folder {folder_name} is already exists")

# 3. List all files and directories in current path
print(f"📋 Contents of folder: {os.listdir('.')}")      # must remember the dot (.)




print("\n")
print("\n")
print("-"* 70)
print("-"* 70)
print("-"* 70)
print("\n")
print("\n")



import sys

# 1. Print Python Version
print(f"current python version is = {sys.version}")


# Check if user passed an argument via sys.argv

if len(sys.argv) > 1:
    print(f"👋 User input argument: {sys.argv[1]}")
else:
    print("💡 No extra arguments passed via command line.")