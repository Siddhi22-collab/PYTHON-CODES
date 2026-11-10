
class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return Complex(
            self.real + other.real,
            self.imaginary + other.imaginary
        )

    def display(self):
        print(f"{self.real} + {self.imaginary}i")


c1 = Complex(10, 5)
c2 = Complex(20, 8)

c3 = c1 + c2
c3.display()
