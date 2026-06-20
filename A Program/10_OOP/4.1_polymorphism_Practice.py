class MACorporation:
    def __init__(self,name):
        self.name = name
    
    def work(self):
        print("Staff does grest job!!!")

class Director(MACorporation):
    def work(self):
        print(f"Director {self.name} is happy because of staff work...")

class CEO(MACorporation):
    def work(self):
        print(f"{self.name} is very skillfull CEO and is supported by the Director...")

class GManager(MACorporation):
    def work(self):
        print(f"Manager {self.name} works hard for company growth...")

director = Director("Mansi Gharat")
ceo = CEO("Atharva")
manager = GManager("Arnav")

for staff in [director,ceo,manager]:
    staff.work()