a = int(input("Please enter a number to check if it is odd or even: "))

b = (a%2)

if (b==0):
    print(a,"is an Even Number")
else:
    print(a,"ia an Odd Number")


# Or also we can write the above code as:

# a = int(input("Please enter a number to check if it is odd or even: "))

# b = (a%2)

# if (b==0):
#     print(a,"is an Even Number")    
# elif (b==1):
#     print(a, "is an Odd Number")

# i have another approach

num = int(input("Enter a number : "))
if(num%2==0):
    print("Number is even")
else:
    print("Number is odd")

# for multiline comment just select it code and use ctrl + /