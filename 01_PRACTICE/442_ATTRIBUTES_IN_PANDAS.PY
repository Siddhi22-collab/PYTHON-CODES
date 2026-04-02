import pandas as pd 

data={
    'Name':['Siddhi','Gargie','Sanket','Varun'],
    'Age':[22,24,21,22],
    'City':['Nagpur','Mumbai','Pune','Nagpur']
}

df=pd.DataFrame(data)
print(df)


print("------DATAFRAME-------")
print("shape:",df.shape)
print("dimensions:",df.ndim)
print("size:",df.size)
print("columns:",df.columns)
print("index:",df.index)
print("Transpose:",df.T)
print("DataTypes:",df.dtypes)
print("Values:",df.values)
print("Is Empty:",df.empty)