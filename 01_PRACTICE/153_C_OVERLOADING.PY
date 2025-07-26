class Student:
    def __init__(self, name="Unknown", grade=None):
        self.name = name
        self.grade = grade

    def info(self):
        return f"{self.name} - {self.grade}"

s1 = Student()
s2 = Student("Siddhi", "A")
print(s1.info())
print(s2.info())
