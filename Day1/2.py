#Hierarchical and Multi-level Inheritance
class Sainadh:
    def m1(temp):
        print("Hello")
    def m2(temp):
        print("World")
class Sainadh1(Sainadh):
    def m3(temp):
        print("Python")
class Sainadh2(Sainadh):
    def m4(temp):
        print("Program")
class Sainadh3(Sainadh1,Sainadh2):
    def m5(temp):
        print("I Love Uh")
obj1=Sainadh1()
obj2=Sainadh2()
obj3=Sainadh3()
obj1.m1()
obj2.m1()
obj3.m1()