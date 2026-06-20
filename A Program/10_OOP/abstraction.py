from abc import ABC, abstractmethod

class CollegeStaff(ABC):     
    def __init__(self, name):
        self.name = name

    @abstractmethod         
    def work(self):
        pass

class Principal(CollegeStaff):
    def work(self):  
        print(f"Principal {self.name} is the senior most Person in the College")

class HOD(CollegeStaff):
    def work(self):         
        print(f"HOD {self.name} takes Care of the Computer Department")    

class Professor(CollegeStaff):
    def work(self):
        print(f"Professor {self.name} reports to the HOD.")


p1 = Principal("Sandesh Gharat")
p1.work() 

m1 = HOD("Mansi Gharat")  
m1.work()    

j1 = Professor("Atharva Thorve")
j1.work()