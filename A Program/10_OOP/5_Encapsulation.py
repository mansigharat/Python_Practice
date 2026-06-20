#Encapsulation

class Animals:
    a = 18
    def hello(self):
        print("Nice work.")


class Humans(Animals):
    def hello2(self):
        print(super().hello())

obj = Humans()
obj.hello2()