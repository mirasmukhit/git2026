#get __init__ --->  Set up this object when it is created
#self.name = name --->  saves the name inside the object.
#get.info --->  used to return information.


class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil") #is eqal to "Person.__init__(p1, "Emil")""
p1.greet() #Hello, my name is Emil











class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))#8
print(calc.multiply(4, 7))#28












class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def get_info(self):
    return f"{self.name} is {self.age} years old"

p1 = Person("Tobias", 28)
print(p1.get_info())