# MAP examples

numbers = [1, 2, 3, 4, 5]

# 1) multiply each number by 2
result1 = list(map(lambda x: x * 2, numbers))
print("map example 1:", result1)   # [2, 4, 6, 8, 10]

# 2) convert strings to integers
nums_str = ["10", "20", "30"]
result2 = list(map(int, nums_str))
print("map example 2:", result2)   # [10, 20, 30]

# 3) get lengths of words
words = ["apple", "banana", "kiwi"]
result3 = list(map(len, words))
print("map example 3:", result3)   # [5, 6, 4]


# FILTER examples

# 4) keep only even numbers
result4 = list(filter(lambda x: x % 2 == 0, numbers))
print("filter example 1:", result4)   # [2, 4]

# 5) keep only words with length more than 4
result5 = list(filter(lambda word: len(word) > 4, words))
print("filter example 2:", result5)   # ['apple', 'banana']

# 6) keep only positive numbers
nums2 = [-3, -1, 0, 2, 5]
result6 = list(filter(lambda x: x > 0, nums2))
print("filter example 3:", result6)   # [2, 5]