import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

a = arr[0:3:2, 0:3:2]
print(a)

flat = a.flatten()
print(flat)