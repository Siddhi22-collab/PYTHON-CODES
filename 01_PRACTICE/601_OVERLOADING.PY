
class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print(self.emp_id, self.name, self.salary)


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.30


class Tester(Employee):
    def calculate_salary(self):
        return self.salary + self.salary * 0.15


d = Developer(101, "Amit", 50000)
t = Tester(102, "Neha", 40000)

d.display()
print("Developer Salary:", d.calculate_salary())

t.display()
print("Tester Salary:", t.calculate_salary())
