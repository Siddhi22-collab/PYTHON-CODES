names = ["Amit", "Neha", "Rahul", "Priya"]
marks = [75, 32, 85, 28]

for name, mark in zip(names, marks):
    if mark >= 35:
        print(name, "Pass")
    else:
        print(name, "Fail")