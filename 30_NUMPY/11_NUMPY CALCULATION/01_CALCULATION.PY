import numpy as np

# 1. Create arrays
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# 2. Basic arithmetic operations
add = a + b           # [6, 8, 10, 12]
sub = a - b           # [-4, -4, -4, -4]
mul = a * b           # [5, 12, 21, 32]
div = b / a           # [5.0, 3.0, 2.333..., 2.0]

# 3. Statistical operations
mean_a = np.mean(a)   # 2.5
std_a = np.std(a)     # Standard deviation
sum_a = np.sum(a)     # 10

# 4. Matrix operations
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])

dot_product = np.dot(mat1, mat2)  # Matrix multiplication

# Print results
print("Add:", add)
print("Subtract:", sub)
print("Multiply:", mul)
print("Divide:", div)
print("Mean of a:", mean_a)
print("Standard Deviation of a:", std_a)
print("Sum of a:", sum_a)
print("Matrix Multiplication:\n", dot_product)
