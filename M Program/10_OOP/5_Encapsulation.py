class Patient:
    def __init__(self, name, blood_type,age):
        self.name = name
        self.__blood_type = blood_type
        self.__age = age

    def get_blood(self):
        return self.__blood_type

    def set_blood(self, blood):
        valid = ["A+", "A-", "B+", "B-", "O+", "O-"]
        if blood in valid:              # check if blood is in list
            self.__blood_type = blood   # update the private attribute
        else:
            print("Invalid Blood group")

    def get_age(self):
        return self.__age
    
    def set_age(self, valid_age):
        if 0 <= valid_age <= 120:
            self.__age = valid_age
        else:
            print("Invalid Age")


n1 = Patient("Sayali", "A+",23)
n2 = Patient("Parth", "B+",20)
print(n1.get_blood())    # A+
print(n1.get_blood())    # A+

n1.set_blood("B+")
n2.set_age(10)

print(n1.get_blood())    # B+
print(n1.get_blood())    # B+

n1.set_blood("P+")       # Invalid Blood group