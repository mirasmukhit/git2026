class Person:
    species = "Human"   # class variable

p1 = Person()
p2 = Person()

print(p1.species) #Human
print(p2.species) #Human










class Student:
    count = 0   # class variable

    def __init__(self, name):
        self.name = name
        Student.count += 1

s1 = Student("Ali")
s2 = Student("Aruzhan")

print(Student.count) #2






class Car:
    wheels = 4

c1 = Car()
Car.wheels = 6

print(c1.wheels)








class Dog:
    type = "Animal"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

d1 = Dog("Rex")
d2 = Dog("Max")

print(d1.type)
print(d1.name)













class Phone:
    brand = "Samsung"

p1 = Phone()
p2 = Phone()

p1.brand = "iPhone"   # override for this object only

print(p1.brand)
print(p2.brand)




