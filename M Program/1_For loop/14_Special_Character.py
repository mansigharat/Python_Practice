a = "Python@123%" 

char = 0
dig = 0
spchr = 0

for i in a:
    if i.isdigit():
        dig += 1
    elif i.isalpha():
        char += 1
    else:
        spchr += 1
print(f" Your digits are {dig} \n Your alphabates are {char} \n Your Special characters are {spchr}")