a=int(input())
b = input().split()
c=set()
for i in range(a):
    b[i]=int(b[i])
    c.add(b[i])
result = sorted(c)
print(*result)