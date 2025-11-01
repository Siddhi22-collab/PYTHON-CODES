def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Rotated Matrix:")
for row in rotate_matrix(mat):
    print(row)

