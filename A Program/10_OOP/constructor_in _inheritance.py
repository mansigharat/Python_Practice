class Human:
    def __init__(self,behaviour):
        self.behaviour = behaviour

    def show(self):
        print(f"Humans are very {self.behaviour}.")


class Animal(Human):
    pass

sentence1 = Human("Selfish")
sentence2 = Animal("Loyal")

sentence1.show()