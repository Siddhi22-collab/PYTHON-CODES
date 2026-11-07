class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Amit", 85)
s2 = Student("Priya", 90)

s1.display()
s2.display()