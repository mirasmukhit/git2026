#result = value_if_true if condition else value_if_false



#Normal if:
a=5
b=2
if a > b:
    print("A is bigger")
else:
    print("B is bigger")



#Short-hand:
print("A is bigger" if a > b else "B is bigger")




x = 10
y = 20
max_num = x if x > y else y
print(max_num)




n = int(input())
print("Even" if n % 2 == 0 else "Odd")
