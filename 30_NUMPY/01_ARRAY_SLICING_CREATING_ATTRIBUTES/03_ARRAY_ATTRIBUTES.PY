import numpy as np
# Create a 1D array with 5 elements
arr= np.array([1, 2, 3, 4, 5])
print(np.size(arr))  # Output: 5
print(np.ndim(arr))  # Output: 1    
print(np.shape(arr))  # Output: (5,)
print(np.dtype(arr))  # Output: int64 (or int32 depending on the system