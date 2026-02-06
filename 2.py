a = int(input())
sum = 0
for i in range(2,a/2):
    if(a % i == 0):
        sum += 1
        break
if(sum<=2):
    print("No")
else:
    print("Yes")