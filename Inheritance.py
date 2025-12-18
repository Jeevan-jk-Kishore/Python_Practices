#Inheritance types
#1.Single Inheritance
class A():
    def alpha(self):
        print("Alpha")

class B(A):
    def beta(self):
        print("Beta")        

access=B()
access.beta()
access.alpha()


#2.Multiple Inheritance
class A():
    def alpha(self):
        print("Alpha")

class B():
    def beta(self):
        print("Beta")

class C(B,A):
    def gamma(self):
        print("Gamma")

acc=C()
acc.alpha()
acc.beta()
acc.gamma()


#3.Multi-Level Inheritance
class A():
    def alpha(self):
        print("Alpha")

class B(A):
    def beta(self):
        print("Beta")

class C(B):
    def gamma(self):
        print("Gamma")
acc=C()
acc.alpha()
acc.beta()
acc.gamma()


#4.Hyrachical Inheritance
class parent():
    def responsible(self):
        print("I'm the parent of my child")
class child1(parent):
    pass
class child2(parent):
    pass
class child3(parent):
    pass

child=child3()
child.responsible()


#5.Hybrid Inheritance
"""
The Combination of all these four Inheritance is called as Hybrid Inheritance
"""

