import pandas as pd

# Load CSV file
data = pd.read_csv('data.csv')

# Display first 5 rows
print(data.head())

# Basic info
print(data.info())

# Summary statistics
print(data.describe())
