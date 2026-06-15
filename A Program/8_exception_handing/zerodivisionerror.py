a = int(input("Give me a number:"))

try:
    print(10/a)

except ZeroDivisionError:
    print("You can't divide by zero!")

print("The operation has been completed.")