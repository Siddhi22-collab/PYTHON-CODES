import time
from functools import wraps

def timing_decorator(enabled=True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if enabled:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                print(f"{func.__name__} took {end - start:.4f} seconds")
                return result
            return func(*args, **kwargs)
        return wrapper
    return decorator

@timing_decorator(enabled=True)
def slow_function():
    time.sleep(2)
    return "Done"

print(slow_function())