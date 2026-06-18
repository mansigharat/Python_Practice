# Multiple level inheritance
class Animals:
    def __init__(self, name=""):
        self.name = name

class Human(Animals):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

class Robots(Human):
    def __init__(self, name, age,model):
        super().__init__(name, age)
        self.model = model
        

obj = Human("Atharva",20)
print(obj.name, obj.age)

bot = Robots("Charlie123",19,"m9")
print(bot.name, bot.age, bot.model)

