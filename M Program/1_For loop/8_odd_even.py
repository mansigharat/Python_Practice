n = int(input("enter a number : "))
even = 0
odd = 0
for i in range(1,n+1):
    if i % 2 ==0:
        even = even + i
    else:
        odd = odd + i
print(f"your even and odd are {even} , {odd}")

