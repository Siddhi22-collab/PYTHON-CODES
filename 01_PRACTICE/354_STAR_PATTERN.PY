def print_right_triangle(rows):
    """Prints a right-angled triangle star pattern."""
    if rows <= 0:
        print("Number of rows must be a positive integer.")
        return
    
    for i in range(1, rows + 1):
        print("*" * i)  # Print i stars in each row


def main():
    try:
        # Take user input
        rows = int(input("Enter the number of rows for the triangle: "))
        print_right_triangle(rows)
    except ValueError:
        print("Invalid input. Please enter an integer.")


if __name__ == "__main__":
    main()