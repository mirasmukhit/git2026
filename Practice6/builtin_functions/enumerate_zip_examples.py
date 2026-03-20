# ENUMERATE examples

fruits = ["apple", "banana", "orange"]

# 1) basic enumerate
for i, fruit in enumerate(fruits):
    print(i, fruit)   # 0 apple / 1 banana / 2 orange

# 2) enumerate with start=1
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)   # 1 apple / 2 banana / 3 orange

# 3) make enumerate into list
result1 = list(enumerate(fruits))
print(result1)   # [(0, 'apple'), (1, 'banana'), (2, 'orange')]


# ZIP examples

names = ["Ali", "Miras", "Dana"]
scores = [90, 85, 100]

# 4) zip two lists
result2 = list(zip(names, scores))
print(result2)   # [('Ali', 90), ('Miras', 85), ('Dana', 100)]

# 5) use zip in loop
for name, score in zip(names, scores):
    print(name, score)   # Ali 90 / Miras 85 / Dana 100

# 6) zip three lists
ages = [16, 17, 18]
result3 = list(zip(names, scores, ages))
print(result3)   # [('Ali', 90, 16), ('Miras', 85, 17), ('Dana', 100, 18)]