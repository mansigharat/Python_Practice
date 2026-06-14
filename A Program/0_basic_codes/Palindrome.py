string = input("Enter a string: ")
reversed_string = string[::-1]

if string == reversed_string:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")