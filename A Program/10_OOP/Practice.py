class admission:

    def __init__(self,name,cet_score):
        self.name = name
        self.cet_score = cet_score

    @classmethod
    def pillai(cls,name,cet_score) :
        return cls(name,cet_score)

candidate1 = admission("Atharva", "93")          # normal way
candidate2 = admission.pillai("Sahil","95") # admin way


print("The name of candidate is:",candidate2.name)   # Sahil

print("The CET Score of candidate is:",candidate2.cet_score)  # 95