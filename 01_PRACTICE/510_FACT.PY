def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n in (0, 1) else n * factorial(n - 1)

try:
    num = int(input("Enter a non-negative integer: "))
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError as e:
    print(f"Error: {e}")