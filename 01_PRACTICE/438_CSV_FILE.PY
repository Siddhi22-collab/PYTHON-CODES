import pandas as pd
import numpy as np
data=pd.DataFrame({
    'Name':pd.Series(['Siddhi','Gargie','Sanket','Varun']),
    'Age':pd.Series([22,24,21,22]),
    'City':pd.Series(['Nagpur','Mumbai','Pune','Nagpur'])
})
df=pd.DataFrame(data)
#df=pd.DataFrame(data,index=['s1','s2','s3','s4'])
print(df)
df.to_csv("Student_data.csv",index=False)