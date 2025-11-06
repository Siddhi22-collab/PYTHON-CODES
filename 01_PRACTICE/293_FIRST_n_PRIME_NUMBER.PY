import math
def is_prime_wilson(n):
    if n<=1:
        return False
    factorial=math.factorial(n-1)
    result=(factorial+1)%n
    return result==0

n=int(input("Enter a Number to check is it's prime using Wilson's Theorem:"))
if is_prime_wilson(n):
    print(f"{n} is a prime number (Confirmed by Wilson's Theorem).")
else:
    
    print(f"{n} is not a prime number (Confirmed by Wilson's Theorem).")
