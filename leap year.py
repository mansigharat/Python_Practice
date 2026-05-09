import random
r = random.randint(1900,2100) 

while True:
    inp = int(input("Mention a year between 1900 and 2100: "))
    if inp % 400 == 0:
        print("The year", inp, "is a leap year!")
        break
    elif inp % 100 == 0:
        print("The year", inp, "is not a leap year!")
    elif inp % 4 == 0:
        print("The year", inp, "is a leap year!")
        break
    else:
        print("The year", inp, "is not a leap year!")