# Method overriding

class Animal:
    def show(self):
        print("Vanilla likes Chocolate.")

class Human(Animal):
    def show(self):
        print("Chocolate likes Vanilla.")

obj = Human()
obj.show()