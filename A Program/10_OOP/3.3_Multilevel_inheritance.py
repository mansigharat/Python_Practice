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

