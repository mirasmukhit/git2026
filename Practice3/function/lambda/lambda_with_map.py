numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)#[1,4,9,16,25]    sqare all elements





words = ["apple", "banana", "cherry"]
upper_words = list(map(lambda w: w.upper(), words))
print(upper_words)#['APPLE', 'BANANA', 'CHERRY']




nums = [5, 10, 15]
result = list(map(lambda x: x + 10, nums))
print(result) #[15, 20, 25] add 10 to each elements


