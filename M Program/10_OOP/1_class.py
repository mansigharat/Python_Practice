#Variables - defined inside the class are Attribute
#Methods - functions defined inside a class are Methods

class Hospital_Form:

    def __init__(self,name,blood):
        self.name = name
        self.blood = blood
    
    def show(self):
        print(f"Patient name is {self.name} and blood group is {self.blood}")

form1 = Hospital_Form("Mansi","A+")
form2 = Hospital_Form("Parth","B+")

form1.show()
print(form1.name)
print(form2.blood)