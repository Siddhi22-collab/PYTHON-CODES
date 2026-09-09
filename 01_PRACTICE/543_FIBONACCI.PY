def fibonacci(n_terms):
n1, n2 = 0, 1
for _ in range(n_terms):
print(n1, end=" ")
n1, n2 = n2, n1 + n2

fibonacci(10)