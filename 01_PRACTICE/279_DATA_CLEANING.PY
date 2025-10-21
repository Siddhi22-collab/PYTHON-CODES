import pandas as pd
import numpy as np

# 16. Handle missing values
data = {'A':[1, 2, np.nan, 4],
        'B':[np.nan, 2, 3, 4]}
df = pd.DataFrame(data)
df['A'].fillna(df['A'].mean(), inplace=True)
df.dropna(inplace=True)
print(df)
