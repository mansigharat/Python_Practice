a = "Python"
b = ""
for i in range(len(a)-1,-1,-1):
    b = b + a[i]
if a == b:
    print("String is Palindrome")
else:
    print("String is not Palindrome")