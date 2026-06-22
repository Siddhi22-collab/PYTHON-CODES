from sklearn.linear_model 
import LinearRegression 
import numpy as np 
X = np.array([[1], [2], [3], [4], [5]]) 
y = np.array([1, 3, 2, 3, 5])
model = LinearRegression() 
model.fit(X, y) 
print(model.predict([[6]])) 