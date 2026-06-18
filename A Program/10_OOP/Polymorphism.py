# Method overriding

class Animal:
    def show(self):
        print("Vanilla likes Chocolate.")

class Human(Animal):
    def show(self):
        print("Chocolate likes Vanilla.")

obj = Human()
obj.show()

#duck typing

class Animal:
    def show(self):
        print("Vanilla likes Chocolate.")

class Human:
    def show(self):
        print("Chocolate likes Vanilla.")

obj = Human()
obj2 = Animal()

obj.show()
obj2.show()