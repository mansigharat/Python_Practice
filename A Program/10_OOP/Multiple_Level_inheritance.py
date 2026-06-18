# Multiple level inheritance
class Animals:
    def __init__(self, name=""):
        self.name = name

class Human:
    def __init__(self,age):
        self.age = age

class Robots(Human,Animals):
    def __init__(self, name, age, model):
        Human.__init__(self, age)
        Animals.__init__(self, name)
        self.model = model
        

obj = Human(20)
print(obj.age)

bot = Robots("Charlie123",19,"m9")
print(bot.name, bot.age, bot.model)