import pandas as pd
data = pd.read_csv(r'C:\Users\siddh\Downloads\placement (1).csv')
print(data.head(10))
print(data.tail(10))
print(data.shape)
print(data.columns)
print(data.info())
print(data.describe())
print(data.isnull().sum())  
print(data.duplicated().sum())