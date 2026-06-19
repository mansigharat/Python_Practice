addition = lambda a : "even" if a%2 == 0 else "odd"
print(addition(5))

cube = lambda a : a*a*a 
print(cube(3))

string = input("enter the string : ")
upper = lambda string : string.upper()
print(upper(string))

large = lambda a,b : f"{a} is Large" if a>b  else f"{b} is large"
print(large(5,7))
