a,b,c = map(int,input("Enter three number ").split(",")) # 2,3,4   3,4,2   4,3,2
if(a>b) and (b > c) :
        print("Largest number is " , b)
if(b > c) and (a>c):
        print("Largest number is ",a)
else: 
    print("Largest number is",c)   

