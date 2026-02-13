class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):   # overriding
        print("Dog barks")

d = Dog()
d.sound()











class Person:
    def greet(self):
        print("Hello!")

class Student(Person):
    def greet(self):
        super().greet()
        print("I am a student")

s = Student()
s.greet()


















class Employee:
    def get_salary(self):
        return 5000

class Manager(Employee):
    def get_salary(self):   # overriding
        return 8000

e = Employee()
m = Manager()

print(e.get_salary())#5000
print(m.get_salary())#8000
