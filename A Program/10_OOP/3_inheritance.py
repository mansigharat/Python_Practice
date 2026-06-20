# Inheritance = A child class reuses code from a parent class.

class Vanilla:
    money = 19090711
    def hello(self):
        print("Hello, I am Vanilla and Choclate has full access to all my assets.")


class Chocolate(Vanilla):
    print("Hello, I am chocolate and I am given full access to the money of Vanilla.")

obj = Vanilla()

obj2 = Chocolate()

obj2.hello()