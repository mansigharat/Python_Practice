# constructor

class Factory:
    def __init__(self,country,salary,age):
        self.country = country
        self.salary = salary
        self.age = age

    def show(self):
        print(f"Atharva is {self.age} old, working in {self.country} with a monthly salary of {self.salary} ")
    
    def tell(self):
        print(f"Manu is {self.age} old, working in {self.country} with a monthly salary of {self.salary} ")
        

Atharva = Factory("Switzerland",250000,25)

Manas = Factory("Switzerland",280000,25)

print(Atharva.salary)

print(Manas.salary)

Atharva.show()

Manas.tell()