from abc import ABC, abstractmethod

class SchoolSystem:

    def __init__(self,name,subject,grade,marks):
        self.marks = marks
        self.name = name
        self.subject = subject
        self.grade = grade
        self.__marks = __marks

    def get_marks(self):
        return self.grade
    
    def set_marks(self,grade):
        if self.marks < 0  and self.marks > 100:
            print("Invalid Marks")
        elif self.marks >= 80:
             self.grade = "A"
        elif self.marks >= 60:
            self.grade = "B"
        elif self.marks >= 40:
            self.grade = "C"
        else:
            self.grade = "F"
class Student(SchoolSystem):

    pass

