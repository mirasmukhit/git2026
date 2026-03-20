from functools import reduce

# 1. Use map() and filter() on lists
numbers = [1, 2, 3, 4, 5, 6]

squared = list(map(lambda x: x * x, numbers))
print("map example:", squared)   # [1, 4, 9, 16, 25, 36]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("filter example:", even_numbers)   # [2, 4, 6]


# 2. Aggregate with reduce()
total = reduce(lambda a, b: a + b, numbers)#reduce(function, iterable)
print("reduce example:", total)   # 21


# 3. Use enumerate() and zip() for paired iteration
fruits = ["apple", "banana", "orange"]

for index, fruit in enumerate(fruits, start=1):
    print("enumerate example:", index, fruit)
# 1 apple
# 2 banana
# 3 orange

names = ["Ali", "Miras", "Dana"]
scores = [90, 85, 100]

for name, score in zip(names, scores):
    print("zip example:", name, score)
# Ali 90
# Miras 85
# Dana 100


# 4. Demonstrate type checking and conversions
x = "123"
y = 45
z = 3.14

print("type of x:", type(x))   # <class 'str'>
print("type of y:", type(y))   # <class 'int'>
print("type of z:", type(z))   # <class 'float'>

x_int = int(x)
y_float = float(y)
z_str = str(z)

print("converted x:", x_int, type(x_int))   # 123 <class 'int'>
print("converted y:", y_float, type(y_float))   # 45.0 <class 'float'>
print("converted z:", z_str, type(z_str))   # 3.14 <class 'str'>