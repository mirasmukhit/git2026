arr = list(map(int,input().split()))
def func(n):
    yield arr*n
n = int(input())
for l in func(n):
    print(l)
