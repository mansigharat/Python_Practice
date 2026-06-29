# lambda functions

addition = lambda a, b : a + b

print(addition(19,7))

square = lambda m : m*m

print(square(9))

cube = lambda m : m*m*m 

print(cube(5))

number = lambda a : "EVEN" if a%2 == 0 else "ODD"

print(number(19))

age = lambda a,m : f"{a} is older than {m}" if a>m  else f"{m} is older than {a}"

print(age(19,20))

Sentence = input("Chocolate and Vanilla are the best combination.")
line = lambda string : string.line()

print(line(Sentence))