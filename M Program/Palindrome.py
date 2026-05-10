# Palindrome means if reverse of string and original string have same output ,
# madam if we reverse it still madam so it is palindrome
# Atharva if we reverse it , become avrahtA
String = input("Enter a string : ")
new_rev = String[::-1]
if String == new_rev:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
