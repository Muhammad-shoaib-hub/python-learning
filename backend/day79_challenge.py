import os
import sys

# 1. Check if folder name argument was provided
if len(sys.argv) < 2:
    sys.exit("❌ Error: Please provide a folder name!")

# 2. Extract folder name and get current working directory

folder_name = sys.argv[1]
current_dis = os.getcwd()

# 3. Check folder existence and create if necessary

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"folder : {folder_name} created successfully in {current_dis}!")
else:
    print(f"foder : {folder_name} already exists in {current_dis}")