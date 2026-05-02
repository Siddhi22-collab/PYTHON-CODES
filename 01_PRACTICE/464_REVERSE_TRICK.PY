matrix = [
    [1,2,3],
    [4,5,6]
]
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            matrix[i][j] = 0