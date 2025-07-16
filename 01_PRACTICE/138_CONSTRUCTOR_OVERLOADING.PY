class Student:
    def __init__(self, name=None, age=None):
        self.name = name if name else "Unknown"
        self.age = age if age else 0

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Raj", 20)
s2 = Student()
s1.display()
s2.display()
