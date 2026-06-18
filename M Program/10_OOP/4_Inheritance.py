# In a hospital there are different types of staff:

# - Every staff member has a name and salary. Doctor, nurse, receptionist. Everyone.
# - A Doctor has one extra thing: specialization. Like heart, brain, bones.
# - A Nurse has one extra thing: ward they work in. Like ICU, emergency.

# That is it. That is inheritance.

# **Write this in your book:**

# HospitalStaff  = Parent  (name, salary)
# Doctor         = Child   (gets name+salary FREE, adds specialization)
# Nurse          = Child   (gets name+salary FREE, adds ward)

# Now before I write any code, you tell me:

# When a Doctor joins the hospital, what details does HR need to fill in for them?

# Just answer that. Plain English. No code.

# okay it say like write my name rahul and also write salary (90000) after filling that here is my spealization that is "Heart" fill it

class HospitalStaff:
    
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def show(self):
        print(f"Name: {self.name} | Salary : {self.salary}")

class Doctor(HospitalStaff):
    def __init__(self, name, salary, specialization):
        super().__init__(name, salary)   
        self.specialization = specialization

    def treat(self):
         print(f"Dr.{self.name} treats {self.specialization} patients")

class Nurse(HospitalStaff):
    def __init__(self, name, salary, ward):
        super().__init__(name,salary)
        self.ward = ward

    def assist(self):
        print(f"Name : {self.name} | Ward : {self.ward}")

d1 = Doctor("Rahul" , 900000 , "Heart")
d2 = Nurse("Priya" , 15000 , "ICU")

d1.show()
d2.assist()
d2.show()