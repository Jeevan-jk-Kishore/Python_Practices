#Super Keyword
''' 
Super Keyword is used for call the parent class constructor fro the child class
'''
class A():
    def __init__(self):
        print("A Class")
    def display(self):
        print("Hello")

class B(A):
    def __init__(self):
        super().__init__()
        print("B Class")
    def display(self):
        print("World")

obj1=B()


#Example-2
class A():
    def __init__(self):
        print("A Class")
    def display(self):
        print("Hello")

class B():
    def __init__(self):
        print("B Class")
    def display(self):
        print("World")

class C(A,B):                #Here the left side of the class take as the super class
    def __init__(self):
        super().__init__()
        print("C Class")
    def display(self):
        print("World")

obj1=C()


#Example-3
class A():
    def __init__(self):
        print("A Class")
    def display(self):
        print("Hello")

class B():
    def __init__(self):
        super().__init__()
        print("B Class")
    def display(self):
        print("World")

class C(B,A):
    def __init__(self):
        super().__init__()
        print("C Class")
    def display(self):
        print("World")

obj1=C()