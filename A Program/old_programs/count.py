def count_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    result = ", ".join(f"{char}: {count}" for char, count in counts.items())
    print(result)

count_characters(input("Enter a string: "))