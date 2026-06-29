# comprehensions

squares = [x**2 for x in range(10)]
print(squares)

l = [i for i in range(1,21) if i%2==0] 
print(l)

s = {x*x for x in range(10) if x%2 ==0}
print(s)

d = {i : i**2 for i in range(1,11)}
print(d)

l = [i*i for i in range(1,21) if i%2 !=0]
print(l)

l = ["agent", "model", "task", "memory", "tool"]
d = {i:len(i) for i in l }
print(d)

s = {x for x in range(1,30) if x%3 ==0 or x%5==0} 
print(s)

m = [i for i in range(1,19) if i%2==0]
print (m)