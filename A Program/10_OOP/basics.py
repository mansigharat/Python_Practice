# class in OOP

class Factory:
    a = 18 #attribute

    def hello():  #method
        print("Hello")
    
    # print("I am getting initialized, this is very exciting.")

# print(Factory().a)

# Factory().hello()

# Objects

# obj = Factory

# print(obj.a)

# obj.hello() 

# constructor

class Factory:
    def __init__(self,country,salary,age):
        self.country = country
        self.salary = salary
        self.age = age

Atharva = Factory("Switzerland",250000,25)

Manu = Factory("Switzerland",280000,25)

print(Atharva.salary)

print(Manu.salary)