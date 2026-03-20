a = int(input())
b = input().split()
c = []
for i in range(a):
    b[i] = int(b[i])
    c.append(b[i])
d = input().split()
e = []
for i in range(a):
    d[i]= int(d[i])
    e.append(d[i])
result = []
for x,y in zip(c,e):
    t = x*y
    result.append(t)
print(sum(result))