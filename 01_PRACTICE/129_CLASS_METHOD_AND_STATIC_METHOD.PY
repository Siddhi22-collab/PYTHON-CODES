class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

    @staticmethod
    def greet():
        return "Welcome to Python OOP"

print(Student.get_school_name())
print(Student.greet())
