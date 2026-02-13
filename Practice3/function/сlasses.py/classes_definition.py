class MyClass:
    x = 5
print(MyClass)#<class '__main__.MyClass'>





class MyClass:
    x = 5
p1 = MyClass()
print(p1.x) #5




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

del p1 #delete p1 and it doesn't exist anymore

print(p1)
