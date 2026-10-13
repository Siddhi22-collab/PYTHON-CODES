try:
    a=10
    b=int(input("Enter a number: "))
    c=a/b
except ValueError:
    print("Please enter a valid integer.")
except ZeroDivisionError:
    print("Please enter a non-zero number.")
finally:
    print("Execution completed.")
    