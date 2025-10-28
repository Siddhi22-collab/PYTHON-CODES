# ml_model.py
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

# Train and save model
iris = load_iris()
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
