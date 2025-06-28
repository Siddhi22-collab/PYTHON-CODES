class Employee:
    def display_role(self):
        print("General Employee")

class Manager(Employee):
    def display_role(self):
        print("Manager manages teams.")

class Developer(Employee):
    def display_role(self):
        print("Developer writes code.")

class Intern(Employee):
    def display_role(self):
        print("Intern learns and assists.")

# Create objects
m = Manager()
d = Developer()
i = Intern()

m.display_role()
d.display_role()
i.display_role()
