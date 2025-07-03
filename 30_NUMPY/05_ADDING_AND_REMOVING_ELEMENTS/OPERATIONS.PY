import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.append(a,[[10,11,12]],axis=0))
print(np.insert(a,1,[[10,11,12]],axis=0))
print(np.delete(a,1,axis=0))
print(np.append(a,[[10],[11],[12]],axis=1))