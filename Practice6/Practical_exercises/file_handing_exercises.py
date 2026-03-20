f = open("sample.txt", "x")
f.close()

with open("sample.txt", "a") as f:
    f.write("Hi, how are you?\n")
    f.write("What is your name?\n")

with open("sample.txt", "r") as f:
    print(f.readlines())

with open("sample.txt", "a") as f:
    f.write("Hi, I am good.\n")
    f.write("My name is Miras.\n")

with open("sample.txt", "r") as f:
    print(f.readlines())


import shutil
shutil.copy("sample.txt","demofile.txt")


import os
if os.path.exists("sample.txt"):
    os.remove("sample.txt")
else:
    print("this file does not exists")