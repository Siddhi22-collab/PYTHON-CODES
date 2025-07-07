import pandas as pd
dict = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],           
    'Subject': ['Math', 'Science', 'Math', 'Science'],
    'Score': [85, 90, 78, 88],  
    'Year': [2021, 2021, 2022, 2022]}
df = pd.DataFrame(dict)
# Pivoting the DataFrame
pivoted_df = df.pivot(index='Name', columns='Subject', values='Score')
# Displaying the pivoted DataFrame  
print(pivoted_df)
