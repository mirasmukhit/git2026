import os

# Example 1: show current working directory
print("Example 1:")
print("Current directory:", os.getcwd())
print()


# Example 2: list all files and folders in current directory
print("Example 2:")
print("Files and folders:", os.listdir())
print()


# Example 3: create one new folder
print("Example 3:")
if not os.path.exists("test_folder"):
    os.mkdir("test_folder")
    print("Folder 'test_folder' created")
else:
    print("Folder 'test_folder' already exists")
print()


# Example 4: create several folders
print("Example 4:")
folders = ["dir1", "dir2", "dir3"]
for folder in folders:
    if not os.path.exists(folder):
        os.mkdir(folder)
        print(folder, "created")
    else:
        print(folder, "already exists")
print()


# Example 5: list only directories
print("Example 5:")
for item in os.listdir():
    if os.path.isdir(item):
        print(item)