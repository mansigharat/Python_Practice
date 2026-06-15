A = {1,2,3,4}
B = {4,5,6,2}

s = union_set = A.union(B) # A|B
print(s)

s = intersection_set = A.intersection(B) #A & B
print(s)

s = difference_set = A.difference(B) # A - B
print(s)

s = symmetric_diff = A.symmetric_difference(B)  # A ^ B
print(s)