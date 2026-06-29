####### 1st code  



def decorator(func):
    def wrapper():
        print("1. Mansi Gharat  98/100")
        func()
        print("3. Shreyash Bhuikot  96/100")
    return wrapper


@decorator
def IAranks():
    print("2. Atharva Thorve  97/100")

IAranks()




####### 2nd code  


# def decorate(func):
#     def wrapper(a,m):
#         print("The addition of a & m:")
#         func(a,m)
#         print("The execution is complete, hope you got the correct asnswer.")
#     return wrapper

# @decorate
# def addition(a,m):
#     print("The answer is",a+m)

# addition(19,7)


def addition(*args):
    sum = 0
    for i in args:
        sum = sum + i
    print(sum)
addition(19,7,9,11,18, 5, 6,9, 14, 15,63,27,45,1,7)

def addition(**kwargs):
    print("Presonal Data \n")
    for i in kwargs:
        print(f"{i} : {kwargs[i]}")
addition(Name = "Atharva", Age = 20 , Designation = "Agentic AI engineer")