f = open("demofile.txt")
print(f.read())



f = open("Practice6/input.txt")
print(f.read())



with open("demofile.txt") as f:
    print(f.read())



f = open("demofile.txt")
print(f.readline())
f.close()



with open("demofile.txt") as f:
    print(f.read(5))#return only first 5 characters of the file


with open("demofile.txt") as f:
    print(f.readline())
    print(f.readline())


with open("demofile.txt") as f:
    for x in f:
        print(x)#output all lines o the file






