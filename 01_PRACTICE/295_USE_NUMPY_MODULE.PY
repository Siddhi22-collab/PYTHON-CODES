
import numpy as np
arr=np.array([1, 2, 3, 4, 5])

# 1. Type or Array
print("Type of arr:", type(arr))

# 2. Axes of Array
print("Number of dimensions (axes) of arr:", arr.ndim)

# 3. Shape of Array
print("Shape of arr:", arr.shape)

# 4. Type of elements in Array
print("Data type of elements in arr:", arr.dtype)

# 5. Size of Array
print("Size of arr:", arr.size)

# 6. Item Size
print("Item size of each element in arr (in bytes):", arr.itemsize)

# 7. Total Bytes
print("Total bytes consumed by arr:", arr.nbytes)

# 8. Sum and Mean
print("Sum of all elements in arr:", np.sum(arr))
print("Mean of all elements in arr:", np.mean(arr))

