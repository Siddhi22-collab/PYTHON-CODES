class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name:", self.name)
        print("Student Marks:", self.marks)

    def check_result(self):
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")


s1 = Student("Rahul", 85)

s1.display()
s1.check_result()