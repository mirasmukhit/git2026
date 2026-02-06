a = int(input())
arr = input().split()
for i in range(a):
    arr[i] = int(arr[i])
maxfr = float("-inf")
count = 0
frnum = 0
for i in range(a):
    for j in range(a):
        if(arr[i]==arr[j]):
            count += 1
        if(maxfr < count):
            maxfr = count
            frnum = arr[i]
        if(maxfr == count):
            if frnum > arr[i]:
                frnum = arr[i]
            else:
                continue
    count = 0
print(frnum)
        