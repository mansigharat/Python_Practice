a= input("Enter the first list of numbers (comma separated): ").split(',')
b= input("Enter the second list of numbers (comma separated): ").split(',')

result=(set(a)^set(b))

print(result)
# print("Only in list 1:", only_in_list_1)
# print("Only in list 2:", only_in_list_2)