

def factorial(n):
    if n < 0:
        return None  # Factorial not defined for negative numbers
    return 1 if n in (0, 1) else n * factorial(n - 1)

try:
    num = int(input("Enter a non-negative integer: "))
    result = factorial(num)
    if result is None:
        print("Factorial is not defined for negative numbers.")
    else:
        print(f"Factorial of {num} is {result}")
except ValueError:
    print("Invalid input! Please enter an integer.")
