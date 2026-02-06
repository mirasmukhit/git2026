nums = [2, -1, 4, -3, 6]
i = 0
while i < len(nums):
    if nums[i] < 0:
        i += 1
        continue #skips negative numbers
    print(nums[i])
    i += 1





i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i) #1 2 4 5





