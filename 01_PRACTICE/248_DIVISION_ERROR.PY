# Program to perform division with exception handling

try:
    # Accept input from user
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))

    # Perform division
    result = numerator / denominator
    print("Result of division:", result)

except ZeroDivisionError:
    print(" Error: Cannot divide by zero.")

except ValueError:
    print(" Error: Please enter valid numbers.")

else:
    print(" Division performed successfully.")

finally:
    print("🔹 Operation completed.")
