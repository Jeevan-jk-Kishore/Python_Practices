#Encapsulation
""" It is used to protect the variable """

#Example 1
class bank():
    def __init__(self):
        self.__balance=10000    #'__' defines the private 
    def display(self):
        print(self.__balance)

obj=bank()
obj.display()
try:
    print(obj.__balance)  #It displays error: because __balance variable is privated it can only access within the class

except:
    print("It comes under privacy")