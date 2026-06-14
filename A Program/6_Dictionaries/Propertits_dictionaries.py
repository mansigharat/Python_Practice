#Dictionary

d = {1:"K.L Rahul", 45:"Rohit Sharma", 18:"Virat Kohli", 96:"Shreyash Iyer", 63:"Suryakumar Yadav", 31:"Rajat Patidar"}

print(d[18])

d[1] = "KL Rahul"

print(d[1])

#Updating
d.update({15: "Bhuvneshwar Kumar"})

print(d)

#Adding new key value pair in the dictionary
d[99] = "Hardik Pandya"

for i in d:
    print(i, ":", d[i])