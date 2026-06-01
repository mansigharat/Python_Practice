n = int(input("Enter your number "))
sum = 0
for i in range(1,n):
    if n % i == 0:
        sum = sum +i
if sum == n:
    print("It is a Perfect number")
else:
    print("It is not a Perfect number") 