# WRITE A PYTHON FUNCTIN TO SUM ALL THE NUMBERS IN A LIST
def sum_of_list(numbers):
    """Returns the sum of all numbers in a list."""
    total = 0
    for number in numbers:
        total += number
    return total
sum_list = [1, 2, 3, 4, 5]  # Example usage