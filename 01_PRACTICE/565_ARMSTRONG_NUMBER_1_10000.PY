for n in range(1, 10001):
    temp = n
    digits = len(str(n))
    total = 0

    for i in range(digits):
        digit = temp % 10
        total += digit ** digits
        temp //= 10

    if total == n:
        print(n)