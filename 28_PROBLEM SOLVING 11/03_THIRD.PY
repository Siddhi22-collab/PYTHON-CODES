# WRITE A PYTHON FUNCTION THAT TAKE A NUMBER AS A PARAMETER AND CHECK IF IT IS PRIME OR NOT
def is_prime(n):
    """Checks if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Example usage
print(is_prime(29))  # Should return True, as 29 is a prime number