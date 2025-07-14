class Employee:
    def __init__(self, name, salary):
        self.name = name         
        self.__salary = salary  
    def get_salary(self):
        return self.__salary
    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Invalid salary amount!")
emp = Employee("Alice", 50000)

print(emp.name)  
print(emp.get_salary())  

emp.set_salary(60000)
print(emp.get_salary()) 