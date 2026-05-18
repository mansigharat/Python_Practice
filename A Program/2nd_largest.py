num = [2,6,4,9,7,1,3,5,8]
def second_largest(lst):
    first=second=float('-inf')
    for num in lst:
        if num > first:
            second = first
            first = num
        elif num> second and num != first:
            second = num
    return second

print(second_largest(num))