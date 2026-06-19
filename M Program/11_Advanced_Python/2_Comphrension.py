l = [i for i in range(1,21) if i%2==0]  #list comphrehension
print(l)

d = {i : i**2 for i in range(1,11)}     # dictionary comphrehension 
print(d)

s = {x*x for x in range(10) if x%2 ==0} # set comphrehension
print(s)

l = [i*i for i in range(1,21) if i%2 !=0]
print(l)

l = ["agent", "model", "task", "memory", "tool"]
d = {i:len(i) for i in l }
print(d)

s = {x for x in range(1,30) if x%3 ==0 or x%5==0} 
print(s)