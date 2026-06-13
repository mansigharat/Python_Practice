#Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

#Union
union_set = A.union(B)
print(f"Union: {union_set}")

#Intersection
intersection_set = A.intersection(B)
print(f"Intersection: {intersection_set}")

#Difference
difference_set = A.difference(B)
print(f"Difference: {difference_set}")

#Symmetric Difference
symmetric_diff_set = A.symmetric_difference(B)
print(f"Symmetric Difference: {symmetric_diff_set}")