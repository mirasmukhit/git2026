def func(x):
    return x>=0
a = int(input())
b = input().split()
c = []
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
if(all(func for x in c)):
    print("Yes")
else:
    print("No")