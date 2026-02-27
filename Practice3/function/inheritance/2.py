x = 100
def outer():
    global x
    x = x / 2
outer()
print(x)
