class Student:
    def __init__(self, name, roll_number):
        self.__name = name                  # private attribute
        self.__roll_number = roll_number    # private attribute
        self.__grades = {}                  # private attribute (subject: grade)

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        if isinstance(name, str) and name.strip():
            self.__name = name
        else:
            print("Invalid name.")

    # Add or update grade
    def add_grade(self, subject, grade):
        if 0 <= grade <= 100:
            self.__grades[subject] = grade
        else:
            print("Grade must be between 0 and 100.")

    # Get grade for a specific subject
    def get_grade(self, subject):
        return self.__grades.get(subject, "No grade recorded")

    # Calculate average grade
    def calculate_average(self):
        if self.__grades:
            return sum(self.__grades.values()) / len(self.__grades)
        return 0.0

    # Display all grades
    def display_grades(self):
        print(f"Grades for {self.__name}:")
        for subject, grade in self.__grades.items():
            print(f"{subject}: {grade}")
        print(f"Average Grade: {self.calculate_average():.2f}")


# Example usage
student1 = Student("Siddhi Lokhande", "A101")

student1.add_grade("Math", 85)
student1.add_grade("Science", 90)
student1.add_grade("History", 78)

student1.display_grades()

# Access name using getter
print("Student Name:", student1.get_name())

# Attempt to directly access private variable (will fail)
try:
    print(student1.__grades)
except AttributeError as e:
    print("Access Denied:", e)

# Change name with setter
student1.set_name("S. Lokhande")
print("Updated Name:", student1.get_name())
