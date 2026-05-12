string = input("Enter a string: ")
count = 0
for char in string:
    if char in 'aeiouAEIOU':
        count += 1

print("The number of vowels in the string are:",count)
