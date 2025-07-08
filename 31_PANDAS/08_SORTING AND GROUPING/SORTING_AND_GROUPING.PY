# Sort by column
df.sort_values('Age', ascending=False, inplace=True)

# Group by column
grouped = df.groupby('Age').mean()

# Count per group
print(df.groupby('Age')['Name'].count())
