a ,b ,c = map(int,input().split())
arr = input().split()
for i in range(a):
    arr[i] = int(arr[i])
m = c - b
if a==c:
    arr[b-1:c+1] = arr[b-1:c+1][::-1]
else:
    arr[b-1:c] = arr[b-1:c][::-1]
print(*arr)
