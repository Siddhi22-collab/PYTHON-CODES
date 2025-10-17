import pandas as pd

# Sample data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'Age': [25, None, 30, 22, None],
    'City': ['NY', 'LA', None, 'SF', 'NY']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)


df['Age'].fillna(df['Age'].mean(), inplace=True)  
df['Name'].fillna('Unknown', inplace=True)        
df['City'].fillna('Unknown', inplace=True)        

print("\nCleaned Data:\n", df)
