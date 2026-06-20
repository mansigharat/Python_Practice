class Student:

    def __init__(self, name, score, city):
        self.name = name
        self.__score = score
        self.__city = city

    def score(self):
        return self.__score

    def eligibility(self, score):
        score = int(score)
        if 82 <= score <= 100:
            self.__score = score
            print("Eligible")
        else:
            print("Not eligible")

    def city(self):
        return self.__city

    def tell_city(self, city):
        valid = ["Uran", "Alibaug", "New Panvel", "Panvel", "Karjat", "Khopoli", "Rasayani"]
        invalid = ["Pen"]
        if city in valid:
            self.__city = city
            print("You dont need to apply for Hostel")
        elif city in invalid:
            print("You dont deserve to get admission.")
        else:
            print("You live far, better you opt for Hostel!")


application1 = Student("Saloni", 92, "Panvel")
application2 = Student("Yash", 27, "Pen")

print("Score of student is:", application2.score())
print("City of student is:", application2.city())


print("Score of student is:", application1.score())
print("City of student is:", application1.city())

application1.tell_city("Rasayani")