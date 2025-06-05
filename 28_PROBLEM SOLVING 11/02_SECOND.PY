# WRITE A PYTHON FUNCTION TO CREATE AND PRINT A LIST WHERE THE VALUES ARE SQUARE OF NUMBER BETWEEN 1 AND 30
def create_square_list():
    """Creates and prints a list of squares of numbers between 1 and 30."""
    square_list = [i ** 2 for i in range(1, 31)]
    print(square_list)
create_square_list()  # Example usage
