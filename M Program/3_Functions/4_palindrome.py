def palin(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev + str[i]

    if rev == str:
        print("It is palindrome")
    else:
        print("It is not palindrome")
    
palin("Manasi")
palin("NAMAN")