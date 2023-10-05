#Polymorphism
class Subject:
    def difficult(x):
        print("Sujects are difficult to understand")

class Java(Subject):
    def difficult(x):
        print("Java is Hard")

class Python(Subject):
    def difficult(x):
        print("Python is Easy")


sub = [Subject(), Java(), Python()]
for obj in sub:
    obj.difficult()