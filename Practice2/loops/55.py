a = int(input())
s = []
for i in range(a):
    x = int(input())
    s.append(x)
total = 0
d = dict()
for i in s:
    if i not in d:
        d[i]= 0
    d[i]+=1
for i in s:
    if d[i]==3:
        total += 1
print(total)