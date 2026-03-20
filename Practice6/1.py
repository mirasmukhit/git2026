f = open("Practice6/input.txt","r")
print(f.read())
f.seek(0) #go bach to the begining
line1 = f.readline()
print(line1)
f.seek(0)
print(*f.readlines())
f.close()





with open("Practice6/input.txt","r") as f:
    for line in f:
        print(line.strip())


#with open("Practice6/input.txt","w") as f: #w deletes old text
    #f.write("Hello\n")
    #f.write("Who are you?\n")


with open("Practice6/input.txt","a") as f:
    f.write("Hello\n")
    f.write("Who are you?\n")

#"w" → write, old text is deleted
#"a" → append, adds to the end

with open("output_1.txt", "x")as f:
    f.write("Hello\n")
    f.write("World\n")

