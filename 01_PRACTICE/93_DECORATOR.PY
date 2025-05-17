import time

# Decorator function
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Start time
        result = func(*args, **kwargs)
        end_time = time.time()    # End time
        print(f"Execution time for '{func.__name__}': {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# Example function to demonstrate
@measure_time
def slow_function():
    print("Starting slow function...")
    time.sleep(2)  # Simulate a time-consuming process
    print("Finished slow function.")

# Another example with arguments
@measure_time
def sum_of_squares(n):
    return s
