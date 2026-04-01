import pandas as pd
df1=pd.DataFrame({'ID':[1,2,3],'Name':['a','b','c']}) 
df2=pd.DataFrame({'ID':[1,2,6],'City':['Nagpur','Pune','Mumbai']})
#result=pd.merge(df1,df2,on='ID',how='inner')
#result=pd.merge(df1,df2,on='ID',how='outer')
#result=pd.merge(df1,df2,on='ID',how='left')/
result=pd.merge(df1,df2,on='ID',how='right')
print(result)