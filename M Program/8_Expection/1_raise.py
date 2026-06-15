# raise is a manual way to throw an exception. 
# It can be used to trigger an exception when a certain condition is met.

age = int(input("Enter your age:"))

try:
    if age<18 or age>25:
        raise ValueError("Age must be between 18 and 25.")

    else:
        print("Age is valid, welcome to the college!")

except ValueError as err:
    print(f"You are not eligible, {err}")


print("Congratulations, if you are eligible. The college would start soon. Please wait for the notice.")