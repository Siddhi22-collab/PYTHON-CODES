import pandas as pd
import numpy as np

df = pd.DataFrame({
    'category': ['A', 'A', 'B', 'B', 'C', 'C'],
    'values': [100, 200, 300, 400, 500, 600],
    'costs': [10, 20, 30, 40, 50, 60]
})

# Custom aggregation function
result = df.groupby('category').agg({
    'values': ['sum', 'mean'],
    'costs': lambda x: np.std(x, ddof=1)
})

print(result)
