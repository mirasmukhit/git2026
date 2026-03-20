with open ("demofile.txt","a") as f:#a is not delete previous texts on the file,it just add lines to the file without deleting old lines
    f.write("Now the file has more content!")



with open("demofile.txt") as f:
    print(f.read())




with open("demofile.txt", "w") as f:
    f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open("demofile.txt") as f:
    print(f.read())




f = open("myfile.txt", "x")#create a new file called "myfile.txt"

