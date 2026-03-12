
students = {
    "Siddhi": {"age": 22, "course": "MCA"},
    "Gargie": {"age": 23, "course": "BCA"},
    "Anita": {"age": 21, "course": "BSc"}
}

for name, info in students.items():
    print("Name:", name)
    for key, value in info.items():
        print(key, ":", value)
    print()