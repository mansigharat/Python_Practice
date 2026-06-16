#Variables - defined inside the class are Attribute
#Methods - functions defined inside a class are Methods

class Animal:
    name = "Lion" #class attribute

    def __init__(self,age):
        self.age = age  #instance attribute

    def show(self):     #instance method
        print("How are you")

    @classmethod   #it target the class location , and self target the object location , this is class method
    def hello(cls):
        print("How are you class ?")

    @staticmethod
    def static():
        print("How are you static ?")

obj = Animal(12)

obj.show()

obj.hello()

obj.static()