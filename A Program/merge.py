print("Enter the first list of numbers (comma separated):")
l1 = list(map(int, input().split(',')))
print("Enter the second list of numbers (comma separated):")
l2 = list(map(int, input().split(',')))
def merged_sorted(l1,l2):
    result=[]
    i=j=0

    while i<len(l1) and j <len(l2):
       if l1[i]<= l2[j]:
        result.append(l1[i])
        i+=1
       else:
        result.append(l2[j])
        j+=1
    result.extend(l1[i:])
    result.extend(l2[j:])
    return result

print(merged_sorted(l1,l2))
