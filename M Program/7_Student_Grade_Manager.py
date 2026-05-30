students = {
    "Rahul": [85, 90, 88, 92, 87],
    "Priya": [95, 96, 92, 93, 94],
    "Amit": [50, 55, 60, 58, 65]
}

topper = ""
highest_avg = 0

print("Name\t | Average | Grade")
print("-" * 30)

for name, marks in students.items():

    total = sum(marks)
    avg = total / len(marks)

    if avg >= 90:
        grade = "A"

    elif avg >= 75:
        grade = "B"

    elif avg >= 60:
        grade = "C"

    else:
        grade = "D"

    if avg > highest_avg:
        highest_avg = avg
        topper = name

    print(name, "\t |", round(avg, 1), "\t |", grade)

print("\nTopper is:", topper, "with average", round(highest_avg, 1))