from abc import ABC, abstractmethod

class HospitalStaff(ABC):
    
    def __init__(self,name,__salary):
        self.name = name
        self.__salary = __salary

    @abstractmethod
    def work(self):
        print("Staff does grest job!!!")

class Doctor(HospitalStaff):

    def __init__(self, name, __salary, specialization):
        super().__init__(name, __salary)   
        self.specialization = specialization

    @classmethod
    def treat(cls):
         print(f"Dr.{cls.name} treats {cls.specialization} patients")

    def work(self):
        print(f"Dr. {self.name} do great work")

class Nurse(HospitalStaff):
    def __init__(self, name, __salary, ward):
        super().__init__(name,__salary)
        self.ward = ward

    @staticmethod
    def assist(self):
        print(f"Name : {self.name} | Ward : {self.ward} with salary {self.__salary}")

    def work(self):
        print(f" Nurse {self.name} taking care of patient")


d1 = Doctor("Rahul" , 900000 , "Heart")
d2 = Nurse("Priya" , 15000 , "ICU")

d1.treat()
d2.assist()
d2.assist()
d1.work()