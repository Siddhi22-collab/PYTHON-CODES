import numpy as np
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
# Combine arrays using np.concatenate
print(np.concatenate((arr1, arr2)))
# Combine arrays using np.vstack
print(np.vstack((arr1, arr2)))
# Combine arrays using np.hstack
print(np.hstack((arr1, arr2)))
