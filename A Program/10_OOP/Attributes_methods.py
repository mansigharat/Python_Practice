#types of attributes

class Atharva:
    #class Attribute
    year = 3

    #instance attribute
    def __init__(self, branch):
        self.branch = branch

    #instance method
    def show(self):
        print("How are you?")

    #class method
    @classmethod
    def Arnav(cls):
        print("This is me....!")


    #static method
    @staticmethod
    def Manu():
        print("Presence of a caring friend is enough to keep you moving.")


obj = Atharva(18)

obj.show()

obj.Arnav()

obj.Manu()
