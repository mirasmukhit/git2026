class Father:
    def skill1(self):
        print("Driving")

class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    pass

c = Child()
c.skill1()
c.skill2()












class A:
    def __init__(self):
        print("Class A")

class B:
    def __init__(self):
        print("Class B")

class C(A, B):
    def __init__(self):
        super().__init__()

c = C()














class A:
    def show(self):
        print("From A")

class B:
    def show(self):
        print("From B")

class C(A, B):#A wrote in a first position.
    pass

c = C()
c.show()





















