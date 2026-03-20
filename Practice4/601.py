def func(x):
    return x**2
a = int(input())
b = input().split()
c = []
for i in range(a):
    b[i]=int(b[i])
    c.append(b[i])
result = map(func,c)
print(sum(result))