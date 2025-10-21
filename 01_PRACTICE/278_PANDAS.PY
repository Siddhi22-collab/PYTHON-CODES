import pandas as pd

# 7. Create and display a DataFrame
data = {'Name': ['Amit', 'Riya', 'Karan'],
        'Age': [22, 25, 20],
        'Marks': [85, 90, 75]}
df = pd.DataFrame(data)
print(df)

# 8. Filter rows where marks > 80
print(df[df['Marks'] > 80])

# 9. Add a new column "Result"
df['Result'] = df['Marks'].apply(lambda x: 'Pass' if x >= 40 else 'Fail')
print(df)
