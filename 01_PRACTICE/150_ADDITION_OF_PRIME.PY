def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
n = int(input("Enter a number: "))
prime_sum = 0
for i in range(2, n + 1):
    if is_prime(i):
        prime_sum += i

print("Sum of prime numbers up to", n, "is:", prime_sum)
