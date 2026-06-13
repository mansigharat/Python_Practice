#Merging two dictionaries

d1 = {10:100, 20:200, 30:300, 40:400, 50:500}
d2 = {40:440, 50:550, 60:600, 70:700, 80:800}

for i in d2:
    d1[i] = d2[i]

print(d1)