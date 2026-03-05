students = [
    ("Siddhi", 85),
    ("Rahul", 90),
    ("Amit", 78)
]

# Sort by marks
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)