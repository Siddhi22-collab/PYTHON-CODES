def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def primes_in_diagonals(matrix):
    n = len(matrix)
    prime_diagonals = []

    for i in range(n):
        # Main diagonal element
        if is_prime(matrix[i][i]):
            prime_diagonals.append(matrix[i][i])

        # Anti-diagonal element (skip if it is the same as main diagonal in odd-sized matrix)
        if i != n - 1 - i and is_prime(matrix[i][n - 1 - i]):
            prime_diagonals.append(matrix[i][n - 1 - i])

    return prime_diagonals

# Example matrix
matrix = [
    [2, 3, 5],
    [7, 11, 13],
    [17, 19, 23]
]

# Find and print prime numbers on diagonals
result = primes_in_diagonals(matrix)
print("Prime numbers on diagonals:", result)
