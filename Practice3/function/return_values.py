def add(a, b):
    return a + b
result = add(3, 5)
print(result)




def greet(name):
    return "Hello " + name
message = greet("Miras")
print(message) #Hello Miras




def calculations(a, b):
    return a + b, a - b
sum_result, sub_result = calculations(10, 5)
print(sum_result)#15
print(sub_result)#5




def is_even(number):
    return number % 2 == 0
print(is_even(4)) #True
print(is_even(7)) #False





