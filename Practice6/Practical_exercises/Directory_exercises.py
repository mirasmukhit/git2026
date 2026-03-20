import os
os.makedirs("Parent/children")
print(os.listdir())



for file in os.listdir():
    if file.endswith(".txt"):
        print(file)

import shutil
shutil.move("file1.txt", "folder1/file1.txt")

shutil.copy("file1.txt", "folder1/file1.txt")






