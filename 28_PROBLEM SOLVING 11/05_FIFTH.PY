# WRITE A PYTHON PROGRAM TO SOLVE THE FIBONACCI SERIES USING RECURSION
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
print(fibonacci(10))  # Should return 55, as the 10th Fibonacci number is 55     