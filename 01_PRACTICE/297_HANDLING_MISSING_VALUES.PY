import pandas as pd
import numpy as np

# Sample dataset
data = {
    'Name': ['Siddhi', 'Pratik', 'Riya', 'Aarav', None],
    'Age': [22, np.nan, 24, 25, 23],
    'City': ['Nagpur', 'Pune', np.nan, 'Mumbai', 'Delhi']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['City'].fillna('Unknown', inplace=True)
df['Name'].fillna('No Name', inplace=True)

print("\nAfter Filling Missing Values:\n", df)
