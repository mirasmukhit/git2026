a = int(input())
arr = input().split()
d = {}
for i in range(a):
    arr[i] = int(arr[i])
for x in arr:
    d[x] += 1
for i in range(a):
    if(d[i]==3):
        print(arr[i])
    else:
        continue


