# empty = list()
# numbers = ['a', '2', 'c', '4', 'e']
# print (empty)
# print (type(empty))
# print (numbers)
# print (type(numbers))
# matrix = [['a', 'b', 'c'],
#          ['d', 'e', 'f']]
# print (matrix)
# print (type(matrix))
# numbers = list(range(5))
# print (numbers)
# list = ['a','b','c','d ']
# print(list[3])  
# matrix = [['a','b','c'],
#           ['d','e','f'],
#           ['g','h','i']]
# print (matrix)
# print (matrix[-1])
# print (matrix[-1][-2])
# print (matrix[0][0])
# print (matrix[2][0])
# nums = [[1,2],[3,[4,5]],[6]]
# flatten  
# print(flatten(nums))

numbers = [3,2,4,1,5,2,4,2,1,3,6,9,6,7,8]

def remove_duplicate(lst):
    seen ={}
    result = []

    for item in lst:
        if item not in seen:
            seen[item] = True
            result.append(item)

    return result

print(remove_duplicate(numbers))

numbers.sort()
print(remove_duplicate(numbers))