a = int(input())
b = input().split()
c = []
for i in range(a):
    c.append(b[i])
for i,word in enumerate(c):
    print(f"{i}:{word}",end=" ")
