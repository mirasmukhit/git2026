a = int(input())
st = input().split()
for i in range(a):
    st[i] = int(st[i])
total = 0
for i in range(a):
    j = i + 1
    for j in range(a):
        if(st[i]==st[j]):
            total+=1
        j+=1
print(total)