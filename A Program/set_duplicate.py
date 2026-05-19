arr = input("Enter the list of numbers (comma separated): ").split(',')
arr = [x.strip() for x in arr if x.strip()]

def remove_duplicates(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            result.append(x)
            seen.add(x)
    return result

print(remove_duplicates(arr))