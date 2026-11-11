class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
        else:
            print("Invalid Salary")


e1 = Employee("Rahul", 30000)

print("Salary:", e1.get_salary())

e1.set_salary(45000)

print("Updated Salary:", e1.get_salary())