matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = [[row[c] for row in matrix] for c in range(3)]
print(result)