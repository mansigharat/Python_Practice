# *args = argument , **kwargs = keyword argument

# class Animal:

#     @property
#     def show(self):
#         print("Python Programming")

# obj = Animal()
# obj.show


# def decorate(func):
#     def wrapper():
#         print("I will print myself before function")
#         func()
#         print("I wil print after function")
#     return wrapper

# @decorate
# def hello():
#     print("hello")
# hello()

# def decorate(func):
#     def wrapper(a,b):
#         print("the addition is ")
#         func(a,b)
#         print("Thank you i hope you get right result")
#     return wrapper

# @decorate
# def add(a,b):
#     print("Total is ",a+b)

# add(2,5)


# def addition(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
# addition(12,23,45,56,56,67,84)

def addition(**kwargs):
    print(kwargs)
addition(name = "Mansi", age = 20 , designation)