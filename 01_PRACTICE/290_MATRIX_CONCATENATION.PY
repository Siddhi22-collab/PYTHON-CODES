import pandas as pd
data1={
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','David'],
}
df1=pd.DataFrame(data1)
data2={
    'ID':[3,4,5,6],
    'Name':['Charlie','David','Eve','Frank'],

}
df2=pd.DataFrame(data2)
concatenated_df=pd.concat([df1,df2],ignore_index=True)
print("Concatenated DataFrame:")
print(concatenated_df)