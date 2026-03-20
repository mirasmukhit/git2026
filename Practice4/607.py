a = int(input())
b = input().split()
c = []
for i in range(a):
    c.append(b[i])
print(max(c,key=len))
    
