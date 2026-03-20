import os
print(os.getcwd())#get current working directory
#It prints "C:\Users\hp\.vscode\git2026"




print(os.listdir())#This shows all files and folders in the current directory.
#It prints "['.git', 'gala.py', 'output_1.txt', 'Practice1', 'Practice2', 'Practice3', 'Practice4', 'Practice5', 'Practice6', 'README.md', 'sample_dataset.csv', 'tempCodeRunnerFile.py', 'tempCodeRunnerFile.python']"










print(os.path.exists("Practice6/input.txt"))#True because i have a file which is named "input.txt"


os.chdir("Practice6/input.txt")

