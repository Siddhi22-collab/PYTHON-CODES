import pandas as pd
data=pd.read_csv('data.csv')
data.drop_duplicates(inplace=True)