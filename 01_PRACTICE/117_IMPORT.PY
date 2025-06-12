import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, np.nan, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'New York', None, 'Chicago'],
    'Salary': ['50k', 'NaN', '40k', '60k', '55k']
}
df = pd.DataFrame(data)
print("Original Data:\n", df)import pandas as pd
import numpy as np

# Sample DataFrame
data = {
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Age': [25, np.nan, 22, 32, 29],
    'City': ['New York', 'Los Angeles', 'New York', None, 'Chicago'],
    'Salary': ['50k', 'NaN', '40k', '60k', '55k']
}
df = pd.DataFrame(data)
print("Original Data:\n", df)
