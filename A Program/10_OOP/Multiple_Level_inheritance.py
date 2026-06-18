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


# multilevel inheritance
class haryanafactory:
    def __init__(self,wood,grip):
        self.wood = wood
        self.grip = grip

class delhifactory(haryanafactory):
    def __init__(self, wood, grip,sticker):
        super().__init__(wood, grip)
        self.sticker = sticker

class mumbaifactory(delhifactory):
    def __init__(self, wood, grip, sticker, costing):
        super().__init__(wood, grip, sticker)
        self.costing = costing


