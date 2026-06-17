# constructor

class Factory:
    def __init__(self,country,salary,age):
        self.country = country
        self.salary = salary
        self.age = age

Atharva = Factory("Switzerland",250000,25)

Manas = Factory("Switzerland",280000,25)

print(Atharva.salary)

print(Manas.salary)