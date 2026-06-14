l1=[1,2,3,4,5]
l2=[4,5,6,7,8]

common=set(l1) & set(l2)
only_in_set1=set(l1) - set(l2)

print("Common elements:", common)
print("Elements only in set 1:", only_in_set1)  