# Objects
class Factory:
    a = 143 #attribute
    
    def __init__(self):
        print("Chocolate Likes Vanilla.")

    def hello(self):  #method
        print("They are the best Combination ;)")
    
    print("I am getting initialized, this is very exciting.")    

obj = Factory()

obj.hello()

print(obj.a) 