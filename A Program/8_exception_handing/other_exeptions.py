#other type of exceptions. There are many other types of exceptions in Python.

a = input("Give me a number:")

try:
    print(10/int(a))

except Exception as err:
    print(f"An error occurred: {err}")

else:
    print("The code is correct and has no exceptions.")

finally:
    print("I would run no matter what, even if there is an exception or not.")

print("The operation has been completed.")