# ==========================================
# DAY 80: AUTOMATED FILE ORGANIZER SCRIPT
# ==========================================

import os
import shutil

# STEP 1: The robot checks where it is standing
target_dir = os.getcwd()

# STEP 2: The rulebook (Tag -> Box name)
CATEGORY_MAP = {
    ".txt": "TextFiles",
    ".csv": "DataFiles",
    ".json": "ConfigFiles"
}

# STEP 3: Scan everything on the floor
for filename in os.listdir(target_dir):
    file_path = os.path.join(target_dir, filename)

    # Only look at files (ignore folders that are already built)
    if os.path.isfile(file_path):
        
        # Read the tag (e.g., "notes", ".txt")
        name, ext = os.path.splitext(filename)
        ext = ext.lower()

        # STEP 4: If the tag is in our rulebook, build box and move file
        if ext in CATEGORY_MAP:
            # Name of the target box folder
            box_folder = os.path.join(target_dir, CATEGORY_MAP[ext])

            # Build the box if it doesn't exist yet
            os.makedirs(box_folder, exist_ok=True)

            # Move the file inside the box
            destination_path = os.path.join(box_folder, filename)
            shutil.move(file_path, destination_path)
            
            print(f"📦 Moved '{filename}' ➡️ {CATEGORY_MAP[ext]}/")

print("\n✨ Cleaning complete!")