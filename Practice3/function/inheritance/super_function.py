# super() is used to call a method from the parent class inside a child class.

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call parent constructor
        self.breed = breed

d = Dog("Rex", "Bulldog")

print(d.name)
print(d.breed)











class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()
        print("I am a student.")

s = Student()
s.greet()
#Output:Hello
#I am a student.








class Vehicle:
    def __init__(self, brand):
        self.brand = brand

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

c = Car("Toyota", "Camry")

print(c.brand, c.model)


