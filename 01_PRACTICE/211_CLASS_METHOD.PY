class Student:
    school_name = "ABC School"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @staticmethod
    def welcome_message():
        print("Welcome to MY school!")

student1 = Student("Nisarg")
Student.welcome_message()
Student.change_school("XYZ School")
print(student1.school_name)
