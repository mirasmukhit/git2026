a = int(input())
b = int(input())
c = int(input())
arr = input().split()
for i in range(a):
    arr[i] = int(arr[i])
for i in range(len(arr)):
    if(i >= b and i <= c):
        arr[b:c+1]=arr[b:c+1][::-1]
print(**arr)
