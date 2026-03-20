import os
import shutil

# Example 1: move one file
if os.path.exists("file1.txt"):
    shutil.move("file1.txt", "folder1/file1.txt")
    print("file1.txt moved to folder1")
else:
    print("file1.txt not found")


# Example 2: move and rename file
if os.path.exists("file2.txt"):
    shutil.move("file2.txt", "folder1/new_file2.txt")
    print("file2.txt moved and renamed")
else:
    print("file2.txt not found")


# Example 3: move file from one folder to another
if os.path.exists("folderA/test.txt"):
    shutil.move("folderA/test.txt", "folderB/test.txt")
    print("test.txt moved from folderA to folderB")
else:
    print("folderA/test.txt not found")


# Example 4: move all .txt files into one folder
if not os.path.exists("texts"):
    os.mkdir("texts")

for file in os.listdir():
    if file.endswith(".txt") and os.path.isfile(file):
        shutil.move(file, os.path.join("texts", file))
        print(file, "moved to texts")


# Example 5: move folder
if os.path.exists("old_folder"):
    shutil.move("old_folder", "new_place/old_folder")
    print("old_folder moved")
else:
    print("old_folder not found")