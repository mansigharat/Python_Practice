class HospitalForm:

    def __init__(self, name, blood):
        self.name = name
        self.blood = blood

    @classmethod
    def from_string(cls, data):
        name, blood = data.split(",")
        return cls(name, blood)

form1 = HospitalForm("Mansi", "A+")          # normal way
form2 = HospitalForm.from_string("Parth,B+") # admin way

print(form2.name)   # Parth
print(form2.blood)  # B+