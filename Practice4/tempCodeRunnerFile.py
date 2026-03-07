from math import pow
def squares(a,b):
    for i in range(a,b+1):
        yield pow(i,2)
a,b = int(input())
print(squares(a,b))