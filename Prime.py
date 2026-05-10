"""
2 is a prime number, so we use condition: num == 2

Numbers less than or equal to 1 are not prime.

For other numbers, we check whether the number is divisible
by any number from 2 to num-1.

If divisible, then it is not prime.
Otherwise, it is prime.
"""

num = int(input('Enter a number :'))  # example: num = 13

if num <= 1:
    print("Number is not prime")  # negative numbers, 0 and 1 are not prime

elif num == 2:  # 2 is the only even prime number
    print("Number is prime")

else:
    for i in range(2, num):  # check numbers from 2 to 12
        if num % i == 0:  
            # if num is divisible by i, then number is not prime
            print("Number is not prime")
            break

    else:
        # loop completed without finding any divisor
        print("Number is prime")

# tu tuza nav lihu shaktos ka ,sarkha tuzya nava chya jagi tuza email id disat ahe graph madhe atharvathorve2@gmail.com , change it to atharva thorve only