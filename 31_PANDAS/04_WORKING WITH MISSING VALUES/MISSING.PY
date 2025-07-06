import pandas as pd
df=pd.read_csv(r"C:\Users\siddh\Downloads\placement (1).csv")
#df.isnull().sum()
print(df.head())
df.dropna(inplace=True)