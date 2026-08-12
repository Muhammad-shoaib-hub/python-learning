"""
Day 80 Challenge: Text File Backup Automator
Copies all .txt files from the current folder into a new "backup_txt" folder.
Originals are NOT deleted (we use shutil.copy, not shutil.move).
"""

import os
import shutil

def backup_txt_files():
    current_folder = "."
    backup_folder = "backup_txt"

    # Step 1: Create the backup folder (do nothing if it already exists)
    os.makedirs(backup_folder, exist_ok=True)

    # Step 2: Scan the current folder for .txt files
    copied_count = 0

    for filename in os.listdir(current_folder):
        if filename.endswith(".txt"):
            source_path = os.path.join(current_folder, filename)
            destination_path = os.path.join(backup_folder, filename)

            # Step 3: Copy the file (original stays where it is)
            shutil.copy(source_path, destination_path)
            copied_count += 1
            print(f"Copied: {filename}")

    # Step 4: Print a summary
    print("\n--- Backup Summary ---")
    if copied_count == 0:
        print("No .txt files were found in this folder.")
    else:
        print(f"Total .txt files copied: {copied_count}")
        print(f"Backup location: {os.path.abspath(backup_folder)}")

if __name__ == "__main__":
    backup_txt_files()