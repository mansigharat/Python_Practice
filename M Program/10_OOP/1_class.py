#Variables - defined inside the class are Attribute
#Methods - functions defined inside a class are Methods

class Factory:
    a = 12 #attribute

    def hello(self):
        print("How are you ?")
    
    print("hello how are you i'm geeting initialized")

obj = Factory()
print(obj.a)

print(Factory().a)
Factory().hello()