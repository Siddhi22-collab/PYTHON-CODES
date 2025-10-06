import pandas as pd

data = {'Age': [21, 22, 23, 24, 25, 100, 27, 28, 29]}
df = pd.DataFrame(data)

Q1 = df['Age'].quantile(0.25)
Q3 = df['Age'].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[(df['Age'] < lower) | (df['Age'] > upper)]
print("Outliers:\n", outliers)
