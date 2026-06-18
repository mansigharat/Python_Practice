from abc import ABC, abstractmethod

class HospitalStaff(ABC):      # ABC makes it abstract
    def __init__(self, name):
        self.name = name

    @abstractmethod            # every child MUST implement this
    def work(self):
        pass

class Doctor(HospitalStaff):
    def work(self):            # implemented, works fine
        print(f"Dr.{self.name} is treating patients")

class Nurse(HospitalStaff):
    def work(self):            # implemented, works fine
        print(f"Nurse {self.name} is treating patients")                  # forgot work(), watch what happens


d1 = Doctor("Rahul")
d1.work()                      # works fine

n1 = Nurse("Priya")  
n1.work()          # CRASHES here