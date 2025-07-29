def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

matrix = [
    [2, 3, 4],
    [5, 11, 6],
    [7, 8, 13]
]

size = len(matrix)
print("Prime numbers in diagonals:")

for i in range(size):
    # Primary diagonal
    if is_prime(matrix[i][i]):
        print(matrix[i][i])
    # Secondary diagonal
    if i != size - 1 - i and is_prime(matrix[i][size - 1 - i]):
        print(matrix[i][size - 1 - i])
