import os
import shutil

print("---System Scan ---")
print("Running on: Linux Mint XFCE")
print("Memory: 4GB RAM Optimized")
print("Task: Organization Script Active")


# 1. Setup the locations
desktop = os.path.expanduser("~/Desktop")
destination = os.path.expanduser("~/Documents/Organized")


# 2. Create the folder if it isn't already there
if not os.path.exists(destination):
    os.makedirs(destination)


# 3. The logic to move the files
for filename in os.listdir(desktop):
     old_path = os.path.join(desktop, filename)

     # Only move files (skip other folders)
     if os.path.isfile(old_path) and filename != "cleaner.py":
        new_path = os.path.join(destination, filename)
        shutil.move(old_path, new_path)
        print(f"Moved:  {filename}")

print("--- Cleanup Complete ---")


