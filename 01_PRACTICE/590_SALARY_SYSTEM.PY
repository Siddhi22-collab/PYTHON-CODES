class Employee:
    def __init__(self, employee_id, basic_salary):
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        return self.basic_salary


class PermanentEmployee(Employee):
    def calculate_salary(self):
        bonus = self.basic_salary * 0.20
        return self.basic_salary + bonus


class ContractEmployee(Employee):
    def calculate_salary(self):
        deduction = self.basic_salary * 0.10
        return self.basic_salary - deduction


employees = [
    PermanentEmployee(101, 50000),
    ContractEmployee(102, 40000)
]

for employee in employees:
    print(employee.employee_id, employee.calculate_salary())