n = int(input())
arr  = input().split()
for i in range(n):
    arr[i] = int(arr[i])
d = dict()
for i in arr:
    if i not in d:
        d[i]=0
    d[i]=d[i]+1
for key in d:
    print(key , d[key])