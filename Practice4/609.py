a = int(input())
b=input().split()
c=[]
for i in range(a):
    b[i]=int(b[i])
    c.append(b[i])
d=input().split()
e=[]
for i in range(a):
    e.append(d[i])
p =input()
found = False
for key,value in zip(c,e):
    if(value == p):
        print(key)
        found = True
        break
if not found:
    print("Not found")

