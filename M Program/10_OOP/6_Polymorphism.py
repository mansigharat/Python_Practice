# class HospitalStaff:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def work(self):
#         print("Staff is working")


# class Doctor(HospitalStaff):
#     def work(self):
#         print(f"Doctor {self.name} is treating patients")


# class Nurse(HospitalStaff):
#     def work(self):
#         print(f"Nurse {self.name} is assisting doctors")


# class Receptionist(HospitalStaff):
#     def work(self):
#         print(f"Receptionist {self.name} is managing appointments")


# d1 = Doctor("Rahul", 90000)
# n1 = Nurse("Priya", 50000)
# r1 = Receptionist("Amit", 30000)

# for staff in [d1, n1, r1]:
#     staff.work()

class Hotel:
    def __init__(self,name):
        self.name = name
    
    def work(self):
        print("Staff does grest job!!!")

class Owner(Hotel):
    def work(self):
        print(f"Owner {self.name} is happy because of staff work...")

class Servant(Hotel):
    def work(self):
        print(f"Servent {self.name} serve food to customer...")

class Cashier(Hotel):
    def work(self):
        print(f"Cashier {self.name} take cash from customer...")

o1 = Owner("Mansi Gharat")
s1 = Servant("Amit")
c1 = Cashier("Atharva")

for staff in [o1,s1,c1]:
    staff.work()