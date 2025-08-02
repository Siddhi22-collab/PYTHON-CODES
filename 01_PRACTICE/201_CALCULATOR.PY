class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Calculator(self.value + other.value)

    def __sub__(self, other):
        return Calculator(self.value - other.value)

    def __str__(self):
        return f"Value: {self.value}"

c1 = Calculator(10)
c2 = Calculator(20)
c3 = c1 + c2
print(c3)  
