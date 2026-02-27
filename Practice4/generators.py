# What is the iterator?
# An iterator is an object that gives items one-by-one using:

# iter(obj) --> makes an iterator
# next(it) --> gets next item 


nums = [10,20,30]
it = iter(nums)
print(next(it))
print(next(it))
print(next(it))
# print(next(it))    If we print more numbers than in the array python gives us "StopIteration"



a = [0,1,2,3,4,5] #if we have a lot of elements in the array,then we can use While True method.Insead of printing every element of array by "print(next(it))"
it = iter(a)
while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        break



class func:
    def __init__ (self,n):
        self.n = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        value = self.n
        self.n-=1
        return value
for x in func(5):#5 4 3 2 1 and it is not gives us 0,because of  
    print(x)
        


def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3





def func(n):
    for i in range(1,n+1):
        yield i*i
n = int(input())
for i in func(n):#all sqare of numbers  until n(including)
    print(i)





g = (x * 2 for x in [1,2,3])
print(next(g))  # 2
print(list(g))  # [4, 6]

    