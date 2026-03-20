def func(x):
    return x%2==0
a = int(input())
b = input().split()
c = []
for i in range(a):
    b[i]=int(b[i])
    c.append(b[i])
result = list(filter(func,c))
print(len(result))