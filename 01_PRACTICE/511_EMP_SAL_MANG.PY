class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def increment(self, percent):
        self.salary += self.salary * percent / 100

    def annual_salary(self):
        return self.salary * 12

    def display(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Salary      :", self.salary)
        print("Annual Salary:", self.annual_salary())

emp = Employee(101, "Siddhi", 50000)

emp.increment(10)

emp.display()