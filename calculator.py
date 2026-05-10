int1 =float(input("Enter the 1st number:"))
op = input("Enter the Operator:")
int2 =float(input("Enter the 2nd Number:"))

if (op=="+"):
    print('The Addition of the Numbers is:',(int1+int2))
elif (op=="-"):
    print('The Subtraction of the Numbers is:',(int1-int2))
elif (op=="*"):
    print('The Multiplication of the Number is:',(int1*int2))
elif (op=="/"):
    print('The Division of the Numbers is:',(int1/int2))
else:
    print("Invalid operator!!!")