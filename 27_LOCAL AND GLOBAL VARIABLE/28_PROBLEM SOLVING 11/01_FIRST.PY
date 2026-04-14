# WRITE A FUNCION TO FIND MAXIMUM OF THREE NUMBERS
def find_maximum(a, b, c):
    """Returns the maximum of three numbers."""
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
find_maximum(10, 20, 30)  # Example usage